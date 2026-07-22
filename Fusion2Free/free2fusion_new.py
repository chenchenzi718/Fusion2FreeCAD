import time
import gc
import logging
import multiprocessing as mp
import tempfile
import shutil
import os

from tqdm import tqdm

import fusion2free
from utils.freeCheck import run_freecad_modeling
from utils.get_free_bbox import get_combined_bbox, setup_to_fusion
from utils.load_fusion import get_fusion_json, get_fusion_sequence, load_fusion
from utils.logging_db import LogDatabase

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("process.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def setup_directories(paths):
    """
    创建所需的目录。
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)


def handle_conversion(key, val, op_seq, output_py_path, log_path):
    """
    处理转换逻辑，返回结果用于数据库更新。
    """
    try:
        ret_str, Free_str, error_code = fusion2free.fusion2free(key, val)
        if op_seq[-1] == 'S':
            error_code = 'UNUSED SKETCH'
        if error_code:
            logger.info(f'data_id:{key}, convert error_code:{error_code}')

        # 准备返回数据
        update_data = {
            'is_convert': 1,
            'fusion_sequence': op_seq,
            'free_sequence': Free_str,
            'is_valid': 0,
            'error_code': error_code
        }

        # 创建子目录并写入文件 - 使用临时文件减少I/O阻塞
        sub_dir = os.path.join(output_py_path, key[:4])
        os.makedirs(sub_dir, exist_ok=True)

        # 使用临时文件写入然后移动，减少文件系统争用
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(ret_str)
            temp_path = temp_file.name

        target_path = os.path.join(sub_dir, f"{key}_free.py")
        shutil.move(temp_path, target_path)

        success = True

    except Exception as e:
        error_code = str(e)
        logger.error(f'data_id:{key}, convert error_code:{error_code}')
        update_data = {
            'is_convert': 0,
            'error_code': error_code
        }
        success = False

    # 显式触发垃圾回收
    gc.collect()

    return key, update_data, success


def handle_validation(key, output_py_path, log_path, output_free_path):
    """
    处理验证逻辑，返回结果用于数据库更新。
    """
    try:
        # 假设这是调用外部进程的函数
        run_freecad_modeling(key, output_py_path, log_path, output_free_path)
        update_data = {'is_valid': 1}
        success = True
    except Exception as e:
        error_code = str(e)
        logger.error(f'data_id:{key}, valid error_code:{error_code}')
        update_data = {'is_valid': 0, 'error_code': error_code}
        success = False

    # 强制垃圾回收
    gc.collect()

    return key, update_data, success


def handle_bbox(key, log_path, output_free_path, fusion_path):
    """
    处理验证逻辑，返回结果用于数据库更新。
    """
    try:
        free_path = os.path.join(output_free_path, key[:4], f"{key}_free.FCStd")
        bbox_tuple = get_combined_bbox(free_path)
        setup_to_fusion(bbox_tuple, fusion_path)
        update_data = {'is_valid': 1}
        success = True
    except Exception as e:
        error_code = str(e)
        logger.error(f'data_id:{key}, valid error_code:{error_code}')
        update_data = {'is_valid': 0, 'error_code': error_code}
        success = False

    # 强制垃圾回收
    gc.collect()

    return key, update_data, success


def process_single_file(path_data):
    """
    处理单个JSON文件，避免传递数据库连接。
    返回需要更新的数据库信息。
    """
    path, output_py_path, output_free_path, log_path = path_data

    key = path[-13:-5]
    result_data = {'key': key, 'updates': []}

    try:
        val = load_fusion(path)
    except Exception as e:
        error_msg = f"Error loading {path}: {e}"
        logger.error(error_msg)
        # 收集错误信息以更新数据库
        result_data['updates'].append({
            'key': key,
            'data': {
                'is_convert': 0,
                'fusion_sequence': '',
                'free_sequence': '',
                'is_valid': 0,
                'error_code': error_msg
            }
        })
        return result_data

    ki = int(key)
    if ki < 1063718 :
        return result_data

    # 初始化数据
    init_data = {
        'is_convert': 0,
        'fusion_sequence': '',
        'free_sequence': '',
        'is_valid': 0,
        'error_code': ''
    }
    result_data['updates'].append({'key': key, 'data': init_data})

    # 获取融合序列
    op_seq = get_fusion_sequence(val)
    fusion_seq_data = {'fusion_sequence': op_seq}
    result_data['updates'].append({'key': key, 'data': fusion_seq_data})

    logger.info(f"Now process: {key}")

    # 处理转换
    key, update_data, success = handle_conversion(key, val, op_seq, output_py_path, log_path)
    result_data['updates'].append({'key': key, 'data': update_data})

    # 仅在转换成功时处理验证
    if success:
        # 处理验证
        key, valid_data, valid_success = handle_validation(key, output_py_path, log_path, output_free_path)
        result_data['updates'].append({'key': key, 'data': valid_data})

        # 仅在验证成功时处理bbox
        if valid_success:
            key, bbox_data, _ = handle_bbox(key, log_path, output_free_path, path)
            result_data['updates'].append({'key': key, 'data': bbox_data})

    # 释放内存
    del val
    gc.collect()

    return result_data


def process_json_files():
    """
    主处理函数，负责整体流程的执行。
    """
    # 定义路径
    output_py_path = './data/cad_py_repair/'
    output_free_path = './data/cad_free_repair/'
    log_path = './logging/'
    db_path = os.path.join(log_path, 'log.db')
    fusion_prefix_path = './data/cad_json_repair/'

    # 创建目录
    setup_directories([output_py_path, output_free_path, log_path])

    # 获取JSON列表 - 改进：使用列表推导式和os.scandir更高效
    json_path_list = []
    for root, _, files in os.walk(fusion_prefix_path):
        json_path_list.extend([os.path.join(root, file) for file in files if file.endswith('.json')])

    # 初始化数据库
    db = LogDatabase(db_path)
    db.begin_transaction()

    try:
        # 准备任务数据 - 为每个文件添加必要的路径信息
        tasks = [(path, output_py_path, output_free_path, log_path) for path in json_path_list]

        # 按批次处理，避免一次加载太多内容
        batch_size = 50
        results_buffer = []  # 用于缓存数据库更新

        # 使用进程池并行处理
        num_processes = min(mp.cpu_count() - 1, 4)  # 留一个核心给操作系统

        with mp.Pool(processes=num_processes) as pool:
            # 使用imap处理任务，按批次获取结果
            for i, result in enumerate(tqdm(pool.imap(process_single_file, tasks, chunksize=5),
                                            total=len(tasks),
                                            desc="处理文件")):
                # 收集结果用于稍后批量更新数据库
                if result and 'updates' in result:
                    results_buffer.extend(result['updates'])

                # 每当缓冲区达到一定大小时，批量更新数据库
                if len(results_buffer) >= batch_size:
                    # 批量更新数据库
                    for update in results_buffer:
                        if 'key' in update and 'data' in update:
                            db.set_data_id(update['key'], **update['data'])

                    # 定期提交数据库
                    if i % 50 == 0:
                        db.commit()

                    # 定期导出CSV
                    if i % 100 == 0:
                        db.dump_to_csv(os.path.join(log_path, 'log.csv'))

                    # 清空缓冲区
                    results_buffer = []

                    # 小暂停，让Windows有时间释放资源
                    time.sleep(0.05)

                    # 强制垃圾回收
                    gc.collect()

        # 处理剩余的更新
        if results_buffer:
            for update in results_buffer:
                if 'key' in update and 'data' in update:
                    db.set_data_id(update['key'], **update['data'])

    finally:
        # 确保数据库最终被保存和关闭
        db.commit()
        db.dump_to_csv(os.path.join(log_path, 'log.csv'))
        db.close()


def run_with_memory_tracking():
    """
    运行主程序，同时监控内存使用情况
    """
    try:
        import psutil
        process = psutil.Process(os.getpid())

        def log_memory():
            # 获取内存使用情况 (MB)
            memory_info = process.memory_info()
            memory_mb = memory_info.rss / 1024 / 1024
            logger.info(f"内存使用: {memory_mb:.2f} MB")

        # 每10分钟记录一次内存使用情况
        import threading
        def memory_logger():
            while True:
                log_memory()
                time.sleep(600)  # 10分钟

        # 启动内存监控线程
        monitor_thread = threading.Thread(target=memory_logger, daemon=True)
        monitor_thread.start()

    except ImportError:
        logger.warning("psutil库未安装，无法监控内存使用情况")

    # 运行主程序
    process_json_files()


if __name__ == "__main__":
    # 设置Windows特定优化
    if os.name == 'nt':  # Windows系统
        # 尝试提高进程优先级
        try:
            import psutil

            p = psutil.Process(os.getpid())
            p.nice(psutil.HIGH_PRIORITY_CLASS)
        except (ImportError, PermissionError):
            logger.warning("无法设置进程优先级")

    # 启动处理并监控内存
    run_with_memory_tracking()
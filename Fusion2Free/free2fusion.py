import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm

import fusion2free
from fusion2free import encoder, angle_fusion_2_free
from utils.define import SOL, RECOMPUTE
from utils.freeCheck import run_freecad_modeling
from utils.free_opeartion import free_make_new_doc, free_make_new_body, free_make_new_sketch, free_make_extrude, mul_mat
from utils.get_free_bbox import get_combined_bbox, setup_to_fusion
from utils.load_fusion import get_fusion_json, get_fusion_sequence, load_fusion
from utils.logging_db import LogDatabase


def generate_division(lower, upper, n, f):
    """
    生成区间的等分数列。

    参数：
    lower (float): 下界
    upper (float): 上界
    n (int): 等分数
    f (str): 控制包含边界的参数
             'u' - 排除上界
             'l' - 排除下界
             其他 - 包含上下界

    返回：
    list: 等分数列
    """
    if n <= 0:
        raise ValueError("等分数n必须是正整数")
    if upper < lower:
        # swap
        lower, upper = upper, lower
    if f not in ['u', 'l', '']:
        raise ValueError("参数f必须是'u', 'l'或其他字符串")

    step = (upper - lower) / n
    divisions = []

    if f == 'u':
        # 包含下界，排除上界
        for i in range(n):
            divisions.append(lower + step * i)
    elif f == 'l':
        # 包含上界，排除下界
        for i in range(1, n + 1):
            divisions.append(lower + step * i)
    else:
        # 包含上下界
        for i in range(n + 1):
            divisions.append(lower + step * i)

    return divisions


def regenerate_fusion(data_id, fusion_json):
    seq_list = fusion_json['sequence']
    entry_dict = fusion_json['entities']
    ret_json_list = []

    # 找到最后一个 ExtrudeFeature 操作
    last_extrude_index = None
    for i, op_info in enumerate(seq_list):
        if op_info['type'] == 'ExtrudeFeature':
            last_extrude_index = i

    # 如果没有找到 ExtrudeFeature 操作，直接返回空列表
    if last_extrude_index is None:
        raise ValueError("未找到 ExtrudeFeature 操作")

    # 只处理最后一个 ExtrudeFeature 操作
    op_info = seq_list[last_extrude_index]
    op_name = op_info['entity']
    fusion_extrude_parameter = entry_dict[op_name]
    e_len1 = fusion_extrude_parameter["extent_one"]["distance"]["value"]
    e_len2 = fusion_extrude_parameter["extent_two"]["distance"]["value"]

    # 生成第一个方向的变体
    e_len1_list = generate_division(e_len1, 1.2 * e_len1, 4, 'l')
    e_len1_list.extend(generate_division(0.8 * e_len1, e_len1, 4, 'u'))
    for e_len1_elem1 in e_len1_list:
        # 创建深拷贝以避免修改原始对象
        import copy
        new_fusion_json = copy.deepcopy(fusion_json)
        new_fusion_json["entities"][op_name]["extent_one"]["distance"]["value"] = e_len1_elem1
        ret_json_list.append(new_fusion_json)

    # 如果第二个方向存在，也为其生成变体
    if abs(e_len2 - 0.0) > 1e-8:
        e_len2_list = generate_division(e_len2, 1.2 * e_len2, 4, 'l')
        e_len2_list.extend(generate_division(0.8 * e_len2, e_len2, 4, 'u'))
        for e_len2_elem1 in e_len2_list:
            # 创建深拷贝以避免修改原始对象
            import copy
            new_fusion_json = copy.deepcopy(fusion_json)
            new_fusion_json["entities"][op_name]["extent_two"]["distance"]["value"] = e_len2_elem1
            ret_json_list.append(new_fusion_json)

    return ret_json_list


def remove_last_profile(fusion_json):
    """
    删除Fusion 360 JSON数据中最后一个Extrude操作的一个profile及其对应的Sketch profile。

    规则:
    1. 只对seq_list长度大于4的建模操作起效
    2. 删除最后一个Extrude中的一个profile（如果只有一个profile则删除整个操作）
    3. 同时删除对应Sketch中的相应profile（如果Sketch的profiles为空则删除整个Sketch）

    :param fusion_json: Fusion 360的JSON数据结构
    :return: 修改后的Fusion 360 JSON数据结构
    """
    # 深拷贝以避免修改原始数据
    import copy
    modified_json = copy.deepcopy(fusion_json)

    seq_list = modified_json.get('sequence', [])
    entry_dict = modified_json.get('entities', {})

    # 规则1: 只有当序列长度大于4时才执行操作
    if len(seq_list) <= 4:
        raise ValueError("序列长度小于4，无法执行操作")

    # 查找最后一个Extrude操作
    last_extrude_idx = None
    for idx in range(len(seq_list) - 1, -1, -1):
        if seq_list[idx].get('type') == 'ExtrudeFeature':
            last_extrude_idx = idx
            break

    if last_extrude_idx is None:
        raise ValueError("未找到ExtrudeFeature操作")

    # 获取最后一个Extrude的实体ID
    last_extrude_id = seq_list[last_extrude_idx].get('entity')
    last_extrude = entry_dict.get(last_extrude_id, {})

    # 获取Extrude的profiles列表
    profiles = last_extrude.get('profiles', [])
    if not profiles:
        raise ValueError("Extrude操作没有profiles")

    # 删除最后一个profile并记录关联的sketch_id和profile_id
    last_profile = profiles.pop()  # 移除并获取最后一个profile
    sketch_id = last_profile.get('sketch')
    profile_id = last_profile.get('profile')

    # 更新Extrude的profiles列表
    if profiles:  # 如果还有其他profile，更新列表
        entry_dict[last_extrude_id]['profiles'] = profiles
    else:  # 如果没有其他profile，删除整个Extrude操作
        del entry_dict[last_extrude_id]
        # 从sequence中移除最后一个Extrude操作
        del seq_list[last_extrude_idx]

    # 删除Sketch中的对应profile
    if sketch_id in entry_dict and profile_id in entry_dict[sketch_id].get('profiles', {}):
        # 删除特定profile
        del entry_dict[sketch_id]['profiles'][profile_id]

        # 检查sketch的profiles是否为空，如果是则删除整个sketch
        if not entry_dict[sketch_id]['profiles']:
            # 找到对应的Sketch在sequence中的位置
            sketch_idx = None
            for idx, op in enumerate(seq_list):
                if op.get('type') == 'Sketch' and op.get('entity') == sketch_id:
                    sketch_idx = idx
                    break

            # 删除Sketch实体和sequence中的条目
            if sketch_idx is not None:
                del entry_dict[sketch_id]
                del seq_list[sketch_idx]

    # 重新排序sequence的index字段，使其连续
    for new_idx, op_info in enumerate(seq_list):
        op_info['index'] = new_idx

    # 更新modified_json
    modified_json['sequence'] = seq_list
    modified_json['entities'] = entry_dict

    return modified_json


def generate_fusion_json(new_key):
    # 打开并读取所有行
    with open('data/filtered_train_list.txt', 'r') as f:
        lines = f.readlines()
    # 使用 tqdm 包装循环，添加进度条
    # 初始化 new_key 和一个锁，用于线程安全地递增 new_key
    new_key_lock = threading.Lock()
    new_key = 0  # 根据需要设置初始值

    def process_key(key):
        global new_key
        key = key.strip()  # 去除可能的换行符或空格
        fusion_json_path = os.path.join('data', 'cad_json_repair', key[:4], f'{key}.json')

        # 加载 fusion_json
        fusion_json = fusion2free.load_fusion(fusion_json_path)  # 假设 fusion2free 已定义

        # 生成重建后的 JSON 列表
        ret_json_list = regenerate_fusion(new_key, fusion_json)  # 假设 regenerate_fusion 已定义
        try:
            rm_json=remove_last_profile(fusion_json)
            ret_json_list.append(rm_json)
        except Exception as e:
            print(f'Error processing key {key}: {e}')
        saved_files = []
        for ret_json in ret_json_list:
            with new_key_lock:
                current_new_key = new_key
                new_key += 1
            str_new_key = f'{int(current_new_key):08}'
            save_json_dir = os.path.join('data', 'cad_json_repair', str_new_key[:4])
            os.makedirs(save_json_dir, exist_ok=True)
            print(f'Now processing {str_new_key}.json')
            output_path = os.path.join(save_json_dir, f'{str_new_key}.json')
            with open(output_path, 'w', encoding='utf-8') as fj:
                fj.write(json.dumps(ret_json, ensure_ascii=False, indent=4))  # 格式化 JSON
            saved_files.append(output_path)
        return len(saved_files)

    # 设置线程数量，根据系统性能调整
    num_threads = 8

    # 使用 ThreadPoolExecutor 进行多线程处理
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # 提交所有 key 的处理任务
        futures = {executor.submit(process_key, key): key for key in lines}

        # 使用 tqdm 显示进度条
        for future in tqdm(as_completed(futures), total=len(futures), desc='Processing keys', unit='key'):
            try:
                result = future.result()
                # 可选：处理返回的结果，例如统计保存的文件数量
            except Exception as e:
                key = futures[future]
                print(f'Error processing key {key}: {e}')


def setup_directories(paths):
    """
    创建所需的目录。
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)


def handle_conversion(db, key, val, op_seq, output_py_path, log_path):
    """
    处理转换逻辑，并更新数据库。
    """
    try:
        ret_str, Free_str, error_code = fusion2free.fusion2free(key, val)
        if op_seq[-1] == 'S':
            error_code = 'UNUSED SKETCH'
        if error_code:
            print(f'data_id:{key}, convert error_code:{error_code}')
        db.set_data_id(
            key,
            is_convert=1,
            fusion_sequence=op_seq,
            free_sequence=Free_str,
            is_valid=0,
            error_code=error_code
        )
        # 创建子目录并写入文件
        sub_dir = os.path.join(output_py_path, key[:4])
        os.makedirs(sub_dir, exist_ok=True)
        with open(os.path.join(sub_dir, f"{key}_free.py"), 'w') as f:
            f.write(ret_str)
    except Exception as e:
        error_code = str(e)
        print(f'data_id:{key}, convert error_code:{error_code}')
        db.set_data_id(key, is_convert=0, error_code=error_code)
        # db.dump_to_csv(os.path.join(log_path, 'log.csv'))


def handle_validation(db, key, output_py_path, log_path, output_free_path):
    """
    处理验证逻辑，并更新数据库。
    """
    try:
        run_freecad_modeling(key, output_py_path, log_path, output_free_path)
        db.set_is_valid(key, 1)
    except Exception as e:
        error_code = str(e)
        print(f'data_id:{key}, valid error_code:{error_code}')
        db.set_data_id(key, is_valid=0, error_code=error_code)
        # db.dump_to_csv(os.path.join(log_path, 'log.csv'))


def handle_bbox(db, key, log_path, output_free_path, fusion_path):
    """
        处理验证逻辑，并更新数据库。
        """
    try:
        free_path = os.path.join(output_free_path, key[:4], f"{key}_free.FCStd")
        bbox_tuple = get_combined_bbox(free_path)
        setup_to_fusion(bbox_tuple, fusion_path)
        db.set_is_valid(key, 1)
    except Exception as e:
        error_code = str(e)
        print(f'data_id:{key}, valid error_code:{error_code}')
        db.set_data_id(key, is_valid=0, error_code=error_code)
        # db.dump_to_csv(os.path.join(log_path, 'log.csv'))


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

    # 获取JSON列表
    # json_list = get_fusion_json(fusion_prefix_path, after_id=1000000)
    json_path_list = []
    for root, dirs, files in os.walk(fusion_prefix_path):
        for file in files:
            if file.endswith('.json'):
                json_path_list.append(os.path.join(root, file))
    # 初始化数据库
    db = LogDatabase(db_path)
    db.begin_transaction()
    try:
        # 处理每个JSON文件
        for index, path in enumerate(tqdm(json_path_list, desc="Processing JSON files")):
            key = path[-13:-5]

            try:
                val = load_fusion(path)
            except Exception as e:
                print(f"Error loading {path}: {e}")
                db.set_data_id(key, is_convert=0, fusion_sequence='', free_sequence='', is_valid=0, error_code=f'Error loading {path}: {e}')
                continue

            ki = int(key)
            if ki < 2001169:
                continue
            if ki >= 2010000:
                break
            db.set_data_id(key, is_convert=0, fusion_sequence='', free_sequence='', is_valid=0, error_code='')

            # 获取融合序列
            op_seq = get_fusion_sequence(val)
            db.set_fusion_sequence(key, op_seq)
            is_convert = db.get_is_convert(key)
            is_valid = db.get_is_valid(key)
            print(f"Now process: {key}")

            # 跳过已转换且有效的数据
            if is_convert == 1 and is_valid == 1:
                continue

            # 处理转换
            if is_convert == 0:
                handle_conversion(db, key, val, op_seq, output_py_path, log_path)

            # 处理验证
            if is_valid == 0:
                handle_validation(db, key, output_py_path, log_path, output_free_path)
                # if is_convert == 1 and is_valid == 1:
                handle_bbox(db, key, log_path, output_free_path, path)
            if index % 100 == 0:
                db.commit()
                db.dump_to_csv(os.path.join(log_path, 'log.csv'))
    finally:
        # 确保数据库最终被保存和关闭
        db.commit()
        db.dump_to_csv(os.path.join(log_path, 'log.csv'))
        db.close()


if __name__ == "__main__":
    process_json_files()
    new_key = 1000000
    # generate_fusion_json(new_key)

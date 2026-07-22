import argparse
import json
import os
from asyncio import as_completed, Lock
from concurrent.futures import ThreadPoolExecutor

from joblib import delayed, Parallel
from tqdm import tqdm

import fusion2free
from utils.freeCheck import run_freecad_modeling
from utils.load_fusion import get_fusion_json, get_fusion_sequence, load_fusion
import sqlite3

from utils.logging_db import LogDatabase
from utils.reduplicate_util import read_pkl, get_filter_set, filter_id_set

brep_gen_filter_set = filter_id_set()


def db_init(log_path='./logging/', fusion_prefix_path='./data/cad_json/'):
    json_list = []
    for root, dirs, files in os.walk(fusion_prefix_path):
        for file in files:
            if file.endswith('.json'):
                json_list.append(os.path.join(root, file))
    db = LogDatabase(os.path.join(log_path, 'log.db'))
    for json_file in tqdm(json_list, desc="Initializing database"):
        fusion_path = os.path.join(json_file)
        # fusion_json = load_fusion(fusion_path)
        key = fusion_path[-13:-5]
        if key not in brep_gen_filter_set:
            continue
        db.set_data_id(key, is_convert=0, fusion_sequence='', free_sequence='', is_valid=0, error_code='')
    # db.set_data_id(key, is_convert=0, fusion_sequence='', free_sequence='', is_valid=0, error_code='')


def process_single_item(item, db_path, output_py_path, output_free_path, log_path, fusion_prefix_path, db_lock):
    """处理单个 JSON item 的逻辑，与串行版本中处理一条数据的逻辑类似。
       在此函数中实现超时保护和DB写入加锁保护。
    """
    key = item[0]
    val = item[1]
    ki = int(key)

    # 根据原逻辑进行过滤条件判断
    if ki <= 152045:
        return  # 跳过不需处理的项

    # 每个任务内单独连接数据库
    with db_lock:
        db = LogDatabase(db_path)
        db.set_data_id(key, is_convert=0, fusion_sequence='', free_sequence='', is_valid=0, error_code='')
        db.close()

    op_seq = get_fusion_sequence(val)

    # 再次打开数据库进行写入（减少锁定范围，仅在写入数据时加锁）
    with db_lock:
        db = LogDatabase(db_path)
        db.set_fusion_sequence(key, op_seq)
        is_convert = db.get_is_convert(key)
        is_valid = db.get_is_valid(key)
        db.close()

    if is_convert == 1 and is_valid == 1:
        # 已处理且有效，跳过
        return

    # 转换逻辑
    if is_convert == 0:
        # 尝试转换
        try:
            ret_str, Free_str, error_code = fusion2free.fusion2free(key, val)
            # 写入数据库
            with db_lock:
                db = LogDatabase(db_path)
                db.set_data_id(key, is_convert=1, fusion_sequence=op_seq, free_sequence=Free_str, is_valid=0,
                               error_code=error_code)
                db.close()

            if error_code:
                print(f'data_id:{key}, convert error_code:{error_code}')
            # 写入py文件
            os.makedirs(os.path.join(output_py_path, key[:4]), exist_ok=True)
            with open(os.path.join(output_py_path, key[:4], key + '_free.py'), 'w') as f:
                f.write(ret_str)
        except Exception as e:
            error_code = str(e)
            print(f'data_id:{key}, convert error_code:{error_code}')
            with db_lock:
                db = LogDatabase(db_path)
                db.set_data_id(key, is_convert=0, error_code=error_code)
                db.dump_to_csv(os.path.join(log_path, 'log.csv'))
                db.close()
            return

    # 校验逻辑
    if is_valid == 0:
        try:
            run_freecad_modeling(key, output_py_path, log_path, output_free_path)
            with db_lock:
                db = LogDatabase(db_path)
                db.set_is_valid(key, 1)
                db.close()
        except Exception as e:
            error_code = str(e)
            print(f'data_id:{key},valid error_code:{error_code}')
            with db_lock:
                db = LogDatabase(db_path)
                db.set_data_id(key, is_valid=0, error_code=error_code)
                db.dump_to_csv(os.path.join(log_path, 'log.csv'))
                db.close()


def main():
    # parser = argparse.ArgumentParser(description="脚本运行模式控制")
    # parser.add_argument('--parallel', action='store_true', help='开启并行处理')
    # parser.add_argument('--init', action='store_true', help='运行初始化逻辑')
    # args = parser.parse_args()

    # 路径与初始化
    output_py_path = './data/cad_py_repair/'
    output_free_path = './data/cad_free_repair/'
    os.makedirs(output_py_path, exist_ok=True)
    os.makedirs(output_free_path, exist_ok=True)
    log_path = './logging/'
    os.makedirs(log_path, exist_ok=True)
    db_path = os.path.join(log_path, 'log.db')

    fusion_prefix_path = './data/cad_json_repair'
    # json_list = get_fusion_json(fusion_prefix_path)
    json_path_list = []
    for root, dirs, files in os.walk(fusion_prefix_path):
        for file in files:
            if file.endswith('.json'):
                json_path_list.append(os.path.join(root, file))

    db = LogDatabase(db_path)
    db.begin_transaction()
    for index, path in enumerate(tqdm(json_path_list, desc="Processing JSON files")):
        val = load_fusion(path)
        key = path[-13:-5]

        # 检查 key 是否是有效的整数
        # fys+添加了对 key 格式的验证，跳过非数字命名的文件
        if not key.isdigit():
            print(f"Skipping file with invalid key format: {path}")
            continue
        
        ki = int(key)
        if ki >= 1000000:
            break
        # if ki <= 5852:
        #     continue
        # if key not in val_data_id_set:
        #     continue
        # if key not in brep_gen_filter_set:
        #     continue
        # db.set_data_id(key, is_convert=0, fusion_sequence='', free_sequence='', is_valid=0, error_code='')

        err = db.get_error_code(key)
        is_convert = db.get_is_convert(key)
        is_valid = db.get_is_valid(key)
        # if 'Recompute' in err or is_valid == 1:
        #     continue

        op_seq = get_fusion_sequence(val)

        db.set_fusion_sequence(key, op_seq)
        if index % 500 == 0:
            db.commit()
            db.dump_to_csv(os.path.join(log_path, 'log.csv'))
        print(f"Now process:{key}")

        if is_convert == 1 and is_valid == 1:
            continue
        if is_convert == 0:
            try:
                ret_str, Free_str, error_code = fusion2free.fusion2free(key, val)
                # 调试信息
                print(f'data_id:{key}, ret_str length: {len(ret_str)}')
                if op_seq[-1] == 'S':
                    error_code = 'UNUSED SKETCH'
                if error_code:
                    print(f'data_id:{key},convert error_code:{error_code}')
                # 先创建目录并写入文件
                os.makedirs(os.path.join(output_py_path, key[:4]), exist_ok=True)
                file_path = os.path.join(output_py_path, key[:4], key + '_free.py')
                print(f'Writing file: {file_path}')
                try:
                    with open(file_path, 'w') as f:
                        f.write(ret_str)
                    print(f'File written successfully: {file_path}')
                except Exception as e:
                    print(f'Error writing file: {e}')
                    continue
                # 确保文件存在后再设置 is_convert=1
                if os.path.exists(file_path):
                    file_size = os.path.getsize(file_path)
                    print(f'File exists, size: {file_size} bytes')
                    db.set_data_id(key, is_convert=1, fusion_sequence=op_seq, free_sequence=Free_str, is_valid=0,
                                   error_code=error_code)
                else:
                    print(f'Failed to create file: {file_path}')
                    continue

            except Exception as e:
                error_code = str(e)
                print(f'data_id:{key},convert error_code:{error_code}')
                db.set_data_id(key, is_convert=0, error_code=error_code)
                continue
        if is_valid == 0:
            try:
                run_freecad_modeling(key, output_py_path, log_path, output_free_path)
                db.set_is_valid(key, 1)
            except Exception as e:
                error_code = str(e)
                print(f'data_id:{key},valid error_code:{error_code}')
                db.set_data_id(key, is_valid=0, error_code=error_code)

    db.commit()
    db.dump_to_csv(os.path.join(log_path, 'log.csv'))
    db.close()


# check


if __name__ == '__main__':
    main()

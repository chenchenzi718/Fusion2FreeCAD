import json
import os

from tqdm import tqdm

from utils.load_fusion import load_fusion


def repair_fusion(fusion_json):
    """
    修复Fusion 360 JSON数据中的问题：
    1. UNUSED SKETCH：未使用的草图
    2. EMPTY SKETCH：空草图
    3. EMPTY EXTRUDE PROFILE：空拉伸剖面

    修复方法：
    - 检查问题；移除对应的实体和在sequence中的元素
    - 处理后的sequence字段中的index必须连续

    :param fusion_json: Fusion 360的JSON数据结构
    :return: 修复后的Fusion 360 JSON数据结构
    """
    seq_list = fusion_json.get('sequence', [])
    entry_dict = fusion_json.get('entities', {})

    # 初始化used_dict，记录所有被草图使用的情况
    used_sketches = set()

    # 收集需要移除的实体ID
    entities_to_remove = set()
    sequence_to_remove_indices = set()

    # 遍历sequence，识别需要修复的项
    for idx, op_info in enumerate(seq_list):
        op_name = op_info.get('entity')
        op_type = op_info.get('type')

        if op_type == 'ExtrudeFeature':
            extrude_feature = entry_dict.get(op_name, {})
            profiles = extrude_feature.get('profiles', [])
            if not profiles:
                # 修复3：空拉伸剖面，标记该ExtrudeFeature和其在sequence中的索引为移除
                entities_to_remove.add(op_name)
                sequence_to_remove_indices.add(idx)
            else:
                # 标记所有被使用的草图
                for profile in profiles:
                    sketch_id = profile.get('sketch')
                    if sketch_id:
                        used_sketches.add(sketch_id)

        elif op_type == 'Sketch':
            sketch = entry_dict.get(op_name, {})
            profiles = sketch.get('profiles', {})
            if not profiles:
                # 修复2：空草图，标记该Sketch和其在sequence中的索引为移除
                entities_to_remove.add(op_name)
                sequence_to_remove_indices.add(idx)

    # 修复1：未使用的草图
    # 遍历所有草图，找出未被使用的草图
    for entity_id, entity in entry_dict.items():
        if entity.get('type') == 'Sketch' and entity_id not in used_sketches:
            entities_to_remove.add(entity_id)
            # 找到对应的sequence索引并标记为移除
            for idx, op_info in enumerate(seq_list):
                if op_info.get('entity') == entity_id:
                    sequence_to_remove_indices.add(idx)
                    break  # 假设每个实体在sequence中只出现一次

    # 移除标记的实体
    for entity_id in entities_to_remove:
        if entity_id in entry_dict:
            del entry_dict[entity_id]

    # 移除标记的sequence项
    # 从高到低排序索引，避免移除时影响后续索引
    for idx in sorted(sequence_to_remove_indices, reverse=True):
        del seq_list[idx]

    # 重新排序sequence的index字段，使其连续
    for new_idx, op_info in enumerate(seq_list):
        op_info['index'] = new_idx

    # 更新fusion_json
    fusion_json['sequence'] = seq_list
    fusion_json['entities'] = entry_dict

    return fusion_json


def read_split_data(path):
    with open(path, 'r') as f:
        split_data = json.load(f)
    # combine train val test
    train_list = split_data['train']
    val_list = split_data['validation']
    test_list = split_data['test']
    split_filtered_list = [index[-8:] for index in train_list + val_list + test_list]
    # sort split_filtered_list
    split_filtered_list.sort()
    return split_filtered_list
    # return split


if __name__ == '__main__':
    split_filtered_list = read_split_data('data/train_val_test_split_filtered.json')
    # print(split_filtered_list)
    for data_id in tqdm(split_filtered_list, desc="Processing JSON files"):

        # fys modefy the path
        fusion_json_path = os.path.join('data/deepcad/cad_json', data_id[:4], f'{data_id}.json')
        fusion_json_path_save=os.path.join('data/cad_json_repair', data_id[:4], f'{data_id}.json')
        os.makedirs(os.path.join('data/cad_json_repair', data_id[:4]), exist_ok=True)
        fusion_json = load_fusion(fusion_json_path)
        repair_fusion_json=repair_fusion(fusion_json)
        # dump json
        with open(fusion_json_path_save, 'w') as f:
            json.dump(repair_fusion_json, f, indent=4)

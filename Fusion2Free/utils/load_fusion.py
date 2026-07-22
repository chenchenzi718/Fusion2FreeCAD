import json
import os

from tqdm import tqdm

from utils.reduplicate_util import filter_id_set


def load_fusion(fusion_path):
    # json load
    with open(fusion_path, 'r', encoding='utf-8') as f:
        fusion = json.load(f)
    return fusion


def get_map_dict(fusion_json):
    entities_list = fusion_json['entities']
    outer_type_list = {}
    for entry in entities_list:
        # name：
        # entry: operation name
        # curve： curve name
        # in ExtrudeFeature：need profile and some curve
        entry_type = entities_list[entry]['type']
        if entry_type == 'Sketch':
            # print('Sketch')
            profile_dict = entities_list[entry]['profiles']
            for key, value in profile_dict.items():
                loop_list = value['loops']
                for loop in loop_list:
                    outer_type = loop['is_outer']
                    # if has plus 1, else set one,simple
                    if outer_type is False:
                        print(json_file)


        elif entry_type == 'ExtrudeFeature':
            # print('Extrude')
            operation_type = entities_list[entry]['operation']
            operation_type_list[operation_type] = operation_type_list.get(operation_type, 0) + 1
            # if operation_type != 'NewBodyFeatureOperation':
            # print(json_file)
    # print(outer_type_list)


def find2E():
    pass


def get_fusion_json(fusion_prefix_path, after_id=0):
    brep_gen_filter_set = filter_id_set()
    json_list = []
    for root, dirs, files in os.walk(fusion_prefix_path):
        for file in files:
            if file.endswith('.json'):
                json_list.append(os.path.join(root, file))
    fusion_json_list = []
    for json_file in tqdm(json_list, desc="Loading JSON files"):
        fusion_path = os.path.join(json_file)
        file_id = int(fusion_path[-13:-5])
        if file_id >= after_id and fusion_path[-13:-5] in brep_gen_filter_set and fusion_path[-13:-5]:
            fusion_json_list.append([fusion_path[-13:-5], load_fusion(fusion_path)])
            # print(f'file_id:{file_id}')
    return fusion_json_list


def get_fusion_sequence(fusion_json):
    entities_list = fusion_json['entities']
    sequence_list = fusion_json['sequence']
    outer_type_list = {}
    op_str = ''
    for elem in sequence_list:
        entry = elem['entity']
        # name：
        # entry: operation name
        # curve： curve name
        # in ExtrudeFeature：need profile and some curve
        entry_type = entities_list[entry]['type']
        if entry_type == 'Sketch':
            # print('Sketch')
            # profile_dict = entities_list[entry]['profiles']
            # for key, value in profile_dict.items():
            #     loop_list = value['loops']
            #     for loop in loop_list:
            #         outer_type = loop['is_outer']
            #         # if has plus 1, else set one,simple
            #         if outer_type is False:
            #             print(json_file)
            op_str += 'S'
            continue

        elif entry_type == 'ExtrudeFeature':
            # print('Extrude')
            operation_type = entities_list[entry]['operation']
            # operation_type_list[operation_type] = operation_type_list.get(operation_type, 0) + 1
            # profile = entities_list[entry]['profiles']
            # if operation_type == 'IntersectFeatureOperation'and len(profile)>1:
            #     print(f'operation_type:{operation_type},json_file:{json_file},len:{len(profile)}')
            op_str += operation_type[0]
    return op_str


if __name__ == '__main__':
    fusion_prefix_path = '../data/cad_json/0000/'
    json_list = []
    for root, dirs, files in os.walk(fusion_prefix_path):
        for file in files:
            if file.endswith('.json'):
                json_list.append(os.path.join(root, file))
    outer_type_list = {}
    op_str_dict = {}
    operation_type_list = {}
    for json_file in json_list:
        fusion_path = os.path.join(json_file)
        fusion_json = load_fusion(fusion_path)
        # print(fusion_json)
        entities_list = fusion_json['entities']
        sequence_list = fusion_json['sequence']
        outer_type_list = {}
        op_str = ''
        for elem in sequence_list:
            entry = elem['entity']
            # name：
            # entry: operation name
            # curve： curve name
            # in ExtrudeFeature：need profile and some curve
            entry_type = entities_list[entry]['type']
            if entry_type == 'Sketch':
                # print('Sketch')
                # profile_dict = entities_list[entry]['profiles']
                # for key, value in profile_dict.items():
                #     loop_list = value['loops']
                #     for loop in loop_list:
                #         outer_type = loop['is_outer']
                #         # if has plus 1, else set one,simple
                #         if outer_type is False:
                #             print(json_file)
                op_str += 'S'
                continue

            elif entry_type == 'ExtrudeFeature':
                # print('Extrude')
                operation_type = entities_list[entry]['operation']
                operation_type_list[operation_type] = operation_type_list.get(operation_type, 0) + 1
                profile = entities_list[entry]['profiles']
                # if operation_type == 'IntersectFeatureOperation'and len(profile)>1:
                #     print(f'operation_type:{operation_type},json_file:{json_file},len:{len(profile)}')
                op_str += operation_type[0]
        print(f'op_str:{op_str}')
        # op_str_dict[op_str] = op_str_dict.get(op_str, 0) + 1
        # please order dict by value
    sorted_op_str_dict = dict(sorted(op_str_dict.items(), key=lambda item: item[1], reverse=True))

    with open('sorted_op_str_dict.json', 'w') as jf:
        json.dump(sorted_op_str_dict, jf, indent=4)
        # print(outer_type_list)
    print(operation_type_list)
    print(sorted_op_str_dict)

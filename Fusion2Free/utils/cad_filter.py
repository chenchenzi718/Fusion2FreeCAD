import json
import os
from tqdm import tqdm

from utils.load_fusion import load_fusion


def get_CAD_model_len(fusion_json):
    cad_sequence = fusion_json['sequence']
    return len(cad_sequence)


def filter_CAD_model_by_len(fusion_json_list, max_len):
    return [data_id for data_id, fusion_json in fusion_json_list.items() if get_CAD_model_len(fusion_json) <= max_len]


def cad_filter(max_len, fusion_prefix_path='../data/cad_json/'):
    json_list = []
    fusion_json_list = {}
    # use tqdm
    # read train_val_test_split.json
    split_path='../data/train_val_test_split.json'
    with open(split_path, 'r') as f:
        split_data = json.load(f)
    test_json_list=split_data['test']
    for short_path in tqdm(test_json_list, desc="Loading CAD models"):
        json_path=(os.path.join(fusion_prefix_path, short_path + '.json'))
        fusion_json = load_fusion(json_path)
        fusion_json_list[short_path]=fusion_json
    # print(fusion_json_list)
    filter_data=filter_CAD_model_by_len(fusion_json_list, max_len)
    print(filter_data)
    # save filter_data as json list
    with open('filter_data.json', 'w') as f:
        json.dump(filter_data, f)
if __name__ == '__main__':
    cad_filter(2)

"""
CAD model length filter -- filter DeepCAD models by operation sequence length.
"""

import json
import os

from tqdm import tqdm

from fusion2free.utils.load_fusion import load_fusion


def get_CAD_model_len(fusion_json):
    """Return the number of operations in a Fusion model's sequence."""
    return len(fusion_json["sequence"])


def filter_CAD_model_by_len(fusion_json_list, max_len):
    """Return data_ids of models whose sequence length is <= max_len."""
    return [
        data_id
        for data_id, fusion_json in fusion_json_list.items()
        if get_CAD_model_len(fusion_json) <= max_len
    ]


def cad_filter(max_len, fusion_prefix_path=None):
    """
    Load test-set models and filter by maximum sequence length.

    Saves the filtered list to filter_data.json.
    """
    from fusion2free.utils.config import INPUT_DIR

    if fusion_prefix_path is None:
        fusion_prefix_path = INPUT_DIR
    split_path = os.path.join(os.path.dirname(INPUT_DIR), "train_val_test_split.json")
    with open(split_path, "r") as f:
        split_data = json.load(f)
    test_json_list = split_data["test"]

    fusion_json_list = {}
    for short_path in tqdm(test_json_list, desc="Loading CAD models"):
        json_path = os.path.join(fusion_prefix_path, f"{short_path}.json")
        fusion_json_list[short_path] = load_fusion(json_path)

    filter_data = filter_CAD_model_by_len(fusion_json_list, max_len)
    print(filter_data)

    with open("filter_data.json", "w") as f:
        json.dump(filter_data, f)


if __name__ == "__main__":
    cad_filter(2)
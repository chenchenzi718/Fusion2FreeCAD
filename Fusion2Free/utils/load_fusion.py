"""
Load and parse Fusion 360 (DeepCAD) JSON files.
"""

import json
import os

from tqdm import tqdm


def load_fusion(fusion_path):
    """Load a Fusion 360 JSON file and return its content as a dict."""
    with open(fusion_path, "r", encoding="utf-8") as f:
        fusion = json.load(f)
    return fusion


def get_fusion_json(fusion_prefix_path, after_id=0):
    """Walk a directory and load all Fusion JSON files whose ID >= after_id."""
    json_list = []
    for root, dirs, files in os.walk(fusion_prefix_path):
        for file in files:
            if file.endswith(".json"):
                json_list.append(os.path.join(root, file))
    fusion_json_list = []
    for json_file in tqdm(json_list, desc="Loading JSON files"):
        fusion_path = os.path.join(json_file)
        file_id = int(fusion_path[-13:-5])
        if file_id >= after_id:
            fusion_json_list.append(
                [fusion_path[-13:-5], load_fusion(fusion_path)]
            )
    return fusion_json_list


def get_fusion_sequence(fusion_json):
    """
    Convert a Fusion JSON model to a short operation sequence string.

    Returns a string where each character represents an operation type:
      'S' = Sketch
      'N' = NewBodyFeatureOperation
      'J' = JoinFeatureOperation
      'C' = CutFeatureOperation
    """
    entities_list = fusion_json["entities"]
    sequence_list = fusion_json["sequence"]
    op_str = ""
    for elem in sequence_list:
        entry = elem["entity"]
        entry_type = entities_list[entry]["type"]
        if entry_type == "Sketch":
            op_str += "S"
        elif entry_type == "ExtrudeFeature":
            operation_type = entities_list[entry]["operation"]
            op_str += operation_type[0]
    return op_str


if __name__ == "__main__":
    from fusion2free.utils.config import INPUT_DIR

    # Quick test: list operation sequences
    test_dir = os.path.join(INPUT_DIR, "0000/")
    if os.path.isdir(test_dir):
        for json_file in os.listdir(test_dir):
            if json_file.endswith(".json"):
                fusion_json = load_fusion(os.path.join(test_dir, json_file))
                op_str = get_fusion_sequence(fusion_json)
                print(f"{json_file}: {op_str}")
    else:
        print(f"Test directory not found: {test_dir}")
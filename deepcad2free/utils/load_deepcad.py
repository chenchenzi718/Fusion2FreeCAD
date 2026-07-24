"""
Load and parse DeepCAD JSON files.
"""

import json
import os

from tqdm import tqdm


def load_deepcad(deepcad_path):
    """Load a DeepCAD JSON file and return its content as a dict."""
    with open(deepcad_path, "r", encoding="utf-8") as f:
        deepcad = json.load(f)
    return deepcad


def get_deepcad_json(deepcad_prefix_path, after_id=0):
    """Walk a directory and load all DeepCAD JSON files whose ID >= after_id."""
    json_list = []
    for root, dirs, files in os.walk(deepcad_prefix_path):
        for file in files:
            if file.endswith(".json"):
                json_list.append(os.path.join(root, file))
    deepcad_json_list = []
    for json_file in tqdm(json_list, desc="Loading JSON files"):
        deepcad_path = os.path.join(json_file)
        file_id = int(deepcad_path[-13:-5])
        if file_id >= after_id:
            deepcad_json_list.append(
                [deepcad_path[-13:-5], load_deepcad(deepcad_path)]
            )
    return deepcad_json_list


def get_deepcad_sequence(deepcad_json):
    """
    Convert a DeepCAD JSON model to a short operation sequence string.

    Returns a string where each character represents an operation type:
      'S' = Sketch
      'N' = NewBodyFeatureOperation
      'J' = JoinFeatureOperation
      'C' = CutFeatureOperation
    """
    entities_list = deepcad_json["entities"]
    sequence_list = deepcad_json["sequence"]
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
    from deepcad2free.utils.config import INPUT_DIR

    # Quick test: list operation sequences
    test_dir = os.path.join(INPUT_DIR, "0000/")
    if os.path.isdir(test_dir):
        for json_file in os.listdir(test_dir):
            if json_file.endswith(".json"):
                deepcad_json = load_deepcad(os.path.join(test_dir, json_file))
                op_str = get_deepcad_sequence(deepcad_json)
                print(f"{json_file}: {op_str}")
    else:
        print(f"Test directory not found: {test_dir}")
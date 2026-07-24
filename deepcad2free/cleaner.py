"""
DeepCAD JSON cleaner -- repairs issues in DeepCAD JSON data.

Removes:
  1. UNUSED SKETCH -- sketches not referenced by any ExtrudeFeature
  2. EMPTY SKETCH -- sketches with no profiles
  3. EMPTY EXTRUDE PROFILE -- ExtrudeFeatures with no profile loops

After removal, the sequence field is re-indexed to be contiguous.
"""

import json
import os

from tqdm import tqdm

from deepcad2free.utils.load_deepcad import load_deepcad


def repair_deepcad(deepcad_json):
    """
    Repair a DeepCAD JSON model by removing problematic entities.

    Args:
        deepcad_json: parsed DeepCAD JSON dict

    Returns:
        Repaired DeepCAD JSON dict
    """
    seq_list = deepcad_json.get("sequence", [])
    entry_dict = deepcad_json.get("entities", {})

    used_sketches = set()
    entities_to_remove = set()
    sequence_to_remove_indices = set()

    for idx, op_info in enumerate(seq_list):
        op_name = op_info.get("entity")
        op_type = op_info.get("type")

        if op_type == "ExtrudeFeature":
            extrude_feature = entry_dict.get(op_name, {})
            profiles = extrude_feature.get("profiles", [])
            if not profiles:
                entities_to_remove.add(op_name)
                sequence_to_remove_indices.add(idx)
            else:
                for profile in profiles:
                    sketch_id = profile.get("sketch")
                    if sketch_id:
                        used_sketches.add(sketch_id)

        elif op_type == "Sketch":
            sketch = entry_dict.get(op_name, {})
            profiles = sketch.get("profiles", {})
            if not profiles:
                entities_to_remove.add(op_name)
                sequence_to_remove_indices.add(idx)

    for entity_id, entity in entry_dict.items():
        if entity.get("type") == "Sketch" and entity_id not in used_sketches:
            entities_to_remove.add(entity_id)
            for idx, op_info in enumerate(seq_list):
                if op_info.get("entity") == entity_id:
                    sequence_to_remove_indices.add(idx)
                    break

    for entity_id in entities_to_remove:
        if entity_id in entry_dict:
            del entry_dict[entity_id]

    for idx in sorted(sequence_to_remove_indices, reverse=True):
        del seq_list[idx]

    for new_idx, op_info in enumerate(seq_list):
        op_info["index"] = new_idx

    deepcad_json["sequence"] = seq_list
    deepcad_json["entities"] = entry_dict

    return deepcad_json


if __name__ == "__main__":
    from deepcad2free.utils.config import INPUT_DIR, REPAIR_DIR

    # Quick test: clean a single model
    test_path = os.path.join(INPUT_DIR, "0000/00000007.json")
    if os.path.exists(test_path):
        save_path = os.path.join(REPAIR_DIR, "0000/00000007.json")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        deepcad_json = load_deepcad(test_path)
        repaired = repair_deepcad(deepcad_json)
        with open(save_path, "w") as f:
            json.dump(repaired, f, indent=4)
        print(f"Saved: {save_path}")
    else:
        print(f"Test file not found: {test_path}")
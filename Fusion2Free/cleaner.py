"""
Fusion 360 JSON cleaner -- repairs issues in Fusion 360 JSON data.

Removes:
  1. UNUSED SKETCH -- sketches not referenced by any ExtrudeFeature
  2. EMPTY SKETCH -- sketches with no profiles
  3. EMPTY EXTRUDE PROFILE -- ExtrudeFeatures with no profile loops

After removal, the sequence field is re-indexed to be contiguous.
"""

import json
import os

from tqdm import tqdm

from fusion2free.utils.load_fusion import load_fusion


def repair_fusion(fusion_json):
    """
    Repair a Fusion 360 JSON model by removing problematic entities.

    Args:
        fusion_json: parsed Fusion 360 JSON dict

    Returns:
        Repaired Fusion 360 JSON dict
    """
    seq_list = fusion_json.get("sequence", [])
    entry_dict = fusion_json.get("entities", {})

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

    fusion_json["sequence"] = seq_list
    fusion_json["entities"] = entry_dict

    return fusion_json


if __name__ == "__main__":
    fusion_json_path = "data/deepcad/cad_json/0000/00000000.json"
    fusion_json_path_save = "data/cad_json_repair/0000/00000000.json"
    os.makedirs(os.path.join("data/cad_json_repair", "0000"), exist_ok=True)
    fusion_json = load_fusion(fusion_json_path)
    repaired = repair_fusion(fusion_json)
    with open(fusion_json_path_save, "w") as f:
        json.dump(repaired, f, indent=4)
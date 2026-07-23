"""
Reverse converter -- FreeCAD .FCStd -> Fusion 360 JSON.

Experimental module for converting FreeCAD models back to Fusion 360 JSON format.
This is provided as a reference implementation and may not handle all FreeCAD
feature types.

Requires FreeCAD to be importable at runtime (set FREECAD_LIB environment variable).
"""

import json
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm

from fusion2free.converter import fusion2free, encoder, angle_fusion_2_free
from fusion2free.utils.config import FREECAD_LIB_PATH, EOL, RECOMPUTE
from fusion2free.utils.free_check import run_freecad_modeling
from fusion2free.utils.free_operation import (
    free_make_new_doc,
    free_make_new_body,
    free_make_new_sketch,
    free_make_extrude,
    mul_mat,
)
from fusion2free.utils.get_free_bbox import get_combined_bbox, setup_to_fusion
from fusion2free.utils.load_fusion import get_fusion_json, get_fusion_sequence, load_fusion
from fusion2free.utils.logging_db import LogDatabase

# Ensure FreeCAD is importable
if FREECAD_LIB_PATH not in sys.path:
    sys.path.append(FREECAD_LIB_PATH)
os.environ["FREECAD_LIB"] = FREECAD_LIB_PATH

import FreeCAD as App
import FreeCAD


# ===================================================================
# Fusion JSON generation helpers
# ===================================================================

def generate_division(lower, upper, n, f):
    """
    Generate equally-spaced division points of an interval.

    Args:
        lower: lower bound
        upper: upper bound
        n: number of divisions
        f: boundary mode -- 'u' exclude upper, 'l' exclude lower, else include both
    """
    if n <= 0:
        raise ValueError("Number of divisions must be positive")
    if upper < lower:
        lower, upper = upper, lower
    if f not in ("u", "l", ""):
        raise ValueError("Parameter f must be 'u', 'l', or ''")

    step = (upper - lower) / n
    divisions = []

    if f == "u":
        for i in range(n):
            divisions.append(lower + step * i)
    elif f == "l":
        for i in range(1, n + 1):
            divisions.append(lower + step * i)
    else:
        for i in range(n + 1):
            divisions.append(lower + step * i)

    return divisions


def regenerate_fusion(data_id, fusion_json):
    """
    Generate parameter variants by perturbing the last ExtrudeFeature's extent.

    Returns a list of modified Fusion JSON dicts.
    """
    seq_list = fusion_json["sequence"]
    entry_dict = fusion_json["entities"]
    ret_json_list = []

    last_extrude_index = None
    for i, op_info in enumerate(seq_list):
        if op_info["type"] == "ExtrudeFeature":
            last_extrude_index = i

    if last_extrude_index is None:
        raise ValueError("No ExtrudeFeature found in the model")

    op_info = seq_list[last_extrude_index]
    op_name = op_info["entity"]
    fusion_extrude_parameter = entry_dict[op_name]
    e_len1 = fusion_extrude_parameter["extent_one"]["distance"]["value"]
    e_len2 = fusion_extrude_parameter["extent_two"]["distance"]["value"]

    e_len1_list = generate_division(e_len1, 1.2 * e_len1, 4, "l")
    e_len1_list.extend(generate_division(0.8 * e_len1, e_len1, 4, "u"))
    for elem in e_len1_list:
        import copy

        new_fusion_json = copy.deepcopy(fusion_json)
        new_fusion_json["entities"][op_name]["extent_one"]["distance"]["value"] = elem
        ret_json_list.append(new_fusion_json)

    if abs(e_len2 - 0.0) > 1e-8:
        e_len2_list = generate_division(e_len2, 1.2 * e_len2, 4, "l")
        e_len2_list.extend(generate_division(0.8 * e_len2, e_len2, 4, "u"))
        for elem in e_len2_list:
            import copy

            new_fusion_json = copy.deepcopy(fusion_json)
            new_fusion_json["entities"][op_name]["extent_two"]["distance"][
                "value"
            ] = elem
            ret_json_list.append(new_fusion_json)

    return ret_json_list


def remove_last_profile(fusion_json):
    """
    Remove the last profile from the last ExtrudeFeature and its associated Sketch profile.

    Only works for models with sequence length > 4.
    """
    import copy

    modified_json = copy.deepcopy(fusion_json)

    seq_list = modified_json.get("sequence", [])
    entry_dict = modified_json.get("entities", {})

    if len(seq_list) <= 4:
        raise ValueError("Sequence length < 4, operation not applicable")

    last_extrude_idx = None
    for idx in range(len(seq_list) - 1, -1, -1):
        if seq_list[idx].get("type") == "ExtrudeFeature":
            last_extrude_idx = idx
            break

    if last_extrude_idx is None:
        raise ValueError("No ExtrudeFeature found")

    last_extrude_id = seq_list[last_extrude_idx].get("entity")
    last_extrude = entry_dict.get(last_extrude_id, {})

    profiles = last_extrude.get("profiles", [])
    if not profiles:
        raise ValueError("Extrude has no profiles")

    last_profile = profiles.pop()
    sketch_id = last_profile.get("sketch")
    profile_id = last_profile.get("profile")

    if profiles:
        entry_dict[last_extrude_id]["profiles"] = profiles
    else:
        del entry_dict[last_extrude_id]
        del seq_list[last_extrude_idx]

    if sketch_id in entry_dict and profile_id in entry_dict[sketch_id].get(
        "profiles", {}
    ):
        del entry_dict[sketch_id]["profiles"][profile_id]

        if not entry_dict[sketch_id]["profiles"]:
            sketch_idx = None
            for idx, op in enumerate(seq_list):
                if op.get("type") == "Sketch" and op.get("entity") == sketch_id:
                    sketch_idx = idx
                    break

            if sketch_idx is not None:
                del entry_dict[sketch_id]
                del seq_list[sketch_idx]

    for new_idx, op_info in enumerate(seq_list):
        op_info["index"] = new_idx

    modified_json["sequence"] = seq_list
    modified_json["entities"] = entry_dict
    return modified_json


# ===================================================================
# FreeCAD -> Fusion JSON reverse conversion
# ===================================================================

def free2fusion(fcstd_path, output_json_path):
    """
    Convert a FreeCAD .FCStd file to Fusion 360 JSON format.

    Extracts Pad/Pocket features as ExtrudeFeatures and Sketch geometry
    as Sketch entities with Line3D/Arc3D/Circle3D curves.

    Args:
        fcstd_path: path to the FreeCAD .FCStd file
        output_json_path: path to write the output JSON

    Returns:
        The converted Fusion JSON dict
    """
    doc = FreeCAD.open(fcstd_path)

    sequence = []
    entities = {}
    index_counter = 0

    for obj in doc.Objects:
        if obj.TypeId in ("PartDesign::Pad", "PartDesign::Pocket"):
            if obj.TypeId == "PartDesign::Pad":
                operation = (
                    "JoinFeatureOperation"
                    if len(sequence) > 0
                    else "NewBodyFeatureOperation"
                )
            else:
                operation = "CutFeatureOperation"

            sketch_entity = f"Sketch_{index_counter}"

            extent_one_distance = float(obj.Length) / 1000.0

            extrude_entity = f"Extrude_{index_counter}"

            entities[extrude_entity] = {
                "type": "ExtrudeFeature",
                "operation": operation,
                "extent_type": "OneSideFeatureExtentType",
                "extent_one": {
                    "distance": {"value": extent_one_distance, "type": "Parameter"}
                },
                "extent_two": {
                    "distance": {"value": 0.0, "type": "Parameter"}
                },
                "profiles": [
                    {
                        "sketch": sketch_entity,
                        "profile": f"Profile_{index_counter}",
                    }
                ],
            }

            sequence.append(
                {
                    "index": index_counter,
                    "entity": extrude_entity,
                    "type": "ExtrudeFeature",
                }
            )
            index_counter += 1

        elif obj.TypeId == "Sketcher::SketchObject":
            sketch_entity = f"Sketch_{index_counter}"

            loops = {
                f"Profile_{index_counter}": {
                    "loops": [
                        {
                            "is_outer": True,
                            "profile_curves": [],
                        }
                    ]
                }
            }

            geometry = getattr(obj, "Geometry", []) if hasattr(obj, "Geometry") else []

            for geo in geometry:
                curve_entry = None

                if "LineSegment" in str(type(geo)):
                    curve_entry = {
                        "type": "Line3D",
                        "start_point": {
                            "x": float(geo.StartPoint.x) / 1000.0,
                            "y": float(geo.StartPoint.y) / 1000.0,
                            "z": float(geo.StartPoint.z) / 1000.0,
                        },
                        "end_point": {
                            "x": float(geo.EndPoint.x) / 1000.0,
                            "y": float(geo.EndPoint.y) / 1000.0,
                            "z": float(geo.EndPoint.z) / 1000.0,
                        },
                    }
                elif "ArcOfCircle" in str(type(geo)) or "Circle" in str(type(geo)):
                    circle = geo.Circle if hasattr(geo, "Circle") else geo
                    curve_entry = {
                        "type": "Circle3D",
                        "center_point": {
                            "x": float(circle.Center.x) / 1000.0,
                            "y": float(circle.Center.y) / 1000.0,
                            "z": float(circle.Center.z) / 1000.0,
                        },
                        "radius": float(circle.Radius) / 1000.0,
                        "normal": {
                            "x": float(circle.Normal.x),
                            "y": float(circle.Normal.y),
                            "z": float(circle.Normal.z),
                        },
                    }

                if curve_entry:
                    loops[f"Profile_{index_counter}"]["loops"][0]["profile_curves"].append(
                        curve_entry
                    )

            entities[sketch_entity] = {
                "type": "Sketch",
                "transform": {
                    "origin": {"x": 0.0, "y": 0.0, "z": 0.0},
                    "x_axis": {"x": 1.0, "y": 0.0, "z": 0.0},
                    "y_axis": {"x": 0.0, "y": 1.0, "z": 0.0},
                    "z_axis": {"x": 0.0, "y": 0.0, "z": 1.0},
                },
                "profiles": loops,
            }

            sequence.append(
                {
                    "index": index_counter,
                    "entity": sketch_entity,
                    "type": "Sketch",
                }
            )
            index_counter += 1

    bbox = {"min_point": {"x": 0, "y": 0, "z": 0}, "max_point": {"x": 0, "y": 0, "z": 0}}
    for obj in doc.Objects:
        if obj.TypeId == "PartDesign::Body":
            try:
                b = obj.Shape.BoundBox
                bbox = {
                    "min_point": {
                        "x": b.XMin / 1000.0,
                        "y": b.YMin / 1000.0,
                        "z": b.ZMin / 1000.0,
                    },
                    "max_point": {
                        "x": b.XMax / 1000.0,
                        "y": b.YMax / 1000.0,
                        "z": b.ZMax / 1000.0,
                    },
                }
                break
            except Exception:
                pass

    fusion_json = {
        "sequence": sequence,
        "entities": entities,
        "properties": {"bounding_box": bbox},
    }

    with open(output_json_path, "w") as f:
        json.dump(fusion_json, f, indent=4)

    FreeCAD.closeDocument(doc.Name)

    return fusion_json


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="FreeCAD -> Fusion 360 JSON converter")
    parser.add_argument("fcstd_path", help="Path to FreeCAD .FCStd file")
    parser.add_argument(
        "-o", "--output", default=None, help="Output JSON path (default: same name .json)"
    )
    args = parser.parse_args()

    if args.output is None:
        base = os.path.splitext(args.fcstd_path)[0]
        args.output = f"{base}.json"

    result = free2fusion(args.fcstd_path, args.output)
    print(f"Converted: {args.fcstd_path} -> {args.output}")
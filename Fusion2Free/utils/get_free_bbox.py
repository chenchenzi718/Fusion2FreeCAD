"""
Bounding-box computation -- extract the combined bounding box from a FreeCAD .FCStd file
and write it back to the source Fusion 360 JSON.

Requires FreeCAD to be importable at runtime (set FREECAD_LIB environment variable).
"""

import json
import os
import sys

from fusion2free.utils.config import FREECAD_LIB_PATH

if FREECAD_LIB_PATH not in sys.path:
    sys.path.append(FREECAD_LIB_PATH)
os.environ["FREECAD_LIB"] = FREECAD_LIB_PATH

import FreeCAD as App
import FreeCAD

from fusion2free.utils.load_fusion import load_fusion


def get_combined_bbox(filepath):
    """
    Open a FreeCAD document and compute the combined bounding box of all Bodies.

    Returns a list [XMin, YMin, ZMin, XMax, YMax, ZMax] in mm.
    """
    doc = FreeCAD.open(filepath)
    doc = FreeCAD.ActiveDocument

    combined_bbox = None
    try:
        for obj in doc.Objects:
            if obj.TypeId == "PartDesign::Body":
                shape = obj.Shape
                bbox = shape.BoundBox
                if combined_bbox is None:
                    combined_bbox = bbox
                else:
                    combined_bbox.add(bbox)
    except Exception as e:
        raise RuntimeError(
            f"Error processing bounding box for {filepath}: {e}"
        )
    return [
        combined_bbox.XMin,
        combined_bbox.YMin,
        combined_bbox.ZMin,
        combined_bbox.XMax,
        combined_bbox.YMax,
        combined_bbox.ZMax,
    ]


def setup_to_fusion(bbox_tuple, json_path):
    """
    Write bounding-box values (in mm) back to the source Fusion JSON (converted to meters).
    """
    fusion_json = load_fusion(json_path)
    fusion_json["properties"]["bounding_box"]["min_point"]["x"] = bbox_tuple[0] / 1000.0
    fusion_json["properties"]["bounding_box"]["min_point"]["y"] = bbox_tuple[1] / 1000.0
    fusion_json["properties"]["bounding_box"]["min_point"]["z"] = bbox_tuple[2] / 1000.0
    fusion_json["properties"]["bounding_box"]["max_point"]["x"] = bbox_tuple[3] / 1000.0
    fusion_json["properties"]["bounding_box"]["max_point"]["y"] = bbox_tuple[4] / 1000.0
    fusion_json["properties"]["bounding_box"]["max_point"]["z"] = bbox_tuple[5] / 1000.0
    with open(json_path, "w") as f:
        json.dump(fusion_json, f, indent=4)
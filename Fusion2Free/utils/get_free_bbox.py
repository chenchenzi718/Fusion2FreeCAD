"""
Bounding-box computation -- extract the combined bounding box from a FreeCAD .FCStd file
and write it back to the source Fusion 360 JSON.

Uses FreeCADCmd (subprocess) so it does not require FreeCAD to be importable
in the host Python interpreter.  Set FREECAD_CMD environment variable.
"""

import json
import os
import subprocess
import tempfile

from fusion2free.utils.config import FREECAD_CMD_PATH
from fusion2free.utils.load_fusion import load_fusion


def get_combined_bbox(filepath):
    """
    Open a FreeCAD document and compute the combined bounding box of all Bodies.

    Uses FreeCADCmd subprocess → avoids Python-version conflicts with FreeCAD.pyd.

    Returns a list [XMin, YMin, ZMin, XMax, YMax, ZMax] in mm.
    """
    script = f"""
import json, sys
import FreeCAD
doc = FreeCAD.open(r"{filepath}")
combined = None
for obj in doc.Objects:
    if obj.TypeId == "PartDesign::Body":
        bbox = obj.Shape.BoundBox
        if combined is None:
            combined = bbox
        else:
            combined.add(bbox)
if combined is None:
    sys.exit("No PartDesign::Body found in the document")
result = [combined.XMin, combined.YMin, combined.ZMin,
          combined.XMax, combined.YMax, combined.ZMax]
print("BBOX:" + json.dumps(result), flush=True)
FreeCAD.closeDocument(doc.Name)
"""

    tmp = tempfile.NamedTemporaryFile(suffix=".py", mode="w",
                                       delete=False, encoding="utf-8")
    tmp.write(script)
    tmp.close()

    try:
        result = subprocess.run(
            [FREECAD_CMD_PATH, tmp.name],
            capture_output=True, text=True, timeout=120,
        )
        os.unlink(tmp.name)

        if result.returncode != 0:
            raise RuntimeError(
                f"FreeCADCmd failed for {filepath}: {result.stderr.strip()}"
            )

        # Find the tagged output line — ignore other FreeCAD log noise
        bbox_line = None
        for line in result.stdout.splitlines():
            if line.startswith("BBOX:"):
                bbox_line = line[5:]
                break
        if bbox_line is None:
            raise RuntimeError(f"No BBOX output in stdout for {filepath}")

        bbox_list = json.loads(bbox_line)
        return bbox_list
    except Exception as e:
        if os.path.exists(tmp.name):
            os.unlink(tmp.name)
        raise RuntimeError(f"Error processing bounding box for {filepath}: {e}")


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
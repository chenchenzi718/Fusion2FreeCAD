"""
FreeCAD script generation -- generates FreeCAD Python API calls.

These functions produce string fragments that, when concatenated, form a
complete FreeCAD Python script. Coordinates are in meters (DeepCAD)
and are multiplied by 1000 to convert to mm (FreeCAD convention).

Compatibility notes for FreeCAD 0.21+:
  1. Uses AttachmentSupport instead of Support
  2. Uses correct Part module import
  3. Uses correct API capitalization
"""

import numpy as np

from deepcad2free.utils.config import EOL, RECOMPUTE


# ---------------------------------------------------------------------------
# Coordinate transformation helpers
# ---------------------------------------------------------------------------

def mul_mat(vec, transform):
    """Multiply a vector by the rotation part of a 12-element transform."""
    np_vec = np.array(vec)
    np_transform = np.array(transform[3:], dtype=np.float64).reshape(3, 3)
    return np.dot(np_transform, np_vec)


def move_vec(vec, transform):
    """Subtract the translation part of a transform from a vector."""
    np_vec = np.array(vec)
    np_transform = np.array(transform[:3], dtype=np.float64)
    result = np_vec - np_transform
    return [result[0], result[1], result[2]]


def apply_transform(coord, transform):
    """
    Transform a global-coordinate point or vector into a sketch's local frame.

    Args:
        coord: length-3 list/array of coordinates
        transform: length-12 transform [Tx, Ty, Tz, R00, R01, R02, R10, R11, R12, R20, R21, R22]
    """
    T = np.array(transform[:3], dtype=np.float64)
    R = np.array(
        [
            [transform[3], transform[6], transform[9]],
            [transform[4], transform[7], transform[10]],
            [transform[5], transform[8], transform[11]],
        ],
        dtype=np.float64,
    )
    U, _, Vt = np.linalg.svd(R)
    R_orth = np.dot(U, Vt)
    R_inv = R_orth.T
    global_coord = np.array(coord, dtype=np.float64)
    local_coord = R_inv.dot(global_coord - T)
    local_coord = np.round(local_coord, decimals=14)
    return local_coord


# ---------------------------------------------------------------------------
# FreeCAD geometry generators
# ---------------------------------------------------------------------------

def free_make_line(data_id, all_id, st_pt, ed_pt) -> str:
    """Generate FreeCAD LineSegment call (coords in meters -> mm)."""
    return (
        f'App.ActiveDocument.getObject("{all_id}").addGeometry('
        f'Part.LineSegment('
        f'App.Vector({st_pt[0] * 1000.0:.14f},{st_pt[1] * 1000.0:.14f},{st_pt[2] * 1000.0:.14f}),'
        f'App.Vector({ed_pt[0] * 1000.0:.14f},{ed_pt[1] * 1000.0:.14f},{ed_pt[2] * 1000.0:.14f}),'
        f'),False){EOL}'
    )


def free_make_circle(data_id, all_id, center_pt, normal_vec, radius) -> str:
    """Generate FreeCAD Circle call."""
    return (
        f'App.ActiveDocument.getObject("{all_id}").addGeometry('
        f'Part.Circle('
        f'App.Vector({center_pt[0] * 1000.0:.14f},{center_pt[1] * 1000.0:.14f},{center_pt[2] * 1000.0:.14f}),'
        f'App.Vector({normal_vec[0]:.14f},{normal_vec[1]:.14f},{normal_vec[2]:.14f}),'
        f'{radius * 1000.0:.14f}'
        f'),False){EOL}'
    )


def free_make_arc(data_id, all_id, center_pt, normal_vec, radius, st_angle, ed_angle) -> str:
    """Generate FreeCAD ArcOfCircle call."""
    return (
        f'App.ActiveDocument.getObject("{all_id}").addGeometry('
        f'Part.ArcOfCircle(Part.Circle('
        f'App.Vector({center_pt[0] * 1000.0:.14f},{center_pt[1] * 1000.0:.14f},{center_pt[2] * 1000.0:.14f}),'
        f'App.Vector({normal_vec[0]:.14f},{normal_vec[1]:.14f},{normal_vec[2]:.14f}),'
        f'{radius * 1000.0:.14f}'
        f'),{st_angle},{ed_angle}),False){EOL}'
    )


# ---------------------------------------------------------------------------
# FreeCAD document / body generators
# ---------------------------------------------------------------------------

def free_make_new_doc(data_id) -> str:
    """Create a new FreeCAD document."""
    return f'App.newDocument("{data_id}"){EOL}'


def free_make_bbox(min_pt, max_pt) -> str:
    """Generate bounding box (currently unused in conversion pipeline)."""
    x_len = max_pt[0] - min_pt[0]
    y_len = max_pt[1] - min_pt[1]
    z_len = max_pt[2] - min_pt[2]
    x_min, y_min, z_min = min_pt
    line1 = (
        f'box = Part.makeBox({x_len * 1000.0:.14f}, {y_len * 1000.0:.14f}, '
        f'{z_len * 1000.0:.14f}, '
        f'App.Vector({x_min * 1000.0:.14f}, {y_min * 1000.0:.14f}, {z_min * 1000.0:.14f}))'
    )
    line2 = 'bbox_obj = App.ActiveDocument.addObject("Part::Feature", "DocumentBoundingBox")'
    line3 = "bbox_obj.Shape = box"
    return f"{line1}{EOL}{line2}{EOL}{line3}{EOL}"


def free_make_new_body(deepcad_sketch_id, deepcad_extrude_id) -> str:
    """Create a new PartDesign Body."""
    body_name = f"Body_{deepcad_sketch_id}"
    line1 = f'App.ActiveDocument.addObject("PartDesign::Body","{body_name}")'
    line2 = f'App.ActiveDocument.getObject("{body_name}").Label = "{body_name}"'
    return f"{line1}{EOL}{line2}{EOL}{RECOMPUTE}{EOL}"


# ---------------------------------------------------------------------------
# PartDesign Pad / Pocket
# ---------------------------------------------------------------------------

def free_pad(extrude_parameter, data_id, deepcad_extrude_id, deepcad_sketch_id, profile_id, now_body) -> str:
    """Generate PartDesign::Pad code."""
    body_name = now_body
    pad_name = f"Extrude_{deepcad_sketch_id}_{deepcad_extrude_id}_{profile_id}"
    sketch_ref = f"Sketch_{deepcad_sketch_id}_{profile_id}"
    ret_str = ""
    line0 = f'App.ActiveDocument.getObject("{body_name}").newObject("PartDesign::Pad","{pad_name}")'
    line1 = f'App.ActiveDocument.getObject("{pad_name}").Profile = App.ActiveDocument.getObject("{sketch_ref}")'
    e_len1 = extrude_parameter["extent_one"]["distance"]["value"] * 1000.0
    e_len2 = extrude_parameter["extent_two"]["distance"]["value"] * 1000.0
    ret_str += f"{line0}{EOL}{line1}{EOL}"

    if extrude_parameter["extent_type"] == "SymmetricFeatureExtentType":
        e_len1 *= 2
        ret_str += _pad_props(pad_name, e_len1, 0, "0", sketch_ref, "Midplane = 1")
    elif extrude_parameter["extent_type"] == "OneSideFeatureExtentType":
        if e_len1 < 0:
            e_len1 = -e_len1
            ret_str += _pad_props(pad_name, e_len1, 0, "1", sketch_ref, "Midplane = 0")
        else:
            extra = ""
            if e_len2 > 0:
                extra = (
                    f'App.ActiveDocument.getObject("{pad_name}").Length2 = {e_len2}{EOL}'
                    f'App.ActiveDocument.getObject("{pad_name}").TaperAngle2 = 0.000000{EOL}'
                )
            ret_str += _pad_props(pad_name, e_len1, 4, "0", sketch_ref, "Midplane = 0", extra=extra)
    elif extrude_parameter["extent_type"] == "TwoSidesFeatureExtentType":
        extra = ""
        if e_len2 > 0:
            extra = (
                f'App.ActiveDocument.getObject("{pad_name}").Length2 = {e_len2}{EOL}'
                f'App.ActiveDocument.getObject("{pad_name}").TaperAngle2 = 0.000000{EOL}'
            )
        ret_str += _pad_props(pad_name, e_len1, 4, "0", sketch_ref, "Midplane = 0", extra=extra)
    else:
        raise NotImplementedError(
            f'Extent Type: {extrude_parameter["extent_type"]} is not implemented'
        )
    return ret_str


def _pad_props(name, length, type_val, reversed_val, sketch_ref, midplane, extra=""):
    """Build common Pad property assignments."""
    return (
        f'App.ActiveDocument.getObject("{name}").Length = {length}{EOL}'
        f'App.ActiveDocument.getObject("{name}").TaperAngle = 0.000000{EOL}'
        f'App.ActiveDocument.getObject("{name}").UseCustomVector = 0{EOL}'
        f'App.ActiveDocument.getObject("{name}").Direction = (0, 0, 1){EOL}'
        f'App.ActiveDocument.getObject("{name}").ReferenceAxis = '
        f'(App.ActiveDocument.getObject("{sketch_ref}"), ["N_Axis"]){EOL}'
        f'App.ActiveDocument.getObject("{name}").AlongSketchNormal = 1{EOL}'
        f'App.ActiveDocument.getObject("{name}").Type = {type_val}{EOL}'
        f'App.ActiveDocument.getObject("{name}").UpToFace = None{EOL}'
        f'App.ActiveDocument.getObject("{name}").Reversed = {reversed_val}{EOL}'
        f'App.ActiveDocument.getObject("{name}").{midplane}{EOL}'
        f'App.ActiveDocument.getObject("{name}").Offset = 0{EOL}'
    )


def free_pocket(extrude_parameter, data_id, deepcad_extrude_id, deepcad_sketch_id, profile_id, now_body):
    """Generate PartDesign::Pocket code."""
    body_name = now_body
    pocket_name = f"Extrude_{deepcad_sketch_id}_{deepcad_extrude_id}_{profile_id}"
    sketch_ref = f"Sketch_{deepcad_sketch_id}_{profile_id}"
    ret_str = ""
    line0 = f'App.ActiveDocument.getObject("{body_name}").newObject("PartDesign::Pocket","{pocket_name}")'
    line1 = f'App.ActiveDocument.getObject("{pocket_name}").Profile = App.ActiveDocument.getObject("{sketch_ref}")'
    e_len1 = extrude_parameter["extent_one"]["distance"]["value"] * 1000.0
    e_len2 = extrude_parameter["extent_two"]["distance"]["value"] * 1000.0
    e_len1 = -e_len1
    e_len2 = -e_len2
    ret_str += f"{line0}{EOL}{line1}{EOL}"

    if extrude_parameter["extent_type"] == "SymmetricFeatureExtentType":
        e_len1 *= 2
        ret_str += _pocket_props(pocket_name, e_len1, 0, "0", sketch_ref, "Midplane = 1")
    elif extrude_parameter["extent_type"] == "OneSideFeatureExtentType":
        if e_len1 < 0:
            e_len1 = -e_len1
            ret_str += _pocket_props(pocket_name, e_len1, 0, "1", sketch_ref, "Midplane = 0")
        else:
            extra = ""
            if e_len2 < 0:
                extra = (
                    f'App.ActiveDocument.getObject("{pocket_name}").Length2 = {e_len2}{EOL}'
                    f'App.ActiveDocument.getObject("{pocket_name}").TaperAngle2 = 0.000000{EOL}'
                )
            ret_str += _pocket_props(pocket_name, e_len1, 4, "0", sketch_ref, "Midplane = 0", extra=extra)
    elif extrude_parameter["extent_type"] == "TwoSidesFeatureExtentType":
        extra = ""
        if e_len2 < 0:
            extra = (
                f'App.ActiveDocument.getObject("{pocket_name}").Length2 = {e_len2}{EOL}'
                f'App.ActiveDocument.getObject("{pocket_name}").TaperAngle2 = 0.000000{EOL}'
            )
        ret_str += _pocket_props(pocket_name, e_len1, 4, "0", sketch_ref, "Midplane = 0", extra=extra)
    else:
        raise NotImplementedError(
            f'Extent Type: {extrude_parameter["extent_type"]} is not implemented'
        )
    return ret_str


def _pocket_props(name, length, type_val, reversed_val, sketch_ref, midplane, extra=""):
    """Build common Pocket property assignments."""
    return (
        f'App.ActiveDocument.getObject("{name}").Length = {length}{EOL}'
        f'App.ActiveDocument.getObject("{name}").TaperAngle = 0.000000{EOL}'
        f'App.ActiveDocument.getObject("{name}").UseCustomVector = 0{EOL}'
        f'App.ActiveDocument.getObject("{name}").Direction = (0, 0, -1){EOL}'
        f'App.ActiveDocument.getObject("{name}").ReferenceAxis = '
        f'(App.ActiveDocument.getObject("{sketch_ref}"), ["N_Axis"]){EOL}'
        f'App.ActiveDocument.getObject("{name}").AlongSketchNormal = 1{EOL}'
        f'App.ActiveDocument.getObject("{name}").Type = {type_val}{EOL}'
        f'App.ActiveDocument.getObject("{name}").UpToFace = None{EOL}'
        f'App.ActiveDocument.getObject("{name}").Reversed = {reversed_val}{EOL}'
        f'App.ActiveDocument.getObject("{name}").{midplane}{EOL}'
        f'App.ActiveDocument.getObject("{name}").Offset = 0{EOL}'
    )


def free_make_extrude(boolean_operation, extrude_parameter, data_id, deepcad_extrude_id,
                      deepcad_sketch_id, loop_id, now_body) -> str:
    """Dispatch to free_pad or free_pocket based on boolean operation type."""
    if boolean_operation in ("NewBodyFeatureOperation", "JoinFeatureOperation"):
        return free_pad(extrude_parameter, data_id, deepcad_extrude_id,
                        deepcad_sketch_id, loop_id, now_body)
    elif boolean_operation == "CutFeatureOperation":
        return free_pocket(extrude_parameter, data_id, deepcad_extrude_id,
                           deepcad_sketch_id, loop_id, now_body)
    else:
        raise NotImplementedError(
            f"Boolean operation '{boolean_operation}' is not supported."
        )


# ---------------------------------------------------------------------------
# Sketch
# ---------------------------------------------------------------------------

def free_make_new_sketch(data_id, deepcad_extrude_id, deepcad_sketch_id, profile_id,
                         operation_list, transform, now_body_name) -> str:
    """Generate a new sketch with geometry inside a PartDesign Body."""
    sketch_name = f"Sketch_{deepcad_sketch_id}_{profile_id}"
    body_name = now_body_name

    line_plane = (
        f'plane = App.ActiveDocument.getObject("{body_name}").newObject('
        f'"PartDesign::Plane", "plane_{sketch_name}")'
    )
    origin_vector_str = (
        f'origin = App.Vector({transform[0] * 1000.0:.14f},'
        f'{transform[1] * 1000.0:.14f},{transform[2] * 1000.0:.14f})'
    )
    x_axis_vector_str = (
        f'x_axis=App.Vector({transform[3]:.14f},{transform[4]:.14f},{transform[5]:.14f})'
    )
    y_axis_vector_str = (
        f'y_axis=App.Vector({transform[6]:.14f},{transform[7]:.14f},{transform[8]:.14f})'
    )
    z_axis_vector_str = (
        f'z_axis=App.Vector({transform[9]:.14f},{transform[10]:.14f},{transform[11]:.14f})'
    )
    rot_vector_str = "rot = App.Rotation(x_axis,y_axis,z_axis)"
    place_vector_str = (
        f'App.ActiveDocument.getObject("plane_{sketch_name}").Placement = '
        f"App.Placement(origin,rot)"
    )
    line1 = (
        f'App.ActiveDocument.getObject("{body_name}").newObject('
        f'"Sketcher::SketchObject","{sketch_name}")'
    )
    line2 = (
        f'App.ActiveDocument.getObject("{sketch_name}").AttachmentSupport = '
        f'(App.ActiveDocument.getObject("plane_{sketch_name}"), [""])'
    )
    line3 = f'App.ActiveDocument.getObject("{sketch_name}").MapMode = "FlatFace"'

    prepare_str = (
        f"{line_plane}{EOL}{origin_vector_str}{EOL}{x_axis_vector_str}{EOL}"
        f"{y_axis_vector_str}{EOL}{z_axis_vector_str}{EOL}{rot_vector_str}{EOL}"
        f"{place_vector_str}{EOL}{line1}{EOL}{line2}{EOL}{line3}{EOL}"
    )

    operation_str = ""
    for operation in operation_list:
        if operation["type"] == "Line":
            st_pt = operation["st_pt"]
            ed_pt = operation["ed_pt"]
            operation_str += free_make_line(data_id, sketch_name, st_pt, ed_pt)
            operation_str += EOL
        elif operation["type"] == "Circle":
            center_pt = operation["center_pt"]
            normal = operation["normal"]
            operation_str += free_make_circle(
                data_id, sketch_name, center_pt, normal, operation["radius"]
            )
            operation_str += EOL
        elif operation["type"] == "Arc":
            center_pt = operation["center_pt"]
            normal = operation["normal"]
            operation_str += free_make_arc(
                data_id, sketch_name, center_pt, normal,
                operation["radius"], operation["st_angle"], operation["ed_angle"],
            )
            operation_str += EOL

    detect_str = (
        f'detect_cnt=App.ActiveDocument.getObject("{sketch_name}").'
        f'detectMissingPointOnPointConstraints(){EOL}'
    )
    fix_str = (
        f'(App.ActiveDocument.getObject("{sketch_name}").'
        f'makeMissingPointOnPointCoincident()) if detect_cnt>0 else None{EOL}'
    )

    return f"{prepare_str}{operation_str}{RECOMPUTE}{detect_str}{fix_str}{RECOMPUTE}"


def select_active_doc(data_id):
    """Set the active document."""
    return f'App.setActiveDocument("{data_id}"){EOL}App.ActiveDocument=App.ActiveDocument{EOL}'
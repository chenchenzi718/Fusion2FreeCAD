"""
Core conversion engine -- DeepCAD JSON -> FreeCAD Python script.

Converts DeepCAD serialized model representations into
executable FreeCAD Python scripts that rebuild the same parametric model.

Supported operations:
  - Sketch: Line3D, Arc3D, Circle3D
  - ExtrudeFeature: NewBodyFeatureOperation, JoinFeatureOperation, CutFeatureOperation

Not supported:
  - IntersectFeatureOperation
  - Revolve, Sweep, Loft, and other features
"""

import math
import os

from deepcad2free.utils.config import NAME_DB_PATH, EOL, RECOMPUTE
from deepcad2free.utils.free_operation import (
    free_make_extrude,
    free_make_new_body,
    free_make_new_doc,
    free_make_new_sketch,
    mul_mat,
)
from deepcad2free.utils.load_deepcad import load_deepcad
from deepcad2free.utils.naming_utils import FreeCADNameEncoder


# Global encoder instance (SQLite-backed, persisted as name_mapping.db)
_encoder = FreeCADNameEncoder(NAME_DB_PATH)


def init_db(db_path):
    """Initialize or replace the name encoder database."""
    global _encoder
    _encoder = FreeCADNameEncoder(db_path)


# Use the module-level encoder
encoder = _encoder


def angle_deepcad_2_free(swept_angle, reference_vec, normal_vec):
    """
    Convert arc angles from DeepCAD convention to FreeCAD convention.
    """
    normal_z = normal_vec[2]
    if normal_z < 0:
        swept_angle = -swept_angle
        reference_vec[0] = -reference_vec[0]

    theta_ref = math.atan2(reference_vec[1], reference_vec[0])
    if theta_ref < 0:
        theta_ref += 2 * math.pi

    start_angle_in_FreeCAD = theta_ref
    end_angle_in_FreeCAD = (theta_ref + swept_angle) % (2 * math.pi)

    if swept_angle < 0:
        start_angle_in_FreeCAD, end_angle_in_FreeCAD = (
            end_angle_in_FreeCAD,
            start_angle_in_FreeCAD,
        )

    start_angle_in_FreeCAD = round(start_angle_in_FreeCAD, 14)
    end_angle_in_FreeCAD = round(end_angle_in_FreeCAD, 14)

    return start_angle_in_FreeCAD, end_angle_in_FreeCAD


def _get_encoder_name(encoder, deepcad_id):
    """Look up encoded name; fall back to a safe replacement."""
    result = encoder.decode_name_deepcad2free(deepcad_id)
    if result is None:
        return deepcad_id.replace(":", "_").replace("/", "_")
    return result


def deepcad2free(data_id, deepcad_json):
    """
    Convert a DeepCAD JSON model to a FreeCAD Python script string.

    Args:
        data_id: model identifier (used as document name)
        deepcad_json: parsed DeepCAD JSON dict

    Returns:
        (ret_str, Free_str, error_code)
            ret_str:     the complete FreeCAD Python script
            Free_str:    abbreviated operation sequence (e.g. 'SNSCSCSC')
            error_code:  empty string on success, error description on failure
    """
    Free_str = ""
    error_code = ""

    sol = (
        f"import FreeCAD as App{EOL}"
        f"import Part{EOL}"
    )
    ret_str = sol

    seq_list = deepcad_json["sequence"]
    entry_dict = deepcad_json["entities"]

    sketch_dict = {}
    ret_str += free_make_new_doc(data_id)

    now_body = ""

    for op_info in seq_list:
        op_name = op_info["entity"]
        op_type = op_info["type"]

        if op_type == "ExtrudeFeature":
            deepcad_extrude_parameter = entry_dict[op_name]
            extrude_profile_list = deepcad_extrude_parameter["profiles"]
            if len(extrude_profile_list) == 0:
                error_code = "EMPTY EXTRUDE PROFILE"
                continue

            extrude_boolean_op = deepcad_extrude_parameter["operation"]
            deepcad_sketch_id = deepcad_extrude_parameter["profiles"][0]["sketch"]
            deepcad_sketch_id_enc = _get_encoder_name(encoder, deepcad_sketch_id)
            deepcad_extrude_id_enc = _get_encoder_name(encoder, op_name)

            if extrude_boolean_op == "NewBodyFeatureOperation":
                body_name = f"Body_{deepcad_sketch_id_enc}"
                now_body = body_name
                ret_str += free_make_new_body(deepcad_sketch_id_enc, deepcad_extrude_id_enc)

                for index, profile in enumerate(extrude_profile_list):
                    sketch_name = profile["sketch"]
                    loop_name = profile["profile"]
                    loop_name_enc = _get_encoder_name(encoder, loop_name)
                    extrude_op_name_enc = _get_encoder_name(encoder, op_name)

                    ret_str += free_make_new_sketch(
                        data_id, deepcad_extrude_id_enc, deepcad_sketch_id_enc,
                        loop_name_enc,
                        sketch_dict[sketch_name]["profile"][loop_name],
                        sketch_dict[sketch_name]["transform"],
                        now_body,
                    )
                    Free_str += "S"
                    if index == 0:
                        Free_str += "N"
                    else:
                        Free_str += "J"

                    ret_str += free_make_extrude(
                        extrude_boolean_op,
                        deepcad_extrude_parameter,
                        data_id,
                        extrude_op_name_enc,
                        deepcad_sketch_id_enc,
                        loop_name_enc,
                        now_body,
                    )
                    ret_str += RECOMPUTE

            elif extrude_boolean_op == "JoinFeatureOperation":
                for profile in extrude_profile_list:
                    sketch_name = profile["sketch"]
                    loop_name = profile["profile"]
                    loop_name_enc = _get_encoder_name(encoder, loop_name)
                    extrude_op_name_enc = _get_encoder_name(encoder, op_name)

                    ret_str += free_make_new_sketch(
                        data_id, deepcad_extrude_id_enc, deepcad_sketch_id_enc,
                        loop_name_enc,
                        sketch_dict[sketch_name]["profile"][loop_name],
                        sketch_dict[sketch_name]["transform"],
                        now_body,
                    )
                    Free_str += "S"
                    ret_str += free_make_extrude(
                        extrude_boolean_op,
                        deepcad_extrude_parameter,
                        data_id,
                        extrude_op_name_enc,
                        deepcad_sketch_id_enc,
                        loop_name_enc,
                        now_body,
                    )
                    Free_str += "J"
                    ret_str += RECOMPUTE

            elif extrude_boolean_op == "CutFeatureOperation":
                for profile in extrude_profile_list:
                    sketch_name = profile["sketch"]
                    loop_name = profile["profile"]
                    loop_name_enc = _get_encoder_name(encoder, loop_name)
                    extrude_op_name_enc = _get_encoder_name(encoder, op_name)

                    ret_str += free_make_new_sketch(
                        data_id, deepcad_extrude_id_enc, deepcad_sketch_id_enc,
                        loop_name_enc,
                        sketch_dict[sketch_name]["profile"][loop_name],
                        sketch_dict[sketch_name]["transform"],
                        now_body,
                    )
                    Free_str += "S"
                    ret_str += free_make_extrude(
                        extrude_boolean_op,
                        deepcad_extrude_parameter,
                        data_id,
                        extrude_op_name_enc,
                        deepcad_sketch_id_enc,
                        loop_name_enc,
                        now_body,
                    )
                    Free_str += "C"
                    ret_str += RECOMPUTE

            elif extrude_boolean_op == "IntersectFeatureOperation":
                raise NotImplementedError(
                    f"Boolean operation '{extrude_boolean_op}' is not implemented"
                )
            else:
                raise NotImplementedError(
                    f"Boolean operation '{extrude_boolean_op}' is not implemented"
                )

        elif op_type == "Sketch":
            sketch_dict[op_name] = {}
            transform_src = entry_dict[op_name]["transform"]
            keys = ["origin", "x_axis", "y_axis", "z_axis"]
            transform_list = [
                transform_src[key][axis]
                for key in keys
                for axis in ["x", "y", "z"]
            ]
            sketch_dict[op_name]["transform"] = transform_list

            profile_dict = entry_dict[op_name]["profiles"]
            if len(profile_dict) == 0:
                error_code = "EMPTY SKETCH"
                continue

            for key, val in profile_dict.items():
                loops_list = val["loops"]
                sket_list = []
                for loops in loops_list:
                    curve_list = loops["profile_curves"]
                    for curve in curve_list:
                        curve_type = curve["type"]

                        if curve_type == "Line3D":
                            st_pt = [curve["start_point"][axis] for axis in ["x", "y", "z"]]
                            ed_pt = [curve["end_point"][axis] for axis in ["x", "y", "z"]]
                            curve_info_dict = {
                                "type": "Line",
                                "st_pt": st_pt,
                                "ed_pt": ed_pt,
                            }
                        elif curve_type == "Arc3D":
                            radius = curve["radius"]
                            swept_angle = curve["end_angle"]
                            center_pt = [curve["center_point"][axis] for axis in ["x", "y", "z"]]
                            normal = [curve["normal"][axis] for axis in ["x", "y", "z"]]
                            reference_vec = [
                                curve["reference_vector"][axis] for axis in ["x", "y", "z"]
                            ]

                            normal = mul_mat(normal, transform_list)

                            start_angle, end_angle = angle_deepcad_2_free(
                                swept_angle, reference_vec, normal_vec=normal
                            )

                            curve_info_dict = {
                                "type": "Arc",
                                "center_pt": center_pt,
                                "radius": radius,
                                "st_angle": start_angle,
                                "ed_angle": end_angle,
                                "normal": normal,
                            }
                        elif curve_type == "Circle3D":
                            center_pt = [curve["center_point"][axis] for axis in ["x", "y", "z"]]
                            radius = curve["radius"]
                            normal = [curve["normal"][axis] for axis in ["x", "y", "z"]]
                            normal = mul_mat(normal, transform_list)
                            curve_info_dict = {
                                "type": "Circle",
                                "center_pt": center_pt,
                                "radius": radius,
                                "normal": normal,
                            }
                        else:
                            raise NotImplementedError(
                                f"Curve type '{curve_type}' is not implemented"
                            )
                        sket_list.append(curve_info_dict)
                profile_dict[key] = sket_list
            sketch_dict[op_name]["profile"] = profile_dict
        else:
            raise NotImplementedError(f"Operation type '{op_type}' is not implemented")

    return ret_str, Free_str, error_code


if __name__ == "__main__":
    from deepcad2free.utils.config import INPUT_DIR

    # Quick test: convert a single model
    test_path = os.path.join(INPUT_DIR, "0000/00000007.json")
    if os.path.exists(test_path):
        deepcad_json = load_deepcad(test_path)
        data_id = "00000007"
        free_str, _, _ = deepcad2free(data_id, deepcad_json)
        print(free_str)
    else:
        print(f"Test file not found: {test_path}")
import math
import os
from math import radians
from typing import OrderedDict

from numpy.ma.core import empty

from utils.define import SOL
from utils.free_opeartion import *
from utils.load_fusion import load_fusion
from utils.naming_utils import FreeCADNameEncoder

empty_sketch = set()
empty_profile_list = set()
has_intersection = []
check_mode = False


def init_db(db_path):
    return FreeCADNameEncoder(db_path)


encoder = init_db('utils/name_mapping.db')


def angle_fusion_2_free(swept_angle, reference_vec, normal_vec):
    # 计算参考角度，确保角度在 [0, 2π) 范围内
    # 尝试根据法线方向，reference_vec的方向也变一下
    # 根据法向量方向调整扫过角度
    normal_z = normal_vec[2]

    if normal_z < 0:
        swept_angle = -swept_angle
        reference_vec[0] = -reference_vec[0]
        # reference_vec[1] = -reference_vec[1]
    theta_ref = math.atan2(reference_vec[1], reference_vec[0])
    if theta_ref < 0:
        theta_ref += 2 * math.pi

    # 获取法向量的方向



    # 计算结束角度
    start_angle_in_FreeCAD = theta_ref
    end_angle_in_FreeCAD = (theta_ref + swept_angle) % (2 * math.pi)

    # 检查并调整角度方向，确保起始角度和结束角度一致
    if swept_angle < 0:
        start_angle_in_FreeCAD, end_angle_in_FreeCAD = end_angle_in_FreeCAD, start_angle_in_FreeCAD

    # 限制角度的精度
    start_angle_in_FreeCAD = round(start_angle_in_FreeCAD, 14)
    end_angle_in_FreeCAD = round(end_angle_in_FreeCAD, 14)

    return start_angle_in_FreeCAD, end_angle_in_FreeCAD




def fusion2free(data_id, fusion_json):
    Free_str: str = ''
    error_code = ''
    ret_str = SOL
    seq_list = fusion_json['sequence']
    entry_dict = fusion_json['entities']
    bbox_fusion = fusion_json['properties']['bounding_box']
    sketch_dict = {}
    # new doc
    ret_str += free_make_new_doc(data_id)
    # bbox:
    keys_bbox = ['min_point', 'max_point']
    body_2_sketch, sketch_2_body = {}, {}
    bbox_list = [bbox_fusion[key][axis] for key in keys_bbox for axis in ['x', 'y', 'z']]
    # ret_str += free_make_bbox(bbox_list[:3], bbox_list[3:])
    now_body = ''
    for op_info in seq_list:
        # print(ret_str)
        op_name = op_info['entity']
        op_type = op_info['type']
        if op_type == 'ExtrudeFeature':
            # start operation
            # new body->new sketch -> new extrude
            fusion_extrude_parameter = entry_dict[op_name]
            extrude_profile_list = fusion_extrude_parameter['profiles']
            if len(extrude_profile_list) == 0:
                error_code = "EMPTY EXTRUDE PROFILE"
                continue
            extrude_boolean_op = fusion_extrude_parameter['operation']
            fusion_sketch_id = fusion_extrude_parameter['profiles'][0]['sketch']
            fusion_sketch_id_enc = encoder.decode_name_fusion2free(fusion_sketch_id)
            # fys+处理 encoder.decode_name_fusion2free 返回 None 的情况
            if fusion_sketch_id_enc is None:
                fusion_sketch_id_enc = fusion_sketch_id.replace(':', '_').replace('/', '_')
            fusion_extrude_id_enc = encoder.decode_name_fusion2free(op_name)
            # fys+处理 encoder.decode_name_fusion2free 返回 None 的情况
            if fusion_extrude_id_enc is None:
                fusion_extrude_id_enc = op_name.replace(':', '_').replace('/', '_')

            if extrude_boolean_op == 'NewBodyFeatureOperation':
                # new body (sketch)
                body_name = f'Body_{fusion_sketch_id_enc}'
                now_body = body_name
                ret_str += free_make_new_body(fusion_sketch_id_enc, fusion_extrude_id_enc)
                sketch_2_body[fusion_sketch_id] = f'Body_{fusion_sketch_id_enc}'
                # for loop create sketch

                # sketch 2 body dict
                # generate extrude (extrude,sketch,loop)
                if len(extrude_profile_list) == 0:
                    error_code = "EMPTY EXTRUDE PROFILE"
                    continue
                for index, profile in enumerate(extrude_profile_list):
                    sketch_name = profile['sketch']
                    loop_name = profile['profile']
                    loop_name_enc = encoder.decode_name_fusion2free(loop_name)
                    # fys+处理 encoder.decode_name_fusion2free 返回 None 的情况
                    if loop_name_enc is None:
                        loop_name_enc = loop_name.replace(':', '_').replace('/', '_')
                    extrude_parameter = {}
                    extrude_op_name_enc = encoder.decode_name_fusion2free(op_name)
                    # fys+处理 encoder.decode_name_fusion2free 返回 None 的情况
                    if extrude_op_name_enc is None:
                        extrude_op_name_enc = op_name.replace(':', '_').replace('/', '_')
                    ret_str += free_make_new_sketch(data_id, fusion_extrude_id_enc, fusion_sketch_id_enc, loop_name_enc,
                                                    sketch_dict[sketch_name]['profile'][loop_name],
                                                    sketch_dict[sketch_name]['transform'], now_body)

                    Free_str += 'S'

                    if index == 0:
                        Free_str += 'N'
                    else:
                        Free_str += 'J'
                        # extrude_boolean_op = 'JoinFeatureOperation'
                    ret_str += free_make_extrude(
                        extrude_boolean_op,
                        fusion_extrude_parameter,
                        data_id,
                        extrude_op_name_enc,
                        fusion_sketch_id_enc,
                        loop_name_enc,
                        now_body
                    )

                    ret_str += RECOMPUTE
            elif extrude_boolean_op == 'JoinFeatureOperation':
                # for loop create sketch

                # find sketch 2 body dict:select the body
                # generate extrude (extrude,sketch,loop)
                for profile in extrude_profile_list:
                    sketch_name = profile['sketch']
                    loop_name = profile['profile']
                    loop_name_enc = encoder.decode_name_fusion2free(loop_name)
                    if loop_name_enc is None:
                        loop_name_enc = loop_name.replace(':', '_').replace('/', '_')
                    extrude_op_name_enc = encoder.decode_name_fusion2free(op_name)
                    if extrude_op_name_enc is None:
                        extrude_op_name_enc = op_name.replace(':', '_').replace('/', '_')

                    ret_str += free_make_new_sketch(data_id, fusion_extrude_id_enc, fusion_sketch_id_enc, loop_name_enc,
                                                    sketch_dict[sketch_name]['profile'][loop_name],
                                                    sketch_dict[sketch_name]['transform'], now_body)
                    Free_str += 'S'
                    ret_str += free_make_extrude(
                        extrude_boolean_op,
                        fusion_extrude_parameter,
                        data_id,
                        extrude_op_name_enc,
                        fusion_sketch_id_enc,
                        loop_name_enc, now_body
                    )
                    Free_str += 'J'
                    ret_str += RECOMPUTE

            elif extrude_boolean_op == 'CutFeatureOperation':
                # for loop create sketch
                # find sketch 2 body dict:select the body
                # generate extrude (extrude,sketch,loop)
                for profile in extrude_profile_list:
                    sketch_name = profile['sketch']
                    loop_name = profile['profile']
                    loop_name_enc = encoder.decode_name_fusion2free(loop_name)
                    if loop_name_enc is None:
                        loop_name_enc = loop_name.replace(':', '_').replace('/', '_')
                    extrude_op_name_enc = encoder.decode_name_fusion2free(op_name)
                    if extrude_op_name_enc is None:
                        extrude_op_name_enc = op_name.replace(':', '_').replace('/', '_')
                    ret_str += free_make_new_sketch(data_id, fusion_extrude_id_enc, fusion_sketch_id_enc, loop_name_enc,
                                                    sketch_dict[sketch_name]['profile'][loop_name],
                                                    sketch_dict[sketch_name]['transform'], now_body)
                    Free_str += 'S'
                    ret_str += free_make_extrude(
                        extrude_boolean_op,
                        fusion_extrude_parameter,
                        data_id,
                        extrude_op_name_enc,
                        fusion_sketch_id_enc,
                        loop_name_enc, now_body
                    )
                    Free_str += 'C'
                    ret_str += RECOMPUTE

            elif extrude_boolean_op == 'IntersectFeatureOperation':
                raise NotImplementedError(f'extrude_boolean_op {extrude_boolean_op} not implemented')
            else:
                raise NotImplementedError(f'extrude_boolean_op {extrude_boolean_op} not implemented')

        elif op_type == 'Sketch':
            # save info to dict
            # deal transform
            sketch_dict[op_name] = {}
            fusion_transform = entry_dict[op_name]['transform']
            keys = ['origin', 'x_axis', 'y_axis', 'z_axis']
            transform_list = [fusion_transform[key][axis] for key in keys for axis in ['x', 'y', 'z']]
            # deal curve
            sketch_dict[op_name]['transform'] = transform_list
            profile_dict = entry_dict[op_name]['profiles']
            # profile_dict = {}
            # detect length of loop_dict is 0
            if len(profile_dict) == 0:
                empty_sketch.add(data_id)
                error_code = "EMPTY SKETCH"
                continue
            for key, val in profile_dict.items():
                loops_list = val['loops']
                sket_list = []
                for loops in loops_list:
                    curve_list = loops['profile_curves']
                    for curve in curve_list:
                        curve_type = curve['type']

                        if curve_type == 'Line3D':
                            st_pt = [curve['start_point'][axis] for axis in ['x', 'y', 'z']]
                            ed_pt = [curve['end_point'][axis] for axis in ['x', 'y', 'z']]
                            curve_info_dict = {'type': 'Line', 'st_pt': st_pt, 'ed_pt': ed_pt}
                        elif curve_type == 'Arc3D':
                            radius = curve['radius']
                            swept_angle = curve['end_angle']
                            center_pt = [curve['center_point'][axis] for axis in ['x', 'y', 'z']]
                            normal = [curve['normal'][axis] for axis in ['x', 'y', 'z']]
                            reference_vec = [curve['reference_vector'][axis] for axis in ['x', 'y', 'z']]
                            st_pt = [curve['start_point'][axis] for axis in ['x', 'y', 'z']]
                            ed_pt = [curve['end_point'][axis] for axis in ['x', 'y', 'z']]
                            # calculate angle which used in FreeCAD
                            # reference_vec =apply_transform(reference_vec,transform_list)
                            # print(f'normal before:{normal}')
                            normal = mul_mat(normal, transform_list)
                            # print(f'normal after:{normal}')

                            start_angle_in_FreeCAD, end_angle_in_FreeCAD = angle_fusion_2_free(swept_angle,
                                                                                               reference_vec,
                                                                                               normal_vec=normal)
                            # start_angle_in_FreeCAD, end_angle_in_FreeCAD = compute_arc_angles(center_pt, st_pt, ed_pt)

                            curve_info_dict = {'type': 'Arc', 'center_pt': center_pt, 'radius': radius,
                                               'st_angle': start_angle_in_FreeCAD,
                                               'ed_angle': end_angle_in_FreeCAD, 'normal': normal}
                        elif curve_type == 'Circle3D':
                            center_pt = [curve['center_point'][axis] for axis in ['x', 'y', 'z']]
                            radius = curve['radius']
                            normal = [curve['normal'][axis] for axis in ['x', 'y', 'z']]
                            normal = mul_mat(normal, transform_list)
                            curve_info_dict = {'type': 'Circle', 'center_pt': center_pt, 'radius': radius,
                                               'normal': normal}
                        else:
                            raise NotImplementedError(f'curve_type {curve_type} not implemented')
                        sket_list.append(curve_info_dict)
                profile_dict[key] = sket_list
            sketch_dict[op_name]['profile'] = profile_dict
        else:
            raise NotImplementedError(f'op_type {op_type} not implemented')


    return ret_str, Free_str, error_code


if __name__ == '__main__':
    fusion_prefix_path = 'data/cad_json/0092/00923353.json'
    fusion_json = load_fusion(fusion_prefix_path)
    data_id = fusion_prefix_path[-13:-5]
    free_str, _, _ = fusion2free(data_id, fusion_json)
    print(free_str)
    # save in py file
    os.makedirs(f'data/output/{data_id[0:4]}/', exist_ok=True)
    with open(f'data/output/{data_id[0:4]}/{data_id}_free.py', 'w') as f:
        f.write(free_str)

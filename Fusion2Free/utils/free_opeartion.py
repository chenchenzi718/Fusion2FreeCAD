from utils.define import EOL, RECOMPUTE
import numpy as np

# FreeCAD 0.21+ 兼容性说明：
# 1. 使用 AttachmentSupport 替代 Support
# 2. 确保正确导入 Part 模块
# 3. 使用正确的 API 大小写

"""
body_name = f'Body_{fusion_sketch_id}_{fusion_extrude_id}'
Docu Name: f'{data_id}'

Sketch Name: f'Sketch_{fusion_Sketch_id}_{Profile_id}'
Extrude Name: f'Extrude_{fusion_sketch_id}_{fusion_extrude_id}_{Profile_id}''

"""


# def apply_transform(coord, transform):
#     """
#     将全局坐标系的点或向量转换为草图的局部坐标系。
#
#     参数：
#     - coord: 长度为3的列表或数组，表示点或向量的坐标。
#     - transform: 长度为12的列表，表示变换矩阵。
#       格式为：[Tx, Ty, Tz, R00, R01, R02, R10, R11, R12, R20, R21, R22]
#       其中 (Tx, Ty, Tz) 为平移向量, R为3x3旋转矩阵。
#
#     返回：
#     - 长度为3的numpy数组，表示转换后的坐标。
#     """
#
#     # 提取平移和旋转矩阵
#     T = np.array(transform[:3], dtype=np.float64)
#     R = np.array([
#         [transform[3], transform[6], transform[9]],
#         [transform[4], transform[7], transform[10]],
#         [transform[5], transform[8], transform[11]]
#     ], dtype=np.float64)
#
#     # 计算旋转矩阵的逆
#     R_inv = np.linalg.inv(R)
#
#     # 进行坐标变换
#     global_coord = np.array(coord, dtype=np.float64)
#     local_coord = R_inv.dot(global_coord - T)
#
#     # 对结果进行适度的精度控制
#     local_coord = np.round(local_coord, decimals=14)
#
#     return local_coord
def mul_mat(vec, transform):
    np_vec = np.array(vec)
    np_transform = np.array(transform[3:], dtype=np.float64).reshape(3, 3)
    return np.dot(np_transform, np_vec)


def move_vec(vec, transform):
    np_vec = np.array(vec)
    np_transform = np.array(transform[:3], dtype=np.float64)
    result = np_vec - np_transform
    return [result[0], result[1], result[2]]


def apply_transform(coord, transform):
    """
    将全局坐标系的点或向量转换为草图的局部坐标系。

    参数：
    - coord: 长度为3的列表或数组，表示点或向量的坐标。
    - transform: 长度为12的列表，表示变换矩阵。

    返回：
    - 长度为3的numpy数组，表示转换后的坐标。
    """
    T = np.array(transform[:3], dtype=np.float64)
    R = np.array([
        [transform[3], transform[6], transform[9]],
        [transform[4], transform[7], transform[10]],
        [transform[5], transform[8], transform[11]]
    ], dtype=np.float64)

    # 保持高精度进行正交化
    U, _, Vt = np.linalg.svd(R)
    R_orth = np.dot(U, Vt)

    R_inv = R_orth.T  # 使用正交化后的矩阵

    global_coord = np.array(coord, dtype=np.float64)
    local_coord = R_inv.dot(global_coord - T)

    # 延迟舍入到1e-8公差
    local_coord = np.round(local_coord, decimals=14)

    return local_coord


def free_make_line(data_id, all_id, st_pt, ed_pt) -> str:
    """
    App.getDocument('Unnamed1').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(-19.722761,0.000000,0),App.Vector(-0.000000,9.555553,0)),False)
    :return:
    """

    return f'App.ActiveDocument.getObject("{all_id}").addGeometry(Part.LineSegment(App.Vector({st_pt[0] * 1000.0:.14f},{st_pt[1] * 1000.0:.14f},{st_pt[2] * 1000.0:.14f}),App.Vector({ed_pt[0] * 1000.0:.14f},{ed_pt[1] * 1000.0:.14f},{ed_pt[2] * 1000.0:.14f})),False){EOL}'


def free_make_circle(data_id, all_id, center_pt, normal_vec, radius) -> str:
    """
    App.getDocument('Unnamed2').getObject('Sketch').addGeometry(Part.Circle(App.Vector(-30.222219,16.222221,0),App.Vector(0,0,1),48.205444),False)
    :return:
    """

    return f'App.ActiveDocument.getObject("{all_id}").addGeometry(Part.Circle(App.Vector({center_pt[0] * 1000.0:.14f},{center_pt[1] * 1000.0:.14f},{center_pt[2] * 1000.0:.14f}),App.Vector({normal_vec[0]:.14f},{normal_vec[1]:.14f},{normal_vec[2]:.14f}),{radius * 1000.0:.14f}),False){EOL}'


def free_make_arc(data_id, all_id, center_pt, normal_vec, radius, st_angle, ed_angle) -> str:
    """
    App.getDocument('Unnamed1').getObject('Sketch').
    addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-13.888889,13.999998,0),App.Vector(0,0,1),14.582672),-0.309703,4.300812),False)
    :return:
    """
    # no need to transform the radian to angle
    return f'App.ActiveDocument.getObject("{all_id}").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector({center_pt[0] * 1000.0:.14f},{center_pt[1] * 1000.0:.14f},{center_pt[2] * 1000.0:.14f}),App.Vector({normal_vec[0]:.14f},{normal_vec[1]:.14f},{normal_vec[2]:.14f}),{radius * 1000.0:.14f}),{st_angle},{ed_angle}),False){EOL}'


def free_make_new_doc(data_id) -> str:
    """
    App.newDocument()
    App.setActiveDocument("Unnamed2")
    App.ActiveDocument=App.getDocument("Unnamed2")
    """
    line1 = f'App.newDocument("{data_id}")'
    # line2 = f'App.setActiveDocument("{data_id}")'
    # line3 = f'App.ActiveDocument=App.ActiveDocument'

    return f'{line1}{EOL}'


def free_make_bbox(min_pt, max_pt) -> str:
    """
    box = Part.makeBox(x_len, y_len, z_len, App.Vector(x_min, y_min, z_min))

    # 将长方体添加到文档中
    bbox_obj = App.ActiveDocument.addObject("Part::Feature", "DocumentBoundingBox")
    bbox_obj.Shape = box
    :param data_id:
    :param min_pt:
    :param max_pt:
    :return:
    """
    x_len = max_pt[0] - min_pt[0]
    y_len = max_pt[1] - min_pt[1]
    z_len = max_pt[2] - min_pt[2]
    x_min, y_min, z_min = min_pt

    line1 = f'box = Part.makeBox({x_len * 1000.0:.14f}, {y_len * 1000.0:.14f}, {z_len * 1000.0:.14f}, App.Vector({x_min * 1000.0:.14f}, {y_min * 1000.0:.14f}, {z_min * 1000.0:.14f}))'
    line2 = f'bbox_obj = App.ActiveDocument.addObject("Part::Feature", "DocumentBoundingBox")'
    line3 = f'bbox_obj.Shape = box'

    return f'{line1}{EOL}{line2}{EOL}{line3}{EOL}'


def free_make_new_body(fusion_sketch_id, fusion_extrude_id) -> str:
    """
    >>> App.activeDocument().addObject('PartDesign::Body','Body001')
    >>> App.ActiveDocument.getObject('Body001').Label = 'Body'
    """
    body_name = f'Body_{fusion_sketch_id}'
    # make a new body
    line1 = f'App.ActiveDocument.addObject("PartDesign::Body","{body_name}")'
    line2 = f'App.ActiveDocument.getObject("{body_name}").Label = "{body_name}"'
    # make the bbox
    # line3 = f'bbox=App.ActiveDocument.getObject("{body_name}").addObject("Part::Feature", "BoundingBox")'
    # line_bbox = f'bbox.shape=Part.Box(App.Vector({bbox.min.x, bbox.min.y, bbox.min.z}),App.Vector({bbox.max.x, bbox.max.y, bbox.max.z}))'
    # return f'{line1}{EOL}{line2}{EOL}{line3}{EOL}{line_bbox}{EOL}{RECOMPUTE}{EOL}'
    return f'{line1}{EOL}{line2}{EOL}{RECOMPUTE}{EOL}'


def free_pad(extrude_parameter, data_id, fusion_extrude_id, fusion_sketch_id, profile_id, now_body) -> str:
    """
    App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pad','Pad')
>>> App.getDocument('Unnamed').getObject('Pad').Profile = App.getDocument('Unnamed').getObject('Sketch')
>>> App.ActiveDocument.recompute()
>>> App.getDocument('Unnamed').getObject('Pad').Length = 10.000000
>>> App.getDocument('Unnamed').getObject('Pad').Length2 = 8.000000
>>> App.getDocument('Unnamed').getObject('Pad').TaperAngle = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad').TaperAngle2 = 0.000000
>>> App.getDocument('Unnamed').getObject('Pad').UseCustomVector = 0
>>> App.getDocument('Unnamed').getObject('Pad').Direction = (0, 0, 1)
>>> App.getDocument('Unnamed').getObject('Pad').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch'), ['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Pad').AlongSketchNormal = 1
>>> App.getDocument('Unnamed').getObject('Pad').Type = 4
>>> App.getDocument('Unnamed').getObject('Pad').UpToFace = None
>>> App.getDocument('Unnamed').getObject('Pad').Reversed = 0
>>> App.getDocument('Unnamed').getObject('Pad').Midplane = 0
>>> App.getDocument('Unnamed').getObject('Pad').Offset = 0
>>> App.getDocument('Unnamed').recompute()
>>> # Gui.getDocument('Unnamed').resetEdit()
>>> App.getDocument('Unnamed').getObject('Sketch').Visibility = False
    :return:
    """
    body_name = now_body
    pad_name = f'Extrude_{fusion_sketch_id}_{fusion_extrude_id}_{profile_id}'
    ret_str = ''
    line0 = f'App.ActiveDocument.getObject("{body_name}").newObject("PartDesign::Pad","{pad_name}")'
    line1 = f'App.ActiveDocument.getObject("{pad_name}").Profile = App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}")'
    e_len1 = extrude_parameter["extent_one"]["distance"]["value"] * 1000.0
    e_len2 = extrude_parameter["extent_two"]["distance"]["value"] * 1000.0
    ret_str += f'{line0}{EOL}{line1}{EOL}'
    if extrude_parameter['extent_type'] == 'SymmetricFeatureExtentType':
        e_len1 *= 2
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Length = {e_len1}{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").TaperAngle = 0.000000{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").UseCustomVector = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Direction = (0, 0, 1){EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}"), ["N_Axis"]){EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").AlongSketchNormal = 1{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Type = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").UpToFace = None{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Reversed = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Midplane = 1{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Offset = 0{EOL}'
    elif extrude_parameter['extent_type'] == 'OneSideFeatureExtentType':
        if e_len1 < 0:
            e_len1 = -e_len1
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Length = {e_len1}{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").TaperAngle = 0.000000{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").UseCustomVector = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Direction = (0, 0, 1){EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}"), ["N_Axis"]){EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").AlongSketchNormal = 1{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Type = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").UpToFace = None{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Reversed = 1{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Midplane = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Offset = 0{EOL}'
        else:
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Length = {e_len1}{EOL}'
            # fys+添加了条件判断，仅当 Length2 有实际意义时才设置该参数
            if e_len2 > 0:
                ret_str += f'App.ActiveDocument.getObject("{pad_name}").Length2 = {e_len2}{EOL}'
                ret_str += f'App.ActiveDocument.getObject("{pad_name}").TaperAngle2 = 0.000000{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").TaperAngle = 0.000000{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Direction = (0, 0, 1){EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}"), ["N_Axis"]){EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").AlongSketchNormal = 1{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Type = 4{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").UpToFace = None{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Reversed = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Midplane = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Offset = 0{EOL}'
    elif extrude_parameter['extent_type'] == 'TwoSidesFeatureExtentType':
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Length = {e_len1}{EOL}'
        # fys+添加了条件判断，仅当 Length2 有实际意义时才设置该参数
        if e_len2 > 0:
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").Length2 = {e_len2}{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pad_name}").TaperAngle2 = 0.000000{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").TaperAngle = 0.000000{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Direction = (0, 0, 1){EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}"), ["N_Axis"]){EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").AlongSketchNormal = 1{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Type = 4{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").UpToFace = None{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Reversed = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Midplane = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pad_name}").Offset = 0{EOL}'
    else:
        raise NotImplementedError(f'Extent Type: {extrude_parameter["extent_type"]} is not implemented')

    return ret_str


def free_pocket(extrude_parameter, data_id, fusion_extrude_id, fusion_sketch_id, profile_id, now_body):
    """
    >>> App.getDocument('Unnamed').getObject('Body').newObject('PartDesign::Pocket','Pocket')
>>> App.getDocument('Unnamed').getObject('Pocket').Profile = App.getDocument('Unnamed').getObject('Sketch001')
>>> App.ActiveDocument.recompute()
    >>> App.getDocument('Unnamed').getObject('Pocket').Length = 5.000000
>>> App.getDocument('Unnamed').getObject('Pocket').Length2 = 5.000000
>>> App.getDocument('Unnamed').getObject('Pocket').TaperAngle = 0.000000
>>> App.getDocument('Unnamed').getObject('Pocket').TaperAngle2 = 0.000000
>>> App.getDocument('Unnamed').getObject('Pocket').UseCustomVector = 0
>>> App.getDocument('Unnamed').getObject('Pocket').Direction = (0, 0, -1)
>>> App.getDocument('Unnamed').getObject('Pocket').ReferenceAxis = (App.getDocument('Unnamed').getObject('Sketch001'), ['N_Axis'])
>>> App.getDocument('Unnamed').getObject('Pocket').AlongSketchNormal = 1
>>> App.getDocument('Unnamed').getObject('Pocket').Type = 4
>>> App.getDocument('Unnamed').getObject('Pocket').UpToFace = None
>>> App.getDocument('Unnamed').getObject('Pocket').Reversed = 0
>>> App.getDocument('Unnamed').getObject('Pocket').Midplane = 0
>>> App.getDocument('Unnamed').getObject('Pocket').Offset = 0
>>> App.getDocument('Unnamed').recompute()
>>> App.getDocument('Unnamed').getObject('Pad').Visibility = False
    :return:
    """
    body_name = now_body
    pocket_name = f'Extrude_{fusion_sketch_id}_{fusion_extrude_id}_{profile_id}'
    ret_str = ''
    line0 = f'App.ActiveDocument.getObject("{body_name}").newObject("PartDesign::Pocket","{pocket_name}")'
    line1 = f'App.ActiveDocument.getObject("{pocket_name}").Profile = App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}")'
    e_len1 = extrude_parameter["extent_one"]["distance"]["value"] * 1000.0
    e_len2 = extrude_parameter["extent_two"]["distance"]["value"] * 1000.0
    e_len1 = -e_len1
    e_len2 = -e_len2
    ret_str += f'{line0}{EOL}{line1}{EOL}'
    if extrude_parameter['extent_type'] == 'SymmetricFeatureExtentType':
        e_len1 *= 2
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Length = {e_len1}{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").TaperAngle = 0.000000{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").UseCustomVector = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Direction = (0, 0, -1){EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}"), ["N_Axis"]){EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").AlongSketchNormal = 1{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Type = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").UpToFace = None{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Reversed = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Midplane = 1{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Offset = 0{EOL}'
    elif extrude_parameter['extent_type'] == 'OneSideFeatureExtentType':
        if e_len1 < 0:
            e_len1 = -e_len1
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Length = {e_len1}{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").TaperAngle = 0.000000{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").UseCustomVector = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Direction = (0, 0, 1){EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}"), ["N_Axis"]){EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").AlongSketchNormal = 1{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Type = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").UpToFace = None{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Reversed = 1{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Midplane = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Offset = 0{EOL}'
        else:
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Length = {e_len1}{EOL}'
            # fys+添加了条件判断，仅当 Length2 有实际意义时才设置该参数
            if e_len2 < 0:  # 注意：pocket 中 e_len2 是负数
                ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Length2 = {e_len2}{EOL}'
                ret_str += f'App.ActiveDocument.getObject("{pocket_name}").TaperAngle2 = 0.000000{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").TaperAngle = 0.000000{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Direction = (0, 0, -1){EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}"), ["N_Axis"]){EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").AlongSketchNormal = 1{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Type = 4{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").UpToFace = None{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Reversed = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Midplane = 0{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Offset = 0{EOL}'
    elif extrude_parameter['extent_type'] == 'TwoSidesFeatureExtentType':
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Length = {e_len1}{EOL}'
        # fys+添加了条件判断，仅当 Length2 有实际意义时才设置该参数
        if e_len2 < 0:  # 注意：pocket 中 e_len2 是负数
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Length2 = {e_len2}{EOL}'
            ret_str += f'App.ActiveDocument.getObject("{pocket_name}").TaperAngle2 = 0.000000{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").TaperAngle = 0.000000{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Direction = (0, 0, -1){EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_{fusion_sketch_id}_{profile_id}"), ["N_Axis"]){EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").AlongSketchNormal = 1{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Type = 4{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").UpToFace = None{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Reversed = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Midplane = 0{EOL}'
        ret_str += f'App.ActiveDocument.getObject("{pocket_name}").Offset = 0{EOL}'
    else:
        raise NotImplementedError(f'Extent Type: {extrude_parameter["extent_type"]} is not implemented')

    return ret_str

    pass


def free_make_extrude(boolean_operation, extrude_parameter, data_id, fusion_extrude_id, fusion_sketch_id,
                      loop_id, now_body) -> str:
    ret_str = ''
    if boolean_operation == 'NewBodyFeatureOperation' or boolean_operation == 'JoinFeatureOperation':

        ret_str += free_pad(extrude_parameter, data_id, fusion_extrude_id, fusion_sketch_id, loop_id, now_body)
    elif boolean_operation == 'CutFeatureOperation':
        ret_str += free_pocket(extrude_parameter, data_id, fusion_extrude_id, fusion_sketch_id, loop_id, now_body)
    else:
        raise NotImplementedError
    return ret_str


def free_make_new_sketch(data_id, fusion_extrude_id, fusion_sketch_id, profile_id, operation_list, transform,
                         now_body_name) -> str:
    """
    >>> App.getDocument('Unnamed2').getObject('Body').newObject('Sketcher::SketchObject','Sketch')
    >>> App.getDocument('Unnamed2').getObject('Sketch').Support = (App.getDocument('Unnamed2').getObject('XY_Plane'),[''])
    >>> App.getDocument('Unnamed2').getObject('Sketch').MapMode = 'FlatFace'
        App.getDocument('Unnamed').getObject('Sketch').Placement.Base=App.Vector(0.7635875, 0.0, 5.32385)
    # A loop get a sketch
    """
    sketch_name = f'Sketch_{fusion_sketch_id}_{profile_id}'
    body_name = now_body_name
    line_plane = f'plane = App.ActiveDocument.getObject("{body_name}").newObject("PartDesign::Plane", "plane_{sketch_name}")'
    origin_vector_str = f'origin = App.Vector({transform[0] * 1000.0:.14f},{transform[1] * 1000.0:.14f},{transform[2] * 1000.0:.14f})'
    x_axis_vector_str = f'x_axis=App.Vector({transform[3]:.14f},{transform[4]:.14f},{transform[5]:.14f})'
    y_axis_vector_str = f'y_axis=App.Vector({transform[6]:.14f},{transform[7]:.14f},{transform[8]:.14f})'
    z_axis_vector_str = f'z_axis=App.Vector({transform[9]:.14f},{transform[10]:.14f},{transform[11]:.14f})'
    rot_vector_str = f'rot = App.Rotation(x_axis,y_axis,z_axis)'
    place_vector_str = f'App.ActiveDocument.getObject("plane_{sketch_name}").Placement = App.Placement(origin,rot)'
    line1 = f'App.ActiveDocument.getObject("{body_name}").newObject("Sketcher::SketchObject","{sketch_name}")'
    line2 = f'App.ActiveDocument.getObject("{sketch_name}").AttachmentSupport = (App.ActiveDocument.getObject("plane_{sketch_name}"), [""])'
    line3 = f'App.ActiveDocument.getObject("{sketch_name}").MapMode = "FlatFace"'

    # prepare_str = f'{line1}{EOL}{line2}{EOL}{line3}{EOL}{place_vector_str}{EOL}{x_axis_vector_str}{EOL}{y_axis_vector_str}{EOL}{z_axis_vector_str}{EOL}{rot_vector_str}{EOL}'
    prepare_str = f'{line_plane}{EOL}{origin_vector_str}{EOL}{x_axis_vector_str}{EOL}{y_axis_vector_str}{EOL}{z_axis_vector_str}{EOL}{rot_vector_str}{EOL}{place_vector_str}{EOL}{line1}{EOL}{line2}{EOL}{line3}{EOL}'
    operation_str = ''
    for operation in operation_list:
        if operation['type'] == 'Line':
            # st_pt = apply_transform(operation['st_pt'], transform)
            # ed_pt = apply_transform(operation['ed_pt'], transform)
            st_pt = operation['st_pt']
            ed_pt = operation['ed_pt']
            # st_pt = move_vec(operation['st_pt'], transform)
            # ed_pt = move_vec(operation['ed_pt'], transform)
            operation_str += free_make_line(data_id, sketch_name, st_pt, ed_pt)
            operation_str += EOL
        elif operation['type'] == 'Circle':
            # normal = apply_transform(operation['normal'], transform)
            # center_pt = apply_transform(operation['center_pt'], transform)
            center_pt = operation['center_pt']
            # center_pt = move_vec(operation['center_pt'], transform)
            normal = operation['normal']
            operation_str += free_make_circle(data_id, sketch_name, center_pt, normal,
                                              operation['radius'])
            operation_str += EOL
        elif operation['type'] == 'Arc':
            # normal = apply_transform(operation['normal'], transform)
            # center_pt = apply_transform(operation['center_pt'], transform)
            center_pt = operation['center_pt']
            # center_pt = move_vec(operation['center_pt'], transform)
            normal = operation['normal']
            operation_str += free_make_arc(data_id, sketch_name, center_pt, normal,
                                           operation['radius'], operation['st_angle'], operation['ed_angle'])
            operation_str += EOL
    MissingPointOnPointConstraints_str = f'detect_cnt=App.ActiveDocument.getObject("{sketch_name}").detectMissingPointOnPointConstraints(){EOL}'
    # MissingPointOnPointConstraints_str += f'if detect_cnt>'
    # MissingPointOnPointConstraints_str += f'App.ActiveDocument.getObject("{sketch_name}").analyseMissingPointOnPointCoincident(){EOL}'
    MissingPointOnPointConstraints_str += f'(App.ActiveDocument.getObject("{sketch_name}").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None{EOL}'
    #
    # return f'{prepare_str}{operation_str}{RECOMPUTE}'
    return f'{prepare_str}{operation_str}{RECOMPUTE}{MissingPointOnPointConstraints_str}{RECOMPUTE}'


def select_active_doc(data_id):
    return f'App.setActiveDocument("{data_id}"){EOL}App.ActiveDocument=App.ActiveDocument{EOL}'

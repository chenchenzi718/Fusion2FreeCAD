import json
import os
import sys

from exceptiongroup import catch

from utils.load_fusion import load_fusion

if os.name == 'nt':
    freecad_path = r"D:\name_and_rebuild\FreeCAD\lib"
elif os.name == 'linux':
    freecad_path = "/usr/lib/freecad-daily/lib"
if freecad_path not in sys.path:
    sys.path.append(freecad_path)
os.environ['FREECAD_LIB'] = freecad_path

import FreeCAD as App
import FreeCAD

def get_combined_bbox(filepath):
    # 打开指定的FreeCAD文档
    doc = FreeCAD.open(filepath)
    doc = FreeCAD.ActiveDocument

    combined_bbox = None
    try:
        # 遍历文档中的对象
        for obj in doc.Objects:
            # 筛选出PartDesign::Body类型的对象
            if obj.TypeId == "PartDesign::Body":
                shape = obj.Shape
                bbox = shape.BoundBox
                # print(f"Bounding Box for {obj.Label}:", bbox)
                # 如果还没有初始化combined_bbox，则将当前bbox作为初始值
                if combined_bbox is None:
                    combined_bbox = bbox
                else:
                    # 将当前Body的bbox合并进总bbox中
                    combined_bbox.add(bbox)
    except Exception as e:
        raise RuntimeError(f"Error occurred while processing BBox: {filepath}: {e}")
    return [combined_bbox.XMin,combined_bbox.YMin,combined_bbox.ZMin,combined_bbox.XMax,combined_bbox.YMax,combined_bbox.ZMax]
def setup_to_fusion(bbox_tuple,json_path):
    fusion_json=load_fusion(json_path)
    fusion_json['properties']['bounding_box']['min_point']['x'] = bbox_tuple[0]/1000.0
    fusion_json['properties']['bounding_box']['min_point']['y'] = bbox_tuple[1]/1000.0
    fusion_json['properties']['bounding_box']['min_point']['z'] = bbox_tuple[2]/1000.0
    fusion_json['properties']['bounding_box']['max_point']['x'] = bbox_tuple[3]/1000.0
    fusion_json['properties']['bounding_box']['max_point']['y'] = bbox_tuple[4]/1000.0
    fusion_json['properties']['bounding_box']['max_point']['z'] = bbox_tuple[5]/1000.0
    with open(json_path, 'w') as f:
        json.dump(fusion_json, f, indent=4)

# 使用示例（请根据实际情况调整文件路径）：
# result_bbox = get_combined_bbox("D:\AI_SDK\Fusion2Free\data\cad_free\\0006\\00069872_free.FCStd")
# print("Combined Bounding Box:", result_bbox)
# print("Combined Bounding Box list :", result_bbox.XMin,result_bbox.YMin,result_bbox.ZMin,result_bbox.XMax,result_bbox.YMax,result_bbox.ZMax)


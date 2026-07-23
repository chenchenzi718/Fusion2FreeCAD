import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00819387")
App.ActiveDocument.addObject("PartDesign::Body","Body_FLkx6tQHW5Y7Cwq_0")
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").Label = "Body_FLkx6tQHW5Y7Cwq_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Plane", "plane_Sketch_FLkx6tQHW5Y7Cwq_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLkx6tQHW5Y7Cwq_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("Sketcher::SketchObject","Sketch_FLkx6tQHW5Y7Cwq_0_JGC")
App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLkx6tQHW5Y7Cwq_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,12.70000000000000,0.00000000000000),App.Vector(12.70000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,12.70000000000000,0.00000000000000),App.Vector(12.70000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,25.40000000000000,0.00000000000000),App.Vector(25.40000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,25.40000000000000,0.00000000000000),App.Vector(25.40000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,12.70000000000000,0.00000000000000),App.Vector(38.10000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,12.70000000000000,0.00000000000000),App.Vector(38.10000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(38.10000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Pad","Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC")
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC")
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLkx6tQHW5Y7Cwq_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLkx6tQHW5Y7Cwq_0_FRX8LODXTMqByUe_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Plane", "plane_Sketch_FqZ50zodwapJezn_1_JJG")
origin = App.Vector(19.05000000000000,19.05000000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqZ50zodwapJezn_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("Sketcher::SketchObject","Sketch_FqZ50zodwapJezn_1_JJG")
App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqZ50zodwapJezn_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,-6.35000000000000,0.00000000000000),App.Vector(6.35000000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-6.35000000000000,0.00000000000000),App.Vector(6.35000000000000,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-19.05000000000000,0.00000000000000),App.Vector(-6.35000000000000,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,-6.35000000000000,0.00000000000000),App.Vector(-6.35000000000000,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Pad","Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG")
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG")
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqZ50zodwapJezn_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqZ50zodwapJezn_1_F7AU9YBAau5zMnO_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Plane", "plane_Sketch_FkZUZaaM3RbS3Wf_1_JNC")
origin = App.Vector(38.10000000000000,6.35000000000000,6.35000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkZUZaaM3RbS3Wf_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("Sketcher::SketchObject","Sketch_FkZUZaaM3RbS3Wf_1_JNC")
App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkZUZaaM3RbS3Wf_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC").addGeometry(Part.LineSegment(App.Vector(-5.08000000000000,-5.08000000000000,0.00000000000000),App.Vector(0.00000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-5.08000000000000,0.00000000000000),App.Vector(0.00000000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC").addGeometry(Part.LineSegment(App.Vector(-5.08000000000000,5.08000000000000,0.00000000000000),App.Vector(0.00000000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC").addGeometry(Part.LineSegment(App.Vector(-5.08000000000000,-5.08000000000000,0.00000000000000),App.Vector(-5.08000000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Pocket","Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC")
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC")
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Plane", "plane_Sketch_FkZUZaaM3RbS3Wf_1_JNK")
origin = App.Vector(38.10000000000000,6.35000000000000,6.35000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkZUZaaM3RbS3Wf_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("Sketcher::SketchObject","Sketch_FkZUZaaM3RbS3Wf_1_JNK")
App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkZUZaaM3RbS3Wf_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-5.08000000000000,0.00000000000000),App.Vector(0.00000000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.08000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Pocket","Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK")
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNK")
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkZUZaaM3RbS3Wf_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkZUZaaM3RbS3Wf_1_FZPv7xZWHJFqQcO_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Plane", "plane_Sketch_FxSRkSfx5Qgb5zO_1_JUC")
origin = App.Vector(19.05000000000000,6.35000000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxSRkSfx5Qgb5zO_1_JUC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("Sketcher::SketchObject","Sketch_FxSRkSfx5Qgb5zO_1_JUC")
App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxSRkSfx5Qgb5zO_1_JUC"), [""])
App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC").addGeometry(Part.LineSegment(App.Vector(5.08000000000000,-5.08000000000000,0.00000000000000),App.Vector(-5.08000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC").addGeometry(Part.LineSegment(App.Vector(-5.08000000000000,-5.08000000000000,0.00000000000000),App.Vector(-5.08000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC").addGeometry(Part.LineSegment(App.Vector(5.08000000000000,0.00000000000000,0.00000000000000),App.Vector(-5.08000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC").addGeometry(Part.LineSegment(App.Vector(5.08000000000000,-5.08000000000000,0.00000000000000),App.Vector(5.08000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Pocket","Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC")
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").Profile = App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC")
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").Type = 4
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Plane", "plane_Sketch_FxSRkSfx5Qgb5zO_1_JUK")
origin = App.Vector(19.05000000000000,6.35000000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxSRkSfx5Qgb5zO_1_JUK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("Sketcher::SketchObject","Sketch_FxSRkSfx5Qgb5zO_1_JUK")
App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxSRkSfx5Qgb5zO_1_JUK"), [""])
App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUK").addGeometry(Part.LineSegment(App.Vector(5.08000000000000,0.00000000000000,0.00000000000000),App.Vector(-5.08000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.08000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Pocket","Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK")
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").Profile = App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUK")
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxSRkSfx5Qgb5zO_1_JUK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").Type = 4
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxSRkSfx5Qgb5zO_1_FaPZTilZGYdUu8r_1_JUK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Plane", "plane_Sketch_FDIRYeUpVZWOKKx_1_JYC")
origin = App.Vector(0.00000000000000,6.35000000000000,6.35000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDIRYeUpVZWOKKx_1_JYC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("Sketcher::SketchObject","Sketch_FDIRYeUpVZWOKKx_1_JYC")
App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDIRYeUpVZWOKKx_1_JYC"), [""])
App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC").addGeometry(Part.LineSegment(App.Vector(5.08000000000000,5.08000000000000,0.00000000000000),App.Vector(0.00000000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,5.08000000000000,0.00000000000000),App.Vector(0.00000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC").addGeometry(Part.LineSegment(App.Vector(5.08000000000000,-5.08000000000000,0.00000000000000),App.Vector(0.00000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC").addGeometry(Part.LineSegment(App.Vector(5.08000000000000,5.08000000000000,0.00000000000000),App.Vector(5.08000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Pocket","Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC")
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").Profile = App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC")
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").Type = 4
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Plane", "plane_Sketch_FDIRYeUpVZWOKKx_1_JYK")
origin = App.Vector(0.00000000000000,6.35000000000000,6.35000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDIRYeUpVZWOKKx_1_JYK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("Sketcher::SketchObject","Sketch_FDIRYeUpVZWOKKx_1_JYK")
App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDIRYeUpVZWOKKx_1_JYK"), [""])
App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,5.08000000000000,0.00000000000000),App.Vector(0.00000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.08000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Pocket","Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK")
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").Profile = App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYK")
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDIRYeUpVZWOKKx_1_JYK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").Type = 4
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDIRYeUpVZWOKKx_1_FVFDJosGKj5Wja7_1_JYK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Plane", "plane_Sketch_FWKc2skdWHQjspk_1_JcC")
origin = App.Vector(19.05000000000000,25.40000000000000,6.35000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWKc2skdWHQjspk_1_JcC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("Sketcher::SketchObject","Sketch_FWKc2skdWHQjspk_1_JcC")
App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWKc2skdWHQjspk_1_JcC"), [""])
App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC").addGeometry(Part.LineSegment(App.Vector(-5.08000000000000,5.08000000000000,0.00000000000000),App.Vector(5.08000000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC").addGeometry(Part.LineSegment(App.Vector(5.08000000000000,5.08000000000000,0.00000000000000),App.Vector(5.08000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC").addGeometry(Part.LineSegment(App.Vector(-5.08000000000000,-5.08000000000000,0.00000000000000),App.Vector(5.08000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC").addGeometry(Part.LineSegment(App.Vector(-5.08000000000000,5.08000000000000,0.00000000000000),App.Vector(-5.08000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLkx6tQHW5Y7Cwq_0").newObject("PartDesign::Pocket","Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC")
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").Profile = App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC")
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWKc2skdWHQjspk_1_JcC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").Type = 4
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWKc2skdWHQjspk_1_FHdAsqmPeCJMHob_1_JcC").Offset = 0
App.ActiveDocument.recompute()

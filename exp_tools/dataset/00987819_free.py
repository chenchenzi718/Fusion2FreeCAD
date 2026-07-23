import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00987819")
App.ActiveDocument.addObject("PartDesign::Body","Body_FKIgJpZX7TSaa1q_0")
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").Label = "Body_FKIgJpZX7TSaa1q_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Plane", "plane_Sketch_FKIgJpZX7TSaa1q_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKIgJpZX7TSaa1q_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("Sketcher::SketchObject","Sketch_FKIgJpZX7TSaa1q_0_JGC")
App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKIgJpZX7TSaa1q_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1074.13582999999994,1086.86089000000015,0.00000000000000),App.Vector(1125.86417000000006,1086.86089000000015,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC").addGeometry(Part.LineSegment(App.Vector(1125.86417000000006,1086.86089000000015,0.00000000000000),App.Vector(1125.86417000000006,-1113.13911000000007,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1074.13582999999994,-1113.13911000000007,0.00000000000000),App.Vector(1125.86417000000006,-1113.13911000000007,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1074.13582999999994,1086.86089000000015,0.00000000000000),App.Vector(-1074.13582999999994,-1113.13911000000007,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Pad","Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC")
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC")
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").Length = 596.0
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKIgJpZX7TSaa1q_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKIgJpZX7TSaa1q_0_FKL4EyLxdR2e0WA_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Plane", "plane_Sketch_Fy7AKY02ENbyptj_1_JJC")
origin = App.Vector(25.86417000000000,298.00000000000000,1086.86089000000015)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fy7AKY02ENbyptj_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("Sketcher::SketchObject","Sketch_Fy7AKY02ENbyptj_1_JJC")
App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fy7AKY02ENbyptj_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC").addGeometry(Part.LineSegment(App.Vector(-874.00000000000000,297.00000000000000,0.00000000000000),App.Vector(874.00000000000000,297.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC").addGeometry(Part.LineSegment(App.Vector(874.00000000000000,297.00000000000000,0.00000000000000),App.Vector(874.00000000000000,-298.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC").addGeometry(Part.LineSegment(App.Vector(-874.00000000000000,-298.00000000000000,0.00000000000000),App.Vector(874.00000000000000,-298.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC").addGeometry(Part.LineSegment(App.Vector(-874.00000000000000,297.00000000000000,0.00000000000000),App.Vector(-874.00000000000000,-298.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Pocket","Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC")
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC")
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").Length = 2415.5039731413126
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fy7AKY02ENbyptj_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fy7AKY02ENbyptj_1_FTwXGvtRLhjmYtf_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Plane", "plane_Sketch_FuKMca7lHr9wIGx_1_JNC")
origin = App.Vector(-848.13583000000006,297.50000000000000,-32.13911000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuKMca7lHr9wIGx_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("Sketcher::SketchObject","Sketch_FuKMca7lHr9wIGx_1_JNC")
App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuKMca7lHr9wIGx_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC").addGeometry(Part.LineSegment(App.Vector(297.50000000000000,1119.00000000000000,0.00000000000000),App.Vector(298.50000000000000,1119.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC").addGeometry(Part.LineSegment(App.Vector(298.50000000000000,1119.00000000000000,0.00000000000000),App.Vector(298.50000000000000,1081.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC").addGeometry(Part.LineSegment(App.Vector(298.50000000000000,1081.00000000000000,0.00000000000000),App.Vector(297.50000000000000,1081.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC").addGeometry(Part.LineSegment(App.Vector(297.50000000000000,1119.00000000000000,0.00000000000000),App.Vector(297.50000000000000,1081.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Pad","Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC")
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC")
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").Length = 1753.233516588807
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Plane", "plane_Sketch_FuKMca7lHr9wIGx_1_JNK")
origin = App.Vector(-848.13583000000006,297.50000000000000,-32.13911000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuKMca7lHr9wIGx_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("Sketcher::SketchObject","Sketch_FuKMca7lHr9wIGx_1_JNK")
App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuKMca7lHr9wIGx_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK").addGeometry(Part.LineSegment(App.Vector(297.50000000000000,1119.00000000000000,0.00000000000000),App.Vector(-297.50000000000000,1119.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK").addGeometry(Part.LineSegment(App.Vector(-297.50000000000000,1119.00000000000000,0.00000000000000),App.Vector(-297.50000000000000,1081.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK").addGeometry(Part.LineSegment(App.Vector(-297.50000000000000,1081.00000000000000,0.00000000000000),App.Vector(297.50000000000000,1081.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK").addGeometry(Part.LineSegment(App.Vector(297.50000000000000,1119.00000000000000,0.00000000000000),App.Vector(297.50000000000000,1081.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Pad","Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK")
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK")
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").Length = 1753.233516588807
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuKMca7lHr9wIGx_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuKMca7lHr9wIGx_1_FXNwjCVcWpnfpGC_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Plane", "plane_Sketch_FvGVqTX8dFKr2jv_1_JRC")
origin = App.Vector(-848.13583000000006,297.50000000000000,-32.13911000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FvGVqTX8dFKr2jv_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("Sketcher::SketchObject","Sketch_FvGVqTX8dFKr2jv_1_JRC")
App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FvGVqTX8dFKr2jv_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC").addGeometry(Part.LineSegment(App.Vector(-297.50000000000000,-1050.00000000000000,0.00000000000000),App.Vector(-266.49999999999994,-1050.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC").addGeometry(Part.LineSegment(App.Vector(-266.49999999999994,-1050.00000000000000,0.00000000000000),App.Vector(-266.49999999999994,-1081.00000000000023,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC").addGeometry(Part.LineSegment(App.Vector(-297.50000000000000,-1081.00000000000023,0.00000000000000),App.Vector(-266.49999999999994,-1081.00000000000023,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC").addGeometry(Part.LineSegment(App.Vector(-297.50000000000000,-1081.00000000000023,0.00000000000000),App.Vector(-297.50000000000000,-1050.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Pad","Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC")
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC")
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").Length = 1759.9843740463257
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FvGVqTX8dFKr2jv_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FvGVqTX8dFKr2jv_1_Fjwb24SJF7heh7G_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Plane", "plane_Sketch_F6d0KZl57cPspH0_1_JVC")
origin = App.Vector(1125.86417000000006,298.00000000000000,-13.13911000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6d0KZl57cPspH0_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("Sketcher::SketchObject","Sketch_F6d0KZl57cPspH0_1_JVC")
App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6d0KZl57cPspH0_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC").addGeometry(Part.LineSegment(App.Vector(-267.00000000000000,1069.00000000000000,0.00000000000000),App.Vector(266.99999999999994,1069.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC").addGeometry(Part.LineSegment(App.Vector(266.99999999999994,1069.00000000000000,0.00000000000000),App.Vector(266.99999999999994,-1069.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC").addGeometry(Part.LineSegment(App.Vector(-267.00000000000000,-1069.00000000000000,0.00000000000000),App.Vector(266.99999999999994,-1069.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC").addGeometry(Part.LineSegment(App.Vector(-267.00000000000000,1069.00000000000000,0.00000000000000),App.Vector(-267.00000000000000,-1069.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Pocket","Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC")
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC")
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").Length = 216.00000000000003
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6d0KZl57cPspH0_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6d0KZl57cPspH0_1_FUxhLtSWApysjs6_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Plane", "plane_Sketch_FkaWR8fNDa8L84B_1_JZC")
origin = App.Vector(1110.36417000000006,298.00000000000000,-1082.13911000000007)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkaWR8fNDa8L84B_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("Sketcher::SketchObject","Sketch_FkaWR8fNDa8L84B_1_JZC")
App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkaWR8fNDa8L84B_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC").addGeometry(Part.LineSegment(App.Vector(-200.50000000000000,-267.00000000000000,0.00000000000000),App.Vector(-15.50000000000007,-267.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC").addGeometry(Part.LineSegment(App.Vector(-15.50000000000007,-267.00000000000000,0.00000000000000),App.Vector(-15.50000000000007,266.99999999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC").addGeometry(Part.LineSegment(App.Vector(-200.50000000000000,266.99999999999994,0.00000000000000),App.Vector(-15.50000000000007,266.99999999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC").addGeometry(Part.LineSegment(App.Vector(-200.50000000000000,-267.00000000000000,0.00000000000000),App.Vector(-200.50000000000000,266.99999999999994,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Pocket","Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC")
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC")
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").Length = 295.37237621843815
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkaWR8fNDa8L84B_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkaWR8fNDa8L84B_1_F3OvvD0Jfjmpa1E_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Plane", "plane_Sketch_FFSK1V9XPci902g_1_JdC")
origin = App.Vector(-1074.13582999999994,298.00000000000000,-13.13911000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFSK1V9XPci902g_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("Sketcher::SketchObject","Sketch_FFSK1V9XPci902g_1_JdC")
App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFSK1V9XPci902g_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC").addGeometry(Part.LineSegment(App.Vector(-266.99999999999994,1069.00000000000000,0.00000000000000),App.Vector(267.00000000000000,1069.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC").addGeometry(Part.LineSegment(App.Vector(267.00000000000000,1069.00000000000000,0.00000000000000),App.Vector(267.00000000000000,-1069.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC").addGeometry(Part.LineSegment(App.Vector(-266.99999999999994,-1069.00000000000000,0.00000000000000),App.Vector(267.00000000000000,-1069.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC").addGeometry(Part.LineSegment(App.Vector(-266.99999999999994,1069.00000000000000,0.00000000000000),App.Vector(-266.99999999999994,-1069.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Pocket","Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC")
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC")
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").Length = 216.00000000000003
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFSK1V9XPci902g_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFSK1V9XPci902g_1_FOZaisbnQakn5JB_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Plane", "plane_Sketch_FB0vYeDccSknJmF_1_JhC")
origin = App.Vector(-1058.63583000000017,298.00000000000000,-1082.13911000000007)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FB0vYeDccSknJmF_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("Sketcher::SketchObject","Sketch_FB0vYeDccSknJmF_1_JhC")
App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FB0vYeDccSknJmF_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC").addGeometry(Part.LineSegment(App.Vector(200.50000000000000,266.99999999999994,0.00000000000000),App.Vector(15.50000000000007,266.99999999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC").addGeometry(Part.LineSegment(App.Vector(15.50000000000007,266.99999999999994,0.00000000000000),App.Vector(15.50000000000007,-267.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC").addGeometry(Part.LineSegment(App.Vector(200.50000000000000,-267.00000000000000,0.00000000000000),App.Vector(15.50000000000007,-267.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC").addGeometry(Part.LineSegment(App.Vector(200.50000000000000,266.99999999999994,0.00000000000000),App.Vector(200.50000000000000,-267.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKIgJpZX7TSaa1q_0").newObject("PartDesign::Pocket","Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC")
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC")
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").Length = 871.4787308126688
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FB0vYeDccSknJmF_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FB0vYeDccSknJmF_1_FRFEQ9pKCa1NiNi_1_JhC").Offset = 0
App.ActiveDocument.recompute()

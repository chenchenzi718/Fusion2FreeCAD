import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00365012")
App.ActiveDocument.addObject("PartDesign::Body","Body_FcSr2Yooi2V4g2r_0")
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").Label = "Body_FcSr2Yooi2V4g2r_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Plane", "plane_Sketch_FcSr2Yooi2V4g2r_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcSr2Yooi2V4g2r_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("Sketcher::SketchObject","Sketch_FcSr2Yooi2V4g2r_0_JGC")
App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcSr2Yooi2V4g2r_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC").addGeometry(Part.LineSegment(App.Vector(127.00000000000000,-25.40000000000000,0.00000000000000),App.Vector(-127.00000000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC").addGeometry(Part.LineSegment(App.Vector(-127.00000000000000,-25.40000000000000,0.00000000000000),App.Vector(-127.00000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC").addGeometry(Part.LineSegment(App.Vector(127.00000000000000,25.40000000000000,0.00000000000000),App.Vector(-127.00000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC").addGeometry(Part.LineSegment(App.Vector(127.00000000000000,-25.40000000000000,0.00000000000000),App.Vector(127.00000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Pad","Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC")
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC")
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcSr2Yooi2V4g2r_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcSr2Yooi2V4g2r_0_FUeTzCqagZytChV_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Plane", "plane_Sketch_Fxw7IFghYkx32Ex_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fxw7IFghYkx32Ex_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("Sketcher::SketchObject","Sketch_Fxw7IFghYkx32Ex_1_JJG")
App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fxw7IFghYkx32Ex_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG").addGeometry(Part.LineSegment(App.Vector(-75.66973000000000,-12.70000000000000,0.00000000000000),App.Vector(-101.06972999999999,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG").addGeometry(Part.LineSegment(App.Vector(-101.06972999999999,-12.70000000000000,0.00000000000000),App.Vector(-101.06972999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG").addGeometry(Part.LineSegment(App.Vector(-75.66973000000000,12.70000000000000,0.00000000000000),App.Vector(-101.06972999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG").addGeometry(Part.LineSegment(App.Vector(-75.66973000000000,-12.70000000000000,0.00000000000000),App.Vector(-75.66973000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Pad","Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG")
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG")
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Plane", "plane_Sketch_Fxw7IFghYkx32Ex_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fxw7IFghYkx32Ex_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("Sketcher::SketchObject","Sketch_Fxw7IFghYkx32Ex_1_JJC")
App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fxw7IFghYkx32Ex_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,-12.70000000000000,0.00000000000000),App.Vector(-12.70000000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC").addGeometry(Part.LineSegment(App.Vector(-12.70000000000000,-12.70000000000000,0.00000000000000),App.Vector(-12.70000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,12.70000000000000,0.00000000000000),App.Vector(-12.70000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,-12.70000000000000,0.00000000000000),App.Vector(12.70000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Pad","Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC")
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC")
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Plane", "plane_Sketch_Fxw7IFghYkx32Ex_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fxw7IFghYkx32Ex_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("Sketcher::SketchObject","Sketch_Fxw7IFghYkx32Ex_1_JJK")
App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fxw7IFghYkx32Ex_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK").addGeometry(Part.LineSegment(App.Vector(100.18604000000001,-12.70000000000000,0.00000000000000),App.Vector(74.78604000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK").addGeometry(Part.LineSegment(App.Vector(74.78604000000000,-12.70000000000000,0.00000000000000),App.Vector(74.78604000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK").addGeometry(Part.LineSegment(App.Vector(100.18604000000001,12.70000000000000,0.00000000000000),App.Vector(74.78604000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK").addGeometry(Part.LineSegment(App.Vector(100.18604000000001,-12.70000000000000,0.00000000000000),App.Vector(100.18604000000001,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Pad","Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK")
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK")
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fxw7IFghYkx32Ex_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fxw7IFghYkx32Ex_1_FytZR6QCmPGJTTM_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Plane", "plane_Sketch_FjZSh45YPnu4OyD_1_JNG")
origin = App.Vector(-88.36972999999999,-12.70000000000000,15.87500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("Sketcher::SketchObject","Sketch_FjZSh45YPnu4OyD_1_JNG")
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,33.07320000000000,0.00000000000000),App.Vector(-6.35000000000001,33.07320000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG").addGeometry(Part.LineSegment(App.Vector(-6.35000000000001,33.07320000000000,0.00000000000000),App.Vector(-6.35000000000001,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,12.70000000000000,0.00000000000000),App.Vector(-6.35000000000001,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,33.07320000000000,0.00000000000000),App.Vector(6.34999999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Pocket","Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").Length = 38.1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Plane", "plane_Sketch_FjZSh45YPnu4OyD_1_JNK")
origin = App.Vector(-88.36972999999999,-12.70000000000000,15.87500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("Sketcher::SketchObject","Sketch_FjZSh45YPnu4OyD_1_JNK")
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,-7.67320000000000,0.00000000000000),App.Vector(-6.35000000000001,-7.67320000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK").addGeometry(Part.LineSegment(App.Vector(-6.35000000000001,-7.67320000000000,0.00000000000000),App.Vector(-6.35000000000001,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,12.70000000000000,0.00000000000000),App.Vector(-6.35000000000001,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,-7.67320000000000,0.00000000000000),App.Vector(6.34999999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Pocket","Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").Length = 38.1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Plane", "plane_Sketch_FjZSh45YPnu4OyD_1_JNC")
origin = App.Vector(-88.36972999999999,-12.70000000000000,15.87500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("Sketcher::SketchObject","Sketch_FjZSh45YPnu4OyD_1_JNC")
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC").addGeometry(Part.LineSegment(App.Vector(94.71972999999998,-7.67080000000000,0.00000000000000),App.Vector(82.01973000000000,-7.67080000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC").addGeometry(Part.LineSegment(App.Vector(82.01973000000000,-7.67080000000000,0.00000000000000),App.Vector(82.01973000000000,33.07080000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC").addGeometry(Part.LineSegment(App.Vector(94.71972999999998,33.07080000000000,0.00000000000000),App.Vector(82.01973000000000,33.07080000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC").addGeometry(Part.LineSegment(App.Vector(94.71972999999998,-7.67080000000000,0.00000000000000),App.Vector(94.71972999999998,33.07080000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Pocket","Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").Length = 38.1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Plane", "plane_Sketch_FjZSh45YPnu4OyD_1_JPC")
origin = App.Vector(87.48604000000000,-12.70000000000000,15.87500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("Sketcher::SketchObject","Sketch_FjZSh45YPnu4OyD_1_JPC")
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,33.07080000000000,0.00000000000000),App.Vector(-6.34999999999999,33.07080000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC").addGeometry(Part.LineSegment(App.Vector(-6.34999999999999,33.07080000000000,0.00000000000000),App.Vector(-6.34999999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,12.70000000000000,0.00000000000000),App.Vector(-6.34999999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,33.07080000000000,0.00000000000000),App.Vector(6.34999999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Pocket","Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").Length = 38.1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Plane", "plane_Sketch_FjZSh45YPnu4OyD_1_JPG")
origin = App.Vector(87.48604000000000,-12.70000000000000,15.87500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("Sketcher::SketchObject","Sketch_FjZSh45YPnu4OyD_1_JPG")
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjZSh45YPnu4OyD_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,-7.67080000000000,0.00000000000000),App.Vector(-6.34999999999999,-7.67080000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG").addGeometry(Part.LineSegment(App.Vector(-6.34999999999999,-7.67080000000000,0.00000000000000),App.Vector(-6.34999999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,12.70000000000000,0.00000000000000),App.Vector(-6.34999999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,-7.67080000000000,0.00000000000000),App.Vector(6.34999999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcSr2Yooi2V4g2r_0").newObject("PartDesign::Pocket","Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG")
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").Length = 38.1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjZSh45YPnu4OyD_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjZSh45YPnu4OyD_1_FTuM4xhazlZVEPe_1_JPG").Offset = 0
App.ActiveDocument.recompute()

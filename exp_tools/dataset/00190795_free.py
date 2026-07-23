import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00190795")
App.ActiveDocument.addObject("PartDesign::Body","Body_FLwi79UbFmN2IdD_0")
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").Label = "Body_FLwi79UbFmN2IdD_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Plane", "plane_Sketch_FLwi79UbFmN2IdD_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLwi79UbFmN2IdD_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("Sketcher::SketchObject","Sketch_FLwi79UbFmN2IdD_0_JGC")
App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLwi79UbFmN2IdD_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-203.50000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-203.50000000000000,0.00000000000000,0.00000000000000),App.Vector(-203.50000000000000,500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-203.50000000000000,500.00000000000000,0.00000000000000),App.Vector(0.00000000000000,500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,500.00000000000000,0.00000000000000),App.Vector(203.50000000000000,500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").addGeometry(Part.LineSegment(App.Vector(203.50000000000000,500.00000000000000,0.00000000000000),App.Vector(203.50000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(203.50000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Pad","Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC")
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC")
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").Length = 6.0
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLwi79UbFmN2IdD_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLwi79UbFmN2IdD_0_Ff3AUhQF2AdEJDr_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Plane", "plane_Sketch_FsLgHIQuo71vfQi_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,250.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsLgHIQuo71vfQi_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("Sketcher::SketchObject","Sketch_FsLgHIQuo71vfQi_1_JJC")
App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsLgHIQuo71vfQi_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC").addGeometry(Part.LineSegment(App.Vector(-118.50000000000000,200.00000000000000,0.00000000000000),App.Vector(153.50000000000000,200.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC").addGeometry(Part.LineSegment(App.Vector(153.50000000000000,200.00000000000000,0.00000000000000),App.Vector(153.50000000000000,-180.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC").addGeometry(Part.LineSegment(App.Vector(-118.50000000000000,-180.00000000000000,0.00000000000000),App.Vector(153.50000000000000,-180.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC").addGeometry(Part.LineSegment(App.Vector(-118.50000000000000,200.00000000000000,0.00000000000000),App.Vector(-118.50000000000000,-180.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Pocket","Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC")
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC")
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").Length = 6.0
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsLgHIQuo71vfQi_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsLgHIQuo71vfQi_1_Fsx87sQjrJS8bM3_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Plane", "plane_Sketch_Fr0260GfHGCfaX7_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,250.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("Sketcher::SketchObject","Sketch_Fr0260GfHGCfaX7_1_JNC")
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNC").addGeometry(Part.Circle(App.Vector(-143.50000000000000,200.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Pocket","Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNC")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Plane", "plane_Sketch_Fr0260GfHGCfaX7_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,250.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("Sketcher::SketchObject","Sketch_Fr0260GfHGCfaX7_1_JNG")
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNG").addGeometry(Part.Circle(App.Vector(173.50000000000000,200.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Pocket","Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNG")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Plane", "plane_Sketch_Fr0260GfHGCfaX7_1_JNK")
origin = App.Vector(0.00000000000000,0.00000000000000,250.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("Sketcher::SketchObject","Sketch_Fr0260GfHGCfaX7_1_JNK")
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-173.50000000000000,150.00000000000003,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK").addGeometry(Part.LineSegment(App.Vector(-175.50000000000000,150.00000000000003,0.00000000000000),App.Vector(-175.50000000000000,125.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-173.50000000000000,125.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK").addGeometry(Part.LineSegment(App.Vector(-171.50000000000000,150.00000000000003,0.00000000000000),App.Vector(-171.50000000000000,125.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Pocket","Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Plane", "plane_Sketch_Fr0260GfHGCfaX7_1_JNO")
origin = App.Vector(0.00000000000000,0.00000000000000,250.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("Sketcher::SketchObject","Sketch_Fr0260GfHGCfaX7_1_JNO")
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-142.50000000000000,150.00000000000003,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO").addGeometry(Part.LineSegment(App.Vector(-144.50000000000000,150.00000000000003,0.00000000000000),App.Vector(-144.50000000000000,125.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-142.50000000000000,125.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO").addGeometry(Part.LineSegment(App.Vector(-140.50000000000000,150.00000000000003,0.00000000000000),App.Vector(-140.50000000000000,125.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Pocket","Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Plane", "plane_Sketch_Fr0260GfHGCfaX7_1_JNS")
origin = App.Vector(0.00000000000000,0.00000000000000,250.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("Sketcher::SketchObject","Sketch_Fr0260GfHGCfaX7_1_JNS")
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-173.50000000000000,119.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS").addGeometry(Part.LineSegment(App.Vector(-175.50000000000000,119.00000000000000,0.00000000000000),App.Vector(-175.50000000000000,93.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-173.50000000000000,93.99999999999997,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS").addGeometry(Part.LineSegment(App.Vector(-171.50000000000000,119.00000000000000,0.00000000000000),App.Vector(-171.50000000000000,93.99999999999997,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Pocket","Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Plane", "plane_Sketch_Fr0260GfHGCfaX7_1_JNW")
origin = App.Vector(0.00000000000000,0.00000000000000,250.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("Sketcher::SketchObject","Sketch_Fr0260GfHGCfaX7_1_JNW")
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr0260GfHGCfaX7_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-142.50000000000000,119.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW").addGeometry(Part.LineSegment(App.Vector(-144.50000000000000,119.00000000000000,0.00000000000000),App.Vector(-144.50000000000000,93.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-142.50000000000000,93.99999999999997,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW").addGeometry(Part.LineSegment(App.Vector(-140.50000000000000,119.00000000000000,0.00000000000000),App.Vector(-140.50000000000000,93.99999999999997,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLwi79UbFmN2IdD_0").newObject("PartDesign::Pocket","Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW")
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr0260GfHGCfaX7_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fr0260GfHGCfaX7_1_FYmaA8BaYOicQAz_1_JNW").Offset = 0
App.ActiveDocument.recompute()

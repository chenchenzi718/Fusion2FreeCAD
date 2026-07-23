import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00246210")
App.ActiveDocument.addObject("PartDesign::Body","Body_FXNVOQWVEItzok9_0")
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").Label = "Body_FXNVOQWVEItzok9_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Plane", "plane_Sketch_FXNVOQWVEItzok9_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXNVOQWVEItzok9_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("Sketcher::SketchObject","Sketch_FXNVOQWVEItzok9_0_JGC")
App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXNVOQWVEItzok9_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(160.01999999999998,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC").addGeometry(Part.LineSegment(App.Vector(160.01999999999998,0.00000000000000,0.00000000000000),App.Vector(160.01999999999998,160.01999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,160.01999999999998,0.00000000000000),App.Vector(160.01999999999998,160.01999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,160.01999999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Pad","Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC")
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC")
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").Length = 29.972
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXNVOQWVEItzok9_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXNVOQWVEItzok9_0_FegAqhPQj8Z9ArY_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Plane", "plane_Sketch_FeyB3vIpmYgCoxh_1_JJG")
origin = App.Vector(80.00999999999999,80.00999999999999,-29.97200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeyB3vIpmYgCoxh_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("Sketcher::SketchObject","Sketch_FeyB3vIpmYgCoxh_1_JJG")
App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeyB3vIpmYgCoxh_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(-75.56500000000000,54.61000000000000,0.00000000000000),App.Vector(-61.08700000000000,54.61000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(-61.08700000000000,54.61000000000000,0.00000000000000),App.Vector(-61.08700000000000,75.56500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(-61.08700000000000,75.56500000000000,0.00000000000000),App.Vector(61.08700000000000,75.56500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(61.08700000000000,54.61000000000000,0.00000000000000),App.Vector(61.08700000000000,75.56500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(75.56500000000000,54.61000000000000,0.00000000000000),App.Vector(61.08700000000000,54.61000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(75.56500000000000,54.61000000000000,0.00000000000000),App.Vector(75.56500000000000,-54.60999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(75.56500000000000,-54.60999999999999,0.00000000000000),App.Vector(61.08700000000000,-54.60999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(61.08700000000000,-54.60999999999999,0.00000000000000),App.Vector(61.08700000000000,-75.56500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(-61.08700000000000,-75.56500000000000,0.00000000000000),App.Vector(61.08700000000000,-75.56500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(-61.08700000000000,-54.60999999999999,0.00000000000000),App.Vector(-61.08700000000000,-75.56500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(-75.56500000000000,-54.60999999999999,0.00000000000000),App.Vector(-61.08700000000000,-54.60999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").addGeometry(Part.LineSegment(App.Vector(-75.56500000000000,54.61000000000000,0.00000000000000),App.Vector(-75.56500000000000,-54.60999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Pocket","Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG")
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG")
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").Length = 26.162000000000006
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeyB3vIpmYgCoxh_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeyB3vIpmYgCoxh_1_Fplmw6MOyC49YQE_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Plane", "plane_Sketch_FJ5nPNIU2yuvmBz_1_JNC")
origin = App.Vector(80.00999999999999,80.00999999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("Sketcher::SketchObject","Sketch_FJ5nPNIU2yuvmBz_1_JNC")
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNC").addGeometry(Part.Circle(App.Vector(-40.00500000000000,-41.91000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Pocket","Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNC")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Plane", "plane_Sketch_FJ5nPNIU2yuvmBz_1_JNG")
origin = App.Vector(80.00999999999999,80.00999999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("Sketcher::SketchObject","Sketch_FJ5nPNIU2yuvmBz_1_JNG")
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNG").addGeometry(Part.Circle(App.Vector(-1.90500000000000,-41.91000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Pocket","Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNG")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Plane", "plane_Sketch_FJ5nPNIU2yuvmBz_1_JNK")
origin = App.Vector(80.00999999999999,80.00999999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("Sketcher::SketchObject","Sketch_FJ5nPNIU2yuvmBz_1_JNK")
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNK").addGeometry(Part.Circle(App.Vector(36.19500000000001,-41.91000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Pocket","Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNK")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Plane", "plane_Sketch_FJ5nPNIU2yuvmBz_1_JNW")
origin = App.Vector(80.00999999999999,80.00999999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("Sketcher::SketchObject","Sketch_FJ5nPNIU2yuvmBz_1_JNW")
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNW").addGeometry(Part.Circle(App.Vector(36.19500000000001,-3.80999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Pocket","Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNW")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Plane", "plane_Sketch_FJ5nPNIU2yuvmBz_1_JNS")
origin = App.Vector(80.00999999999999,80.00999999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("Sketcher::SketchObject","Sketch_FJ5nPNIU2yuvmBz_1_JNS")
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNS").addGeometry(Part.Circle(App.Vector(-1.90500000000000,-3.80999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Pocket","Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNS")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Plane", "plane_Sketch_FJ5nPNIU2yuvmBz_1_JNO")
origin = App.Vector(80.00999999999999,80.00999999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("Sketcher::SketchObject","Sketch_FJ5nPNIU2yuvmBz_1_JNO")
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ5nPNIU2yuvmBz_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNO").addGeometry(Part.Circle(App.Vector(-40.00500000000000,-3.80999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXNVOQWVEItzok9_0").newObject("PartDesign::Pocket","Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNO")
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ5nPNIU2yuvmBz_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ5nPNIU2yuvmBz_1_F1QRgH1SvmKMh4R_1_JNO").Offset = 0
App.ActiveDocument.recompute()

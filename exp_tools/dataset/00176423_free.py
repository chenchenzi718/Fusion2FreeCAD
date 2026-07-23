import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00176423")
App.ActiveDocument.addObject("PartDesign::Body","Body_FlM2nbiE3Uw8BWK")
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").Label = "Body_FlM2nbiE3Uw8BWK"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FlM2nbiE3Uw8BWK_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlM2nbiE3Uw8BWK_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FlM2nbiE3Uw8BWK_JGC")
App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlM2nbiE3Uw8BWK_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(133.70000000000002,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),133.70000000000002),2.08148808814468,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC").addGeometry(Part.LineSegment(App.Vector(68.34999999999999,111.45410000000000,0.00000000000000),App.Vector(68.34999999999999,116.64076000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(133.70000000000002,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),129.20000000000002),2.10111117583642,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(4.50000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pad","Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC")
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC")
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").Length = 800.0
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FlM2nbiE3Uw8BWK_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlM2nbiE3Uw8BWK_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FlM2nbiE3Uw8BWK_JGG")
App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlM2nbiE3Uw8BWK_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(4.50000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG").addGeometry(Part.LineSegment(App.Vector(4.50000000000000,0.00000000000000,0.00000000000000),App.Vector(4.50000000000000,-407.30000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-407.30000000000001,0.00000000000000),App.Vector(4.50000000000000,-407.30000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-407.30000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pad","Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG")
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG")
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").Length = 800.0
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlM2nbiE3Uw8BWK_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").Type = 0
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlM2nbiE3Uw8BWK_FAMU8mYBkJmf7Ss_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FCIHX8qu8DS8x2W_0_JIG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FCIHX8qu8DS8x2W_0_JIG")
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIG"), [""])
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").addGeometry(Part.LineSegment(App.Vector(508.49999999999994,-365.80000000000001,0.00000000000000),App.Vector(508.49999999999994,-265.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(470.00000000000000,-265.79999999999995,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),38.50000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").addGeometry(Part.LineSegment(App.Vector(431.50000000000000,-265.79999999999995,0.00000000000000),App.Vector(431.50000000000000,-365.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(390.00000000000000,-365.80000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),41.50000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").addGeometry(Part.LineSegment(App.Vector(550.00000000000000,-407.30000000000001,0.00000000000000),App.Vector(390.00000000000000,-407.30000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(550.00000000000000,-365.80000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),41.50000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pocket","Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").Profile = App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").Type = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FCIHX8qu8DS8x2W_0_JIC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FCIHX8qu8DS8x2W_0_JIC")
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIC"), [""])
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").addGeometry(Part.LineSegment(App.Vector(760.00000000000000,-197.30000000000001,0.00000000000000),App.Vector(730.00000000000000,-197.30000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(730.00000000000000,-235.80000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),38.50000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").addGeometry(Part.LineSegment(App.Vector(691.50000000000000,-235.80000000000001,0.00000000000000),App.Vector(691.50000000000000,-365.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(650.00000000000000,-365.80000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),41.50000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").addGeometry(Part.LineSegment(App.Vector(650.00000000000000,-407.30000000000001,0.00000000000000),App.Vector(800.00000000000000,-407.30000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").addGeometry(Part.LineSegment(App.Vector(800.00000000000000,-157.29999999999998,0.00000000000000),App.Vector(800.00000000000000,-407.30000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(760.00000000000000,-157.29999999999998,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),40.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pocket","Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").Profile = App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").Type = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FCIHX8qu8DS8x2W_0_JIK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FCIHX8qu8DS8x2W_0_JIK")
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIK"), [""])
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(41.50000000000000,-365.80000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),41.50000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-365.80000000000001,0.00000000000000),App.Vector(0.00000000000000,-407.30000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIK").addGeometry(Part.LineSegment(App.Vector(41.50000000000000,-407.30000000000001,0.00000000000000),App.Vector(0.00000000000000,-407.30000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pocket","Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").Profile = App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIK")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").Type = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FCIHX8qu8DS8x2W_0_JIO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FCIHX8qu8DS8x2W_0_JIO")
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIO"), [""])
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIO").addGeometry(Part.Circle(App.Vector(41.50000000000000,-365.80000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pocket","Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").Profile = App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIO")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").Type = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FCIHX8qu8DS8x2W_0_JIe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FCIHX8qu8DS8x2W_0_JIe")
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIe"), [""])
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(770.00000000000000,-115.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),10.50000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe").addGeometry(Part.LineSegment(App.Vector(780.50000000000000,-115.80000000000000,0.00000000000000),App.Vector(780.50000000000000,-155.79999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(770.00000000000000,-155.79999999999998,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),10.50000000000000),3.14159265358979,-0.0),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe").addGeometry(Part.LineSegment(App.Vector(759.50000000000000,-115.80000000000000,0.00000000000000),App.Vector(759.50000000000000,-155.79999999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pocket","Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").Profile = App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").Length = 25.0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").Type = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FCIHX8qu8DS8x2W_0_JIa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FCIHX8qu8DS8x2W_0_JIa")
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIa"), [""])
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(600.00000000000000,-135.80000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),10.50000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa").addGeometry(Part.LineSegment(App.Vector(610.50000000000000,-135.80000000000001,0.00000000000000),App.Vector(610.50000000000000,-155.79999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(600.00000000000000,-155.79999999999998,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),10.50000000000000),3.14159265358979,-0.0),False)

App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa").addGeometry(Part.LineSegment(App.Vector(589.50000000000000,-135.80000000000001,0.00000000000000),App.Vector(589.50000000000000,-155.79999999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pocket","Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").Profile = App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").Length = 25.0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").Type = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FCIHX8qu8DS8x2W_0_JIW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FCIHX8qu8DS8x2W_0_JIW")
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIW"), [""])
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIW").addGeometry(Part.Circle(App.Vector(650.00000000000000,-365.80000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pocket","Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").Profile = App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIW")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").Length = 25.0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").Type = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Plane", "plane_Sketch_FCIHX8qu8DS8x2W_0_JIS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("Sketcher::SketchObject","Sketch_FCIHX8qu8DS8x2W_0_JIS")
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCIHX8qu8DS8x2W_0_JIS"), [""])
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIS").addGeometry(Part.Circle(App.Vector(550.00000000000000,-365.80000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlM2nbiE3Uw8BWK").newObject("PartDesign::Pocket","Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").Profile = App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIS")
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").Length = 25.0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCIHX8qu8DS8x2W_0_JIS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").Type = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCIHX8qu8DS8x2W_0_FQv4zazww5qUnQs_1_JIS").Offset = 0
App.ActiveDocument.recompute()

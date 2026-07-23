import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00576154")
App.ActiveDocument.addObject("PartDesign::Body","Body_F4j0egeWCPPSgwS_0")
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").Label = "Body_F4j0egeWCPPSgwS_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Plane", "plane_Sketch_F4j0egeWCPPSgwS_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4j0egeWCPPSgwS_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("Sketcher::SketchObject","Sketch_F4j0egeWCPPSgwS_0_JGC")
App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4j0egeWCPPSgwS_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC").addGeometry(Part.LineSegment(App.Vector(-61.70050000000000,-75.37253000000000,0.00000000000000),App.Vector(15.55053000000000,-75.37253000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC").addGeometry(Part.LineSegment(App.Vector(15.55053000000000,-75.37253000000000,0.00000000000000),App.Vector(15.55053000000000,-34.74050000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC").addGeometry(Part.LineSegment(App.Vector(-61.70050000000000,-34.74050000000000,0.00000000000000),App.Vector(15.55053000000000,-34.74050000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC").addGeometry(Part.LineSegment(App.Vector(-61.70050000000000,-75.37253000000000,0.00000000000000),App.Vector(-61.70050000000000,-34.74050000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Pad","Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC")
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC")
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").Length = 76.2
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Plane", "plane_Sketch_F4j0egeWCPPSgwS_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4j0egeWCPPSgwS_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("Sketcher::SketchObject","Sketch_F4j0egeWCPPSgwS_0_JGG")
App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4j0egeWCPPSgwS_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGG").addGeometry(Part.LineSegment(App.Vector(15.55053000000000,-75.37253000000000,0.00000000000000),App.Vector(15.55053000000000,-34.74050000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGG").addGeometry(Part.LineSegment(App.Vector(15.55053000000000,-34.74050000000000,0.00000000000000),App.Vector(66.21517000000000,-75.62335000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGG").addGeometry(Part.LineSegment(App.Vector(15.55053000000000,-75.37253000000000,0.00000000000000),App.Vector(66.21517000000000,-75.62335000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Pad","Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG")
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGG")
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").Length = 76.2
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4j0egeWCPPSgwS_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4j0egeWCPPSgwS_0_Fza0OiGawBD8l0f_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Plane", "plane_Sketch_FMKkmHhDVNVWSXJ_1_JJC")
origin = App.Vector(40.88285000000000,-50.80000000000000,-55.18192000000001)
x_axis=App.Vector(0.77823084000000,0.00000000000000,-0.62797832000000)
y_axis=App.Vector(-0.00000000000000,1.00000001071713,0.00000000000000)
z_axis=App.Vector(0.62797832000000,0.00000000000000,0.77823084000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMKkmHhDVNVWSXJ_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("Sketcher::SketchObject","Sketch_FMKkmHhDVNVWSXJ_1_JJC")
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMKkmHhDVNVWSXJ_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJC").addGeometry(Part.Circle(App.Vector(-20.83930425650520,-13.52980014500061,-0.00000146064360),App.Vector(0.00000000000000,0.00000000000000,1.00000001071713),8.84910000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Pocket","Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC")
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJC")
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").Length = 88.646
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Plane", "plane_Sketch_FMKkmHhDVNVWSXJ_1_JJG")
origin = App.Vector(40.88285000000000,-50.80000000000000,-55.18192000000001)
x_axis=App.Vector(0.77823084000000,0.00000000000000,-0.62797832000000)
y_axis=App.Vector(-0.00000000000000,1.00000001071713,0.00000000000000)
z_axis=App.Vector(0.62797832000000,0.00000000000000,0.77823084000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMKkmHhDVNVWSXJ_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("Sketcher::SketchObject","Sketch_FMKkmHhDVNVWSXJ_1_JJG")
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMKkmHhDVNVWSXJ_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJG").addGeometry(Part.Circle(App.Vector(-17.63724833165320,27.27093029226605,0.00000069640840),App.Vector(0.00000000000000,0.00000000000000,1.00000001071713),9.56346000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Pocket","Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG")
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJG")
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").Length = 88.646
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Plane", "plane_Sketch_FMKkmHhDVNVWSXJ_1_JJK")
origin = App.Vector(40.88285000000000,-50.80000000000000,-55.18192000000001)
x_axis=App.Vector(0.77823084000000,0.00000000000000,-0.62797832000000)
y_axis=App.Vector(-0.00000000000000,1.00000001071713,0.00000000000000)
z_axis=App.Vector(0.62797832000000,0.00000000000000,0.77823084000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMKkmHhDVNVWSXJ_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("Sketcher::SketchObject","Sketch_FMKkmHhDVNVWSXJ_1_JJK")
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMKkmHhDVNVWSXJ_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJK").addGeometry(Part.Circle(App.Vector(13.69449896793520,25.74940027595962,-0.00000210354040),App.Vector(0.00000000000000,0.00000000000000,1.00000001071713),10.11011000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Pocket","Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK")
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJK")
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").Length = 88.646
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Plane", "plane_Sketch_FMKkmHhDVNVWSXJ_1_JJO")
origin = App.Vector(40.88285000000000,-50.80000000000000,-55.18192000000001)
x_axis=App.Vector(0.77823084000000,0.00000000000000,-0.62797832000000)
y_axis=App.Vector(-0.00000000000000,1.00000001071713,0.00000000000000)
z_axis=App.Vector(0.62797832000000,0.00000000000000,0.77823084000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMKkmHhDVNVWSXJ_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("Sketcher::SketchObject","Sketch_FMKkmHhDVNVWSXJ_1_JJO")
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMKkmHhDVNVWSXJ_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJO").addGeometry(Part.Circle(App.Vector(13.62878357751120,-11.90185012755366,0.00000067194160),App.Vector(0.00000000000000,0.00000000000000,1.00000001071713),10.43973000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Pocket","Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO")
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJO")
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").Length = 88.646
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMKkmHhDVNVWSXJ_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMKkmHhDVNVWSXJ_1_FWFEjmY2ZfZkSjD_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Plane", "plane_Sketch_F10CnlCAhd6VX8K_1_JNC")
origin = App.Vector(2.25733000000000,-76.20000000000000,-55.18192000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F10CnlCAhd6VX8K_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("Sketcher::SketchObject","Sketch_F10CnlCAhd6VX8K_1_JNC")
App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F10CnlCAhd6VX8K_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC").addGeometry(Part.LineSegment(App.Vector(13.29320000000000,20.44142000000000,0.00000000000000),App.Vector(25.69949000000000,10.43041000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC").addGeometry(Part.LineSegment(App.Vector(25.69949000000000,10.43041000000000,0.00000000000000),App.Vector(25.54790000000000,-20.19060999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC").addGeometry(Part.LineSegment(App.Vector(25.54790000000000,-20.19060999999999,0.00000000000000),App.Vector(-2.25733000000000,-20.05296000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC").addGeometry(Part.LineSegment(App.Vector(-2.25733000000000,-20.05296000000000,0.00000000000000),App.Vector(-2.25733000000000,20.44142000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC").addGeometry(Part.LineSegment(App.Vector(13.29320000000000,20.44142000000000,0.00000000000000),App.Vector(-2.25733000000000,20.44142000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Pad","Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC")
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC")
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F10CnlCAhd6VX8K_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F10CnlCAhd6VX8K_1_FiWckaY1dUYTI66_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Plane", "plane_Sketch_F2I9ymgRXYHl24g_1_JRC")
origin = App.Vector(-61.70050000000000,-38.10000000000000,-55.05651000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2I9ymgRXYHl24g_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("Sketcher::SketchObject","Sketch_F2I9ymgRXYHl24g_1_JRC")
App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2I9ymgRXYHl24g_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC").addGeometry(Part.LineSegment(App.Vector(30.85155999999999,20.31601000000000,0.00000000000000),App.Vector(19.14351000000000,20.31601000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.14351000000000,20.31601000000000,0.00000000000000),App.Vector(19.14351000000000,15.77929000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.14351000000000,15.77929000000000,0.00000000000000),App.Vector(30.85155999999999,15.77929000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC").addGeometry(Part.LineSegment(App.Vector(30.85155999999999,20.31601000000000,0.00000000000000),App.Vector(30.85155999999999,15.77929000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4j0egeWCPPSgwS_0").newObject("PartDesign::Pocket","Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC")
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC")
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").Length = 124.46000000000001
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2I9ymgRXYHl24g_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2I9ymgRXYHl24g_1_F6ik6teiBcECYfd_1_JRC").Offset = 0
App.ActiveDocument.recompute()

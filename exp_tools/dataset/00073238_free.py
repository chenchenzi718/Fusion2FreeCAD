import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00073238")
App.ActiveDocument.addObject("PartDesign::Body","Body_FzmFPTebEwfwL91_0")
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").Label = "Body_FzmFPTebEwfwL91_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_FzmFPTebEwfwL91_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzmFPTebEwfwL91_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_FzmFPTebEwfwL91_0_JGC")
App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzmFPTebEwfwL91_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC").addGeometry(Part.LineSegment(App.Vector(-724.61467999999991,1070.16047000000003,0.00000000000000),App.Vector(697.78532000000007,1070.16047000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC").addGeometry(Part.LineSegment(App.Vector(697.78532000000007,1070.16047000000003,0.00000000000000),App.Vector(697.78532000000007,-352.23953000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC").addGeometry(Part.LineSegment(App.Vector(-724.61467999999991,-352.23953000000000,0.00000000000000),App.Vector(697.78532000000007,-352.23953000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC").addGeometry(Part.LineSegment(App.Vector(-724.61467999999991,1070.16047000000003,0.00000000000000),App.Vector(-724.61467999999991,-352.23953000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pad","Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC")
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC")
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").Length = 28.575000000000003
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzmFPTebEwfwL91_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzmFPTebEwfwL91_0_FzGeveTBRPHvurR_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_Fd9qbsIJK241Y5C_1_JJC")
origin = App.Vector(-13.41468000000000,358.96046999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fd9qbsIJK241Y5C_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_Fd9qbsIJK241Y5C_1_JJC")
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fd9qbsIJK241Y5C_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJC").addGeometry(Part.Circle(App.Vector(604.65795000000003,625.24072999999999,0.00000000000000),App.Vector(0.0,0.0,1.0),53.87830000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pad","Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC")
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJC")
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").Length = 127.0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_Fd9qbsIJK241Y5C_1_JJG")
origin = App.Vector(-13.41468000000000,358.96046999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fd9qbsIJK241Y5C_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_Fd9qbsIJK241Y5C_1_JJG")
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fd9qbsIJK241Y5C_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJG").addGeometry(Part.Circle(App.Vector(604.65795000000003,-617.22931999999992,0.00000000000000),App.Vector(0.0,0.0,1.0),61.70435000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pad","Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG")
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJG")
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").Length = 127.0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_Fd9qbsIJK241Y5C_1_JJK")
origin = App.Vector(-13.41468000000000,358.96046999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fd9qbsIJK241Y5C_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_Fd9qbsIJK241Y5C_1_JJK")
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fd9qbsIJK241Y5C_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJK").addGeometry(Part.Circle(App.Vector(-618.77740000000006,-617.22931999999992,0.00000000000000),App.Vector(0.0,0.0,1.0),59.41066000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pad","Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK")
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJK")
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").Length = 127.0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_Fd9qbsIJK241Y5C_1_JJO")
origin = App.Vector(-13.41468000000000,358.96046999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fd9qbsIJK241Y5C_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_Fd9qbsIJK241Y5C_1_JJO")
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fd9qbsIJK241Y5C_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJO").addGeometry(Part.Circle(App.Vector(-618.77740000000006,625.24072999999999,0.00000000000000),App.Vector(0.0,0.0,1.0),61.38842000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pad","Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO")
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJO")
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").Length = 127.0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fd9qbsIJK241Y5C_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fd9qbsIJK241Y5C_1_FMqOM2rTrZBl5F3_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_F7aqa1m1pTMPwHx_1_JNC")
origin = App.Vector(-13.41468000000000,358.96046999999999,28.57500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7aqa1m1pTMPwHx_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_F7aqa1m1pTMPwHx_1_JNC")
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7aqa1m1pTMPwHx_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNC").addGeometry(Part.Circle(App.Vector(309.73658000000006,349.63414999999998,0.00000000000000),App.Vector(0.0,0.0,1.0),29.44728000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pocket","Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC")
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNC")
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").Length = 428.45565999999997
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_F7aqa1m1pTMPwHx_1_JNG")
origin = App.Vector(-13.41468000000000,358.96046999999999,28.57500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7aqa1m1pTMPwHx_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_F7aqa1m1pTMPwHx_1_JNG")
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7aqa1m1pTMPwHx_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNG").addGeometry(Part.Circle(App.Vector(-441.78790000000004,349.63414999999998,0.00000000000000),App.Vector(0.0,0.0,1.0),25.29826000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pocket","Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG")
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNG")
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").Length = 428.45565999999997
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_F7aqa1m1pTMPwHx_1_JNK")
origin = App.Vector(-13.41468000000000,358.96046999999999,28.57500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7aqa1m1pTMPwHx_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_F7aqa1m1pTMPwHx_1_JNK")
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7aqa1m1pTMPwHx_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNK").addGeometry(Part.Circle(App.Vector(-441.78790000000004,-418.01488000000001,0.00000000000000),App.Vector(0.0,0.0,1.0),30.57307000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pocket","Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK")
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNK")
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").Length = 428.45565999999997
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_F7aqa1m1pTMPwHx_1_JNO")
origin = App.Vector(-13.41468000000000,358.96046999999999,28.57500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7aqa1m1pTMPwHx_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_F7aqa1m1pTMPwHx_1_JNO")
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7aqa1m1pTMPwHx_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNO").addGeometry(Part.Circle(App.Vector(309.73658000000006,-418.01488000000001,0.00000000000000),App.Vector(0.0,0.0,1.0),27.37008000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pocket","Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO")
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNO")
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").Length = 428.45565999999997
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7aqa1m1pTMPwHx_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7aqa1m1pTMPwHx_1_FYxYVlZQzSH7qqW_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Plane", "plane_Sketch_F316j6qKlEJuf7m_1_JRC")
origin = App.Vector(-13.41468000000000,358.96046999999999,28.57500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F316j6qKlEJuf7m_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("Sketcher::SketchObject","Sketch_F316j6qKlEJuf7m_1_JRC")
App.ActiveDocument.getObject("Sketch_F316j6qKlEJuf7m_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F316j6qKlEJuf7m_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F316j6qKlEJuf7m_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F316j6qKlEJuf7m_1_JRC").addGeometry(Part.Circle(App.Vector(-70.42809000000000,-460.58175999999997,0.00000000000000),App.Vector(0.0,0.0,1.0),124.80614000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F316j6qKlEJuf7m_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F316j6qKlEJuf7m_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzmFPTebEwfwL91_0").newObject("PartDesign::Pocket","Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC")
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F316j6qKlEJuf7m_1_JRC")
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").Length = 511.49744
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F316j6qKlEJuf7m_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F316j6qKlEJuf7m_1_F0Z8s1m6fZ03L9X_1_JRC").Offset = 0
App.ActiveDocument.recompute()

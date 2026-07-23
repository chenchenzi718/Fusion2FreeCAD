import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00232441")
App.ActiveDocument.addObject("PartDesign::Body","Body_FUMX2Ewx873BA3l_0")
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").Label = "Body_FUMX2Ewx873BA3l_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Plane", "plane_Sketch_FUMX2Ewx873BA3l_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUMX2Ewx873BA3l_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("Sketcher::SketchObject","Sketch_FUMX2Ewx873BA3l_0_JGC")
App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUMX2Ewx873BA3l_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.04560000000000,-58.06440000000000,0.00000000000000),App.Vector(67.05600000000001,-58.06440000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC").addGeometry(Part.LineSegment(App.Vector(67.05600000000001,-58.06440000000000,0.00000000000000),App.Vector(67.05600000000001,-32.76600000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC").addGeometry(Part.LineSegment(App.Vector(67.05600000000001,-32.76600000000001,0.00000000000000),App.Vector(-60.04560000000000,-32.76600000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.04560000000000,-58.06440000000000,0.00000000000000),App.Vector(-60.04560000000000,-32.76600000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Pad","Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC")
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC")
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").Length = 126.746
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUMX2Ewx873BA3l_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUMX2Ewx873BA3l_0_FAbcn18kp9Ddb6X_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Plane", "plane_Sketch_Fio1Y96zDLsHnbM_1_JJC")
origin = App.Vector(3.50520000000000,126.74600000000000,5.00380000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fio1Y96zDLsHnbM_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("Sketcher::SketchObject","Sketch_Fio1Y96zDLsHnbM_1_JJC")
App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fio1Y96zDLsHnbM_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC").addGeometry(Part.LineSegment(App.Vector(28.80360000000000,-63.06820000000000,0.00000000000000),App.Vector(-25.14600000000000,-63.06820000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC").addGeometry(Part.LineSegment(App.Vector(-25.14600000000000,-63.06820000000000,0.00000000000000),App.Vector(-25.14600000000000,-48.13300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC").addGeometry(Part.LineSegment(App.Vector(-25.14600000000000,-48.13300000000000,0.00000000000000),App.Vector(28.80360000000000,-48.13300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC").addGeometry(Part.LineSegment(App.Vector(28.80360000000000,-63.06820000000000,0.00000000000000),App.Vector(28.80360000000000,-48.13300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Pocket","Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC")
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC")
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").Length = 57.14999999999999
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fio1Y96zDLsHnbM_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fio1Y96zDLsHnbM_1_F59Faaul734zqeX_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Plane", "plane_Sketch_FoAVa6lykBIWL5R_1_JNC")
origin = App.Vector(3.50520000000000,50.68886999999999,-32.76600000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoAVa6lykBIWL5R_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("Sketcher::SketchObject","Sketch_FoAVa6lykBIWL5R_1_JNC")
App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoAVa6lykBIWL5R_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC").addGeometry(Part.LineSegment(App.Vector(63.55080000000000,76.05713000000000,0.00000000000000),App.Vector(-63.55079999999999,76.05713000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC").addGeometry(Part.LineSegment(App.Vector(-63.55079999999999,76.05713000000000,0.00000000000000),App.Vector(-63.55079999999999,50.68888000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC").addGeometry(Part.LineSegment(App.Vector(-63.55079999999999,50.68888000000000,0.00000000000000),App.Vector(63.55080000000000,50.68888000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC").addGeometry(Part.LineSegment(App.Vector(63.55080000000000,76.05713000000000,0.00000000000000),App.Vector(63.55080000000000,50.68888000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Pad","Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC")
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC")
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").Length = 100.838
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoAVa6lykBIWL5R_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoAVa6lykBIWL5R_1_FeDNO9v304U0Hen_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Plane", "plane_Sketch_FUc63UhEqLu1LEb_1_JRC")
origin = App.Vector(-60.04560000000000,63.37300000000000,5.00380000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUc63UhEqLu1LEb_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("Sketcher::SketchObject","Sketch_FUc63UhEqLu1LEb_1_JRC")
App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUc63UhEqLu1LEb_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC").addGeometry(Part.LineSegment(App.Vector(-57.30240000000001,56.41340000000000,0.00000000000000),App.Vector(-46.63440000000001,56.41340000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC").addGeometry(Part.LineSegment(App.Vector(-46.63440000000001,56.41340000000000,0.00000000000000),App.Vector(-46.63440000000001,-37.76980000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC").addGeometry(Part.LineSegment(App.Vector(-57.30240000000001,-37.76980000000000,0.00000000000000),App.Vector(-46.63440000000001,-37.76980000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC").addGeometry(Part.LineSegment(App.Vector(-57.30240000000001,56.41340000000000,0.00000000000000),App.Vector(-57.30240000000001,-37.76980000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Pocket","Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC")
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC")
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").Length = 124.96799999999998
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUc63UhEqLu1LEb_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUc63UhEqLu1LEb_1_F6w5fHsAl999Czr_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Plane", "plane_Sketch_FljnNS8UuBP8aQw_1_JVC")
origin = App.Vector(3.50520000000000,101.37775000000001,17.65300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FljnNS8UuBP8aQw_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("Sketcher::SketchObject","Sketch_FljnNS8UuBP8aQw_1_JVC")
App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FljnNS8UuBP8aQw_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC").addGeometry(Part.LineSegment(App.Vector(-59.89320000000000,-46.15180000000000,0.00000000000000),App.Vector(59.58840000000000,-46.15180000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC").addGeometry(Part.LineSegment(App.Vector(59.58840000000000,-46.15180000000000,0.00000000000000),App.Vector(59.58840000000000,45.89780000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC").addGeometry(Part.LineSegment(App.Vector(-59.89320000000000,45.89780000000000,0.00000000000000),App.Vector(59.58840000000000,45.89780000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC").addGeometry(Part.LineSegment(App.Vector(-59.89320000000000,-46.15180000000000,0.00000000000000),App.Vector(-59.89320000000000,45.89780000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Pocket","Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC")
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC")
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").Length = 19.304000000000002
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FljnNS8UuBP8aQw_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FljnNS8UuBP8aQw_1_FAsGbYn3Q9N4y3g_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Plane", "plane_Sketch_FdUAMrbafAg438Q_1_JZC")
origin = App.Vector(3.50520000000000,50.68886999999999,-32.76600000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdUAMrbafAg438Q_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("Sketcher::SketchObject","Sketch_FdUAMrbafAg438Q_1_JZC")
App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdUAMrbafAg438Q_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZC").addGeometry(Part.Circle(App.Vector(15.57172000000000,-26.02471000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.64144000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Pocket","Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC")
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZC")
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").Length = 25.4
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Plane", "plane_Sketch_FdUAMrbafAg438Q_1_JZG")
origin = App.Vector(3.50520000000000,50.68886999999999,-32.76600000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdUAMrbafAg438Q_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("Sketcher::SketchObject","Sketch_FdUAMrbafAg438Q_1_JZG")
App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdUAMrbafAg438Q_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZG").addGeometry(Part.Circle(App.Vector(44.39006000000001,-26.02471000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.81617000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Pocket","Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG")
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZG")
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").Length = 25.4
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Plane", "plane_Sketch_FdUAMrbafAg438Q_1_JZK")
origin = App.Vector(3.50520000000000,50.68886999999999,-32.76600000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdUAMrbafAg438Q_1_JZK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("Sketcher::SketchObject","Sketch_FdUAMrbafAg438Q_1_JZK")
App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdUAMrbafAg438Q_1_JZK"), [""])
App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZK").addGeometry(Part.Circle(App.Vector(-39.22370000000000,-26.02471000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.75460000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUMX2Ewx873BA3l_0").newObject("PartDesign::Pocket","Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK")
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").Profile = App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZK")
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").Length = 25.4
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdUAMrbafAg438Q_1_JZK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").Type = 4
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdUAMrbafAg438Q_1_FHONb023pnPfasU_1_JZK").Offset = 0
App.ActiveDocument.recompute()

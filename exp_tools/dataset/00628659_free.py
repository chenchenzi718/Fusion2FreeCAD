import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00628659")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fz0iZdRW2piLTQM_0")
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").Label = "Body_Fz0iZdRW2piLTQM_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Plane", "plane_Sketch_Fz0iZdRW2piLTQM_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fz0iZdRW2piLTQM_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("Sketcher::SketchObject","Sketch_Fz0iZdRW2piLTQM_0_JGC")
App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fz0iZdRW2piLTQM_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,25.00000000000000,0.00000000000000),App.Vector(25.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,25.00000000000000,0.00000000000000),App.Vector(25.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(25.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Pad","Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC")
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC")
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").Length = 450.0
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fz0iZdRW2piLTQM_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fz0iZdRW2piLTQM_0_FNvipgxwagXGV3V_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Plane", "plane_Sketch_F17QMom0w0RIaCj_1_JJC")
origin = App.Vector(225.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F17QMom0w0RIaCj_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("Sketcher::SketchObject","Sketch_F17QMom0w0RIaCj_1_JJC")
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F17QMom0w0RIaCj_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJC").addGeometry(Part.Circle(App.Vector(-10.00000000000000,10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Pocket","Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC")
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJC")
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Plane", "plane_Sketch_F17QMom0w0RIaCj_1_JJG")
origin = App.Vector(225.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F17QMom0w0RIaCj_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("Sketcher::SketchObject","Sketch_F17QMom0w0RIaCj_1_JJG")
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F17QMom0w0RIaCj_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJG").addGeometry(Part.Circle(App.Vector(10.00000000000000,10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Pocket","Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG")
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJG")
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").Length = 25.0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Plane", "plane_Sketch_F17QMom0w0RIaCj_1_JJO")
origin = App.Vector(225.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F17QMom0w0RIaCj_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("Sketcher::SketchObject","Sketch_F17QMom0w0RIaCj_1_JJO")
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F17QMom0w0RIaCj_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJO").addGeometry(Part.Circle(App.Vector(10.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Pocket","Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO")
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJO")
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").Length = 25.0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Plane", "plane_Sketch_F17QMom0w0RIaCj_1_JJK")
origin = App.Vector(225.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F17QMom0w0RIaCj_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("Sketcher::SketchObject","Sketch_F17QMom0w0RIaCj_1_JJK")
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F17QMom0w0RIaCj_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJK").addGeometry(Part.Circle(App.Vector(-10.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Pocket","Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK")
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJK")
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").Length = 25.0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F17QMom0w0RIaCj_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F17QMom0w0RIaCj_1_F0kP6ePncUQm8LM_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Plane", "plane_Sketch_F28BtROslnfJRP0_5_JNC")
origin = App.Vector(-225.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F28BtROslnfJRP0_5_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("Sketcher::SketchObject","Sketch_F28BtROslnfJRP0_5_JNC")
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F28BtROslnfJRP0_5_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNC").addGeometry(Part.Circle(App.Vector(-10.00000000000000,10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Pocket","Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC")
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").Profile = App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNC")
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Plane", "plane_Sketch_F28BtROslnfJRP0_5_JNG")
origin = App.Vector(-225.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F28BtROslnfJRP0_5_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("Sketcher::SketchObject","Sketch_F28BtROslnfJRP0_5_JNG")
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F28BtROslnfJRP0_5_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNG").addGeometry(Part.Circle(App.Vector(10.00000000000000,10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Pocket","Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG")
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").Profile = App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNG")
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Plane", "plane_Sketch_F28BtROslnfJRP0_5_JNO")
origin = App.Vector(-225.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F28BtROslnfJRP0_5_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("Sketcher::SketchObject","Sketch_F28BtROslnfJRP0_5_JNO")
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F28BtROslnfJRP0_5_JNO"), [""])
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNO").addGeometry(Part.Circle(App.Vector(10.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Pocket","Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO")
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").Profile = App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNO")
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").Length = 25.0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Plane", "plane_Sketch_F28BtROslnfJRP0_5_JNK")
origin = App.Vector(-225.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F28BtROslnfJRP0_5_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("Sketcher::SketchObject","Sketch_F28BtROslnfJRP0_5_JNK")
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F28BtROslnfJRP0_5_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNK").addGeometry(Part.Circle(App.Vector(-10.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fz0iZdRW2piLTQM_0").newObject("PartDesign::Pocket","Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK")
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").Profile = App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNK")
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").Length = 25.0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F28BtROslnfJRP0_5_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F28BtROslnfJRP0_5_FEi8b8peYH4ufEJ_5_JNK").Offset = 0
App.ActiveDocument.recompute()

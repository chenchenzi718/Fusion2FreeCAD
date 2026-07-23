import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00694828")
App.ActiveDocument.addObject("PartDesign::Body","Body_F3VsP0HrK9PlERb_0")
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").Label = "Body_F3VsP0HrK9PlERb_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Plane", "plane_Sketch_F3VsP0HrK9PlERb_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3VsP0HrK9PlERb_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("Sketcher::SketchObject","Sketch_F3VsP0HrK9PlERb_0_JGC")
App.ActiveDocument.getObject("Sketch_F3VsP0HrK9PlERb_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3VsP0HrK9PlERb_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F3VsP0HrK9PlERb_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3VsP0HrK9PlERb_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),40.64000000000000),False)

App.ActiveDocument.getObject("Sketch_F3VsP0HrK9PlERb_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),20.32000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3VsP0HrK9PlERb_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3VsP0HrK9PlERb_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Pad","Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC")
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F3VsP0HrK9PlERb_0_JGC")
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").Length = 10.160000000000002
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3VsP0HrK9PlERb_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3VsP0HrK9PlERb_0_FOCLG9z1fTrg1Qr_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Plane", "plane_Sketch_FMcxkDuQKDO214v_1_JLC")
origin = App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("Sketcher::SketchObject","Sketch_FMcxkDuQKDO214v_1_JLC")
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLC").addGeometry(Part.Circle(App.Vector(-31.36900000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.48198000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Pocket","Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLC")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Plane", "plane_Sketch_FMcxkDuQKDO214v_1_JLG")
origin = App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("Sketcher::SketchObject","Sketch_FMcxkDuQKDO214v_1_JLG")
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLG").addGeometry(Part.Circle(App.Vector(-23.24100000000000,-20.70100000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.18009000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Pocket","Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLG")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Plane", "plane_Sketch_FMcxkDuQKDO214v_1_JLK")
origin = App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("Sketcher::SketchObject","Sketch_FMcxkDuQKDO214v_1_JLK")
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLK").addGeometry(Part.Circle(App.Vector(0.00000000000000,-31.87700000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.15720000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Pocket","Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLK")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Plane", "plane_Sketch_FMcxkDuQKDO214v_1_JLO")
origin = App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("Sketcher::SketchObject","Sketch_FMcxkDuQKDO214v_1_JLO")
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLO").addGeometry(Part.Circle(App.Vector(19.43100000000000,-21.71700000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.28361000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Pocket","Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLO")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Plane", "plane_Sketch_FMcxkDuQKDO214v_1_JLS")
origin = App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("Sketcher::SketchObject","Sketch_FMcxkDuQKDO214v_1_JLS")
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLS"), [""])
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLS").addGeometry(Part.Circle(App.Vector(31.62300000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.05485000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Pocket","Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").Profile = App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLS")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").Type = 4
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Plane", "plane_Sketch_FMcxkDuQKDO214v_1_JLW")
origin = App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("Sketcher::SketchObject","Sketch_FMcxkDuQKDO214v_1_JLW")
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLW"), [""])
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLW").addGeometry(Part.Circle(App.Vector(20.44700000000000,23.24100000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.18008000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Pocket","Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").Profile = App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLW")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").Type = 4
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Plane", "plane_Sketch_FMcxkDuQKDO214v_1_JLa")
origin = App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("Sketcher::SketchObject","Sketch_FMcxkDuQKDO214v_1_JLa")
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLa"), [""])
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLa").addGeometry(Part.Circle(App.Vector(-3.93700000000000,31.87700000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.53032000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Pocket","Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").Profile = App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLa")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").Type = 4
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Plane", "plane_Sketch_FMcxkDuQKDO214v_1_JLe")
origin = App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("Sketcher::SketchObject","Sketch_FMcxkDuQKDO214v_1_JLe")
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcxkDuQKDO214v_1_JLe"), [""])
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLe").addGeometry(Part.Circle(App.Vector(-24.00300000000000,19.17700000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.68170000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3VsP0HrK9PlERb_0").newObject("PartDesign::Pocket","Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").Profile = App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLe")
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcxkDuQKDO214v_1_JLe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").Type = 4
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcxkDuQKDO214v_1_FSwUIxzBe3TQXkr_1_JLe").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00577043")
App.ActiveDocument.addObject("PartDesign::Body","Body_FOPNksGBFCmVAy8_0")
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").Label = "Body_FOPNksGBFCmVAy8_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Plane", "plane_Sketch_FOPNksGBFCmVAy8_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOPNksGBFCmVAy8_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("Sketcher::SketchObject","Sketch_FOPNksGBFCmVAy8_0_JGC")
App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOPNksGBFCmVAy8_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-100.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC").addGeometry(Part.LineSegment(App.Vector(-100.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-100.00000000000000,100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,100.00000000000000,0.00000000000000),App.Vector(-100.00000000000000,100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Pad","Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC")
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC")
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOPNksGBFCmVAy8_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOPNksGBFCmVAy8_0_Fez8FBAQnAvBDt7_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Plane", "plane_Sketch_Fj16JtCBRqVCn6R_1_JJC")
origin = App.Vector(-50.00000000000000,0.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj16JtCBRqVCn6R_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("Sketcher::SketchObject","Sketch_Fj16JtCBRqVCn6R_1_JJC")
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj16JtCBRqVCn6R_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJC").addGeometry(Part.Circle(App.Vector(-39.99999999999999,39.99999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Pocket","Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC")
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJC")
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Plane", "plane_Sketch_Fj16JtCBRqVCn6R_1_JJG")
origin = App.Vector(-50.00000000000000,0.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj16JtCBRqVCn6R_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("Sketcher::SketchObject","Sketch_Fj16JtCBRqVCn6R_1_JJG")
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj16JtCBRqVCn6R_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJG").addGeometry(Part.Circle(App.Vector(40.00000000000000,39.99999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Pocket","Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG")
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJG")
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Plane", "plane_Sketch_Fj16JtCBRqVCn6R_1_JJK")
origin = App.Vector(-50.00000000000000,0.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj16JtCBRqVCn6R_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("Sketcher::SketchObject","Sketch_Fj16JtCBRqVCn6R_1_JJK")
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj16JtCBRqVCn6R_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJK").addGeometry(Part.Circle(App.Vector(40.00000000000000,-40.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Pocket","Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK")
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJK")
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Plane", "plane_Sketch_Fj16JtCBRqVCn6R_1_JJO")
origin = App.Vector(-50.00000000000000,0.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj16JtCBRqVCn6R_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("Sketcher::SketchObject","Sketch_Fj16JtCBRqVCn6R_1_JJO")
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj16JtCBRqVCn6R_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJO").addGeometry(Part.Circle(App.Vector(-39.99999999999999,-40.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Pocket","Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO")
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJO")
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj16JtCBRqVCn6R_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj16JtCBRqVCn6R_1_F0AHv0SGKDdKjLC_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Plane", "plane_Sketch_FCa8HZ7tiLNvoLl_1_JNC")
origin = App.Vector(-50.00000000000000,0.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCa8HZ7tiLNvoLl_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("Sketcher::SketchObject","Sketch_FCa8HZ7tiLNvoLl_1_JNC")
App.ActiveDocument.getObject("Sketch_FCa8HZ7tiLNvoLl_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCa8HZ7tiLNvoLl_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FCa8HZ7tiLNvoLl_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCa8HZ7tiLNvoLl_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCa8HZ7tiLNvoLl_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCa8HZ7tiLNvoLl_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Pocket","Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC")
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FCa8HZ7tiLNvoLl_1_JNC")
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCa8HZ7tiLNvoLl_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCa8HZ7tiLNvoLl_1_FieofNO7qWFvfeJ_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Plane", "plane_Sketch_FI3GgRBQIJTWJE1_1_JRS")
origin = App.Vector(-50.00000000000000,0.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FI3GgRBQIJTWJE1_1_JRS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("Sketcher::SketchObject","Sketch_FI3GgRBQIJTWJE1_1_JRS")
App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FI3GgRBQIJTWJE1_1_JRS"), [""])
App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRS").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Pad","Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS")
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").Profile = App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRS")
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").Length = 18.000000000000004
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").Type = 4
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Plane", "plane_Sketch_FI3GgRBQIJTWJE1_1_JRW")
origin = App.Vector(-50.00000000000000,0.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FI3GgRBQIJTWJE1_1_JRW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("Sketcher::SketchObject","Sketch_FI3GgRBQIJTWJE1_1_JRW")
App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FI3GgRBQIJTWJE1_1_JRW"), [""])
App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,35.00000000000000,0.00000000000000),App.Vector(20.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(20.00000000000000,20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,20.00000000000000,0.00000000000000),App.Vector(35.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(20.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-20.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").addGeometry(Part.LineSegment(App.Vector(-35.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-35.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-20.00000000000000,20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Pad","Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW")
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").Profile = App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW")
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").Length = 18.000000000000004
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FI3GgRBQIJTWJE1_1_JRW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").Type = 4
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FI3GgRBQIJTWJE1_1_FjPDPVNXsQarj35_1_JRW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Plane", "plane_Sketch_FfV7OxYpoCVbF9P_1_JTC")
origin = App.Vector(-50.00000000000000,0.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfV7OxYpoCVbF9P_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("Sketcher::SketchObject","Sketch_FfV7OxYpoCVbF9P_1_JTC")
App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfV7OxYpoCVbF9P_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,30.00000000000000,0.00000000000000),App.Vector(20.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(20.00000000000000,20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,20.00000000000000,0.00000000000000),App.Vector(30.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(20.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-30.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-20.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-20.00000000000000,20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FOPNksGBFCmVAy8_0").newObject("PartDesign::Pocket","Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC")
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC")
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfV7OxYpoCVbF9P_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").Type = 0
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfV7OxYpoCVbF9P_1_FK8v2edHU8lfQdn_1_JTC").Offset = 0
App.ActiveDocument.recompute()

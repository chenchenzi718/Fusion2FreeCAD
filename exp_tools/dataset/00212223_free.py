import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00212223")
App.ActiveDocument.addObject("PartDesign::Body","Body_F1paRBLzH6P92U9_1")
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").Label = "Body_F1paRBLzH6P92U9_1"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_F1paRBLzH6P92U9_1_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1paRBLzH6P92U9_1_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_F1paRBLzH6P92U9_1_JGC")
App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1paRBLzH6P92U9_1_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC").addGeometry(Part.LineSegment(App.Vector(-14.13768000000000,50.76707000000000,0.00000000000000),App.Vector(-14.13768000000000,-18.12676000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC").addGeometry(Part.LineSegment(App.Vector(-14.13768000000000,-18.12676000000000,0.00000000000000),App.Vector(24.08783000000000,-18.12676000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC").addGeometry(Part.LineSegment(App.Vector(24.08783000000000,50.76707000000000,0.00000000000000),App.Vector(24.08783000000000,-18.12676000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC").addGeometry(Part.LineSegment(App.Vector(-14.13768000000000,50.76707000000000,0.00000000000000),App.Vector(24.08783000000000,50.76707000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pad","Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC")
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").Profile = App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC")
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").Length = 5.0
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1paRBLzH6P92U9_1_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1paRBLzH6P92U9_1_FrM0S1BdwquSU4h_1_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_F6hY2jKIGn6grS7_2_JJC")
origin = App.Vector(5.09230000000000,16.32015000000000,-5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6hY2jKIGn6grS7_2_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_F6hY2jKIGn6grS7_2_JJC")
App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6hY2jKIGn6grS7_2_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,-14.69469000000000,0.00000000000000),App.Vector(-19.22998000000000,-14.69469000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC").addGeometry(Part.LineSegment(App.Vector(-19.22998000000000,-14.69469000000000,0.00000000000000),App.Vector(-19.22998000000000,10.21534000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,10.21534000000000,0.00000000000000),App.Vector(-19.22998000000000,10.21534000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,-14.69469000000000,0.00000000000000),App.Vector(-50.00000000000000,10.21534000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pad","Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC")
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").Profile = App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC")
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").Length = 5.0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_F6hY2jKIGn6grS7_2_JJG")
origin = App.Vector(5.09230000000000,16.32015000000000,-5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6hY2jKIGn6grS7_2_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_F6hY2jKIGn6grS7_2_JJG")
App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6hY2jKIGn6grS7_2_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG").addGeometry(Part.LineSegment(App.Vector(49.99999999999999,-14.69469000000000,0.00000000000000),App.Vector(18.99553000000000,-14.69469000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG").addGeometry(Part.LineSegment(App.Vector(18.99553000000000,-14.69469000000000,0.00000000000000),App.Vector(18.99553000000000,10.21534000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG").addGeometry(Part.LineSegment(App.Vector(49.99999999999999,10.21534000000000,0.00000000000000),App.Vector(18.99553000000000,10.21534000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG").addGeometry(Part.LineSegment(App.Vector(49.99999999999999,-14.69469000000000,0.00000000000000),App.Vector(49.99999999999999,10.21534000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pad","Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG")
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").Profile = App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG")
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").Length = 5.0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_F6hY2jKIGn6grS7_2_JJS")
origin = App.Vector(5.09230000000000,16.32015000000000,-5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6hY2jKIGn6grS7_2_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_F6hY2jKIGn6grS7_2_JJS")
App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6hY2jKIGn6grS7_2_JJS"), [""])
App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS").addGeometry(Part.LineSegment(App.Vector(-19.22998000000000,-14.69469000000000,0.00000000000000),App.Vector(18.99553000000000,-14.69469000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS").addGeometry(Part.LineSegment(App.Vector(18.99553000000000,-14.69469000000000,0.00000000000000),App.Vector(18.99553000000000,10.21534000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS").addGeometry(Part.LineSegment(App.Vector(-19.22998000000000,10.21534000000000,0.00000000000000),App.Vector(18.99553000000000,10.21534000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS").addGeometry(Part.LineSegment(App.Vector(-19.22998000000000,-14.69469000000000,0.00000000000000),App.Vector(-19.22998000000000,10.21534000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pad","Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS")
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").Profile = App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS")
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").Length = 5.0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6hY2jKIGn6grS7_2_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").Type = 0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").Reversed = 1
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6hY2jKIGn6grS7_2_Fb56vzZOPQSBYdr_2_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_FeiYz6D2rMEppKz_2_JNC")
origin = App.Vector(5.09230000000000,16.32015000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeiYz6D2rMEppKz_2_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_FeiYz6D2rMEppKz_2_JNC")
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeiYz6D2rMEppKz_2_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNC").addGeometry(Part.Circle(App.Vector(-46.47993000000000,11.25578000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.85000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pocket","Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC")
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").Profile = App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNC")
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_FeiYz6D2rMEppKz_2_JNG")
origin = App.Vector(5.09230000000000,16.32015000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeiYz6D2rMEppKz_2_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_FeiYz6D2rMEppKz_2_JNG")
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeiYz6D2rMEppKz_2_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNG").addGeometry(Part.Circle(App.Vector(46.50745000000000,11.19425000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.85000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pocket","Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG")
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").Profile = App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNG")
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_FeiYz6D2rMEppKz_2_JNK")
origin = App.Vector(5.09230000000000,16.32015000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeiYz6D2rMEppKz_2_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_FeiYz6D2rMEppKz_2_JNK")
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeiYz6D2rMEppKz_2_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNK").addGeometry(Part.Circle(App.Vector(-46.50598000000000,-6.75575000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.85000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pocket","Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK")
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").Profile = App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNK")
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_FeiYz6D2rMEppKz_2_JNO")
origin = App.Vector(5.09230000000000,16.32015000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeiYz6D2rMEppKz_2_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_FeiYz6D2rMEppKz_2_JNO")
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeiYz6D2rMEppKz_2_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNO").addGeometry(Part.Circle(App.Vector(46.53267000000000,-6.61721000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.85000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pocket","Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO")
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").Profile = App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNO")
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeiYz6D2rMEppKz_2_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeiYz6D2rMEppKz_2_Fsx61707gYc73gQ_2_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_Fry1sojZk37hurR_2_JRC")
origin = App.Vector(5.09230000000000,16.32015000000000,-5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fry1sojZk37hurR_2_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_Fry1sojZk37hurR_2_JRC")
App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fry1sojZk37hurR_2_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC").addGeometry(Part.LineSegment(App.Vector(-12.72998000000000,30.91329000000000,0.00000000000000),App.Vector(12.27002000000000,30.91329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC").addGeometry(Part.LineSegment(App.Vector(12.27002000000000,30.91329000000000,0.00000000000000),App.Vector(12.27002000000000,10.91329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC").addGeometry(Part.LineSegment(App.Vector(-12.72998000000000,10.91329000000000,0.00000000000000),App.Vector(12.27002000000000,10.91329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC").addGeometry(Part.LineSegment(App.Vector(-12.72998000000000,30.91329000000000,0.00000000000000),App.Vector(-12.72998000000000,10.91329000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pad","Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC")
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC")
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fry1sojZk37hurR_2_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fry1sojZk37hurR_2_FJ5IVRxyDXB9lSU_2_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Plane", "plane_Sketch_F1RwocoMHEbkdaj_2_JVC")
origin = App.Vector(4.86232000000000,-4.59314000000000,-15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1RwocoMHEbkdaj_2_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("Sketcher::SketchObject","Sketch_F1RwocoMHEbkdaj_2_JVC")
App.ActiveDocument.getObject("Sketch_F1RwocoMHEbkdaj_2_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1RwocoMHEbkdaj_2_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F1RwocoMHEbkdaj_2_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1RwocoMHEbkdaj_2_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1RwocoMHEbkdaj_2_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1RwocoMHEbkdaj_2_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1paRBLzH6P92U9_1").newObject("PartDesign::Pocket","Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC")
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").Profile = App.ActiveDocument.getObject("Sketch_F1RwocoMHEbkdaj_2_JVC")
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").Length = 5.0
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1RwocoMHEbkdaj_2_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1RwocoMHEbkdaj_2_FIoSh50DMonWiOq_2_JVC").Offset = 0
App.ActiveDocument.recompute()

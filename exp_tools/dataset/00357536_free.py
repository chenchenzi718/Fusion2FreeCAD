import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00357536")
App.ActiveDocument.addObject("PartDesign::Body","Body_FORX0LHPl09Bn7K_0")
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").Label = "Body_FORX0LHPl09Bn7K_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_FORX0LHPl09Bn7K_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FORX0LHPl09Bn7K_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_FORX0LHPl09Bn7K_0_JGC")
App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FORX0LHPl09Bn7K_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.66366000000000,-15.43345000000000,0.00000000000000),App.Vector(-50.66366000000000,-28.13345000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.66366000000000,-28.13345000000000,0.00000000000000),App.Vector(0.13634000000000,-28.13345000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.13634000000000,-28.13345000000000,0.00000000000000),App.Vector(0.13634000000000,-15.43345000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.13634000000000,-15.43345000000000,0.00000000000000),App.Vector(-12.56366000000000,-15.43345000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").addGeometry(Part.LineSegment(App.Vector(-12.56366000000000,-15.43345000000000,0.00000000000000),App.Vector(-12.56366000000000,3.61655000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").addGeometry(Part.LineSegment(App.Vector(-12.56366000000000,3.61655000000000,0.00000000000000),App.Vector(-37.96366000000000,3.61655000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").addGeometry(Part.LineSegment(App.Vector(-37.96366000000000,3.61655000000000,0.00000000000000),App.Vector(-37.96366000000000,-15.43345000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.66366000000000,-15.43345000000000,0.00000000000000),App.Vector(-37.96366000000000,-15.43345000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pad","Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC")
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC")
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FORX0LHPl09Bn7K_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FORX0LHPl09Bn7K_0_FI5UP3jygNYXpXb_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_FkpELiY0stQNpRq_1_JJC")
origin = App.Vector(-50.73986000000000,-12.70000000000000,-15.43345000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkpELiY0stQNpRq_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_FkpELiY0stQNpRq_1_JJC")
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkpELiY0stQNpRq_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJC").addGeometry(Part.LineSegment(App.Vector(50.87620000000000,12.70000000000000,0.00000000000000),App.Vector(50.87620000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJC").addGeometry(Part.LineSegment(App.Vector(50.87620000000000,0.00000000000000,0.00000000000000),App.Vector(63.57620000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(50.87620000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.70000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pad","Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC")
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJC")
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_FkpELiY0stQNpRq_1_JJG")
origin = App.Vector(-50.73986000000000,-12.70000000000000,-15.43345000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkpELiY0stQNpRq_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_FkpELiY0stQNpRq_1_JJG")
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkpELiY0stQNpRq_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJG").addGeometry(Part.LineSegment(App.Vector(50.87620000000000,0.00000000000000,0.00000000000000),App.Vector(50.87620000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(50.87620000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.70000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJG").addGeometry(Part.LineSegment(App.Vector(50.87620000000000,0.00000000000000,0.00000000000000),App.Vector(63.57620000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pad","Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG")
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJG")
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_FkpELiY0stQNpRq_1_JJO")
origin = App.Vector(-50.73986000000000,-12.70000000000000,-15.43345000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkpELiY0stQNpRq_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_FkpELiY0stQNpRq_1_JJO")
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkpELiY0stQNpRq_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJO").addGeometry(Part.LineSegment(App.Vector(0.07620000000000,12.70000000000000,0.00000000000000),App.Vector(0.07620000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJO").addGeometry(Part.LineSegment(App.Vector(0.07620000000000,0.00000000000000,0.00000000000000),App.Vector(-12.62380000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.07620000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.70000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pad","Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO")
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJO")
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").Type = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").Reversed = 1
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_FkpELiY0stQNpRq_1_JJS")
origin = App.Vector(-50.73986000000000,-12.70000000000000,-15.43345000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkpELiY0stQNpRq_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_FkpELiY0stQNpRq_1_JJS")
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkpELiY0stQNpRq_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJS").addGeometry(Part.LineSegment(App.Vector(0.07620000000000,-12.70000000000000,0.00000000000000),App.Vector(0.07620000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJS").addGeometry(Part.LineSegment(App.Vector(0.07620000000000,0.00000000000000,0.00000000000000),App.Vector(-12.62380000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.07620000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.70000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pad","Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS")
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJS")
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkpELiY0stQNpRq_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").Type = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").Reversed = 1
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkpELiY0stQNpRq_1_F49Ed4Lg7OkTSUY_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_F5LGGWEFoSBLVYc_1_JNG")
origin = App.Vector(-12.56366000000000,-12.70000000000000,0.53680000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5LGGWEFoSBLVYc_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_F5LGGWEFoSBLVYc_1_JNG")
App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5LGGWEFoSBLVYc_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNG").addGeometry(Part.LineSegment(App.Vector(-12.70000000000000,3.07975000000000,0.00000000000000),App.Vector(0.00000000000000,3.07975000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,3.07975000000000,0.00000000000000),App.Vector(0.00000000000000,15.77975000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,3.07975000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.70000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pad","Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG")
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNG")
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").Type = 0
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").Reversed = 1
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_F5LGGWEFoSBLVYc_1_JNK")
origin = App.Vector(-12.56366000000000,-12.70000000000000,0.53680000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5LGGWEFoSBLVYc_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_F5LGGWEFoSBLVYc_1_JNK")
App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5LGGWEFoSBLVYc_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNK").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,3.07975000000000,0.00000000000000),App.Vector(0.00000000000000,3.07975000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,3.07975000000000,0.00000000000000),App.Vector(0.00000000000000,15.77975000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,3.07975000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.70000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pad","Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK")
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNK")
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5LGGWEFoSBLVYc_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").Type = 0
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").Reversed = 1
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5LGGWEFoSBLVYc_1_FsK9RGL2RdFnChL_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_F54VXXaJv040Wyv_1_JRG")
origin = App.Vector(-12.56366000000000,-12.70000000000000,0.53680000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F54VXXaJv040Wyv_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_F54VXXaJv040Wyv_1_JRG")
App.ActiveDocument.getObject("Sketch_F54VXXaJv040Wyv_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F54VXXaJv040Wyv_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_F54VXXaJv040Wyv_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F54VXXaJv040Wyv_1_JRG").addGeometry(Part.Circle(App.Vector(0.00000000000000,3.07975000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F54VXXaJv040Wyv_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F54VXXaJv040Wyv_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pocket","Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG")
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_F54VXXaJv040Wyv_1_JRG")
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F54VXXaJv040Wyv_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F54VXXaJv040Wyv_1_FkLqbg2dOvhYLA1_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_FSqx2YwfD5d8gWP_1_JVK")
origin = App.Vector(-50.73986000000000,-12.70000000000000,-15.43345000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSqx2YwfD5d8gWP_1_JVK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_FSqx2YwfD5d8gWP_1_JVK")
App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSqx2YwfD5d8gWP_1_JVK"), [""])
App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVK").addGeometry(Part.Circle(App.Vector(0.07620000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pocket","Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK")
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").Profile = App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVK")
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").Type = 4
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Plane", "plane_Sketch_FSqx2YwfD5d8gWP_1_JVC")
origin = App.Vector(-50.73986000000000,-12.70000000000000,-15.43345000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSqx2YwfD5d8gWP_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("Sketcher::SketchObject","Sketch_FSqx2YwfD5d8gWP_1_JVC")
App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSqx2YwfD5d8gWP_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVC").addGeometry(Part.Circle(App.Vector(50.87620000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FORX0LHPl09Bn7K_0").newObject("PartDesign::Pocket","Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC")
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVC")
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSqx2YwfD5d8gWP_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSqx2YwfD5d8gWP_1_FyA84820LJBAg8M_1_JVC").Offset = 0
App.ActiveDocument.recompute()

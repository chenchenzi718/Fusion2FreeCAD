import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00900095")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fqb75gYB7twGN7A_0")
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").Label = "Body_Fqb75gYB7twGN7A_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Plane", "plane_Sketch_Fqb75gYB7twGN7A_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fqb75gYB7twGN7A_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("Sketcher::SketchObject","Sketch_Fqb75gYB7twGN7A_0_JGC")
App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fqb75gYB7twGN7A_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC").addGeometry(Part.LineSegment(App.Vector(195.57359000000000,-106.22231000000001,0.00000000000000),App.Vector(195.57359000000000,-69.84999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC").addGeometry(Part.LineSegment(App.Vector(195.57359000000000,-69.84999999999999,0.00000000000000),App.Vector(0.00000000000000,125.72359000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,125.72359000000000,0.00000000000000),App.Vector(-107.95000000000000,125.72359000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC").addGeometry(Part.LineSegment(App.Vector(-107.95000000000000,125.72359000000000,0.00000000000000),App.Vector(-107.95000000000000,-106.22231000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC").addGeometry(Part.LineSegment(App.Vector(195.57359000000000,-106.22231000000001,0.00000000000000),App.Vector(-107.95000000000000,-106.22231000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Pad","Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC")
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC")
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").Length = 1143.0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Plane", "plane_Sketch_Fqb75gYB7twGN7A_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fqb75gYB7twGN7A_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("Sketcher::SketchObject","Sketch_Fqb75gYB7twGN7A_0_JGG")
App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fqb75gYB7twGN7A_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG").addGeometry(Part.LineSegment(App.Vector(195.57359000000000,-106.22231000000001,0.00000000000000),App.Vector(195.57359000000000,-69.84999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG").addGeometry(Part.LineSegment(App.Vector(195.57359000000000,-69.84999999999999,0.00000000000000),App.Vector(195.57359000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG").addGeometry(Part.LineSegment(App.Vector(276.39588999999995,-80.82230999999999,0.00000000000000),App.Vector(195.57359000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG").addGeometry(Part.LineSegment(App.Vector(276.39588999999995,-80.82230999999999,0.00000000000000),App.Vector(276.39588999999995,-106.22231000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG").addGeometry(Part.LineSegment(App.Vector(195.57359000000000,-106.22231000000001,0.00000000000000),App.Vector(276.39588999999995,-106.22231000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Pad","Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG")
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG")
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").Length = 1143.0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").Type = 0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Plane", "plane_Sketch_Fqb75gYB7twGN7A_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fqb75gYB7twGN7A_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("Sketcher::SketchObject","Sketch_Fqb75gYB7twGN7A_0_JGK")
App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fqb75gYB7twGN7A_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK").addGeometry(Part.LineSegment(App.Vector(195.57359000000000,-69.84999999999999,0.00000000000000),App.Vector(195.57359000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK").addGeometry(Part.LineSegment(App.Vector(195.57359000000000,0.00000000000000,0.00000000000000),App.Vector(69.84999999999999,125.72359000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,125.72359000000000,0.00000000000000),App.Vector(69.84999999999999,125.72359000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK").addGeometry(Part.LineSegment(App.Vector(195.57359000000000,-69.84999999999999,0.00000000000000),App.Vector(0.00000000000000,125.72359000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Pad","Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK")
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK")
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").Length = 1143.0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fqb75gYB7twGN7A_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").Type = 0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fqb75gYB7twGN7A_0_FUykOOEd7Jqwjph_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Plane", "plane_Sketch_FKeNoNv2jtFzPNY_1_JJC")
origin = App.Vector(173.12295000000000,0.00000000000000,22.45064000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKeNoNv2jtFzPNY_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("Sketcher::SketchObject","Sketch_FKeNoNv2jtFzPNY_1_JJC")
App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKeNoNv2jtFzPNY_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC").addGeometry(Part.LineSegment(App.Vector(-557.15722000000005,106.54141195926181,-0.00000707106781),App.Vector(-557.15722000000005,-48.55420829761560,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC").addGeometry(Part.LineSegment(App.Vector(-557.15722000000005,-48.55420829761560,0.00000000000000),App.Vector(556.25272000000007,-48.55420829761560,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC").addGeometry(Part.LineSegment(App.Vector(556.25272000000007,106.54141195926181,-0.00000707106781),App.Vector(556.25272000000007,-48.55420829761560,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC").addGeometry(Part.LineSegment(App.Vector(-557.15722000000005,106.54141195926181,-0.00000707106781),App.Vector(556.25272000000007,106.54141195926181,-0.00000707106781)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Pocket","Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC")
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC")
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").Length = 55.88
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKeNoNv2jtFzPNY_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKeNoNv2jtFzPNY_1_FqQNsnYT7s5fhGb_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Plane", "plane_Sketch_FYQXpOcLH44BcFx_1_JNC")
origin = App.Vector(173.12295000000000,0.00000000000000,22.45064000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYQXpOcLH44BcFx_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("Sketcher::SketchObject","Sketch_FYQXpOcLH44BcFx_1_JNC")
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYQXpOcLH44BcFx_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-56.01814462458360,0.00000000000000),App.Vector(-551.75286999999992,-69.04835481303360,-0.00000000000001)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-69.04835481303360,-0.00000000000001),App.Vector(-471.28807999999998,-69.04835481303360,-0.00000000000001)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC").addGeometry(Part.LineSegment(App.Vector(-471.28807999999998,-56.01814462458360,0.00000000000000),App.Vector(-471.28807999999998,-69.04835481303360,-0.00000000000001)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-56.01814462458360,0.00000000000000),App.Vector(-471.28807999999998,-56.01814462458360,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Pad","Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC")
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC")
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").Length = 4.064
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Plane", "plane_Sketch_FYQXpOcLH44BcFx_1_JNG")
origin = App.Vector(173.12295000000000,0.00000000000000,22.45064000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYQXpOcLH44BcFx_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("Sketcher::SketchObject","Sketch_FYQXpOcLH44BcFx_1_JNG")
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYQXpOcLH44BcFx_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-75.18021510356641,0.00000000000000),App.Vector(-551.75286999999992,-89.74339036464963,0.00000000000001)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-89.74339036464963,0.00000000000001),App.Vector(-471.28807999999998,-89.74339036464963,0.00000000000001)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG").addGeometry(Part.LineSegment(App.Vector(-471.28807999999998,-75.18021510356641,0.00000000000000),App.Vector(-471.28807999999998,-89.74339036464963,0.00000000000001)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-75.18021510356641,0.00000000000000),App.Vector(-471.28807999999998,-75.18021510356641,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Pad","Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG")
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG")
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").Length = 4.064
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Plane", "plane_Sketch_FYQXpOcLH44BcFx_1_JNK")
origin = App.Vector(173.12295000000000,0.00000000000000,22.45064000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYQXpOcLH44BcFx_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("Sketcher::SketchObject","Sketch_FYQXpOcLH44BcFx_1_JNK")
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYQXpOcLH44BcFx_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-95.87526479731801,0.00000000000000),App.Vector(-551.75286999999992,-110.43843298733341,-0.00000707106779)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-110.43843298733341,-0.00000707106779),App.Vector(-471.28807999999998,-110.43843298733341,-0.00000707106779)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK").addGeometry(Part.LineSegment(App.Vector(-471.28807999999998,-95.87526479731801,0.00000000000000),App.Vector(-471.28807999999998,-110.43843298733341,-0.00000707106779)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-95.87526479731801,0.00000000000000),App.Vector(-471.28807999999998,-95.87526479731801,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Pad","Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK")
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK")
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").Length = 4.064
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Plane", "plane_Sketch_FYQXpOcLH44BcFx_1_JNO")
origin = App.Vector(173.12295000000000,0.00000000000000,22.45064000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYQXpOcLH44BcFx_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("Sketcher::SketchObject","Sketch_FYQXpOcLH44BcFx_1_JNO")
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYQXpOcLH44BcFx_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-118.86974795788382,-0.00000707106780),App.Vector(-551.75286999999992,-133.43292321896706,-0.00000707106780)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-133.43292321896706,-0.00000707106780),App.Vector(-471.28807999999998,-133.43292321896706,-0.00000707106780)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO").addGeometry(Part.LineSegment(App.Vector(-471.28807999999998,-118.86974795788382,-0.00000707106780),App.Vector(-471.28807999999998,-133.43292321896706,-0.00000707106780)),False)

App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO").addGeometry(Part.LineSegment(App.Vector(-551.75286999999992,-118.86974795788382,-0.00000707106780),App.Vector(-471.28807999999998,-118.86974795788382,-0.00000707106780)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fqb75gYB7twGN7A_0").newObject("PartDesign::Pad","Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO")
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO")
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").Length = 4.064
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYQXpOcLH44BcFx_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYQXpOcLH44BcFx_1_FjfJZePyUjKAk3d_1_JNO").Offset = 0
App.ActiveDocument.recompute()

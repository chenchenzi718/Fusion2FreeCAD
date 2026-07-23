import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00273908")
App.ActiveDocument.addObject("PartDesign::Body","Body_FxQewGwiELHuV0k_0")
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").Label = "Body_FxQewGwiELHuV0k_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Plane", "plane_Sketch_FxQewGwiELHuV0k_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxQewGwiELHuV0k_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("Sketcher::SketchObject","Sketch_FxQewGwiELHuV0k_0_JGC")
App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxQewGwiELHuV0k_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC").addGeometry(Part.LineSegment(App.Vector(-15.80000000000000,14.95000000000000,0.00000000000000),App.Vector(15.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC").addGeometry(Part.LineSegment(App.Vector(15.80000000000000,14.95000000000000,0.00000000000000),App.Vector(15.80000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC").addGeometry(Part.LineSegment(App.Vector(-15.80000000000000,-14.95000000000000,0.00000000000000),App.Vector(15.80000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC").addGeometry(Part.LineSegment(App.Vector(-15.80000000000000,14.95000000000000,0.00000000000000),App.Vector(-15.80000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Pad","Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC")
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC")
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").Length = 1.3000000000000003
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxQewGwiELHuV0k_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxQewGwiELHuV0k_0_F9CXhwCHbNkSZ4H_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Plane", "plane_Sketch_FKpj6HkwzVjFTZ9_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKpj6HkwzVjFTZ9_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("Sketcher::SketchObject","Sketch_FKpj6HkwzVjFTZ9_1_JJC")
App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKpj6HkwzVjFTZ9_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.05000000000000,12.15000000000000,0.00000000000000),App.Vector(-12.55000000000000,12.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC").addGeometry(Part.LineSegment(App.Vector(-12.55000000000000,12.15000000000000,0.00000000000000),App.Vector(-12.55000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.05000000000000,-7.35000000000000,0.00000000000000),App.Vector(-12.55000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.05000000000000,12.15000000000000,0.00000000000000),App.Vector(-15.05000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Pad","Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC")
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC")
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").Length2 = 10.0
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Plane", "plane_Sketch_FKpj6HkwzVjFTZ9_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKpj6HkwzVjFTZ9_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("Sketcher::SketchObject","Sketch_FKpj6HkwzVjFTZ9_1_JJG")
App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKpj6HkwzVjFTZ9_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG").addGeometry(Part.LineSegment(App.Vector(12.55000000000000,12.15000000000000,0.00000000000000),App.Vector(15.05000000000000,12.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG").addGeometry(Part.LineSegment(App.Vector(15.05000000000000,12.15000000000000,0.00000000000000),App.Vector(15.05000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG").addGeometry(Part.LineSegment(App.Vector(12.55000000000000,-7.35000000000000,0.00000000000000),App.Vector(15.05000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG").addGeometry(Part.LineSegment(App.Vector(12.55000000000000,12.15000000000000,0.00000000000000),App.Vector(12.55000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Pad","Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG")
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG")
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").Length = 2.0
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").Length2 = 10.0
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKpj6HkwzVjFTZ9_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKpj6HkwzVjFTZ9_1_FHew1NJRYUZhWsz_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Plane", "plane_Sketch_FMrzZ4G50nlggd3_1_JOO")
origin = App.Vector(0.00000000000000,0.00000000000000,1.30000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMrzZ4G50nlggd3_1_JOO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("Sketcher::SketchObject","Sketch_FMrzZ4G50nlggd3_1_JOO")
App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMrzZ4G50nlggd3_1_JOO"), [""])
App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,-10.30000000000000,0.00000000000000),App.Vector(4.00000000000000,-10.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO").addGeometry(Part.LineSegment(App.Vector(4.00000000000000,-10.30000000000000,0.00000000000000),App.Vector(4.00000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,-14.95000000000000,0.00000000000000),App.Vector(4.00000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,-10.30000000000000,0.00000000000000),App.Vector(-4.00000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Pad","Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO")
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").Profile = App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO")
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").Length = 3.0
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").Type = 4
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Plane", "plane_Sketch_FMrzZ4G50nlggd3_1_JOK")
origin = App.Vector(0.00000000000000,0.00000000000000,1.30000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMrzZ4G50nlggd3_1_JOK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("Sketcher::SketchObject","Sketch_FMrzZ4G50nlggd3_1_JOK")
App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMrzZ4G50nlggd3_1_JOK"), [""])
App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,-16.05000000000000,0.00000000000000),App.Vector(4.00000000000000,-16.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK").addGeometry(Part.LineSegment(App.Vector(4.00000000000000,-16.05000000000000,0.00000000000000),App.Vector(4.00000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,-14.95000000000000,0.00000000000000),App.Vector(4.00000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,-16.05000000000000,0.00000000000000),App.Vector(-4.00000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Pad","Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK")
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").Profile = App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK")
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").Length = 3.0
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMrzZ4G50nlggd3_1_JOK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").Type = 4
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMrzZ4G50nlggd3_1_FxA7N9L6yDko95X_1_JOK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Plane", "plane_Sketch_FMaTiEofhjqRDl5_1_JSS")
origin = App.Vector(0.00000000000000,0.00000000000000,1.30000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaTiEofhjqRDl5_1_JSS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("Sketcher::SketchObject","Sketch_FMaTiEofhjqRDl5_1_JSS")
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaTiEofhjqRDl5_1_JSS"), [""])
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS").addGeometry(Part.LineSegment(App.Vector(-10.80000000000000,12.65000000000000,0.00000000000000),App.Vector(-3.80000000000000,12.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS").addGeometry(Part.LineSegment(App.Vector(-3.80000000000000,12.65000000000000,0.00000000000000),App.Vector(-3.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS").addGeometry(Part.LineSegment(App.Vector(-10.80000000000000,14.95000000000000,0.00000000000000),App.Vector(-3.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS").addGeometry(Part.LineSegment(App.Vector(-10.80000000000000,12.65000000000000,0.00000000000000),App.Vector(-10.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Pad","Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS")
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").Profile = App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS")
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").Length = 4.0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").Type = 4
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Plane", "plane_Sketch_FMaTiEofhjqRDl5_1_JSK")
origin = App.Vector(0.00000000000000,0.00000000000000,1.30000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaTiEofhjqRDl5_1_JSK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("Sketcher::SketchObject","Sketch_FMaTiEofhjqRDl5_1_JSK")
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaTiEofhjqRDl5_1_JSK"), [""])
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK").addGeometry(Part.LineSegment(App.Vector(-10.80000000000000,16.15000000000000,0.00000000000000),App.Vector(-3.80000000000000,16.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK").addGeometry(Part.LineSegment(App.Vector(-3.80000000000000,16.15000000000000,0.00000000000000),App.Vector(-3.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK").addGeometry(Part.LineSegment(App.Vector(-10.80000000000000,14.95000000000000,0.00000000000000),App.Vector(-3.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK").addGeometry(Part.LineSegment(App.Vector(-10.80000000000000,16.15000000000000,0.00000000000000),App.Vector(-10.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Pad","Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK")
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").Profile = App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK")
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").Length = 4.0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").Type = 4
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Plane", "plane_Sketch_FMaTiEofhjqRDl5_1_JSO")
origin = App.Vector(0.00000000000000,0.00000000000000,1.30000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaTiEofhjqRDl5_1_JSO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("Sketcher::SketchObject","Sketch_FMaTiEofhjqRDl5_1_JSO")
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaTiEofhjqRDl5_1_JSO"), [""])
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO").addGeometry(Part.LineSegment(App.Vector(2.80000000000000,16.15000000000000,0.00000000000000),App.Vector(9.80000000000000,16.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO").addGeometry(Part.LineSegment(App.Vector(9.80000000000000,16.15000000000000,0.00000000000000),App.Vector(9.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO").addGeometry(Part.LineSegment(App.Vector(2.80000000000000,14.95000000000000,0.00000000000000),App.Vector(9.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO").addGeometry(Part.LineSegment(App.Vector(2.80000000000000,16.15000000000000,0.00000000000000),App.Vector(2.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Pad","Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO")
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").Profile = App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO")
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").Length = 4.0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").Type = 4
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Plane", "plane_Sketch_FMaTiEofhjqRDl5_1_JSW")
origin = App.Vector(0.00000000000000,0.00000000000000,1.30000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaTiEofhjqRDl5_1_JSW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("Sketcher::SketchObject","Sketch_FMaTiEofhjqRDl5_1_JSW")
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaTiEofhjqRDl5_1_JSW"), [""])
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW").addGeometry(Part.LineSegment(App.Vector(2.80000000000000,12.65000000000000,0.00000000000000),App.Vector(9.80000000000000,12.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW").addGeometry(Part.LineSegment(App.Vector(9.80000000000000,12.65000000000000,0.00000000000000),App.Vector(9.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW").addGeometry(Part.LineSegment(App.Vector(2.80000000000000,14.95000000000000,0.00000000000000),App.Vector(9.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW").addGeometry(Part.LineSegment(App.Vector(2.80000000000000,12.65000000000000,0.00000000000000),App.Vector(2.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxQewGwiELHuV0k_0").newObject("PartDesign::Pad","Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW")
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").Profile = App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW")
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").Length = 4.0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaTiEofhjqRDl5_1_JSW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").Type = 4
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaTiEofhjqRDl5_1_FcXuV9t5HCtSujH_1_JSW").Offset = 0
App.ActiveDocument.recompute()

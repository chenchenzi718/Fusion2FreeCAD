import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00511551")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fb2gCkjXbUjxXNG_0")
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").Label = "Body_Fb2gCkjXbUjxXNG_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_Fb2gCkjXbUjxXNG_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb2gCkjXbUjxXNG_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_Fb2gCkjXbUjxXNG_0_JGG")
App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb2gCkjXbUjxXNG_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").addGeometry(Part.LineSegment(App.Vector(-7.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-7.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").addGeometry(Part.LineSegment(App.Vector(-7.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(7.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").addGeometry(Part.LineSegment(App.Vector(7.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(7.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").addGeometry(Part.LineSegment(App.Vector(7.00000000000000,0.00000000000000,0.00000000000000),App.Vector(27.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").addGeometry(Part.LineSegment(App.Vector(27.00000000000000,0.00000000000000,0.00000000000000),App.Vector(27.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").addGeometry(Part.LineSegment(App.Vector(27.00000000000000,-16.00000000000000,0.00000000000000),App.Vector(-27.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,-16.00000000000000,0.00000000000000),App.Vector(-27.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").addGeometry(Part.LineSegment(App.Vector(-7.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-27.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pad","Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG")
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG")
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").Length = 16.0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").Type = 0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FP9LzPNAkafzJC9_0_JGG").Offset = 0
App.ActiveDocument.recompute()
App.ActiveDocument.addObject("PartDesign::Body","Body_Fb2gCkjXbUjxXNG_0")
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").Label = "Body_Fb2gCkjXbUjxXNG_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_Fb2gCkjXbUjxXNG_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb2gCkjXbUjxXNG_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_Fb2gCkjXbUjxXNG_0_JGO")
App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb2gCkjXbUjxXNG_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").addGeometry(Part.LineSegment(App.Vector(7.00000000000000,0.00000000000000,0.00000000000000),App.Vector(27.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").addGeometry(Part.LineSegment(App.Vector(27.00000000000000,0.00000000000000,0.00000000000000),App.Vector(27.00000000000000,3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,3.00000000000000,0.00000000000000),App.Vector(27.00000000000000,3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-27.00000000000000,3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").addGeometry(Part.LineSegment(App.Vector(-7.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-27.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").addGeometry(Part.LineSegment(App.Vector(-7.00000000000000,0.00000000000000,0.00000000000000),App.Vector(7.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pad","Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO")
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO")
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").Length = 16.0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").Type = 0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FxsiJP6B0Z3jqkz_0_JGO").Offset = 0
App.ActiveDocument.recompute()
App.ActiveDocument.addObject("PartDesign::Body","Body_Fb2gCkjXbUjxXNG_0")
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").Label = "Body_Fb2gCkjXbUjxXNG_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_Fb2gCkjXbUjxXNG_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb2gCkjXbUjxXNG_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_Fb2gCkjXbUjxXNG_0_JGC")
App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb2gCkjXbUjxXNG_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,3.00000000000000,0.00000000000000),App.Vector(27.00000000000000,3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC").addGeometry(Part.LineSegment(App.Vector(27.00000000000000,3.00000000000000,0.00000000000000),App.Vector(27.00000000000000,6.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,6.00000000000000,0.00000000000000),App.Vector(27.00000000000000,6.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,3.00000000000000,0.00000000000000),App.Vector(-27.00000000000000,6.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pad","Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC")
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC")
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").Length = 16.0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb2gCkjXbUjxXNG_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fb2gCkjXbUjxXNG_0_FLP71H3pdyAFOr5_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_FEyFWK9Kuuy8D6u_1_JLG")
origin = App.Vector(-0.00000000000000,0.00000000000000,6.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEyFWK9Kuuy8D6u_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_FEyFWK9Kuuy8D6u_1_JLG")
App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEyFWK9Kuuy8D6u_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLG").addGeometry(Part.Circle(App.Vector(-20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pocket","Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG")
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLG")
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").Length = 30.0
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_FEyFWK9Kuuy8D6u_1_JLK")
origin = App.Vector(-0.00000000000000,0.00000000000000,6.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEyFWK9Kuuy8D6u_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_FEyFWK9Kuuy8D6u_1_JLK")
App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEyFWK9Kuuy8D6u_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLK").addGeometry(Part.Circle(App.Vector(20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pocket","Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK")
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLK")
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").Length = 30.0
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_FEyFWK9Kuuy8D6u_1_JLC")
origin = App.Vector(-0.00000000000000,0.00000000000000,6.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEyFWK9Kuuy8D6u_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_FEyFWK9Kuuy8D6u_1_JLC")
App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEyFWK9Kuuy8D6u_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pocket","Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC")
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLC")
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEyFWK9Kuuy8D6u_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEyFWK9Kuuy8D6u_1_FLTYZxwNs21CPOg_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_Ffo1ZOg9TXG4WzY_1_JQG")
origin = App.Vector(-0.00000000000000,-8.00000000000000,4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ffo1ZOg9TXG4WzY_1_JQG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_Ffo1ZOg9TXG4WzY_1_JQG")
App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ffo1ZOg9TXG4WzY_1_JQG"), [""])
App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQG").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,-1.50000000000000,0.00000000000000),App.Vector(0.00000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQG").addGeometry(Part.LineSegment(App.Vector(-1.00000000000000,-1.50000000000000,0.00000000000000),App.Vector(0.00000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQG").addGeometry(Part.LineSegment(App.Vector(-1.00000000000000,-1.50000000000000,0.00000000000000),App.Vector(1.00000000000000,-1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pocket","Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG")
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").Profile = App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQG")
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").Length = 16.0
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").Type = 4
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_Ffo1ZOg9TXG4WzY_1_JQC")
origin = App.Vector(-0.00000000000000,-8.00000000000000,4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ffo1ZOg9TXG4WzY_1_JQC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_Ffo1ZOg9TXG4WzY_1_JQC")
App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ffo1ZOg9TXG4WzY_1_JQC"), [""])
App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQC").addGeometry(Part.LineSegment(App.Vector(-1.00000000000000,-1.50000000000000,0.00000000000000),App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000),App.Vector(1.00000000000000,-1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQC").addGeometry(Part.LineSegment(App.Vector(-1.00000000000000,-1.50000000000000,0.00000000000000),App.Vector(1.00000000000000,-1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pocket","Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC")
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").Profile = App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQC")
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").Length = 16.0
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ffo1ZOg9TXG4WzY_1_JQC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").Type = 4
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ffo1ZOg9TXG4WzY_1_Fe38mYOMRugnkIk_1_JQC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_FZxzQBIBONE32nG_1_JUG")
origin = App.Vector(-0.00000000000000,8.00000000000000,-8.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZxzQBIBONE32nG_1_JUG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_FZxzQBIBONE32nG_1_JUG")
App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZxzQBIBONE32nG_1_JUG"), [""])
App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG").addGeometry(Part.LineSegment(App.Vector(12.00000000000000,-8.00000000000000,0.00000000000000),App.Vector(12.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG").addGeometry(Part.LineSegment(App.Vector(12.00000000000000,4.00000000000000,0.00000000000000),App.Vector(27.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG").addGeometry(Part.LineSegment(App.Vector(27.00000000000000,-8.00000000000000,0.00000000000000),App.Vector(27.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG").addGeometry(Part.LineSegment(App.Vector(27.00000000000000,-8.00000000000000,0.00000000000000),App.Vector(12.00000000000000,-8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pocket","Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG")
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").Profile = App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG")
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").Type = 4
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Plane", "plane_Sketch_FZxzQBIBONE32nG_1_JUC")
origin = App.Vector(-0.00000000000000,8.00000000000000,-8.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZxzQBIBONE32nG_1_JUC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("Sketcher::SketchObject","Sketch_FZxzQBIBONE32nG_1_JUC")
App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZxzQBIBONE32nG_1_JUC"), [""])
App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,4.00000000000000,0.00000000000000),App.Vector(-12.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC").addGeometry(Part.LineSegment(App.Vector(-12.00000000000000,4.00000000000000,0.00000000000000),App.Vector(-12.00000000000000,-8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,-8.00000000000000,0.00000000000000),App.Vector(-12.00000000000000,-8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,-8.00000000000000,0.00000000000000),App.Vector(-27.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fb2gCkjXbUjxXNG_0").newObject("PartDesign::Pocket","Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC")
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").Profile = App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC")
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZxzQBIBONE32nG_1_JUC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").Type = 4
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZxzQBIBONE32nG_1_FCcxDwCZ736Bqx1_1_JUC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00220987")
App.ActiveDocument.addObject("PartDesign::Body","Body_FNXhDgeUaItOEaJ_0")
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").Label = "Body_FNXhDgeUaItOEaJ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Plane", "plane_Sketch_FNXhDgeUaItOEaJ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("Sketcher::SketchObject","Sketch_FNXhDgeUaItOEaJ_0_JGC")
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,2.50000000000000,0.00000000000000),App.Vector(2.16506000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2.16506000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Pad","Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGC")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Plane", "plane_Sketch_FNXhDgeUaItOEaJ_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("Sketcher::SketchObject","Sketch_FNXhDgeUaItOEaJ_0_JGG")
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,2.50000000000000,0.00000000000000),App.Vector(-2.16506000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-2.16506000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Pad","Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGG")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").Length = 50.0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Plane", "plane_Sketch_FNXhDgeUaItOEaJ_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("Sketcher::SketchObject","Sketch_FNXhDgeUaItOEaJ_0_JGK")
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000),App.Vector(2.16506000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2.16506000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Pad","Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGK")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").Length = 50.0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Plane", "plane_Sketch_FNXhDgeUaItOEaJ_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("Sketcher::SketchObject","Sketch_FNXhDgeUaItOEaJ_0_JGO")
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000),App.Vector(-2.16506000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-2.16506000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Pad","Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGO")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").Length = 50.0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Plane", "plane_Sketch_FNXhDgeUaItOEaJ_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("Sketcher::SketchObject","Sketch_FNXhDgeUaItOEaJ_0_JGS")
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGS").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2.16506000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGS").addGeometry(Part.LineSegment(App.Vector(2.16506000000000,1.25000000000000,0.00000000000000),App.Vector(2.16506000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGS").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2.16506000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Pad","Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").Profile = App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGS")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").Length = 50.0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Plane", "plane_Sketch_FNXhDgeUaItOEaJ_0_JGW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("Sketcher::SketchObject","Sketch_FNXhDgeUaItOEaJ_0_JGW")
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNXhDgeUaItOEaJ_0_JGW"), [""])
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGW").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-2.16506000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGW").addGeometry(Part.LineSegment(App.Vector(-2.16506000000000,-1.25000000000000,0.00000000000000),App.Vector(-2.16506000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGW").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-2.16506000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Pad","Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").Profile = App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGW")
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").Length = 50.0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNXhDgeUaItOEaJ_0_JGW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").Type = 4
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNXhDgeUaItOEaJ_0_F4JnbYNdqkQW0oY_0_JGW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Plane", "plane_Sketch_F8TQA5PK1k9yqRh_1_JJC")
origin = App.Vector(-0.00000000000000,-50.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8TQA5PK1k9yqRh_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("Sketcher::SketchObject","Sketch_F8TQA5PK1k9yqRh_1_JJC")
App.ActiveDocument.getObject("Sketch_F8TQA5PK1k9yqRh_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8TQA5PK1k9yqRh_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F8TQA5PK1k9yqRh_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8TQA5PK1k9yqRh_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8TQA5PK1k9yqRh_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8TQA5PK1k9yqRh_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Pad","Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC")
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F8TQA5PK1k9yqRh_1_JJC")
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").Length = 7.0
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8TQA5PK1k9yqRh_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8TQA5PK1k9yqRh_1_FxmtMfW0NBVsqHB_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Plane", "plane_Sketch_FxvuI2nVDicY02K_1_JNC")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxvuI2nVDicY02K_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("Sketcher::SketchObject","Sketch_FxvuI2nVDicY02K_1_JNC")
App.ActiveDocument.getObject("Sketch_FxvuI2nVDicY02K_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxvuI2nVDicY02K_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FxvuI2nVDicY02K_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxvuI2nVDicY02K_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxvuI2nVDicY02K_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxvuI2nVDicY02K_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FNXhDgeUaItOEaJ_0").newObject("PartDesign::Pocket","Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC")
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FxvuI2nVDicY02K_1_JNC")
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").Length = 7.0
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxvuI2nVDicY02K_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxvuI2nVDicY02K_1_FYY4WKqIiYIr3u8_1_JNC").Offset = 0
App.ActiveDocument.recompute()

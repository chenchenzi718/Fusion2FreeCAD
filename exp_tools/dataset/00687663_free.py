import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00687663")
App.ActiveDocument.addObject("PartDesign::Body","Body_FC5QljAk1vMNLUt_0")
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").Label = "Body_FC5QljAk1vMNLUt_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Plane", "plane_Sketch_FC5QljAk1vMNLUt_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FC5QljAk1vMNLUt_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("Sketcher::SketchObject","Sketch_FC5QljAk1vMNLUt_0_JGC")
App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FC5QljAk1vMNLUt_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(-52.09181000000000,16.15281000000000,0.00000000000000),App.Vector(-52.09181000000000,-13.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(-52.09181000000000,-13.84719000000000,0.00000000000000),App.Vector(-48.09181000000000,-13.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(-48.09181000000000,-13.84719000000000,0.00000000000000),App.Vector(-48.09181000000000,-11.02123000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(-48.09181000000000,-11.02123000000000,0.00000000000000),App.Vector(-44.09181000000000,-11.02123000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(-44.09181000000000,-11.02123000000000,0.00000000000000),App.Vector(-44.09181000000000,-13.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(-44.09181000000000,-13.84719000000000,0.00000000000000),App.Vector(35.90819000000000,-13.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(35.90819000000000,-13.84719000000000,0.00000000000000),App.Vector(35.90819000000000,-11.02123000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(35.90819000000000,-11.02123000000000,0.00000000000000),App.Vector(39.90819000000000,-11.02123000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(39.90819000000000,-11.02123000000000,0.00000000000000),App.Vector(39.90819000000000,-13.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(39.90819000000000,-13.84719000000000,0.00000000000000),App.Vector(43.90819000000000,-13.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(43.90819000000000,-13.84719000000000,0.00000000000000),App.Vector(43.90819000000000,16.15281000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").addGeometry(Part.LineSegment(App.Vector(-52.09181000000000,16.15281000000000,0.00000000000000),App.Vector(43.90819000000000,16.15281000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Pad","Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC")
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC")
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FC5QljAk1vMNLUt_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FC5QljAk1vMNLUt_0_FIh0McJhPub3HSO_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Plane", "plane_Sketch_F4J4QNIFQJhCJXu_1_JJC")
origin = App.Vector(-4.09181000000000,1.15281000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4J4QNIFQJhCJXu_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("Sketcher::SketchObject","Sketch_F4J4QNIFQJhCJXu_1_JJC")
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4J4QNIFQJhCJXu_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC").addGeometry(Part.LineSegment(App.Vector(-42.69074000000000,3.84719000000000,0.00000000000000),App.Vector(-28.69074000000000,3.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC").addGeometry(Part.LineSegment(App.Vector(-28.69074000000000,3.84719000000000,0.00000000000000),App.Vector(-28.69074000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC").addGeometry(Part.LineSegment(App.Vector(-42.69074000000000,-1.15281000000000,0.00000000000000),App.Vector(-28.69074000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC").addGeometry(Part.LineSegment(App.Vector(-42.69074000000000,3.84719000000000,0.00000000000000),App.Vector(-42.69074000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Pad","Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC")
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC")
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Plane", "plane_Sketch_F4J4QNIFQJhCJXu_1_JJG")
origin = App.Vector(-4.09181000000000,1.15281000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4J4QNIFQJhCJXu_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("Sketcher::SketchObject","Sketch_F4J4QNIFQJhCJXu_1_JJG")
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4J4QNIFQJhCJXu_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG").addGeometry(Part.LineSegment(App.Vector(-18.57905000000000,3.84719000000000,0.00000000000000),App.Vector(-4.57905000000000,3.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG").addGeometry(Part.LineSegment(App.Vector(-4.57905000000000,3.84719000000000,0.00000000000000),App.Vector(-4.57905000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG").addGeometry(Part.LineSegment(App.Vector(-18.57905000000000,-1.15281000000000,0.00000000000000),App.Vector(-4.57905000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG").addGeometry(Part.LineSegment(App.Vector(-18.57905000000000,3.84719000000000,0.00000000000000),App.Vector(-18.57905000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Pad","Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG")
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG")
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Plane", "plane_Sketch_F4J4QNIFQJhCJXu_1_JJK")
origin = App.Vector(-4.09181000000000,1.15281000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4J4QNIFQJhCJXu_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("Sketcher::SketchObject","Sketch_F4J4QNIFQJhCJXu_1_JJK")
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4J4QNIFQJhCJXu_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK").addGeometry(Part.LineSegment(App.Vector(9.77630000000000,3.84719000000000,0.00000000000000),App.Vector(23.77630000000000,3.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK").addGeometry(Part.LineSegment(App.Vector(23.77630000000000,3.84719000000000,0.00000000000000),App.Vector(23.77630000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK").addGeometry(Part.LineSegment(App.Vector(9.77630000000000,-1.15281000000000,0.00000000000000),App.Vector(23.77630000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK").addGeometry(Part.LineSegment(App.Vector(9.77630000000000,3.84719000000000,0.00000000000000),App.Vector(9.77630000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Pad","Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK")
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK")
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Plane", "plane_Sketch_F4J4QNIFQJhCJXu_1_JJO")
origin = App.Vector(-4.09181000000000,1.15281000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4J4QNIFQJhCJXu_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("Sketcher::SketchObject","Sketch_F4J4QNIFQJhCJXu_1_JJO")
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4J4QNIFQJhCJXu_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO").addGeometry(Part.LineSegment(App.Vector(31.28393000000000,3.84719000000000,0.00000000000000),App.Vector(45.28393000000000,3.84719000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO").addGeometry(Part.LineSegment(App.Vector(45.28393000000000,3.84719000000000,0.00000000000000),App.Vector(45.28393000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO").addGeometry(Part.LineSegment(App.Vector(31.28393000000000,-1.15281000000000,0.00000000000000),App.Vector(45.28393000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO").addGeometry(Part.LineSegment(App.Vector(31.28393000000000,3.84719000000000,0.00000000000000),App.Vector(31.28393000000000,-1.15281000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Pad","Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO")
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO")
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4J4QNIFQJhCJXu_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4J4QNIFQJhCJXu_1_FMre3J7UwsmTev8_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Plane", "plane_Sketch_FHIe1lO5cYch07H_1_JNC")
origin = App.Vector(-4.09181000000000,1.15281000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHIe1lO5cYch07H_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("Sketcher::SketchObject","Sketch_FHIe1lO5cYch07H_1_JNC")
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHIe1lO5cYch07H_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNC").addGeometry(Part.Circle(App.Vector(-44.38827000000000,12.17796000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Pocket","Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC")
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNC")
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Plane", "plane_Sketch_FHIe1lO5cYch07H_1_JNG")
origin = App.Vector(-4.09181000000000,1.15281000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHIe1lO5cYch07H_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("Sketcher::SketchObject","Sketch_FHIe1lO5cYch07H_1_JNG")
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHIe1lO5cYch07H_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNG").addGeometry(Part.Circle(App.Vector(44.80722000000000,11.84268000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Pocket","Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG")
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNG")
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Plane", "plane_Sketch_FHIe1lO5cYch07H_1_JNK")
origin = App.Vector(-4.09181000000000,1.15281000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHIe1lO5cYch07H_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("Sketcher::SketchObject","Sketch_FHIe1lO5cYch07H_1_JNK")
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHIe1lO5cYch07H_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNK").addGeometry(Part.Circle(App.Vector(23.73733000000000,-12.17404000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Pocket","Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK")
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNK")
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Plane", "plane_Sketch_FHIe1lO5cYch07H_1_JNO")
origin = App.Vector(-4.09181000000000,1.15281000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHIe1lO5cYch07H_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("Sketcher::SketchObject","Sketch_FHIe1lO5cYch07H_1_JNO")
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHIe1lO5cYch07H_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNO").addGeometry(Part.Circle(App.Vector(-26.19469000000000,-12.17404000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FC5QljAk1vMNLUt_0").newObject("PartDesign::Pocket","Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO")
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNO")
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHIe1lO5cYch07H_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHIe1lO5cYch07H_1_FjbxbtcAdSc59Vc_1_JNO").Offset = 0
App.ActiveDocument.recompute()

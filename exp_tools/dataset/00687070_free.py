import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00687070")
App.ActiveDocument.addObject("PartDesign::Body","Body_FhnbzmhJfJIq0KQ_0")
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").Label = "Body_FhnbzmhJfJIq0KQ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Plane", "plane_Sketch_FhnbzmhJfJIq0KQ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhnbzmhJfJIq0KQ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("Sketcher::SketchObject","Sketch_FhnbzmhJfJIq0KQ_0_JGC")
App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhnbzmhJfJIq0KQ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.98076000000000,-15.00000000000000,0.00000000000000),App.Vector(-25.98076000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.98076000000000,15.00000000000000,0.00000000000000),App.Vector(0.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,30.00000000000000,0.00000000000000),App.Vector(25.98076000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.98076000000000,15.00000000000000,0.00000000000000),App.Vector(25.98076000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.98076000000000,-15.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.98076000000000,-15.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Pad","Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC")
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC")
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhnbzmhJfJIq0KQ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhnbzmhJfJIq0KQ_0_F5ADVSSzj593f2v_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Plane", "plane_Sketch_FAwB1hGnFG0xcDC_1_JJC")
origin = App.Vector(-6.95909000000000,15.66667000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAwB1hGnFG0xcDC_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("Sketcher::SketchObject","Sketch_FAwB1hGnFG0xcDC_1_JJC")
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAwB1hGnFG0xcDC_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJC").addGeometry(Part.LineSegment(App.Vector(-21.33107000000000,-15.66667000000000,0.00000000000000),App.Vector(-19.02167000000000,-14.33334000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJC").addGeometry(Part.LineSegment(App.Vector(-19.02167000000000,-14.33334000000000,0.00000000000000),App.Vector(-19.02167000000000,-17.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJC").addGeometry(Part.LineSegment(App.Vector(-21.33107000000000,-15.66667000000000,0.00000000000000),App.Vector(-19.02167000000000,-17.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Pocket","Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC")
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJC")
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Plane", "plane_Sketch_FAwB1hGnFG0xcDC_1_JJG")
origin = App.Vector(-6.95909000000000,15.66667000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAwB1hGnFG0xcDC_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("Sketcher::SketchObject","Sketch_FAwB1hGnFG0xcDC_1_JJG")
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAwB1hGnFG0xcDC_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJG").addGeometry(Part.LineSegment(App.Vector(21.10417000000000,8.83333000000000,0.00000000000000),App.Vector(18.79477000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJG").addGeometry(Part.LineSegment(App.Vector(18.79477000000000,7.50000000000000,0.00000000000000),App.Vector(21.10417000000000,6.16666000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJG").addGeometry(Part.LineSegment(App.Vector(21.10417000000000,8.83333000000000,0.00000000000000),App.Vector(21.10417000000000,6.16666000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Pocket","Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG")
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJG")
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").Length = 50.0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Plane", "plane_Sketch_FAwB1hGnFG0xcDC_1_JJK")
origin = App.Vector(-6.95909000000000,15.66667000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAwB1hGnFG0xcDC_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("Sketcher::SketchObject","Sketch_FAwB1hGnFG0xcDC_1_JJK")
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAwB1hGnFG0xcDC_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJK").addGeometry(Part.LineSegment(App.Vector(21.10417000000000,-40.16667000000000,0.00000000000000),App.Vector(21.10417000000000,-37.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJK").addGeometry(Part.LineSegment(App.Vector(21.10417000000000,-37.50000000000001,0.00000000000000),App.Vector(18.79477000000000,-38.83334000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJK").addGeometry(Part.LineSegment(App.Vector(21.10417000000000,-40.16667000000000,0.00000000000000),App.Vector(18.79477000000000,-38.83334000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Pocket","Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK")
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJK")
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").Length = 50.0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Plane", "plane_Sketch_FAwB1hGnFG0xcDC_1_JJa")
origin = App.Vector(-6.95909000000000,15.66667000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAwB1hGnFG0xcDC_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("Sketcher::SketchObject","Sketch_FAwB1hGnFG0xcDC_1_JJa")
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAwB1hGnFG0xcDC_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").addGeometry(Part.LineSegment(App.Vector(-19.02167000000000,-14.33334000000000,0.00000000000000),App.Vector(18.79477000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").addGeometry(Part.LineSegment(App.Vector(18.79477000000000,7.50000000000000,0.00000000000000),App.Vector(21.10417000000000,6.16666000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").addGeometry(Part.LineSegment(App.Vector(21.10417000000000,6.16666000000000,0.00000000000000),App.Vector(21.10417000000000,-37.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").addGeometry(Part.LineSegment(App.Vector(21.10417000000000,-37.50000000000001,0.00000000000000),App.Vector(18.79477000000000,-38.83334000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").addGeometry(Part.LineSegment(App.Vector(18.79477000000000,-38.83334000000000,0.00000000000000),App.Vector(-19.02167000000000,-17.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").addGeometry(Part.LineSegment(App.Vector(-19.02167000000000,-14.33334000000000,0.00000000000000),App.Vector(-19.02167000000000,-17.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Pocket","Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa")
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa")
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").Length = 50.0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAwB1hGnFG0xcDC_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAwB1hGnFG0xcDC_1_FJ0x21PR6bTNTPm_1_JJa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Plane", "plane_Sketch_FqyP6pW9b7qc8Mv_1_JNC")
origin = App.Vector(-12.99038000000000,-22.50000000000000,12.50000000000000)
x_axis=App.Vector(0.86602540000000,-0.50000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,0.99999999344516)
z_axis=App.Vector(-0.50000000000000,-0.86602540000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqyP6pW9b7qc8Mv_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("Sketcher::SketchObject","Sketch_FqyP6pW9b7qc8Mv_1_JNC")
App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqyP6pW9b7qc8Mv_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNC").addGeometry(Part.LineSegment(App.Vector(-18.66026063060400,8.83974994205685,0.00000043469800),App.Vector(-14.99999903565200,15.17948990050087,-0.00000050000000)),False)

App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNC").addGeometry(Part.LineSegment(App.Vector(-14.99999903565200,15.17948990050087,-0.00000050000000),App.Vector(-14.99999903565200,6.72649995590887,-0.00000050000000)),False)

App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNC").addGeometry(Part.LineSegment(App.Vector(-18.66026063060400,8.83974994205685,0.00000043469800),App.Vector(-14.99999903565200,6.72649995590887,-0.00000050000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Pad","Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC")
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNC")
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Plane", "plane_Sketch_FqyP6pW9b7qc8Mv_1_JNG")
origin = App.Vector(-12.99038000000000,-22.50000000000000,12.50000000000000)
x_axis=App.Vector(0.86602540000000,-0.50000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,0.99999999344516)
z_axis=App.Vector(-0.50000000000000,-0.86602540000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqyP6pW9b7qc8Mv_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("Sketcher::SketchObject","Sketch_FqyP6pW9b7qc8Mv_1_JNG")
App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqyP6pW9b7qc8Mv_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNG").addGeometry(Part.LineSegment(App.Vector(18.66025197035000,18.83974987650845,0.00000456530200),App.Vector(14.99999903565200,20.95298986265650,0.00000050000000)),False)

App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNG").addGeometry(Part.LineSegment(App.Vector(14.99999903565200,20.95298986265650,0.00000050000000),App.Vector(14.99999903565200,12.49999991806450,0.00000050000000)),False)

App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNG").addGeometry(Part.LineSegment(App.Vector(18.66025197035000,18.83974987650845,0.00000456530200),App.Vector(14.99999903565200,12.49999991806450,0.00000050000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Pad","Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG")
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNG")
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Plane", "plane_Sketch_FqyP6pW9b7qc8Mv_1_JNS")
origin = App.Vector(-12.99038000000000,-22.50000000000000,12.50000000000000)
x_axis=App.Vector(0.86602540000000,-0.50000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,0.99999999344516)
z_axis=App.Vector(-0.50000000000000,-0.86602540000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqyP6pW9b7qc8Mv_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("Sketcher::SketchObject","Sketch_FqyP6pW9b7qc8Mv_1_JNS")
App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqyP6pW9b7qc8Mv_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").addGeometry(Part.LineSegment(App.Vector(-5.00000256530200,32.49999978696769,0.00000150000000),App.Vector(-14.99999903565200,15.17948990050087,-0.00000050000000)),False)

App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").addGeometry(Part.LineSegment(App.Vector(-14.99999903565200,15.17948990050087,-0.00000050000000),App.Vector(-14.99999903565200,6.72649995590887,-0.00000050000000)),False)

App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").addGeometry(Part.LineSegment(App.Vector(5.00000256530200,-4.82050996840233,-0.00000150000000),App.Vector(-14.99999903565200,6.72649995590887,-0.00000050000000)),False)

App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").addGeometry(Part.LineSegment(App.Vector(5.00000256530200,-4.82050996840233,-0.00000150000000),App.Vector(14.99999903565200,12.49999991806450,0.00000050000000)),False)

App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").addGeometry(Part.LineSegment(App.Vector(14.99999903565200,20.95298986265650,0.00000050000000),App.Vector(14.99999903565200,12.49999991806450,0.00000050000000)),False)

App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").addGeometry(Part.LineSegment(App.Vector(-5.00000256530200,32.49999978696769,0.00000150000000),App.Vector(14.99999903565200,20.95298986265650,0.00000050000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Pad","Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS")
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS")
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").Length = 25.0
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqyP6pW9b7qc8Mv_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqyP6pW9b7qc8Mv_1_FRCfyBLlk3xZkWq_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Plane", "plane_Sketch_FxbUfMWQQ6I76xV_1_JRC")
origin = App.Vector(-12.99038000000000,22.50000000000000,25.00000000000000)
x_axis=App.Vector(-0.86602540000000,-0.50000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,0.99999999344516)
z_axis=App.Vector(-0.50000000000000,0.86602540000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxbUfMWQQ6I76xV_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("Sketcher::SketchObject","Sketch_FxbUfMWQQ6I76xV_1_JRC")
App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxbUfMWQQ6I76xV_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC").addGeometry(Part.LineSegment(App.Vector(7.46409978814000,6.53589995715822,-0.00000009407000),App.Vector(-1.99999929407000,1.07179999297452,0.00000040000000)),False)

App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC").addGeometry(Part.LineSegment(App.Vector(-1.99999929407000,1.07179999297452,0.00000040000000),App.Vector(-7.46409978814000,10.53589993093886,0.00000009407000)),False)

App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC").addGeometry(Part.LineSegment(App.Vector(-7.46409978814000,10.53589993093886,0.00000009407000),App.Vector(1.99999929407000,15.99999989512256,-0.00000040000000)),False)

App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC").addGeometry(Part.LineSegment(App.Vector(7.46409978814000,6.53589995715822,-0.00000009407000),App.Vector(1.99999929407000,15.99999989512256,-0.00000040000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FhnbzmhJfJIq0KQ_0").newObject("PartDesign::Pad","Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC")
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC")
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxbUfMWQQ6I76xV_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxbUfMWQQ6I76xV_1_Fi7TnqyW4d9rfE9_1_JRC").Offset = 0
App.ActiveDocument.recompute()

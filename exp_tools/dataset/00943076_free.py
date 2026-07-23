import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00943076")
App.ActiveDocument.addObject("PartDesign::Body","Body_F5kEcrIK0SnEKPy_0")
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").Label = "Body_F5kEcrIK0SnEKPy_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Plane", "plane_Sketch_F5kEcrIK0SnEKPy_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5kEcrIK0SnEKPy_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("Sketcher::SketchObject","Sketch_F5kEcrIK0SnEKPy_0_JGO")
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5kEcrIK0SnEKPy_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(-197.05621000000002,127.15531999999999,0.00000000000000),App.Vector(112.94379000000001,127.15531999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(112.94379000000001,127.15531999999999,0.00000000000000),App.Vector(112.94379000000001,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(112.94379000000001,-142.84468000000001,0.00000000000000),App.Vector(42.94379000000000,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(22.94379000000000,-142.84468000000001,0.00000000000000),App.Vector(42.94379000000000,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(-42.05621000000000,-142.84468000000001,0.00000000000000),App.Vector(22.94379000000000,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(-62.05621000000000,-142.84468000000001,0.00000000000000),App.Vector(-42.05621000000000,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(-127.05621000000001,-142.84468000000001,0.00000000000000),App.Vector(-62.05621000000000,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(-147.05620999999999,-142.84468000000001,0.00000000000000),App.Vector(-127.05621000000001,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(-197.05621000000002,-142.84468000000001,0.00000000000000),App.Vector(-147.05620999999999,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").addGeometry(Part.LineSegment(App.Vector(-197.05621000000002,127.15531999999999,0.00000000000000),App.Vector(-197.05621000000002,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Pad","Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO")
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO")
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").Length = 20.0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Plane", "plane_Sketch_F5kEcrIK0SnEKPy_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5kEcrIK0SnEKPy_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("Sketcher::SketchObject","Sketch_F5kEcrIK0SnEKPy_0_JGC")
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5kEcrIK0SnEKPy_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC").addGeometry(Part.LineSegment(App.Vector(-147.05620999999999,-142.84468000000001,0.00000000000000),App.Vector(-127.05621000000001,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC").addGeometry(Part.LineSegment(App.Vector(-127.05621000000001,-142.84468000000001,0.00000000000000),App.Vector(-127.05621000000001,-162.84467999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC").addGeometry(Part.LineSegment(App.Vector(-147.05620999999999,-162.84467999999998,0.00000000000000),App.Vector(-127.05621000000001,-162.84467999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC").addGeometry(Part.LineSegment(App.Vector(-147.05620999999999,-142.84468000000001,0.00000000000000),App.Vector(-147.05620999999999,-162.84467999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Pad","Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC")
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC")
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").Length = 20.0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Plane", "plane_Sketch_F5kEcrIK0SnEKPy_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5kEcrIK0SnEKPy_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("Sketcher::SketchObject","Sketch_F5kEcrIK0SnEKPy_0_JGG")
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5kEcrIK0SnEKPy_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG").addGeometry(Part.LineSegment(App.Vector(-62.05621000000000,-142.84468000000001,0.00000000000000),App.Vector(-42.05621000000000,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG").addGeometry(Part.LineSegment(App.Vector(-42.05621000000000,-142.84468000000001,0.00000000000000),App.Vector(-42.05621000000000,-162.84467999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG").addGeometry(Part.LineSegment(App.Vector(-62.05621000000000,-162.84467999999998,0.00000000000000),App.Vector(-42.05621000000000,-162.84467999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG").addGeometry(Part.LineSegment(App.Vector(-62.05621000000000,-142.84468000000001,0.00000000000000),App.Vector(-62.05621000000000,-162.84467999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Pad","Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG")
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG")
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").Length = 20.0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Plane", "plane_Sketch_F5kEcrIK0SnEKPy_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5kEcrIK0SnEKPy_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("Sketcher::SketchObject","Sketch_F5kEcrIK0SnEKPy_0_JGK")
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5kEcrIK0SnEKPy_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK").addGeometry(Part.LineSegment(App.Vector(22.94379000000000,-142.84468000000001,0.00000000000000),App.Vector(42.94379000000000,-142.84468000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK").addGeometry(Part.LineSegment(App.Vector(42.94379000000000,-142.84468000000001,0.00000000000000),App.Vector(42.94379000000000,-162.84467999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK").addGeometry(Part.LineSegment(App.Vector(22.94379000000000,-162.84467999999998,0.00000000000000),App.Vector(42.94379000000000,-162.84467999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK").addGeometry(Part.LineSegment(App.Vector(22.94379000000000,-142.84468000000001,0.00000000000000),App.Vector(22.94379000000000,-162.84467999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Pad","Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK")
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK")
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").Length = 20.0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5kEcrIK0SnEKPy_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5kEcrIK0SnEKPy_0_Fu7WTBK2WLIdbgQ_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Plane", "plane_Sketch_F3CEHdun9VAy0NM_1_JJK")
origin = App.Vector(-137.11621000000000,-162.84467999999998,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3CEHdun9VAy0NM_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("Sketcher::SketchObject","Sketch_F3CEHdun9VAy0NM_1_JJK")
App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3CEHdun9VAy0NM_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJK").addGeometry(Part.LineSegment(App.Vector(-9.94000000000000,-10.00000000000000,0.00000000000000),App.Vector(-4.94000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJK").addGeometry(Part.LineSegment(App.Vector(-9.94000000000000,10.00000000000000,0.00000000000000),App.Vector(-4.94000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJK").addGeometry(Part.LineSegment(App.Vector(-9.94000000000000,-10.00000000000000,0.00000000000000),App.Vector(-9.94000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Pocket","Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK")
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJK")
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").Length = 20.0
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Plane", "plane_Sketch_F3CEHdun9VAy0NM_1_JJC")
origin = App.Vector(-137.11621000000000,-162.84467999999998,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3CEHdun9VAy0NM_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("Sketcher::SketchObject","Sketch_F3CEHdun9VAy0NM_1_JJC")
App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3CEHdun9VAy0NM_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJC").addGeometry(Part.LineSegment(App.Vector(75.05999999999999,10.00000000000000,0.00000000000000),App.Vector(80.05999999999999,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJC").addGeometry(Part.LineSegment(App.Vector(80.05999999999999,-10.00000000000000,0.00000000000000),App.Vector(75.05999999999999,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJC").addGeometry(Part.LineSegment(App.Vector(75.05999999999999,10.00000000000000,0.00000000000000),App.Vector(75.05999999999999,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Pocket","Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC")
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJC")
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").Length = 20.0
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Plane", "plane_Sketch_F3CEHdun9VAy0NM_1_JJG")
origin = App.Vector(-137.11621000000000,-162.84467999999998,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3CEHdun9VAy0NM_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("Sketcher::SketchObject","Sketch_F3CEHdun9VAy0NM_1_JJG")
App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3CEHdun9VAy0NM_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJG").addGeometry(Part.LineSegment(App.Vector(160.05999999999997,10.00000000000000,0.00000000000000),App.Vector(165.05999999999997,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJG").addGeometry(Part.LineSegment(App.Vector(165.05999999999997,-10.00000000000000,0.00000000000000),App.Vector(160.05999999999997,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJG").addGeometry(Part.LineSegment(App.Vector(160.05999999999997,10.00000000000000,0.00000000000000),App.Vector(160.05999999999997,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Pocket","Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG")
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJG")
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").Length = 20.0
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3CEHdun9VAy0NM_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3CEHdun9VAy0NM_1_FHYG3E2se7vbzn4_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Plane", "plane_Sketch_FieaEqOPcnYmlcv_1_JNC")
origin = App.Vector(-42.05621000000000,127.15531999999999,15.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FieaEqOPcnYmlcv_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("Sketcher::SketchObject","Sketch_FieaEqOPcnYmlcv_1_JNC")
App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FieaEqOPcnYmlcv_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC").addGeometry(Part.LineSegment(App.Vector(-155.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(155.00000000000003,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC").addGeometry(Part.LineSegment(App.Vector(155.00000000000003,-15.00000000000000,0.00000000000000),App.Vector(155.00000000000003,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC").addGeometry(Part.LineSegment(App.Vector(155.00000000000003,-15.00000000000000,0.00000000000000),App.Vector(-155.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC").addGeometry(Part.LineSegment(App.Vector(-155.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(-155.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5kEcrIK0SnEKPy_0").newObject("PartDesign::Pad","Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC")
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC")
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FieaEqOPcnYmlcv_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FieaEqOPcnYmlcv_1_FvqS3GIdg9D0M6x_1_JNC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00646675")
App.ActiveDocument.addObject("PartDesign::Body","Body_FE86eGJ8xICmrxK_0")
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").Label = "Body_FE86eGJ8xICmrxK_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Plane", "plane_Sketch_FE86eGJ8xICmrxK_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE86eGJ8xICmrxK_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("Sketcher::SketchObject","Sketch_FE86eGJ8xICmrxK_0_JGC")
App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE86eGJ8xICmrxK_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,63.50000000000000,0.00000000000000),App.Vector(-63.50000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,63.50000000000000,0.00000000000000),App.Vector(-63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,-63.50000000000000,0.00000000000000),App.Vector(-63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,63.50000000000000,0.00000000000000),App.Vector(63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Pad","Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC")
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC")
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE86eGJ8xICmrxK_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE86eGJ8xICmrxK_0_FnuXo9GCpe10PJ3_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Plane", "plane_Sketch_FKDgQOdgXpwhm0g_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKDgQOdgXpwhm0g_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("Sketcher::SketchObject","Sketch_FKDgQOdgXpwhm0g_1_JJC")
App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKDgQOdgXpwhm0g_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,48.26000000000000,0.00000000000000),App.Vector(-60.96000000000000,48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC").addGeometry(Part.LineSegment(App.Vector(-60.96000000000000,48.26000000000000,0.00000000000000),App.Vector(-60.96000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,60.96000000000000,0.00000000000000),App.Vector(-60.96000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,48.26000000000000,0.00000000000000),App.Vector(-48.26000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Pad","Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC")
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC")
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Plane", "plane_Sketch_FKDgQOdgXpwhm0g_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKDgQOdgXpwhm0g_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("Sketcher::SketchObject","Sketch_FKDgQOdgXpwhm0g_1_JJK")
App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKDgQOdgXpwhm0g_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,-60.96000000000000,0.00000000000000),App.Vector(-60.96000000000000,-60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK").addGeometry(Part.LineSegment(App.Vector(-60.96000000000000,-60.96000000000000,0.00000000000000),App.Vector(-60.96000000000000,-48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,-48.26000000000000,0.00000000000000),App.Vector(-60.96000000000000,-48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,-60.96000000000000,0.00000000000000),App.Vector(-48.26000000000000,-48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Pad","Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK")
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK")
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Plane", "plane_Sketch_FKDgQOdgXpwhm0g_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKDgQOdgXpwhm0g_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("Sketcher::SketchObject","Sketch_FKDgQOdgXpwhm0g_1_JJG")
App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKDgQOdgXpwhm0g_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,48.26000000000000,0.00000000000000),App.Vector(60.96000000000000,48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG").addGeometry(Part.LineSegment(App.Vector(60.96000000000000,48.26000000000000,0.00000000000000),App.Vector(60.96000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,60.96000000000000,0.00000000000000),App.Vector(60.96000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,48.26000000000000,0.00000000000000),App.Vector(48.26000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Pad","Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG")
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG")
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKDgQOdgXpwhm0g_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKDgQOdgXpwhm0g_1_FCIsOiHnaoSfVX5_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Plane", "plane_Sketch_FTORFYLLzs8xiiw_1_JLC")
origin = App.Vector(0.00000000000000,0.00000000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTORFYLLzs8xiiw_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("Sketcher::SketchObject","Sketch_FTORFYLLzs8xiiw_1_JLC")
App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTORFYLLzs8xiiw_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,-48.26000000000000,0.00000000000000),App.Vector(60.96000000000000,-48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC").addGeometry(Part.LineSegment(App.Vector(60.96000000000000,-48.26000000000000,0.00000000000000),App.Vector(60.96000000000000,-60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,-60.96000000000000,0.00000000000000),App.Vector(60.96000000000000,-60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,-48.26000000000000,0.00000000000000),App.Vector(48.26000000000000,-60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Pad","Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC")
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC")
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTORFYLLzs8xiiw_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTORFYLLzs8xiiw_1_FedPVUK4i3otNBS_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Plane", "plane_Sketch_FAkzrzIIoYOTJuf_1_JRO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAkzrzIIoYOTJuf_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("Sketcher::SketchObject","Sketch_FAkzrzIIoYOTJuf_1_JRO")
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAkzrzIIoYOTJuf_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO").addGeometry(Part.LineSegment(App.Vector(-60.96000000000000,-60.96000000000000,0.00000000000000),App.Vector(-48.26000000000000,-60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,-60.96000000000000,0.00000000000000),App.Vector(-48.26000000000000,-48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO").addGeometry(Part.LineSegment(App.Vector(-60.96000000000000,-48.26000000000000,0.00000000000000),App.Vector(-48.26000000000000,-48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO").addGeometry(Part.LineSegment(App.Vector(-60.96000000000000,-60.96000000000000,0.00000000000000),App.Vector(-60.96000000000000,-48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Pad","Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO")
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO")
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Plane", "plane_Sketch_FAkzrzIIoYOTJuf_1_JRK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAkzrzIIoYOTJuf_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("Sketcher::SketchObject","Sketch_FAkzrzIIoYOTJuf_1_JRK")
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAkzrzIIoYOTJuf_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,-48.26000000000000,0.00000000000000),App.Vector(60.96000000000000,-48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK").addGeometry(Part.LineSegment(App.Vector(60.96000000000000,-48.26000000000000,0.00000000000000),App.Vector(60.96000000000000,-60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,-60.96000000000000,0.00000000000000),App.Vector(60.96000000000000,-60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,-48.26000000000000,0.00000000000000),App.Vector(48.26000000000000,-60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Pad","Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK")
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK")
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Plane", "plane_Sketch_FAkzrzIIoYOTJuf_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAkzrzIIoYOTJuf_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("Sketcher::SketchObject","Sketch_FAkzrzIIoYOTJuf_1_JRG")
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAkzrzIIoYOTJuf_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,48.26000000000000,0.00000000000000),App.Vector(60.96000000000000,48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG").addGeometry(Part.LineSegment(App.Vector(60.96000000000000,48.26000000000000,0.00000000000000),App.Vector(60.96000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,60.96000000000000,0.00000000000000),App.Vector(60.96000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG").addGeometry(Part.LineSegment(App.Vector(48.26000000000000,48.26000000000000,0.00000000000000),App.Vector(48.26000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Pad","Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG")
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG")
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Plane", "plane_Sketch_FAkzrzIIoYOTJuf_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAkzrzIIoYOTJuf_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("Sketcher::SketchObject","Sketch_FAkzrzIIoYOTJuf_1_JRC")
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAkzrzIIoYOTJuf_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,48.26000000000000,0.00000000000000),App.Vector(-60.96000000000000,48.26000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC").addGeometry(Part.LineSegment(App.Vector(-60.96000000000000,48.26000000000000,0.00000000000000),App.Vector(-60.96000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,60.96000000000000,0.00000000000000),App.Vector(-60.96000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC").addGeometry(Part.LineSegment(App.Vector(-48.26000000000000,48.26000000000000,0.00000000000000),App.Vector(-48.26000000000000,60.96000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FE86eGJ8xICmrxK_0").newObject("PartDesign::Pad","Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC")
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC")
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAkzrzIIoYOTJuf_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAkzrzIIoYOTJuf_1_FloGMwurjg51i9q_1_JRC").Offset = 0
App.ActiveDocument.recompute()

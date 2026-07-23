import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00479811")
App.ActiveDocument.addObject("PartDesign::Body","Body_FFbbvhEd1iBQdPv_0")
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").Label = "Body_FFbbvhEd1iBQdPv_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Plane", "plane_Sketch_FFbbvhEd1iBQdPv_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFbbvhEd1iBQdPv_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("Sketcher::SketchObject","Sketch_FFbbvhEd1iBQdPv_0_JGC")
App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFbbvhEd1iBQdPv_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(100.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,0.00000000000000,0.00000000000000),App.Vector(100.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,50.00000000000000,0.00000000000000),App.Vector(100.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Pad","Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC")
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC")
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").Length = 4.0
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFbbvhEd1iBQdPv_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFbbvhEd1iBQdPv_0_FxA6bRXGsGBHFzM_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Plane", "plane_Sketch_Fa2sBsTeSrHWTgO_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("Sketcher::SketchObject","Sketch_Fa2sBsTeSrHWTgO_1_JJC")
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,16.66667000000000,0.00000000000000),App.Vector(4.00000000000000,16.66667000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC").addGeometry(Part.LineSegment(App.Vector(4.00000000000000,16.66667000000000,0.00000000000000),App.Vector(4.00000000000000,33.33333000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,33.33333000000000,0.00000000000000),App.Vector(4.00000000000000,33.33333000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,16.66667000000000,0.00000000000000),App.Vector(0.00000000000000,33.33333000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Pocket","Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Plane", "plane_Sketch_Fa2sBsTeSrHWTgO_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("Sketcher::SketchObject","Sketch_Fa2sBsTeSrHWTgO_1_JJG")
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(20.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(20.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,4.00000000000000,0.00000000000000),App.Vector(20.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Pocket","Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Plane", "plane_Sketch_Fa2sBsTeSrHWTgO_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("Sketcher::SketchObject","Sketch_Fa2sBsTeSrHWTgO_1_JJK")
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,0.00000000000000,0.00000000000000),App.Vector(60.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,0.00000000000000,0.00000000000000),App.Vector(60.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,4.00000000000000,0.00000000000000),App.Vector(60.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,0.00000000000000,0.00000000000000),App.Vector(40.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Pocket","Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Plane", "plane_Sketch_Fa2sBsTeSrHWTgO_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("Sketcher::SketchObject","Sketch_Fa2sBsTeSrHWTgO_1_JJO")
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO").addGeometry(Part.LineSegment(App.Vector(80.00000000000000,0.00000000000000,0.00000000000000),App.Vector(100.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,0.00000000000000,0.00000000000000),App.Vector(100.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO").addGeometry(Part.LineSegment(App.Vector(80.00000000000000,4.00000000000000,0.00000000000000),App.Vector(100.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO").addGeometry(Part.LineSegment(App.Vector(80.00000000000000,0.00000000000000,0.00000000000000),App.Vector(80.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Pocket","Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").Type = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Plane", "plane_Sketch_Fa2sBsTeSrHWTgO_1_JJS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("Sketcher::SketchObject","Sketch_Fa2sBsTeSrHWTgO_1_JJS")
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa2sBsTeSrHWTgO_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,16.66667000000000,0.00000000000000),App.Vector(96.00000000000000,16.66667000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS").addGeometry(Part.LineSegment(App.Vector(96.00000000000000,16.66667000000000,0.00000000000000),App.Vector(96.00000000000000,33.33333000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,33.33333000000000,0.00000000000000),App.Vector(96.00000000000000,33.33333000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,16.66667000000000,0.00000000000000),App.Vector(100.00000000000000,33.33333000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Pocket","Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS")
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa2sBsTeSrHWTgO_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").Type = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa2sBsTeSrHWTgO_1_FBlFujxWctCuUon_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Plane", "plane_Sketch_F6gNKxQJyTZLsfg_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6gNKxQJyTZLsfg_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("Sketcher::SketchObject","Sketch_F6gNKxQJyTZLsfg_1_JNC")
App.ActiveDocument.getObject("Sketch_F6gNKxQJyTZLsfg_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6gNKxQJyTZLsfg_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F6gNKxQJyTZLsfg_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6gNKxQJyTZLsfg_1_JNC").addGeometry(Part.Circle(App.Vector(10.00000000000000,50.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6gNKxQJyTZLsfg_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6gNKxQJyTZLsfg_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Pad","Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC")
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F6gNKxQJyTZLsfg_1_JNC")
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").Length = 4.0
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6gNKxQJyTZLsfg_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6gNKxQJyTZLsfg_1_FQ1SlHDTWIBD005_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Plane", "plane_Sketch_FlVD4gJNnMHxzuJ_1_JSC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlVD4gJNnMHxzuJ_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("Sketcher::SketchObject","Sketch_FlVD4gJNnMHxzuJ_1_JSC")
App.ActiveDocument.getObject("Sketch_FlVD4gJNnMHxzuJ_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlVD4gJNnMHxzuJ_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FlVD4gJNnMHxzuJ_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlVD4gJNnMHxzuJ_1_JSC").addGeometry(Part.Circle(App.Vector(10.74160000000000,52.53675000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlVD4gJNnMHxzuJ_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlVD4gJNnMHxzuJ_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFbbvhEd1iBQdPv_0").newObject("PartDesign::Pocket","Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC")
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FlVD4gJNnMHxzuJ_1_JSC")
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").Length = 4.0
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlVD4gJNnMHxzuJ_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").Type = 0
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlVD4gJNnMHxzuJ_1_F4TDl2eaBhCojSv_1_JSC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00188073")
App.ActiveDocument.addObject("PartDesign::Body","Body_FnF4hEpuPKPepZ0_0")
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").Label = "Body_FnF4hEpuPKPepZ0_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Plane", "plane_Sketch_FnF4hEpuPKPepZ0_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnF4hEpuPKPepZ0_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("Sketcher::SketchObject","Sketch_FnF4hEpuPKPepZ0_0_JGC")
App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnF4hEpuPKPepZ0_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(20.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(20.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,12.50000000000000,0.00000000000000),App.Vector(20.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Pad","Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC")
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC")
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").Length = 40.0
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnF4hEpuPKPepZ0_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnF4hEpuPKPepZ0_0_FElo9ROWaQSHs5S_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Plane", "plane_Sketch_Ff0LM621zvqj8q0_1_JJC")
origin = App.Vector(10.00000000000000,-20.00000000000000,12.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff0LM621zvqj8q0_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("Sketcher::SketchObject","Sketch_Ff0LM621zvqj8q0_1_JJC")
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff0LM621zvqj8q0_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-28.04231000000000,0.00000000000000),App.Vector(-2.00000000000000,-28.04231000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,-28.04231000000000,0.00000000000000),App.Vector(-2.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(-2.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,-28.04231000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Pad","Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC")
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC")
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").Length = 6.999999999999999
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Plane", "plane_Sketch_Ff0LM621zvqj8q0_1_JJG")
origin = App.Vector(10.00000000000000,-20.00000000000000,12.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff0LM621zvqj8q0_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("Sketcher::SketchObject","Sketch_Ff0LM621zvqj8q0_1_JJG")
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff0LM621zvqj8q0_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-28.04231000000000,0.00000000000000),App.Vector(2.00000000000000,-28.04231000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,-28.04231000000000,0.00000000000000),App.Vector(2.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(2.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(10.00000000000000,-28.04231000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Pad","Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG")
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG")
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").Length = 6.999999999999999
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Plane", "plane_Sketch_Ff0LM621zvqj8q0_1_JJK")
origin = App.Vector(10.00000000000000,-20.00000000000000,12.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff0LM621zvqj8q0_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("Sketcher::SketchObject","Sketch_Ff0LM621zvqj8q0_1_JJK")
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff0LM621zvqj8q0_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-13.33263000000000,0.00000000000000),App.Vector(-2.00000000000000,-13.33263000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,-13.33263000000000,0.00000000000000),App.Vector(-2.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(-2.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,-13.33263000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Pad","Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK")
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK")
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").Length = 6.999999999999999
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Plane", "plane_Sketch_Ff0LM621zvqj8q0_1_JJS")
origin = App.Vector(10.00000000000000,-20.00000000000000,12.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff0LM621zvqj8q0_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("Sketcher::SketchObject","Sketch_Ff0LM621zvqj8q0_1_JJS")
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff0LM621zvqj8q0_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-13.33263000000000,0.00000000000000),App.Vector(2.00000000000000,-13.33263000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,-13.33263000000000,0.00000000000000),App.Vector(2.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(2.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(10.00000000000000,-13.33263000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Pad","Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS")
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS")
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").Length = 6.999999999999999
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff0LM621zvqj8q0_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff0LM621zvqj8q0_1_FkFEUin3U05A1hG_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Plane", "plane_Sketch_FtyHMb7M8sozyiV_1_JNC")
origin = App.Vector(10.00000000000000,-20.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtyHMb7M8sozyiV_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("Sketcher::SketchObject","Sketch_FtyHMb7M8sozyiV_1_JNC")
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtyHMb7M8sozyiV_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,27.94056000000000,0.00000000000000),App.Vector(-2.00000000000000,27.94056000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,27.94056000000000,0.00000000000000),App.Vector(-2.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-2.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,27.94056000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Pad","Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC")
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC")
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").Length = 6.999999999999999
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Plane", "plane_Sketch_FtyHMb7M8sozyiV_1_JNK")
origin = App.Vector(10.00000000000000,-20.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtyHMb7M8sozyiV_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("Sketcher::SketchObject","Sketch_FtyHMb7M8sozyiV_1_JNK")
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtyHMb7M8sozyiV_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,13.06703000000000,0.00000000000000),App.Vector(-2.00000000000000,13.06703000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,13.06703000000000,0.00000000000000),App.Vector(-2.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-2.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,13.06703000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Pad","Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK")
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK")
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").Length = 6.999999999999999
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Plane", "plane_Sketch_FtyHMb7M8sozyiV_1_JNS")
origin = App.Vector(10.00000000000000,-20.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtyHMb7M8sozyiV_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("Sketcher::SketchObject","Sketch_FtyHMb7M8sozyiV_1_JNS")
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtyHMb7M8sozyiV_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,13.06703000000000,0.00000000000000),App.Vector(2.00000000000000,13.06703000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,13.06703000000000,0.00000000000000),App.Vector(2.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,20.00000000000000,0.00000000000000),App.Vector(2.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,20.00000000000000,0.00000000000000),App.Vector(10.00000000000000,13.06703000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Pad","Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS")
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS")
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").Length = 6.999999999999999
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Plane", "plane_Sketch_FtyHMb7M8sozyiV_1_JNG")
origin = App.Vector(10.00000000000000,-20.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtyHMb7M8sozyiV_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("Sketcher::SketchObject","Sketch_FtyHMb7M8sozyiV_1_JNG")
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtyHMb7M8sozyiV_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,27.94056000000000,0.00000000000000),App.Vector(2.00000000000000,27.94056000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,27.94056000000000,0.00000000000000),App.Vector(2.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,20.00000000000000,0.00000000000000),App.Vector(2.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,20.00000000000000,0.00000000000000),App.Vector(10.00000000000000,27.94056000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnF4hEpuPKPepZ0_0").newObject("PartDesign::Pad","Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG")
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG")
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").Length = 6.999999999999999
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtyHMb7M8sozyiV_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtyHMb7M8sozyiV_1_FkKnx769yY1a21b_1_JNG").Offset = 0
App.ActiveDocument.recompute()

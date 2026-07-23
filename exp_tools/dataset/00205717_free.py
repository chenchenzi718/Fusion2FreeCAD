import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00205717")
App.ActiveDocument.addObject("PartDesign::Body","Body_FkwqkkIUtJAV5Sl_0")
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").Label = "Body_FkwqkkIUtJAV5Sl_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Plane", "plane_Sketch_FkwqkkIUtJAV5Sl_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkwqkkIUtJAV5Sl_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("Sketcher::SketchObject","Sketch_FkwqkkIUtJAV5Sl_0_JGC")
App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkwqkkIUtJAV5Sl_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(41.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC").addGeometry(Part.LineSegment(App.Vector(41.00000000000000,0.00000000000000,0.00000000000000),App.Vector(41.00000000000000,41.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,41.00000000000000,0.00000000000000),App.Vector(41.00000000000000,41.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,41.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Pad","Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC")
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC")
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").Length = 47.0
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkwqkkIUtJAV5Sl_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkwqkkIUtJAV5Sl_0_FifxwIdvmZU7cfa_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Plane", "plane_Sketch_FhtXT0hUtyg92HD_1_JJC")
origin = App.Vector(20.50000000000000,20.50000000000000,47.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhtXT0hUtyg92HD_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("Sketcher::SketchObject","Sketch_FhtXT0hUtyg92HD_1_JJC")
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhtXT0hUtyg92HD_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJC").addGeometry(Part.Circle(App.Vector(-15.50000000000000,-15.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Pocket","Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC")
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJC")
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Plane", "plane_Sketch_FhtXT0hUtyg92HD_1_JJG")
origin = App.Vector(20.50000000000000,20.50000000000000,47.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhtXT0hUtyg92HD_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("Sketcher::SketchObject","Sketch_FhtXT0hUtyg92HD_1_JJG")
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhtXT0hUtyg92HD_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJG").addGeometry(Part.Circle(App.Vector(15.50000000000000,-15.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Pocket","Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG")
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJG")
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Plane", "plane_Sketch_FhtXT0hUtyg92HD_1_JJK")
origin = App.Vector(20.50000000000000,20.50000000000000,47.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhtXT0hUtyg92HD_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("Sketcher::SketchObject","Sketch_FhtXT0hUtyg92HD_1_JJK")
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhtXT0hUtyg92HD_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJK").addGeometry(Part.Circle(App.Vector(15.50000000000000,15.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Pocket","Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK")
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJK")
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Plane", "plane_Sketch_FhtXT0hUtyg92HD_1_JJO")
origin = App.Vector(20.50000000000000,20.50000000000000,47.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhtXT0hUtyg92HD_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("Sketcher::SketchObject","Sketch_FhtXT0hUtyg92HD_1_JJO")
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhtXT0hUtyg92HD_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJO").addGeometry(Part.Circle(App.Vector(-15.50000000000000,15.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Pocket","Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO")
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJO")
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhtXT0hUtyg92HD_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhtXT0hUtyg92HD_1_FFa0RsYYkvlO9Lm_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Plane", "plane_Sketch_Fvzx5ymdNtwulOQ_1_JNC")
origin = App.Vector(20.50000000000000,20.50000000000000,47.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fvzx5ymdNtwulOQ_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("Sketcher::SketchObject","Sketch_Fvzx5ymdNtwulOQ_1_JNC")
App.ActiveDocument.getObject("Sketch_Fvzx5ymdNtwulOQ_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fvzx5ymdNtwulOQ_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fvzx5ymdNtwulOQ_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fvzx5ymdNtwulOQ_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fvzx5ymdNtwulOQ_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fvzx5ymdNtwulOQ_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Pad","Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC")
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fvzx5ymdNtwulOQ_1_JNC")
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fvzx5ymdNtwulOQ_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fvzx5ymdNtwulOQ_1_FDYm0k6B929Ezuf_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Plane", "plane_Sketch_FeQWlllGtRAKfr0_1_JRC")
origin = App.Vector(20.50000000000000,20.50000000000000,49.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeQWlllGtRAKfr0_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("Sketcher::SketchObject","Sketch_FeQWlllGtRAKfr0_1_JRC")
App.ActiveDocument.getObject("Sketch_FeQWlllGtRAKfr0_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeQWlllGtRAKfr0_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FeQWlllGtRAKfr0_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeQWlllGtRAKfr0_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeQWlllGtRAKfr0_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeQWlllGtRAKfr0_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Pad","Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC")
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FeQWlllGtRAKfr0_1_JRC")
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").Length = 21.0
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeQWlllGtRAKfr0_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeQWlllGtRAKfr0_1_FA7ETEmaSD9bCDP_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Plane", "plane_Sketch_FRrYMhSk9fYY2GM_1_JVC")
origin = App.Vector(20.50000000000000,20.50000000000000,70.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRrYMhSk9fYY2GM_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("Sketcher::SketchObject","Sketch_FRrYMhSk9fYY2GM_1_JVC")
App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRrYMhSk9fYY2GM_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Pad","Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC")
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVC")
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").Length = 7.0
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").Type = 0
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Plane", "plane_Sketch_FRrYMhSk9fYY2GM_1_JVG")
origin = App.Vector(20.50000000000000,20.50000000000000,70.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRrYMhSk9fYY2GM_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("Sketcher::SketchObject","Sketch_FRrYMhSk9fYY2GM_1_JVG")
App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRrYMhSk9fYY2GM_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVG").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkwqkkIUtJAV5Sl_0").newObject("PartDesign::Pad","Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG")
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVG")
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").Length = 7.0
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRrYMhSk9fYY2GM_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").Type = 0
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRrYMhSk9fYY2GM_1_F1QJv0zmB8hWPSI_1_JVG").Offset = 0
App.ActiveDocument.recompute()

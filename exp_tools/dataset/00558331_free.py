import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00558331")
App.ActiveDocument.addObject("PartDesign::Body","Body_FF6S7zln7cdnNru_0")
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").Label = "Body_FF6S7zln7cdnNru_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Plane", "plane_Sketch_FF6S7zln7cdnNru_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FF6S7zln7cdnNru_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("Sketcher::SketchObject","Sketch_FF6S7zln7cdnNru_0_JGG")
App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FF6S7zln7cdnNru_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGG").addGeometry(Part.LineSegment(App.Vector(66.24393999999999,22.03960000000000,0.00000000000000),App.Vector(-73.45606000000001,22.03960000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGG").addGeometry(Part.LineSegment(App.Vector(-73.45606000000001,22.03960000000000,0.00000000000000),App.Vector(-3.60606000000000,72.83960000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGG").addGeometry(Part.LineSegment(App.Vector(66.24393999999999,22.03960000000000,0.00000000000000),App.Vector(-3.60606000000000,72.83960000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Pad","Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG")
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGG")
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").Length = 381.00000000000006
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Plane", "plane_Sketch_FF6S7zln7cdnNru_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FF6S7zln7cdnNru_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("Sketcher::SketchObject","Sketch_FF6S7zln7cdnNru_0_JGC")
App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FF6S7zln7cdnNru_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC").addGeometry(Part.LineSegment(App.Vector(66.24393999999999,22.03960000000000,0.00000000000000),App.Vector(-73.45606000000001,22.03960000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC").addGeometry(Part.LineSegment(App.Vector(-73.45606000000001,22.03960000000000,0.00000000000000),App.Vector(-73.45606000000001,-54.16040000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC").addGeometry(Part.LineSegment(App.Vector(66.24393999999999,-54.16040000000000,0.00000000000000),App.Vector(-73.45606000000001,-54.16040000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC").addGeometry(Part.LineSegment(App.Vector(66.24393999999999,22.03960000000000,0.00000000000000),App.Vector(66.24393999999999,-54.16040000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Pad","Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC")
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC")
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").Length = 381.00000000000006
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FF6S7zln7cdnNru_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FF6S7zln7cdnNru_0_FMBdN0qL1MJKBpI_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Plane", "plane_Sketch_FnynCByO8Qatwb4_1_JJG")
origin = App.Vector(0.00000000000000,-16.30606000000000,9.33960000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnynCByO8Qatwb4_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("Sketcher::SketchObject","Sketch_FnynCByO8Qatwb4_1_JJG")
App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnynCByO8Qatwb4_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJG").addGeometry(Part.LineSegment(App.Vector(32.09160000000000,12.70000000000000,0.00000000000000),App.Vector(-12.21796000000000,55.48602000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJG").addGeometry(Part.LineSegment(App.Vector(-56.80839999999999,12.70000000000000,0.00000000000000),App.Vector(-12.21796000000000,55.48602000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJG").addGeometry(Part.LineSegment(App.Vector(-56.80839999999999,12.70000000000000,0.00000000000000),App.Vector(32.09160000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Pad","Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG")
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJG")
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Plane", "plane_Sketch_FnynCByO8Qatwb4_1_JJC")
origin = App.Vector(0.00000000000000,-16.30606000000000,9.33960000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnynCByO8Qatwb4_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("Sketcher::SketchObject","Sketch_FnynCByO8Qatwb4_1_JJC")
App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnynCByO8Qatwb4_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC").addGeometry(Part.LineSegment(App.Vector(-56.80839999999999,-63.50000000000000,0.00000000000000),App.Vector(32.09160000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC").addGeometry(Part.LineSegment(App.Vector(32.09160000000000,-63.50000000000000,0.00000000000000),App.Vector(32.09160000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC").addGeometry(Part.LineSegment(App.Vector(-56.80839999999999,12.70000000000000,0.00000000000000),App.Vector(32.09160000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC").addGeometry(Part.LineSegment(App.Vector(-56.80839999999999,-63.50000000000000,0.00000000000000),App.Vector(-56.80839999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Pad","Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC")
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC")
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnynCByO8Qatwb4_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnynCByO8Qatwb4_1_FcrBkkXvROP491y_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Plane", "plane_Sketch_F8IM05ClnYQBKml_1_JNG")
origin = App.Vector(58.18506000000000,-73.45606000000001,-35.11040000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8IM05ClnYQBKml_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("Sketcher::SketchObject","Sketch_F8IM05ClnYQBKml_1_JNG")
App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8IM05ClnYQBKml_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG").addGeometry(Part.LineSegment(App.Vector(204.33442000000002,-19.05000000000000,0.00000000000000),App.Vector(58.18507000000000,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG").addGeometry(Part.LineSegment(App.Vector(58.18507000000000,-19.05000000000000,0.00000000000000),App.Vector(58.18507000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG").addGeometry(Part.LineSegment(App.Vector(204.33442000000002,57.15000000000000,0.00000000000000),App.Vector(58.18507000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG").addGeometry(Part.LineSegment(App.Vector(204.33442000000002,-19.05000000000000,0.00000000000000),App.Vector(204.33442000000002,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Pad","Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG")
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG")
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Plane", "plane_Sketch_F8IM05ClnYQBKml_1_JNC")
origin = App.Vector(58.18506000000000,-73.45606000000001,-35.11040000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8IM05ClnYQBKml_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("Sketcher::SketchObject","Sketch_F8IM05ClnYQBKml_1_JNC")
App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8IM05ClnYQBKml_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNC").addGeometry(Part.LineSegment(App.Vector(204.33442000000002,57.15000000000000,0.00000000000000),App.Vector(58.18507000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNC").addGeometry(Part.LineSegment(App.Vector(58.18507000000000,57.15000000000000,0.00000000000000),App.Vector(132.31493999999998,107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNC").addGeometry(Part.LineSegment(App.Vector(204.33442000000002,57.15000000000000,0.00000000000000),App.Vector(132.31493999999998,107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Pad","Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC")
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNC")
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8IM05ClnYQBKml_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8IM05ClnYQBKml_1_FlS6BfiKQVceWAx_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Plane", "plane_Sketch_FghlZcXBAkP9Rr1_1_JRK")
origin = App.Vector(111.81336999999999,66.24393999999999,-35.11040000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FghlZcXBAkP9Rr1_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("Sketcher::SketchObject","Sketch_FghlZcXBAkP9Rr1_1_JRK")
App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FghlZcXBAkP9Rr1_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK").addGeometry(Part.LineSegment(App.Vector(-261.33304000000004,57.15000000000000,0.00000000000000),App.Vector(-111.81338000000002,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK").addGeometry(Part.LineSegment(App.Vector(-111.81338000000002,57.15000000000000,0.00000000000000),App.Vector(-111.81338000000002,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK").addGeometry(Part.LineSegment(App.Vector(-269.18662999999998,-19.05000000000000,0.00000000000000),App.Vector(-111.81338000000002,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK").addGeometry(Part.LineSegment(App.Vector(-269.18662999999998,57.15000000000000,0.00000000000000),App.Vector(-269.18662999999998,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK").addGeometry(Part.LineSegment(App.Vector(-269.18662999999998,57.15000000000000,0.00000000000000),App.Vector(-261.33304000000004,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Pad","Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK")
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK")
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").Length = 76.2
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Plane", "plane_Sketch_FghlZcXBAkP9Rr1_1_JRC")
origin = App.Vector(111.81336999999999,66.24393999999999,-35.11040000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FghlZcXBAkP9Rr1_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("Sketcher::SketchObject","Sketch_FghlZcXBAkP9Rr1_1_JRC")
App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FghlZcXBAkP9Rr1_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC").addGeometry(Part.LineSegment(App.Vector(-261.33304000000004,57.15000000000000,0.00000000000000),App.Vector(-111.81338000000002,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC").addGeometry(Part.LineSegment(App.Vector(-111.81338000000002,57.15000000000000,0.00000000000000),App.Vector(-190.50000000000003,107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC").addGeometry(Part.LineSegment(App.Vector(-269.18662999999998,57.15000000000000,0.00000000000000),App.Vector(-190.50000000000003,107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC").addGeometry(Part.LineSegment(App.Vector(-269.18662999999998,57.15000000000000,0.00000000000000),App.Vector(-261.33304000000004,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Pad","Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC")
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC")
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FghlZcXBAkP9Rr1_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FghlZcXBAkP9Rr1_1_FFaBu9bhF579mso_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Plane", "plane_Sketch_FGaS8NygqwKwggu_1_JVC")
origin = App.Vector(58.18506000000000,-73.45606000000001,-35.11040000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGaS8NygqwKwggu_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("Sketcher::SketchObject","Sketch_FGaS8NygqwKwggu_1_JVC")
App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGaS8NygqwKwggu_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC").addGeometry(Part.LineSegment(App.Vector(-58.18506000000000,19.05000000000000,0.00000000000000),App.Vector(58.18507000000000,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC").addGeometry(Part.LineSegment(App.Vector(58.18507000000000,19.05000000000000,0.00000000000000),App.Vector(58.18507000000000,23.28567000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC").addGeometry(Part.LineSegment(App.Vector(-58.18506000000000,23.28567000000000,0.00000000000000),App.Vector(58.18507000000000,23.28567000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC").addGeometry(Part.LineSegment(App.Vector(-58.18506000000000,19.05000000000000,0.00000000000000),App.Vector(-58.18506000000000,23.28567000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FF6S7zln7cdnNru_0").newObject("PartDesign::Pad","Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC")
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC")
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGaS8NygqwKwggu_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGaS8NygqwKwggu_1_FRmSAMqNcsoxouX_1_JVC").Offset = 0
App.ActiveDocument.recompute()

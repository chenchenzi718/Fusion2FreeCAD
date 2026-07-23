import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00491599")
App.ActiveDocument.addObject("PartDesign::Body","Body_F0q283dmXG4gzju_0")
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").Label = "Body_F0q283dmXG4gzju_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_F0q283dmXG4gzju_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0q283dmXG4gzju_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_F0q283dmXG4gzju_0_JGC")
App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0q283dmXG4gzju_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1.58750000000000,-5.43575000000000,0.00000000000000),App.Vector(1.58750000000000,-5.43575000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC").addGeometry(Part.LineSegment(App.Vector(1.58750000000000,-5.43575000000000,0.00000000000000),App.Vector(1.58750000000000,137.82025000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1.58750000000000,137.82025000000002,0.00000000000000),App.Vector(1.58750000000000,137.82025000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1.58750000000000,-5.43575000000000,0.00000000000000),App.Vector(-1.58750000000000,137.82025000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pad","Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC")
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC")
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").Length = 38.1
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_F0q283dmXG4gzju_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0q283dmXG4gzju_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_F0q283dmXG4gzju_0_JGK")
App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0q283dmXG4gzju_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK").addGeometry(Part.LineSegment(App.Vector(-1.58750000000000,-5.43575000000000,0.00000000000000),App.Vector(1.58750000000000,-5.43575000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-6.66750000000000,-5.43575000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.25500000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK").addGeometry(Part.LineSegment(App.Vector(-6.66750000000000,-10.51575000000000,0.00000000000000),App.Vector(-6.66750000000000,-13.69075000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-6.66750000000000,-5.43575000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.08000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pad","Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK")
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK")
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").Length = 38.1
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_F0q283dmXG4gzju_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0q283dmXG4gzju_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_F0q283dmXG4gzju_0_JGG")
App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0q283dmXG4gzju_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG").addGeometry(Part.LineSegment(App.Vector(-57.46750000000000,-10.51575000000000,0.00000000000000),App.Vector(-6.66750000000000,-10.51575000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG").addGeometry(Part.LineSegment(App.Vector(-6.66750000000000,-10.51575000000000,0.00000000000000),App.Vector(-6.66750000000000,-13.69075000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG").addGeometry(Part.LineSegment(App.Vector(-57.46750000000000,-13.69075000000000,0.00000000000000),App.Vector(-6.66750000000000,-13.69075000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG").addGeometry(Part.LineSegment(App.Vector(-57.46750000000000,-10.51575000000000,0.00000000000000),App.Vector(-57.46750000000000,-13.69075000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pad","Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG")
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG")
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").Length = 38.1
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0q283dmXG4gzju_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0q283dmXG4gzju_0_FGXNqZYUcDYnpET_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_FxI6fVhRiFVRgIJ_1_JJC")
origin = App.Vector(-1.58750000000000,66.19224999999999,19.05000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_FxI6fVhRiFVRgIJ_1_JJC")
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJC").addGeometry(Part.Circle(App.Vector(-66.54800000000002,13.97000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pocket","Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJC")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_FxI6fVhRiFVRgIJ_1_JJG")
origin = App.Vector(-1.58750000000000,66.19224999999999,19.05000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_FxI6fVhRiFVRgIJ_1_JJG")
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJG").addGeometry(Part.Circle(App.Vector(-66.54800000000002,-13.97000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pocket","Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJG")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_FxI6fVhRiFVRgIJ_1_JJK")
origin = App.Vector(-1.58750000000000,66.19224999999999,19.05000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_FxI6fVhRiFVRgIJ_1_JJK")
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJK").addGeometry(Part.Circle(App.Vector(-38.70403000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pocket","Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJK")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_FxI6fVhRiFVRgIJ_1_JJO")
origin = App.Vector(-1.58750000000000,66.19224999999999,19.05000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_FxI6fVhRiFVRgIJ_1_JJO")
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJO").addGeometry(Part.Circle(App.Vector(64.00800000000000,13.97000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pocket","Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJO")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_FxI6fVhRiFVRgIJ_1_JJS")
origin = App.Vector(-1.58750000000000,66.19224999999999,19.05000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_FxI6fVhRiFVRgIJ_1_JJS")
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxI6fVhRiFVRgIJ_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJS").addGeometry(Part.Circle(App.Vector(64.00800000000000,-13.97000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pocket","Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJS")
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxI6fVhRiFVRgIJ_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxI6fVhRiFVRgIJ_1_FJoltKwrlO1dRip_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_F0lp4um3dvGC5lI_1_JNC")
origin = App.Vector(-32.06750000000000,-13.69075000000000,19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lp4um3dvGC5lI_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_F0lp4um3dvGC5lI_1_JNC")
App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lp4um3dvGC5lI_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNC").addGeometry(Part.Circle(App.Vector(-19.68500000000000,13.33500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pocket","Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC")
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNC")
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Plane", "plane_Sketch_F0lp4um3dvGC5lI_1_JNG")
origin = App.Vector(-32.06750000000000,-13.69075000000000,19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lp4um3dvGC5lI_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("Sketcher::SketchObject","Sketch_F0lp4um3dvGC5lI_1_JNG")
App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lp4um3dvGC5lI_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNG").addGeometry(Part.Circle(App.Vector(-19.68500000000000,-13.33500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0q283dmXG4gzju_0").newObject("PartDesign::Pocket","Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG")
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNG")
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lp4um3dvGC5lI_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lp4um3dvGC5lI_1_FI2RkfKY6pzgCAt_1_JNG").Offset = 0
App.ActiveDocument.recompute()

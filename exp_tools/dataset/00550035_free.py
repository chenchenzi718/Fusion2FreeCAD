import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00550035")
App.ActiveDocument.addObject("PartDesign::Body","Body_FsQNP52u8OfjNBf_0")
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").Label = "Body_FsQNP52u8OfjNBf_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Plane", "plane_Sketch_FsQNP52u8OfjNBf_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsQNP52u8OfjNBf_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("Sketcher::SketchObject","Sketch_FsQNP52u8OfjNBf_0_JGC")
App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsQNP52u8OfjNBf_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC").addGeometry(Part.LineSegment(App.Vector(42.81553000000000,-61.01008000000000,0.00000000000000),App.Vector(30.81553000000000,-61.01008000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC").addGeometry(Part.LineSegment(App.Vector(30.81553000000000,2.98992000000000,0.00000000000000),App.Vector(30.81553000000000,-61.01008000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC").addGeometry(Part.LineSegment(App.Vector(30.81553000000000,2.98992000000000,0.00000000000000),App.Vector(42.81553000000000,2.98992000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC").addGeometry(Part.LineSegment(App.Vector(42.81553000000000,-61.01008000000000,0.00000000000000),App.Vector(42.81553000000000,2.98992000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Pad","Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC")
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC")
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").Length = 24.0
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FVY3o6NNS4p10xo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Plane", "plane_Sketch_FsQNP52u8OfjNBf_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsQNP52u8OfjNBf_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("Sketcher::SketchObject","Sketch_FsQNP52u8OfjNBf_0_JGO")
App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsQNP52u8OfjNBf_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO").addGeometry(Part.LineSegment(App.Vector(30.81553000000000,2.98992000000000,0.00000000000000),App.Vector(0.00000000000000,2.98992000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,2.98992000000000,0.00000000000000),App.Vector(-0.38549000000000,-17.83919000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO").addGeometry(Part.LineSegment(App.Vector(-1.18447000000000,-61.01008000000000,0.00000000000000),App.Vector(-0.38549000000000,-17.83919000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO").addGeometry(Part.LineSegment(App.Vector(30.81553000000000,-61.01008000000000,0.00000000000000),App.Vector(-1.18447000000000,-61.01008000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO").addGeometry(Part.LineSegment(App.Vector(30.81553000000000,2.98992000000000,0.00000000000000),App.Vector(30.81553000000000,-61.01008000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Pad","Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO")
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").Profile = App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO")
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").Length = 56.0
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Plane", "plane_Sketch_FsQNP52u8OfjNBf_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsQNP52u8OfjNBf_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("Sketcher::SketchObject","Sketch_FsQNP52u8OfjNBf_0_JGG")
App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsQNP52u8OfjNBf_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG").addGeometry(Part.LineSegment(App.Vector(-45.18447000000000,2.98992000000000,0.00000000000000),App.Vector(0.00000000000000,2.98992000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,2.98992000000000,0.00000000000000),App.Vector(-0.38549000000000,-17.83919000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG").addGeometry(Part.LineSegment(App.Vector(-45.18447000000000,-17.01008000000000,0.00000000000000),App.Vector(-0.38549000000000,-17.83919000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG").addGeometry(Part.LineSegment(App.Vector(-45.18447000000000,2.98992000000000,0.00000000000000),App.Vector(-45.18447000000000,-17.01008000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Pad","Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG")
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").Profile = App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG")
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").Length = 56.0
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsQNP52u8OfjNBf_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsQNP52u8OfjNBf_0_FWka5srm6OnzpPh_1_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Plane", "plane_Sketch_F6vTzTfNGPOvUj6_1_JLG")
origin = App.Vector(-7.18447000000000,-29.01008000000000,56.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6vTzTfNGPOvUj6_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("Sketcher::SketchObject","Sketch_F6vTzTfNGPOvUj6_1_JLG")
App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6vTzTfNGPOvUj6_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(38.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),20.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLG").addGeometry(Part.LineSegment(App.Vector(38.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(38.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Pocket","Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG")
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLG")
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").Length = 32.0
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Plane", "plane_Sketch_F6vTzTfNGPOvUj6_1_JLK")
origin = App.Vector(-7.18447000000000,-29.01008000000000,56.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6vTzTfNGPOvUj6_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("Sketcher::SketchObject","Sketch_F6vTzTfNGPOvUj6_1_JLK")
App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6vTzTfNGPOvUj6_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(38.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),20.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLK").addGeometry(Part.LineSegment(App.Vector(38.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(38.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Pocket","Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK")
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLK")
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").Length = 32.0
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6vTzTfNGPOvUj6_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6vTzTfNGPOvUj6_1_F74oS7qb2yr6wqD_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Plane", "plane_Sketch_Fmfnib06RpCPDOi_1_JPC")
origin = App.Vector(-22.65058000000000,-38.87808000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fmfnib06RpCPDOi_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("Sketcher::SketchObject","Sketch_Fmfnib06RpCPDOi_1_JPC")
App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fmfnib06RpCPDOi_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPC").addGeometry(Part.LineSegment(App.Vector(21.46611000000000,-22.13200000000000,0.00000000000000),App.Vector(22.26509000000000,21.03889000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPC").addGeometry(Part.LineSegment(App.Vector(22.26509000000000,21.03889000000000,0.00000000000000),App.Vector(21.46611000000000,21.05368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPC").addGeometry(Part.LineSegment(App.Vector(21.46611000000000,-22.13200000000000,0.00000000000000),App.Vector(21.46611000000000,21.05368000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Pad","Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC")
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPC")
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").Length = 56.0
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Plane", "plane_Sketch_Fmfnib06RpCPDOi_1_JPG")
origin = App.Vector(-22.65058000000000,-38.87808000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fmfnib06RpCPDOi_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("Sketcher::SketchObject","Sketch_Fmfnib06RpCPDOi_1_JPG")
App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fmfnib06RpCPDOi_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPG").addGeometry(Part.LineSegment(App.Vector(-22.53389000000000,21.86800000000000,0.00000000000000),App.Vector(21.46611000000000,21.05368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPG").addGeometry(Part.LineSegment(App.Vector(21.46611000000000,21.86800000000000,0.00000000000000),App.Vector(21.46611000000000,21.05368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPG").addGeometry(Part.LineSegment(App.Vector(-22.53389000000000,21.86800000000000,0.00000000000000),App.Vector(21.46611000000000,21.86800000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Pad","Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG")
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPG")
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").Length = 56.0
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Plane", "plane_Sketch_Fmfnib06RpCPDOi_1_JPK")
origin = App.Vector(-22.65058000000000,-38.87808000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fmfnib06RpCPDOi_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("Sketcher::SketchObject","Sketch_Fmfnib06RpCPDOi_1_JPK")
App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fmfnib06RpCPDOi_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK").addGeometry(Part.LineSegment(App.Vector(-22.53389000000000,21.86800000000000,0.00000000000000),App.Vector(21.46611000000000,21.05368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK").addGeometry(Part.LineSegment(App.Vector(21.46611000000000,-22.13200000000000,0.00000000000000),App.Vector(21.46611000000000,21.05368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK").addGeometry(Part.LineSegment(App.Vector(-22.53389000000000,-22.13200000000000,0.00000000000000),App.Vector(21.46611000000000,-22.13200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK").addGeometry(Part.LineSegment(App.Vector(-22.53389000000000,-22.13200000000000,0.00000000000000),App.Vector(-22.53389000000000,21.86800000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsQNP52u8OfjNBf_0").newObject("PartDesign::Pad","Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK")
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK")
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").Length = 56.0
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fmfnib06RpCPDOi_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fmfnib06RpCPDOi_1_FnfdnRpnOYg2qjj_1_JPK").Offset = 0
App.ActiveDocument.recompute()

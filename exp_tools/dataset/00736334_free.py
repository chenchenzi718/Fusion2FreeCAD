import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00736334")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fj9PU6WfzpeDZqL_0")
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").Label = "Body_Fj9PU6WfzpeDZqL_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_Fj9PU6WfzpeDZqL_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj9PU6WfzpeDZqL_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_Fj9PU6WfzpeDZqL_0_JGC")
App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj9PU6WfzpeDZqL_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,30.00000000000000,0.00000000000000),App.Vector(25.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(25.00000000000000,25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,25.00000000000000,0.00000000000000),App.Vector(30.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(25.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,-30.00000000000000,0.00000000000000),App.Vector(25.00000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-25.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-25.00000000000000,25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.LineSegment(App.Vector(-27.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-27.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-25.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,-27.00000000000000,0.00000000000000),App.Vector(25.00000000000000,-27.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(25.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.LineSegment(App.Vector(27.00000000000000,25.00000000000000,0.00000000000000),App.Vector(27.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(25.00000000000000,25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,27.00000000000000,0.00000000000000),App.Vector(25.00000000000000,27.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-25.00000000000000,25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pad","Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC")
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC")
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").Length = 5450.0
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj9PU6WfzpeDZqL_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj9PU6WfzpeDZqL_0_FI06STbMmNQF3OE_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_FGtWK50qdeOqQv6_1_JKC")
origin = App.Vector(0.00000000000000,-2725.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_FGtWK50qdeOqQv6_1_JKC")
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKC"), [""])
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-2699.99999999999955,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pocket","Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").Profile = App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKC")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").Type = 4
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_FGtWK50qdeOqQv6_1_JKG")
origin = App.Vector(0.00000000000000,-2725.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_FGtWK50qdeOqQv6_1_JKG")
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKG"), [""])
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKG").addGeometry(Part.Circle(App.Vector(0.00000000000000,-2025.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pocket","Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").Profile = App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKG")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").Type = 4
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_FGtWK50qdeOqQv6_1_JKK")
origin = App.Vector(0.00000000000000,-2725.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_FGtWK50qdeOqQv6_1_JKK")
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKK"), [""])
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKK").addGeometry(Part.Circle(App.Vector(0.00000000000000,-1350.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pocket","Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").Profile = App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKK")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").Type = 4
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_FGtWK50qdeOqQv6_1_JKO")
origin = App.Vector(0.00000000000000,-2725.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_FGtWK50qdeOqQv6_1_JKO")
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKO"), [""])
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKO").addGeometry(Part.Circle(App.Vector(0.00000000000000,-674.99999999999977,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pocket","Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").Profile = App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKO")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").Type = 4
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_FGtWK50qdeOqQv6_1_JKS")
origin = App.Vector(0.00000000000000,-2725.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_FGtWK50qdeOqQv6_1_JKS")
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKS"), [""])
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKS").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pocket","Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").Profile = App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKS")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").Type = 4
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_FGtWK50qdeOqQv6_1_JKW")
origin = App.Vector(0.00000000000000,-2725.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_FGtWK50qdeOqQv6_1_JKW")
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKW"), [""])
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKW").addGeometry(Part.Circle(App.Vector(0.00000000000000,675.00000000000023,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pocket","Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").Profile = App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKW")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").Type = 4
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_FGtWK50qdeOqQv6_1_JKa")
origin = App.Vector(0.00000000000000,-2725.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_FGtWK50qdeOqQv6_1_JKa")
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKa"), [""])
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKa").addGeometry(Part.Circle(App.Vector(0.00000000000000,1350.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pocket","Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").Profile = App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKa")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").Type = 4
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_FGtWK50qdeOqQv6_1_JKe")
origin = App.Vector(0.00000000000000,-2725.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_FGtWK50qdeOqQv6_1_JKe")
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKe"), [""])
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKe").addGeometry(Part.Circle(App.Vector(0.00000000000000,2025.00000000000045,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pocket","Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").Profile = App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKe")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").Type = 4
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Plane", "plane_Sketch_FGtWK50qdeOqQv6_1_JKi")
origin = App.Vector(0.00000000000000,-2725.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("Sketcher::SketchObject","Sketch_FGtWK50qdeOqQv6_1_JKi")
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGtWK50qdeOqQv6_1_JKi"), [""])
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKi").addGeometry(Part.Circle(App.Vector(0.00000000000000,2700.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj9PU6WfzpeDZqL_0").newObject("PartDesign::Pocket","Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").Profile = App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKi")
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGtWK50qdeOqQv6_1_JKi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").Type = 4
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGtWK50qdeOqQv6_1_F7FP0NUvSOMADYO_1_JKi").Offset = 0
App.ActiveDocument.recompute()

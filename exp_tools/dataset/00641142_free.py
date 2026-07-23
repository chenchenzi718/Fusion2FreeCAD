import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00641142")
App.ActiveDocument.addObject("PartDesign::Body","Body_FDufYfCR9ucqwk9_0")
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").Label = "Body_FDufYfCR9ucqwk9_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Plane", "plane_Sketch_FDufYfCR9ucqwk9_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDufYfCR9ucqwk9_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("Sketcher::SketchObject","Sketch_FDufYfCR9ucqwk9_0_JGG")
App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDufYfCR9ucqwk9_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-12.11830000000000,18.54246000000000,0.00000000000000),App.Vector(10.79695000000000,19.02092000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(10.79695000000000,19.02092000000000,0.00000000000000),App.Vector(27.20902000000000,12.18187000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(27.20902000000000,-23.28097000000000,0.00000000000000),App.Vector(27.20902000000000,12.18187000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-27.71602000000000,-23.28097000000000,0.00000000000000),App.Vector(27.20902000000000,-23.28097000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-27.71602000000000,10.00786000000000,0.00000000000000),App.Vector(-27.71602000000000,-23.28097000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-12.11830000000000,18.54246000000000,0.00000000000000),App.Vector(-27.71602000000000,10.00786000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Pad","Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG")
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG")
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").Length = 14.478
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FAh9EKQYRt6ExvV_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Plane", "plane_Sketch_Fv756LNpoi1g9VE_1_JJC")
origin = App.Vector(-0.25350000000000,-2.00312000000000,14.47800000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fv756LNpoi1g9VE_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("Sketcher::SketchObject","Sketch_Fv756LNpoi1g9VE_1_JJC")
App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fv756LNpoi1g9VE_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJC").addGeometry(Part.Circle(App.Vector(-12.02068000000000,5.00282000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.62932000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Pocket","Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC")
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJC")
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Plane", "plane_Sketch_Fv756LNpoi1g9VE_1_JJG")
origin = App.Vector(-0.25350000000000,-2.00312000000000,14.47800000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fv756LNpoi1g9VE_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("Sketcher::SketchObject","Sketch_Fv756LNpoi1g9VE_1_JJG")
App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fv756LNpoi1g9VE_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJG").addGeometry(Part.Circle(App.Vector(13.96979000000000,2.00312000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.93750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Pocket","Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG")
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJG")
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fv756LNpoi1g9VE_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fv756LNpoi1g9VE_1_FqaaFKMysRqdX78_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Plane", "plane_Sketch_FuAw7M7ywvIhTgA_1_JLC")
origin = App.Vector(-0.25350000000000,-2.00312000000000,14.47800000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuAw7M7ywvIhTgA_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("Sketcher::SketchObject","Sketch_FuAw7M7ywvIhTgA_1_JLC")
App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuAw7M7ywvIhTgA_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").addGeometry(Part.LineSegment(App.Vector(-19.65796000000000,-6.22610000000000,0.00000000000000),App.Vector(-10.88767000000000,-13.06598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").addGeometry(Part.LineSegment(App.Vector(-10.88767000000000,-13.06598000000000,0.00000000000000),App.Vector(13.05651000000000,-13.06598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").addGeometry(Part.LineSegment(App.Vector(13.05651000000000,-13.06598000000000,0.00000000000000),App.Vector(21.84544000000000,-7.07503000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").addGeometry(Part.LineSegment(App.Vector(21.84544000000000,-7.07503000000000,0.00000000000000),App.Vector(25.24028000000000,-12.87478000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").addGeometry(Part.LineSegment(App.Vector(13.85888000000000,-19.75325000000000,0.00000000000000),App.Vector(25.24028000000000,-12.87478000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").addGeometry(Part.LineSegment(App.Vector(-12.30275000000000,-19.75325000000000,0.00000000000000),App.Vector(13.85888000000000,-19.75325000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").addGeometry(Part.LineSegment(App.Vector(-25.26252000000000,-9.64604000000000,0.00000000000000),App.Vector(-12.30275000000000,-19.75325000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").addGeometry(Part.LineSegment(App.Vector(-19.65796000000000,-6.22610000000000,0.00000000000000),App.Vector(-25.26252000000000,-9.64604000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Pocket","Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC")
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC")
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Plane", "plane_Sketch_FuAw7M7ywvIhTgA_1_JLK")
origin = App.Vector(-0.25350000000000,-2.00312000000000,14.47800000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuAw7M7ywvIhTgA_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("Sketcher::SketchObject","Sketch_FuAw7M7ywvIhTgA_1_JLK")
App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuAw7M7ywvIhTgA_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK").addGeometry(Part.LineSegment(App.Vector(10.57173000000000,16.99006000000000,0.00000000000000),App.Vector(21.32708000000000,13.02261000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK").addGeometry(Part.LineSegment(App.Vector(21.32708000000000,13.02261000000000,0.00000000000000),App.Vector(21.14686000000000,10.00263000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK").addGeometry(Part.LineSegment(App.Vector(9.56956000000000,14.27328000000000,0.00000000000000),App.Vector(21.14686000000000,10.00263000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK").addGeometry(Part.LineSegment(App.Vector(10.57173000000000,16.99006000000000,0.00000000000000),App.Vector(9.56956000000000,14.27328000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Pocket","Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK")
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK")
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Plane", "plane_Sketch_FuAw7M7ywvIhTgA_1_JLG")
origin = App.Vector(-0.25350000000000,-2.00312000000000,14.47800000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuAw7M7ywvIhTgA_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("Sketcher::SketchObject","Sketch_FuAw7M7ywvIhTgA_1_JLG")
App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuAw7M7ywvIhTgA_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG").addGeometry(Part.LineSegment(App.Vector(-17.85222000000000,14.27328000000000,0.00000000000000),App.Vector(-4.91603000000000,16.99006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG").addGeometry(Part.LineSegment(App.Vector(-4.91603000000000,16.99006000000000,0.00000000000000),App.Vector(-3.93881000000000,13.75111000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG").addGeometry(Part.LineSegment(App.Vector(-17.15945000000000,10.97459000000000,0.00000000000000),App.Vector(-3.93881000000000,13.75111000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG").addGeometry(Part.LineSegment(App.Vector(-17.85222000000000,14.27328000000000,0.00000000000000),App.Vector(-17.15945000000000,10.97459000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Pocket","Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG")
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG")
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuAw7M7ywvIhTgA_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuAw7M7ywvIhTgA_1_FBmmHsaz2PGh2ht_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Plane", "plane_Sketch_FDufYfCR9ucqwk9_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDufYfCR9ucqwk9_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("Sketcher::SketchObject","Sketch_FDufYfCR9ucqwk9_0_JGC")
App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDufYfCR9ucqwk9_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGC").addGeometry(Part.LineSegment(App.Vector(-12.11830000000000,18.54246000000000,0.00000000000000),App.Vector(0.00000000000000,30.22275000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,30.22275000000000,0.00000000000000),App.Vector(10.79695000000000,19.02092000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGC").addGeometry(Part.LineSegment(App.Vector(-12.11830000000000,18.54246000000000,0.00000000000000),App.Vector(10.79695000000000,19.02092000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Pad","Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC")
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGC")
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").Length = 3.048
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDufYfCR9ucqwk9_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDufYfCR9ucqwk9_0_FYWdeuvLfcHkAJD_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Plane", "plane_Sketch_FFXkl0F0Etfyi61_1_JTC")
origin = App.Vector(-0.66068000000000,24.38261000000000,3.04800000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFXkl0F0Etfyi61_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("Sketcher::SketchObject","Sketch_FFXkl0F0Etfyi61_1_JTC")
App.ActiveDocument.getObject("Sketch_FFXkl0F0Etfyi61_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFXkl0F0Etfyi61_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FFXkl0F0Etfyi61_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFXkl0F0Etfyi61_1_JTC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.49204000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFXkl0F0Etfyi61_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFXkl0F0Etfyi61_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FDufYfCR9ucqwk9_0").newObject("PartDesign::Pocket","Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC")
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FFXkl0F0Etfyi61_1_JTC")
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFXkl0F0Etfyi61_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFXkl0F0Etfyi61_1_F7UqKHFuXYrQQ77_1_JTC").Offset = 0
App.ActiveDocument.recompute()

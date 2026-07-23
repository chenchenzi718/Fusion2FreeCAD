import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00745902")
App.ActiveDocument.addObject("PartDesign::Body","Body_FZbLHCo0w5QJfrn_0")
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").Label = "Body_FZbLHCo0w5QJfrn_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_FZbLHCo0w5QJfrn_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZbLHCo0w5QJfrn_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_FZbLHCo0w5QJfrn_0_JGK")
App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZbLHCo0w5QJfrn_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,6.35000000000000,0.00000000000000),App.Vector(-6.35000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,6.35000000000000,0.00000000000000),App.Vector(-6.35000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,38.10000000000000,0.00000000000000),App.Vector(57.15000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").addGeometry(Part.LineSegment(App.Vector(57.15000000000000,38.10000000000000,0.00000000000000),App.Vector(57.15000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").addGeometry(Part.LineSegment(App.Vector(57.15000000000000,6.35000000000000,0.00000000000000),App.Vector(50.80000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").addGeometry(Part.LineSegment(App.Vector(50.80000000000000,6.35000000000000,0.00000000000000),App.Vector(50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pad","Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK")
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK")
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_FZbLHCo0w5QJfrn_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZbLHCo0w5QJfrn_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_FZbLHCo0w5QJfrn_0_JGG")
App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZbLHCo0w5QJfrn_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGG").addGeometry(Part.LineSegment(App.Vector(57.15000000000000,6.35000000000000,0.00000000000000),App.Vector(50.80000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGG").addGeometry(Part.LineSegment(App.Vector(50.80000000000000,6.35000000000000,0.00000000000000),App.Vector(50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(50.80000000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pad","Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG")
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGG")
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_FZbLHCo0w5QJfrn_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZbLHCo0w5QJfrn_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_FZbLHCo0w5QJfrn_0_JGC")
App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZbLHCo0w5QJfrn_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,6.35000000000000,0.00000000000000),App.Vector(-6.35000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pad","Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC")
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGC")
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZbLHCo0w5QJfrn_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZbLHCo0w5QJfrn_0_F1LXWIQIG7t18WQ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_FpqQSPizRD6nUbj_1_JJK")
origin = App.Vector(25.40000000000000,38.10000000000000,22.35835000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpqQSPizRD6nUbj_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_FpqQSPizRD6nUbj_1_JJK")
App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpqQSPizRD6nUbj_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK").addGeometry(Part.LineSegment(App.Vector(31.75000000000000,-16.00835000000000,0.00000000000000),App.Vector(31.75000000000000,9.39165000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK").addGeometry(Part.LineSegment(App.Vector(31.75000000000000,9.39165000000000,0.00000000000000),App.Vector(6.35000000000000,9.39165000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,9.39165000000000,0.00000000000000),App.Vector(6.35000000000000,-16.00835000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK").addGeometry(Part.LineSegment(App.Vector(31.75000000000000,-16.00835000000000,0.00000000000000),App.Vector(6.35000000000000,-16.00835000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pad","Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK")
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK")
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_FpqQSPizRD6nUbj_1_JJC")
origin = App.Vector(25.40000000000000,38.10000000000000,22.35835000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpqQSPizRD6nUbj_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_FpqQSPizRD6nUbj_1_JJC")
App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpqQSPizRD6nUbj_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJC").addGeometry(Part.LineSegment(App.Vector(31.75000000000000,9.39165000000000,0.00000000000000),App.Vector(6.35000000000000,9.39165000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(19.05000000000000,9.39165000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.70000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pad","Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC")
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJC")
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpqQSPizRD6nUbj_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpqQSPizRD6nUbj_1_Foob8IgjBVcAvfB_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_FbI1HQzcSmNyRZz_1_JNC")
origin = App.Vector(12.81430000000000,25.40000000000000,25.51430000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbI1HQzcSmNyRZz_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_FbI1HQzcSmNyRZz_1_JNC")
App.ActiveDocument.getObject("Sketch_FbI1HQzcSmNyRZz_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbI1HQzcSmNyRZz_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FbI1HQzcSmNyRZz_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbI1HQzcSmNyRZz_1_JNC").addGeometry(Part.Circle(App.Vector(-6.46430000000000,6.23570000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbI1HQzcSmNyRZz_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbI1HQzcSmNyRZz_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pocket","Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC")
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FbI1HQzcSmNyRZz_1_JNC")
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbI1HQzcSmNyRZz_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbI1HQzcSmNyRZz_1_FE9Di9Hv3ggE16k_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_Fhs0pKEhT3EM3Nr_1_JRC")
origin = App.Vector(25.40000000000000,19.05000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fhs0pKEhT3EM3Nr_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_Fhs0pKEhT3EM3Nr_1_JRC")
App.ActiveDocument.getObject("Sketch_Fhs0pKEhT3EM3Nr_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fhs0pKEhT3EM3Nr_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fhs0pKEhT3EM3Nr_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fhs0pKEhT3EM3Nr_1_JRC").addGeometry(Part.Circle(App.Vector(-22.22500000000000,-10.06974000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fhs0pKEhT3EM3Nr_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fhs0pKEhT3EM3Nr_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pocket","Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC")
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fhs0pKEhT3EM3Nr_1_JRC")
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fhs0pKEhT3EM3Nr_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fhs0pKEhT3EM3Nr_1_FgfSEw5rnUs7Qqc_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_FrpErPZm2dQb80q_1_JVG")
origin = App.Vector(25.40000000000000,19.05000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrpErPZm2dQb80q_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_FrpErPZm2dQb80q_1_JVG")
App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrpErPZm2dQb80q_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVG").addGeometry(Part.Circle(App.Vector(22.22500000000000,9.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pocket","Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG")
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVG")
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_FrpErPZm2dQb80q_1_JVC")
origin = App.Vector(25.40000000000000,19.05000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrpErPZm2dQb80q_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_FrpErPZm2dQb80q_1_JVC")
App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrpErPZm2dQb80q_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVC").addGeometry(Part.Circle(App.Vector(22.22500000000000,-9.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pocket","Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC")
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVC")
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrpErPZm2dQb80q_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrpErPZm2dQb80q_1_FPJEs8WIMIBYt3s_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Plane", "plane_Sketch_Fwd7MKVSTcmPOz3_1_JZC")
origin = App.Vector(25.40000000000000,38.10000000000000,22.35835000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fwd7MKVSTcmPOz3_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("Sketcher::SketchObject","Sketch_Fwd7MKVSTcmPOz3_1_JZC")
App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fwd7MKVSTcmPOz3_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,3.04165000000000,0.00000000000000),App.Vector(-6.35000000000000,3.04165000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,3.04165000000000,0.00000000000000),App.Vector(-6.35000000000000,-16.00835000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-16.00835000000000,0.00000000000000),App.Vector(-6.35000000000000,-16.00835000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-16.00835000000000,0.00000000000000),App.Vector(6.35000000000000,3.04165000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZbLHCo0w5QJfrn_0").newObject("PartDesign::Pad","Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC")
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC")
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fwd7MKVSTcmPOz3_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").Type = 0
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fwd7MKVSTcmPOz3_1_FJTELTKikM25lOK_1_JZC").Offset = 0
App.ActiveDocument.recompute()

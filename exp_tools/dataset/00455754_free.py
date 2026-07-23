import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00455754")
App.ActiveDocument.addObject("PartDesign::Body","Body_FgnTzXT4IHz8pRo_0")
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").Label = "Body_FgnTzXT4IHz8pRo_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Plane", "plane_Sketch_FgnTzXT4IHz8pRo_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgnTzXT4IHz8pRo_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("Sketcher::SketchObject","Sketch_FgnTzXT4IHz8pRo_0_JGK")
App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgnTzXT4IHz8pRo_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,2133.59999999999991,0.00000000000000),App.Vector(-50.80000000000000,2133.59999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,2133.59999999999991,0.00000000000000),App.Vector(-50.80000000000000,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000),App.Vector(-50.80000000000000,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,2133.59999999999991,0.00000000000000),App.Vector(0.00000000000000,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Pad","Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK")
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK")
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Plane", "plane_Sketch_FgnTzXT4IHz8pRo_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgnTzXT4IHz8pRo_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("Sketcher::SketchObject","Sketch_FgnTzXT4IHz8pRo_0_JGG")
App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgnTzXT4IHz8pRo_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,2133.59999999999991,0.00000000000000),App.Vector(457.19999999999999,2133.59999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG").addGeometry(Part.LineSegment(App.Vector(457.19999999999999,2133.59999999999991,0.00000000000000),App.Vector(457.19999999999999,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,2082.80000000000018,0.00000000000000),App.Vector(457.19999999999999,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,2133.59999999999991,0.00000000000000),App.Vector(0.00000000000000,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Pad","Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG")
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG")
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Plane", "plane_Sketch_FgnTzXT4IHz8pRo_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgnTzXT4IHz8pRo_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("Sketcher::SketchObject","Sketch_FgnTzXT4IHz8pRo_0_JGC")
App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgnTzXT4IHz8pRo_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,2133.59999999999991,0.00000000000000),App.Vector(-508.00000000000000,2133.59999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC").addGeometry(Part.LineSegment(App.Vector(-508.00000000000000,2133.59999999999991,0.00000000000000),App.Vector(-508.00000000000000,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,2082.80000000000018,0.00000000000000),App.Vector(-508.00000000000000,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,2133.59999999999991,0.00000000000000),App.Vector(-50.80000000000000,2082.80000000000018,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Pad","Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC")
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC")
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgnTzXT4IHz8pRo_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgnTzXT4IHz8pRo_0_F6wORaJxn0qLHcu_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Plane", "plane_Sketch_FwoOlCF7n2Cuf0P_1_JJC")
origin = App.Vector(-25.40000000000000,1676.39999999999986,50.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwoOlCF7n2Cuf0P_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("Sketcher::SketchObject","Sketch_FwoOlCF7n2Cuf0P_1_JJC")
App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwoOlCF7n2Cuf0P_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC").addGeometry(Part.LineSegment(App.Vector(-482.60000000000002,457.20000000000005,0.00000000000000),App.Vector(-431.80000000000001,457.20000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC").addGeometry(Part.LineSegment(App.Vector(-431.80000000000001,457.20000000000005,0.00000000000000),App.Vector(-431.80000000000001,406.40000000000032,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC").addGeometry(Part.LineSegment(App.Vector(-482.60000000000002,406.40000000000032,0.00000000000000),App.Vector(-431.80000000000001,406.40000000000032,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC").addGeometry(Part.LineSegment(App.Vector(-482.60000000000002,457.20000000000005,0.00000000000000),App.Vector(-482.60000000000002,406.40000000000032,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Pad","Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC")
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC")
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Plane", "plane_Sketch_FwoOlCF7n2Cuf0P_1_JJG")
origin = App.Vector(-25.40000000000000,1676.39999999999986,50.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwoOlCF7n2Cuf0P_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("Sketcher::SketchObject","Sketch_FwoOlCF7n2Cuf0P_1_JJG")
App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwoOlCF7n2Cuf0P_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG").addGeometry(Part.LineSegment(App.Vector(482.59999999999997,457.20000000000005,0.00000000000000),App.Vector(431.79999999999995,457.20000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG").addGeometry(Part.LineSegment(App.Vector(431.79999999999995,457.20000000000005,0.00000000000000),App.Vector(431.79999999999995,406.40000000000032,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG").addGeometry(Part.LineSegment(App.Vector(482.59999999999997,406.40000000000032,0.00000000000000),App.Vector(431.79999999999995,406.40000000000032,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG").addGeometry(Part.LineSegment(App.Vector(482.59999999999997,457.20000000000005,0.00000000000000),App.Vector(482.59999999999997,406.40000000000032,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Pad","Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG")
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG")
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwoOlCF7n2Cuf0P_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwoOlCF7n2Cuf0P_1_FrLeBlZOkMPc6hx_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Plane", "plane_Sketch_F0SxefWjaZdTcoC_1_JOC")
origin = App.Vector(-25.40000000000000,1676.39999999999986,50.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0SxefWjaZdTcoC_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("Sketcher::SketchObject","Sketch_F0SxefWjaZdTcoC_1_JOC")
App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0SxefWjaZdTcoC_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-457.19999999999982,0.00000000000000),App.Vector(25.40000000000000,-457.19999999999982,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-457.19999999999982,0.00000000000000),App.Vector(25.40000000000000,-507.99999999999977,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-507.99999999999977,0.00000000000000),App.Vector(25.40000000000000,-507.99999999999977,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-457.19999999999982,0.00000000000000),App.Vector(-25.40000000000000,-507.99999999999977,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Pad","Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC")
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC")
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0SxefWjaZdTcoC_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0SxefWjaZdTcoC_1_F6YDhzuxKresxnC_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Plane", "plane_Sketch_Ffjwpia2JAnFd8N_1_JSC")
origin = App.Vector(-25.40000000000000,381.00000000000000,50.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ffjwpia2JAnFd8N_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("Sketcher::SketchObject","Sketch_Ffjwpia2JAnFd8N_1_JSC")
App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ffjwpia2JAnFd8N_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,431.79999999999995,0.00000000000000),App.Vector(25.40000000000000,431.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,431.79999999999995,0.00000000000000),App.Vector(25.40000000000000,381.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,381.00000000000000,0.00000000000000),App.Vector(25.40000000000000,381.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,431.79999999999995,0.00000000000000),App.Vector(-25.40000000000000,381.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Pad","Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC")
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC")
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").Length = 304.8
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ffjwpia2JAnFd8N_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").Type = 4
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ffjwpia2JAnFd8N_1_FxnFcAD6QJYAYEE_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Plane", "plane_Sketch_FHlRlwwxyESWcGS_1_JWC")
origin = App.Vector(-50.80000000000000,1041.40000000000009,482.59999999999997)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHlRlwwxyESWcGS_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("Sketcher::SketchObject","Sketch_FHlRlwwxyESWcGS_1_JWC")
App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHlRlwwxyESWcGS_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWC").addGeometry(Part.Circle(App.Vector(901.70000000000016,-457.19999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.93750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Pocket","Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC")
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWC")
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Plane", "plane_Sketch_FHlRlwwxyESWcGS_1_JWG")
origin = App.Vector(-50.80000000000000,1041.40000000000009,482.59999999999997)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHlRlwwxyESWcGS_1_JWG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("Sketcher::SketchObject","Sketch_FHlRlwwxyESWcGS_1_JWG")
App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHlRlwwxyESWcGS_1_JWG"), [""])
App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWG").addGeometry(Part.Circle(App.Vector(1003.30000000000007,-457.19999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.93750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgnTzXT4IHz8pRo_0").newObject("PartDesign::Pocket","Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG")
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").Profile = App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWG")
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHlRlwwxyESWcGS_1_JWG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").Type = 4
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHlRlwwxyESWcGS_1_FmdnvO78fRbhuwg_1_JWG").Offset = 0
App.ActiveDocument.recompute()

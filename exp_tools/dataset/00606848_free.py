import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00606848")
App.ActiveDocument.addObject("PartDesign::Body","Body_FYbfxXvmtZUwIiy_0")
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").Label = "Body_FYbfxXvmtZUwIiy_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Plane", "plane_Sketch_FYbfxXvmtZUwIiy_0_JHC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYbfxXvmtZUwIiy_0_JHC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("Sketcher::SketchObject","Sketch_FYbfxXvmtZUwIiy_0_JHC")
App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYbfxXvmtZUwIiy_0_JHC"), [""])
App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(203.19999999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC").addGeometry(Part.LineSegment(App.Vector(203.19999999999999,0.00000000000000,0.00000000000000),App.Vector(203.19999999999999,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,50.80000000000000,0.00000000000000),App.Vector(203.19999999999999,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Pad","Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC")
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").Profile = App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC")
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").Length = 3048.0000000000005
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYbfxXvmtZUwIiy_0_JHC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").Type = 4
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYbfxXvmtZUwIiy_0_FqQexEQ3xcB0jFZ_0_JHC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Plane", "plane_Sketch_FsT5CndLqEJgKGu_1_JKC")
origin = App.Vector(101.59999999999999,-1524.00000000000000,50.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsT5CndLqEJgKGu_1_JKC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("Sketcher::SketchObject","Sketch_FsT5CndLqEJgKGu_1_JKC")
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsT5CndLqEJgKGu_1_JKC"), [""])
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,-1524.00000000000000,0.00000000000000),App.Vector(50.80000000000001,-1524.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC").addGeometry(Part.LineSegment(App.Vector(50.80000000000001,-1524.00000000000000,0.00000000000000),App.Vector(50.80000000000001,-1422.40000000000009,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,-1422.40000000000009,0.00000000000000),App.Vector(50.80000000000001,-1422.40000000000009,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,-1524.00000000000000,0.00000000000000),App.Vector(-50.80000000000000,-1422.40000000000009,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Pad","Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC")
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").Profile = App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC")
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").Length = 762.0000000000001
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").Type = 4
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Plane", "plane_Sketch_FsT5CndLqEJgKGu_1_JKO")
origin = App.Vector(101.59999999999999,-1524.00000000000000,50.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsT5CndLqEJgKGu_1_JKO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("Sketcher::SketchObject","Sketch_FsT5CndLqEJgKGu_1_JKO")
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsT5CndLqEJgKGu_1_JKO"), [""])
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000),App.Vector(50.80000000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO").addGeometry(Part.LineSegment(App.Vector(50.80000000000001,-50.79999999999995,0.00000000000000),App.Vector(50.80000000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO").addGeometry(Part.LineSegment(App.Vector(50.80000000000001,-50.79999999999995,0.00000000000000),App.Vector(-50.80000000000000,-50.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,-50.79999999999995,0.00000000000000),App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Pad","Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO")
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").Profile = App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO")
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").Length = 762.0000000000001
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").Type = 4
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Plane", "plane_Sketch_FsT5CndLqEJgKGu_1_JKK")
origin = App.Vector(101.59999999999999,-1524.00000000000000,50.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsT5CndLqEJgKGu_1_JKK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("Sketcher::SketchObject","Sketch_FsT5CndLqEJgKGu_1_JKK")
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsT5CndLqEJgKGu_1_JKK"), [""])
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000),App.Vector(50.80000000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK").addGeometry(Part.LineSegment(App.Vector(50.80000000000001,50.79999999999995,0.00000000000000),App.Vector(50.80000000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK").addGeometry(Part.LineSegment(App.Vector(50.80000000000001,50.79999999999995,0.00000000000000),App.Vector(-50.80000000000000,50.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,50.79999999999995,0.00000000000000),App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Pad","Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK")
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").Profile = App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK")
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").Length = 762.0000000000001
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").Type = 4
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Plane", "plane_Sketch_FsT5CndLqEJgKGu_1_JKG")
origin = App.Vector(101.59999999999999,-1524.00000000000000,50.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsT5CndLqEJgKGu_1_JKG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("Sketcher::SketchObject","Sketch_FsT5CndLqEJgKGu_1_JKG")
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsT5CndLqEJgKGu_1_JKG"), [""])
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,1524.00000000000000,0.00000000000000),App.Vector(50.80000000000001,1524.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG").addGeometry(Part.LineSegment(App.Vector(50.80000000000001,1524.00000000000000,0.00000000000000),App.Vector(50.80000000000001,1422.40000000000009,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,1422.40000000000009,0.00000000000000),App.Vector(50.80000000000001,1422.40000000000009,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,1524.00000000000000,0.00000000000000),App.Vector(-50.80000000000000,1422.40000000000009,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Pad","Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG")
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").Profile = App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG")
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").Length = 762.0000000000001
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsT5CndLqEJgKGu_1_JKG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").Type = 4
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsT5CndLqEJgKGu_1_FIR6sUS3NdumypX_1_JKG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Plane", "plane_Sketch_FpthJgSQhn07FCo_1_JOC")
origin = App.Vector(152.40000000000001,-1524.00000000000000,457.19999999999999)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpthJgSQhn07FCo_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("Sketcher::SketchObject","Sketch_FpthJgSQhn07FCo_1_JOC")
App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpthJgSQhn07FCo_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC").addGeometry(Part.LineSegment(App.Vector(1524.00000000000000,355.59999999999997,0.00000000000000),App.Vector(1574.79999999999995,355.59999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC").addGeometry(Part.LineSegment(App.Vector(1574.79999999999995,355.59999999999997,0.00000000000000),App.Vector(1574.79999999999995,254.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC").addGeometry(Part.LineSegment(App.Vector(1524.00000000000000,254.00000000000006,0.00000000000000),App.Vector(1574.79999999999995,254.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC").addGeometry(Part.LineSegment(App.Vector(1524.00000000000000,355.59999999999997,0.00000000000000),App.Vector(1524.00000000000000,254.00000000000006,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Pad","Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC")
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC")
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpthJgSQhn07FCo_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").Type = 0
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpthJgSQhn07FCo_1_FloF146Sxz9eIRE_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Plane", "plane_Sketch_FYZNdZg2wCTq3bB_1_JSC")
origin = App.Vector(152.40000000000001,-1524.00000000000000,457.19999999999999)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYZNdZg2wCTq3bB_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("Sketcher::SketchObject","Sketch_FYZNdZg2wCTq3bB_1_JSC")
App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYZNdZg2wCTq3bB_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC").addGeometry(Part.LineSegment(App.Vector(-1524.00000000000000,355.59999999999997,0.00000000000000),App.Vector(-1574.80000000000018,355.59999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC").addGeometry(Part.LineSegment(App.Vector(-1574.80000000000018,355.59999999999997,0.00000000000000),App.Vector(-1574.80000000000018,254.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC").addGeometry(Part.LineSegment(App.Vector(-1524.00000000000000,254.00000000000006,0.00000000000000),App.Vector(-1574.80000000000018,254.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC").addGeometry(Part.LineSegment(App.Vector(-1524.00000000000000,355.59999999999997,0.00000000000000),App.Vector(-1524.00000000000000,254.00000000000006,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Pad","Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC")
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC")
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYZNdZg2wCTq3bB_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").Type = 0
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYZNdZg2wCTq3bB_1_Fut2Lxgjq3QIcOZ_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Plane", "plane_Sketch_FTQ4nYR2yZobFis_1_JWC")
origin = App.Vector(152.40000000000001,-1524.00000000000000,457.19999999999999)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTQ4nYR2yZobFis_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("Sketcher::SketchObject","Sketch_FTQ4nYR2yZobFis_1_JWC")
App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTQ4nYR2yZobFis_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC").addGeometry(Part.LineSegment(App.Vector(50.79999999999995,355.59999999999997,0.00000000000000),App.Vector(101.59999999999991,355.59999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC").addGeometry(Part.LineSegment(App.Vector(101.59999999999991,355.59999999999997,0.00000000000000),App.Vector(101.59999999999991,254.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC").addGeometry(Part.LineSegment(App.Vector(50.79999999999995,254.00000000000006,0.00000000000000),App.Vector(101.59999999999991,254.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC").addGeometry(Part.LineSegment(App.Vector(50.79999999999995,355.59999999999997,0.00000000000000),App.Vector(50.79999999999995,254.00000000000006,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYbfxXvmtZUwIiy_0").newObject("PartDesign::Pad","Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC")
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC")
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTQ4nYR2yZobFis_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").Type = 0
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTQ4nYR2yZobFis_1_FcnmaTvfRb7fhFJ_1_JWC").Offset = 0
App.ActiveDocument.recompute()

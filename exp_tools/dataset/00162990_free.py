import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00162990")
App.ActiveDocument.addObject("PartDesign::Body","Body_FyABC9MpmANxvXH_0")
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").Label = "Body_FyABC9MpmANxvXH_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Plane", "plane_Sketch_FyABC9MpmANxvXH_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyABC9MpmANxvXH_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("Sketcher::SketchObject","Sketch_FyABC9MpmANxvXH_0_JGC")
App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyABC9MpmANxvXH_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").addGeometry(Part.LineSegment(App.Vector(317.50000000000000,-330.19999999999999,0.00000000000000),App.Vector(-317.50000000000000,-330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").addGeometry(Part.LineSegment(App.Vector(-317.50000000000000,-330.19999999999999,0.00000000000000),App.Vector(-317.50000000000000,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").addGeometry(Part.LineSegment(App.Vector(139.69999999999999,330.19999999999999,0.00000000000000),App.Vector(-317.50000000000000,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").addGeometry(Part.LineSegment(App.Vector(139.69999999999999,330.19999999999999,0.00000000000000),App.Vector(139.69999999999999,228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").addGeometry(Part.LineSegment(App.Vector(317.50000000000000,228.59999999999999,0.00000000000000),App.Vector(139.69999999999999,228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").addGeometry(Part.LineSegment(App.Vector(317.50000000000000,-330.19999999999999,0.00000000000000),App.Vector(317.50000000000000,228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Pad","Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC")
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC")
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyABC9MpmANxvXH_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyABC9MpmANxvXH_0_FRVvMCp2B4OhOi5_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Plane", "plane_Sketch_FqfpQmGYwPYjE1s_1_JJG")
origin = App.Vector(-0.00000000000000,-0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqfpQmGYwPYjE1s_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("Sketcher::SketchObject","Sketch_FqfpQmGYwPYjE1s_1_JJG")
App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqfpQmGYwPYjE1s_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG").addGeometry(Part.LineSegment(App.Vector(-241.29999999999998,228.59999999999999,0.00000000000000),App.Vector(-292.10000000000002,228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG").addGeometry(Part.LineSegment(App.Vector(-292.10000000000002,228.59999999999999,0.00000000000000),App.Vector(-292.10000000000002,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG").addGeometry(Part.LineSegment(App.Vector(-241.29999999999998,330.19999999999999,0.00000000000000),App.Vector(-292.10000000000002,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG").addGeometry(Part.LineSegment(App.Vector(-241.29999999999998,228.59999999999999,0.00000000000000),App.Vector(-241.29999999999998,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Pad","Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG")
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG")
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").Length = 9.525
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Plane", "plane_Sketch_FqfpQmGYwPYjE1s_1_JJC")
origin = App.Vector(-0.00000000000000,-0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqfpQmGYwPYjE1s_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("Sketcher::SketchObject","Sketch_FqfpQmGYwPYjE1s_1_JJC")
App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqfpQmGYwPYjE1s_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC").addGeometry(Part.LineSegment(App.Vector(-241.29999999999998,431.80000000000001,0.00000000000000),App.Vector(-292.10000000000002,431.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC").addGeometry(Part.LineSegment(App.Vector(-292.10000000000002,431.80000000000001,0.00000000000000),App.Vector(-292.10000000000002,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC").addGeometry(Part.LineSegment(App.Vector(-241.29999999999998,330.19999999999999,0.00000000000000),App.Vector(-292.10000000000002,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC").addGeometry(Part.LineSegment(App.Vector(-241.29999999999998,431.80000000000001,0.00000000000000),App.Vector(-241.29999999999998,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Pad","Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC")
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC")
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").Length = 9.525
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqfpQmGYwPYjE1s_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqfpQmGYwPYjE1s_1_FI9lQgvECwY1mXz_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Plane", "plane_Sketch_FdKLyKcCSR9HqZK_1_JNC")
origin = App.Vector(-0.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdKLyKcCSR9HqZK_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("Sketcher::SketchObject","Sketch_FdKLyKcCSR9HqZK_1_JNC")
App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdKLyKcCSR9HqZK_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,-295.27500000000003,0.00000000000000),App.Vector(63.50000000000000,-295.27500000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,-295.27500000000003,0.00000000000000),App.Vector(63.50000000000000,-304.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,-304.80000000000001,0.00000000000000),App.Vector(63.50000000000000,-304.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,-295.27500000000003,0.00000000000000),App.Vector(12.70000000000000,-304.80000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Pad","Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC")
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC")
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdKLyKcCSR9HqZK_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdKLyKcCSR9HqZK_1_Fv816D6Vvx8pNXC_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Plane", "plane_Sketch_Fx6T2jVczv0T5JX_1_JRC")
origin = App.Vector(38.10000000000000,304.80000000000001,-33.33750000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx6T2jVczv0T5JX_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("Sketcher::SketchObject","Sketch_Fx6T2jVczv0T5JX_1_JRC")
App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx6T2jVczv0T5JX_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-42.86250000000000,0.00000000000000),App.Vector(-25.40000000000000,-42.86250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-42.86250000000000,0.00000000000000),App.Vector(-25.40000000000000,-33.33750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-33.33750000000000,0.00000000000000),App.Vector(25.40000000000000,-33.33750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-42.86250000000000,0.00000000000000),App.Vector(25.40000000000000,-33.33750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Pad","Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC")
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC")
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").Length = 92.075
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx6T2jVczv0T5JX_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx6T2jVczv0T5JX_1_FrfDPYBYBtL90mn_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Plane", "plane_Sketch_FvgbMyVOSh48mXw_1_JVC")
origin = App.Vector(38.10000000000000,346.07500000000005,-76.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FvgbMyVOSh48mXw_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("Sketcher::SketchObject","Sketch_FvgbMyVOSh48mXw_1_JVC")
App.ActiveDocument.getObject("Sketch_FvgbMyVOSh48mXw_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FvgbMyVOSh48mXw_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FvgbMyVOSh48mXw_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FvgbMyVOSh48mXw_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-38.09999999999997,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FvgbMyVOSh48mXw_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FvgbMyVOSh48mXw_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Pocket","Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC")
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FvgbMyVOSh48mXw_1_JVC")
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FvgbMyVOSh48mXw_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FvgbMyVOSh48mXw_1_FCj7R2LcAzPkMKc_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Plane", "plane_Sketch_FH5VVADw3F8y8Ou_1_JZK")
origin = App.Vector(-0.00000000000000,-0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH5VVADw3F8y8Ou_1_JZK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("Sketcher::SketchObject","Sketch_FH5VVADw3F8y8Ou_1_JZK")
App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH5VVADw3F8y8Ou_1_JZK"), [""])
App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,396.87500000000000,0.00000000000000),App.Vector(63.50000000000000,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,330.19999999999999,0.00000000000000),App.Vector(12.70000000000000,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,396.87500000000000,0.00000000000000),App.Vector(12.70000000000000,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,396.87500000000000,0.00000000000000),App.Vector(63.50000000000000,396.87500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Pad","Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK")
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").Profile = App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK")
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").Length = 9.525
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").Type = 4
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Plane", "plane_Sketch_FH5VVADw3F8y8Ou_1_JZG")
origin = App.Vector(-0.00000000000000,-0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH5VVADw3F8y8Ou_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("Sketcher::SketchObject","Sketch_FH5VVADw3F8y8Ou_1_JZG")
App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH5VVADw3F8y8Ou_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,279.39999999999998,0.00000000000000),App.Vector(63.50000000000000,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,330.19999999999999,0.00000000000000),App.Vector(12.70000000000000,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,279.39999999999998,0.00000000000000),App.Vector(12.70000000000000,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,279.39999999999998,0.00000000000000),App.Vector(12.70000000000000,279.39999999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FyABC9MpmANxvXH_0").newObject("PartDesign::Pad","Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG")
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG")
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").Length = 9.525
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH5VVADw3F8y8Ou_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH5VVADw3F8y8Ou_1_FEjZAJnxRP8lgET_1_JZG").Offset = 0
App.ActiveDocument.recompute()

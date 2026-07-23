import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00840794")
App.ActiveDocument.addObject("PartDesign::Body","Body_F44bix5NupAvA3J_0")
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").Label = "Body_F44bix5NupAvA3J_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Plane", "plane_Sketch_F44bix5NupAvA3J_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F44bix5NupAvA3J_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("Sketcher::SketchObject","Sketch_F44bix5NupAvA3J_0_JGC")
App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F44bix5NupAvA3J_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC").addGeometry(Part.LineSegment(App.Vector(-61.80589000000001,35.82098999999999,0.00000000000000),App.Vector(82.94614000000000,35.82098999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC").addGeometry(Part.LineSegment(App.Vector(82.94614000000000,35.82098999999999,0.00000000000000),App.Vector(82.94614000000000,-43.16136000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC").addGeometry(Part.LineSegment(App.Vector(-61.80589000000001,-43.16136000000000,0.00000000000000),App.Vector(82.94614000000000,-43.16136000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC").addGeometry(Part.LineSegment(App.Vector(-61.80589000000001,35.82098999999999,0.00000000000000),App.Vector(-61.80589000000001,-43.16136000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Pad","Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC")
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC")
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F44bix5NupAvA3J_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F44bix5NupAvA3J_0_FoliGs6lh1x6fum_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Plane", "plane_Sketch_Fz9kEhl6djQ5q1Y_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fz9kEhl6djQ5q1Y_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("Sketcher::SketchObject","Sketch_Fz9kEhl6djQ5q1Y_1_JJC")
App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fz9kEhl6djQ5q1Y_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-48.88684000000000,-33.17846000000000,0.00000000000000),App.Vector(72.66963000000000,-33.17846000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(72.66963000000000,-33.17846000000000,0.00000000000000),App.Vector(72.66963000000000,-39.63798000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-48.88684000000000,-39.63798000000001,0.00000000000000),App.Vector(72.66963000000000,-39.63798000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-48.88684000000000,-33.17846000000000,0.00000000000000),App.Vector(-48.88684000000000,-39.63798000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Pad","Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC")
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC")
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Plane", "plane_Sketch_Fz9kEhl6djQ5q1Y_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fz9kEhl6djQ5q1Y_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("Sketcher::SketchObject","Sketch_Fz9kEhl6djQ5q1Y_1_JJG")
App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fz9kEhl6djQ5q1Y_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG").addGeometry(Part.LineSegment(App.Vector(-48.88684000000000,26.13171000000000,0.00000000000000),App.Vector(72.66963000000000,26.13171000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG").addGeometry(Part.LineSegment(App.Vector(72.66963000000000,26.13171000000000,0.00000000000000),App.Vector(72.66963000000000,33.47207000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG").addGeometry(Part.LineSegment(App.Vector(-48.88684000000000,33.47207000000000,0.00000000000000),App.Vector(72.66963000000000,33.47207000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG").addGeometry(Part.LineSegment(App.Vector(-48.88684000000000,26.13171000000000,0.00000000000000),App.Vector(-48.88684000000000,33.47207000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Pad","Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG")
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG")
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fz9kEhl6djQ5q1Y_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fz9kEhl6djQ5q1Y_1_F5xOtaYCpvBVurZ_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Plane", "plane_Sketch_Fgo7rVd0Ybj0ZaP_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fgo7rVd0Ybj0ZaP_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("Sketcher::SketchObject","Sketch_Fgo7rVd0Ybj0ZaP_1_JNC")
App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fgo7rVd0Ybj0ZaP_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-48.59323000000000,33.47207000000000,0.00000000000000),App.Vector(-54.46552000000001,33.47207000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-54.46552000000001,33.47207000000000,0.00000000000000),App.Vector(-54.46552000000001,-39.34437000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-48.59323000000000,-39.34437000000000,0.00000000000000),App.Vector(-54.46552000000001,-39.34437000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-48.59323000000000,33.47207000000000,0.00000000000000),App.Vector(-48.59323000000000,-39.34437000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Pad","Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC")
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC")
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Plane", "plane_Sketch_Fgo7rVd0Ybj0ZaP_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fgo7rVd0Ybj0ZaP_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("Sketcher::SketchObject","Sketch_Fgo7rVd0Ybj0ZaP_1_JNG")
App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fgo7rVd0Ybj0ZaP_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG").addGeometry(Part.LineSegment(App.Vector(71.49518000000000,33.47207000000000,0.00000000000000),App.Vector(78.83553999999999,33.47207000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG").addGeometry(Part.LineSegment(App.Vector(78.83553999999999,33.47207000000000,0.00000000000000),App.Vector(78.83553999999999,-39.34437000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG").addGeometry(Part.LineSegment(App.Vector(71.49518000000000,-39.34437000000000,0.00000000000000),App.Vector(78.83553999999999,-39.34437000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG").addGeometry(Part.LineSegment(App.Vector(71.49518000000000,33.47207000000000,0.00000000000000),App.Vector(71.49518000000000,-39.34437000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Pad","Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG")
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG")
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fgo7rVd0Ybj0ZaP_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fgo7rVd0Ybj0ZaP_1_FoFRUJtvoNrGNWY_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Plane", "plane_Sketch_FzuPTyA0h9xjDWk_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzuPTyA0h9xjDWk_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("Sketcher::SketchObject","Sketch_FzuPTyA0h9xjDWk_1_JRC")
App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzuPTyA0h9xjDWk_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC").addGeometry(Part.LineSegment(App.Vector(-54.46552000000001,11.74459000000000,0.00000000000000),App.Vector(-48.88684000000000,11.74459000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC").addGeometry(Part.LineSegment(App.Vector(-48.88684000000000,11.74459000000000,0.00000000000000),App.Vector(-48.88684000000000,-17.61688000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC").addGeometry(Part.LineSegment(App.Vector(-54.46552000000001,-17.61688000000000,0.00000000000000),App.Vector(-48.88684000000000,-17.61688000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC").addGeometry(Part.LineSegment(App.Vector(-54.46552000000001,11.74459000000000,0.00000000000000),App.Vector(-54.46552000000001,-17.61688000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Pad","Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC")
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC")
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").Length = 63.5
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Plane", "plane_Sketch_FzuPTyA0h9xjDWk_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzuPTyA0h9xjDWk_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("Sketcher::SketchObject","Sketch_FzuPTyA0h9xjDWk_1_JRG")
App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzuPTyA0h9xjDWk_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG").addGeometry(Part.LineSegment(App.Vector(71.49518000000000,11.74459000000000,0.00000000000000),App.Vector(78.54192999999999,11.74459000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG").addGeometry(Part.LineSegment(App.Vector(78.54192999999999,11.74459000000000,0.00000000000000),App.Vector(78.54192999999999,-17.91050000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG").addGeometry(Part.LineSegment(App.Vector(71.49518000000000,-17.91050000000000,0.00000000000000),App.Vector(78.54192999999999,-17.91050000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG").addGeometry(Part.LineSegment(App.Vector(71.49518000000000,11.74459000000000,0.00000000000000),App.Vector(71.49518000000000,-17.91050000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Pad","Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG")
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG")
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").Length = 63.5
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzuPTyA0h9xjDWk_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzuPTyA0h9xjDWk_1_FG6XZ4mJLBR1yLA_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Plane", "plane_Sketch_FLv9EYSiyulPDBJ_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLv9EYSiyulPDBJ_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("Sketcher::SketchObject","Sketch_FLv9EYSiyulPDBJ_1_JVC")
App.ActiveDocument.getObject("Sketch_FLv9EYSiyulPDBJ_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLv9EYSiyulPDBJ_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FLv9EYSiyulPDBJ_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLv9EYSiyulPDBJ_1_JVC").addGeometry(Part.Circle(App.Vector(-3.08296000000000,58.42932000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.08000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLv9EYSiyulPDBJ_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLv9EYSiyulPDBJ_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Pad","Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC")
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FLv9EYSiyulPDBJ_1_JVC")
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLv9EYSiyulPDBJ_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLv9EYSiyulPDBJ_1_FXpqj6EQXHpaK4E_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Plane", "plane_Sketch_FoApDTK0Hk5ewFN_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoApDTK0Hk5ewFN_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("Sketcher::SketchObject","Sketch_FoApDTK0Hk5ewFN_1_JZC")
App.ActiveDocument.getObject("Sketch_FoApDTK0Hk5ewFN_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoApDTK0Hk5ewFN_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FoApDTK0Hk5ewFN_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoApDTK0Hk5ewFN_1_JZC").addGeometry(Part.Circle(App.Vector(-2.78934000000000,58.42932000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.08000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoApDTK0Hk5ewFN_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoApDTK0Hk5ewFN_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F44bix5NupAvA3J_0").newObject("PartDesign::Pad","Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC")
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FoApDTK0Hk5ewFN_1_JZC")
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoApDTK0Hk5ewFN_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").Type = 0
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoApDTK0Hk5ewFN_1_F4NZJw8z1qC4xt8_1_JZC").Offset = 0
App.ActiveDocument.recompute()

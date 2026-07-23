import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00777330")
App.ActiveDocument.addObject("PartDesign::Body","Body_FaGKoCfap9ujTtx_0")
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").Label = "Body_FaGKoCfap9ujTtx_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FaGKoCfap9ujTtx_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaGKoCfap9ujTtx_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FaGKoCfap9ujTtx_0_JGC")
App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaGKoCfap9ujTtx_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC").addGeometry(Part.LineSegment(App.Vector(-88.90000000000001,50.80000000000000,0.00000000000000),App.Vector(88.90000000000001,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC").addGeometry(Part.LineSegment(App.Vector(88.90000000000001,50.80000000000000,0.00000000000000),App.Vector(88.90000000000001,-50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC").addGeometry(Part.LineSegment(App.Vector(-88.90000000000001,-50.80000000000000,0.00000000000000),App.Vector(88.90000000000001,-50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC").addGeometry(Part.LineSegment(App.Vector(-88.90000000000001,50.80000000000000,0.00000000000000),App.Vector(-88.90000000000001,-50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pad","Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC")
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC")
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaGKoCfap9ujTtx_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaGKoCfap9ujTtx_0_FZaljHSCO1SlDEL_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FBip9xGKbS8xyPK_0_JKC")
origin = App.Vector(0.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JKC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FBip9xGKbS8xyPK_0_JKC")
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JKC"), [""])
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC").addGeometry(Part.LineSegment(App.Vector(-36.28390000000000,11.68400000000000,0.00000000000000),App.Vector(-82.25789999999999,11.68400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC").addGeometry(Part.LineSegment(App.Vector(-82.25789999999999,11.68400000000000,0.00000000000000),App.Vector(-82.25789999999999,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC").addGeometry(Part.LineSegment(App.Vector(-36.28390000000000,38.10000000000000,0.00000000000000),App.Vector(-82.25789999999999,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC").addGeometry(Part.LineSegment(App.Vector(-36.28390000000000,11.68400000000000,0.00000000000000),App.Vector(-36.28390000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pocket","Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").Profile = App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").Length = 16.256
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JKC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").Type = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JKC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FBip9xGKbS8xyPK_0_JMC")
origin = App.Vector(0.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JMC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FBip9xGKbS8xyPK_0_JMC")
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JMC"), [""])
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC").addGeometry(Part.LineSegment(App.Vector(22.98700000000000,11.68400000000000,0.00000000000000),App.Vector(-22.98700000000000,11.68400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC").addGeometry(Part.LineSegment(App.Vector(-22.98700000000000,11.68400000000000,0.00000000000000),App.Vector(-22.98700000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC").addGeometry(Part.LineSegment(App.Vector(22.98700000000000,38.10000000000000,0.00000000000000),App.Vector(-22.98700000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC").addGeometry(Part.LineSegment(App.Vector(22.98700000000000,11.68400000000000,0.00000000000000),App.Vector(22.98700000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pocket","Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").Profile = App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").Length = 16.256
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JMC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").Type = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JMC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FBip9xGKbS8xyPK_0_JOC")
origin = App.Vector(-0.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FBip9xGKbS8xyPK_0_JOC")
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JOC"), [""])
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC").addGeometry(Part.LineSegment(App.Vector(82.25789999999999,11.68400000000000,0.00000000000000),App.Vector(36.28390000000000,11.68400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC").addGeometry(Part.LineSegment(App.Vector(36.28390000000000,11.68400000000000,0.00000000000000),App.Vector(36.28390000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC").addGeometry(Part.LineSegment(App.Vector(82.25789999999999,38.10000000000000,0.00000000000000),App.Vector(36.28390000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC").addGeometry(Part.LineSegment(App.Vector(82.25789999999999,11.68400000000000,0.00000000000000),App.Vector(82.25789999999999,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pocket","Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").Length = 16.256
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").Type = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FBip9xGKbS8xyPK_0_JQC")
origin = App.Vector(-0.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JQC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FBip9xGKbS8xyPK_0_JQC")
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JQC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JQC"), [""])
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JQC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JQC").addGeometry(Part.Circle(App.Vector(-59.27090000000000,-7.36600000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JQC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JQC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pocket","Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").Profile = App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JQC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").Length = 16.256
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JQC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").Type = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JQC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FBip9xGKbS8xyPK_0_JSC")
origin = App.Vector(-0.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FBip9xGKbS8xyPK_0_JSC")
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JSC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-7.36600000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pocket","Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JSC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").Length = 16.256
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").Type = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FBip9xGKbS8xyPK_0_JUC")
origin = App.Vector(-0.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JUC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FBip9xGKbS8xyPK_0_JUC")
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JUC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBip9xGKbS8xyPK_0_JUC"), [""])
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JUC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JUC").addGeometry(Part.Circle(App.Vector(59.27090000000000,-7.36600000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.84200000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JUC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JUC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pocket","Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").Profile = App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JUC")
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").Length = 16.256
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBip9xGKbS8xyPK_0_JUC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").Type = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBip9xGKbS8xyPK_0_FiFQ97JeCuwcNmc_1_JUC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FLDD4eJbX07cXDu_0_JWC")
origin = App.Vector(-0.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLDD4eJbX07cXDu_0_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FLDD4eJbX07cXDu_0_JWC")
App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLDD4eJbX07cXDu_0_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JWC").addGeometry(Part.Circle(App.Vector(-59.27090000000000,-32.76600000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pocket","Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC")
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JWC")
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").Length = 10.921999999999999
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").Type = 0
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FLDD4eJbX07cXDu_0_JYC")
origin = App.Vector(-67.06895000000000,-32.76600000000001,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLDD4eJbX07cXDu_0_JYC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FLDD4eJbX07cXDu_0_JYC")
App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JYC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLDD4eJbX07cXDu_0_JYC"), [""])
App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JYC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JYC").addGeometry(Part.Circle(App.Vector(67.06895000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JYC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JYC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pocket","Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC")
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").Profile = App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JYC")
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").Length = 10.921999999999999
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JYC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").Type = 0
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JYC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Plane", "plane_Sketch_FLDD4eJbX07cXDu_0_JaC")
origin = App.Vector(-0.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLDD4eJbX07cXDu_0_JaC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("Sketcher::SketchObject","Sketch_FLDD4eJbX07cXDu_0_JaC")
App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JaC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLDD4eJbX07cXDu_0_JaC"), [""])
App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JaC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JaC").addGeometry(Part.Circle(App.Vector(59.27090000000000,-32.76600000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JaC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JaC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FaGKoCfap9ujTtx_0").newObject("PartDesign::Pocket","Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC")
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").Profile = App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JaC")
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").Length = 10.921999999999999
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLDD4eJbX07cXDu_0_JaC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").Type = 0
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLDD4eJbX07cXDu_0_FYuMqXXqYdqnheK_1_JaC").Offset = 0
App.ActiveDocument.recompute()

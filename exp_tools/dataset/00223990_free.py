import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00223990")
App.ActiveDocument.addObject("PartDesign::Body","Body_FVrb4g1IqgmKBK4_0")
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").Label = "Body_FVrb4g1IqgmKBK4_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Plane", "plane_Sketch_FVrb4g1IqgmKBK4_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVrb4g1IqgmKBK4_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("Sketcher::SketchObject","Sketch_FVrb4g1IqgmKBK4_0_JGC")
App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVrb4g1IqgmKBK4_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC").addGeometry(Part.LineSegment(App.Vector(84.95000000000000,-84.95000000000000,0.00000000000000),App.Vector(-84.95000000000000,-84.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC").addGeometry(Part.LineSegment(App.Vector(-84.95000000000000,-84.95000000000000,0.00000000000000),App.Vector(-84.95000000000000,84.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC").addGeometry(Part.LineSegment(App.Vector(84.95000000000000,84.95000000000000,0.00000000000000),App.Vector(-84.95000000000000,84.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC").addGeometry(Part.LineSegment(App.Vector(84.95000000000000,-84.95000000000000,0.00000000000000),App.Vector(84.95000000000000,84.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Pad","Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC")
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC")
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").Length = 1.7
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVrb4g1IqgmKBK4_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVrb4g1IqgmKBK4_0_FMOF9IiUdUDH2eC_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Plane", "plane_Sketch_FtjEcqc4IMMvknD_1_JJC")
origin = App.Vector(0.00000000000000,-1.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtjEcqc4IMMvknD_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("Sketcher::SketchObject","Sketch_FtjEcqc4IMMvknD_1_JJC")
App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtjEcqc4IMMvknD_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC").addGeometry(Part.LineSegment(App.Vector(-60.95000000000000,84.95000000000000,0.00000000000000),App.Vector(-79.94999999999999,84.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC").addGeometry(Part.LineSegment(App.Vector(-79.94999999999999,84.95000000000000,0.00000000000000),App.Vector(-79.94999999999999,57.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC").addGeometry(Part.LineSegment(App.Vector(-79.94999999999999,57.95000000000000,0.00000000000000),App.Vector(-60.95000000000000,57.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC").addGeometry(Part.LineSegment(App.Vector(-60.95000000000000,84.95000000000000,0.00000000000000),App.Vector(-60.95000000000000,57.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Pad","Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC")
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC")
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").Length = 31.0
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Plane", "plane_Sketch_FtjEcqc4IMMvknD_1_JJG")
origin = App.Vector(0.00000000000000,-1.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtjEcqc4IMMvknD_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("Sketcher::SketchObject","Sketch_FtjEcqc4IMMvknD_1_JJG")
App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtjEcqc4IMMvknD_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG").addGeometry(Part.LineSegment(App.Vector(26.05000000000000,84.95000000000000,0.00000000000000),App.Vector(9.05000000000000,84.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG").addGeometry(Part.LineSegment(App.Vector(9.05000000000000,84.95000000000000,0.00000000000000),App.Vector(9.05000000000000,43.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG").addGeometry(Part.LineSegment(App.Vector(9.05000000000000,43.95000000000000,0.00000000000000),App.Vector(26.05000000000000,43.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG").addGeometry(Part.LineSegment(App.Vector(26.05000000000000,84.95000000000000,0.00000000000000),App.Vector(26.05000000000000,43.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Pad","Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG")
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG")
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").Length = 31.0
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Plane", "plane_Sketch_FtjEcqc4IMMvknD_1_JJK")
origin = App.Vector(0.00000000000000,-1.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtjEcqc4IMMvknD_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("Sketcher::SketchObject","Sketch_FtjEcqc4IMMvknD_1_JJK")
App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtjEcqc4IMMvknD_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK").addGeometry(Part.LineSegment(App.Vector(4.05000000000000,84.95000000000000,0.00000000000000),App.Vector(-12.95000000000000,84.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK").addGeometry(Part.LineSegment(App.Vector(-12.95000000000000,84.95000000000000,0.00000000000000),App.Vector(-12.95000000000000,56.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK").addGeometry(Part.LineSegment(App.Vector(-12.95000000000000,56.95000000000000,0.00000000000000),App.Vector(4.05000000000000,56.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK").addGeometry(Part.LineSegment(App.Vector(4.05000000000000,84.95000000000000,0.00000000000000),App.Vector(4.05000000000000,56.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Pad","Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK")
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK")
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").Length = 31.0
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtjEcqc4IMMvknD_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtjEcqc4IMMvknD_1_FdaraTBW0cn93gE_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Plane", "plane_Sketch_Fo2PwseZ8871rBg_1_JNC")
origin = App.Vector(0.00000000000000,-1.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fo2PwseZ8871rBg_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("Sketcher::SketchObject","Sketch_Fo2PwseZ8871rBg_1_JNC")
App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fo2PwseZ8871rBg_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC").addGeometry(Part.LineSegment(App.Vector(-84.95000000000000,-74.95000000000000,0.00000000000000),App.Vector(-74.95000000000000,-74.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC").addGeometry(Part.LineSegment(App.Vector(-74.95000000000000,-74.95000000000000,0.00000000000000),App.Vector(-74.95000000000000,-12.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC").addGeometry(Part.LineSegment(App.Vector(-84.95000000000000,-12.95000000000000,0.00000000000000),App.Vector(-74.95000000000000,-12.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC").addGeometry(Part.LineSegment(App.Vector(-84.95000000000000,-74.95000000000000,0.00000000000000),App.Vector(-84.95000000000000,-12.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Pad","Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC")
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC")
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").Length = 35.0
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fo2PwseZ8871rBg_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fo2PwseZ8871rBg_1_F1t1qrTWN5a92vA_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Plane", "plane_Sketch_FwRmIjJfBQg3U3i_1_JRC")
origin = App.Vector(0.00000000000000,-1.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwRmIjJfBQg3U3i_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("Sketcher::SketchObject","Sketch_FwRmIjJfBQg3U3i_1_JRC")
App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwRmIjJfBQg3U3i_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC").addGeometry(Part.LineSegment(App.Vector(-59.95000000000000,62.05000000000000,0.00000000000000),App.Vector(-57.95000000000000,62.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC").addGeometry(Part.LineSegment(App.Vector(-57.95000000000000,62.05000000000000,0.00000000000000),App.Vector(-57.95000000000000,-79.94999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC").addGeometry(Part.LineSegment(App.Vector(-59.95000000000000,-79.94999999999999,0.00000000000000),App.Vector(-57.95000000000000,-79.94999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC").addGeometry(Part.LineSegment(App.Vector(-59.95000000000000,62.05000000000000,0.00000000000000),App.Vector(-59.95000000000000,-79.94999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Pad","Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC")
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC")
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").Length = 34.0
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwRmIjJfBQg3U3i_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwRmIjJfBQg3U3i_1_FYbJzRO5cfL7XR1_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Plane", "plane_Sketch_FLO3m9owqZjnkbG_1_JVC")
origin = App.Vector(0.00000000000000,-1.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLO3m9owqZjnkbG_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("Sketcher::SketchObject","Sketch_FLO3m9owqZjnkbG_1_JVC")
App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLO3m9owqZjnkbG_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,16.05000000000000,0.00000000000000),App.Vector(40.95000000000000,16.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC").addGeometry(Part.LineSegment(App.Vector(40.95000000000000,16.05000000000000,0.00000000000000),App.Vector(40.95000000000000,-43.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,-43.95000000000000,0.00000000000000),App.Vector(40.95000000000000,-43.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,16.05000000000000,0.00000000000000),App.Vector(-19.05000000000000,-43.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Pad","Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC")
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC")
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLO3m9owqZjnkbG_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLO3m9owqZjnkbG_1_FXVHe7BjS6U3sxn_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Plane", "plane_Sketch_FuE3cE4TsiXOezq_1_JZC")
origin = App.Vector(0.00000000000000,-1.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuE3cE4TsiXOezq_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("Sketcher::SketchObject","Sketch_FuE3cE4TsiXOezq_1_JZC")
App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuE3cE4TsiXOezq_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC").addGeometry(Part.LineSegment(App.Vector(-37.95000000000000,81.94999999999999,0.00000000000000),App.Vector(-21.95000000000000,81.94999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC").addGeometry(Part.LineSegment(App.Vector(-21.95000000000000,81.94999999999999,0.00000000000000),App.Vector(-21.95000000000000,65.94999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC").addGeometry(Part.LineSegment(App.Vector(-37.95000000000000,65.94999999999999,0.00000000000000),App.Vector(-21.95000000000000,65.94999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC").addGeometry(Part.LineSegment(App.Vector(-37.95000000000000,81.94999999999999,0.00000000000000),App.Vector(-37.95000000000000,65.94999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVrb4g1IqgmKBK4_0").newObject("PartDesign::Pad","Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC")
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC")
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").Length = 1.3000000000000003
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuE3cE4TsiXOezq_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuE3cE4TsiXOezq_1_FzfNg0eiUf3vCQB_1_JZC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00204157")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fa5D738Nqu0phTo_0")
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").Label = "Body_Fa5D738Nqu0phTo_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Plane", "plane_Sketch_Fa5D738Nqu0phTo_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa5D738Nqu0phTo_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("Sketcher::SketchObject","Sketch_Fa5D738Nqu0phTo_0_JGC")
App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa5D738Nqu0phTo_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2438.40000000000009,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC").addGeometry(Part.LineSegment(App.Vector(2438.40000000000009,0.00000000000000,0.00000000000000),App.Vector(2438.40000000000009,1219.20000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,1219.20000000000005,0.00000000000000),App.Vector(2438.40000000000009,1219.20000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1219.20000000000005,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Pad","Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC")
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC")
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").Length = 60.96000000000001
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa5D738Nqu0phTo_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa5D738Nqu0phTo_0_FDE5Er6aj7IbDo0_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Plane", "plane_Sketch_Fx2No9zwwnNygxh_1_JLC")
origin = App.Vector(1219.20000000000005,-60.96000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("Sketcher::SketchObject","Sketch_Fx2No9zwwnNygxh_1_JLC")
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC").addGeometry(Part.LineSegment(App.Vector(-1219.20000000000005,-609.60000000000002,0.00000000000000),App.Vector(-1118.61599999999999,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC").addGeometry(Part.LineSegment(App.Vector(-1118.61599999999999,-609.60000000000002,0.00000000000000),App.Vector(-1118.61599999999999,-509.01600000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC").addGeometry(Part.LineSegment(App.Vector(-1219.20000000000005,-509.01600000000002,0.00000000000000),App.Vector(-1118.61599999999999,-509.01600000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC").addGeometry(Part.LineSegment(App.Vector(-1219.20000000000005,-609.60000000000002,0.00000000000000),App.Vector(-1219.20000000000005,-509.01600000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Pad","Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Plane", "plane_Sketch_Fx2No9zwwnNygxh_1_JLG")
origin = App.Vector(1219.20000000000005,-60.96000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("Sketcher::SketchObject","Sketch_Fx2No9zwwnNygxh_1_JLG")
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG").addGeometry(Part.LineSegment(App.Vector(-1219.20000000000005,607.99736999999993,0.00000000000000),App.Vector(-1118.61599999999999,607.99736999999993,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG").addGeometry(Part.LineSegment(App.Vector(-1118.61599999999999,607.99736999999993,0.00000000000000),App.Vector(-1118.61599999999999,507.41336999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG").addGeometry(Part.LineSegment(App.Vector(-1219.20000000000005,507.41336999999999,0.00000000000000),App.Vector(-1118.61599999999999,507.41336999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG").addGeometry(Part.LineSegment(App.Vector(-1219.20000000000005,607.99736999999993,0.00000000000000),App.Vector(-1219.20000000000005,507.41336999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Pad","Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Plane", "plane_Sketch_Fx2No9zwwnNygxh_1_JLK")
origin = App.Vector(1219.20000000000005,-60.96000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("Sketcher::SketchObject","Sketch_Fx2No9zwwnNygxh_1_JLK")
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK").addGeometry(Part.LineSegment(App.Vector(1118.59743000000003,609.62433000000010,0.00000000000000),App.Vector(1219.18143000000009,609.62433000000010,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK").addGeometry(Part.LineSegment(App.Vector(1219.18143000000009,609.62433000000010,0.00000000000000),App.Vector(1219.18143000000009,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK").addGeometry(Part.LineSegment(App.Vector(1118.59743000000003,609.60000000000002,0.00000000000000),App.Vector(1219.18143000000009,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK").addGeometry(Part.LineSegment(App.Vector(1118.59743000000003,609.62433000000010,0.00000000000000),App.Vector(1118.59743000000003,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Pad","Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Plane", "plane_Sketch_Fx2No9zwwnNygxh_1_JLO")
origin = App.Vector(1219.20000000000005,-60.96000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("Sketcher::SketchObject","Sketch_Fx2No9zwwnNygxh_1_JLO")
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO").addGeometry(Part.LineSegment(App.Vector(1118.59743000000003,509.04033000000004,0.00000000000000),App.Vector(1219.18143000000009,509.04033000000004,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO").addGeometry(Part.LineSegment(App.Vector(1219.18143000000009,509.04033000000004,0.00000000000000),App.Vector(1219.18143000000009,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO").addGeometry(Part.LineSegment(App.Vector(1118.59743000000003,609.60000000000002,0.00000000000000),App.Vector(1219.18143000000009,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO").addGeometry(Part.LineSegment(App.Vector(1118.59743000000003,509.04033000000004,0.00000000000000),App.Vector(1118.59743000000003,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Pad","Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Plane", "plane_Sketch_Fx2No9zwwnNygxh_1_JLS")
origin = App.Vector(1219.20000000000005,-60.96000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("Sketcher::SketchObject","Sketch_Fx2No9zwwnNygxh_1_JLS")
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLS"), [""])
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").addGeometry(Part.LineSegment(App.Vector(1219.28894999999989,-509.09262000000001,0.00000000000000),App.Vector(1219.20000000000005,-509.09262000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").addGeometry(Part.LineSegment(App.Vector(1219.20000000000005,-609.60000000000002,0.00000000000000),App.Vector(1219.20000000000005,-509.09262000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").addGeometry(Part.LineSegment(App.Vector(1219.20000000000005,-609.60000000000002,0.00000000000000),App.Vector(1118.70494999999983,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").addGeometry(Part.LineSegment(App.Vector(1118.70494999999983,-609.67661999999996,0.00000000000000),App.Vector(1118.70494999999983,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").addGeometry(Part.LineSegment(App.Vector(1118.70494999999983,-609.67661999999996,0.00000000000000),App.Vector(1219.28894999999989,-609.67661999999996,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").addGeometry(Part.LineSegment(App.Vector(1219.28894999999989,-509.09262000000001,0.00000000000000),App.Vector(1219.28894999999989,-609.67661999999996,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Pad","Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").Profile = App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").Type = 4
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Plane", "plane_Sketch_Fx2No9zwwnNygxh_1_JLW")
origin = App.Vector(1219.20000000000005,-60.96000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("Sketcher::SketchObject","Sketch_Fx2No9zwwnNygxh_1_JLW")
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx2No9zwwnNygxh_1_JLW"), [""])
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW").addGeometry(Part.LineSegment(App.Vector(1118.70494999999983,-509.09262000000001,0.00000000000000),App.Vector(1219.20000000000005,-509.09262000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW").addGeometry(Part.LineSegment(App.Vector(1219.20000000000005,-609.60000000000002,0.00000000000000),App.Vector(1219.20000000000005,-509.09262000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW").addGeometry(Part.LineSegment(App.Vector(1219.20000000000005,-609.60000000000002,0.00000000000000),App.Vector(1118.70494999999983,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW").addGeometry(Part.LineSegment(App.Vector(1118.70494999999983,-509.09262000000001,0.00000000000000),App.Vector(1118.70494999999983,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Pad","Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").Profile = App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW")
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx2No9zwwnNygxh_1_JLW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").Type = 4
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx2No9zwwnNygxh_1_FKhej6jFa59W6HF_1_JLW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Plane", "plane_Sketch_FOpvX4apQvq8Q45_1_JPC")
origin = App.Vector(291.56066000000004,0.00000000000000,609.60000000000002)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOpvX4apQvq8Q45_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("Sketcher::SketchObject","Sketch_FOpvX4apQvq8Q45_1_JPC")
App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOpvX4apQvq8Q45_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC").addGeometry(Part.LineSegment(App.Vector(-291.56064999999995,-609.60000000000002,0.00000000000000),App.Vector(-1510.76064999999994,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC").addGeometry(Part.LineSegment(App.Vector(-1510.76064999999994,-609.60000000000002,0.00000000000000),App.Vector(-1510.76064999999994,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC").addGeometry(Part.LineSegment(App.Vector(-291.56064999999995,609.60000000000002,0.00000000000000),App.Vector(-1510.76064999999994,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC").addGeometry(Part.LineSegment(App.Vector(-291.56064999999995,-609.60000000000002,0.00000000000000),App.Vector(-291.56064999999995,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Pad","Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC")
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC")
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").Length = 1219.2
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOpvX4apQvq8Q45_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOpvX4apQvq8Q45_1_FRS2KTloT2TU07F_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Plane", "plane_Sketch_FYslAFjRII30uNP_1_JTC")
origin = App.Vector(1219.20000000000005,121.92000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYslAFjRII30uNP_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("Sketcher::SketchObject","Sketch_FYslAFjRII30uNP_1_JTC")
App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYslAFjRII30uNP_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC").addGeometry(Part.LineSegment(App.Vector(573.67565000000002,-1086.71067999999991,0.00000000000000),App.Vector(-625.83952000000011,-1086.71067999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC").addGeometry(Part.LineSegment(App.Vector(-625.83952000000011,-1086.71067999999991,0.00000000000000),App.Vector(-625.83952000000011,107.56209999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC").addGeometry(Part.LineSegment(App.Vector(573.67565000000002,107.56209999999999,0.00000000000000),App.Vector(-625.83952000000011,107.56209999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC").addGeometry(Part.LineSegment(App.Vector(573.67565000000002,-1086.71067999999991,0.00000000000000),App.Vector(573.67565000000002,107.56209999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa5D738Nqu0phTo_0").newObject("PartDesign::Pocket","Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC")
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC")
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").Length = 1188.72
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYslAFjRII30uNP_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYslAFjRII30uNP_1_FEp9DOWQUOPBpYS_1_JTC").Offset = 0
App.ActiveDocument.recompute()

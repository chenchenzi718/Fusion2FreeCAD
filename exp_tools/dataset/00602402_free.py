import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00602402")
App.ActiveDocument.addObject("PartDesign::Body","Body_FngKb6Mxoa5iB8V_0")
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").Label = "Body_FngKb6Mxoa5iB8V_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Plane", "plane_Sketch_FngKb6Mxoa5iB8V_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FngKb6Mxoa5iB8V_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("Sketcher::SketchObject","Sketch_FngKb6Mxoa5iB8V_0_JGC")
App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FngKb6Mxoa5iB8V_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(914.39999999999998,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC").addGeometry(Part.LineSegment(App.Vector(914.39999999999998,0.00000000000000,0.00000000000000),App.Vector(914.39999999999998,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-609.60000000000002,0.00000000000000),App.Vector(914.39999999999998,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Pad","Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC")
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC")
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FngKb6Mxoa5iB8V_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FngKb6Mxoa5iB8V_0_FGSIoHum4C9BZCu_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Plane", "plane_Sketch_Fu2ASXUPWem0HNO_1_JJC")
origin = App.Vector(457.19999999999999,-609.60000000000002,457.19999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu2ASXUPWem0HNO_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("Sketcher::SketchObject","Sketch_Fu2ASXUPWem0HNO_1_JJC")
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu2ASXUPWem0HNO_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC").addGeometry(Part.LineSegment(App.Vector(-420.99293999999998,419.36005999999998,0.00000000000000),App.Vector(417.20706000000001,419.36005999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC").addGeometry(Part.LineSegment(App.Vector(417.20706000000001,419.36005999999998,0.00000000000000),App.Vector(417.20706000000001,268.74597000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC").addGeometry(Part.LineSegment(App.Vector(-420.99293999999998,268.74597000000006,0.00000000000000),App.Vector(417.20706000000001,268.74597000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC").addGeometry(Part.LineSegment(App.Vector(-420.99293999999998,419.36005999999998,0.00000000000000),App.Vector(-420.99293999999998,268.74597000000006,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Pad","Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC")
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC")
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").Length = 16.764000000000003
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Plane", "plane_Sketch_Fu2ASXUPWem0HNO_1_JJG")
origin = App.Vector(457.19999999999999,-609.60000000000002,457.19999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu2ASXUPWem0HNO_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("Sketcher::SketchObject","Sketch_Fu2ASXUPWem0HNO_1_JJG")
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu2ASXUPWem0HNO_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG").addGeometry(Part.LineSegment(App.Vector(-420.99293999999998,233.82096999999996,0.00000000000000),App.Vector(417.20706000000001,233.82096999999996,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG").addGeometry(Part.LineSegment(App.Vector(417.20706000000001,233.82096999999996,0.00000000000000),App.Vector(417.20706000000001,72.29287000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG").addGeometry(Part.LineSegment(App.Vector(-420.99293999999998,72.29287000000001,0.00000000000000),App.Vector(417.20706000000001,72.29287000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG").addGeometry(Part.LineSegment(App.Vector(-420.99293999999998,233.82096999999996,0.00000000000000),App.Vector(-420.99293999999998,72.29287000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Pad","Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG")
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG")
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").Length = 16.764000000000003
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Plane", "plane_Sketch_Fu2ASXUPWem0HNO_1_JJK")
origin = App.Vector(457.19999999999999,-609.60000000000002,457.19999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu2ASXUPWem0HNO_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("Sketcher::SketchObject","Sketch_Fu2ASXUPWem0HNO_1_JJK")
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu2ASXUPWem0HNO_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK").addGeometry(Part.LineSegment(App.Vector(-420.99293999999998,27.44599000000003,0.00000000000000),App.Vector(-24.75294000000000,27.44599000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK").addGeometry(Part.LineSegment(App.Vector(-24.75294000000000,27.44599000000003,0.00000000000000),App.Vector(-24.75294000000000,-429.75400999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK").addGeometry(Part.LineSegment(App.Vector(-420.99293999999998,-429.75400999999999,0.00000000000000),App.Vector(-24.75294000000000,-429.75400999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK").addGeometry(Part.LineSegment(App.Vector(-420.99293999999998,27.44599000000003,0.00000000000000),App.Vector(-420.99293999999998,-429.75400999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Pad","Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK")
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK")
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").Length = 16.764000000000003
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Plane", "plane_Sketch_Fu2ASXUPWem0HNO_1_JJO")
origin = App.Vector(457.19999999999999,-609.60000000000002,457.19999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu2ASXUPWem0HNO_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("Sketcher::SketchObject","Sketch_Fu2ASXUPWem0HNO_1_JJO")
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu2ASXUPWem0HNO_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO").addGeometry(Part.LineSegment(App.Vector(22.11800000000003,27.44599000000003,0.00000000000000),App.Vector(418.35799999999995,27.44599000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO").addGeometry(Part.LineSegment(App.Vector(418.35799999999995,27.44599000000003,0.00000000000000),App.Vector(418.35799999999995,-429.75400999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO").addGeometry(Part.LineSegment(App.Vector(22.11800000000003,-429.75400999999999,0.00000000000000),App.Vector(418.35799999999995,-429.75400999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO").addGeometry(Part.LineSegment(App.Vector(22.11800000000003,27.44599000000003,0.00000000000000),App.Vector(22.11800000000003,-429.75400999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Pad","Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO")
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO")
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").Length = 16.764000000000003
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu2ASXUPWem0HNO_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu2ASXUPWem0HNO_1_F2JW4Sn8ZmvprIp_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Plane", "plane_Sketch_F71UZ59KWwVlBZQ_1_JNC")
origin = App.Vector(457.19999999999999,-609.60000000000002,457.19999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F71UZ59KWwVlBZQ_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("Sketcher::SketchObject","Sketch_F71UZ59KWwVlBZQ_1_JNC")
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F71UZ59KWwVlBZQ_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-245.80536000000001,389.15976999999998,0.00000000000000),App.Vector(226.63464000000005,389.15976999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC").addGeometry(Part.LineSegment(App.Vector(226.63464000000005,389.15976999999998,0.00000000000000),App.Vector(226.63464000000005,371.58065999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-245.80536000000001,371.58065999999997,0.00000000000000),App.Vector(226.63464000000005,371.58065999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-245.80536000000001,389.15976999999998,0.00000000000000),App.Vector(-245.80536000000001,371.58065999999997,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Pad","Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC")
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC")
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").Length = 27.432000000000002
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Plane", "plane_Sketch_F71UZ59KWwVlBZQ_1_JNG")
origin = App.Vector(457.19999999999999,-609.60000000000002,457.19999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F71UZ59KWwVlBZQ_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("Sketcher::SketchObject","Sketch_F71UZ59KWwVlBZQ_1_JNG")
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F71UZ59KWwVlBZQ_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG").addGeometry(Part.LineSegment(App.Vector(-245.80536000000001,213.36817000000002,0.00000000000000),App.Vector(226.63464000000005,213.36817000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG").addGeometry(Part.LineSegment(App.Vector(226.63464000000005,213.36817000000002,0.00000000000000),App.Vector(226.63464000000005,197.98637999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG").addGeometry(Part.LineSegment(App.Vector(-245.80536000000001,197.98637999999997,0.00000000000000),App.Vector(226.63464000000005,197.98637999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG").addGeometry(Part.LineSegment(App.Vector(-245.80536000000001,213.36817000000002,0.00000000000000),App.Vector(-245.80536000000001,197.98637999999997,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Pad","Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG")
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG")
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").Length = 27.432000000000002
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Plane", "plane_Sketch_F71UZ59KWwVlBZQ_1_JNK")
origin = App.Vector(457.19999999999999,-609.60000000000002,457.19999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F71UZ59KWwVlBZQ_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("Sketcher::SketchObject","Sketch_F71UZ59KWwVlBZQ_1_JNK")
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F71UZ59KWwVlBZQ_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK").addGeometry(Part.LineSegment(App.Vector(-56.82935000000000,-91.71538000000001,0.00000000000000),App.Vector(-78.80332000000001,-91.71538000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK").addGeometry(Part.LineSegment(App.Vector(-78.80332000000001,-91.71538000000001,0.00000000000000),App.Vector(-78.80332000000001,-289.83537999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK").addGeometry(Part.LineSegment(App.Vector(-56.82935000000000,-289.83537999999999,0.00000000000000),App.Vector(-78.80332000000001,-289.83537999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK").addGeometry(Part.LineSegment(App.Vector(-56.82935000000000,-91.71538000000001,0.00000000000000),App.Vector(-56.82935000000000,-289.83537999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Pad","Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK")
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK")
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").Length = 27.432000000000002
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Plane", "plane_Sketch_F71UZ59KWwVlBZQ_1_JNO")
origin = App.Vector(457.19999999999999,-609.60000000000002,457.19999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F71UZ59KWwVlBZQ_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("Sketcher::SketchObject","Sketch_F71UZ59KWwVlBZQ_1_JNO")
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F71UZ59KWwVlBZQ_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO").addGeometry(Part.LineSegment(App.Vector(39.85602999999999,-91.71538000000001,0.00000000000000),App.Vector(61.82996999999995,-91.71538000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO").addGeometry(Part.LineSegment(App.Vector(61.82996999999995,-91.71538000000001,0.00000000000000),App.Vector(61.82996999999995,-289.83537999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO").addGeometry(Part.LineSegment(App.Vector(39.85602999999999,-289.83537999999999,0.00000000000000),App.Vector(61.82996999999995,-289.83537999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO").addGeometry(Part.LineSegment(App.Vector(39.85602999999999,-91.71538000000001,0.00000000000000),App.Vector(39.85602999999999,-289.83537999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FngKb6Mxoa5iB8V_0").newObject("PartDesign::Pad","Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO")
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO")
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").Length = 27.432000000000002
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F71UZ59KWwVlBZQ_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F71UZ59KWwVlBZQ_1_F1qQWTOMBaNx4u2_1_JNO").Offset = 0
App.ActiveDocument.recompute()

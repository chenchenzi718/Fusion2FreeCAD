import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00821616")
App.ActiveDocument.addObject("PartDesign::Body","Body_FT0BFI3wuQUXGXW_0")
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").Label = "Body_FT0BFI3wuQUXGXW_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Plane", "plane_Sketch_FT0BFI3wuQUXGXW_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FT0BFI3wuQUXGXW_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("Sketcher::SketchObject","Sketch_FT0BFI3wuQUXGXW_0_JGC")
App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FT0BFI3wuQUXGXW_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(406.39999999999998,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC").addGeometry(Part.LineSegment(App.Vector(406.39999999999998,0.00000000000000,0.00000000000000),App.Vector(406.39999999999998,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,609.60000000000002,0.00000000000000),App.Vector(406.39999999999998,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Pad","Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC")
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC")
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").Length = 609.6
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FT0BFI3wuQUXGXW_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FT0BFI3wuQUXGXW_0_FLKSggyVGHgxzzv_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Plane", "plane_Sketch_FBWGk5k2OsMiRTS_1_JNC")
origin = App.Vector(76.20000000000000,48.74384999999999,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBWGk5k2OsMiRTS_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("Sketcher::SketchObject","Sketch_FBWGk5k2OsMiRTS_1_JNC")
App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBWGk5k2OsMiRTS_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,-709.14385000000004,0.00000000000000),App.Vector(308.91230000000002,-709.14385000000004,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC").addGeometry(Part.LineSegment(App.Vector(308.91230000000002,-27.45615000000000,0.00000000000000),App.Vector(308.91230000000002,-709.14385000000004,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC").addGeometry(Part.LineSegment(App.Vector(308.91230000000002,-27.45615000000000,0.00000000000000),App.Vector(105.71230000000000,-27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,-709.14385000000004,0.00000000000000),App.Vector(105.71230000000000,-27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Pad","Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC")
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC")
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").Length = 152.4
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Plane", "plane_Sketch_FBWGk5k2OsMiRTS_1_JNG")
origin = App.Vector(76.20000000000000,48.74384999999999,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBWGk5k2OsMiRTS_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("Sketcher::SketchObject","Sketch_FBWGk5k2OsMiRTS_1_JNG")
App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBWGk5k2OsMiRTS_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,1221.25615000000016,0.00000000000000),App.Vector(308.91230000000002,1221.25615000000016,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG").addGeometry(Part.LineSegment(App.Vector(308.91230000000002,539.56844999999998,0.00000000000000),App.Vector(308.91230000000002,1221.25615000000016,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG").addGeometry(Part.LineSegment(App.Vector(308.91230000000002,539.56844999999998,0.00000000000000),App.Vector(105.71230000000000,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,1221.25615000000016,0.00000000000000),App.Vector(105.71230000000000,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Pad","Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG")
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG")
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").Length = 152.4
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Plane", "plane_Sketch_FBWGk5k2OsMiRTS_1_JNO")
origin = App.Vector(76.20000000000000,48.74384999999999,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBWGk5k2OsMiRTS_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("Sketcher::SketchObject","Sketch_FBWGk5k2OsMiRTS_1_JNO")
App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBWGk5k2OsMiRTS_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,-27.45615000000000,0.00000000000000),App.Vector(105.71230000000000,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO").addGeometry(Part.LineSegment(App.Vector(308.91230000000002,539.56844999999998,0.00000000000000),App.Vector(105.71230000000000,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO").addGeometry(Part.LineSegment(App.Vector(308.91230000000002,-27.45615000000000,0.00000000000000),App.Vector(308.91230000000002,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO").addGeometry(Part.LineSegment(App.Vector(308.91230000000002,-27.45615000000000,0.00000000000000),App.Vector(105.71230000000000,-27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Pad","Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO")
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO")
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").Length = 152.4
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBWGk5k2OsMiRTS_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBWGk5k2OsMiRTS_1_Fp4kAfUODAXRG7D_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Plane", "plane_Sketch_FiPDoKyRzWBz7PM_1_JSC")
origin = App.Vector(76.20000000000000,48.74384999999999,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiPDoKyRzWBz7PM_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("Sketcher::SketchObject","Sketch_FiPDoKyRzWBz7PM_1_JSC")
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiPDoKyRzWBz7PM_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,713.25614999999993,0.00000000000000),App.Vector(54.91229999999998,713.25614999999993,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC").addGeometry(Part.LineSegment(App.Vector(54.91229999999998,713.25614999999993,0.00000000000000),App.Vector(54.91229999999998,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,539.56844999999998,0.00000000000000),App.Vector(54.91229999999998,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,539.56844999999998,0.00000000000000),App.Vector(105.71230000000000,713.25614999999993,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Pad","Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC")
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC")
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").Length = 304.8
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").Type = 4
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Plane", "plane_Sketch_FiPDoKyRzWBz7PM_1_JSG")
origin = App.Vector(76.20000000000000,48.74384999999999,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiPDoKyRzWBz7PM_1_JSG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("Sketcher::SketchObject","Sketch_FiPDoKyRzWBz7PM_1_JSG")
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiPDoKyRzWBz7PM_1_JSG"), [""])
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG").addGeometry(Part.LineSegment(App.Vector(-199.08770000000001,484.65615000000003,0.00000000000000),App.Vector(-54.91230000000000,484.65615000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG").addGeometry(Part.LineSegment(App.Vector(-54.91230000000000,484.65615000000003,0.00000000000000),App.Vector(-54.91230000000000,27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG").addGeometry(Part.LineSegment(App.Vector(-199.08770000000001,27.45615000000000,0.00000000000000),App.Vector(-54.91230000000000,27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG").addGeometry(Part.LineSegment(App.Vector(-199.08770000000001,484.65615000000003,0.00000000000000),App.Vector(-199.08770000000001,27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Pad","Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG")
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").Profile = App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG")
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").Length = 304.8
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").Type = 4
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Plane", "plane_Sketch_FiPDoKyRzWBz7PM_1_JSK")
origin = App.Vector(76.20000000000000,48.74384999999999,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiPDoKyRzWBz7PM_1_JSK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("Sketcher::SketchObject","Sketch_FiPDoKyRzWBz7PM_1_JSK")
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiPDoKyRzWBz7PM_1_JSK"), [""])
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK").addGeometry(Part.LineSegment(App.Vector(54.91229999999998,-201.14385000000001,0.00000000000000),App.Vector(54.91229999999998,-27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,-27.45615000000000,0.00000000000000),App.Vector(54.91229999999998,-27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,-27.45615000000000,0.00000000000000),App.Vector(105.71230000000000,-201.14385000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK").addGeometry(Part.LineSegment(App.Vector(54.91229999999998,-201.14385000000001,0.00000000000000),App.Vector(105.71230000000000,-201.14385000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Pad","Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK")
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").Profile = App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK")
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").Length = 304.8
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").Type = 4
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Plane", "plane_Sketch_FiPDoKyRzWBz7PM_1_JSW")
origin = App.Vector(76.20000000000000,48.74384999999999,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiPDoKyRzWBz7PM_1_JSW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("Sketcher::SketchObject","Sketch_FiPDoKyRzWBz7PM_1_JSW")
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiPDoKyRzWBz7PM_1_JSW"), [""])
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").addGeometry(Part.LineSegment(App.Vector(54.91229999999998,484.65615000000003,0.00000000000000),App.Vector(54.91229999999998,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,539.56844999999998,0.00000000000000),App.Vector(54.91229999999998,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,-27.45615000000000,0.00000000000000),App.Vector(105.71230000000000,539.56844999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").addGeometry(Part.LineSegment(App.Vector(105.71230000000000,-27.45615000000000,0.00000000000000),App.Vector(54.91229999999998,-27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").addGeometry(Part.LineSegment(App.Vector(54.91229999999998,27.45615000000000,0.00000000000000),App.Vector(54.91229999999998,-27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").addGeometry(Part.LineSegment(App.Vector(54.91229999999998,27.45615000000000,0.00000000000000),App.Vector(-54.91230000000000,27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").addGeometry(Part.LineSegment(App.Vector(-54.91230000000000,484.65615000000003,0.00000000000000),App.Vector(-54.91230000000000,27.45615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").addGeometry(Part.LineSegment(App.Vector(54.91229999999998,484.65615000000003,0.00000000000000),App.Vector(-54.91230000000000,484.65615000000003,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT0BFI3wuQUXGXW_0").newObject("PartDesign::Pad","Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW")
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").Profile = App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW")
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").Length = 304.8
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiPDoKyRzWBz7PM_1_JSW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").Type = 4
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiPDoKyRzWBz7PM_1_FRoARfS7QDkMQrN_1_JSW").Offset = 0
App.ActiveDocument.recompute()

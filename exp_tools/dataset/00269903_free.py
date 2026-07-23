import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00269903")
App.ActiveDocument.addObject("PartDesign::Body","Body_F56NoDBKRr0Xu81_0")
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").Label = "Body_F56NoDBKRr0Xu81_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F56NoDBKRr0Xu81_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F56NoDBKRr0Xu81_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F56NoDBKRr0Xu81_0_JGC")
App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F56NoDBKRr0Xu81_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC").addGeometry(Part.LineSegment(App.Vector(50.95000000000000,-63.11716000000001,0.00000000000000),App.Vector(-50.95000000000000,-63.11716000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.95000000000000,-63.11716000000001,0.00000000000000),App.Vector(-50.95000000000000,63.11716000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC").addGeometry(Part.LineSegment(App.Vector(50.95000000000000,63.11716000000001,0.00000000000000),App.Vector(-50.95000000000000,63.11716000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC").addGeometry(Part.LineSegment(App.Vector(50.95000000000000,-63.11716000000001,0.00000000000000),App.Vector(50.95000000000000,63.11716000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pad","Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC")
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC")
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").Length = 12.480000000000002
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F56NoDBKRr0Xu81_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F56NoDBKRr0Xu81_0_FVSo5Qt0pYY2AiC_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F22SnjAkznxAXOb_0_JIC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F22SnjAkznxAXOb_0_JIC")
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIC"), [""])
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIC").addGeometry(Part.Circle(App.Vector(0.00000000000000,22.66817000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pocket","Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").Profile = App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIC")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").Length = 12.78
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").Type = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F22SnjAkznxAXOb_0_JIG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F22SnjAkznxAXOb_0_JIG")
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIG"), [""])
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIG").addGeometry(Part.Circle(App.Vector(0.00000000000000,40.66817000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pocket","Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").Profile = App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIG")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").Length = 12.78
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").Type = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").Reversed = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F22SnjAkznxAXOb_0_JIK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F22SnjAkznxAXOb_0_JIK")
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIK"), [""])
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIK").addGeometry(Part.Circle(App.Vector(0.00000000000000,4.66817000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pocket","Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").Profile = App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIK")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").Length = 12.78
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").Type = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").Reversed = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F22SnjAkznxAXOb_0_JIO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F22SnjAkznxAXOb_0_JIO")
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIO"), [""])
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIO").addGeometry(Part.Circle(App.Vector(-28.67200000000000,47.39296000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pocket","Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").Profile = App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIO")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").Length = 12.78
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").Type = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").Reversed = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F22SnjAkznxAXOb_0_JIS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F22SnjAkznxAXOb_0_JIS")
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIS"), [""])
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIS").addGeometry(Part.Circle(App.Vector(-28.67200000000000,-12.60704000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pocket","Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").Profile = App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIS")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").Length = 12.78
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").Type = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").Reversed = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F22SnjAkznxAXOb_0_JIW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F22SnjAkznxAXOb_0_JIW")
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIW"), [""])
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIW").addGeometry(Part.Circle(App.Vector(28.67174000000000,47.39458000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pocket","Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").Profile = App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIW")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").Length = 12.78
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").Type = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").Reversed = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F22SnjAkznxAXOb_0_JIa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F22SnjAkznxAXOb_0_JIa")
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIa"), [""])
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIa").addGeometry(Part.Circle(App.Vector(28.67174000000000,-12.60542000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pocket","Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").Profile = App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIa")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").Length = 12.78
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").Type = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").Reversed = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F22SnjAkznxAXOb_0_JIe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F22SnjAkznxAXOb_0_JIe")
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIe"), [""])
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-28.67200000000000,47.39296000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.50000000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe").addGeometry(Part.LineSegment(App.Vector(-21.17200000000000,47.39296000000000,0.00000000000000),App.Vector(-21.17200000000000,-12.60704000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-28.67200000000000,-12.60704000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.50000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe").addGeometry(Part.LineSegment(App.Vector(-36.17200000000000,47.39296000000000,0.00000000000000),App.Vector(-36.17200000000000,-12.60704000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pocket","Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").Profile = App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").Length = 12.78
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").Type = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").UpToFace = None
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").Reversed = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").Midplane = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Plane", "plane_Sketch_F22SnjAkznxAXOb_0_JIi")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("Sketcher::SketchObject","Sketch_F22SnjAkznxAXOb_0_JIi")
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F22SnjAkznxAXOb_0_JIi"), [""])
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(28.67174000000000,47.39458000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.50000000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi").addGeometry(Part.LineSegment(App.Vector(21.17174000000000,-12.60542000000000,0.00000000000000),App.Vector(21.17174000000000,47.39458000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(28.67174000000000,-12.60542000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.50000000000000),0.00021733332991,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi").addGeometry(Part.LineSegment(App.Vector(36.17174000000000,47.39458000000000,0.00000000000000),App.Vector(36.17174000000000,-12.60379000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56NoDBKRr0Xu81_0").newObject("PartDesign::Pocket","Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").Profile = App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi")
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").Length = 12.78
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F22SnjAkznxAXOb_0_JIi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").Type = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").UpToFace = None
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").Reversed = 1
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").Midplane = 0
App.ActiveDocument.getObject("Extrude_F22SnjAkznxAXOb_0_Fn3e7bdSdg0LBw4_0_JIi").Offset = 0
App.ActiveDocument.recompute()

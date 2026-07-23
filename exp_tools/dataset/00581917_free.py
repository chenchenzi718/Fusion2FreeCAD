import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00581917")
App.ActiveDocument.addObject("PartDesign::Body","Body_F7GBE42tpGZ4gK1_0")
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").Label = "Body_F7GBE42tpGZ4gK1_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Plane", "plane_Sketch_F7GBE42tpGZ4gK1_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7GBE42tpGZ4gK1_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("Sketcher::SketchObject","Sketch_F7GBE42tpGZ4gK1_0_JGC")
App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7GBE42tpGZ4gK1_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-75.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,-75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-75.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,75.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-75.00000000000000,0.00000000000000),App.Vector(60.00000000000000,75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Pad","Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC")
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC")
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").Length = 3.0
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7GBE42tpGZ4gK1_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7GBE42tpGZ4gK1_0_FVcreLGPnFq3lCh_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Plane", "plane_Sketch_Fs0Bcm0qwNlU7QR_1_JJC")
origin = App.Vector(43.50000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fs0Bcm0qwNlU7QR_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("Sketcher::SketchObject","Sketch_Fs0Bcm0qwNlU7QR_1_JJC")
App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fs0Bcm0qwNlU7QR_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-58.50000000000000,19.26168000000000,0.00000000000000),App.Vector(-66.50000000000000,19.26168000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-66.50000000000000,19.26168000000000,0.00000000000000),App.Vector(-66.50000000000000,-23.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-66.50000000000000,-23.00000000000000,0.00000000000000),App.Vector(-20.50000000000000,-23.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-20.50000000000000,-23.00000000000000,0.00000000000000),App.Vector(-20.50000000000000,19.26168000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-20.50000000000000,19.26168000000000,0.00000000000000),App.Vector(-28.50000000000000,19.26168000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-28.50000000000000,19.26168000000000,0.00000000000000),App.Vector(-28.50000000000000,21.26168000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-28.50000000000000,21.26168000000000,0.00000000000000),App.Vector(-18.50000000000000,21.26168000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-18.50000000000000,21.26168000000000,0.00000000000000),App.Vector(-18.50000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-18.50000000000000,-25.00000000000000,0.00000000000000),App.Vector(-68.50000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-68.50000000000000,-25.00000000000000,0.00000000000000),App.Vector(-68.50000000000000,21.26168000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-68.50000000000000,21.26168000000000,0.00000000000000),App.Vector(-58.50000000000000,21.26168000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-58.50000000000000,19.26168000000000,0.00000000000000),App.Vector(-58.50000000000000,21.26168000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Pad","Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC")
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC")
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").Length = 750.0
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fs0Bcm0qwNlU7QR_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fs0Bcm0qwNlU7QR_1_FqTALN9mQAsPZv0_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Plane", "plane_Sketch_FJuiFrSowRPAM8l_1_JNC")
origin = App.Vector(25.00000000000000,-400.00000000000000,-1.86916000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJuiFrSowRPAM8l_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("Sketcher::SketchObject","Sketch_FJuiFrSowRPAM8l_1_JNC")
App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJuiFrSowRPAM8l_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNC").addGeometry(Part.LineSegment(App.Vector(400.00000000000000,-23.13084000000000,0.00000000000000),App.Vector(400.00000000000000,-73.13084000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNC").addGeometry(Part.LineSegment(App.Vector(400.00000000000000,-73.13084000000001,0.00000000000000),App.Vector(350.00000000000006,-23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNC").addGeometry(Part.LineSegment(App.Vector(400.00000000000000,-23.13084000000000,0.00000000000000),App.Vector(350.00000000000006,-23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Pad","Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC")
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNC")
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Plane", "plane_Sketch_FJuiFrSowRPAM8l_1_JNG")
origin = App.Vector(25.00000000000000,-400.00000000000000,-1.86916000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJuiFrSowRPAM8l_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("Sketcher::SketchObject","Sketch_FJuiFrSowRPAM8l_1_JNG")
App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJuiFrSowRPAM8l_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNG").addGeometry(Part.LineSegment(App.Vector(400.00000000000000,23.13084000000000,0.00000000000000),App.Vector(400.00000000000000,76.86915999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNG").addGeometry(Part.LineSegment(App.Vector(400.00000000000000,76.86915999999999,0.00000000000000),App.Vector(350.00000000000006,23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNG").addGeometry(Part.LineSegment(App.Vector(400.00000000000000,23.13084000000000,0.00000000000000),App.Vector(350.00000000000006,23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Pad","Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG")
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNG")
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").Length = 2.0
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Plane", "plane_Sketch_FJuiFrSowRPAM8l_1_JNO")
origin = App.Vector(25.00000000000000,-400.00000000000000,-1.86916000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJuiFrSowRPAM8l_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("Sketcher::SketchObject","Sketch_FJuiFrSowRPAM8l_1_JNO")
App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJuiFrSowRPAM8l_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO").addGeometry(Part.LineSegment(App.Vector(400.00000000000000,23.13084000000000,0.00000000000000),App.Vector(400.00000000000000,-23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO").addGeometry(Part.LineSegment(App.Vector(400.00000000000000,-23.13084000000000,0.00000000000000),App.Vector(350.00000000000006,-23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO").addGeometry(Part.LineSegment(App.Vector(350.00000000000006,23.13084000000000,0.00000000000000),App.Vector(350.00000000000006,-23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO").addGeometry(Part.LineSegment(App.Vector(400.00000000000000,23.13084000000000,0.00000000000000),App.Vector(350.00000000000006,23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Pad","Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO")
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO")
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").Length = 2.0
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJuiFrSowRPAM8l_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJuiFrSowRPAM8l_1_FKTEybDuLuHu3q8_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Plane", "plane_Sketch_FegEHn1pR9Nh8Kc_1_JRC")
origin = App.Vector(-25.00000000000000,-400.00000000000000,-1.86916000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FegEHn1pR9Nh8Kc_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("Sketcher::SketchObject","Sketch_FegEHn1pR9Nh8Kc_1_JRC")
App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FegEHn1pR9Nh8Kc_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRC").addGeometry(Part.LineSegment(App.Vector(-400.00000000000000,-23.13084000000000,0.00000000000000),App.Vector(-400.00000000000000,-73.13084000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRC").addGeometry(Part.LineSegment(App.Vector(-400.00000000000000,-73.13084000000001,0.00000000000000),App.Vector(-350.00000000000006,-23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRC").addGeometry(Part.LineSegment(App.Vector(-400.00000000000000,-23.13084000000000,0.00000000000000),App.Vector(-350.00000000000006,-23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Pad","Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC")
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRC")
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Plane", "plane_Sketch_FegEHn1pR9Nh8Kc_1_JRG")
origin = App.Vector(-25.00000000000000,-400.00000000000000,-1.86916000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FegEHn1pR9Nh8Kc_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("Sketcher::SketchObject","Sketch_FegEHn1pR9Nh8Kc_1_JRG")
App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FegEHn1pR9Nh8Kc_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRG").addGeometry(Part.LineSegment(App.Vector(-400.00000000000000,23.13084000000000,0.00000000000000),App.Vector(-400.00000000000000,76.86915999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRG").addGeometry(Part.LineSegment(App.Vector(-400.00000000000000,76.86915999999999,0.00000000000000),App.Vector(-350.00000000000006,23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRG").addGeometry(Part.LineSegment(App.Vector(-400.00000000000000,23.13084000000000,0.00000000000000),App.Vector(-350.00000000000006,23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Pad","Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG")
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRG")
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").Length = 2.0
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Plane", "plane_Sketch_FegEHn1pR9Nh8Kc_1_JRO")
origin = App.Vector(-25.00000000000000,-400.00000000000000,-1.86916000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FegEHn1pR9Nh8Kc_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("Sketcher::SketchObject","Sketch_FegEHn1pR9Nh8Kc_1_JRO")
App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FegEHn1pR9Nh8Kc_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO").addGeometry(Part.LineSegment(App.Vector(-400.00000000000000,-23.13084000000000,0.00000000000000),App.Vector(-400.00000000000000,23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO").addGeometry(Part.LineSegment(App.Vector(-400.00000000000000,23.13084000000000,0.00000000000000),App.Vector(-350.00000000000006,23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO").addGeometry(Part.LineSegment(App.Vector(-350.00000000000006,23.13084000000000,0.00000000000000),App.Vector(-350.00000000000006,-23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO").addGeometry(Part.LineSegment(App.Vector(-400.00000000000000,-23.13084000000000,0.00000000000000),App.Vector(-350.00000000000006,-23.13084000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7GBE42tpGZ4gK1_0").newObject("PartDesign::Pad","Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO")
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO")
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").Length = 2.0
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FegEHn1pR9Nh8Kc_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FegEHn1pR9Nh8Kc_1_FR5UMA9qZMgPcfn_1_JRO").Offset = 0
App.ActiveDocument.recompute()

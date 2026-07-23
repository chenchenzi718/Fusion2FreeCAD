import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00142960")
App.ActiveDocument.addObject("PartDesign::Body","Body_F1r0CqDpLJrS0Lj_0")
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").Label = "Body_F1r0CqDpLJrS0Lj_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Plane", "plane_Sketch_F1r0CqDpLJrS0Lj_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1r0CqDpLJrS0Lj_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("Sketcher::SketchObject","Sketch_F1r0CqDpLJrS0Lj_0_JGC")
App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1r0CqDpLJrS0Lj_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC").addGeometry(Part.LineSegment(App.Vector(12.00000000000000,34.00000000000000,0.00000000000000),App.Vector(-12.00000000000000,34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC").addGeometry(Part.LineSegment(App.Vector(-12.00000000000000,34.00000000000000,0.00000000000000),App.Vector(-12.00000000000000,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC").addGeometry(Part.LineSegment(App.Vector(12.00000000000000,-34.00000000000000,0.00000000000000),App.Vector(-12.00000000000000,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC").addGeometry(Part.LineSegment(App.Vector(12.00000000000000,34.00000000000000,0.00000000000000),App.Vector(12.00000000000000,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Pad","Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC")
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC")
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").Length = 8.0
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1r0CqDpLJrS0Lj_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1r0CqDpLJrS0Lj_0_F7tuYCbipjPx7sV_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Plane", "plane_Sketch_FXzRsWfqFE8jgUT_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXzRsWfqFE8jgUT_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("Sketcher::SketchObject","Sketch_FXzRsWfqFE8jgUT_1_JJC")
App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXzRsWfqFE8jgUT_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJC").addGeometry(Part.Circle(App.Vector(32.00000000000000,2.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Pad","Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC")
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJC")
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").Length = 40.0
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Plane", "plane_Sketch_FXzRsWfqFE8jgUT_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXzRsWfqFE8jgUT_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("Sketcher::SketchObject","Sketch_FXzRsWfqFE8jgUT_1_JJG")
App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXzRsWfqFE8jgUT_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJG").addGeometry(Part.Circle(App.Vector(-15.50000000000000,2.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Pad","Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG")
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJG")
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").Length = 40.0
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXzRsWfqFE8jgUT_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").Midplane = 1
App.ActiveDocument.getObject("Extrude_FXzRsWfqFE8jgUT_1_FyOAsDfpCYuMqNg_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Plane", "plane_Sketch_FHEMZvGqjISxWAP_1_JNC")
origin = App.Vector(12.00000000000000,0.00000000000000,4.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHEMZvGqjISxWAP_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("Sketcher::SketchObject","Sketch_FHEMZvGqjISxWAP_1_JNC")
App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHEMZvGqjISxWAP_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(30.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),4.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNC").addGeometry(Part.LineSegment(App.Vector(34.00000000000000,4.00000000000000,0.00000000000000),App.Vector(30.00000000000000,4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNC").addGeometry(Part.LineSegment(App.Vector(34.00000000000000,4.00000000000000,0.00000000000000),App.Vector(34.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Pocket","Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC")
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNC")
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Plane", "plane_Sketch_FHEMZvGqjISxWAP_1_JNG")
origin = App.Vector(12.00000000000000,0.00000000000000,4.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHEMZvGqjISxWAP_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("Sketcher::SketchObject","Sketch_FHEMZvGqjISxWAP_1_JNG")
App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHEMZvGqjISxWAP_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-34.00000000000000,-4.00000000000000,0.00000000000000),App.Vector(-19.17245000000000,-4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-19.17245000000000,-4.00000000000000,0.00000000000000),App.Vector(-19.17245000000000,1.42860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-19.17245000000000,1.42860000000000,0.00000000000000),App.Vector(-34.00000000000000,1.42860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-34.00000000000000,-4.00000000000000,0.00000000000000),App.Vector(-34.00000000000000,1.42860000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Pocket","Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG")
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG")
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Plane", "plane_Sketch_FHEMZvGqjISxWAP_1_JNK")
origin = App.Vector(12.00000000000000,0.00000000000000,4.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHEMZvGqjISxWAP_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("Sketcher::SketchObject","Sketch_FHEMZvGqjISxWAP_1_JNK")
App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHEMZvGqjISxWAP_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK").addGeometry(Part.LineSegment(App.Vector(27.24592000000000,-4.00000000000000,0.00000000000000),App.Vector(-12.06821000000000,-4.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK").addGeometry(Part.LineSegment(App.Vector(-12.06821000000000,-4.00000000000000,0.00000000000000),App.Vector(-12.06821000000000,1.42860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK").addGeometry(Part.LineSegment(App.Vector(-12.06821000000000,1.42860000000000,0.00000000000000),App.Vector(27.24592000000000,1.42860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK").addGeometry(Part.LineSegment(App.Vector(27.24592000000000,-4.00000000000000,0.00000000000000),App.Vector(27.24592000000000,1.42860000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Pocket","Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK")
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK")
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHEMZvGqjISxWAP_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHEMZvGqjISxWAP_1_F1U1CdAynk6wswu_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Plane", "plane_Sketch_FtNUY1zLrOmED1m_1_JRC")
origin = App.Vector(0.00000000000000,-2.00000000000000,8.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtNUY1zLrOmED1m_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("Sketcher::SketchObject","Sketch_FtNUY1zLrOmED1m_1_JRC")
App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtNUY1zLrOmED1m_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,30.23360000000000,0.00000000000000),App.Vector(8.00000000000000,30.23360000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC").addGeometry(Part.LineSegment(App.Vector(8.00000000000000,30.23360000000000,0.00000000000000),App.Vector(8.00000000000000,-10.68316000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,-10.68316000000000,0.00000000000000),App.Vector(8.00000000000000,-10.68316000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,30.23360000000000,0.00000000000000),App.Vector(-8.00000000000000,-10.68316000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Pocket","Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC")
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC")
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Plane", "plane_Sketch_FtNUY1zLrOmED1m_1_JRG")
origin = App.Vector(0.00000000000000,-2.00000000000000,8.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtNUY1zLrOmED1m_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("Sketcher::SketchObject","Sketch_FtNUY1zLrOmED1m_1_JRG")
App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtNUY1zLrOmED1m_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,-17.29912000000000,0.00000000000000),App.Vector(8.00000000000000,-17.29912000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG").addGeometry(Part.LineSegment(App.Vector(8.00000000000000,-17.29912000000000,0.00000000000000),App.Vector(8.00000000000000,-28.86311000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,-28.86311000000000,0.00000000000000),App.Vector(8.00000000000000,-28.86311000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,-17.29912000000000,0.00000000000000),App.Vector(-8.00000000000000,-28.86311000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1r0CqDpLJrS0Lj_0").newObject("PartDesign::Pocket","Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG")
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG")
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtNUY1zLrOmED1m_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtNUY1zLrOmED1m_1_FmUNnzMHTYo49Mx_1_JRG").Offset = 0
App.ActiveDocument.recompute()

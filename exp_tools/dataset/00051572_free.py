import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00051572")
App.ActiveDocument.addObject("PartDesign::Body","Body_FsH9T4E5rqVitDJ_0")
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").Label = "Body_FsH9T4E5rqVitDJ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Plane", "plane_Sketch_FsH9T4E5rqVitDJ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsH9T4E5rqVitDJ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("Sketcher::SketchObject","Sketch_FsH9T4E5rqVitDJ_0_JGC")
App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsH9T4E5rqVitDJ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(20.00000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,10.00000000000000,0.00000000000000),App.Vector(20.00000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(-20.00000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Pad","Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC")
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC")
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsH9T4E5rqVitDJ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsH9T4E5rqVitDJ_0_FwFTr4VMrx5D6gs_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Plane", "plane_Sketch_FIeLOzKa7XRHUNl_1_JJC")
origin = App.Vector(-12.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIeLOzKa7XRHUNl_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("Sketcher::SketchObject","Sketch_FIeLOzKa7XRHUNl_1_JJC")
App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIeLOzKa7XRHUNl_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,10.00000000000000,0.00000000000000),App.Vector(32.00000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC").addGeometry(Part.LineSegment(App.Vector(32.00000000000000,10.00000000000000,0.00000000000000),App.Vector(32.00000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,8.00000000000000,0.00000000000000),App.Vector(32.00000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,10.00000000000000,0.00000000000000),App.Vector(-8.00000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Pad","Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC")
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC")
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Plane", "plane_Sketch_FIeLOzKa7XRHUNl_1_JJG")
origin = App.Vector(-12.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIeLOzKa7XRHUNl_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("Sketcher::SketchObject","Sketch_FIeLOzKa7XRHUNl_1_JJG")
App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIeLOzKa7XRHUNl_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(32.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG").addGeometry(Part.LineSegment(App.Vector(32.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(32.00000000000000,-8.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,-8.50000000000000,0.00000000000000),App.Vector(32.00000000000000,-8.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG").addGeometry(Part.LineSegment(App.Vector(-8.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(-8.00000000000000,-8.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Pad","Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG")
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG")
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").Length = 5.0
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIeLOzKa7XRHUNl_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIeLOzKa7XRHUNl_1_FwVPq2WTNKmPdJ8_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Plane", "plane_Sketch_FE0f4TXKEQ1QE5c_1_JNS")
origin = App.Vector(-12.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE0f4TXKEQ1QE5c_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("Sketcher::SketchObject","Sketch_FE0f4TXKEQ1QE5c_1_JNS")
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE0f4TXKEQ1QE5c_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNS").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNS").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Pad","Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS")
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNS")
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").Length = 5.0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Plane", "plane_Sketch_FE0f4TXKEQ1QE5c_1_JNW")
origin = App.Vector(-12.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE0f4TXKEQ1QE5c_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("Sketcher::SketchObject","Sketch_FE0f4TXKEQ1QE5c_1_JNW")
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE0f4TXKEQ1QE5c_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNW").addGeometry(Part.Circle(App.Vector(8.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.05000000000000),False)

App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNW").addGeometry(Part.Circle(App.Vector(8.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Pad","Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW")
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNW")
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").Length = 5.0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Plane", "plane_Sketch_FE0f4TXKEQ1QE5c_1_JNa")
origin = App.Vector(-12.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE0f4TXKEQ1QE5c_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("Sketcher::SketchObject","Sketch_FE0f4TXKEQ1QE5c_1_JNa")
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE0f4TXKEQ1QE5c_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNa").addGeometry(Part.Circle(App.Vector(16.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.15000000000000),False)

App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNa").addGeometry(Part.Circle(App.Vector(16.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Pad","Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa")
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNa")
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").Length = 5.0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").Type = 4
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Plane", "plane_Sketch_FE0f4TXKEQ1QE5c_1_JNe")
origin = App.Vector(-12.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE0f4TXKEQ1QE5c_1_JNe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("Sketcher::SketchObject","Sketch_FE0f4TXKEQ1QE5c_1_JNe")
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE0f4TXKEQ1QE5c_1_JNe"), [""])
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNe").addGeometry(Part.Circle(App.Vector(24.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.25000000000000),False)

App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNe").addGeometry(Part.Circle(App.Vector(24.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Pad","Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe")
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").Profile = App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNe")
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").Length = 5.0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE0f4TXKEQ1QE5c_1_JNe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").Type = 4
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE0f4TXKEQ1QE5c_1_FgiSWA5E8i9aiIQ_1_JNe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Plane", "plane_Sketch_FtHGcj5muELfgsU_1_JRC")
origin = App.Vector(0.85000000000000,-0.25000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtHGcj5muELfgsU_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("Sketcher::SketchObject","Sketch_FtHGcj5muELfgsU_1_JRC")
App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtHGcj5muELfgsU_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC").addGeometry(Part.LineSegment(App.Vector(-20.85000000000000,8.25000000000000,0.00000000000000),App.Vector(-19.15000000000000,8.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC").addGeometry(Part.LineSegment(App.Vector(-19.15000000000000,8.25000000000000,0.00000000000000),App.Vector(-19.15000000000000,-8.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC").addGeometry(Part.LineSegment(App.Vector(-20.85000000000000,-8.25000000000000,0.00000000000000),App.Vector(-19.15000000000000,-8.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC").addGeometry(Part.LineSegment(App.Vector(-20.85000000000000,8.25000000000000,0.00000000000000),App.Vector(-20.85000000000000,-8.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsH9T4E5rqVitDJ_0").newObject("PartDesign::Pad","Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC")
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC")
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtHGcj5muELfgsU_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtHGcj5muELfgsU_1_FZY1tCYQZ8Y6WaA_1_JRC").Offset = 0
App.ActiveDocument.recompute()

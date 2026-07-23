import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00534868")
App.ActiveDocument.addObject("PartDesign::Body","Body_FKNxiIwYJPx4W1b_0")
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").Label = "Body_FKNxiIwYJPx4W1b_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Plane", "plane_Sketch_FKNxiIwYJPx4W1b_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKNxiIwYJPx4W1b_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("Sketcher::SketchObject","Sketch_FKNxiIwYJPx4W1b_0_JGC")
App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKNxiIwYJPx4W1b_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,63.50000000000000,0.00000000000000),App.Vector(63.50000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,63.50000000000000,0.00000000000000),App.Vector(63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,-63.50000000000000,0.00000000000000),App.Vector(63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,63.50000000000000,0.00000000000000),App.Vector(-63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Pad","Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC")
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC")
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").Length = 127.0
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKNxiIwYJPx4W1b_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKNxiIwYJPx4W1b_0_FXhgRJdfsZSEhdI_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Plane", "plane_Sketch_Fp5oCaq8J3WKzAs_1_JJC")
origin = App.Vector(0.00000000000000,-127.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fp5oCaq8J3WKzAs_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("Sketcher::SketchObject","Sketch_Fp5oCaq8J3WKzAs_1_JJC")
App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fp5oCaq8J3WKzAs_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,-63.50000000000000,0.00000000000000),App.Vector(-25.40000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-63.50000000000000,0.00000000000000),App.Vector(-25.40000000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,-25.40000000000000,0.00000000000000),App.Vector(-25.40000000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,-63.50000000000000,0.00000000000000),App.Vector(-63.50000000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Pad","Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC")
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC")
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Plane", "plane_Sketch_Fp5oCaq8J3WKzAs_1_JJG")
origin = App.Vector(0.00000000000000,-127.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fp5oCaq8J3WKzAs_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("Sketcher::SketchObject","Sketch_Fp5oCaq8J3WKzAs_1_JJG")
App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fp5oCaq8J3WKzAs_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,-63.50000000000000,0.00000000000000),App.Vector(25.40000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-63.50000000000000,0.00000000000000),App.Vector(25.40000000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,-25.40000000000000,0.00000000000000),App.Vector(25.40000000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,-63.50000000000000,0.00000000000000),App.Vector(63.50000000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Pad","Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG")
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG")
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fp5oCaq8J3WKzAs_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fp5oCaq8J3WKzAs_1_FqleyBzAp1fokOH_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Plane", "plane_Sketch_F0EgWpXhl1eHqgA_1_JNC")
origin = App.Vector(0.00000000000000,-127.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0EgWpXhl1eHqgA_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("Sketcher::SketchObject","Sketch_F0EgWpXhl1eHqgA_1_JNC")
App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0EgWpXhl1eHqgA_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,88.90000000000001,0.00000000000000),App.Vector(44.45000000000000,88.90000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,88.90000000000001,0.00000000000000),App.Vector(44.45000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,63.50000000000000,0.00000000000000),App.Vector(44.45000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,88.90000000000001,0.00000000000000),App.Vector(-44.45000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Pad","Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC")
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC")
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Plane", "plane_Sketch_F0EgWpXhl1eHqgA_1_JNG")
origin = App.Vector(0.00000000000000,-127.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0EgWpXhl1eHqgA_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("Sketcher::SketchObject","Sketch_F0EgWpXhl1eHqgA_1_JNG")
App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0EgWpXhl1eHqgA_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,38.10000000000000,0.00000000000000),App.Vector(44.45000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,38.10000000000000,0.00000000000000),App.Vector(44.45000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,63.50000000000000,0.00000000000000),App.Vector(44.45000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,38.10000000000000,0.00000000000000),App.Vector(-44.45000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Pad","Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG")
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG")
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0EgWpXhl1eHqgA_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0EgWpXhl1eHqgA_1_Fs2HaODfcPp4zt5_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Plane", "plane_Sketch_FdxhaQ07tYyAx91_1_JRC")
origin = App.Vector(0.00000000000000,-152.40000000000001,88.90000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdxhaQ07tYyAx91_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("Sketcher::SketchObject","Sketch_FdxhaQ07tYyAx91_1_JRC")
App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdxhaQ07tYyAx91_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,25.40000000000001,0.00000000000000),App.Vector(-19.05000000000000,25.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,25.40000000000001,0.00000000000000),App.Vector(-19.05000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,0.00000000000000,0.00000000000000),App.Vector(-19.05000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,25.40000000000001,0.00000000000000),App.Vector(-44.45000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Pad","Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC")
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC")
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").Length = 63.5
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Plane", "plane_Sketch_FdxhaQ07tYyAx91_1_JRG")
origin = App.Vector(0.00000000000000,-152.40000000000001,88.90000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdxhaQ07tYyAx91_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("Sketcher::SketchObject","Sketch_FdxhaQ07tYyAx91_1_JRG")
App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdxhaQ07tYyAx91_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,25.40000000000001,0.00000000000000),App.Vector(19.05000000000000,25.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG").addGeometry(Part.LineSegment(App.Vector(19.05000000000000,25.40000000000001,0.00000000000000),App.Vector(19.05000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,0.00000000000000,0.00000000000000),App.Vector(19.05000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,25.40000000000001,0.00000000000000),App.Vector(44.45000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Pad","Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG")
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG")
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").Length = 63.5
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdxhaQ07tYyAx91_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdxhaQ07tYyAx91_1_FlcKvTufwWs5tFC_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Plane", "plane_Sketch_F6QXODASjyXbdcP_1_JVC")
origin = App.Vector(0.00000000000000,-177.80000000000001,63.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6QXODASjyXbdcP_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("Sketcher::SketchObject","Sketch_F6QXODASjyXbdcP_1_JVC")
App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6QXODASjyXbdcP_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,-7.41914000000000,0.00000000000000),App.Vector(6.35000000000000,-7.41914000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-7.41914000000000,0.00000000000000),App.Vector(6.35000000000000,5.28086000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,5.28086000000000,0.00000000000000),App.Vector(6.35000000000000,5.28086000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,-7.41914000000000,0.00000000000000),App.Vector(-6.35000000000000,5.28086000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKNxiIwYJPx4W1b_0").newObject("PartDesign::Pad","Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC")
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC")
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").Length = 10.160000000000002
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6QXODASjyXbdcP_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6QXODASjyXbdcP_1_F37bzx1oERjpXG4_1_JVC").Offset = 0
App.ActiveDocument.recompute()

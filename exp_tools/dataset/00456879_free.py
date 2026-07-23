import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00456879")
App.ActiveDocument.addObject("PartDesign::Body","Body_FQmbalYa9HMt2TP_0")
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").Label = "Body_FQmbalYa9HMt2TP_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_FQmbalYa9HMt2TP_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQmbalYa9HMt2TP_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_FQmbalYa9HMt2TP_0_JGC")
App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQmbalYa9HMt2TP_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC").addGeometry(Part.LineSegment(App.Vector(-148.50000000000000,105.00000000000000,0.00000000000000),App.Vector(148.50000000000000,105.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC").addGeometry(Part.LineSegment(App.Vector(148.50000000000000,105.00000000000000,0.00000000000000),App.Vector(148.50000000000000,-105.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC").addGeometry(Part.LineSegment(App.Vector(-148.50000000000000,-105.00000000000000,0.00000000000000),App.Vector(148.50000000000000,-105.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC").addGeometry(Part.LineSegment(App.Vector(-148.50000000000000,105.00000000000000,0.00000000000000),App.Vector(-148.50000000000000,-105.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC")
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC")
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQmbalYa9HMt2TP_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQmbalYa9HMt2TP_0_F6rQlId0X2UzPRE_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_FGIuPI4jvJj4Ox4_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGIuPI4jvJj4Ox4_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_FGIuPI4jvJj4Ox4_1_JJC")
App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGIuPI4jvJj4Ox4_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJC").addGeometry(Part.Circle(App.Vector(50.00000000000000,45.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC")
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJC")
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").Length = 1.0
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_FGIuPI4jvJj4Ox4_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGIuPI4jvJj4Ox4_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_FGIuPI4jvJj4Ox4_1_JJG")
App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGIuPI4jvJj4Ox4_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJG").addGeometry(Part.Circle(App.Vector(50.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG")
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJG")
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").Length = 1.0
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_FGIuPI4jvJj4Ox4_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGIuPI4jvJj4Ox4_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_FGIuPI4jvJj4Ox4_1_JJK")
App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGIuPI4jvJj4Ox4_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJK").addGeometry(Part.Circle(App.Vector(50.00000000000000,-45.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK")
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJK")
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").Length = 1.0
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGIuPI4jvJj4Ox4_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGIuPI4jvJj4Ox4_1_FPdOVpwY49OKYfn_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_F6w0ej5NIOTPcC6_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6w0ej5NIOTPcC6_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_F6w0ej5NIOTPcC6_1_JNC")
App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6w0ej5NIOTPcC6_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,45.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC")
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNC")
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").Length = 1.0
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_F6w0ej5NIOTPcC6_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6w0ej5NIOTPcC6_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_F6w0ej5NIOTPcC6_1_JNG")
App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6w0ej5NIOTPcC6_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNG").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG")
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNG")
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").Length = 1.0
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_F6w0ej5NIOTPcC6_1_JNK")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6w0ej5NIOTPcC6_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_F6w0ej5NIOTPcC6_1_JNK")
App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6w0ej5NIOTPcC6_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNK").addGeometry(Part.Circle(App.Vector(0.00000000000000,-45.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK")
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNK")
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").Length = 1.0
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6w0ej5NIOTPcC6_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6w0ej5NIOTPcC6_1_FsseOY0qsNqAeKg_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_FjGBvUTwVYUpjO4_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjGBvUTwVYUpjO4_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_FjGBvUTwVYUpjO4_1_JRC")
App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjGBvUTwVYUpjO4_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRC").addGeometry(Part.Circle(App.Vector(-50.00000000000000,45.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC")
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRC")
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").Length = 1.0
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_FjGBvUTwVYUpjO4_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjGBvUTwVYUpjO4_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_FjGBvUTwVYUpjO4_1_JRG")
App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjGBvUTwVYUpjO4_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRG").addGeometry(Part.Circle(App.Vector(-50.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG")
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRG")
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").Length = 1.0
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Plane", "plane_Sketch_FjGBvUTwVYUpjO4_1_JRK")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjGBvUTwVYUpjO4_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("Sketcher::SketchObject","Sketch_FjGBvUTwVYUpjO4_1_JRK")
App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjGBvUTwVYUpjO4_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRK").addGeometry(Part.Circle(App.Vector(-50.00000000000000,-45.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQmbalYa9HMt2TP_0").newObject("PartDesign::Pad","Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK")
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRK")
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").Length = 1.0
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjGBvUTwVYUpjO4_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjGBvUTwVYUpjO4_1_FtQ4xRYgxS4dfqs_1_JRK").Offset = 0
App.ActiveDocument.recompute()

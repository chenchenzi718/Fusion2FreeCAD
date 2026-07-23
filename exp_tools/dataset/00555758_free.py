import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00555758")
App.ActiveDocument.addObject("PartDesign::Body","Body_FRDFt2zAmXO0AuD_0")
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").Label = "Body_FRDFt2zAmXO0AuD_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Plane", "plane_Sketch_FRDFt2zAmXO0AuD_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRDFt2zAmXO0AuD_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("Sketcher::SketchObject","Sketch_FRDFt2zAmXO0AuD_0_JGC")
App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRDFt2zAmXO0AuD_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.50800000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.50800000000000,0.00000000000000,0.00000000000000),App.Vector(0.50800000000000,-25.90800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-25.90800000000000,0.00000000000000),App.Vector(0.50800000000000,-25.90800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-25.90800000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Pad","Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC")
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC")
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").Length = 431.8
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRDFt2zAmXO0AuD_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRDFt2zAmXO0AuD_0_FriODFbSNTLQWt2_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Plane", "plane_Sketch_FhMB1243v4raN41_1_JJC")
origin = App.Vector(0.50800000000000,-12.70000000000000,215.90000000000001)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhMB1243v4raN41_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("Sketcher::SketchObject","Sketch_FhMB1243v4raN41_1_JJC")
App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhMB1243v4raN41_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC").addGeometry(Part.LineSegment(App.Vector(-13.20800000000000,215.90000000000001,0.00000000000000),App.Vector(-12.70000000000000,215.90000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC").addGeometry(Part.LineSegment(App.Vector(-12.70000000000000,215.90000000000001,0.00000000000000),App.Vector(-12.70000000000000,-215.90000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC").addGeometry(Part.LineSegment(App.Vector(-13.20800000000000,-215.90000000000001,0.00000000000000),App.Vector(-12.70000000000000,-215.90000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC").addGeometry(Part.LineSegment(App.Vector(-13.20800000000000,-215.90000000000001,0.00000000000000),App.Vector(-13.20800000000000,215.90000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Pad","Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC")
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC")
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhMB1243v4raN41_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhMB1243v4raN41_1_FB9cSWQ3yRxCO5E_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Plane", "plane_Sketch_FmZgFN3nA02gRH6_1_JNC")
origin = App.Vector(0.50800000000000,-12.70000000000000,215.90000000000001)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmZgFN3nA02gRH6_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("Sketcher::SketchObject","Sketch_FmZgFN3nA02gRH6_1_JNC")
App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmZgFN3nA02gRH6_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,209.54999999999998,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Pocket","Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC")
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNC")
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Plane", "plane_Sketch_FmZgFN3nA02gRH6_1_JNG")
origin = App.Vector(0.50800000000000,-12.70000000000000,215.90000000000001)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmZgFN3nA02gRH6_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("Sketcher::SketchObject","Sketch_FmZgFN3nA02gRH6_1_JNG")
App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmZgFN3nA02gRH6_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNG").addGeometry(Part.Circle(App.Vector(0.00000000000000,-186.69000000000003,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Pocket","Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG")
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNG")
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Plane", "plane_Sketch_FmZgFN3nA02gRH6_1_JNK")
origin = App.Vector(0.50800000000000,-12.70000000000000,215.90000000000001)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmZgFN3nA02gRH6_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("Sketcher::SketchObject","Sketch_FmZgFN3nA02gRH6_1_JNK")
App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmZgFN3nA02gRH6_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNK").addGeometry(Part.Circle(App.Vector(0.00000000000000,-207.00999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Pocket","Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK")
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNK")
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmZgFN3nA02gRH6_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmZgFN3nA02gRH6_1_FxilwGRnJJY5TF7_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Plane", "plane_Sketch_FcLzOmi0ztsULcy_1_JRC")
origin = App.Vector(13.20800000000000,-25.40000000000000,215.90000000000001)
x_axis=App.Vector(-1.00000000000000,-0.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcLzOmi0ztsULcy_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("Sketcher::SketchObject","Sketch_FcLzOmi0ztsULcy_1_JRC")
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcLzOmi0ztsULcy_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRC").addGeometry(Part.Circle(App.Vector(-6.35000000000000,184.15000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.96875000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Pocket","Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC")
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRC")
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Plane", "plane_Sketch_FcLzOmi0ztsULcy_1_JRK")
origin = App.Vector(13.20800000000000,-25.40000000000000,215.90000000000001)
x_axis=App.Vector(-1.00000000000000,-0.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcLzOmi0ztsULcy_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("Sketcher::SketchObject","Sketch_FcLzOmi0ztsULcy_1_JRK")
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcLzOmi0ztsULcy_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRK").addGeometry(Part.Circle(App.Vector(0.00000000000000,49.21249999999996,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Pocket","Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK")
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRK")
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Plane", "plane_Sketch_FcLzOmi0ztsULcy_1_JRG")
origin = App.Vector(13.20800000000000,-25.40000000000000,215.90000000000001)
x_axis=App.Vector(-1.00000000000000,-0.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcLzOmi0ztsULcy_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("Sketcher::SketchObject","Sketch_FcLzOmi0ztsULcy_1_JRG")
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcLzOmi0ztsULcy_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRG").addGeometry(Part.Circle(App.Vector(0.00000000000000,26.98750000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Pocket","Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG")
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRG")
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Plane", "plane_Sketch_FcLzOmi0ztsULcy_1_JRO")
origin = App.Vector(13.20800000000000,-25.40000000000000,215.90000000000001)
x_axis=App.Vector(-1.00000000000000,-0.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcLzOmi0ztsULcy_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("Sketcher::SketchObject","Sketch_FcLzOmi0ztsULcy_1_JRO")
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcLzOmi0ztsULcy_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRO").addGeometry(Part.Circle(App.Vector(0.00000000000000,-196.84999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FRDFt2zAmXO0AuD_0").newObject("PartDesign::Pocket","Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO")
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRO")
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcLzOmi0ztsULcy_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcLzOmi0ztsULcy_1_FROLNGNcPMtMu3n_1_JRO").Offset = 0
App.ActiveDocument.recompute()

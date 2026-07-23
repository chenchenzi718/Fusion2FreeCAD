import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00249795")
App.ActiveDocument.addObject("PartDesign::Body","Body_FbK7onxIIs4ISWO_0")
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").Label = "Body_FbK7onxIIs4ISWO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Plane", "plane_Sketch_FbK7onxIIs4ISWO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbK7onxIIs4ISWO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("Sketcher::SketchObject","Sketch_FbK7onxIIs4ISWO_0_JGC")
App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbK7onxIIs4ISWO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC").addGeometry(Part.LineSegment(App.Vector(31.00000000000000,-7.50000000000000,0.00000000000000),App.Vector(-31.00000000000000,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-31.00000000000000,-7.50000000000000,0.00000000000000),App.Vector(-31.00000000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC").addGeometry(Part.LineSegment(App.Vector(31.00000000000000,7.50000000000000,0.00000000000000),App.Vector(-31.00000000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC").addGeometry(Part.LineSegment(App.Vector(31.00000000000000,-7.50000000000000,0.00000000000000),App.Vector(31.00000000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Pad","Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC")
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC")
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").Length = 3.4
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbK7onxIIs4ISWO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbK7onxIIs4ISWO_0_FkAEKZA9bbbbecK_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Plane", "plane_Sketch_FKbdy3uPBgMBeec_1_JJG")
origin = App.Vector(0.00000000000000,-0.35000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKbdy3uPBgMBeec_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("Sketcher::SketchObject","Sketch_FKbdy3uPBgMBeec_1_JJG")
App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKbdy3uPBgMBeec_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG").addGeometry(Part.LineSegment(App.Vector(31.00000000000000,-7.85000000000000,0.00000000000000),App.Vector(-31.00000000000000,-7.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG").addGeometry(Part.LineSegment(App.Vector(-31.00000000000000,-7.85000000000000,0.00000000000000),App.Vector(-31.00000000000000,-7.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG").addGeometry(Part.LineSegment(App.Vector(31.00000000000000,-7.15000000000000,0.00000000000000),App.Vector(-31.00000000000000,-7.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG").addGeometry(Part.LineSegment(App.Vector(31.00000000000000,-7.85000000000000,0.00000000000000),App.Vector(31.00000000000000,-7.15000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Pad","Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG")
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG")
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").Length = 2.5
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKbdy3uPBgMBeec_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKbdy3uPBgMBeec_1_FkKhmddR9cSKcU1_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Plane", "plane_Sketch_FDobE0W0hAr8DEy_1_JNC")
origin = App.Vector(-0.00000000000000,-7.50000000000000,1.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("Sketcher::SketchObject","Sketch_FDobE0W0hAr8DEy_1_JNC")
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC").addGeometry(Part.LineSegment(App.Vector(-23.60000000000000,-0.50000000000000,0.00000000000000),App.Vector(-28.00000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC").addGeometry(Part.LineSegment(App.Vector(-28.00000000000000,-0.50000000000000,0.00000000000000),App.Vector(-28.00000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC").addGeometry(Part.LineSegment(App.Vector(-23.60000000000000,0.50000000000000,0.00000000000000),App.Vector(-28.00000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC").addGeometry(Part.LineSegment(App.Vector(-23.60000000000000,-0.50000000000000,0.00000000000000),App.Vector(-23.60000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Pad","Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").Length = 1.0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Plane", "plane_Sketch_FDobE0W0hAr8DEy_1_JNG")
origin = App.Vector(-0.00000000000000,-7.50000000000000,1.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("Sketcher::SketchObject","Sketch_FDobE0W0hAr8DEy_1_JNG")
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG").addGeometry(Part.LineSegment(App.Vector(-13.30000000000000,-0.50000000000000,0.00000000000000),App.Vector(-13.30000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG").addGeometry(Part.LineSegment(App.Vector(-13.30000000000000,0.50000000000000,0.00000000000000),App.Vector(-17.70000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG").addGeometry(Part.LineSegment(App.Vector(-17.70000000000000,0.50000000000000,0.00000000000000),App.Vector(-17.70000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG").addGeometry(Part.LineSegment(App.Vector(-13.30000000000000,-0.50000000000000,0.00000000000000),App.Vector(-17.70000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Pad","Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").Length = 1.0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Plane", "plane_Sketch_FDobE0W0hAr8DEy_1_JNK")
origin = App.Vector(-0.00000000000000,-7.50000000000000,1.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("Sketcher::SketchObject","Sketch_FDobE0W0hAr8DEy_1_JNK")
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK").addGeometry(Part.LineSegment(App.Vector(-3.00000000000000,-0.50000000000000,0.00000000000000),App.Vector(-3.00000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK").addGeometry(Part.LineSegment(App.Vector(-3.00000000000000,0.50000000000000,0.00000000000000),App.Vector(-7.40000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK").addGeometry(Part.LineSegment(App.Vector(-7.40000000000000,0.50000000000000,0.00000000000000),App.Vector(-7.40000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK").addGeometry(Part.LineSegment(App.Vector(-3.00000000000000,-0.50000000000000,0.00000000000000),App.Vector(-7.40000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Pad","Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").Length = 1.0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Plane", "plane_Sketch_FDobE0W0hAr8DEy_1_JNO")
origin = App.Vector(-0.00000000000000,-7.50000000000000,1.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("Sketcher::SketchObject","Sketch_FDobE0W0hAr8DEy_1_JNO")
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO").addGeometry(Part.LineSegment(App.Vector(7.30000000000000,-0.50000000000000,0.00000000000000),App.Vector(7.30000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO").addGeometry(Part.LineSegment(App.Vector(7.30000000000000,0.50000000000000,0.00000000000000),App.Vector(2.90000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO").addGeometry(Part.LineSegment(App.Vector(2.90000000000000,0.50000000000000,0.00000000000000),App.Vector(2.90000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO").addGeometry(Part.LineSegment(App.Vector(7.30000000000000,-0.50000000000000,0.00000000000000),App.Vector(2.90000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Pad","Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").Length = 1.0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Plane", "plane_Sketch_FDobE0W0hAr8DEy_1_JNS")
origin = App.Vector(-0.00000000000000,-7.50000000000000,1.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("Sketcher::SketchObject","Sketch_FDobE0W0hAr8DEy_1_JNS")
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS").addGeometry(Part.LineSegment(App.Vector(17.60000000000000,-0.50000000000000,0.00000000000000),App.Vector(17.60000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS").addGeometry(Part.LineSegment(App.Vector(17.60000000000000,0.50000000000000,0.00000000000000),App.Vector(13.20000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS").addGeometry(Part.LineSegment(App.Vector(13.20000000000000,0.50000000000000,0.00000000000000),App.Vector(13.20000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS").addGeometry(Part.LineSegment(App.Vector(17.60000000000000,-0.50000000000000,0.00000000000000),App.Vector(13.20000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Pad","Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").Length = 1.0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Plane", "plane_Sketch_FDobE0W0hAr8DEy_1_JNW")
origin = App.Vector(-0.00000000000000,-7.50000000000000,1.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("Sketcher::SketchObject","Sketch_FDobE0W0hAr8DEy_1_JNW")
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDobE0W0hAr8DEy_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW").addGeometry(Part.LineSegment(App.Vector(27.90000000000000,-0.50000000000000,0.00000000000000),App.Vector(27.90000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW").addGeometry(Part.LineSegment(App.Vector(27.90000000000000,0.50000000000000,0.00000000000000),App.Vector(23.50000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW").addGeometry(Part.LineSegment(App.Vector(23.50000000000000,0.50000000000000,0.00000000000000),App.Vector(23.50000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW").addGeometry(Part.LineSegment(App.Vector(27.90000000000000,-0.50000000000000,0.00000000000000),App.Vector(23.50000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbK7onxIIs4ISWO_0").newObject("PartDesign::Pad","Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW")
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").Length = 1.0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDobE0W0hAr8DEy_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDobE0W0hAr8DEy_1_FB4HgQPhupGvRfi_1_JNW").Offset = 0
App.ActiveDocument.recompute()

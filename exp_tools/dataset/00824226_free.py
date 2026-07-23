import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00824226")
App.ActiveDocument.addObject("PartDesign::Body","Body_F9HiXscuKp8zwi5_0")
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").Label = "Body_F9HiXscuKp8zwi5_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Plane", "plane_Sketch_F9HiXscuKp8zwi5_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9HiXscuKp8zwi5_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("Sketcher::SketchObject","Sketch_F9HiXscuKp8zwi5_0_JGC")
App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9HiXscuKp8zwi5_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").addGeometry(Part.LineSegment(App.Vector(10.15000000000000,-14.50000000000000,0.00000000000000),App.Vector(-10.15000000000000,-14.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-10.15000000000000,-14.50000000000000,0.00000000000000),App.Vector(-10.15000000000000,14.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-0.55000000000000,14.50000000000000,0.00000000000000),App.Vector(-10.15000000000000,14.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-0.55000000000000,14.50000000000000,0.00000000000000),App.Vector(-0.55000000000000,11.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").addGeometry(Part.LineSegment(App.Vector(10.15000000000000,11.50000000000000,0.00000000000000),App.Vector(-0.55000000000000,11.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").addGeometry(Part.LineSegment(App.Vector(10.15000000000000,-14.50000000000000,0.00000000000000),App.Vector(10.15000000000000,11.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Pad","Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC")
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC")
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").Length = 1.7
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9HiXscuKp8zwi5_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9HiXscuKp8zwi5_0_FlJpnhPiwbi7rsC_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Plane", "plane_Sketch_FUoTNAWE2qGwZiK_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,1.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUoTNAWE2qGwZiK_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("Sketcher::SketchObject","Sketch_FUoTNAWE2qGwZiK_1_JJC")
App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUoTNAWE2qGwZiK_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC").addGeometry(Part.LineSegment(App.Vector(9.35000000000000,-10.15000000000000,0.00000000000000),App.Vector(-9.35000000000000,-10.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC").addGeometry(Part.LineSegment(App.Vector(-9.35000000000000,-10.15000000000000,0.00000000000000),App.Vector(-9.35000000000000,10.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC").addGeometry(Part.LineSegment(App.Vector(9.35000000000000,10.15000000000000,0.00000000000000),App.Vector(-9.35000000000000,10.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC").addGeometry(Part.LineSegment(App.Vector(9.35000000000000,-10.15000000000000,0.00000000000000),App.Vector(9.35000000000000,10.15000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Pad","Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC")
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC")
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").Length = 3.4
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUoTNAWE2qGwZiK_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUoTNAWE2qGwZiK_1_FMEdttIjP3UJuX5_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Plane", "plane_Sketch_FS2gJ255oSJ9gHi_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS2gJ255oSJ9gHi_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("Sketcher::SketchObject","Sketch_FS2gJ255oSJ9gHi_1_JNC")
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS2gJ255oSJ9gHi_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC").addGeometry(Part.LineSegment(App.Vector(-10.15000000000000,12.70787000000000,0.00000000000000),App.Vector(-5.15000000000000,12.70787000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC").addGeometry(Part.LineSegment(App.Vector(-5.15000000000000,12.70787000000000,0.00000000000000),App.Vector(-5.15000000000000,5.40787000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC").addGeometry(Part.LineSegment(App.Vector(-10.15000000000000,5.40787000000000,0.00000000000000),App.Vector(-5.15000000000000,5.40787000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC").addGeometry(Part.LineSegment(App.Vector(-10.15000000000000,12.70787000000000,0.00000000000000),App.Vector(-10.15000000000000,5.40787000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Pad","Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC")
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC")
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").Length = 3.3
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FLpTrSURo7p7Xfg_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Plane", "plane_Sketch_FS2gJ255oSJ9gHi_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS2gJ255oSJ9gHi_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("Sketcher::SketchObject","Sketch_FS2gJ255oSJ9gHi_1_JNG")
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS2gJ255oSJ9gHi_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG").addGeometry(Part.LineSegment(App.Vector(-6.04082000000000,2.97644000000000,0.00000000000000),App.Vector(-0.54082000000000,2.97644000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG").addGeometry(Part.LineSegment(App.Vector(-0.54082000000000,2.97644000000000,0.00000000000000),App.Vector(-0.54082000000000,-6.52356000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG").addGeometry(Part.LineSegment(App.Vector(-6.04082000000000,-6.52356000000000,0.00000000000000),App.Vector(-0.54082000000000,-6.52356000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG").addGeometry(Part.LineSegment(App.Vector(-6.04082000000000,2.97644000000000,0.00000000000000),App.Vector(-6.04082000000000,-6.52356000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Pad","Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG")
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG")
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").Length = 2.5
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Plane", "plane_Sketch_FS2gJ255oSJ9gHi_1_JNK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS2gJ255oSJ9gHi_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("Sketcher::SketchObject","Sketch_FS2gJ255oSJ9gHi_1_JNK")
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS2gJ255oSJ9gHi_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK").addGeometry(Part.LineSegment(App.Vector(1.05857000000000,-5.24780000000000,0.00000000000000),App.Vector(9.75857000000000,-5.24780000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK").addGeometry(Part.LineSegment(App.Vector(9.75857000000000,-5.24780000000000,0.00000000000000),App.Vector(9.75857000000000,-9.54780000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK").addGeometry(Part.LineSegment(App.Vector(1.05857000000000,-9.54780000000000,0.00000000000000),App.Vector(9.75857000000000,-9.54780000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK").addGeometry(Part.LineSegment(App.Vector(1.05857000000000,-5.24780000000000,0.00000000000000),App.Vector(1.05857000000000,-9.54780000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Pad","Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK")
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK")
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").Length = 2.5
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Plane", "plane_Sketch_FS2gJ255oSJ9gHi_1_JNO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS2gJ255oSJ9gHi_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("Sketcher::SketchObject","Sketch_FS2gJ255oSJ9gHi_1_JNO")
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS2gJ255oSJ9gHi_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNO").addGeometry(Part.Circle(App.Vector(6.66458000000000,8.93390000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Pad","Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO")
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNO")
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").Length = 2.5
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS2gJ255oSJ9gHi_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS2gJ255oSJ9gHi_1_FbElHzILqDzyx91_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Plane", "plane_Sketch_FnlYaaye82xDj24_1_JTC")
origin = App.Vector(-1.25000000000000,14.50000000000000,0.85000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnlYaaye82xDj24_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("Sketcher::SketchObject","Sketch_FnlYaaye82xDj24_1_JTC")
App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnlYaaye82xDj24_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC").addGeometry(Part.LineSegment(App.Vector(0.70000000000000,4.85000000000000,0.00000000000000),App.Vector(7.40000000000000,4.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC").addGeometry(Part.LineSegment(App.Vector(7.40000000000000,4.85000000000000,0.00000000000000),App.Vector(7.40000000000000,0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC").addGeometry(Part.LineSegment(App.Vector(0.70000000000000,0.85000000000000,0.00000000000000),App.Vector(7.40000000000000,0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC").addGeometry(Part.LineSegment(App.Vector(0.70000000000000,4.85000000000000,0.00000000000000),App.Vector(0.70000000000000,0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Pad","Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC")
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC")
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").Length = 1.6
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Plane", "plane_Sketch_FnlYaaye82xDj24_1_JTG")
origin = App.Vector(-1.25000000000000,14.50000000000000,0.85000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnlYaaye82xDj24_1_JTG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("Sketcher::SketchObject","Sketch_FnlYaaye82xDj24_1_JTG")
App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnlYaaye82xDj24_1_JTG"), [""])
App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG").addGeometry(Part.LineSegment(App.Vector(0.70000000000000,-1.85000000000000,0.00000000000000),App.Vector(7.40000000000000,-1.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG").addGeometry(Part.LineSegment(App.Vector(7.40000000000000,-1.85000000000000,0.00000000000000),App.Vector(7.40000000000000,-0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG").addGeometry(Part.LineSegment(App.Vector(0.70000000000000,-0.85000000000000,0.00000000000000),App.Vector(7.40000000000000,-0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG").addGeometry(Part.LineSegment(App.Vector(0.70000000000000,-1.85000000000000,0.00000000000000),App.Vector(0.70000000000000,-0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Pad","Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG")
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").Profile = App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG")
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").Length = 1.6
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").Type = 4
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Plane", "plane_Sketch_FnlYaaye82xDj24_1_JTS")
origin = App.Vector(-1.25000000000000,14.50000000000000,0.85000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnlYaaye82xDj24_1_JTS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("Sketcher::SketchObject","Sketch_FnlYaaye82xDj24_1_JTS")
App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnlYaaye82xDj24_1_JTS"), [""])
App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS").addGeometry(Part.LineSegment(App.Vector(0.70000000000000,0.85000000000000,0.00000000000000),App.Vector(0.70000000000000,-0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS").addGeometry(Part.LineSegment(App.Vector(0.70000000000000,-0.85000000000000,0.00000000000000),App.Vector(7.40000000000000,-0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS").addGeometry(Part.LineSegment(App.Vector(7.40000000000000,0.85000000000000,0.00000000000000),App.Vector(7.40000000000000,-0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS").addGeometry(Part.LineSegment(App.Vector(0.70000000000000,0.85000000000000,0.00000000000000),App.Vector(7.40000000000000,0.85000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F9HiXscuKp8zwi5_0").newObject("PartDesign::Pad","Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS")
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").Profile = App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS")
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").Length = 1.6
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnlYaaye82xDj24_1_JTS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").Type = 4
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnlYaaye82xDj24_1_FtRf2rjjiLT33jM_1_JTS").Offset = 0
App.ActiveDocument.recompute()

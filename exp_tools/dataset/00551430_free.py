import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00551430")
App.ActiveDocument.addObject("PartDesign::Body","Body_FtSORxnZY83VpcJ_0")
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").Label = "Body_FtSORxnZY83VpcJ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Plane", "plane_Sketch_FtSORxnZY83VpcJ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtSORxnZY83VpcJ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("Sketcher::SketchObject","Sketch_FtSORxnZY83VpcJ_0_JGC")
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtSORxnZY83VpcJ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-28.00000000000000,0.00000000000000),App.Vector(-28.00000000000000,-28.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-28.00000000000000,-28.00000000000000,0.00000000000000),App.Vector(-28.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-28.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-28.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Pad","Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC")
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC")
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").Length = 24.0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Plane", "plane_Sketch_FtSORxnZY83VpcJ_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtSORxnZY83VpcJ_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("Sketcher::SketchObject","Sketch_FtSORxnZY83VpcJ_0_JGO")
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtSORxnZY83VpcJ_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(28.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO").addGeometry(Part.LineSegment(App.Vector(28.00000000000000,0.00000000000000,0.00000000000000),App.Vector(28.00000000000000,-28.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-28.00000000000000,0.00000000000000),App.Vector(28.00000000000000,-28.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-28.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Pad","Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO")
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO")
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").Length = 24.0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Plane", "plane_Sketch_FtSORxnZY83VpcJ_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtSORxnZY83VpcJ_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("Sketcher::SketchObject","Sketch_FtSORxnZY83VpcJ_0_JGK")
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtSORxnZY83VpcJ_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,28.00000000000000,0.00000000000000),App.Vector(28.00000000000000,28.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK").addGeometry(Part.LineSegment(App.Vector(28.00000000000000,28.00000000000000,0.00000000000000),App.Vector(28.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(28.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,28.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Pad","Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK")
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK")
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").Length = 24.0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Plane", "plane_Sketch_FtSORxnZY83VpcJ_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtSORxnZY83VpcJ_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("Sketcher::SketchObject","Sketch_FtSORxnZY83VpcJ_0_JGG")
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtSORxnZY83VpcJ_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG").addGeometry(Part.LineSegment(App.Vector(-28.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,28.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,28.00000000000000,0.00000000000000),App.Vector(-28.00000000000000,28.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG").addGeometry(Part.LineSegment(App.Vector(-28.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-28.00000000000000,28.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Pad","Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG")
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG")
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").Length = 24.0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtSORxnZY83VpcJ_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtSORxnZY83VpcJ_0_FBEXviBCCDjczYZ_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Plane", "plane_Sketch_FA5Lljoosvuk92f_1_JJC")
origin = App.Vector(-0.00000000000000,28.00000000000000,12.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FA5Lljoosvuk92f_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("Sketcher::SketchObject","Sketch_FA5Lljoosvuk92f_1_JJC")
App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FA5Lljoosvuk92f_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC").addGeometry(Part.LineSegment(App.Vector(-21.82255000000000,1.82147000000000,0.00000000000000),App.Vector(-11.82255000000000,1.82147000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC").addGeometry(Part.LineSegment(App.Vector(-11.82255000000000,1.82147000000000,0.00000000000000),App.Vector(-11.82255000000000,-8.17853000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC").addGeometry(Part.LineSegment(App.Vector(-21.82255000000000,-8.17853000000000,0.00000000000000),App.Vector(-11.82255000000000,-8.17853000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC").addGeometry(Part.LineSegment(App.Vector(-21.82255000000000,1.82147000000000,0.00000000000000),App.Vector(-21.82255000000000,-8.17853000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Pad","Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC")
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC")
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").Length = 8.0
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Plane", "plane_Sketch_FA5Lljoosvuk92f_1_JJG")
origin = App.Vector(-0.00000000000000,28.00000000000000,12.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FA5Lljoosvuk92f_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("Sketcher::SketchObject","Sketch_FA5Lljoosvuk92f_1_JJG")
App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FA5Lljoosvuk92f_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG").addGeometry(Part.LineSegment(App.Vector(22.00900000000000,3.98818000000000,0.00000000000000),App.Vector(10.00900000000000,3.98818000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG").addGeometry(Part.LineSegment(App.Vector(10.00900000000000,3.98818000000000,0.00000000000000),App.Vector(10.00900000000000,-8.01182000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG").addGeometry(Part.LineSegment(App.Vector(22.00900000000000,-8.01182000000000,0.00000000000000),App.Vector(10.00900000000000,-8.01182000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG").addGeometry(Part.LineSegment(App.Vector(22.00900000000000,3.98818000000000,0.00000000000000),App.Vector(22.00900000000000,-8.01182000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Pad","Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG")
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG")
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").Length = 8.0
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FA5Lljoosvuk92f_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FA5Lljoosvuk92f_1_Fum2pOD2jz2f8pY_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Plane", "plane_Sketch_FeDLP574Cz0eOgz_1_JNC")
origin = App.Vector(0.00000000000000,-28.00000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeDLP574Cz0eOgz_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("Sketcher::SketchObject","Sketch_FeDLP574Cz0eOgz_1_JNC")
App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeDLP574Cz0eOgz_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC").addGeometry(Part.LineSegment(App.Vector(-24.08143000000000,6.24954000000000,0.00000000000000),App.Vector(-12.08143000000000,6.24954000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC").addGeometry(Part.LineSegment(App.Vector(-12.08143000000000,6.24954000000000,0.00000000000000),App.Vector(-12.08143000000000,-5.75046000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC").addGeometry(Part.LineSegment(App.Vector(-24.08143000000000,-5.75046000000000,0.00000000000000),App.Vector(-12.08143000000000,-5.75046000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC").addGeometry(Part.LineSegment(App.Vector(-24.08143000000000,6.24954000000000,0.00000000000000),App.Vector(-24.08143000000000,-5.75046000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Pad","Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC")
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC")
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").Length = 8.0
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Plane", "plane_Sketch_FeDLP574Cz0eOgz_1_JNG")
origin = App.Vector(0.00000000000000,-28.00000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeDLP574Cz0eOgz_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("Sketcher::SketchObject","Sketch_FeDLP574Cz0eOgz_1_JNG")
App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeDLP574Cz0eOgz_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG").addGeometry(Part.LineSegment(App.Vector(12.49849000000000,-5.75046000000000,0.00000000000000),App.Vector(22.49849000000000,-5.75046000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG").addGeometry(Part.LineSegment(App.Vector(22.49849000000000,-5.75046000000000,0.00000000000000),App.Vector(22.49849000000000,4.24954000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG").addGeometry(Part.LineSegment(App.Vector(12.49849000000000,4.24954000000000,0.00000000000000),App.Vector(22.49849000000000,4.24954000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG").addGeometry(Part.LineSegment(App.Vector(12.49849000000000,-5.75046000000000,0.00000000000000),App.Vector(12.49849000000000,4.24954000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtSORxnZY83VpcJ_0").newObject("PartDesign::Pad","Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG")
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG")
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").Length = 8.0
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeDLP574Cz0eOgz_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeDLP574Cz0eOgz_1_FYjT3FcTcscvX7E_1_JNG").Offset = 0
App.ActiveDocument.recompute()

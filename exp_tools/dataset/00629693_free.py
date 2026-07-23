import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00629693")
App.ActiveDocument.addObject("PartDesign::Body","Body_FYYEuJhmXjyoAX1_0")
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").Label = "Body_FYYEuJhmXjyoAX1_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Plane", "plane_Sketch_FYYEuJhmXjyoAX1_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYYEuJhmXjyoAX1_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("Sketcher::SketchObject","Sketch_FYYEuJhmXjyoAX1_0_JGC")
App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYYEuJhmXjyoAX1_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC").addGeometry(Part.LineSegment(App.Vector(21.62810000000000,-9.02970000000000,0.00000000000000),App.Vector(-21.62810000000000,-9.02970000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC").addGeometry(Part.LineSegment(App.Vector(-21.62810000000000,-9.02970000000000,0.00000000000000),App.Vector(-21.62810000000000,9.02970000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC").addGeometry(Part.LineSegment(App.Vector(21.62810000000000,9.02970000000000,0.00000000000000),App.Vector(-21.62810000000000,9.02970000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC").addGeometry(Part.LineSegment(App.Vector(21.62810000000000,-9.02970000000000,0.00000000000000),App.Vector(21.62810000000000,9.02970000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Pad","Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC")
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC")
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").Length = 1.651
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYYEuJhmXjyoAX1_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FYYEuJhmXjyoAX1_0_FBMHTkMqYFqMlia_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Plane", "plane_Sketch_FUmjwNP0GmrxMf7_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.82550000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUmjwNP0GmrxMf7_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("Sketcher::SketchObject","Sketch_FUmjwNP0GmrxMf7_1_JJC")
App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUmjwNP0GmrxMf7_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC").addGeometry(Part.LineSegment(App.Vector(23.30450000000000,3.82270000000000,0.00000000000000),App.Vector(21.62810000000000,3.82270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC").addGeometry(Part.LineSegment(App.Vector(21.62810000000000,3.82270000000000,0.00000000000000),App.Vector(21.62810000000000,-3.82270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC").addGeometry(Part.LineSegment(App.Vector(23.30450000000000,-3.82270000000000,0.00000000000000),App.Vector(21.62810000000000,-3.82270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC").addGeometry(Part.LineSegment(App.Vector(23.30450000000000,3.82270000000000,0.00000000000000),App.Vector(23.30450000000000,-3.82270000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Pad","Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC")
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC")
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").Length = 3.81
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Plane", "plane_Sketch_FUmjwNP0GmrxMf7_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.82550000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUmjwNP0GmrxMf7_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("Sketcher::SketchObject","Sketch_FUmjwNP0GmrxMf7_1_JJG")
App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUmjwNP0GmrxMf7_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG").addGeometry(Part.LineSegment(App.Vector(14.03350000000000,3.82270000000000,0.00000000000000),App.Vector(21.62810000000000,3.82270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG").addGeometry(Part.LineSegment(App.Vector(21.62810000000000,3.82270000000000,0.00000000000000),App.Vector(21.62810000000000,-3.82270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG").addGeometry(Part.LineSegment(App.Vector(14.03350000000000,-3.82270000000000,0.00000000000000),App.Vector(21.62810000000000,-3.82270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG").addGeometry(Part.LineSegment(App.Vector(14.03350000000000,3.82270000000000,0.00000000000000),App.Vector(14.03350000000000,-3.82270000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Pad","Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG")
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG")
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").Length = 3.81
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUmjwNP0GmrxMf7_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUmjwNP0GmrxMf7_1_F1TyoFfjFCTanyD_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Plane", "plane_Sketch_F6P8rGpCupCLzNe_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.82550000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6P8rGpCupCLzNe_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("Sketcher::SketchObject","Sketch_F6P8rGpCupCLzNe_1_JNC")
App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6P8rGpCupCLzNe_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC").addGeometry(Part.LineSegment(App.Vector(-2.67970000000000,3.06070000000000,0.00000000000000),App.Vector(-6.38810000000000,3.06070000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC").addGeometry(Part.LineSegment(App.Vector(-6.38810000000000,3.06070000000000,0.00000000000000),App.Vector(-6.38810000000000,-3.06070000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC").addGeometry(Part.LineSegment(App.Vector(-2.67970000000000,-3.06070000000000,0.00000000000000),App.Vector(-6.38810000000000,-3.06070000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC").addGeometry(Part.LineSegment(App.Vector(-2.67970000000000,3.06070000000000,0.00000000000000),App.Vector(-2.67970000000000,-3.06070000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Pad","Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC")
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC")
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").Length = 2.5400000000000005
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Plane", "plane_Sketch_F6P8rGpCupCLzNe_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.82550000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6P8rGpCupCLzNe_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("Sketcher::SketchObject","Sketch_F6P8rGpCupCLzNe_1_JNG")
App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6P8rGpCupCLzNe_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG").addGeometry(Part.LineSegment(App.Vector(6.38810000000000,5.65756000000000,0.00000000000000),App.Vector(12.04566000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG").addGeometry(Part.LineSegment(App.Vector(12.04566000000000,0.00000000000000,0.00000000000000),App.Vector(6.38810000000000,-5.65756000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG").addGeometry(Part.LineSegment(App.Vector(6.38810000000000,-5.65756000000000,0.00000000000000),App.Vector(0.73054000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG").addGeometry(Part.LineSegment(App.Vector(6.38810000000000,5.65756000000000,0.00000000000000),App.Vector(0.73054000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Pad","Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG")
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG")
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").Length = 2.5400000000000005
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6P8rGpCupCLzNe_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6P8rGpCupCLzNe_1_FUBVeDICrKqdb93_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Plane", "plane_Sketch_FmX5tZo9w6JC2oe_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,-0.82550000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmX5tZo9w6JC2oe_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("Sketcher::SketchObject","Sketch_FmX5tZo9w6JC2oe_1_JRC")
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmX5tZo9w6JC2oe_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC").addGeometry(Part.LineSegment(App.Vector(13.88110000000000,2.60350000000000,0.00000000000000),App.Vector(3.72110000000000,2.60350000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC").addGeometry(Part.LineSegment(App.Vector(3.72110000000000,2.60350000000000,0.00000000000000),App.Vector(3.72110000000000,-2.60350000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC").addGeometry(Part.LineSegment(App.Vector(13.88110000000000,-2.60350000000000,0.00000000000000),App.Vector(3.72110000000000,-2.60350000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC").addGeometry(Part.LineSegment(App.Vector(13.88110000000000,2.60350000000000,0.00000000000000),App.Vector(13.88110000000000,-2.60350000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Pad","Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC")
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC")
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").Length = 1.7780000000000002
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Plane", "plane_Sketch_FmX5tZo9w6JC2oe_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,-0.82550000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmX5tZo9w6JC2oe_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("Sketcher::SketchObject","Sketch_FmX5tZo9w6JC2oe_1_JRG")
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmX5tZo9w6JC2oe_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG").addGeometry(Part.LineSegment(App.Vector(16.24618000000000,7.14177000000000,0.00000000000000),App.Vector(12.76638000000000,7.14177000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG").addGeometry(Part.LineSegment(App.Vector(12.76638000000000,7.14177000000000,0.00000000000000),App.Vector(12.76638000000000,5.46537000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG").addGeometry(Part.LineSegment(App.Vector(16.24618000000000,5.46537000000000,0.00000000000000),App.Vector(12.76638000000000,5.46537000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG").addGeometry(Part.LineSegment(App.Vector(16.24618000000000,7.14177000000000,0.00000000000000),App.Vector(16.24618000000000,5.46537000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Pad","Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG")
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG")
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").Length = 1.7780000000000002
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Plane", "plane_Sketch_FmX5tZo9w6JC2oe_1_JRK")
origin = App.Vector(0.00000000000000,0.00000000000000,-0.82550000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmX5tZo9w6JC2oe_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("Sketcher::SketchObject","Sketch_FmX5tZo9w6JC2oe_1_JRK")
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmX5tZo9w6JC2oe_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK").addGeometry(Part.LineSegment(App.Vector(-10.38545000000000,-7.28554000000000,0.00000000000000),App.Vector(-13.89065000000000,-7.28554000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK").addGeometry(Part.LineSegment(App.Vector(-13.89065000000000,-7.28554000000000,0.00000000000000),App.Vector(-13.89065000000000,0.75791000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK").addGeometry(Part.LineSegment(App.Vector(-10.38545000000000,0.75791000000000,0.00000000000000),App.Vector(-13.89065000000000,0.75791000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK").addGeometry(Part.LineSegment(App.Vector(-10.38545000000000,-7.28554000000000,0.00000000000000),App.Vector(-10.38545000000000,0.75791000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Pad","Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK")
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK")
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").Length = 1.7780000000000002
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Plane", "plane_Sketch_FmX5tZo9w6JC2oe_1_JRO")
origin = App.Vector(0.00000000000000,0.00000000000000,-0.82550000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmX5tZo9w6JC2oe_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("Sketcher::SketchObject","Sketch_FmX5tZo9w6JC2oe_1_JRO")
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmX5tZo9w6JC2oe_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO").addGeometry(Part.LineSegment(App.Vector(-9.97371000000000,2.27330000000000,0.00000000000000),App.Vector(-13.45351000000000,2.27330000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO").addGeometry(Part.LineSegment(App.Vector(-13.45351000000000,2.27330000000000,0.00000000000000),App.Vector(-13.45351000000000,3.94970000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO").addGeometry(Part.LineSegment(App.Vector(-9.97371000000000,3.94970000000000,0.00000000000000),App.Vector(-13.45351000000000,3.94970000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO").addGeometry(Part.LineSegment(App.Vector(-9.97371000000000,2.27330000000000,0.00000000000000),App.Vector(-9.97371000000000,3.94970000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYYEuJhmXjyoAX1_0").newObject("PartDesign::Pad","Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO")
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO")
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").Length = 1.7780000000000002
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmX5tZo9w6JC2oe_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmX5tZo9w6JC2oe_1_FTHNDmJW9UHuV0w_1_JRO").Offset = 0
App.ActiveDocument.recompute()

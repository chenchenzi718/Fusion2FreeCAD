import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00527230")
App.ActiveDocument.addObject("PartDesign::Body","Body_FVz85vOgSPeuYka_0")
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").Label = "Body_FVz85vOgSPeuYka_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Plane", "plane_Sketch_FVz85vOgSPeuYka_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVz85vOgSPeuYka_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("Sketcher::SketchObject","Sketch_FVz85vOgSPeuYka_0_JGC")
App.ActiveDocument.getObject("Sketch_FVz85vOgSPeuYka_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVz85vOgSPeuYka_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FVz85vOgSPeuYka_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVz85vOgSPeuYka_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.85000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVz85vOgSPeuYka_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVz85vOgSPeuYka_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Pad","Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC")
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FVz85vOgSPeuYka_0_JGC")
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVz85vOgSPeuYka_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVz85vOgSPeuYka_0_FUZULJIa7P9TFcD_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Plane", "plane_Sketch_FPph0Ujlp5auhSr_1_JJC")
origin = App.Vector(0.00000000000000,7.64843000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPph0Ujlp5auhSr_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("Sketcher::SketchObject","Sketch_FPph0Ujlp5auhSr_1_JJC")
App.ActiveDocument.getObject("Sketch_FPph0Ujlp5auhSr_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPph0Ujlp5auhSr_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FPph0Ujlp5auhSr_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPph0Ujlp5auhSr_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-7.64843000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.64870000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPph0Ujlp5auhSr_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPph0Ujlp5auhSr_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Pocket","Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC")
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FPph0Ujlp5auhSr_1_JJC")
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPph0Ujlp5auhSr_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPph0Ujlp5auhSr_1_FMDT6keFh8ZDGyk_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Plane", "plane_Sketch_Fq7ISqjIveijzcj_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq7ISqjIveijzcj_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("Sketcher::SketchObject","Sketch_Fq7ISqjIveijzcj_1_JNC")
App.ActiveDocument.getObject("Sketch_Fq7ISqjIveijzcj_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq7ISqjIveijzcj_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fq7ISqjIveijzcj_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq7ISqjIveijzcj_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,6.41308000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.39874000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq7ISqjIveijzcj_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq7ISqjIveijzcj_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Pocket","Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC")
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fq7ISqjIveijzcj_1_JNC")
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq7ISqjIveijzcj_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq7ISqjIveijzcj_1_FeIl3hEhDx54ajl_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Plane", "plane_Sketch_F7rOl02SrCbainW_2_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7rOl02SrCbainW_2_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("Sketcher::SketchObject","Sketch_F7rOl02SrCbainW_2_JRC")
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7rOl02SrCbainW_2_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC").addGeometry(Part.LineSegment(App.Vector(3.43349000000000,7.26620000000000,0.00000000000000),App.Vector(3.43349000000000,5.82731000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC").addGeometry(Part.LineSegment(App.Vector(3.43349000000000,5.82731000000000,0.00000000000000),App.Vector(5.52806000000000,5.82731000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC").addGeometry(Part.LineSegment(App.Vector(5.52806000000000,5.82731000000000,0.00000000000000),App.Vector(5.52806000000000,7.26620000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC").addGeometry(Part.LineSegment(App.Vector(3.43349000000000,7.26620000000000,0.00000000000000),App.Vector(5.52806000000000,7.26620000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Pad","Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC")
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").Profile = App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC")
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").Length = -9.0424
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").Length2 = 8.636
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Plane", "plane_Sketch_F7rOl02SrCbainW_2_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7rOl02SrCbainW_2_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("Sketcher::SketchObject","Sketch_F7rOl02SrCbainW_2_JRG")
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7rOl02SrCbainW_2_JRG"), [""])
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG").addGeometry(Part.LineSegment(App.Vector(-3.28737000000000,7.26620000000000,0.00000000000000),App.Vector(-3.28737000000000,5.82731000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG").addGeometry(Part.LineSegment(App.Vector(-3.28737000000000,5.82731000000000,0.00000000000000),App.Vector(-5.56409000000000,5.82731000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG").addGeometry(Part.LineSegment(App.Vector(-5.56409000000000,5.82731000000000,0.00000000000000),App.Vector(-5.56409000000000,7.26620000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG").addGeometry(Part.LineSegment(App.Vector(-3.28737000000000,7.26620000000000,0.00000000000000),App.Vector(-5.56409000000000,7.26620000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Pad","Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG")
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").Profile = App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG")
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").Length = -9.0424
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").Length2 = 8.636
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Plane", "plane_Sketch_F7rOl02SrCbainW_2_JRK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7rOl02SrCbainW_2_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("Sketcher::SketchObject","Sketch_F7rOl02SrCbainW_2_JRK")
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7rOl02SrCbainW_2_JRK"), [""])
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK").addGeometry(Part.LineSegment(App.Vector(0.73786000000000,9.81612000000000,0.00000000000000),App.Vector(-0.75567000000000,9.81612000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK").addGeometry(Part.LineSegment(App.Vector(-0.75567000000000,9.81612000000000,0.00000000000000),App.Vector(-0.75567000000000,11.93665000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK").addGeometry(Part.LineSegment(App.Vector(-0.75567000000000,11.93665000000000,0.00000000000000),App.Vector(0.73786000000000,11.93665000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK").addGeometry(Part.LineSegment(App.Vector(0.73786000000000,9.81612000000000,0.00000000000000),App.Vector(0.73786000000000,11.93665000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Pad","Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK")
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").Profile = App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK")
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").Length = -9.0424
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").Length2 = 8.636
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Plane", "plane_Sketch_F7rOl02SrCbainW_2_JRO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7rOl02SrCbainW_2_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("Sketcher::SketchObject","Sketch_F7rOl02SrCbainW_2_JRO")
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7rOl02SrCbainW_2_JRO"), [""])
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO").addGeometry(Part.LineSegment(App.Vector(0.73786000000000,3.15511000000000,0.00000000000000),App.Vector(-0.75567000000000,3.15511000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO").addGeometry(Part.LineSegment(App.Vector(-0.75567000000000,3.15511000000000,0.00000000000000),App.Vector(-0.75567000000000,0.87533000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO").addGeometry(Part.LineSegment(App.Vector(-0.75567000000000,0.87533000000000,0.00000000000000),App.Vector(0.73786000000000,0.87533000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO").addGeometry(Part.LineSegment(App.Vector(0.73786000000000,3.15511000000000,0.00000000000000),App.Vector(0.73786000000000,0.87533000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Pad","Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO")
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").Profile = App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO")
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").Length = -9.0424
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").Length2 = 8.636
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7rOl02SrCbainW_2_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7rOl02SrCbainW_2_FRm5tDWwt1xzGhS_2_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Plane", "plane_Sketch_FL7uGCOiNhMBwl2_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FL7uGCOiNhMBwl2_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("Sketcher::SketchObject","Sketch_FL7uGCOiNhMBwl2_1_JVC")
App.ActiveDocument.getObject("Sketch_FL7uGCOiNhMBwl2_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FL7uGCOiNhMBwl2_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FL7uGCOiNhMBwl2_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FL7uGCOiNhMBwl2_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,6.46663000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.51081000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FL7uGCOiNhMBwl2_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FL7uGCOiNhMBwl2_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVz85vOgSPeuYka_0").newObject("PartDesign::Pad","Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC")
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FL7uGCOiNhMBwl2_1_JVC")
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").Length = -10.160000000000002
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").Length2 = 7.3660000000000005
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FL7uGCOiNhMBwl2_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FL7uGCOiNhMBwl2_1_FuBy6tgyTBCFMtJ_1_JVC").Offset = 0
App.ActiveDocument.recompute()

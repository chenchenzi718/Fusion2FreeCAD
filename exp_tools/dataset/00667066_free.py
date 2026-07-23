import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00667066")
App.ActiveDocument.addObject("PartDesign::Body","Body_FlJAPEYcylVEl4j_0")
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").Label = "Body_FlJAPEYcylVEl4j_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FlJAPEYcylVEl4j_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlJAPEYcylVEl4j_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FlJAPEYcylVEl4j_0_JGC")
App.ActiveDocument.getObject("Sketch_FlJAPEYcylVEl4j_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlJAPEYcylVEl4j_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FlJAPEYcylVEl4j_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlJAPEYcylVEl4j_0_JGC").addGeometry(Part.Circle(App.Vector(8.12800000000000,26.79700000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),19.49996000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlJAPEYcylVEl4j_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlJAPEYcylVEl4j_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pad","Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC")
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FlJAPEYcylVEl4j_0_JGC")
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").Length = 16.999991400000003
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlJAPEYcylVEl4j_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlJAPEYcylVEl4j_0_F6hQhMvA6wlnvyd_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FpHvm90oBLnWAUr_0_JIC")
origin = App.Vector(8.12800000000000,0.00000000000000,26.79700000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpHvm90oBLnWAUr_0_JIC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FpHvm90oBLnWAUr_0_JIC")
App.ActiveDocument.getObject("Sketch_FpHvm90oBLnWAUr_0_JIC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpHvm90oBLnWAUr_0_JIC"), [""])
App.ActiveDocument.getObject("Sketch_FpHvm90oBLnWAUr_0_JIC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpHvm90oBLnWAUr_0_JIC").addGeometry(Part.Circle(App.Vector(0.17367000000000,0.11983000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpHvm90oBLnWAUr_0_JIC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpHvm90oBLnWAUr_0_JIC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pocket","Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC")
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").Profile = App.ActiveDocument.getObject("Sketch_FpHvm90oBLnWAUr_0_JIC")
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").Length = 12.000001400000002
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpHvm90oBLnWAUr_0_JIC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").Type = 4
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpHvm90oBLnWAUr_0_FdoA6gBeLGmUpyH_1_JIC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FTSbo5ZOW42iawu_1_JNC")
origin = App.Vector(8.30167000000000,12.00000000000000,26.91683000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FTSbo5ZOW42iawu_1_JNC")
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNC").addGeometry(Part.Circle(App.Vector(-1.60411000000000,7.02841000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.49163000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pocket","Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNC")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FTSbo5ZOW42iawu_1_JNe")
origin = App.Vector(8.30167000000000,12.00000000000000,26.91683000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FTSbo5ZOW42iawu_1_JNe")
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNe"), [""])
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNe").addGeometry(Part.Circle(App.Vector(3.83556000000000,6.10412000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.49163000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pocket","Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").Profile = App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNe")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").Type = 4
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FTSbo5ZOW42iawu_1_JNa")
origin = App.Vector(8.30167000000000,12.00000000000000,26.91683000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FTSbo5ZOW42iawu_1_JNa")
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNa").addGeometry(Part.Circle(App.Vector(7.02841000000000,1.60411000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.49163000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pocket","Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNa")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").Type = 4
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FTSbo5ZOW42iawu_1_JNW")
origin = App.Vector(8.30167000000000,12.00000000000000,26.91683000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FTSbo5ZOW42iawu_1_JNW")
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNW").addGeometry(Part.Circle(App.Vector(6.10412000000000,-3.83556000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.49163000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pocket","Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNW")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FTSbo5ZOW42iawu_1_JNS")
origin = App.Vector(8.30167000000000,12.00000000000000,26.91683000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FTSbo5ZOW42iawu_1_JNS")
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNS").addGeometry(Part.Circle(App.Vector(1.60411000000000,-7.02841000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.49163000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pocket","Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNS")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FTSbo5ZOW42iawu_1_JNO")
origin = App.Vector(8.30167000000000,12.00000000000000,26.91683000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FTSbo5ZOW42iawu_1_JNO")
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNO").addGeometry(Part.Circle(App.Vector(-3.83556000000000,-6.10411000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.49163000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pocket","Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNO")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FTSbo5ZOW42iawu_1_JNK")
origin = App.Vector(8.30167000000000,12.00000000000000,26.91683000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FTSbo5ZOW42iawu_1_JNK")
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNK").addGeometry(Part.Circle(App.Vector(-7.02841000000000,-1.60411000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.49163000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pocket","Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNK")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Plane", "plane_Sketch_FTSbo5ZOW42iawu_1_JNG")
origin = App.Vector(8.30167000000000,12.00000000000000,26.91683000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("Sketcher::SketchObject","Sketch_FTSbo5ZOW42iawu_1_JNG")
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTSbo5ZOW42iawu_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNG").addGeometry(Part.Circle(App.Vector(-6.10411000000000,3.83556000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.49163000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlJAPEYcylVEl4j_0").newObject("PartDesign::Pocket","Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNG")
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTSbo5ZOW42iawu_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTSbo5ZOW42iawu_1_FDmEYCHrjXCtgMG_1_JNG").Offset = 0
App.ActiveDocument.recompute()

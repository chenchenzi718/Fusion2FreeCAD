import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00477984")
App.ActiveDocument.addObject("PartDesign::Body","Body_FqKVd07s815pSJW_0")
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").Label = "Body_FqKVd07s815pSJW_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Plane", "plane_Sketch_FqKVd07s815pSJW_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqKVd07s815pSJW_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("Sketcher::SketchObject","Sketch_FqKVd07s815pSJW_0_JGC")
App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqKVd07s815pSJW_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC").addGeometry(Part.LineSegment(App.Vector(-72.68997000000000,42.62871000000000,0.00000000000000),App.Vector(232.11002999999999,42.62871000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC").addGeometry(Part.LineSegment(App.Vector(232.11002999999999,42.62871000000000,0.00000000000000),App.Vector(232.11002999999999,-58.97129000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC").addGeometry(Part.LineSegment(App.Vector(-72.68997000000000,-58.97129000000000,0.00000000000000),App.Vector(232.11002999999999,-58.97129000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC").addGeometry(Part.LineSegment(App.Vector(-72.68997000000000,42.62871000000000,0.00000000000000),App.Vector(-72.68997000000000,-58.97129000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Pad","Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC")
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC")
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqKVd07s815pSJW_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqKVd07s815pSJW_0_FRsO9NAb6TUGNUG_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Plane", "plane_Sketch_FnXB3lkVEmy2fuw_1_JJC")
origin = App.Vector(79.71003000000000,-8.17129000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnXB3lkVEmy2fuw_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("Sketcher::SketchObject","Sketch_FnXB3lkVEmy2fuw_1_JJC")
App.ActiveDocument.getObject("Sketch_FnXB3lkVEmy2fuw_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnXB3lkVEmy2fuw_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FnXB3lkVEmy2fuw_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnXB3lkVEmy2fuw_1_JJC").addGeometry(Part.Circle(App.Vector(-127.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnXB3lkVEmy2fuw_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnXB3lkVEmy2fuw_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Pocket","Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC")
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FnXB3lkVEmy2fuw_1_JJC")
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnXB3lkVEmy2fuw_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnXB3lkVEmy2fuw_1_FgiwfcgObDnlf4v_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Plane", "plane_Sketch_FTHaUBgbcXlVEOF_1_JOC")
origin = App.Vector(79.71003000000000,-8.17129000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTHaUBgbcXlVEOF_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("Sketcher::SketchObject","Sketch_FTHaUBgbcXlVEOF_1_JOC")
App.ActiveDocument.getObject("Sketch_FTHaUBgbcXlVEOF_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTHaUBgbcXlVEOF_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_FTHaUBgbcXlVEOF_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTHaUBgbcXlVEOF_1_JOC").addGeometry(Part.Circle(App.Vector(114.30000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.28750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTHaUBgbcXlVEOF_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTHaUBgbcXlVEOF_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Pocket","Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC")
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_FTHaUBgbcXlVEOF_1_JOC")
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTHaUBgbcXlVEOF_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTHaUBgbcXlVEOF_1_FE8vL59LExcZ9fV_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Plane", "plane_Sketch_F0jnQvijBAeeCSz_1_JSC")
origin = App.Vector(79.71003000000000,-8.17129000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0jnQvijBAeeCSz_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("Sketcher::SketchObject","Sketch_F0jnQvijBAeeCSz_1_JSC")
App.ActiveDocument.getObject("Sketch_F0jnQvijBAeeCSz_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0jnQvijBAeeCSz_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_F0jnQvijBAeeCSz_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0jnQvijBAeeCSz_1_JSC").addGeometry(Part.Circle(App.Vector(-25.40000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.28750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0jnQvijBAeeCSz_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0jnQvijBAeeCSz_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Pocket","Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC")
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_F0jnQvijBAeeCSz_1_JSC")
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0jnQvijBAeeCSz_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").Type = 4
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0jnQvijBAeeCSz_1_FsDJLVsFgEii1wW_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Plane", "plane_Sketch_FJtz4GYszgEY2rQ_1_JYC")
origin = App.Vector(54.31003000000000,-8.17129000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJtz4GYszgEY2rQ_1_JYC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("Sketcher::SketchObject","Sketch_FJtz4GYszgEY2rQ_1_JYC")
App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJtz4GYszgEY2rQ_1_JYC"), [""])
App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYC").addGeometry(Part.Circle(App.Vector(-17.72920000000000,-17.72920000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.41300000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Pocket","Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC")
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").Profile = App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYC")
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").Type = 4
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Plane", "plane_Sketch_FJtz4GYszgEY2rQ_1_JYG")
origin = App.Vector(54.31003000000000,-8.17129000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJtz4GYszgEY2rQ_1_JYG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("Sketcher::SketchObject","Sketch_FJtz4GYszgEY2rQ_1_JYG")
App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJtz4GYszgEY2rQ_1_JYG"), [""])
App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYG").addGeometry(Part.Circle(App.Vector(17.72920000000000,17.72920000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.41300000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Pocket","Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG")
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").Profile = App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYG")
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJtz4GYszgEY2rQ_1_JYG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").Type = 4
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJtz4GYszgEY2rQ_1_FLVBovxb01DdTwp_1_JYG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Plane", "plane_Sketch_Fx1rWwziKhWRn44_1_JcC")
origin = App.Vector(79.71003000000000,-8.17129000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx1rWwziKhWRn44_1_JcC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("Sketcher::SketchObject","Sketch_Fx1rWwziKhWRn44_1_JcC")
App.ActiveDocument.getObject("Sketch_Fx1rWwziKhWRn44_1_JcC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx1rWwziKhWRn44_1_JcC"), [""])
App.ActiveDocument.getObject("Sketch_Fx1rWwziKhWRn44_1_JcC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx1rWwziKhWRn44_1_JcC").addGeometry(Part.Circle(App.Vector(25.39999999999999,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.08610000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx1rWwziKhWRn44_1_JcC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx1rWwziKhWRn44_1_JcC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Pocket","Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC")
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").Profile = App.ActiveDocument.getObject("Sketch_Fx1rWwziKhWRn44_1_JcC")
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx1rWwziKhWRn44_1_JcC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").Type = 0
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx1rWwziKhWRn44_1_FETki6sKqIwymtR_1_JcC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Plane", "plane_Sketch_FbD7JGZ0U7SCK6D_1_JgC")
origin = App.Vector(79.71003000000000,-8.17129000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbD7JGZ0U7SCK6D_1_JgC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("Sketcher::SketchObject","Sketch_FbD7JGZ0U7SCK6D_1_JgC")
App.ActiveDocument.getObject("Sketch_FbD7JGZ0U7SCK6D_1_JgC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbD7JGZ0U7SCK6D_1_JgC"), [""])
App.ActiveDocument.getObject("Sketch_FbD7JGZ0U7SCK6D_1_JgC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbD7JGZ0U7SCK6D_1_JgC").addGeometry(Part.Circle(App.Vector(-52.38750000000000,38.10000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.08610000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbD7JGZ0U7SCK6D_1_JgC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbD7JGZ0U7SCK6D_1_JgC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Pocket","Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC")
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").Profile = App.ActiveDocument.getObject("Sketch_FbD7JGZ0U7SCK6D_1_JgC")
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbD7JGZ0U7SCK6D_1_JgC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").Type = 0
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbD7JGZ0U7SCK6D_1_Frs3V9scFN5TgGH_1_JgC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Plane", "plane_Sketch_FP4rzwCA8gRuQSK_1_JkC")
origin = App.Vector(79.71003000000000,-8.17129000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FP4rzwCA8gRuQSK_1_JkC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("Sketcher::SketchObject","Sketch_FP4rzwCA8gRuQSK_1_JkC")
App.ActiveDocument.getObject("Sketch_FP4rzwCA8gRuQSK_1_JkC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FP4rzwCA8gRuQSK_1_JkC"), [""])
App.ActiveDocument.getObject("Sketch_FP4rzwCA8gRuQSK_1_JkC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FP4rzwCA8gRuQSK_1_JkC").addGeometry(Part.Circle(App.Vector(139.69999999999999,38.10000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.08610000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FP4rzwCA8gRuQSK_1_JkC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FP4rzwCA8gRuQSK_1_JkC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqKVd07s815pSJW_0").newObject("PartDesign::Pocket","Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC")
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").Profile = App.ActiveDocument.getObject("Sketch_FP4rzwCA8gRuQSK_1_JkC")
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FP4rzwCA8gRuQSK_1_JkC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").Type = 4
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FP4rzwCA8gRuQSK_1_FwTAqWpStW9FX4T_1_JkC").Offset = 0
App.ActiveDocument.recompute()

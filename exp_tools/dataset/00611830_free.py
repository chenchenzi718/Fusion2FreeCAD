import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00611830")
App.ActiveDocument.addObject("PartDesign::Body","Body_Ft73JOyHpbn5KJ6_0")
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").Label = "Body_Ft73JOyHpbn5KJ6_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Plane", "plane_Sketch_Ft73JOyHpbn5KJ6_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft73JOyHpbn5KJ6_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("Sketcher::SketchObject","Sketch_Ft73JOyHpbn5KJ6_0_JGC")
App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft73JOyHpbn5KJ6_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-59.69084000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC").addGeometry(Part.LineSegment(App.Vector(-59.69084000000000,0.00000000000000,0.00000000000000),App.Vector(-59.69084000000000,-73.27628999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-73.27628999999999,0.00000000000000),App.Vector(-59.69084000000000,-73.27628999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-73.27628999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Pad","Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC")
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC")
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").Length = 38.1
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Plane", "plane_Sketch_Ft73JOyHpbn5KJ6_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft73JOyHpbn5KJ6_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("Sketcher::SketchObject","Sketch_Ft73JOyHpbn5KJ6_0_JGG")
App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft73JOyHpbn5KJ6_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(45.37568000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG").addGeometry(Part.LineSegment(App.Vector(45.37568000000000,0.00000000000000,0.00000000000000),App.Vector(45.37568000000000,-73.27628999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-73.27628999999999,0.00000000000000),App.Vector(45.37568000000000,-73.27628999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-73.27628999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Pad","Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG")
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG")
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").Length = 38.1
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft73JOyHpbn5KJ6_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft73JOyHpbn5KJ6_0_FhkHgMq6vv1Ndur_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Plane", "plane_Sketch_Fm3gBHO6YBccYYW_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fm3gBHO6YBccYYW_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("Sketcher::SketchObject","Sketch_Fm3gBHO6YBccYYW_1_JJC")
App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fm3gBHO6YBccYYW_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC").addGeometry(Part.LineSegment(App.Vector(46.19282000000000,0.00000000000000,0.00000000000000),App.Vector(-9.06588000000000,42.45135000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC").addGeometry(Part.LineSegment(App.Vector(-9.06588000000000,42.45135000000000,0.00000000000000),App.Vector(48.20747000000000,42.45135000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC").addGeometry(Part.LineSegment(App.Vector(48.20747000000000,42.45135000000000,0.00000000000000),App.Vector(48.20747000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC").addGeometry(Part.LineSegment(App.Vector(46.19282000000000,0.00000000000000,0.00000000000000),App.Vector(48.20747000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Pocket","Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC")
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC")
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").Length = 76.2
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fm3gBHO6YBccYYW_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fm3gBHO6YBccYYW_1_FaMLZndSmiUTMsq_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Plane", "plane_Sketch_FlEAHVQZoK0XWuf_1_JNC")
origin = App.Vector(-59.69084000000000,-36.63815000000000,19.05000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlEAHVQZoK0XWuf_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("Sketcher::SketchObject","Sketch_FlEAHVQZoK0XWuf_1_JNC")
App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlEAHVQZoK0XWuf_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC").addGeometry(Part.LineSegment(App.Vector(-9.15270000000000,19.05000000000000,0.00000000000000),App.Vector(-9.15270000000000,10.16228000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC").addGeometry(Part.LineSegment(App.Vector(-9.15270000000000,10.16228000000000,0.00000000000000),App.Vector(11.28151000000000,10.16228000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC").addGeometry(Part.LineSegment(App.Vector(11.28151000000000,10.16228000000000,0.00000000000000),App.Vector(11.28151000000000,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC").addGeometry(Part.LineSegment(App.Vector(-9.15270000000000,19.05000000000000,0.00000000000000),App.Vector(11.28151000000000,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Pocket","Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC")
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC")
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlEAHVQZoK0XWuf_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlEAHVQZoK0XWuf_1_F1d74Hb6P7wsK6K_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Plane", "plane_Sketch_FTUN3ljUUXG2bQC_1_JTC")
origin = App.Vector(-7.15758000000000,-36.63815000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTUN3ljUUXG2bQC_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("Sketcher::SketchObject","Sketch_FTUN3ljUUXG2bQC_1_JTC")
App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTUN3ljUUXG2bQC_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC").addGeometry(Part.LineSegment(App.Vector(24.56983000000000,36.63813999999999,0.00000000000000),App.Vector(24.56983000000000,21.93031999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC").addGeometry(Part.LineSegment(App.Vector(24.56983000000000,21.93031999999999,0.00000000000000),App.Vector(52.53326000000000,21.93031999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC").addGeometry(Part.LineSegment(App.Vector(52.53326000000000,36.63813999999999,0.00000000000000),App.Vector(52.53326000000000,21.93031999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC").addGeometry(Part.LineSegment(App.Vector(52.53326000000000,36.63813999999999,0.00000000000000),App.Vector(24.56983000000000,36.63813999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Pocket","Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC")
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC")
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTUN3ljUUXG2bQC_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTUN3ljUUXG2bQC_1_FwQKUDf5rUJXz7W_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Plane", "plane_Sketch_FVWetmgttQc7w2W_1_JXC")
origin = App.Vector(-7.15758000000000,-36.63815000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVWetmgttQc7w2W_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("Sketcher::SketchObject","Sketch_FVWetmgttQc7w2W_1_JXC")
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVWetmgttQc7w2W_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXC").addGeometry(Part.Circle(App.Vector(19.67713000000000,3.51075000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.89270000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Pocket","Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC")
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXC")
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Plane", "plane_Sketch_FVWetmgttQc7w2W_1_JXG")
origin = App.Vector(-7.15758000000000,-36.63815000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVWetmgttQc7w2W_1_JXG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("Sketcher::SketchObject","Sketch_FVWetmgttQc7w2W_1_JXG")
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVWetmgttQc7w2W_1_JXG"), [""])
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXG").addGeometry(Part.Circle(App.Vector(19.62118000000000,-22.39425000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.94864000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Pocket","Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG")
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").Profile = App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXG")
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").Length = 76.2
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").Type = 4
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Plane", "plane_Sketch_FVWetmgttQc7w2W_1_JXK")
origin = App.Vector(-7.15758000000000,-36.63815000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVWetmgttQc7w2W_1_JXK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("Sketcher::SketchObject","Sketch_FVWetmgttQc7w2W_1_JXK")
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVWetmgttQc7w2W_1_JXK"), [""])
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXK").addGeometry(Part.Circle(App.Vector(39.37803000000000,3.51075000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.91294000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Pocket","Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK")
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").Profile = App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXK")
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").Length = 76.2
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").Type = 4
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Plane", "plane_Sketch_FVWetmgttQc7w2W_1_JXO")
origin = App.Vector(-7.15758000000000,-36.63815000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVWetmgttQc7w2W_1_JXO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("Sketcher::SketchObject","Sketch_FVWetmgttQc7w2W_1_JXO")
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVWetmgttQc7w2W_1_JXO"), [""])
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXO").addGeometry(Part.Circle(App.Vector(39.48090000000000,-22.67979000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.36046000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ft73JOyHpbn5KJ6_0").newObject("PartDesign::Pocket","Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO")
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").Profile = App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXO")
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").Length = 76.2
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVWetmgttQc7w2W_1_JXO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").Type = 4
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVWetmgttQc7w2W_1_F3uWGu0eCo9cfbj_1_JXO").Offset = 0
App.ActiveDocument.recompute()

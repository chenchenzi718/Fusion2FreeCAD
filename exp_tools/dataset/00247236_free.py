import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00247236")
App.ActiveDocument.addObject("PartDesign::Body","Body_FnyyVfIzMCZcsiL_0")
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").Label = "Body_FnyyVfIzMCZcsiL_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Plane", "plane_Sketch_FnyyVfIzMCZcsiL_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnyyVfIzMCZcsiL_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("Sketcher::SketchObject","Sketch_FnyyVfIzMCZcsiL_0_JGC")
App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnyyVfIzMCZcsiL_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,22.50000000000000,0.00000000000000),App.Vector(-35.00000000000000,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC").addGeometry(Part.LineSegment(App.Vector(-35.00000000000000,22.50000000000000,0.00000000000000),App.Vector(-35.00000000000000,-22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-22.50000000000000,0.00000000000000),App.Vector(-35.00000000000000,-22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,22.50000000000000,0.00000000000000),App.Vector(35.00000000000000,-22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Pad","Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC")
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC")
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").Length = 40.0
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnyyVfIzMCZcsiL_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FnyyVfIzMCZcsiL_0_Flw2phFmWcpABie_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Plane", "plane_Sketch_F4gPJGbq1LeKfH1_1_JKC")
origin = App.Vector(0.00000000000000,-0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4gPJGbq1LeKfH1_1_JKC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("Sketcher::SketchObject","Sketch_F4gPJGbq1LeKfH1_1_JKC")
App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4gPJGbq1LeKfH1_1_JKC"), [""])
App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,12.50000000000000,0.00000000000000),App.Vector(-15.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC").addGeometry(Part.LineSegment(App.Vector(-15.00000000000000,12.50000000000000,0.00000000000000),App.Vector(-15.00000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(-15.00000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,12.50000000000000,0.00000000000000),App.Vector(-30.00000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Pad","Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC")
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").Profile = App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC")
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").Length = 1.0
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4gPJGbq1LeKfH1_1_JKC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").Type = 4
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4gPJGbq1LeKfH1_1_FmehYd76ThOrSLn_1_JKC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Plane", "plane_Sketch_FkPepIciK67Uv1a_1_JOC")
origin = App.Vector(0.00000000000000,-0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkPepIciK67Uv1a_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("Sketcher::SketchObject","Sketch_FkPepIciK67Uv1a_1_JOC")
App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkPepIciK67Uv1a_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,15.00000000000000,0.00000000000000),App.Vector(25.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,15.00000000000000,0.00000000000000),App.Vector(25.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(25.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,15.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Pocket","Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC")
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC")
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").Length = 1.0
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkPepIciK67Uv1a_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkPepIciK67Uv1a_1_FjhCksxRqFBzVI0_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Plane", "plane_Sketch_FkeuvxHYU8fXRlF_1_JSC")
origin = App.Vector(-22.50000000000000,-0.00000000000000,21.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkeuvxHYU8fXRlF_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("Sketcher::SketchObject","Sketch_FkeuvxHYU8fXRlF_1_JSC")
App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkeuvxHYU8fXRlF_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC").addGeometry(Part.LineSegment(App.Vector(-2.50000000000000,7.50000000000000,0.00000000000000),App.Vector(2.50000000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC").addGeometry(Part.LineSegment(App.Vector(2.50000000000000,7.50000000000000,0.00000000000000),App.Vector(2.50000000000000,5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC").addGeometry(Part.LineSegment(App.Vector(-2.50000000000000,5.50000000000000,0.00000000000000),App.Vector(2.50000000000000,5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC").addGeometry(Part.LineSegment(App.Vector(-2.50000000000000,7.50000000000000,0.00000000000000),App.Vector(-2.50000000000000,5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Pad","Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC")
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC")
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").Length = 15.0
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkeuvxHYU8fXRlF_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").Type = 4
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkeuvxHYU8fXRlF_1_FNf5oldVQCS8Sxg_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Plane", "plane_Sketch_FiR432Dq09iQGb7_1_JXC")
origin = App.Vector(-22.50000000000000,-0.00000000000000,21.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiR432Dq09iQGb7_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("Sketcher::SketchObject","Sketch_FiR432Dq09iQGb7_1_JXC")
App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiR432Dq09iQGb7_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC").addGeometry(Part.LineSegment(App.Vector(-2.50000000000000,-5.50000000000000,0.00000000000000),App.Vector(2.50000000000000,-5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC").addGeometry(Part.LineSegment(App.Vector(2.50000000000000,-5.50000000000000,0.00000000000000),App.Vector(2.50000000000000,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC").addGeometry(Part.LineSegment(App.Vector(-2.50000000000000,-7.50000000000000,0.00000000000000),App.Vector(2.50000000000000,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC").addGeometry(Part.LineSegment(App.Vector(-2.50000000000000,-5.50000000000000,0.00000000000000),App.Vector(-2.50000000000000,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Pad","Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC")
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC")
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").Length = 15.0
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiR432Dq09iQGb7_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiR432Dq09iQGb7_1_FqQIYvxysNbvEDs_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Plane", "plane_Sketch_Fr7ezOnqVEsQZn6_1_JbC")
origin = App.Vector(35.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr7ezOnqVEsQZn6_1_JbC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("Sketcher::SketchObject","Sketch_Fr7ezOnqVEsQZn6_1_JbC")
App.ActiveDocument.getObject("Sketch_Fr7ezOnqVEsQZn6_1_JbC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr7ezOnqVEsQZn6_1_JbC"), [""])
App.ActiveDocument.getObject("Sketch_Fr7ezOnqVEsQZn6_1_JbC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr7ezOnqVEsQZn6_1_JbC").addGeometry(Part.Circle(App.Vector(-8.75000000000000,6.25000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr7ezOnqVEsQZn6_1_JbC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr7ezOnqVEsQZn6_1_JbC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Pad","Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC")
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").Profile = App.ActiveDocument.getObject("Sketch_Fr7ezOnqVEsQZn6_1_JbC")
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").Length = 20.0
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr7ezOnqVEsQZn6_1_JbC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").Type = 4
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fr7ezOnqVEsQZn6_1_FWnCWjdttkIfbAB_1_JbC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Plane", "plane_Sketch_FGznHwe0NzpHSc3_1_JfC")
origin = App.Vector(0.00000000000000,-0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGznHwe0NzpHSc3_1_JfC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("Sketcher::SketchObject","Sketch_FGznHwe0NzpHSc3_1_JfC")
App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGznHwe0NzpHSc3_1_JfC"), [""])
App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,22.50000000000000,0.00000000000000),App.Vector(25.00000000000000,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,22.50000000000000,0.00000000000000),App.Vector(25.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(30.00000000000000,17.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,12.50000000000000,0.00000000000000),App.Vector(30.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,22.50000000000000,0.00000000000000),App.Vector(35.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Pocket","Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC")
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").Profile = App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC")
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGznHwe0NzpHSc3_1_JfC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").Type = 4
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGznHwe0NzpHSc3_1_F2UL1Kj9XgSFrcz_1_JfC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Plane", "plane_Sketch_Fb51YuRIUBzbo7s_1_JjC")
origin = App.Vector(0.00000000000000,-0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb51YuRIUBzbo7s_1_JjC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("Sketcher::SketchObject","Sketch_Fb51YuRIUBzbo7s_1_JjC")
App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb51YuRIUBzbo7s_1_JjC"), [""])
App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC").addGeometry(Part.LineSegment(App.Vector(-35.00000000000000,22.50000000000000,0.00000000000000),App.Vector(-25.00000000000000,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,22.50000000000000,0.00000000000000),App.Vector(-25.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-30.00000000000000,17.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,12.50000000000000,0.00000000000000),App.Vector(-35.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC").addGeometry(Part.LineSegment(App.Vector(-35.00000000000000,22.50000000000000,0.00000000000000),App.Vector(-35.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Pad","Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC")
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").Profile = App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC")
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb51YuRIUBzbo7s_1_JjC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").Type = 4
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb51YuRIUBzbo7s_1_FY4XFdLWc0BYIuA_1_JjC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Plane", "plane_Sketch_FiB5PrjPxKRqovn_1_JlC")
origin = App.Vector(0.00000000000000,-0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiB5PrjPxKRqovn_1_JlC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("Sketcher::SketchObject","Sketch_FiB5PrjPxKRqovn_1_JlC")
App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiB5PrjPxKRqovn_1_JlC"), [""])
App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-22.50000000000000,0.00000000000000),App.Vector(25.00000000000000,-22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,-22.50000000000000,0.00000000000000),App.Vector(25.00000000000000,-17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(30.00000000000000,-17.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(30.00000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-22.50000000000000,0.00000000000000),App.Vector(35.00000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FnyyVfIzMCZcsiL_0").newObject("PartDesign::Pocket","Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC")
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").Profile = App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC")
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiB5PrjPxKRqovn_1_JlC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").Type = 4
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiB5PrjPxKRqovn_1_FLh9BuHTrNCmg2u_1_JlC").Offset = 0
App.ActiveDocument.recompute()

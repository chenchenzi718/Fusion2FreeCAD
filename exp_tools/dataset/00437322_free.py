import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00437322")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fd8VMifuQp9ekng_0")
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").Label = "Body_Fd8VMifuQp9ekng_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_Fd8VMifuQp9ekng_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fd8VMifuQp9ekng_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_Fd8VMifuQp9ekng_0_JGC")
App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fd8VMifuQp9ekng_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,-4.50000000000000,0.00000000000000),App.Vector(-16.00000000000000,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,-4.50000000000000,0.00000000000000),App.Vector(-16.00000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,4.50000000000000,0.00000000000000),App.Vector(-16.00000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,-4.50000000000000,0.00000000000000),App.Vector(16.00000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pad","Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC")
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC")
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").Length = 8.0
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fd8VMifuQp9ekng_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fd8VMifuQp9ekng_0_F41TvNrhNCuGHIg_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_Fo2f4kHo3esuUMb_1_JJC")
origin = App.Vector(-0.00000000000000,4.00000000000000,4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fo2f4kHo3esuUMb_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_Fo2f4kHo3esuUMb_1_JJC")
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fo2f4kHo3esuUMb_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJC").addGeometry(Part.Circle(App.Vector(-12.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pad","Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC")
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJC")
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_Fo2f4kHo3esuUMb_1_JJG")
origin = App.Vector(-0.00000000000000,4.00000000000000,4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fo2f4kHo3esuUMb_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_Fo2f4kHo3esuUMb_1_JJG")
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fo2f4kHo3esuUMb_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJG").addGeometry(Part.Circle(App.Vector(-4.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pad","Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG")
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJG")
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_Fo2f4kHo3esuUMb_1_JJK")
origin = App.Vector(-0.00000000000000,4.00000000000000,4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fo2f4kHo3esuUMb_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_Fo2f4kHo3esuUMb_1_JJK")
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fo2f4kHo3esuUMb_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJK").addGeometry(Part.Circle(App.Vector(4.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pad","Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK")
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJK")
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_Fo2f4kHo3esuUMb_1_JJO")
origin = App.Vector(-0.00000000000000,4.00000000000000,4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fo2f4kHo3esuUMb_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_Fo2f4kHo3esuUMb_1_JJO")
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fo2f4kHo3esuUMb_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJO").addGeometry(Part.Circle(App.Vector(12.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pad","Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO")
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJO")
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fo2f4kHo3esuUMb_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fo2f4kHo3esuUMb_1_F8mIlKWFwYxwckw_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_FcIPT609C8k72wL_1_JNS")
origin = App.Vector(-0.00000000000000,4.00000000000000,-4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcIPT609C8k72wL_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_FcIPT609C8k72wL_1_JNS")
App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcIPT609C8k72wL_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").addGeometry(Part.LineSegment(App.Vector(14.50000000000000,-2.50000000000000,0.00000000000000),App.Vector(-14.50000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").addGeometry(Part.LineSegment(App.Vector(-14.50000000000000,-2.50000000000000,0.00000000000000),App.Vector(-14.50000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").addGeometry(Part.LineSegment(App.Vector(14.50000000000000,2.50000000000000,0.00000000000000),App.Vector(-14.50000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").addGeometry(Part.LineSegment(App.Vector(14.50000000000000,-2.50000000000000,0.00000000000000),App.Vector(14.50000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").addGeometry(Part.Circle(App.Vector(8.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").addGeometry(Part.Circle(App.Vector(-8.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pocket","Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS")
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS")
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").Length = 8.0
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcIPT609C8k72wL_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcIPT609C8k72wL_1_FTUmvVi85M8mtZi_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_FJwQhox7blpz8fy_1_JRC")
origin = App.Vector(-0.00000000000000,4.00000000000000,-4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJwQhox7blpz8fy_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_FJwQhox7blpz8fy_1_JRC")
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJwQhox7blpz8fy_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRC").addGeometry(Part.Circle(App.Vector(-12.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pocket","Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC")
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRC")
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_FJwQhox7blpz8fy_1_JRG")
origin = App.Vector(-0.00000000000000,4.00000000000000,-4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJwQhox7blpz8fy_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_FJwQhox7blpz8fy_1_JRG")
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJwQhox7blpz8fy_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRG").addGeometry(Part.Circle(App.Vector(-4.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pocket","Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG")
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRG")
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").Length = 10.0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_FJwQhox7blpz8fy_1_JRK")
origin = App.Vector(-0.00000000000000,4.00000000000000,-4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJwQhox7blpz8fy_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_FJwQhox7blpz8fy_1_JRK")
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJwQhox7blpz8fy_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRK").addGeometry(Part.Circle(App.Vector(4.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pocket","Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK")
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRK")
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").Length = 10.0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Plane", "plane_Sketch_FJwQhox7blpz8fy_1_JRO")
origin = App.Vector(-0.00000000000000,4.00000000000000,-4.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJwQhox7blpz8fy_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("Sketcher::SketchObject","Sketch_FJwQhox7blpz8fy_1_JRO")
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJwQhox7blpz8fy_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRO").addGeometry(Part.Circle(App.Vector(12.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd8VMifuQp9ekng_0").newObject("PartDesign::Pocket","Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO")
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRO")
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").Length = 10.0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJwQhox7blpz8fy_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJwQhox7blpz8fy_1_FIXtDOXhL1knKJv_1_JRO").Offset = 0
App.ActiveDocument.recompute()

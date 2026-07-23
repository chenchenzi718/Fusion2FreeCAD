import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00263112")
App.ActiveDocument.addObject("PartDesign::Body","Body_F7jdBWjrzL9dSEP_0")
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").Label = "Body_F7jdBWjrzL9dSEP_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Plane", "plane_Sketch_F7jdBWjrzL9dSEP_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7jdBWjrzL9dSEP_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("Sketcher::SketchObject","Sketch_F7jdBWjrzL9dSEP_0_JGC")
App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7jdBWjrzL9dSEP_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC").addGeometry(Part.LineSegment(App.Vector(32.87477000000000,45.57638000000000,0.00000000000000),App.Vector(-32.87477000000000,45.57638000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC").addGeometry(Part.LineSegment(App.Vector(-32.87477000000000,45.57638000000000,0.00000000000000),App.Vector(-32.87477000000000,-45.57638000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC").addGeometry(Part.LineSegment(App.Vector(32.87477000000000,-45.57638000000000,0.00000000000000),App.Vector(-32.87477000000000,-45.57638000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC").addGeometry(Part.LineSegment(App.Vector(32.87477000000000,45.57638000000000,0.00000000000000),App.Vector(32.87477000000000,-45.57638000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Pad","Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC")
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC")
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").Length = 50.0
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7jdBWjrzL9dSEP_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F7jdBWjrzL9dSEP_0_FcDJwnc7NGzazLo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Plane", "plane_Sketch_FJBvG0nrWySUR6e_1_JJC")
origin = App.Vector(0.00000000000000,-25.00000000000000,-1.78246000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJBvG0nrWySUR6e_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("Sketcher::SketchObject","Sketch_FJBvG0nrWySUR6e_1_JJC")
App.ActiveDocument.getObject("Sketch_FJBvG0nrWySUR6e_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJBvG0nrWySUR6e_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FJBvG0nrWySUR6e_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJBvG0nrWySUR6e_1_JJC").addGeometry(Part.LineSegment(App.Vector(-26.87477000000000,43.35884000000000,0.00000000000000),App.Vector(26.87477000000000,43.35884000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJBvG0nrWySUR6e_1_JJC").addGeometry(Part.LineSegment(App.Vector(26.87477000000000,43.35884000000000,0.00000000000000),App.Vector(0.00000000000000,4.78246000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJBvG0nrWySUR6e_1_JJC").addGeometry(Part.LineSegment(App.Vector(-26.87477000000000,43.35884000000000,0.00000000000000),App.Vector(0.00000000000000,4.78246000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJBvG0nrWySUR6e_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJBvG0nrWySUR6e_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Pocket","Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC")
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FJBvG0nrWySUR6e_1_JJC")
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJBvG0nrWySUR6e_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FJBvG0nrWySUR6e_1_FS8VnEnf7LY2e0O_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Plane", "plane_Sketch_F4f64uYtaz1b2U1_1_JNG")
origin = App.Vector(0.00000000000000,-25.00000000000000,-1.78246000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4f64uYtaz1b2U1_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("Sketcher::SketchObject","Sketch_F4f64uYtaz1b2U1_1_JNG")
App.ActiveDocument.getObject("Sketch_F4f64uYtaz1b2U1_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4f64uYtaz1b2U1_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F4f64uYtaz1b2U1_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4f64uYtaz1b2U1_1_JNG").addGeometry(Part.LineSegment(App.Vector(-26.87477000000000,-40.79392000000000,0.00000000000000),App.Vector(26.87477000000000,-40.79392000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4f64uYtaz1b2U1_1_JNG").addGeometry(Part.LineSegment(App.Vector(26.87477000000000,-40.79392000000000,0.00000000000000),App.Vector(0.00000000000000,-1.21754000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4f64uYtaz1b2U1_1_JNG").addGeometry(Part.LineSegment(App.Vector(-26.87477000000000,-40.79392000000000,0.00000000000000),App.Vector(0.00000000000000,-1.21754000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4f64uYtaz1b2U1_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4f64uYtaz1b2U1_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Pocket","Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG")
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F4f64uYtaz1b2U1_1_JNG")
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").Length = 100.0
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4f64uYtaz1b2U1_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").Type = 0
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").Midplane = 1
App.ActiveDocument.getObject("Extrude_F4f64uYtaz1b2U1_1_F9XkTLf7BeOkZj8_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Plane", "plane_Sketch_Fbmfc4NZtRfxfcl_1_JRC")
origin = App.Vector(0.00000000000000,-25.00000000000000,-1.78246000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fbmfc4NZtRfxfcl_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("Sketcher::SketchObject","Sketch_Fbmfc4NZtRfxfcl_1_JRC")
App.ActiveDocument.getObject("Sketch_Fbmfc4NZtRfxfcl_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fbmfc4NZtRfxfcl_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fbmfc4NZtRfxfcl_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fbmfc4NZtRfxfcl_1_JRC").addGeometry(Part.LineSegment(App.Vector(-26.87477000000000,37.35884000000000,0.00000000000000),App.Vector(-26.87477000000000,-34.79392000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fbmfc4NZtRfxfcl_1_JRC").addGeometry(Part.LineSegment(App.Vector(-26.87477000000000,-34.79392000000000,0.00000000000000),App.Vector(-3.00000000000000,1.78246000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fbmfc4NZtRfxfcl_1_JRC").addGeometry(Part.LineSegment(App.Vector(-26.87477000000000,37.35884000000000,0.00000000000000),App.Vector(-3.00000000000000,1.78246000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fbmfc4NZtRfxfcl_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fbmfc4NZtRfxfcl_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Pocket","Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC")
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fbmfc4NZtRfxfcl_1_JRC")
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").Length = 100.0
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fbmfc4NZtRfxfcl_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fbmfc4NZtRfxfcl_1_FS6EWc1hwRGjHTC_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Plane", "plane_Sketch_FzmGJItIj5hPFFN_1_JVO")
origin = App.Vector(0.00000000000000,-25.00000000000000,-1.78246000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzmGJItIj5hPFFN_1_JVO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("Sketcher::SketchObject","Sketch_FzmGJItIj5hPFFN_1_JVO")
App.ActiveDocument.getObject("Sketch_FzmGJItIj5hPFFN_1_JVO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzmGJItIj5hPFFN_1_JVO"), [""])
App.ActiveDocument.getObject("Sketch_FzmGJItIj5hPFFN_1_JVO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzmGJItIj5hPFFN_1_JVO").addGeometry(Part.LineSegment(App.Vector(26.87477000000000,37.35884000000000,0.00000000000000),App.Vector(26.87477000000000,-34.79392000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzmGJItIj5hPFFN_1_JVO").addGeometry(Part.LineSegment(App.Vector(26.87477000000000,-34.79392000000000,0.00000000000000),App.Vector(3.00000000000000,1.78246000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzmGJItIj5hPFFN_1_JVO").addGeometry(Part.LineSegment(App.Vector(26.87477000000000,37.35884000000000,0.00000000000000),App.Vector(3.00000000000000,1.78246000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzmGJItIj5hPFFN_1_JVO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzmGJItIj5hPFFN_1_JVO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Pocket","Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO")
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").Profile = App.ActiveDocument.getObject("Sketch_FzmGJItIj5hPFFN_1_JVO")
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").Length = 100.0
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzmGJItIj5hPFFN_1_JVO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").Type = 0
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").Midplane = 1
App.ActiveDocument.getObject("Extrude_FzmGJItIj5hPFFN_1_F5o3FNskyVHVgG7_1_JVO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Plane", "plane_Sketch_FdedqY7OQ4UOzBa_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,45.57638000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdedqY7OQ4UOzBa_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("Sketcher::SketchObject","Sketch_FdedqY7OQ4UOzBa_1_JZC")
App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdedqY7OQ4UOzBa_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC").addGeometry(Part.LineSegment(App.Vector(27.50000000000000,21.00000000000000,0.00000000000000),App.Vector(-27.50000000000000,21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC").addGeometry(Part.LineSegment(App.Vector(-27.50000000000000,21.00000000000000,0.00000000000000),App.Vector(-27.50000000000000,-21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC").addGeometry(Part.LineSegment(App.Vector(27.50000000000000,-21.00000000000000,0.00000000000000),App.Vector(-27.50000000000000,-21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC").addGeometry(Part.LineSegment(App.Vector(27.50000000000000,21.00000000000000,0.00000000000000),App.Vector(27.50000000000000,-21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Pocket","Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC")
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC")
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdedqY7OQ4UOzBa_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").Type = 0
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FdedqY7OQ4UOzBa_1_FXJ4HjHjjRdytRt_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Plane", "plane_Sketch_FNyyPt4Y3Fn1bvR_1_JdC")
origin = App.Vector(0.00000000000000,0.00000000000000,-45.57638000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNyyPt4Y3Fn1bvR_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("Sketcher::SketchObject","Sketch_FNyyPt4Y3Fn1bvR_1_JdC")
App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNyyPt4Y3Fn1bvR_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC").addGeometry(Part.LineSegment(App.Vector(27.50000000000000,21.00000000000000,0.00000000000000),App.Vector(-27.50000000000000,21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC").addGeometry(Part.LineSegment(App.Vector(-27.50000000000000,21.00000000000000,0.00000000000000),App.Vector(-27.50000000000000,-21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC").addGeometry(Part.LineSegment(App.Vector(27.50000000000000,-21.00000000000000,0.00000000000000),App.Vector(-27.50000000000000,-21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC").addGeometry(Part.LineSegment(App.Vector(27.50000000000000,21.00000000000000,0.00000000000000),App.Vector(27.50000000000000,-21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Pocket","Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC")
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC")
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNyyPt4Y3Fn1bvR_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").Type = 0
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FNyyPt4Y3Fn1bvR_1_FKpgTNCg1kI2pjG_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Plane", "plane_Sketch_F9uq5A8U04ToAgV_1_JhC")
origin = App.Vector(32.87477000000000,0.00000000000000,43.57638000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9uq5A8U04ToAgV_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("Sketcher::SketchObject","Sketch_F9uq5A8U04ToAgV_1_JhC")
App.ActiveDocument.getObject("Sketch_F9uq5A8U04ToAgV_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9uq5A8U04ToAgV_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_F9uq5A8U04ToAgV_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9uq5A8U04ToAgV_1_JhC").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,-6.66699000000000,0.00000000000000),App.Vector(19.00000000000000,-6.66699000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9uq5A8U04ToAgV_1_JhC").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,-6.66699000000000,0.00000000000000),App.Vector(0.00000000000000,-40.57637999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9uq5A8U04ToAgV_1_JhC").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,-6.66699000000000,0.00000000000000),App.Vector(0.00000000000000,-40.57637999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9uq5A8U04ToAgV_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9uq5A8U04ToAgV_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7jdBWjrzL9dSEP_0").newObject("PartDesign::Pocket","Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC")
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_F9uq5A8U04ToAgV_1_JhC")
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").Length = 200.0
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9uq5A8U04ToAgV_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").Type = 0
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F9uq5A8U04ToAgV_1_F8u7wvfwoncQWf2_1_JhC").Offset = 0
App.ActiveDocument.recompute()

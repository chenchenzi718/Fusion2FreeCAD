import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00966830")
App.ActiveDocument.addObject("PartDesign::Body","Body_FkqLpb4dcz82pKX_0")
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").Label = "Body_FkqLpb4dcz82pKX_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Plane", "plane_Sketch_FkqLpb4dcz82pKX_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkqLpb4dcz82pKX_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("Sketcher::SketchObject","Sketch_FkqLpb4dcz82pKX_0_JGC")
App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkqLpb4dcz82pKX_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").addGeometry(Part.LineSegment(App.Vector(-23.15000000000000,5.10000000000000,0.00000000000000),App.Vector(-23.15000000000000,-5.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").addGeometry(Part.LineSegment(App.Vector(-23.15000000000000,-5.10000000000000,0.00000000000000),App.Vector(-16.15000000000000,-5.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").addGeometry(Part.LineSegment(App.Vector(-11.85000000000000,-7.00000000000000,0.00000000000000),App.Vector(-16.15000000000000,-5.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").addGeometry(Part.LineSegment(App.Vector(23.15000000000000,-7.00000000000000,0.00000000000000),App.Vector(-11.85000000000000,-7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").addGeometry(Part.LineSegment(App.Vector(23.15000000000000,7.00000000000000,0.00000000000000),App.Vector(23.15000000000000,-7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").addGeometry(Part.LineSegment(App.Vector(23.15000000000000,7.00000000000000,0.00000000000000),App.Vector(-11.85000000000000,7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").addGeometry(Part.LineSegment(App.Vector(-11.85000000000000,7.00000000000000,0.00000000000000),App.Vector(-16.15000000000000,5.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").addGeometry(Part.LineSegment(App.Vector(-23.15000000000000,5.10000000000000,0.00000000000000),App.Vector(-16.15000000000000,5.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").addGeometry(Part.Circle(App.Vector(-14.15000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Pad","Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC")
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC")
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").Length = 1.6
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkqLpb4dcz82pKX_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkqLpb4dcz82pKX_0_FlxLXbRwm4kdmvK_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Plane", "plane_Sketch_FtqrIQst6YomX5J_1_JJC")
origin = App.Vector(3.50000000000000,0.00000000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtqrIQst6YomX5J_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("Sketcher::SketchObject","Sketch_FtqrIQst6YomX5J_1_JJC")
App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtqrIQst6YomX5J_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC").addGeometry(Part.LineSegment(App.Vector(-26.65000000000000,5.10000000000000,0.00000000000000),App.Vector(-19.65000000000000,5.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC").addGeometry(Part.LineSegment(App.Vector(-19.65000000000000,5.10000000000000,0.00000000000000),App.Vector(-19.65000000000000,-5.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC").addGeometry(Part.LineSegment(App.Vector(-26.65000000000000,-5.10000000000000,0.00000000000000),App.Vector(-19.65000000000000,-5.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC").addGeometry(Part.LineSegment(App.Vector(-26.65000000000000,5.10000000000000,0.00000000000000),App.Vector(-26.65000000000000,-5.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Pad","Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC")
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC")
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").Length = 8.5
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtqrIQst6YomX5J_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtqrIQst6YomX5J_1_F0H0R4KPAUpJIqw_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Plane", "plane_Sketch_FcMhnWEY4Wv0Omx_1_JNC")
origin = App.Vector(3.50000000000000,0.00000000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcMhnWEY4Wv0Omx_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("Sketcher::SketchObject","Sketch_FcMhnWEY4Wv0Omx_1_JNC")
App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcMhnWEY4Wv0Omx_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC").addGeometry(Part.LineSegment(App.Vector(-11.25000000000000,3.10000000000000,0.00000000000000),App.Vector(-5.05000000000000,3.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC").addGeometry(Part.LineSegment(App.Vector(-5.05000000000000,3.10000000000000,0.00000000000000),App.Vector(-5.05000000000000,-3.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC").addGeometry(Part.LineSegment(App.Vector(-11.25000000000000,-3.10000000000000,0.00000000000000),App.Vector(-5.05000000000000,-3.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC").addGeometry(Part.LineSegment(App.Vector(-11.25000000000000,3.10000000000000,0.00000000000000),App.Vector(-11.25000000000000,-3.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Pad","Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC")
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC")
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").Length = 5.4
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Plane", "plane_Sketch_FcMhnWEY4Wv0Omx_1_JNG")
origin = App.Vector(3.50000000000000,0.00000000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcMhnWEY4Wv0Omx_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("Sketcher::SketchObject","Sketch_FcMhnWEY4Wv0Omx_1_JNG")
App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcMhnWEY4Wv0Omx_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG").addGeometry(Part.LineSegment(App.Vector(4.35000000000000,3.10000000000000,0.00000000000000),App.Vector(10.55000000000000,3.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG").addGeometry(Part.LineSegment(App.Vector(10.55000000000000,3.10000000000000,0.00000000000000),App.Vector(10.55000000000000,-3.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG").addGeometry(Part.LineSegment(App.Vector(4.35000000000000,-3.10000000000000,0.00000000000000),App.Vector(10.55000000000000,-3.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG").addGeometry(Part.LineSegment(App.Vector(4.35000000000000,3.10000000000000,0.00000000000000),App.Vector(4.35000000000000,-3.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Pad","Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG")
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG")
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").Length = 5.4
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcMhnWEY4Wv0Omx_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcMhnWEY4Wv0Omx_1_Frx9pSiWlFzBbbz_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Plane", "plane_Sketch_FXfU1N4wwXr2NFq_1_JRC")
origin = App.Vector(-4.65000000000000,0.00000000000000,7.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXfU1N4wwXr2NFq_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("Sketcher::SketchObject","Sketch_FXfU1N4wwXr2NFq_1_JRC")
App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXfU1N4wwXr2NFq_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.72500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Pad","Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC")
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JRC")
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").Length = 0.6
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Plane", "plane_Sketch_FXfU1N4wwXr2NFq_1_JTC")
origin = App.Vector(10.95000000000000,-0.00000000000000,7.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXfU1N4wwXr2NFq_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("Sketcher::SketchObject","Sketch_FXfU1N4wwXr2NFq_1_JTC")
App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXfU1N4wwXr2NFq_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JTC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.72500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Pad","Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC")
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JTC")
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").Length = 0.6
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXfU1N4wwXr2NFq_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXfU1N4wwXr2NFq_1_FNSSAOs8DAA8hFa_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Plane", "plane_Sketch_FymPUj5lDow1Zwl_1_JXC")
origin = App.Vector(-5.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FymPUj5lDow1Zwl_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("Sketcher::SketchObject","Sketch_FymPUj5lDow1Zwl_1_JXC")
App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FymPUj5lDow1Zwl_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC").addGeometry(Part.LineSegment(App.Vector(28.15000000000000,7.00000000000000,0.00000000000000),App.Vector(28.35000000000000,7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC").addGeometry(Part.LineSegment(App.Vector(28.35000000000000,7.00000000000000,0.00000000000000),App.Vector(28.35000000000000,-7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC").addGeometry(Part.LineSegment(App.Vector(28.15000000000000,-7.00000000000000,0.00000000000000),App.Vector(28.35000000000000,-7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC").addGeometry(Part.LineSegment(App.Vector(28.15000000000000,-7.00000000000000,0.00000000000000),App.Vector(28.15000000000000,7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Pad","Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC")
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC")
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").Length = 1.5
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Plane", "plane_Sketch_FymPUj5lDow1Zwl_1_JXK")
origin = App.Vector(-5.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FymPUj5lDow1Zwl_1_JXK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("Sketcher::SketchObject","Sketch_FymPUj5lDow1Zwl_1_JXK")
App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FymPUj5lDow1Zwl_1_JXK"), [""])
App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK").addGeometry(Part.LineSegment(App.Vector(28.15000000000000,7.00000000000000,0.00000000000000),App.Vector(18.15000000000000,7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK").addGeometry(Part.LineSegment(App.Vector(18.15000000000000,7.00000000000000,0.00000000000000),App.Vector(18.15000000000000,-7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK").addGeometry(Part.LineSegment(App.Vector(28.15000000000000,-7.00000000000000,0.00000000000000),App.Vector(18.15000000000000,-7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK").addGeometry(Part.LineSegment(App.Vector(28.15000000000000,-7.00000000000000,0.00000000000000),App.Vector(28.15000000000000,7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkqLpb4dcz82pKX_0").newObject("PartDesign::Pad","Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK")
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").Profile = App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK")
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").Length = 1.5
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FymPUj5lDow1Zwl_1_JXK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").Type = 4
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FymPUj5lDow1Zwl_1_FD6sUJLlZ5G9Xqr_1_JXK").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00297336")
App.ActiveDocument.addObject("PartDesign::Body","Body_FfJLMACeuem1CvF_0")
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").Label = "Body_FfJLMACeuem1CvF_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Plane", "plane_Sketch_FfJLMACeuem1CvF_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfJLMACeuem1CvF_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("Sketcher::SketchObject","Sketch_FfJLMACeuem1CvF_0_JGC")
App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfJLMACeuem1CvF_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC").addGeometry(Part.LineSegment(App.Vector(72.50000000000000,40.00000000000000,0.00000000000000),App.Vector(-72.50000000000000,40.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC").addGeometry(Part.LineSegment(App.Vector(-72.50000000000000,40.00000000000000,0.00000000000000),App.Vector(-72.50000000000000,-40.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC").addGeometry(Part.LineSegment(App.Vector(72.50000000000000,-40.00000000000000,0.00000000000000),App.Vector(-72.50000000000000,-40.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC").addGeometry(Part.LineSegment(App.Vector(72.50000000000000,40.00000000000000,0.00000000000000),App.Vector(72.50000000000000,-40.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Pad","Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC")
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC")
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfJLMACeuem1CvF_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfJLMACeuem1CvF_0_FVQDmdr42kSvSVq_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Plane", "plane_Sketch_FMcmMQ4CEkl50kC_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcmMQ4CEkl50kC_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("Sketcher::SketchObject","Sketch_FMcmMQ4CEkl50kC_1_JJC")
App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcmMQ4CEkl50kC_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC").addGeometry(Part.LineSegment(App.Vector(70.50000000000000,38.00000000000000,0.00000000000000),App.Vector(-70.50000000000000,38.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC").addGeometry(Part.LineSegment(App.Vector(-70.50000000000000,38.00000000000000,0.00000000000000),App.Vector(-70.50000000000000,-38.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC").addGeometry(Part.LineSegment(App.Vector(70.50000000000000,-38.00000000000000,0.00000000000000),App.Vector(-70.50000000000000,-38.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC").addGeometry(Part.LineSegment(App.Vector(70.50000000000000,38.00000000000000,0.00000000000000),App.Vector(70.50000000000000,-38.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Pad","Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC")
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC")
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").Length = 1.0
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcmMQ4CEkl50kC_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcmMQ4CEkl50kC_1_FXFDWsCcDaoAQ1V_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Plane", "plane_Sketch_FMXde0xDu46kiSx_1_JNC")
origin = App.Vector(0.00000000000000,-2.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMXde0xDu46kiSx_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("Sketcher::SketchObject","Sketch_FMXde0xDu46kiSx_1_JNC")
App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMXde0xDu46kiSx_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC").addGeometry(Part.LineSegment(App.Vector(3.00000000000000,4.50000000000000,0.00000000000000),App.Vector(3.00000000000000,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,-4.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC").addGeometry(Part.LineSegment(App.Vector(-3.00000000000000,4.50000000000000,0.00000000000000),App.Vector(-3.00000000000000,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,4.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Pocket","Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC")
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC")
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMXde0xDu46kiSx_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMXde0xDu46kiSx_1_FIzS4S3xwG1eBNi_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Plane", "plane_Sketch_FOUm2Ff9hAXwxtg_1_JSC")
origin = App.Vector(0.00000000000000,-2.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("Sketcher::SketchObject","Sketch_FOUm2Ff9hAXwxtg_1_JSC")
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSC").addGeometry(Part.Circle(App.Vector(-6.50000000000000,16.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Pocket","Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSC")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").Type = 4
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Plane", "plane_Sketch_FOUm2Ff9hAXwxtg_1_JSG")
origin = App.Vector(0.00000000000000,-2.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("Sketcher::SketchObject","Sketch_FOUm2Ff9hAXwxtg_1_JSG")
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSG"), [""])
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSG").addGeometry(Part.Circle(App.Vector(6.50000000000000,16.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Pocket","Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").Profile = App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSG")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").Type = 4
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Plane", "plane_Sketch_FOUm2Ff9hAXwxtg_1_JSK")
origin = App.Vector(0.00000000000000,-2.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("Sketcher::SketchObject","Sketch_FOUm2Ff9hAXwxtg_1_JSK")
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSK"), [""])
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSK").addGeometry(Part.Circle(App.Vector(6.50000000000000,-7.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Pocket","Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").Profile = App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSK")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").Type = 4
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Plane", "plane_Sketch_FOUm2Ff9hAXwxtg_1_JSO")
origin = App.Vector(0.00000000000000,-2.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("Sketcher::SketchObject","Sketch_FOUm2Ff9hAXwxtg_1_JSO")
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSO"), [""])
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSO").addGeometry(Part.Circle(App.Vector(-6.50000000000000,-7.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Pocket","Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").Profile = App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSO")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").Type = 4
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Plane", "plane_Sketch_FOUm2Ff9hAXwxtg_1_JSS")
origin = App.Vector(0.00000000000000,-2.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("Sketcher::SketchObject","Sketch_FOUm2Ff9hAXwxtg_1_JSS")
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSS"), [""])
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSS").addGeometry(Part.Circle(App.Vector(-6.50000000000000,4.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Pocket","Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").Profile = App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSS")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").Type = 4
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Plane", "plane_Sketch_FOUm2Ff9hAXwxtg_1_JSW")
origin = App.Vector(0.00000000000000,-2.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("Sketcher::SketchObject","Sketch_FOUm2Ff9hAXwxtg_1_JSW")
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOUm2Ff9hAXwxtg_1_JSW"), [""])
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSW").addGeometry(Part.Circle(App.Vector(6.50000000000000,4.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfJLMACeuem1CvF_0").newObject("PartDesign::Pocket","Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").Profile = App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSW")
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOUm2Ff9hAXwxtg_1_JSW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").Type = 4
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOUm2Ff9hAXwxtg_1_FG4hSzpv3s7HF90_1_JSW").Offset = 0
App.ActiveDocument.recompute()

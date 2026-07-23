import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00385630")
App.ActiveDocument.addObject("PartDesign::Body","Body_FUIC4hKGdCuRwxh_0")
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").Label = "Body_FUIC4hKGdCuRwxh_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Plane", "plane_Sketch_FUIC4hKGdCuRwxh_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUIC4hKGdCuRwxh_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("Sketcher::SketchObject","Sketch_FUIC4hKGdCuRwxh_0_JGC")
App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUIC4hKGdCuRwxh_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC").addGeometry(Part.LineSegment(App.Vector(-66.39565000000000,139.69999999999999,0.00000000000000),App.Vector(670.20434999999998,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC").addGeometry(Part.LineSegment(App.Vector(670.20434999999998,139.69999999999999,0.00000000000000),App.Vector(670.20434999999998,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC").addGeometry(Part.LineSegment(App.Vector(-66.39565000000000,0.00000000000000,0.00000000000000),App.Vector(670.20434999999998,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC").addGeometry(Part.LineSegment(App.Vector(-66.39565000000000,139.69999999999999,0.00000000000000),App.Vector(-66.39565000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Pad","Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC")
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC")
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").Length = 19.05
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Plane", "plane_Sketch_FUIC4hKGdCuRwxh_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUIC4hKGdCuRwxh_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("Sketcher::SketchObject","Sketch_FUIC4hKGdCuRwxh_0_JGG")
App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUIC4hKGdCuRwxh_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG").addGeometry(Part.LineSegment(App.Vector(-66.39565000000000,0.00000000000000,0.00000000000000),App.Vector(670.20434999999998,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG").addGeometry(Part.LineSegment(App.Vector(670.20434999999998,0.00000000000000,0.00000000000000),App.Vector(670.20434999999998,-139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG").addGeometry(Part.LineSegment(App.Vector(-66.39565000000000,-139.69999999999999,0.00000000000000),App.Vector(670.20434999999998,-139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG").addGeometry(Part.LineSegment(App.Vector(-66.39565000000000,0.00000000000000,0.00000000000000),App.Vector(-66.39565000000000,-139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Pad","Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG")
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG")
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").Length = 19.05
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUIC4hKGdCuRwxh_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUIC4hKGdCuRwxh_0_Fgnt2MJEbJxoxdR_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Plane", "plane_Sketch_Fag1V4Hdzb1o77N_2_JJC")
origin = App.Vector(-48.41525000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fag1V4Hdzb1o77N_2_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("Sketcher::SketchObject","Sketch_Fag1V4Hdzb1o77N_2_JJC")
App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fag1V4Hdzb1o77N_2_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC").addGeometry(Part.LineSegment(App.Vector(17.98039000000000,-114.30000000000000,0.00000000000000),App.Vector(56.08039000000000,-114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC").addGeometry(Part.LineSegment(App.Vector(56.08039000000000,-114.30000000000000,0.00000000000000),App.Vector(56.08039000000000,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC").addGeometry(Part.LineSegment(App.Vector(17.98039000000000,114.30000000000000,0.00000000000000),App.Vector(56.08039000000000,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC").addGeometry(Part.LineSegment(App.Vector(17.98039000000000,-114.30000000000000,0.00000000000000),App.Vector(17.98039000000000,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Pad","Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC")
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC")
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").Length = 38.1
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Plane", "plane_Sketch_Fag1V4Hdzb1o77N_2_JJG")
origin = App.Vector(-48.41525000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fag1V4Hdzb1o77N_2_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("Sketcher::SketchObject","Sketch_Fag1V4Hdzb1o77N_2_JJG")
App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fag1V4Hdzb1o77N_2_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG").addGeometry(Part.LineSegment(App.Vector(644.55880999999999,-114.30000000000000,0.00000000000000),App.Vector(644.55880999999999,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG").addGeometry(Part.LineSegment(App.Vector(644.55880999999999,114.30000000000000,0.00000000000000),App.Vector(682.65881000000002,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG").addGeometry(Part.LineSegment(App.Vector(682.65881000000002,-114.30000000000000,0.00000000000000),App.Vector(682.65881000000002,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG").addGeometry(Part.LineSegment(App.Vector(644.55880999999999,-114.30000000000000,0.00000000000000),App.Vector(682.65881000000002,-114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Pad","Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG")
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG")
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").Length = 38.1
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fag1V4Hdzb1o77N_2_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fag1V4Hdzb1o77N_2_FoTQjL9DD4W3LGX_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Plane", "plane_Sketch_FFfjH9Kcidaylhs_1_JNC")
origin = App.Vector(-48.41525000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFfjH9Kcidaylhs_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("Sketcher::SketchObject","Sketch_FFfjH9Kcidaylhs_1_JNC")
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFfjH9Kcidaylhs_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC").addGeometry(Part.LineSegment(App.Vector(644.55880999999999,-114.30000000000000,0.00000000000000),App.Vector(682.65881000000002,-114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC").addGeometry(Part.LineSegment(App.Vector(682.65881000000002,-114.30000000000000,0.00000000000000),App.Vector(682.65881000000002,-139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC").addGeometry(Part.LineSegment(App.Vector(644.55880999999999,-139.69999999999999,0.00000000000000),App.Vector(682.65881000000002,-139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC").addGeometry(Part.LineSegment(App.Vector(644.55880999999999,-114.30000000000000,0.00000000000000),App.Vector(644.55880999999999,-139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Pad","Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC")
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC")
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").Length = 279.40000000000003
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Plane", "plane_Sketch_FFfjH9Kcidaylhs_1_JNG")
origin = App.Vector(-48.41525000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFfjH9Kcidaylhs_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("Sketcher::SketchObject","Sketch_FFfjH9Kcidaylhs_1_JNG")
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFfjH9Kcidaylhs_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG").addGeometry(Part.LineSegment(App.Vector(644.55880999999999,114.30000000000000,0.00000000000000),App.Vector(682.65881000000002,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG").addGeometry(Part.LineSegment(App.Vector(682.65881000000002,114.30000000000000,0.00000000000000),App.Vector(682.65881000000002,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG").addGeometry(Part.LineSegment(App.Vector(644.55880999999999,139.69999999999999,0.00000000000000),App.Vector(682.65881000000002,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG").addGeometry(Part.LineSegment(App.Vector(644.55880999999999,114.30000000000000,0.00000000000000),App.Vector(644.55880999999999,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Pad","Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG")
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG")
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").Length = 279.40000000000003
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Plane", "plane_Sketch_FFfjH9Kcidaylhs_1_JNK")
origin = App.Vector(-48.41525000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFfjH9Kcidaylhs_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("Sketcher::SketchObject","Sketch_FFfjH9Kcidaylhs_1_JNK")
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFfjH9Kcidaylhs_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK").addGeometry(Part.LineSegment(App.Vector(17.98039000000000,-114.30000000000000,0.00000000000000),App.Vector(56.08039000000000,-114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK").addGeometry(Part.LineSegment(App.Vector(56.08039000000000,-114.30000000000000,0.00000000000000),App.Vector(56.08039000000000,-139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK").addGeometry(Part.LineSegment(App.Vector(17.98039000000000,-139.69999999999999,0.00000000000000),App.Vector(56.08039000000000,-139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK").addGeometry(Part.LineSegment(App.Vector(17.98039000000000,-114.30000000000000,0.00000000000000),App.Vector(17.98039000000000,-139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Pad","Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK")
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK")
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").Length = 279.40000000000003
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Plane", "plane_Sketch_FFfjH9Kcidaylhs_1_JNO")
origin = App.Vector(-48.41525000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFfjH9Kcidaylhs_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("Sketcher::SketchObject","Sketch_FFfjH9Kcidaylhs_1_JNO")
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFfjH9Kcidaylhs_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO").addGeometry(Part.LineSegment(App.Vector(17.98039000000000,114.30000000000000,0.00000000000000),App.Vector(56.08039000000000,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO").addGeometry(Part.LineSegment(App.Vector(56.08039000000000,114.30000000000000,0.00000000000000),App.Vector(56.08039000000000,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO").addGeometry(Part.LineSegment(App.Vector(17.98039000000000,139.69999999999999,0.00000000000000),App.Vector(56.08039000000000,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO").addGeometry(Part.LineSegment(App.Vector(17.98039000000000,114.30000000000000,0.00000000000000),App.Vector(17.98039000000000,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIC4hKGdCuRwxh_0").newObject("PartDesign::Pad","Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO")
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO")
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").Length = 279.40000000000003
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFfjH9Kcidaylhs_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFfjH9Kcidaylhs_1_FNzRY3Zo4lrgFVW_1_JNO").Offset = 0
App.ActiveDocument.recompute()

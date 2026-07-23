import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00858127")
App.ActiveDocument.addObject("PartDesign::Body","Body_FlTpyZhIIbwlk4M_0")
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").Label = "Body_FlTpyZhIIbwlk4M_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Plane", "plane_Sketch_FlTpyZhIIbwlk4M_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlTpyZhIIbwlk4M_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("Sketcher::SketchObject","Sketch_FlTpyZhIIbwlk4M_0_JGC")
App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlTpyZhIIbwlk4M_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC").addGeometry(Part.LineSegment(App.Vector(-66.96008000000000,65.41608000000001,0.00000000000000),App.Vector(16.22015000000000,65.41608000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.22015000000000,65.41608000000001,0.00000000000000),App.Vector(16.22015000000000,-51.57191000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC").addGeometry(Part.LineSegment(App.Vector(-66.96008000000000,-51.57191000000000,0.00000000000000),App.Vector(16.22015000000000,-51.57191000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC").addGeometry(Part.LineSegment(App.Vector(-66.96008000000000,65.41608000000001,0.00000000000000),App.Vector(-66.96008000000000,-51.57191000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Pad","Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC")
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC")
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlTpyZhIIbwlk4M_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlTpyZhIIbwlk4M_0_FMKPErU381VrHvS_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Plane", "plane_Sketch_FhgsPke6tgRSk7L_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhgsPke6tgRSk7L_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("Sketcher::SketchObject","Sketch_FhgsPke6tgRSk7L_1_JJC")
App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhgsPke6tgRSk7L_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC").addGeometry(Part.LineSegment(App.Vector(-100.27575000000000,50.16005000000000,0.00000000000000),App.Vector(71.84732000000001,50.16005000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC").addGeometry(Part.LineSegment(App.Vector(71.84732000000001,50.16005000000000,0.00000000000000),App.Vector(71.84732000000001,-60.81033000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC").addGeometry(Part.LineSegment(App.Vector(-100.27575000000000,-60.81033000000000,0.00000000000000),App.Vector(71.84732000000001,-60.81033000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC").addGeometry(Part.LineSegment(App.Vector(-100.27575000000000,50.16005000000000,0.00000000000000),App.Vector(-100.27575000000000,-60.81033000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Pad","Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC")
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC")
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhgsPke6tgRSk7L_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhgsPke6tgRSk7L_1_FYDusF0enLgGa8k_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Plane", "plane_Sketch_Fs4rOfj3n1fLoS2_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fs4rOfj3n1fLoS2_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("Sketcher::SketchObject","Sketch_Fs4rOfj3n1fLoS2_1_JNC")
App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fs4rOfj3n1fLoS2_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC").addGeometry(Part.LineSegment(App.Vector(-89.56500000000001,-30.41748000000000,0.00000000000000),App.Vector(27.13364000000000,-30.41748000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC").addGeometry(Part.LineSegment(App.Vector(27.13364000000000,-30.41748000000000,0.00000000000000),App.Vector(27.13364000000000,-61.08182000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC").addGeometry(Part.LineSegment(App.Vector(-89.56500000000001,-61.08182000000000,0.00000000000000),App.Vector(27.13364000000000,-61.08182000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC").addGeometry(Part.LineSegment(App.Vector(-89.56500000000001,-30.41748000000000,0.00000000000000),App.Vector(-89.56500000000001,-61.08182000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Pad","Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC")
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC")
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fs4rOfj3n1fLoS2_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fs4rOfj3n1fLoS2_1_FxGwZYb2uugp8f1_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Plane", "plane_Sketch_FhpNbuJdZwGe6Te_1_JRC")
origin = App.Vector(-14.21422000000000,-5.32514000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhpNbuJdZwGe6Te_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("Sketcher::SketchObject","Sketch_FhpNbuJdZwGe6Te_1_JRC")
App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhpNbuJdZwGe6Te_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC").addGeometry(Part.LineSegment(App.Vector(-56.30366000000001,12.26107000000000,0.00000000000000),App.Vector(14.21422000000000,12.26107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC").addGeometry(Part.LineSegment(App.Vector(14.21422000000000,-26.65818000000001,0.00000000000000),App.Vector(14.21422000000000,12.26107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC").addGeometry(Part.LineSegment(App.Vector(-56.30366000000001,-26.65818000000001,0.00000000000000),App.Vector(14.21422000000000,-26.65818000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC").addGeometry(Part.LineSegment(App.Vector(-56.30366000000001,12.26107000000000,0.00000000000000),App.Vector(-56.30366000000001,-26.65818000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Pad","Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC")
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC")
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Plane", "plane_Sketch_FhpNbuJdZwGe6Te_1_JRG")
origin = App.Vector(-14.21422000000000,-5.32514000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhpNbuJdZwGe6Te_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("Sketcher::SketchObject","Sketch_FhpNbuJdZwGe6Te_1_JRG")
App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhpNbuJdZwGe6Te_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG").addGeometry(Part.LineSegment(App.Vector(77.58234999999999,12.26107000000000,0.00000000000000),App.Vector(39.61422000000000,12.26107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG").addGeometry(Part.LineSegment(App.Vector(39.61422000000000,-26.65818000000001,0.00000000000000),App.Vector(39.61422000000000,12.26107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG").addGeometry(Part.LineSegment(App.Vector(77.58234999999999,-26.65818000000001,0.00000000000000),App.Vector(39.61422000000000,-26.65818000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG").addGeometry(Part.LineSegment(App.Vector(77.58234999999999,12.26107000000000,0.00000000000000),App.Vector(77.58234999999999,-26.65818000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Pad","Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG")
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG")
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Plane", "plane_Sketch_FhpNbuJdZwGe6Te_1_JRO")
origin = App.Vector(-14.21422000000000,-5.32514000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhpNbuJdZwGe6Te_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("Sketcher::SketchObject","Sketch_FhpNbuJdZwGe6Te_1_JRO")
App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhpNbuJdZwGe6Te_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO").addGeometry(Part.LineSegment(App.Vector(14.21422000000000,12.26107000000000,0.00000000000000),App.Vector(39.61422000000000,12.26107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO").addGeometry(Part.LineSegment(App.Vector(39.61422000000000,-26.65818000000001,0.00000000000000),App.Vector(39.61422000000000,12.26107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO").addGeometry(Part.LineSegment(App.Vector(14.21422000000000,-26.65818000000001,0.00000000000000),App.Vector(39.61422000000000,-26.65818000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO").addGeometry(Part.LineSegment(App.Vector(14.21422000000000,-26.65818000000001,0.00000000000000),App.Vector(14.21422000000000,12.26107000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Pad","Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO")
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO")
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhpNbuJdZwGe6Te_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhpNbuJdZwGe6Te_1_F7TdguOHmpqJawb_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Plane", "plane_Sketch_F9bSlfkacBdocn9_1_JVC")
origin = App.Vector(-71.60305000000000,-60.81033000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9bSlfkacBdocn9_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("Sketcher::SketchObject","Sketch_F9bSlfkacBdocn9_1_JVC")
App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9bSlfkacBdocn9_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC").addGeometry(Part.LineSegment(App.Vector(28.67270000000000,24.28177000000000,0.00000000000000),App.Vector(57.96742000000000,24.28177000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC").addGeometry(Part.LineSegment(App.Vector(57.96742000000000,24.28177000000000,0.00000000000000),App.Vector(57.96742000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC").addGeometry(Part.LineSegment(App.Vector(28.67270000000000,12.70000000000000,0.00000000000000),App.Vector(57.96742000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC").addGeometry(Part.LineSegment(App.Vector(28.67270000000000,24.28177000000000,0.00000000000000),App.Vector(28.67270000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Pad","Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC")
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC")
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Plane", "plane_Sketch_F9bSlfkacBdocn9_1_JVG")
origin = App.Vector(-71.60305000000000,-60.81033000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9bSlfkacBdocn9_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("Sketcher::SketchObject","Sketch_F9bSlfkacBdocn9_1_JVG")
App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9bSlfkacBdocn9_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG").addGeometry(Part.LineSegment(App.Vector(28.67270000000000,-93.08479000000000,0.00000000000000),App.Vector(57.96742000000000,-93.08479000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG").addGeometry(Part.LineSegment(App.Vector(57.96742000000000,-93.08479000000000,0.00000000000000),App.Vector(57.96742000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG").addGeometry(Part.LineSegment(App.Vector(28.67270000000000,-12.70000000000000,0.00000000000000),App.Vector(57.96742000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG").addGeometry(Part.LineSegment(App.Vector(28.67270000000000,-93.08479000000000,0.00000000000000),App.Vector(28.67270000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Pad","Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG")
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG")
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Plane", "plane_Sketch_F9bSlfkacBdocn9_1_JVS")
origin = App.Vector(-71.60305000000000,-60.81033000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9bSlfkacBdocn9_1_JVS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("Sketcher::SketchObject","Sketch_F9bSlfkacBdocn9_1_JVS")
App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9bSlfkacBdocn9_1_JVS"), [""])
App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS").addGeometry(Part.LineSegment(App.Vector(28.67270000000000,12.70000000000000,0.00000000000000),App.Vector(28.67270000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS").addGeometry(Part.LineSegment(App.Vector(28.67270000000000,-12.70000000000000,0.00000000000000),App.Vector(57.96742000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS").addGeometry(Part.LineSegment(App.Vector(57.96742000000000,12.70000000000000,0.00000000000000),App.Vector(57.96742000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS").addGeometry(Part.LineSegment(App.Vector(28.67270000000000,12.70000000000000,0.00000000000000),App.Vector(57.96742000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlTpyZhIIbwlk4M_0").newObject("PartDesign::Pad","Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS")
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").Profile = App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS")
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9bSlfkacBdocn9_1_JVS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").Type = 4
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9bSlfkacBdocn9_1_Fh0HpKTDVTmjtKu_1_JVS").Offset = 0
App.ActiveDocument.recompute()

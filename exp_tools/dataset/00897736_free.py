import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00897736")
App.ActiveDocument.addObject("PartDesign::Body","Body_F33Ld9jJmFm0iah_0")
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").Label = "Body_F33Ld9jJmFm0iah_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Plane", "plane_Sketch_F33Ld9jJmFm0iah_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F33Ld9jJmFm0iah_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("Sketcher::SketchObject","Sketch_F33Ld9jJmFm0iah_0_JGC")
App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F33Ld9jJmFm0iah_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-31.56254000000000,10.88484000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").addGeometry(Part.LineSegment(App.Vector(-31.56254000000000,10.88484000000000,0.00000000000000),App.Vector(-45.91474000000000,-17.53948000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.91474000000000,-17.53948000000000,0.00000000000000),App.Vector(29.66591000000000,-17.53948000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").addGeometry(Part.LineSegment(App.Vector(10.43074000000000,5.98077000000000,0.00000000000000),App.Vector(29.66591000000000,-17.53948000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").addGeometry(Part.LineSegment(App.Vector(2.06256000000000,5.98077000000000,0.00000000000000),App.Vector(10.43074000000000,5.98077000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2.06256000000000,5.98077000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Pad","Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC")
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC")
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").Length = 140.0
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F33Ld9jJmFm0iah_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F33Ld9jJmFm0iah_0_FiZXUGq6Kd6NPsg_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Plane", "plane_Sketch_Fq9ljJGrEkQAubo_1_JJG")
origin = App.Vector(-15.78127000000000,-70.00000000000000,5.44242000000000)
x_axis=App.Vector(0.94536184000000,0.00000000000000,-0.32602299000000)
y_axis=App.Vector(-0.00000000000000,0.99999999853673,0.00000000000000)
z_axis=App.Vector(0.32602299000000,0.00000000000000,0.94536184000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq9ljJGrEkQAubo_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("Sketcher::SketchObject","Sketch_Fq9ljJGrEkQAubo_1_JJG")
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq9ljJGrEkQAubo_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJG").addGeometry(Part.Circle(App.Vector(-6.69337240904250,59.99999991220355,-0.00000347927380),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Pocket","Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG")
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJG")
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").Length = 30.0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Plane", "plane_Sketch_Fq9ljJGrEkQAubo_1_JJK")
origin = App.Vector(-15.78127000000000,-70.00000000000000,5.44242000000000)
x_axis=App.Vector(0.94536184000000,0.00000000000000,-0.32602299000000)
y_axis=App.Vector(-0.00000000000000,0.99999999853673,0.00000000000000)
z_axis=App.Vector(0.32602299000000,0.00000000000000,0.94536184000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq9ljJGrEkQAubo_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("Sketcher::SketchObject","Sketch_Fq9ljJGrEkQAubo_1_JJK")
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq9ljJGrEkQAubo_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJK").addGeometry(Part.Circle(App.Vector(-11.69337480443170,19.99999997073452,0.00000103398510),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Pocket","Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK")
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJK")
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").Length = 30.0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Plane", "plane_Sketch_Fq9ljJGrEkQAubo_1_JJC")
origin = App.Vector(-15.78127000000000,-70.00000000000000,5.44242000000000)
x_axis=App.Vector(0.94536184000000,0.00000000000000,-0.32602299000000)
y_axis=App.Vector(-0.00000000000000,0.99999999853673,0.00000000000000)
z_axis=App.Vector(0.32602299000000,0.00000000000000,0.94536184000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq9ljJGrEkQAubo_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("Sketcher::SketchObject","Sketch_Fq9ljJGrEkQAubo_1_JJC")
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq9ljJGrEkQAubo_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJC").addGeometry(Part.Circle(App.Vector(-6.69337240904250,-59.99999991220354,-0.00000347927380),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Pocket","Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC")
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJC")
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").Length = 30.0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Plane", "plane_Sketch_Fq9ljJGrEkQAubo_1_JJO")
origin = App.Vector(-15.78127000000000,-70.00000000000000,5.44242000000000)
x_axis=App.Vector(0.94536184000000,0.00000000000000,-0.32602299000000)
y_axis=App.Vector(-0.00000000000000,0.99999999853673,0.00000000000000)
z_axis=App.Vector(0.32602299000000,0.00000000000000,0.94536184000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq9ljJGrEkQAubo_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("Sketcher::SketchObject","Sketch_Fq9ljJGrEkQAubo_1_JJO")
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq9ljJGrEkQAubo_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJO").addGeometry(Part.Circle(App.Vector(-1.69337327388320,-19.99999997073450,0.00000146108570),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Pocket","Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO")
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJO")
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").Length = 30.0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq9ljJGrEkQAubo_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq9ljJGrEkQAubo_1_FPyzC0fJpPBJuPj_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Plane", "plane_Sketch_FIaiHuTsAsY6v8S_1_JNW")
origin = App.Vector(-15.78127000000000,-70.00000000000000,5.44242000000000)
x_axis=App.Vector(0.94536184000000,0.00000000000000,-0.32602299000000)
y_axis=App.Vector(-0.00000000000000,0.99999999853673,0.00000000000000)
z_axis=App.Vector(0.32602299000000,0.00000000000000,0.94536184000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIaiHuTsAsY6v8S_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("Sketcher::SketchObject","Sketch_FIaiHuTsAsY6v8S_1_JNW")
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIaiHuTsAsY6v8S_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNW").addGeometry(Part.Circle(App.Vector(-6.69337240904250,59.99999991220355,-0.00000347927380),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),4.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNW").addGeometry(Part.Circle(App.Vector(-6.69337240904250,59.99999991220355,-0.00000347927380),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Pad","Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW")
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNW")
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").Length = 10.0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").Type = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").Reversed = 1
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Plane", "plane_Sketch_FIaiHuTsAsY6v8S_1_JNS")
origin = App.Vector(-15.78127000000000,-70.00000000000000,5.44242000000000)
x_axis=App.Vector(0.94536184000000,0.00000000000000,-0.32602299000000)
y_axis=App.Vector(-0.00000000000000,0.99999999853673,0.00000000000000)
z_axis=App.Vector(0.32602299000000,0.00000000000000,0.94536184000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIaiHuTsAsY6v8S_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("Sketcher::SketchObject","Sketch_FIaiHuTsAsY6v8S_1_JNS")
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIaiHuTsAsY6v8S_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNS").addGeometry(Part.Circle(App.Vector(-6.69337240904250,-59.99999991220354,-0.00000347927380),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),4.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNS").addGeometry(Part.Circle(App.Vector(-6.69337240904250,-59.99999991220354,-0.00000347927380),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Pad","Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS")
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNS")
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").Length = 10.0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").Type = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").Reversed = 1
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Plane", "plane_Sketch_FIaiHuTsAsY6v8S_1_JNa")
origin = App.Vector(-15.78127000000000,-70.00000000000000,5.44242000000000)
x_axis=App.Vector(0.94536184000000,0.00000000000000,-0.32602299000000)
y_axis=App.Vector(-0.00000000000000,0.99999999853673,0.00000000000000)
z_axis=App.Vector(0.32602299000000,0.00000000000000,0.94536184000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIaiHuTsAsY6v8S_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("Sketcher::SketchObject","Sketch_FIaiHuTsAsY6v8S_1_JNa")
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIaiHuTsAsY6v8S_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNa").addGeometry(Part.Circle(App.Vector(-11.69337480443170,19.99999997073452,0.00000103398510),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),4.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNa").addGeometry(Part.Circle(App.Vector(-11.69337480443170,19.99999997073452,0.00000103398510),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Pad","Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa")
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNa")
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").Length = 10.0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").Type = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").Reversed = 1
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Plane", "plane_Sketch_FIaiHuTsAsY6v8S_1_JNe")
origin = App.Vector(-15.78127000000000,-70.00000000000000,5.44242000000000)
x_axis=App.Vector(0.94536184000000,0.00000000000000,-0.32602299000000)
y_axis=App.Vector(-0.00000000000000,0.99999999853673,0.00000000000000)
z_axis=App.Vector(0.32602299000000,0.00000000000000,0.94536184000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIaiHuTsAsY6v8S_1_JNe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("Sketcher::SketchObject","Sketch_FIaiHuTsAsY6v8S_1_JNe")
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIaiHuTsAsY6v8S_1_JNe"), [""])
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNe").addGeometry(Part.Circle(App.Vector(-1.69337327388320,-19.99999997073450,0.00000146108570),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),4.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNe").addGeometry(Part.Circle(App.Vector(-1.69337327388320,-19.99999997073450,0.00000146108570),App.Vector(-0.00000000000000,0.00000000000000,0.99999999853673),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F33Ld9jJmFm0iah_0").newObject("PartDesign::Pad","Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe")
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").Profile = App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNe")
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").Length = 10.0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIaiHuTsAsY6v8S_1_JNe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").Type = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").Reversed = 1
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIaiHuTsAsY6v8S_1_FDqxsy9xB1Jo0n6_1_JNe").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00195000")
App.ActiveDocument.addObject("PartDesign::Body","Body_FXLxL5lC615wbzm_0")
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").Label = "Body_FXLxL5lC615wbzm_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Plane", "plane_Sketch_FXLxL5lC615wbzm_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXLxL5lC615wbzm_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("Sketcher::SketchObject","Sketch_FXLxL5lC615wbzm_0_JGC")
App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXLxL5lC615wbzm_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,-100.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-100.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,-100.00000000000000,0.00000000000000),App.Vector(100.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Pad","Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC")
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC")
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXLxL5lC615wbzm_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXLxL5lC615wbzm_0_FuYT4NYD5dvzgAr_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Plane", "plane_Sketch_FWuVGk8zlqWKuPk_1_JKC")
origin = App.Vector(100.00000000000000,-50.00000000000000,50.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWuVGk8zlqWKuPk_1_JKC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("Sketcher::SketchObject","Sketch_FWuVGk8zlqWKuPk_1_JKC")
App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWuVGk8zlqWKuPk_1_JKC"), [""])
App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKC").addGeometry(Part.LineSegment(App.Vector(-39.99999999999999,-50.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,-40.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,-40.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(-39.99999999999999,-50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Pocket","Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC")
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").Profile = App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKC")
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").Type = 4
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Plane", "plane_Sketch_FWuVGk8zlqWKuPk_1_JKG")
origin = App.Vector(100.00000000000000,-50.00000000000000,50.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWuVGk8zlqWKuPk_1_JKG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("Sketcher::SketchObject","Sketch_FWuVGk8zlqWKuPk_1_JKG")
App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWuVGk8zlqWKuPk_1_JKG"), [""])
App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").addGeometry(Part.LineSegment(App.Vector(-39.99999999999999,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,35.00000000000000,0.00000000000000),App.Vector(15.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,50.00000000000000,0.00000000000000),App.Vector(15.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,50.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-39.99999999999999,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Pocket","Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG")
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").Profile = App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG")
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").Length = 100.0
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").Type = 4
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Plane", "plane_Sketch_FWuVGk8zlqWKuPk_1_JKO")
origin = App.Vector(100.00000000000000,-50.00000000000000,50.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWuVGk8zlqWKuPk_1_JKO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("Sketcher::SketchObject","Sketch_FWuVGk8zlqWKuPk_1_JKO")
App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWuVGk8zlqWKuPk_1_JKO"), [""])
App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,-40.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,50.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,50.00000000000000,0.00000000000000),App.Vector(15.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(15.00000000000000,50.00000000000000,0.00000000000000),App.Vector(15.00000000000000,80.03269999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(15.00000000000000,80.03269999999999,0.00000000000000),App.Vector(-98.71992999999999,80.03269999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(-98.71992999999999,80.03269999999999,0.00000000000000),App.Vector(-98.71992999999999,-55.63025000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(-98.71992999999999,-55.63025000000000,0.00000000000000),App.Vector(-38.57602000000000,-55.63025000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(-39.99999999999999,-50.00000000000000,0.00000000000000),App.Vector(-38.57602000000000,-55.63025000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(-39.99999999999999,-50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,-40.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Pocket","Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO")
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").Profile = App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO")
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").Length = 100.0
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWuVGk8zlqWKuPk_1_JKO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").Type = 4
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWuVGk8zlqWKuPk_1_FpcivITIyq0fO23_1_JKO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Plane", "plane_Sketch_F1pcb8Ebed1HmBF_1_JOC")
origin = App.Vector(100.00000000000000,-50.00000000000000,50.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1pcb8Ebed1HmBF_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("Sketcher::SketchObject","Sketch_F1pcb8Ebed1HmBF_1_JOC")
App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1pcb8Ebed1HmBF_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOC").addGeometry(Part.Circle(App.Vector(25.00000000000000,9.99999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Pocket","Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC")
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOC")
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").Length = 30.0
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Plane", "plane_Sketch_F1pcb8Ebed1HmBF_1_JOG")
origin = App.Vector(100.00000000000000,-50.00000000000000,50.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1pcb8Ebed1HmBF_1_JOG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("Sketcher::SketchObject","Sketch_F1pcb8Ebed1HmBF_1_JOG")
App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1pcb8Ebed1HmBF_1_JOG"), [""])
App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOG").addGeometry(Part.Circle(App.Vector(25.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Pocket","Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG")
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").Profile = App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOG")
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").Length = 30.0
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1pcb8Ebed1HmBF_1_JOG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").Type = 4
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1pcb8Ebed1HmBF_1_F7Sns5EoFpcqORj_1_JOG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Plane", "plane_Sketch_FaeTFYhcWUbmoKc_1_JSC")
origin = App.Vector(50.00000000000000,-70.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaeTFYhcWUbmoKc_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("Sketcher::SketchObject","Sketch_FaeTFYhcWUbmoKc_1_JSC")
App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaeTFYhcWUbmoKc_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-20.00000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-20.00000000000000,-4.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,-4.99999999999999,0.00000000000000),App.Vector(-20.00000000000000,-4.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,-4.99999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Pocket","Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC")
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC")
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").Type = 4
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Plane", "plane_Sketch_FaeTFYhcWUbmoKc_1_JSG")
origin = App.Vector(50.00000000000000,-70.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaeTFYhcWUbmoKc_1_JSG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("Sketcher::SketchObject","Sketch_FaeTFYhcWUbmoKc_1_JSG")
App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaeTFYhcWUbmoKc_1_JSG"), [""])
App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,-4.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,-4.99999999999999,0.00000000000000),App.Vector(5.00000000000000,-4.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-4.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Pocket","Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG")
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").Profile = App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG")
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").Length = 50.0
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").Type = 4
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Plane", "plane_Sketch_FaeTFYhcWUbmoKc_1_JSK")
origin = App.Vector(50.00000000000000,-70.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaeTFYhcWUbmoKc_1_JSK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("Sketcher::SketchObject","Sketch_FaeTFYhcWUbmoKc_1_JSK")
App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaeTFYhcWUbmoKc_1_JSK"), [""])
App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,5.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-4.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-4.99999999999999,0.00000000000000),App.Vector(30.00000000000000,-4.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,5.00000000000000,0.00000000000000),App.Vector(30.00000000000000,-4.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,5.00000000000000,0.00000000000000),App.Vector(30.00000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLxL5lC615wbzm_0").newObject("PartDesign::Pocket","Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK")
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").Profile = App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK")
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").Length = 50.0
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaeTFYhcWUbmoKc_1_JSK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").Type = 4
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaeTFYhcWUbmoKc_1_FCUieS6ilPnB79Y_1_JSK").Offset = 0
App.ActiveDocument.recompute()

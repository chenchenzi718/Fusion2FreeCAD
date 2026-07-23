import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00764486")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fp868pKgWlrUQly_0")
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").Label = "Body_Fp868pKgWlrUQly_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_Fp868pKgWlrUQly_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fp868pKgWlrUQly_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_Fp868pKgWlrUQly_0_JGC")
App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fp868pKgWlrUQly_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,75.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,75.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,-75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,-75.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,-75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,75.00000000000000,0.00000000000000),App.Vector(25.00000000000000,-75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pad","Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC")
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC")
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").Length = 15.0
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fp868pKgWlrUQly_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fp868pKgWlrUQly_0_F8iphP35Y20tpHQ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_F1u15JspK2PLBsz_1_JLC")
origin = App.Vector(0.00000000000000,0.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1u15JspK2PLBsz_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_F1u15JspK2PLBsz_1_JLC")
App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1u15JspK2PLBsz_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLC").addGeometry(Part.Circle(App.Vector(0.00000000000000,40.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pocket","Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC")
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLC")
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_F1u15JspK2PLBsz_1_JLG")
origin = App.Vector(0.00000000000000,0.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1u15JspK2PLBsz_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_F1u15JspK2PLBsz_1_JLG")
App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1u15JspK2PLBsz_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLG").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pocket","Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG")
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLG")
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").Length = 25.0
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_F1u15JspK2PLBsz_1_JLK")
origin = App.Vector(0.00000000000000,0.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1u15JspK2PLBsz_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_F1u15JspK2PLBsz_1_JLK")
App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1u15JspK2PLBsz_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLK").addGeometry(Part.Circle(App.Vector(0.00000000000000,-40.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pocket","Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK")
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLK")
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").Length = 25.0
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1u15JspK2PLBsz_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1u15JspK2PLBsz_1_Ft8MwXphadgfYDS_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_FqESyU5b4x88coI_1_JRC")
origin = App.Vector(25.00000000000000,0.00000000000000,7.50000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqESyU5b4x88coI_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_FqESyU5b4x88coI_1_JRC")
App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqESyU5b4x88coI_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRC").addGeometry(Part.Circle(App.Vector(-40.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pad","Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC")
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRC")
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_FqESyU5b4x88coI_1_JRG")
origin = App.Vector(25.00000000000000,0.00000000000000,7.50000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqESyU5b4x88coI_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_FqESyU5b4x88coI_1_JRG")
App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqESyU5b4x88coI_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRG").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pad","Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG")
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRG")
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").Length = 10.0
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_FqESyU5b4x88coI_1_JRK")
origin = App.Vector(25.00000000000000,0.00000000000000,7.50000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqESyU5b4x88coI_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_FqESyU5b4x88coI_1_JRK")
App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqESyU5b4x88coI_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRK").addGeometry(Part.Circle(App.Vector(40.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pad","Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK")
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRK")
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").Length = 10.0
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqESyU5b4x88coI_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqESyU5b4x88coI_1_FdAwf1HD0hvS73a_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_FiiotrankpRAeXH_1_JXC")
origin = App.Vector(-25.00000000000000,0.00000000000000,7.50000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiiotrankpRAeXH_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_FiiotrankpRAeXH_1_JXC")
App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiiotrankpRAeXH_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXC").addGeometry(Part.Circle(App.Vector(-40.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pocket","Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC")
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXC")
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").Length = 10.2
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_FiiotrankpRAeXH_1_JXK")
origin = App.Vector(-25.00000000000000,0.00000000000000,7.50000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiiotrankpRAeXH_1_JXK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_FiiotrankpRAeXH_1_JXK")
App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiiotrankpRAeXH_1_JXK"), [""])
App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXK").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pocket","Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK")
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").Profile = App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXK")
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").Length = 10.2
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").Type = 4
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Plane", "plane_Sketch_FiiotrankpRAeXH_1_JXG")
origin = App.Vector(-25.00000000000000,0.00000000000000,7.50000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiiotrankpRAeXH_1_JXG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("Sketcher::SketchObject","Sketch_FiiotrankpRAeXH_1_JXG")
App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiiotrankpRAeXH_1_JXG"), [""])
App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXG").addGeometry(Part.Circle(App.Vector(40.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fp868pKgWlrUQly_0").newObject("PartDesign::Pocket","Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG")
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").Profile = App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXG")
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").Length = 10.2
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiiotrankpRAeXH_1_JXG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").Type = 4
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiiotrankpRAeXH_1_F7Ercdcgt7XPHCU_1_JXG").Offset = 0
App.ActiveDocument.recompute()

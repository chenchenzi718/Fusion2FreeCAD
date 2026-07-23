import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00117331")
App.ActiveDocument.addObject("PartDesign::Body","Body_FrVvZHux1ccAEAm_0")
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").Label = "Body_FrVvZHux1ccAEAm_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Plane", "plane_Sketch_FrVvZHux1ccAEAm_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrVvZHux1ccAEAm_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("Sketcher::SketchObject","Sketch_FrVvZHux1ccAEAm_0_JGC")
App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrVvZHux1ccAEAm_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-78.73931000000000,2.00000000000000,0.00000000000000),App.Vector(-8.73931000000000,2.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-8.73931000000000,2.00000000000000,0.00000000000000),App.Vector(-8.73931000000000,3.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-8.73931000000000,3.50000000000000,0.00000000000000),App.Vector(81.26069000000000,3.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").addGeometry(Part.LineSegment(App.Vector(81.26069000000000,0.00000000000000,0.00000000000000),App.Vector(81.26069000000000,3.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-8.73931000000000,0.00000000000000,0.00000000000000),App.Vector(81.26069000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-78.73931000000000,0.00000000000000,0.00000000000000),App.Vector(-8.73931000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-78.73931000000000,0.00000000000000,0.00000000000000),App.Vector(-88.26559000000000,5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-87.39956000000001,7.00000000000000,0.00000000000000),App.Vector(-88.26559000000000,5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-78.73931000000000,2.00000000000000,0.00000000000000),App.Vector(-87.39956000000001,7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Pad","Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC")
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC")
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrVvZHux1ccAEAm_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrVvZHux1ccAEAm_0_FNQScy7SzSQrpH7_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Plane", "plane_Sketch_Fax9cK6WsqlwzZ3_1_JJC")
origin = App.Vector(81.26069000000000,-3.75000000000000,1.75000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fax9cK6WsqlwzZ3_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("Sketcher::SketchObject","Sketch_Fax9cK6WsqlwzZ3_1_JJC")
App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fax9cK6WsqlwzZ3_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-18.75000000000000,-1.75000000000000,0.00000000000000),App.Vector(-3.75000000000000,-1.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-3.75000000000000,-1.75000000000000,0.00000000000000),App.Vector(-3.75000000000000,1.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-18.75000000000000,1.75000000000000,0.00000000000000),App.Vector(-3.75000000000000,1.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-18.75000000000000,-1.75000000000000,0.00000000000000),App.Vector(-18.75000000000000,1.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Pad","Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC")
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC")
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fax9cK6WsqlwzZ3_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fax9cK6WsqlwzZ3_1_F24Xs6zvOTvfbDB_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Plane", "plane_Sketch_Flpm3dWCBMlQtM3_1_JNC")
origin = App.Vector(86.26069000000000,-22.50000000000000,1.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Flpm3dWCBMlQtM3_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("Sketcher::SketchObject","Sketch_Flpm3dWCBMlQtM3_1_JNC")
App.ActiveDocument.getObject("Sketch_Flpm3dWCBMlQtM3_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Flpm3dWCBMlQtM3_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Flpm3dWCBMlQtM3_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Flpm3dWCBMlQtM3_1_JNC").addGeometry(Part.Circle(App.Vector(0.16452000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Flpm3dWCBMlQtM3_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Flpm3dWCBMlQtM3_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Pad","Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC")
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Flpm3dWCBMlQtM3_1_JNC")
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").Length = 7.5
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Flpm3dWCBMlQtM3_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Flpm3dWCBMlQtM3_1_F2rIWMEcvnzMbuR_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Plane", "plane_Sketch_FG2a7mxBwN7j2hT_1_JRC")
origin = App.Vector(86.26069000000000,-7.50000000000000,1.75000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FG2a7mxBwN7j2hT_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("Sketcher::SketchObject","Sketch_FG2a7mxBwN7j2hT_1_JRC")
App.ActiveDocument.getObject("Sketch_FG2a7mxBwN7j2hT_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FG2a7mxBwN7j2hT_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FG2a7mxBwN7j2hT_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FG2a7mxBwN7j2hT_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FG2a7mxBwN7j2hT_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FG2a7mxBwN7j2hT_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Pad","Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC")
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FG2a7mxBwN7j2hT_1_JRC")
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").Length = 7.5
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FG2a7mxBwN7j2hT_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FG2a7mxBwN7j2hT_1_F6H7a8D1u41Du0e_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Plane", "plane_Sketch_FJo4kvhl4JlzOeJ_1_JVC")
origin = App.Vector(-43.73931000000000,-15.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJo4kvhl4JlzOeJ_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("Sketcher::SketchObject","Sketch_FJo4kvhl4JlzOeJ_1_JVC")
App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJo4kvhl4JlzOeJ_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(30.00000000000001,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC").addGeometry(Part.LineSegment(App.Vector(30.00000000000001,3.00000000000000,0.00000000000000),App.Vector(26.00000000000000,3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(26.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC").addGeometry(Part.LineSegment(App.Vector(30.00000000000001,-3.00000000000000,0.00000000000000),App.Vector(26.00000000000000,-3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Pocket","Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC")
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC")
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Plane", "plane_Sketch_FJo4kvhl4JlzOeJ_1_JVG")
origin = App.Vector(-43.73931000000000,-15.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJo4kvhl4JlzOeJ_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("Sketcher::SketchObject","Sketch_FJo4kvhl4JlzOeJ_1_JVG")
App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJo4kvhl4JlzOeJ_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG").addGeometry(Part.LineSegment(App.Vector(26.00000000000000,-6.00000000000000,0.00000000000000),App.Vector(30.00000000000001,-6.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(30.00000000000001,-9.00000000000000,0.00000000000000),App.Vector(0.0,0.0,-1.0),3.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG").addGeometry(Part.LineSegment(App.Vector(30.00000000000001,-12.00000000000000,0.00000000000000),App.Vector(26.00000000000000,-12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(26.00000000000000,-9.00000000000000,0.00000000000000),App.Vector(0.0,0.0,-1.0),3.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Pocket","Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG")
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG")
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Plane", "plane_Sketch_FJo4kvhl4JlzOeJ_1_JVK")
origin = App.Vector(-43.73931000000000,-15.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJo4kvhl4JlzOeJ_1_JVK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("Sketcher::SketchObject","Sketch_FJo4kvhl4JlzOeJ_1_JVK")
App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJo4kvhl4JlzOeJ_1_JVK"), [""])
App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK").addGeometry(Part.LineSegment(App.Vector(26.00000000000000,6.00000000000000,0.00000000000000),App.Vector(30.00000000000001,6.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(30.00000000000001,9.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK").addGeometry(Part.LineSegment(App.Vector(30.00000000000001,12.00000000000000,0.00000000000000),App.Vector(26.00000000000000,12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(26.00000000000000,9.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Pocket","Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK")
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").Profile = App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK")
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJo4kvhl4JlzOeJ_1_JVK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").Type = 4
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJo4kvhl4JlzOeJ_1_FwwsbUXMTfNEDdm_1_JVK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Plane", "plane_Sketch_FiiF78YC1ilb3Vg_1_JZC")
origin = App.Vector(41.26069000000000,-15.00000000000000,3.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiiF78YC1ilb3Vg_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("Sketcher::SketchObject","Sketch_FiiF78YC1ilb3Vg_1_JZC")
App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiiF78YC1ilb3Vg_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZC").addGeometry(Part.Circle(App.Vector(20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Pocket","Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC")
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZC")
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Plane", "plane_Sketch_FiiF78YC1ilb3Vg_1_JZG")
origin = App.Vector(41.26069000000000,-15.00000000000000,3.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiiF78YC1ilb3Vg_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("Sketcher::SketchObject","Sketch_FiiF78YC1ilb3Vg_1_JZG")
App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiiF78YC1ilb3Vg_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZG").addGeometry(Part.Circle(App.Vector(-10.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),5.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FrVvZHux1ccAEAm_0").newObject("PartDesign::Pocket","Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG")
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZG")
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiiF78YC1ilb3Vg_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiiF78YC1ilb3Vg_1_FIxkcDWz7CS3ZB4_1_JZG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00521693")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fd1YCREI9kybJKQ_0")
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").Label = "Body_Fd1YCREI9kybJKQ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Plane", "plane_Sketch_Fd1YCREI9kybJKQ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fd1YCREI9kybJKQ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("Sketcher::SketchObject","Sketch_Fd1YCREI9kybJKQ_0_JGC")
App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fd1YCREI9kybJKQ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2133.59999999999991,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(2133.59999999999991,0.00000000000000,0.00000000000000),App.Vector(2133.59999999999991,1219.20000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,1219.20000000000005,0.00000000000000),App.Vector(2133.59999999999991,1219.20000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1219.20000000000005,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Pad","Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC")
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC")
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fd1YCREI9kybJKQ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fd1YCREI9kybJKQ_0_FBl8hsYFV3PgA47_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Plane", "plane_Sketch_FVclOwBleswJUS8_1_JJC")
origin = App.Vector(1066.79999999999995,-25.40000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVclOwBleswJUS8_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("Sketcher::SketchObject","Sketch_FVclOwBleswJUS8_1_JJC")
App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVclOwBleswJUS8_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,609.60000000000002,0.00000000000000),App.Vector(984.25000000000011,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,609.60000000000002,0.00000000000000),App.Vector(984.25000000000011,584.19999999999993,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,584.19999999999993,0.00000000000000),App.Vector(-984.25000000000000,584.19999999999993,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,609.60000000000002,0.00000000000000),App.Vector(-984.25000000000000,584.19999999999993,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Pad","Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC")
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC")
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVclOwBleswJUS8_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVclOwBleswJUS8_1_FbEEjHbA5klyrVG_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Plane", "plane_Sketch_F1CkIsdIypB23V5_1_JNC")
origin = App.Vector(1066.79999999999995,-25.40000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1CkIsdIypB23V5_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("Sketcher::SketchObject","Sketch_F1CkIsdIypB23V5_1_JNC")
App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1CkIsdIypB23V5_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,-609.60000000000002,0.00000000000000),App.Vector(984.25000000000011,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,-609.60000000000002,0.00000000000000),App.Vector(984.25000000000011,-584.20000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,-584.20000000000005,0.00000000000000),App.Vector(984.25000000000011,-584.20000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,-609.60000000000002,0.00000000000000),App.Vector(-984.25000000000000,-584.20000000000005,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Pad","Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC")
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC")
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1CkIsdIypB23V5_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1CkIsdIypB23V5_1_FYWtcpTRO4wHUod_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Plane", "plane_Sketch_FRVxMPbOf9xipzK_1_JRC")
origin = App.Vector(1066.79999999999995,-25.40000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRVxMPbOf9xipzK_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("Sketcher::SketchObject","Sketch_FRVxMPbOf9xipzK_1_JRC")
App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRVxMPbOf9xipzK_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC").addGeometry(Part.LineSegment(App.Vector(-1066.79999999999995,609.60000000000002,0.00000000000000),App.Vector(-1041.39999999999986,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC").addGeometry(Part.LineSegment(App.Vector(-1041.39999999999986,609.60000000000002,0.00000000000000),App.Vector(-1041.39999999999986,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC").addGeometry(Part.LineSegment(App.Vector(-1066.79999999999995,-609.60000000000002,0.00000000000000),App.Vector(-1041.39999999999986,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC").addGeometry(Part.LineSegment(App.Vector(-1066.79999999999995,-609.60000000000002,0.00000000000000),App.Vector(-1066.79999999999995,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Pad","Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC")
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC")
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRVxMPbOf9xipzK_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRVxMPbOf9xipzK_1_FhJ5uyvfjZtmRdB_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Plane", "plane_Sketch_FUCVBrezXoNAT4v_1_JVC")
origin = App.Vector(1066.79999999999995,-25.40000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUCVBrezXoNAT4v_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("Sketcher::SketchObject","Sketch_FUCVBrezXoNAT4v_1_JVC")
App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUCVBrezXoNAT4v_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC").addGeometry(Part.LineSegment(App.Vector(1066.79999999999995,-609.60000000000002,0.00000000000000),App.Vector(1041.40000000000009,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC").addGeometry(Part.LineSegment(App.Vector(1041.40000000000009,-609.60000000000002,0.00000000000000),App.Vector(1041.40000000000009,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC").addGeometry(Part.LineSegment(App.Vector(1066.79999999999995,609.60000000000002,0.00000000000000),App.Vector(1041.40000000000009,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC").addGeometry(Part.LineSegment(App.Vector(1066.79999999999995,-609.60000000000002,0.00000000000000),App.Vector(1066.79999999999995,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Pad","Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC")
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC")
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUCVBrezXoNAT4v_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUCVBrezXoNAT4v_1_FrXoaEvdLyMLtsb_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Plane", "plane_Sketch_F0vnw00KYUV7ZDF_1_JZC")
origin = App.Vector(1066.79999999999995,-25.40000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0vnw00KYUV7ZDF_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("Sketcher::SketchObject","Sketch_F0vnw00KYUV7ZDF_1_JZC")
App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0vnw00KYUV7ZDF_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,527.04999999999995,0.00000000000000),App.Vector(-984.25000000000000,527.04999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,527.04999999999995,0.00000000000000),App.Vector(-984.25000000000000,501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,501.65000000000003,0.00000000000000),App.Vector(-984.25000000000000,501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,527.04999999999995,0.00000000000000),App.Vector(984.25000000000011,501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Pad","Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC")
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC")
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0vnw00KYUV7ZDF_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0vnw00KYUV7ZDF_1_F8qWEn5UsnGWrgE_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Plane", "plane_Sketch_F7NA5FqTKwxhf2k_1_JdC")
origin = App.Vector(1066.79999999999995,-25.40000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7NA5FqTKwxhf2k_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("Sketcher::SketchObject","Sketch_F7NA5FqTKwxhf2k_1_JdC")
App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7NA5FqTKwxhf2k_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,-527.05000000000007,0.00000000000000),App.Vector(984.25000000000011,-527.05000000000007,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,-527.05000000000007,0.00000000000000),App.Vector(984.25000000000011,-501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,-501.65000000000003,0.00000000000000),App.Vector(984.25000000000011,-501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,-527.05000000000007,0.00000000000000),App.Vector(-984.25000000000000,-501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Pad","Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC")
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC")
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7NA5FqTKwxhf2k_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7NA5FqTKwxhf2k_1_Fl39k5kGq9CGemF_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Plane", "plane_Sketch_FkxTsq3RGtgsUqw_1_JhK")
origin = App.Vector(1066.79999999999995,-25.40000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkxTsq3RGtgsUqw_1_JhK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("Sketcher::SketchObject","Sketch_FkxTsq3RGtgsUqw_1_JhK")
App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkxTsq3RGtgsUqw_1_JhK"), [""])
App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,-501.65000000000003,0.00000000000000),App.Vector(958.85000000000025,-501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK").addGeometry(Part.LineSegment(App.Vector(958.85000000000025,-501.65000000000003,0.00000000000000),App.Vector(958.85000000000025,501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,501.65000000000003,0.00000000000000),App.Vector(958.85000000000025,501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK").addGeometry(Part.LineSegment(App.Vector(984.25000000000011,501.65000000000003,0.00000000000000),App.Vector(984.25000000000011,-501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Pad","Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK")
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").Profile = App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK")
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkxTsq3RGtgsUqw_1_JhK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").Type = 4
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkxTsq3RGtgsUqw_1_FcMj6zgdWH9iH9b_1_JhK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Plane", "plane_Sketch_FEv6qJ5WL70eatu_1_JlK")
origin = App.Vector(1066.79999999999995,-25.40000000000000,609.60000000000002)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEv6qJ5WL70eatu_1_JlK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("Sketcher::SketchObject","Sketch_FEv6qJ5WL70eatu_1_JlK")
App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEv6qJ5WL70eatu_1_JlK"), [""])
App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,-501.65000000000003,0.00000000000000),App.Vector(-958.85000000000002,-501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK").addGeometry(Part.LineSegment(App.Vector(-958.85000000000002,-501.65000000000003,0.00000000000000),App.Vector(-958.85000000000002,501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,501.65000000000003,0.00000000000000),App.Vector(-958.85000000000002,501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK").addGeometry(Part.LineSegment(App.Vector(-984.25000000000000,501.65000000000003,0.00000000000000),App.Vector(-984.25000000000000,-501.65000000000003,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fd1YCREI9kybJKQ_0").newObject("PartDesign::Pad","Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK")
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").Profile = App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK")
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEv6qJ5WL70eatu_1_JlK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").Type = 4
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEv6qJ5WL70eatu_1_FHa9wVznB8tn0x5_1_JlK").Offset = 0
App.ActiveDocument.recompute()

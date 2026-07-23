import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00577368")
App.ActiveDocument.addObject("PartDesign::Body","Body_FShRnMDqjUdMkCO_0")
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").Label = "Body_FShRnMDqjUdMkCO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_FShRnMDqjUdMkCO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FShRnMDqjUdMkCO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_FShRnMDqjUdMkCO_0_JGC")
App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FShRnMDqjUdMkCO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.00000000000000,60.00000000000000,0.00000000000000),App.Vector(45.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(45.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pad","Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC")
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC")
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FShRnMDqjUdMkCO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FShRnMDqjUdMkCO_0_F6xRzjAPQGWF1LB_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_Fw2H2zRuHqSf0L9_1_JLK")
origin = App.Vector(0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fw2H2zRuHqSf0L9_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_Fw2H2zRuHqSf0L9_1_JLK")
App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fw2H2zRuHqSf0L9_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),30.00000000000000),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.LineSegment(App.Vector(-40.00000000000000,-45.00000000000000,0.00000000000000),App.Vector(-40.00000000000000,40.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-25.00000000000000,40.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,55.00000000000000,0.00000000000000),App.Vector(18.00000000000000,55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.LineSegment(App.Vector(18.00000000000000,55.00000000000000,0.00000000000000),App.Vector(18.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(33.00000000000000,50.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,35.00000000000000,0.00000000000000),App.Vector(33.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,35.00000000000000,0.00000000000000),App.Vector(40.00000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(33.00000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(33.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.LineSegment(App.Vector(18.00000000000000,-55.00000000000000,0.00000000000000),App.Vector(18.00000000000000,-50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.LineSegment(App.Vector(18.00000000000000,-55.00000000000000,0.00000000000000),App.Vector(-18.00000000000000,-55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").addGeometry(Part.LineSegment(App.Vector(-40.00000000000000,-45.00000000000000,0.00000000000000),App.Vector(-18.00000000000000,-55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pad","Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK")
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK")
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fw2H2zRuHqSf0L9_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fw2H2zRuHqSf0L9_1_FcF99QkJuhagTLS_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_Fg0LrU7lhzpNZXx_1_JPG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_Fg0LrU7lhzpNZXx_1_JPG")
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPG").addGeometry(Part.Circle(App.Vector(0.00000000000000,20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pocket","Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPG")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_Fg0LrU7lhzpNZXx_1_JPK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_Fg0LrU7lhzpNZXx_1_JPK")
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPK").addGeometry(Part.Circle(App.Vector(20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pocket","Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPK")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_Fg0LrU7lhzpNZXx_1_JPO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_Fg0LrU7lhzpNZXx_1_JPO")
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPO"), [""])
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPO").addGeometry(Part.Circle(App.Vector(0.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pocket","Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").Profile = App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPO")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").Type = 4
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_Fg0LrU7lhzpNZXx_1_JPS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_Fg0LrU7lhzpNZXx_1_JPS")
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPS"), [""])
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPS").addGeometry(Part.Circle(App.Vector(-14.14427000000000,-14.14000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pocket","Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").Profile = App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPS")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").Type = 4
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_Fg0LrU7lhzpNZXx_1_JPW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_Fg0LrU7lhzpNZXx_1_JPW")
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPW"), [""])
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPW").addGeometry(Part.Circle(App.Vector(-14.14427000000000,14.14000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pocket","Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").Profile = App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPW")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").Type = 4
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_Fg0LrU7lhzpNZXx_1_JPa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_Fg0LrU7lhzpNZXx_1_JPa")
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPa"), [""])
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPa").addGeometry(Part.Circle(App.Vector(14.14427000000000,14.14000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pocket","Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").Profile = App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPa")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").Type = 4
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_Fg0LrU7lhzpNZXx_1_JPe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_Fg0LrU7lhzpNZXx_1_JPe")
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPe"), [""])
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPe").addGeometry(Part.Circle(App.Vector(14.14427000000000,-14.14000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pocket","Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").Profile = App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPe")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").Type = 4
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Plane", "plane_Sketch_Fg0LrU7lhzpNZXx_1_JPC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("Sketcher::SketchObject","Sketch_Fg0LrU7lhzpNZXx_1_JPC")
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg0LrU7lhzpNZXx_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPC").addGeometry(Part.Circle(App.Vector(-20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FShRnMDqjUdMkCO_0").newObject("PartDesign::Pocket","Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPC")
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg0LrU7lhzpNZXx_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg0LrU7lhzpNZXx_1_Fuh5mz0CIzG3XLJ_1_JPC").Offset = 0
App.ActiveDocument.recompute()

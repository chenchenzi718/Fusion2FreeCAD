import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00404531")
App.ActiveDocument.addObject("PartDesign::Body","Body_FTQ6gVNPSD0S4TQ_0")
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").Label = "Body_FTQ6gVNPSD0S4TQ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Plane", "plane_Sketch_FTQ6gVNPSD0S4TQ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTQ6gVNPSD0S4TQ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("Sketcher::SketchObject","Sketch_FTQ6gVNPSD0S4TQ_0_JGC")
App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTQ6gVNPSD0S4TQ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,16.00000000000000,0.00000000000000),App.Vector(25.00000000000000,16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,16.00000000000000,0.00000000000000),App.Vector(25.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2.45968000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2.45968000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,16.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Pad","Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC")
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC")
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").Length = 16.0
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Plane", "plane_Sketch_FTQ6gVNPSD0S4TQ_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTQ6gVNPSD0S4TQ_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("Sketcher::SketchObject","Sketch_FTQ6gVNPSD0S4TQ_0_JGG")
App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTQ6gVNPSD0S4TQ_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,0.00000000000000,0.00000000000000),App.Vector(2.45968000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG").addGeometry(Part.LineSegment(App.Vector(2.45968000000000,0.00000000000000,0.00000000000000),App.Vector(20.07869000000000,-17.61902000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG").addGeometry(Part.LineSegment(App.Vector(9.18012000000000,-28.73123000000000,0.00000000000000),App.Vector(20.07869000000000,-17.61902000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,-10.55111000000000,0.00000000000000),App.Vector(9.18012000000000,-28.73123000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,-10.55111000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Pad","Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG")
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG")
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").Length = 16.0
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Plane", "plane_Sketch_FTQ6gVNPSD0S4TQ_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTQ6gVNPSD0S4TQ_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("Sketcher::SketchObject","Sketch_FTQ6gVNPSD0S4TQ_0_JGK")
App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTQ6gVNPSD0S4TQ_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,-34.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,-34.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,-10.55111000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,-10.55111000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Pad","Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK")
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK")
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").Length = 16.0
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTQ6gVNPSD0S4TQ_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTQ6gVNPSD0S4TQ_0_FOwZyOLjcVfOujr_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Plane", "plane_Sketch_FzmtvomGp8VNXb1_1_JJC")
origin = App.Vector(25.00000000000000,8.00000000000000,8.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzmtvomGp8VNXb1_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("Sketcher::SketchObject","Sketch_FzmtvomGp8VNXb1_1_JJC")
App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzmtvomGp8VNXb1_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Pocket","Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC")
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC")
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzmtvomGp8VNXb1_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzmtvomGp8VNXb1_1_FgyLvMKosC0NWrC_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Plane", "plane_Sketch_FqjwltSpbn2Ml96_1_JOC")
origin = App.Vector(-17.00000000000000,-34.00000000000000,8.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqjwltSpbn2Ml96_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("Sketcher::SketchObject","Sketch_FqjwltSpbn2Ml96_1_JOC")
App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqjwltSpbn2Ml96_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Pocket","Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC")
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC")
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqjwltSpbn2Ml96_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqjwltSpbn2Ml96_1_FpRfCxOR51aLUMX_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Plane", "plane_Sketch_FFt437cJnSTW4Cq_1_JTC")
origin = App.Vector(0.00000000000000,-9.00000000000000,16.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFt437cJnSTW4Cq_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("Sketcher::SketchObject","Sketch_FFt437cJnSTW4Cq_1_JTC")
App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFt437cJnSTW4Cq_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTC").addGeometry(Part.Circle(App.Vector(-17.00000000000000,-17.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Pocket","Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC")
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTC")
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").Length = 16.0
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Plane", "plane_Sketch_FFt437cJnSTW4Cq_1_JTG")
origin = App.Vector(0.00000000000000,-9.00000000000000,16.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFt437cJnSTW4Cq_1_JTG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("Sketcher::SketchObject","Sketch_FFt437cJnSTW4Cq_1_JTG")
App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFt437cJnSTW4Cq_1_JTG"), [""])
App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTG").addGeometry(Part.Circle(App.Vector(17.00000000000000,17.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Pocket","Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG")
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").Profile = App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTG")
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").Length = 16.0
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").Type = 4
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Plane", "plane_Sketch_FFt437cJnSTW4Cq_1_JTK")
origin = App.Vector(0.00000000000000,-9.00000000000000,16.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFt437cJnSTW4Cq_1_JTK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("Sketcher::SketchObject","Sketch_FFt437cJnSTW4Cq_1_JTK")
App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFt437cJnSTW4Cq_1_JTK"), [""])
App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTK").addGeometry(Part.Circle(App.Vector(8.81962000000000,-8.67365000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Pocket","Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK")
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").Profile = App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTK")
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").Length = 16.0
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFt437cJnSTW4Cq_1_JTK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").Type = 4
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFt437cJnSTW4Cq_1_FyaHXT47uPN4zfd_1_JTK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Plane", "plane_Sketch_FhBWggGIjJz1ZM8_1_JXC")
origin = App.Vector(14.62940000000000,-23.17512000000000,8.00000000000000)
x_axis=App.Vector(0.70021065000000,0.71393630000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,0.99999999483111)
z_axis=App.Vector(0.71393630000000,-0.70021065000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhBWggGIjJz1ZM8_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("Sketcher::SketchObject","Sketch_FhBWggGIjJz1ZM8_1_JXC")
App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhBWggGIjJz1ZM8_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC").addGeometry(Part.LineSegment(App.Vector(-4.78235310221250,4.99999997415556,0.00000643130000),App.Vector(5.21764729228350,4.99999997415556,-0.00000311076050)),False)

App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC").addGeometry(Part.LineSegment(App.Vector(5.21764729228350,4.99999997415556,-0.00000311076050),App.Vector(5.21764729228350,-4.99999997415556,-0.00000311076050)),False)

App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC").addGeometry(Part.LineSegment(App.Vector(-4.78235310221250,-4.99999997415556,0.00000643130000),App.Vector(5.21764729228350,-4.99999997415556,-0.00000311076050)),False)

App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC").addGeometry(Part.LineSegment(App.Vector(-4.78235310221250,4.99999997415556,0.00000643130000),App.Vector(-4.78235310221250,-4.99999997415556,0.00000643130000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTQ6gVNPSD0S4TQ_0").newObject("PartDesign::Pocket","Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC")
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC")
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhBWggGIjJz1ZM8_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhBWggGIjJz1ZM8_1_FOaDTjY2mDFg9zg_1_JXC").Offset = 0
App.ActiveDocument.recompute()

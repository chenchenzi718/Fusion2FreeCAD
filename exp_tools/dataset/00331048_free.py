import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00331048")
App.ActiveDocument.addObject("PartDesign::Body","Body_FTGtqRwLKSSPQAf_0")
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").Label = "Body_FTGtqRwLKSSPQAf_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Plane", "plane_Sketch_FTGtqRwLKSSPQAf_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTGtqRwLKSSPQAf_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("Sketcher::SketchObject","Sketch_FTGtqRwLKSSPQAf_0_JGC")
App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTGtqRwLKSSPQAf_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,38.10000000000000,0.00000000000000),App.Vector(38.10000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,38.10000000000000,0.00000000000000),App.Vector(38.10000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,25.40000000000000,0.00000000000000),App.Vector(88.90000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").addGeometry(Part.LineSegment(App.Vector(88.90000000000001,25.40000000000000,0.00000000000000),App.Vector(88.90000000000001,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").addGeometry(Part.LineSegment(App.Vector(88.90000000000001,12.70000000000000,0.00000000000000),App.Vector(38.10000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,12.70000000000000,0.00000000000000),App.Vector(38.10000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(38.10000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Pad","Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC")
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC")
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").Length = 38.1
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTGtqRwLKSSPQAf_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTGtqRwLKSSPQAf_0_FcR84HX9tjY0vbI_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Plane", "plane_Sketch_FLaTbL8T8mVijVe_1_JJC")
origin = App.Vector(63.65240000000000,-19.05000000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLaTbL8T8mVijVe_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("Sketcher::SketchObject","Sketch_FLaTbL8T8mVijVe_1_JJC")
App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLaTbL8T8mVijVe_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJC").addGeometry(Part.LineSegment(App.Vector(25.24760000000001,19.05000000000000,0.00000000000000),App.Vector(6.19760000000000,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(6.19760000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),19.05000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJC").addGeometry(Part.LineSegment(App.Vector(25.24760000000001,19.05000000000000,0.00000000000000),App.Vector(25.24760000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Pocket","Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC")
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJC")
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Plane", "plane_Sketch_FLaTbL8T8mVijVe_1_JJG")
origin = App.Vector(63.65240000000000,-19.05000000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLaTbL8T8mVijVe_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("Sketcher::SketchObject","Sketch_FLaTbL8T8mVijVe_1_JJG")
App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLaTbL8T8mVijVe_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJG").addGeometry(Part.LineSegment(App.Vector(25.24760000000001,-19.05000000000000,0.00000000000000),App.Vector(6.19760000000000,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(6.19760000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),19.05000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJG").addGeometry(Part.LineSegment(App.Vector(25.24760000000001,-19.05000000000000,0.00000000000000),App.Vector(25.24760000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Pocket","Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG")
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJG")
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLaTbL8T8mVijVe_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLaTbL8T8mVijVe_1_F0Iq6HAk0665Bi4_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Plane", "plane_Sketch_Fa5ok7CFvIMCm24_1_JNC")
origin = App.Vector(19.05000000000000,-19.05000000000000,38.10000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa5ok7CFvIMCm24_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("Sketcher::SketchObject","Sketch_Fa5ok7CFvIMCm24_1_JNC")
App.ActiveDocument.getObject("Sketch_Fa5ok7CFvIMCm24_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa5ok7CFvIMCm24_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fa5ok7CFvIMCm24_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa5ok7CFvIMCm24_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa5ok7CFvIMCm24_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa5ok7CFvIMCm24_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Pocket","Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC")
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fa5ok7CFvIMCm24_1_JNC")
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").Length = 38.1
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa5ok7CFvIMCm24_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa5ok7CFvIMCm24_1_F1TdiIEAiYLLdn4_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Plane", "plane_Sketch_FA3vpqqW1EwMBtl_1_JRC")
origin = App.Vector(63.65240000000000,-19.05000000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FA3vpqqW1EwMBtl_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("Sketcher::SketchObject","Sketch_FA3vpqqW1EwMBtl_1_JRC")
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FA3vpqqW1EwMBtl_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRC").addGeometry(Part.Circle(App.Vector(-12.85240000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Pocket","Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC")
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRC")
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Plane", "plane_Sketch_FA3vpqqW1EwMBtl_1_JRG")
origin = App.Vector(63.65240000000000,-19.05000000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FA3vpqqW1EwMBtl_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("Sketcher::SketchObject","Sketch_FA3vpqqW1EwMBtl_1_JRG")
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FA3vpqqW1EwMBtl_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRG").addGeometry(Part.Circle(App.Vector(-12.85240000000000,-6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Pocket","Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG")
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRG")
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Plane", "plane_Sketch_FA3vpqqW1EwMBtl_1_JRK")
origin = App.Vector(63.65240000000000,-19.05000000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FA3vpqqW1EwMBtl_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("Sketcher::SketchObject","Sketch_FA3vpqqW1EwMBtl_1_JRK")
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FA3vpqqW1EwMBtl_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRK").addGeometry(Part.Circle(App.Vector(6.19760000000000,-6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Pocket","Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK")
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRK")
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Plane", "plane_Sketch_FA3vpqqW1EwMBtl_1_JRO")
origin = App.Vector(63.65240000000000,-19.05000000000000,25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FA3vpqqW1EwMBtl_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("Sketcher::SketchObject","Sketch_FA3vpqqW1EwMBtl_1_JRO")
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FA3vpqqW1EwMBtl_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRO").addGeometry(Part.Circle(App.Vector(6.19760000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTGtqRwLKSSPQAf_0").newObject("PartDesign::Pocket","Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO")
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRO")
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FA3vpqqW1EwMBtl_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FA3vpqqW1EwMBtl_1_Ff0HJh6gkYqbda5_1_JRO").Offset = 0
App.ActiveDocument.recompute()

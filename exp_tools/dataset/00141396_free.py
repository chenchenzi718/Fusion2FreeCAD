import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00141396")
App.ActiveDocument.addObject("PartDesign::Body","Body_FUVem7RZonQabuk_0")
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").Label = "Body_FUVem7RZonQabuk_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Plane", "plane_Sketch_FUVem7RZonQabuk_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUVem7RZonQabuk_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("Sketcher::SketchObject","Sketch_FUVem7RZonQabuk_0_JGC")
App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUVem7RZonQabuk_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-288.92500000000001,177.80000000000001,0.00000000000000),App.Vector(288.92500000000001,177.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC").addGeometry(Part.LineSegment(App.Vector(288.92500000000001,177.80000000000001,0.00000000000000),App.Vector(288.92500000000001,-177.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-288.92500000000001,-177.80000000000001,0.00000000000000),App.Vector(288.92500000000001,-177.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-288.92500000000001,177.80000000000001,0.00000000000000),App.Vector(-288.92500000000001,-177.80000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Pad","Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC")
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC")
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").Length = 304.8
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUVem7RZonQabuk_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUVem7RZonQabuk_0_FCSj1WE5vfcqbk3_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Plane", "plane_Sketch_FRQMEYHSCZv5OK3_1_JJC")
origin = App.Vector(-0.00000000000000,-177.80000000000001,152.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRQMEYHSCZv5OK3_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("Sketcher::SketchObject","Sketch_FRQMEYHSCZv5OK3_1_JJC")
App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRQMEYHSCZv5OK3_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-282.57500000000005,146.04999999999998,0.00000000000000),App.Vector(282.57500000000005,146.04999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC").addGeometry(Part.LineSegment(App.Vector(282.57500000000005,146.04999999999998,0.00000000000000),App.Vector(282.57500000000005,-146.05000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-282.57500000000005,-146.05000000000001,0.00000000000000),App.Vector(282.57500000000005,-146.05000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-282.57500000000005,146.04999999999998,0.00000000000000),App.Vector(-282.57500000000005,-146.05000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Pocket","Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC")
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC")
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").Length = 352.42500000000007
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRQMEYHSCZv5OK3_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRQMEYHSCZv5OK3_1_FYjKU1rjK61mOZ3_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Plane", "plane_Sketch_F1UISOO8rgj57tT_1_JNC")
origin = App.Vector(0.00000000000000,174.62500000000000,152.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1UISOO8rgj57tT_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("Sketcher::SketchObject","Sketch_F1UISOO8rgj57tT_1_JNC")
App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1UISOO8rgj57tT_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC").addGeometry(Part.LineSegment(App.Vector(-279.39999999999998,142.87500000000000,0.00000000000000),App.Vector(279.39999999999998,142.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC").addGeometry(Part.LineSegment(App.Vector(279.39999999999998,142.87500000000000,0.00000000000000),App.Vector(279.39999999999998,1.65099999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC").addGeometry(Part.LineSegment(App.Vector(-279.39999999999998,1.65099999999999,0.00000000000000),App.Vector(279.39999999999998,1.65099999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC").addGeometry(Part.LineSegment(App.Vector(-279.39999999999998,142.87500000000000,0.00000000000000),App.Vector(-279.39999999999998,1.65099999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Pad","Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC")
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC")
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").Length = 352.42500000000007
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Plane", "plane_Sketch_F1UISOO8rgj57tT_1_JNG")
origin = App.Vector(0.00000000000000,174.62500000000000,152.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1UISOO8rgj57tT_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("Sketcher::SketchObject","Sketch_F1UISOO8rgj57tT_1_JNG")
App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1UISOO8rgj57tT_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG").addGeometry(Part.LineSegment(App.Vector(-279.39999999999998,-142.87500000000000,0.00000000000000),App.Vector(279.39999999999998,-142.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG").addGeometry(Part.LineSegment(App.Vector(279.39999999999998,-142.87500000000000,0.00000000000000),App.Vector(279.39999999999998,-1.65100000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG").addGeometry(Part.LineSegment(App.Vector(-279.39999999999998,-1.65100000000001,0.00000000000000),App.Vector(279.39999999999998,-1.65100000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG").addGeometry(Part.LineSegment(App.Vector(-279.39999999999998,-142.87500000000000,0.00000000000000),App.Vector(-279.39999999999998,-1.65100000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Pad","Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG")
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG")
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").Length = 352.42500000000007
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1UISOO8rgj57tT_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1UISOO8rgj57tT_1_FCujvIdIvEdYUZ8_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Plane", "plane_Sketch_FbDbTBoyM9ZOkg4_1_JRC")
origin = App.Vector(-0.00000000000000,-177.80000000000001,224.66300000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbDbTBoyM9ZOkg4_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("Sketcher::SketchObject","Sketch_FbDbTBoyM9ZOkg4_1_JRC")
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbDbTBoyM9ZOkg4_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-86.61399999999999,0.00000000000000),App.Vector(0.00000000000000,-188.21400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC").addGeometry(Part.LineSegment(App.Vector(-101.59999999999999,-188.21400000000000,0.00000000000000),App.Vector(0.00000000000000,-188.21400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-101.59999999999999,-137.41400000000002,0.00000000000000),App.Vector(0.0,0.0,1.0),50.80000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC").addGeometry(Part.LineSegment(App.Vector(-101.59999999999999,-86.61399999999999,0.00000000000000),App.Vector(0.00000000000000,-86.61399999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Pocket","Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC")
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC")
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Plane", "plane_Sketch_FbDbTBoyM9ZOkg4_1_JRG")
origin = App.Vector(-0.00000000000000,-177.80000000000001,224.66300000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbDbTBoyM9ZOkg4_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("Sketcher::SketchObject","Sketch_FbDbTBoyM9ZOkg4_1_JRG")
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbDbTBoyM9ZOkg4_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-86.61399999999999,0.00000000000000),App.Vector(0.00000000000000,-188.21400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG").addGeometry(Part.LineSegment(App.Vector(101.59999999999999,-188.21400000000000,0.00000000000000),App.Vector(0.00000000000000,-188.21400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(101.59999999999999,-137.41400000000002,0.00000000000000),App.Vector(0.0,0.0,1.0),50.80000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG").addGeometry(Part.LineSegment(App.Vector(101.59999999999999,-86.61399999999999,0.00000000000000),App.Vector(0.00000000000000,-86.61399999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Pocket","Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG")
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG")
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Plane", "plane_Sketch_FbDbTBoyM9ZOkg4_1_JRK")
origin = App.Vector(-0.00000000000000,-177.80000000000001,224.66300000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbDbTBoyM9ZOkg4_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("Sketcher::SketchObject","Sketch_FbDbTBoyM9ZOkg4_1_JRK")
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbDbTBoyM9ZOkg4_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK").addGeometry(Part.LineSegment(App.Vector(-101.59999999999999,57.91200000000002,0.00000000000000),App.Vector(0.00000000000000,57.91200000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,57.91200000000002,0.00000000000000),App.Vector(0.00000000000000,-43.68800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK").addGeometry(Part.LineSegment(App.Vector(-101.59999999999999,-43.68800000000000,0.00000000000000),App.Vector(0.00000000000000,-43.68800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-101.59999999999999,7.11200000000001,0.00000000000000),App.Vector(0.0,0.0,1.0),50.80000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Pocket","Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK")
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK")
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Plane", "plane_Sketch_FbDbTBoyM9ZOkg4_1_JRO")
origin = App.Vector(-0.00000000000000,-177.80000000000001,224.66300000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbDbTBoyM9ZOkg4_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("Sketcher::SketchObject","Sketch_FbDbTBoyM9ZOkg4_1_JRO")
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbDbTBoyM9ZOkg4_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO").addGeometry(Part.LineSegment(App.Vector(101.59999999999999,57.91200000000002,0.00000000000000),App.Vector(0.00000000000000,57.91200000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,57.91200000000002,0.00000000000000),App.Vector(0.00000000000000,-43.68800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO").addGeometry(Part.LineSegment(App.Vector(101.59999999999999,-43.68800000000000,0.00000000000000),App.Vector(0.00000000000000,-43.68800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(101.59999999999999,7.11200000000001,0.00000000000000),App.Vector(0.0,0.0,1.0),50.80000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUVem7RZonQabuk_0").newObject("PartDesign::Pocket","Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO")
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO")
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbDbTBoyM9ZOkg4_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbDbTBoyM9ZOkg4_1_FI0fOi4qRWOYt4H_1_JRO").Offset = 0
App.ActiveDocument.recompute()

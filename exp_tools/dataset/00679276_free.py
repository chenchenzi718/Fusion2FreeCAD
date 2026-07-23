import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00679276")
App.ActiveDocument.addObject("PartDesign::Body","Body_FT5RA0Uzh48lhQ1_0")
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").Label = "Body_FT5RA0Uzh48lhQ1_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Plane", "plane_Sketch_FT5RA0Uzh48lhQ1_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FT5RA0Uzh48lhQ1_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("Sketcher::SketchObject","Sketch_FT5RA0Uzh48lhQ1_0_JGK")
App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FT5RA0Uzh48lhQ1_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").addGeometry(Part.LineSegment(App.Vector(-127.00000000000000,-57.15000000000000,0.00000000000000),App.Vector(127.00000000000000,-57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").addGeometry(Part.LineSegment(App.Vector(127.00000000000000,-57.15000000000000,0.00000000000000),App.Vector(127.00000000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").addGeometry(Part.LineSegment(App.Vector(-127.00000000000000,57.15000000000000,0.00000000000000),App.Vector(127.00000000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").addGeometry(Part.LineSegment(App.Vector(-127.00000000000000,-57.15000000000000,0.00000000000000),App.Vector(-127.00000000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").addGeometry(Part.Circle(App.Vector(63.50000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),50.80000000000000),False)

App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").addGeometry(Part.Circle(App.Vector(-63.50000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),50.80000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Pad","Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK")
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK")
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").Length = 1.5875000000000001
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FT5RA0Uzh48lhQ1_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FT5RA0Uzh48lhQ1_0_FLybYbhkN0mpChl_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Plane", "plane_Sketch_FfptcHngbvDQdgs_1_JJC")
origin = App.Vector(0.00000000000000,-1.58750000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfptcHngbvDQdgs_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("Sketcher::SketchObject","Sketch_FfptcHngbvDQdgs_1_JJC")
App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfptcHngbvDQdgs_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-122.01062000000000,57.15000000000000,0.00000000000000),App.Vector(-9.49660000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-9.49660000000000,57.15000000000000,0.00000000000000),App.Vector(-9.49660000000000,55.56250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-122.01062000000000,55.56250000000000,0.00000000000000),App.Vector(-9.49660000000000,55.56250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-122.01062000000000,55.56250000000000,0.00000000000000),App.Vector(-124.51560000000001,55.56250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-124.51560000000001,55.56250000000000,0.00000000000000),App.Vector(-124.51560000000001,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").addGeometry(Part.LineSegment(App.Vector(-122.01062000000000,57.15000000000000,0.00000000000000),App.Vector(-124.51560000000001,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Pad","Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC")
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC")
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Plane", "plane_Sketch_FfptcHngbvDQdgs_1_JJG")
origin = App.Vector(0.00000000000000,-1.58750000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfptcHngbvDQdgs_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("Sketcher::SketchObject","Sketch_FfptcHngbvDQdgs_1_JJG")
App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfptcHngbvDQdgs_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").addGeometry(Part.LineSegment(App.Vector(9.58847000000000,57.15000000000000,0.00000000000000),App.Vector(121.81662000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").addGeometry(Part.LineSegment(App.Vector(121.81662000000000,57.15000000000000,0.00000000000000),App.Vector(124.48658000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").addGeometry(Part.LineSegment(App.Vector(124.48658000000000,55.56250000000000,0.00000000000000),App.Vector(124.48658000000000,57.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").addGeometry(Part.LineSegment(App.Vector(121.81662000000000,55.56250000000000,0.00000000000000),App.Vector(124.48658000000000,55.56250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").addGeometry(Part.LineSegment(App.Vector(9.58847000000000,55.56250000000000,0.00000000000000),App.Vector(121.81662000000000,55.56250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").addGeometry(Part.LineSegment(App.Vector(9.58847000000000,57.15000000000000,0.00000000000000),App.Vector(9.58847000000000,55.56250000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Pad","Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG")
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG")
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfptcHngbvDQdgs_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfptcHngbvDQdgs_1_F7DsPbdFMee5Tqb_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Plane", "plane_Sketch_FyAZIdQSZMX0l8z_1_JNC")
origin = App.Vector(0.00000000000000,-7.14375000000000,57.15000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyAZIdQSZMX0l8z_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("Sketcher::SketchObject","Sketch_FyAZIdQSZMX0l8z_1_JNC")
App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyAZIdQSZMX0l8z_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNC").addGeometry(Part.LineSegment(App.Vector(-9.49660000000000,5.55625000000000,0.00000000000000),App.Vector(-9.49660000000000,-3.18552000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNC").addGeometry(Part.LineSegment(App.Vector(-9.49660000000000,-3.18552000000000,0.00000000000000),App.Vector(-6.47010000000000,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNC").addGeometry(Part.LineSegment(App.Vector(-9.49660000000000,5.55625000000000,0.00000000000000),App.Vector(-6.47010000000000,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Pad","Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC")
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNC")
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").Length = 1.5875000000000001
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Plane", "plane_Sketch_FyAZIdQSZMX0l8z_1_JNG")
origin = App.Vector(0.00000000000000,-7.14375000000000,57.15000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyAZIdQSZMX0l8z_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("Sketcher::SketchObject","Sketch_FyAZIdQSZMX0l8z_1_JNG")
App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyAZIdQSZMX0l8z_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNG").addGeometry(Part.LineSegment(App.Vector(9.58847000000000,5.55625000000000,0.00000000000000),App.Vector(9.58847000000000,-3.43418000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNG").addGeometry(Part.LineSegment(App.Vector(9.58847000000000,-3.43418000000000,0.00000000000000),App.Vector(6.45652000000000,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNG").addGeometry(Part.LineSegment(App.Vector(9.58847000000000,5.55625000000000,0.00000000000000),App.Vector(6.45652000000000,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Pad","Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG")
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNG")
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").Length = 1.5875000000000001
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyAZIdQSZMX0l8z_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").Type = 0
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyAZIdQSZMX0l8z_1_Fm4B8puKGdqNxmU_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Plane", "plane_Sketch_FblCUqPUl2hxL0W_1_JRC")
origin = App.Vector(0.00000000000000,-7.14375000000000,57.15000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FblCUqPUl2hxL0W_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("Sketcher::SketchObject","Sketch_FblCUqPUl2hxL0W_1_JRC")
App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FblCUqPUl2hxL0W_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRC").addGeometry(Part.LineSegment(App.Vector(-9.49660000000000,-7.14375000000000,0.00000000000000),App.Vector(-10.89034000000000,-7.14375000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRC").addGeometry(Part.LineSegment(App.Vector(-9.49660000000000,-3.18552000000000,0.00000000000000),App.Vector(-10.89034000000000,-7.14375000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRC").addGeometry(Part.LineSegment(App.Vector(-9.49660000000000,-7.14375000000000,0.00000000000000),App.Vector(-9.49660000000000,-3.18552000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Pocket","Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC")
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRC")
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Plane", "plane_Sketch_FblCUqPUl2hxL0W_1_JRG")
origin = App.Vector(0.00000000000000,-7.14375000000000,57.15000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FblCUqPUl2hxL0W_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("Sketcher::SketchObject","Sketch_FblCUqPUl2hxL0W_1_JRG")
App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FblCUqPUl2hxL0W_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRG").addGeometry(Part.LineSegment(App.Vector(9.58847000000000,-7.14375000000000,0.00000000000000),App.Vector(10.88902000000000,-7.14375000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRG").addGeometry(Part.LineSegment(App.Vector(9.58847000000000,-3.43418000000000,0.00000000000000),App.Vector(10.88902000000000,-7.14375000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRG").addGeometry(Part.LineSegment(App.Vector(9.58847000000000,-7.14375000000000,0.00000000000000),App.Vector(9.58847000000000,-3.43418000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Pocket","Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG")
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRG")
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FblCUqPUl2hxL0W_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FblCUqPUl2hxL0W_1_FmaCeJsYVudBEAS_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Plane", "plane_Sketch_FNGZfmzfzLurbTz_1_JVC")
origin = App.Vector(0.00000000000000,-7.14375000000000,57.15000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNGZfmzfzLurbTz_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("Sketcher::SketchObject","Sketch_FNGZfmzfzLurbTz_1_JVC")
App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNGZfmzfzLurbTz_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVC").addGeometry(Part.LineSegment(App.Vector(-124.51560000000001,5.55625000000000,0.00000000000000),App.Vector(-118.55844999999999,-7.14375000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVC").addGeometry(Part.LineSegment(App.Vector(-124.51560000000001,-7.14375000000000,0.00000000000000),App.Vector(-118.55844999999999,-7.14375000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVC").addGeometry(Part.LineSegment(App.Vector(-124.51560000000001,-7.14375000000000,0.00000000000000),App.Vector(-124.51560000000001,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Pocket","Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC")
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVC")
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Plane", "plane_Sketch_FNGZfmzfzLurbTz_1_JVG")
origin = App.Vector(0.00000000000000,-7.14375000000000,57.15000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNGZfmzfzLurbTz_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("Sketcher::SketchObject","Sketch_FNGZfmzfzLurbTz_1_JVG")
App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNGZfmzfzLurbTz_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVG").addGeometry(Part.LineSegment(App.Vector(124.48658000000000,5.55625000000000,0.00000000000000),App.Vector(118.69673999999999,-7.14375000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVG").addGeometry(Part.LineSegment(App.Vector(124.48658000000000,-7.14375000000000,0.00000000000000),App.Vector(118.69673999999999,-7.14375000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVG").addGeometry(Part.LineSegment(App.Vector(124.48658000000000,-7.14375000000000,0.00000000000000),App.Vector(124.48658000000000,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FT5RA0Uzh48lhQ1_0").newObject("PartDesign::Pocket","Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG")
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVG")
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNGZfmzfzLurbTz_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNGZfmzfzLurbTz_1_Fj3ZRainiKcClu4_1_JVG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00857755")
App.ActiveDocument.addObject("PartDesign::Body","Body_FkDQ6NAbUG3lmW5_0")
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").Label = "Body_FkDQ6NAbUG3lmW5_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Plane", "plane_Sketch_FkDQ6NAbUG3lmW5_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkDQ6NAbUG3lmW5_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("Sketcher::SketchObject","Sketch_FkDQ6NAbUG3lmW5_0_JGC")
App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkDQ6NAbUG3lmW5_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-44.00000000000000,32.58389000000000,0.00000000000000),App.Vector(44.00000000000000,32.58389000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC").addGeometry(Part.LineSegment(App.Vector(44.00000000000000,32.58389000000000,0.00000000000000),App.Vector(44.00000000000000,-34.41611000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-44.00000000000000,-34.41611000000000,0.00000000000000),App.Vector(44.00000000000000,-34.41611000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-44.00000000000000,32.58389000000000,0.00000000000000),App.Vector(-44.00000000000000,-34.41611000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Pad","Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC")
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC")
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").Length = 1.5
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkDQ6NAbUG3lmW5_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkDQ6NAbUG3lmW5_0_FAcL9UFSm6C3Re7_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Plane", "plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJO")
origin = App.Vector(0.00000000000000,-0.91611000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("Sketcher::SketchObject","Sketch_Fy5CCwbiJ5BGwcI_1_JJO")
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJO").addGeometry(Part.Circle(App.Vector(-40.19059000000000,29.40569000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Pad","Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO")
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJO")
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Plane", "plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJG")
origin = App.Vector(0.00000000000000,-0.91611000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("Sketcher::SketchObject","Sketch_Fy5CCwbiJ5BGwcI_1_JJG")
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJG").addGeometry(Part.Circle(App.Vector(39.80941000000001,29.40432000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Pad","Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG")
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJG")
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Plane", "plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJK")
origin = App.Vector(0.00000000000000,-0.91611000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("Sketcher::SketchObject","Sketch_Fy5CCwbiJ5BGwcI_1_JJK")
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJK").addGeometry(Part.Circle(App.Vector(-40.23079000000000,-29.59431000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Pad","Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK")
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJK")
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Plane", "plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJC")
origin = App.Vector(0.00000000000000,-0.91611000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("Sketcher::SketchObject","Sketch_Fy5CCwbiJ5BGwcI_1_JJC")
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fy5CCwbiJ5BGwcI_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJC").addGeometry(Part.Circle(App.Vector(39.76921000000000,-29.59568000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Pad","Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC")
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJC")
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fy5CCwbiJ5BGwcI_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fy5CCwbiJ5BGwcI_1_FAjY1Jrob7cFLwG_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Plane", "plane_Sketch_Fq4IGxUCKcqxF3g_1_JNC")
origin = App.Vector(-40.23079000000000,-30.51042000000000,4.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq4IGxUCKcqxF3g_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("Sketcher::SketchObject","Sketch_Fq4IGxUCKcqxF3g_1_JNC")
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq4IGxUCKcqxF3g_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.45000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Pocket","Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC")
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JNC")
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Plane", "plane_Sketch_Fq4IGxUCKcqxF3g_1_JPC")
origin = App.Vector(-40.19059000000000,28.48958000000000,4.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq4IGxUCKcqxF3g_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("Sketcher::SketchObject","Sketch_Fq4IGxUCKcqxF3g_1_JPC")
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq4IGxUCKcqxF3g_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JPC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.45000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Pocket","Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC")
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JPC")
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Plane", "plane_Sketch_Fq4IGxUCKcqxF3g_1_JRC")
origin = App.Vector(39.76921000000000,-30.51179000000000,4.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq4IGxUCKcqxF3g_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("Sketcher::SketchObject","Sketch_Fq4IGxUCKcqxF3g_1_JRC")
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq4IGxUCKcqxF3g_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.45000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Pocket","Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC")
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JRC")
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Plane", "plane_Sketch_Fq4IGxUCKcqxF3g_1_JTC")
origin = App.Vector(39.80941000000001,28.48821000000000,4.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq4IGxUCKcqxF3g_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("Sketcher::SketchObject","Sketch_Fq4IGxUCKcqxF3g_1_JTC")
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq4IGxUCKcqxF3g_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JTC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.45000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkDQ6NAbUG3lmW5_0").newObject("PartDesign::Pocket","Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC")
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JTC")
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq4IGxUCKcqxF3g_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq4IGxUCKcqxF3g_1_FBJiIW5xP4jsFnt_1_JTC").Offset = 0
App.ActiveDocument.recompute()

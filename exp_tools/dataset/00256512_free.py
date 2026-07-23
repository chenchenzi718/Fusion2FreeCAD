import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00256512")
App.ActiveDocument.addObject("PartDesign::Body","Body_FQGksFUmsqsRUL5_0")
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").Label = "Body_FQGksFUmsqsRUL5_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Plane", "plane_Sketch_FQGksFUmsqsRUL5_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQGksFUmsqsRUL5_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("Sketcher::SketchObject","Sketch_FQGksFUmsqsRUL5_0_JGC")
App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQGksFUmsqsRUL5_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-62.07220000000000,36.57974000000000,0.00000000000000),App.Vector(52.42251000000000,36.57974000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC").addGeometry(Part.LineSegment(App.Vector(52.42251000000000,36.57974000000000,0.00000000000000),App.Vector(52.42251000000000,-26.05731000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC").addGeometry(Part.LineSegment(App.Vector(52.42251000000000,-26.05731000000000,0.00000000000000),App.Vector(-62.07220000000000,-26.05731000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-62.07220000000000,36.57974000000000,0.00000000000000),App.Vector(-62.07220000000000,-26.05731000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Pad","Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC")
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC")
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQGksFUmsqsRUL5_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQGksFUmsqsRUL5_0_FdaKG6s59suyJoj_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Plane", "plane_Sketch_F3l9X4CJa6xRsBf_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3l9X4CJa6xRsBf_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("Sketcher::SketchObject","Sketch_F3l9X4CJa6xRsBf_1_JJC")
App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3l9X4CJa6xRsBf_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJC").addGeometry(Part.Circle(App.Vector(13.09227000000000,4.24154000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.79514000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Pocket","Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC")
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJC")
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").Length = 116.84
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Plane", "plane_Sketch_F3l9X4CJa6xRsBf_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3l9X4CJa6xRsBf_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("Sketcher::SketchObject","Sketch_F3l9X4CJa6xRsBf_1_JJK")
App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3l9X4CJa6xRsBf_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJK").addGeometry(Part.Circle(App.Vector(-28.56866000000000,5.40688000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.79514000000000),False)

App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJK").addGeometry(Part.Circle(App.Vector(-28.56866000000000,5.40688000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.84121000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Pocket","Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK")
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJK")
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").Length = 116.84
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Plane", "plane_Sketch_F3l9X4CJa6xRsBf_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3l9X4CJa6xRsBf_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("Sketcher::SketchObject","Sketch_F3l9X4CJa6xRsBf_1_JJG")
App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3l9X4CJa6xRsBf_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJG").addGeometry(Part.Circle(App.Vector(-28.56866000000000,5.40688000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.79514000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Pocket","Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG")
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJG")
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").Length = 116.84
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3l9X4CJa6xRsBf_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3l9X4CJa6xRsBf_1_F9tTkPMnRrJkziN_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Plane", "plane_Sketch_F4iBZxB2gHZiVxs_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4iBZxB2gHZiVxs_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("Sketcher::SketchObject","Sketch_F4iBZxB2gHZiVxs_1_JNC")
App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4iBZxB2gHZiVxs_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC").addGeometry(Part.LineSegment(App.Vector(-42.86079000000000,36.28576000000000,0.00000000000000),App.Vector(-42.86079000000000,-25.60831000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC").addGeometry(Part.LineSegment(App.Vector(-42.86079000000000,-25.60831000000000,0.00000000000000),App.Vector(-62.28499000000000,-26.40905000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC").addGeometry(Part.LineSegment(App.Vector(-62.28499000000000,-26.40905000000000,0.00000000000000),App.Vector(-62.28499000000000,36.47270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC").addGeometry(Part.LineSegment(App.Vector(-42.86079000000000,36.28576000000000,0.00000000000000),App.Vector(-62.28499000000000,36.47270000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Pad","Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC")
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC")
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").Length = 42.926
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4iBZxB2gHZiVxs_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4iBZxB2gHZiVxs_1_FzlIPN3183tUWJq_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Plane", "plane_Sketch_F5YrrHMLGVCYEQm_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5YrrHMLGVCYEQm_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("Sketcher::SketchObject","Sketch_F5YrrHMLGVCYEQm_1_JRC")
App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5YrrHMLGVCYEQm_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC").addGeometry(Part.LineSegment(App.Vector(-62.08427000000000,-26.08705000000000,0.00000000000000),App.Vector(-10.49311000000000,-26.08705000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC").addGeometry(Part.LineSegment(App.Vector(-10.49311000000000,-26.08705000000000,0.00000000000000),App.Vector(-10.49311000000000,36.58016000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC").addGeometry(Part.LineSegment(App.Vector(-10.49311000000000,36.58016000000000,0.00000000000000),App.Vector(-62.08427000000000,36.58016000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC").addGeometry(Part.LineSegment(App.Vector(-62.08427000000000,-26.08705000000000,0.00000000000000),App.Vector(-62.08427000000000,36.58016000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Pad","Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC")
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC")
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").Length = 11.176
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5YrrHMLGVCYEQm_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5YrrHMLGVCYEQm_1_F2lPA4YlMMAAZ9v_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Plane", "plane_Sketch_Fe5rlEykRvggTiU_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fe5rlEykRvggTiU_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("Sketcher::SketchObject","Sketch_Fe5rlEykRvggTiU_1_JVC")
App.ActiveDocument.getObject("Sketch_Fe5rlEykRvggTiU_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fe5rlEykRvggTiU_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fe5rlEykRvggTiU_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fe5rlEykRvggTiU_1_JVC").addGeometry(Part.Circle(App.Vector(-26.23279000000000,2.56363000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.84701000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fe5rlEykRvggTiU_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fe5rlEykRvggTiU_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Pocket","Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC")
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fe5rlEykRvggTiU_1_JVC")
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").Length = 65.53200000000001
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fe5rlEykRvggTiU_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fe5rlEykRvggTiU_1_FWwr9xUHKxE77Zr_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Plane", "plane_Sketch_FTrhDVXLFCDXIxy_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTrhDVXLFCDXIxy_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("Sketcher::SketchObject","Sketch_FTrhDVXLFCDXIxy_1_JZC")
App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTrhDVXLFCDXIxy_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC").addGeometry(Part.LineSegment(App.Vector(51.88262000000000,-5.68377000000000,0.00000000000000),App.Vector(33.22820000000000,-5.68377000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC").addGeometry(Part.LineSegment(App.Vector(33.22820000000000,-5.68377000000000,0.00000000000000),App.Vector(33.22820000000000,-25.79558000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC").addGeometry(Part.LineSegment(App.Vector(33.22820000000000,-25.79558000000000,0.00000000000000),App.Vector(51.88262000000000,-25.79558000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC").addGeometry(Part.LineSegment(App.Vector(51.88262000000000,-5.68377000000000,0.00000000000000),App.Vector(51.88262000000000,-25.79558000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Pad","Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC")
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC")
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").Length = 45.212
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Plane", "plane_Sketch_FTrhDVXLFCDXIxy_1_JZG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTrhDVXLFCDXIxy_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("Sketcher::SketchObject","Sketch_FTrhDVXLFCDXIxy_1_JZG")
App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTrhDVXLFCDXIxy_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG").addGeometry(Part.LineSegment(App.Vector(33.22820000000000,36.58016000000000,0.00000000000000),App.Vector(33.22820000000000,19.09164000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG").addGeometry(Part.LineSegment(App.Vector(33.22820000000000,19.09164000000000,0.00000000000000),App.Vector(51.88262000000000,19.09164000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG").addGeometry(Part.LineSegment(App.Vector(51.88262000000000,19.09164000000000,0.00000000000000),App.Vector(51.88262000000000,36.58016000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG").addGeometry(Part.LineSegment(App.Vector(33.22820000000000,36.58016000000000,0.00000000000000),App.Vector(51.88262000000000,36.58016000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGksFUmsqsRUL5_0").newObject("PartDesign::Pad","Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG")
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG")
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").Length = 45.212
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTrhDVXLFCDXIxy_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTrhDVXLFCDXIxy_1_FQRyx54TaymYLKQ_1_JZG").Offset = 0
App.ActiveDocument.recompute()

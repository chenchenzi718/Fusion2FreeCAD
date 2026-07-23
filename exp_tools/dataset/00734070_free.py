import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00734070")
App.ActiveDocument.addObject("PartDesign::Body","Body_FeIUGQG3DwDX4SA_0")
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").Label = "Body_FeIUGQG3DwDX4SA_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Plane", "plane_Sketch_FeIUGQG3DwDX4SA_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeIUGQG3DwDX4SA_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("Sketcher::SketchObject","Sketch_FeIUGQG3DwDX4SA_0_JGC")
App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeIUGQG3DwDX4SA_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-30.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-30.00000000000000,0.00000000000000),App.Vector(60.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,30.00000000000000,0.00000000000000),App.Vector(60.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-30.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Pad","Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC")
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC")
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").Length = 34.0
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeIUGQG3DwDX4SA_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeIUGQG3DwDX4SA_0_FjNdMJ4QfjxxlhE_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Plane", "plane_Sketch_FuaxuFqWPpzfaBe_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,34.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuaxuFqWPpzfaBe_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("Sketcher::SketchObject","Sketch_FuaxuFqWPpzfaBe_1_JJC")
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuaxuFqWPpzfaBe_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-60.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Pocket","Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC")
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJC")
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").Length = 15.0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Plane", "plane_Sketch_FuaxuFqWPpzfaBe_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,34.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuaxuFqWPpzfaBe_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("Sketcher::SketchObject","Sketch_FuaxuFqWPpzfaBe_1_JJG")
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuaxuFqWPpzfaBe_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(60.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJG").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(60.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Pocket","Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG")
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJG")
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").Length = 15.0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Plane", "plane_Sketch_FuaxuFqWPpzfaBe_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,34.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuaxuFqWPpzfaBe_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("Sketcher::SketchObject","Sketch_FuaxuFqWPpzfaBe_1_JJK")
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuaxuFqWPpzfaBe_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-60.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJK").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Pocket","Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK")
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJK")
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").Length = 15.0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Plane", "plane_Sketch_FuaxuFqWPpzfaBe_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,34.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuaxuFqWPpzfaBe_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("Sketcher::SketchObject","Sketch_FuaxuFqWPpzfaBe_1_JJO")
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuaxuFqWPpzfaBe_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(60.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJO").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(60.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Pocket","Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO")
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJO")
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").Length = 15.0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuaxuFqWPpzfaBe_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuaxuFqWPpzfaBe_1_FHnZknwOfZNmZiH_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Plane", "plane_Sketch_FmVzgR8HbolevTH_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,34.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmVzgR8HbolevTH_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("Sketcher::SketchObject","Sketch_FmVzgR8HbolevTH_1_JNG")
App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmVzgR8HbolevTH_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").addGeometry(Part.LineSegment(App.Vector(-29.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(29.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(29.00000000000000,-14.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-14.00000000000000,0.00000000000000),App.Vector(35.00000000000000,14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(29.00000000000000,14.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").addGeometry(Part.LineSegment(App.Vector(29.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-29.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-29.00000000000000,14.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").addGeometry(Part.LineSegment(App.Vector(-35.00000000000000,14.00000000000000,0.00000000000000),App.Vector(-35.00000000000000,-14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-29.00000000000000,-14.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Pad","Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG")
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG")
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").Length = 16.0
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmVzgR8HbolevTH_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmVzgR8HbolevTH_1_Fv3ckzKOY3WFTX4_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Plane", "plane_Sketch_F1FtkCryluIPeVD_1_JRC")
origin = App.Vector(-0.00000000000000,0.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1FtkCryluIPeVD_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("Sketcher::SketchObject","Sketch_F1FtkCryluIPeVD_1_JRC")
App.ActiveDocument.getObject("Sketch_F1FtkCryluIPeVD_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1FtkCryluIPeVD_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F1FtkCryluIPeVD_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1FtkCryluIPeVD_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1FtkCryluIPeVD_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1FtkCryluIPeVD_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Pocket","Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC")
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F1FtkCryluIPeVD_1_JRC")
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").Length = 38.0
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1FtkCryluIPeVD_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1FtkCryluIPeVD_1_Fzi32XSFWqUVJg2_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Plane", "plane_Sketch_F1fFu6AjoJjfnJA_1_JVG")
origin = App.Vector(0.00000000000000,30.00000000000000,17.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1fFu6AjoJjfnJA_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("Sketcher::SketchObject","Sketch_F1fFu6AjoJjfnJA_1_JVG")
App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1fFu6AjoJjfnJA_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-17.00000000000000,0.00000000000000),App.Vector(-20.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-17.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-17.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-17.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeIUGQG3DwDX4SA_0").newObject("PartDesign::Pocket","Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG")
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG")
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").Length = 60.0
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1fFu6AjoJjfnJA_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1fFu6AjoJjfnJA_1_FMNuhoPwXAVjD4m_1_JVG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00408869")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fk1KvyOrVmIzjHD_0")
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").Label = "Body_Fk1KvyOrVmIzjHD_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Plane", "plane_Sketch_Fk1KvyOrVmIzjHD_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk1KvyOrVmIzjHD_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("Sketcher::SketchObject","Sketch_Fk1KvyOrVmIzjHD_0_JGC")
App.ActiveDocument.getObject("Sketch_Fk1KvyOrVmIzjHD_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk1KvyOrVmIzjHD_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fk1KvyOrVmIzjHD_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk1KvyOrVmIzjHD_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.57500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk1KvyOrVmIzjHD_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk1KvyOrVmIzjHD_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Pad","Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC")
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fk1KvyOrVmIzjHD_0_JGC")
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").Length = 26.5
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk1KvyOrVmIzjHD_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk1KvyOrVmIzjHD_0_Ffzl0if6wP8QpDE_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Plane", "plane_Sketch_FMpeB9N5y1khszY_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("Sketcher::SketchObject","Sketch_FMpeB9N5y1khszY_1_JJK")
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJK").addGeometry(Part.LineSegment(App.Vector(4.98577000000000,0.37699000000000,0.00000000000000),App.Vector(2.38406000000000,1.62776000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJK").addGeometry(Part.LineSegment(App.Vector(2.38406000000000,1.62776000000000,0.00000000000000),App.Vector(2.60171000000000,-1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJK").addGeometry(Part.LineSegment(App.Vector(4.98577000000000,0.37699000000000,0.00000000000000),App.Vector(2.60171000000000,-1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Pocket","Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJK")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").Length = 26.5
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Plane", "plane_Sketch_FMpeB9N5y1khszY_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("Sketcher::SketchObject","Sketch_FMpeB9N5y1khszY_1_JJO")
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJO").addGeometry(Part.LineSegment(App.Vector(2.60171000000000,-1.25077000000000,0.00000000000000),App.Vector(0.21766000000000,-2.87853000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJO").addGeometry(Part.LineSegment(App.Vector(2.81937000000000,-4.12931000000000,0.00000000000000),App.Vector(0.21766000000000,-2.87853000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJO").addGeometry(Part.LineSegment(App.Vector(2.81937000000000,-4.12931000000000,0.00000000000000),App.Vector(2.60171000000000,-1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Pocket","Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJO")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").Length = 26.5
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Plane", "plane_Sketch_FMpeB9N5y1khszY_1_JJS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("Sketcher::SketchObject","Sketch_FMpeB9N5y1khszY_1_JJS")
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJS").addGeometry(Part.LineSegment(App.Vector(-2.16640000000000,-4.50630000000000,0.00000000000000),App.Vector(0.21766000000000,-2.87853000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJS").addGeometry(Part.LineSegment(App.Vector(0.21766000000000,-2.87853000000000,0.00000000000000),App.Vector(-2.38406000000000,-1.62776000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJS").addGeometry(Part.LineSegment(App.Vector(-2.16640000000000,-4.50630000000000,0.00000000000000),App.Vector(-2.38406000000000,-1.62776000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Pocket","Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJS")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").Length = 26.5
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Plane", "plane_Sketch_FMpeB9N5y1khszY_1_JJW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("Sketcher::SketchObject","Sketch_FMpeB9N5y1khszY_1_JJW")
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJW").addGeometry(Part.LineSegment(App.Vector(-2.38406000000000,-1.62776000000000,0.00000000000000),App.Vector(-2.60171000000000,1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJW").addGeometry(Part.LineSegment(App.Vector(-4.98577000000000,-0.37699000000000,0.00000000000000),App.Vector(-2.60171000000000,1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJW").addGeometry(Part.LineSegment(App.Vector(-4.98577000000000,-0.37699000000000,0.00000000000000),App.Vector(-2.38406000000000,-1.62776000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Pocket","Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJW")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").Length = 26.5
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Plane", "plane_Sketch_FMpeB9N5y1khszY_1_JJe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("Sketcher::SketchObject","Sketch_FMpeB9N5y1khszY_1_JJe")
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJe"), [""])
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").addGeometry(Part.LineSegment(App.Vector(-0.21766000000000,2.87853000000000,0.00000000000000),App.Vector(2.38406000000000,1.62776000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").addGeometry(Part.LineSegment(App.Vector(2.38406000000000,1.62776000000000,0.00000000000000),App.Vector(2.60171000000000,-1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").addGeometry(Part.LineSegment(App.Vector(2.60171000000000,-1.25077000000000,0.00000000000000),App.Vector(0.21766000000000,-2.87853000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").addGeometry(Part.LineSegment(App.Vector(0.21766000000000,-2.87853000000000,0.00000000000000),App.Vector(-2.38406000000000,-1.62776000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").addGeometry(Part.LineSegment(App.Vector(-2.38406000000000,-1.62776000000000,0.00000000000000),App.Vector(-2.60171000000000,1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").addGeometry(Part.LineSegment(App.Vector(-0.21766000000000,2.87853000000000,0.00000000000000),App.Vector(-2.60171000000000,1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Pocket","Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").Profile = App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").Length = 26.5
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").Type = 4
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Plane", "plane_Sketch_FMpeB9N5y1khszY_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("Sketcher::SketchObject","Sketch_FMpeB9N5y1khszY_1_JJG")
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJG").addGeometry(Part.LineSegment(App.Vector(-0.21766000000000,2.87853000000000,0.00000000000000),App.Vector(2.38406000000000,1.62776000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJG").addGeometry(Part.LineSegment(App.Vector(2.16640000000000,4.50630000000000,0.00000000000000),App.Vector(2.38406000000000,1.62776000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJG").addGeometry(Part.LineSegment(App.Vector(2.16640000000000,4.50630000000000,0.00000000000000),App.Vector(-0.21766000000000,2.87853000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Pocket","Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJG")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").Length = 26.5
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Plane", "plane_Sketch_FMpeB9N5y1khszY_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("Sketcher::SketchObject","Sketch_FMpeB9N5y1khszY_1_JJC")
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMpeB9N5y1khszY_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJC").addGeometry(Part.LineSegment(App.Vector(-2.81937000000000,4.12931000000000,0.00000000000000),App.Vector(-0.21766000000000,2.87853000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJC").addGeometry(Part.LineSegment(App.Vector(-0.21766000000000,2.87853000000000,0.00000000000000),App.Vector(-2.60171000000000,1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJC").addGeometry(Part.LineSegment(App.Vector(-2.81937000000000,4.12931000000000,0.00000000000000),App.Vector(-2.60171000000000,1.25077000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fk1KvyOrVmIzjHD_0").newObject("PartDesign::Pocket","Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJC")
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").Length = 26.5
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMpeB9N5y1khszY_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMpeB9N5y1khszY_1_F9eSKLdUZ6cZTDj_1_JJC").Offset = 0
App.ActiveDocument.recompute()

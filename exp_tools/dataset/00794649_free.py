import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00794649")
App.ActiveDocument.addObject("PartDesign::Body","Body_F19WqvGwZow8o4M_0")
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").Label = "Body_F19WqvGwZow8o4M_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Plane", "plane_Sketch_F19WqvGwZow8o4M_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F19WqvGwZow8o4M_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("Sketcher::SketchObject","Sketch_F19WqvGwZow8o4M_0_JGC")
App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F19WqvGwZow8o4M_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC").addGeometry(Part.LineSegment(App.Vector(-49.29182000000000,33.27628000000000,0.00000000000000),App.Vector(25.70818000000000,33.27628000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.70818000000000,33.27628000000000,0.00000000000000),App.Vector(25.70818000000000,-41.72372000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC").addGeometry(Part.LineSegment(App.Vector(-49.29182000000000,-41.72372000000000,0.00000000000000),App.Vector(25.70818000000000,-41.72372000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC").addGeometry(Part.LineSegment(App.Vector(-49.29182000000000,33.27628000000000,0.00000000000000),App.Vector(-49.29182000000000,-41.72372000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Pad","Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC")
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC")
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").Length = 75.0
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F19WqvGwZow8o4M_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F19WqvGwZow8o4M_0_FEkOyV0axgKT95g_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Plane", "plane_Sketch_FS7ognPGkzr7Dbf_1_JLC")
origin = App.Vector(-11.79182000000000,-4.22372000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS7ognPGkzr7Dbf_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("Sketcher::SketchObject","Sketch_FS7ognPGkzr7Dbf_1_JLC")
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS7ognPGkzr7Dbf_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,-37.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,-12.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(-37.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Pocket","Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC")
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC")
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Plane", "plane_Sketch_FS7ognPGkzr7Dbf_1_JLG")
origin = App.Vector(-11.79182000000000,-4.22372000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS7ognPGkzr7Dbf_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("Sketcher::SketchObject","Sketch_FS7ognPGkzr7Dbf_1_JLG")
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS7ognPGkzr7Dbf_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(12.50000000000000,-37.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(12.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-12.50000000000000,0.00000000000000),App.Vector(12.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(37.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Pocket","Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG")
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG")
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Plane", "plane_Sketch_FS7ognPGkzr7Dbf_1_JLK")
origin = App.Vector(-11.79182000000000,-4.22372000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS7ognPGkzr7Dbf_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("Sketcher::SketchObject","Sketch_FS7ognPGkzr7Dbf_1_JLK")
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS7ognPGkzr7Dbf_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,37.50000000000000,0.00000000000000),App.Vector(12.50000000000000,37.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,37.50000000000000,0.00000000000000),App.Vector(12.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,12.50000000000000,0.00000000000000),App.Vector(12.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,37.50000000000000,0.00000000000000),App.Vector(37.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Pocket","Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK")
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK")
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Plane", "plane_Sketch_FS7ognPGkzr7Dbf_1_JLO")
origin = App.Vector(-11.79182000000000,-4.22372000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS7ognPGkzr7Dbf_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("Sketcher::SketchObject","Sketch_FS7ognPGkzr7Dbf_1_JLO")
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS7ognPGkzr7Dbf_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,37.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,37.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,37.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,12.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,37.50000000000000,0.00000000000000),App.Vector(-37.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Pocket","Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO")
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO")
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS7ognPGkzr7Dbf_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS7ognPGkzr7Dbf_1_FnfXOR8btnpHGmk_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Plane", "plane_Sketch_Fjw5xU3LLusm5j3_1_JPC")
origin = App.Vector(-11.79182000000000,-4.22372000000000,75.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fjw5xU3LLusm5j3_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("Sketcher::SketchObject","Sketch_Fjw5xU3LLusm5j3_1_JPC")
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fjw5xU3LLusm5j3_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,37.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,37.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,37.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,12.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,37.50000000000000,0.00000000000000),App.Vector(-37.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Pocket","Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC")
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC")
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Plane", "plane_Sketch_Fjw5xU3LLusm5j3_1_JPG")
origin = App.Vector(-11.79182000000000,-4.22372000000000,75.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fjw5xU3LLusm5j3_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("Sketcher::SketchObject","Sketch_Fjw5xU3LLusm5j3_1_JPG")
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fjw5xU3LLusm5j3_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,37.50000000000000,0.00000000000000),App.Vector(12.50000000000000,37.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,37.50000000000000,0.00000000000000),App.Vector(12.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,12.50000000000000,0.00000000000000),App.Vector(12.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,37.50000000000000,0.00000000000000),App.Vector(37.50000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Pocket","Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG")
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG")
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Plane", "plane_Sketch_Fjw5xU3LLusm5j3_1_JPK")
origin = App.Vector(-11.79182000000000,-4.22372000000000,75.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fjw5xU3LLusm5j3_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("Sketcher::SketchObject","Sketch_Fjw5xU3LLusm5j3_1_JPK")
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fjw5xU3LLusm5j3_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,-37.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,-12.50000000000000,0.00000000000000),App.Vector(-12.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(-37.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Pocket","Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK")
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK")
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Plane", "plane_Sketch_Fjw5xU3LLusm5j3_1_JPO")
origin = App.Vector(-11.79182000000000,-4.22372000000000,75.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fjw5xU3LLusm5j3_1_JPO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("Sketcher::SketchObject","Sketch_Fjw5xU3LLusm5j3_1_JPO")
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fjw5xU3LLusm5j3_1_JPO"), [""])
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(12.50000000000000,-37.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(12.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-12.50000000000000,0.00000000000000),App.Vector(12.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-37.50000000000000,0.00000000000000),App.Vector(37.50000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F19WqvGwZow8o4M_0").newObject("PartDesign::Pocket","Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO")
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").Profile = App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO")
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fjw5xU3LLusm5j3_1_JPO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").Type = 4
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fjw5xU3LLusm5j3_1_F3HHMAczmYuevQm_1_JPO").Offset = 0
App.ActiveDocument.recompute()

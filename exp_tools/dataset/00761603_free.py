import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00761603")
App.ActiveDocument.addObject("PartDesign::Body","Body_FUsarj8N4ailOP6_0")
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").Label = "Body_FUsarj8N4ailOP6_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Plane", "plane_Sketch_FUsarj8N4ailOP6_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUsarj8N4ailOP6_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("Sketcher::SketchObject","Sketch_FUsarj8N4ailOP6_0_JGC")
App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUsarj8N4ailOP6_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-33.02000000000000,0.00000000000000),App.Vector(-25.40000000000000,-33.02000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-33.02000000000000,0.00000000000000),App.Vector(-25.40000000000000,33.02000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,33.02000000000000,0.00000000000000),App.Vector(-25.40000000000000,33.02000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-33.02000000000000,0.00000000000000),App.Vector(25.40000000000000,33.02000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Pad","Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC")
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC")
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").Length = 3.5
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUsarj8N4ailOP6_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUsarj8N4ailOP6_0_FLam4O6isI2HEG0_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Plane", "plane_Sketch_FWV0pbtnPIx8QT8_1_JJC")
origin = App.Vector(-0.00000000000000,15.57700000000000,3.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWV0pbtnPIx8QT8_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("Sketcher::SketchObject","Sketch_FWV0pbtnPIx8QT8_1_JJC")
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWV0pbtnPIx8QT8_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJC").addGeometry(Part.Circle(App.Vector(-22.25000000000000,12.23600000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Pocket","Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC")
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJC")
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Plane", "plane_Sketch_FWV0pbtnPIx8QT8_1_JJG")
origin = App.Vector(-0.00000000000000,15.57700000000000,3.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWV0pbtnPIx8QT8_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("Sketcher::SketchObject","Sketch_FWV0pbtnPIx8QT8_1_JJG")
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWV0pbtnPIx8QT8_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJG").addGeometry(Part.Circle(App.Vector(-22.25000000000000,-44.91399999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Pocket","Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG")
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJG")
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Plane", "plane_Sketch_FWV0pbtnPIx8QT8_1_JJK")
origin = App.Vector(-0.00000000000000,15.57700000000000,3.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWV0pbtnPIx8QT8_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("Sketcher::SketchObject","Sketch_FWV0pbtnPIx8QT8_1_JJK")
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWV0pbtnPIx8QT8_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJK").addGeometry(Part.Circle(App.Vector(22.25000000000000,12.23600000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Pocket","Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK")
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJK")
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Plane", "plane_Sketch_FWV0pbtnPIx8QT8_1_JJO")
origin = App.Vector(-0.00000000000000,15.57700000000000,3.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWV0pbtnPIx8QT8_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("Sketcher::SketchObject","Sketch_FWV0pbtnPIx8QT8_1_JJO")
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWV0pbtnPIx8QT8_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJO").addGeometry(Part.Circle(App.Vector(22.25000000000000,-44.91399999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Pocket","Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO")
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJO")
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWV0pbtnPIx8QT8_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWV0pbtnPIx8QT8_1_FPevpVLYFEuG24K_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Plane", "plane_Sketch_FBAO1OIlEd0toQn_1_JNC")
origin = App.Vector(-0.00000000000000,15.57700000000000,3.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBAO1OIlEd0toQn_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("Sketcher::SketchObject","Sketch_FBAO1OIlEd0toQn_1_JNC")
App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBAO1OIlEd0toQn_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC").addGeometry(Part.LineSegment(App.Vector(-7.50000000000000,14.94300000000000,0.00000000000000),App.Vector(12.82000000000000,14.94300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC").addGeometry(Part.LineSegment(App.Vector(12.82000000000000,14.94300000000000,0.00000000000000),App.Vector(12.82000000000000,6.43400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC").addGeometry(Part.LineSegment(App.Vector(12.82000000000000,6.43400000000000,0.00000000000000),App.Vector(-7.50000000000000,6.43400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC").addGeometry(Part.LineSegment(App.Vector(-7.50000000000000,14.94300000000000,0.00000000000000),App.Vector(-7.50000000000000,6.43400000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Pad","Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC")
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC")
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").Length = 10.16
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBAO1OIlEd0toQn_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBAO1OIlEd0toQn_1_FCZaxxVjFryX3VE_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Plane", "plane_Sketch_FxeRfkOJ4SlTnk9_1_JRC")
origin = App.Vector(0.00000000000000,15.57700000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxeRfkOJ4SlTnk9_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("Sketcher::SketchObject","Sketch_FxeRfkOJ4SlTnk9_1_JRC")
App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxeRfkOJ4SlTnk9_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,48.59700000000000,0.00000000000000),App.Vector(40.38600000000000,48.59700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC").addGeometry(Part.LineSegment(App.Vector(40.38600000000000,48.59700000000000,0.00000000000000),App.Vector(40.38600000000000,-17.44300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-17.44300000000000,0.00000000000000),App.Vector(40.38600000000000,-17.44300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,48.59700000000000,0.00000000000000),App.Vector(25.40000000000000,-17.44300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Pad","Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC")
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC")
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Plane", "plane_Sketch_FxeRfkOJ4SlTnk9_1_JRG")
origin = App.Vector(0.00000000000000,15.57700000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxeRfkOJ4SlTnk9_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("Sketcher::SketchObject","Sketch_FxeRfkOJ4SlTnk9_1_JRG")
App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxeRfkOJ4SlTnk9_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,48.59700000000000,0.00000000000000),App.Vector(-25.40000000000000,-17.44300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-17.44300000000000,0.00000000000000),App.Vector(-40.38600000000000,-17.44300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG").addGeometry(Part.LineSegment(App.Vector(-40.38600000000000,48.59700000000000,0.00000000000000),App.Vector(-40.38600000000000,-17.44300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,48.59700000000000,0.00000000000000),App.Vector(-40.38600000000000,48.59700000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUsarj8N4ailOP6_0").newObject("PartDesign::Pad","Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG")
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG")
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").Length = 20.0
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxeRfkOJ4SlTnk9_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").Type = 0
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxeRfkOJ4SlTnk9_1_FTG0ZW1X0vKbyH7_1_JRG").Offset = 0
App.ActiveDocument.recompute()

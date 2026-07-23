import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00660538")
App.ActiveDocument.addObject("PartDesign::Body","Body_FH29XKtOHYS8J8L_0")
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").Label = "Body_FH29XKtOHYS8J8L_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Plane", "plane_Sketch_FH29XKtOHYS8J8L_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("Sketcher::SketchObject","Sketch_FH29XKtOHYS8J8L_0_JGC")
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC").addGeometry(Part.LineSegment(App.Vector(13.04979000000000,7.53430000000000,0.00000000000000),App.Vector(23.04979000000000,-9.78621000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC").addGeometry(Part.LineSegment(App.Vector(23.04979000000000,-9.78621000000000,0.00000000000000),App.Vector(10.00000000000000,-17.32051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(10.00000000000000,-17.32051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(13.04979000000000,7.53430000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Pad","Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Plane", "plane_Sketch_FH29XKtOHYS8J8L_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("Sketcher::SketchObject","Sketch_FH29XKtOHYS8J8L_0_JGG")
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,15.06860000000000,0.00000000000000),App.Vector(8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,15.06860000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Pad","Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGG")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Plane", "plane_Sketch_FH29XKtOHYS8J8L_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("Sketcher::SketchObject","Sketch_FH29XKtOHYS8J8L_0_JGK")
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-15.06860000000000,0.00000000000000),App.Vector(-8.69986000000000,-15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-8.69986000000000,-15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Pad","Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGK")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Plane", "plane_Sketch_FH29XKtOHYS8J8L_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("Sketcher::SketchObject","Sketch_FH29XKtOHYS8J8L_0_JGO")
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,15.06860000000000,0.00000000000000),App.Vector(8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,17.32051000000000,0.00000000000000),App.Vector(8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").addGeometry(Part.LineSegment(App.Vector(-3.04979000000000,24.85481000000000,0.00000000000000),App.Vector(10.00000000000000,17.32051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").addGeometry(Part.LineSegment(App.Vector(-3.04979000000000,24.85481000000000,0.00000000000000),App.Vector(-8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,15.06860000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Pad","Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Plane", "plane_Sketch_FH29XKtOHYS8J8L_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("Sketcher::SketchObject","Sketch_FH29XKtOHYS8J8L_0_JGS")
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").addGeometry(Part.LineSegment(App.Vector(-13.04979000000000,7.53430000000000,0.00000000000000),App.Vector(-8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,17.32051000000000,0.00000000000000),App.Vector(-8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").addGeometry(Part.LineSegment(App.Vector(-23.04979000000000,9.78621000000000,0.00000000000000),App.Vector(-10.00000000000000,17.32051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").addGeometry(Part.LineSegment(App.Vector(-23.04979000000000,9.78621000000000,0.00000000000000),App.Vector(-17.39972000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-17.39972000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-13.04979000000000,7.53430000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Pad","Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").Profile = App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Plane", "plane_Sketch_FH29XKtOHYS8J8L_0_JGW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("Sketcher::SketchObject","Sketch_FH29XKtOHYS8J8L_0_JGW")
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGW"), [""])
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGW").addGeometry(Part.LineSegment(App.Vector(-13.04979000000000,7.53430000000000,0.00000000000000),App.Vector(-8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGW").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-8.69986000000000,15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGW").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-13.04979000000000,7.53430000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Pad","Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").Profile = App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGW")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").Type = 4
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Plane", "plane_Sketch_FH29XKtOHYS8J8L_0_JGa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("Sketcher::SketchObject","Sketch_FH29XKtOHYS8J8L_0_JGa")
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGa"), [""])
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").addGeometry(Part.LineSegment(App.Vector(-13.04979000000000,-7.53430000000000,0.00000000000000),App.Vector(-17.39972000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-17.39972000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-15.06860000000000,0.00000000000000),App.Vector(-20.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-15.06860000000000,0.00000000000000),App.Vector(-8.69986000000000,-15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-8.69986000000000,-15.06860000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-13.04979000000000,-7.53430000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Pad","Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").Profile = App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").Type = 4
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Plane", "plane_Sketch_FH29XKtOHYS8J8L_0_JGe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("Sketcher::SketchObject","Sketch_FH29XKtOHYS8J8L_0_JGe")
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH29XKtOHYS8J8L_0_JGe"), [""])
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGe").addGeometry(Part.LineSegment(App.Vector(-13.04979000000000,-7.53430000000000,0.00000000000000),App.Vector(-17.39972000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGe").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-17.39972000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGe").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-13.04979000000000,-7.53430000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FH29XKtOHYS8J8L_0").newObject("PartDesign::Pad","Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").Profile = App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGe")
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH29XKtOHYS8J8L_0_JGe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").Type = 4
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH29XKtOHYS8J8L_0_FguDJmEK1eWkYsZ_0_JGe").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00360489")
App.ActiveDocument.addObject("PartDesign::Body","Body_FcC2RgMZ7XEQSA6_0")
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").Label = "Body_FcC2RgMZ7XEQSA6_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Plane", "plane_Sketch_FcC2RgMZ7XEQSA6_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcC2RgMZ7XEQSA6_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("Sketcher::SketchObject","Sketch_FcC2RgMZ7XEQSA6_0_JGG")
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcC2RgMZ7XEQSA6_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,50.80000000000000,0.00000000000000),App.Vector(-50.80000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000),App.Vector(-50.80000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Pad","Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG")
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG")
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Plane", "plane_Sketch_FcC2RgMZ7XEQSA6_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcC2RgMZ7XEQSA6_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("Sketcher::SketchObject","Sketch_FcC2RgMZ7XEQSA6_0_JGC")
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcC2RgMZ7XEQSA6_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,50.80000000000000,0.00000000000000),App.Vector(50.80000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC").addGeometry(Part.LineSegment(App.Vector(50.80000000000000,50.80000000000000,0.00000000000000),App.Vector(50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Pad","Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC")
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC")
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Plane", "plane_Sketch_FcC2RgMZ7XEQSA6_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcC2RgMZ7XEQSA6_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("Sketcher::SketchObject","Sketch_FcC2RgMZ7XEQSA6_0_JGK")
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcC2RgMZ7XEQSA6_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK").addGeometry(Part.LineSegment(App.Vector(50.80000000000000,0.00000000000000,0.00000000000000),App.Vector(50.80000000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK").addGeometry(Part.LineSegment(App.Vector(50.80000000000000,-38.10000000000000,0.00000000000000),App.Vector(0.00000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Pad","Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK")
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK")
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Plane", "plane_Sketch_FcC2RgMZ7XEQSA6_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcC2RgMZ7XEQSA6_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("Sketcher::SketchObject","Sketch_FcC2RgMZ7XEQSA6_0_JGO")
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcC2RgMZ7XEQSA6_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-63.50000000000000,0.00000000000000),App.Vector(-50.80000000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,-38.10000000000000,0.00000000000000),App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Pad","Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO")
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO")
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcC2RgMZ7XEQSA6_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcC2RgMZ7XEQSA6_0_FmahXBhaImjA4Cv_0_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Plane", "plane_Sketch_Fr7dn4qlAVfQY25_1_JJC")
origin = App.Vector(0.00000000000000,-6.35000000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr7dn4qlAVfQY25_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("Sketcher::SketchObject","Sketch_Fr7dn4qlAVfQY25_1_JJC")
App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr7dn4qlAVfQY25_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,50.80000000000000,0.00000000000000),App.Vector(-44.45000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,12.70000000000000,0.00000000000000),App.Vector(-6.35000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,12.70000000000000,0.00000000000000),App.Vector(-6.35000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,50.80000000000000,0.00000000000000),App.Vector(-6.35000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Pocket","Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC")
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC")
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Plane", "plane_Sketch_Fr7dn4qlAVfQY25_1_JJG")
origin = App.Vector(0.00000000000000,-6.35000000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr7dn4qlAVfQY25_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("Sketcher::SketchObject","Sketch_Fr7dn4qlAVfQY25_1_JJG")
App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr7dn4qlAVfQY25_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,12.70000000000000,0.00000000000000),App.Vector(6.35000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,50.80000000000000,0.00000000000000),App.Vector(44.45000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,50.80000000000000,0.00000000000000),App.Vector(44.45000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,12.70000000000000,0.00000000000000),App.Vector(44.45000000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Pocket","Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG")
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG")
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr7dn4qlAVfQY25_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fr7dn4qlAVfQY25_1_Fj38dTLx3gpMoEj_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Plane", "plane_Sketch_FMpPQDPUKU0PsuN_1_JLC")
origin = App.Vector(0.00000000000000,-6.35000000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMpPQDPUKU0PsuN_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("Sketcher::SketchObject","Sketch_FMpPQDPUKU0PsuN_1_JLC")
App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMpPQDPUKU0PsuN_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,0.00000000000000,0.00000000000000),App.Vector(-44.45000000000000,-27.94000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,-27.94000000000000,0.00000000000000),App.Vector(-6.35000000000000,-46.98999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,-46.98999999999999,0.00000000000000),App.Vector(-6.35000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,0.00000000000000,0.00000000000000),App.Vector(-6.35000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Pocket","Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC")
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC")
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Plane", "plane_Sketch_FMpPQDPUKU0PsuN_1_JLG")
origin = App.Vector(0.00000000000000,-6.35000000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMpPQDPUKU0PsuN_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("Sketcher::SketchObject","Sketch_FMpPQDPUKU0PsuN_1_JLG")
App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMpPQDPUKU0PsuN_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-46.98999999999999,0.00000000000000),App.Vector(6.35000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,0.00000000000000,0.00000000000000),App.Vector(44.45000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,0.00000000000000,0.00000000000000),App.Vector(44.45000000000000,-27.94000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-46.98999999999999,0.00000000000000),App.Vector(44.45000000000000,-27.94000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcC2RgMZ7XEQSA6_0").newObject("PartDesign::Pocket","Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG")
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG")
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMpPQDPUKU0PsuN_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMpPQDPUKU0PsuN_1_FVWIXzvghPWOVLR_1_JLG").Offset = 0
App.ActiveDocument.recompute()

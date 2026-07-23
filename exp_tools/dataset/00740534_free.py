import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00740534")
App.ActiveDocument.addObject("PartDesign::Body","Body_FkvooWkJSO485yR_0")
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").Label = "Body_FkvooWkJSO485yR_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Plane", "plane_Sketch_FkvooWkJSO485yR_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkvooWkJSO485yR_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("Sketcher::SketchObject","Sketch_FkvooWkJSO485yR_0_JGC")
App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkvooWkJSO485yR_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC").addGeometry(Part.LineSegment(App.Vector(47.90576000000000,51.59668000000000,0.00000000000000),App.Vector(0.00000000000000,51.59668000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,51.59668000000000,0.00000000000000),App.Vector(0.00000000000000,-22.25508000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC").addGeometry(Part.LineSegment(App.Vector(47.90576000000000,-22.25508000000000,0.00000000000000),App.Vector(0.00000000000000,-22.25508000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC").addGeometry(Part.LineSegment(App.Vector(47.90576000000000,51.59668000000000,0.00000000000000),App.Vector(47.90576000000000,-22.25508000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Pad","Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC")
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC")
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkvooWkJSO485yR_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkvooWkJSO485yR_0_F2GLr0t8uk80d6a_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Plane", "plane_Sketch_FusJY0AfcenVhB9_1_JLC")
origin = App.Vector(28.65932000000000,-22.25508000000000,79.52583000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FusJY0AfcenVhB9_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("Sketcher::SketchObject","Sketch_FusJY0AfcenVhB9_1_JLC")
App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FusJY0AfcenVhB9_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").addGeometry(Part.LineSegment(App.Vector(-49.10793000000000,-8.18525000000001,0.00000000000000),App.Vector(-28.65932000000000,-8.18525000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").addGeometry(Part.LineSegment(App.Vector(-28.65932000000000,-3.32583000000000,0.00000000000000),App.Vector(-28.65932000000000,-8.18525000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").addGeometry(Part.LineSegment(App.Vector(19.24644000000000,-3.32583000000000,0.00000000000000),App.Vector(-28.65932000000000,-3.32583000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").addGeometry(Part.LineSegment(App.Vector(19.24644000000000,-3.32583000000000,0.00000000000000),App.Vector(19.24644000000000,-8.18525000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").addGeometry(Part.LineSegment(App.Vector(49.10793000000000,-8.18525000000001,0.00000000000000),App.Vector(19.24644000000000,-8.18525000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").addGeometry(Part.LineSegment(App.Vector(49.10793000000000,-8.18525000000001,0.00000000000000),App.Vector(9.10295000000000,79.52583000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").addGeometry(Part.LineSegment(App.Vector(-49.10793000000000,-8.18525000000001,0.00000000000000),App.Vector(9.10295000000000,79.52583000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Pad","Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC")
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC")
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").Length = 73.72905313968658
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FusJY0AfcenVhB9_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").Type = 0
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FusJY0AfcenVhB9_1_FoD5ZooeI2eUgPJ_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Plane", "plane_Sketch_FfcAb1WD0nGNwKs_1_JPC")
origin = App.Vector(28.65932000000000,-22.25508000000000,79.52583000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfcAb1WD0nGNwKs_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("Sketcher::SketchObject","Sketch_FfcAb1WD0nGNwKs_1_JPC")
App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfcAb1WD0nGNwKs_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC").addGeometry(Part.LineSegment(App.Vector(-20.76778000000000,-18.60865000000000,0.00000000000000),App.Vector(-12.94489000000000,-18.60865000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC").addGeometry(Part.LineSegment(App.Vector(-12.94489000000000,-18.60865000000000,0.00000000000000),App.Vector(-12.94489000000000,-32.98429000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC").addGeometry(Part.LineSegment(App.Vector(-20.76778000000000,-32.98429000000001,0.00000000000000),App.Vector(-12.94489000000000,-32.98429000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC").addGeometry(Part.LineSegment(App.Vector(-20.76778000000000,-18.60865000000000,0.00000000000000),App.Vector(-20.76778000000000,-32.98429000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Pocket","Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC")
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC")
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").Length = 6.529986858367919
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Plane", "plane_Sketch_FfcAb1WD0nGNwKs_1_JPG")
origin = App.Vector(28.65932000000000,-22.25508000000000,79.52583000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfcAb1WD0nGNwKs_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("Sketcher::SketchObject","Sketch_FfcAb1WD0nGNwKs_1_JPG")
App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfcAb1WD0nGNwKs_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG").addGeometry(Part.LineSegment(App.Vector(1.55788000000000,-18.34369000000000,0.00000000000000),App.Vector(9.87576000000000,-18.34369000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG").addGeometry(Part.LineSegment(App.Vector(9.87576000000000,-18.34369000000000,0.00000000000000),App.Vector(9.87576000000000,-32.35095000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG").addGeometry(Part.LineSegment(App.Vector(1.55788000000000,-32.35095000000000,0.00000000000000),App.Vector(9.87576000000000,-32.35095000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG").addGeometry(Part.LineSegment(App.Vector(1.55788000000000,-18.34369000000000,0.00000000000000),App.Vector(1.55788000000000,-32.35095000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Pocket","Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG")
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG")
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").Length = 6.529986858367919
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Plane", "plane_Sketch_FfcAb1WD0nGNwKs_1_JPK")
origin = App.Vector(28.65932000000000,-22.25508000000000,79.52583000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfcAb1WD0nGNwKs_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("Sketcher::SketchObject","Sketch_FfcAb1WD0nGNwKs_1_JPK")
App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfcAb1WD0nGNwKs_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK").addGeometry(Part.LineSegment(App.Vector(-10.74021000000000,-50.86021000000000,0.00000000000000),App.Vector(-4.70644000000000,-50.86021000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK").addGeometry(Part.LineSegment(App.Vector(-4.70644000000000,-50.86021000000000,0.00000000000000),App.Vector(-4.70644000000000,-79.52583000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK").addGeometry(Part.LineSegment(App.Vector(-4.70644000000000,-79.52583000000000,0.00000000000000),App.Vector(-10.74021000000000,-79.52583000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK").addGeometry(Part.LineSegment(App.Vector(-10.74021000000000,-50.86021000000000,0.00000000000000),App.Vector(-10.74021000000000,-79.52583000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Pocket","Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK")
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK")
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").Length = 6.529986858367919
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfcAb1WD0nGNwKs_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfcAb1WD0nGNwKs_1_FwRjwuxW85EWU6U_1_JPK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Plane", "plane_Sketch_F7Z0HOypYzbQtBH_1_JTC")
origin = App.Vector(47.90576000000000,14.67080000000000,38.10000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7Z0HOypYzbQtBH_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("Sketcher::SketchObject","Sketch_F7Z0HOypYzbQtBH_1_JTC")
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7Z0HOypYzbQtBH_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC").addGeometry(Part.LineSegment(App.Vector(-25.27720000000000,21.76892000000000,0.00000000000000),App.Vector(-14.67080000000000,21.76892000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC").addGeometry(Part.LineSegment(App.Vector(-14.67080000000000,21.76892000000000,0.00000000000000),App.Vector(-14.67080000000000,8.38578000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC").addGeometry(Part.LineSegment(App.Vector(-25.27720000000000,8.38578000000000,0.00000000000000),App.Vector(-14.67080000000000,8.38578000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC").addGeometry(Part.LineSegment(App.Vector(-25.27720000000000,21.76892000000000,0.00000000000000),App.Vector(-25.27720000000000,8.38578000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Pocket","Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC")
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC")
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Plane", "plane_Sketch_F7Z0HOypYzbQtBH_1_JTK")
origin = App.Vector(47.90576000000000,14.67080000000000,38.10000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7Z0HOypYzbQtBH_1_JTK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("Sketcher::SketchObject","Sketch_F7Z0HOypYzbQtBH_1_JTK")
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7Z0HOypYzbQtBH_1_JTK"), [""])
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK").addGeometry(Part.LineSegment(App.Vector(-25.27720000000000,-6.97423000000000,0.00000000000000),App.Vector(-14.67080000000000,-6.97423000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK").addGeometry(Part.LineSegment(App.Vector(-14.67080000000000,-6.97423000000000,0.00000000000000),App.Vector(-14.67080000000000,-19.79271000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK").addGeometry(Part.LineSegment(App.Vector(-25.27720000000000,-19.79271000000000,0.00000000000000),App.Vector(-14.67080000000000,-19.79271000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK").addGeometry(Part.LineSegment(App.Vector(-25.27720000000000,-6.97423000000000,0.00000000000000),App.Vector(-25.27720000000000,-19.79271000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Pocket","Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK")
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").Profile = App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK")
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").Type = 4
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Plane", "plane_Sketch_F7Z0HOypYzbQtBH_1_JTO")
origin = App.Vector(47.90576000000000,14.67080000000000,38.10000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7Z0HOypYzbQtBH_1_JTO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("Sketcher::SketchObject","Sketch_F7Z0HOypYzbQtBH_1_JTO")
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7Z0HOypYzbQtBH_1_JTO"), [""])
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO").addGeometry(Part.LineSegment(App.Vector(7.47594000000000,-6.97423000000000,0.00000000000000),App.Vector(18.18929000000000,-6.97423000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO").addGeometry(Part.LineSegment(App.Vector(18.18929000000000,-6.97423000000000,0.00000000000000),App.Vector(18.18929000000000,-19.79271000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO").addGeometry(Part.LineSegment(App.Vector(7.47594000000000,-19.79271000000000,0.00000000000000),App.Vector(18.18929000000000,-19.79271000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO").addGeometry(Part.LineSegment(App.Vector(7.47594000000000,-6.97423000000000,0.00000000000000),App.Vector(7.47594000000000,-19.79271000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Pocket","Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO")
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").Profile = App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO")
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").Type = 4
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Plane", "plane_Sketch_F7Z0HOypYzbQtBH_1_JTG")
origin = App.Vector(47.90576000000000,14.67080000000000,38.10000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7Z0HOypYzbQtBH_1_JTG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("Sketcher::SketchObject","Sketch_F7Z0HOypYzbQtBH_1_JTG")
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7Z0HOypYzbQtBH_1_JTG"), [""])
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG").addGeometry(Part.LineSegment(App.Vector(7.47594000000000,21.76892000000000,0.00000000000000),App.Vector(18.18929000000000,21.76892000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG").addGeometry(Part.LineSegment(App.Vector(18.18929000000000,21.76892000000000,0.00000000000000),App.Vector(18.18929000000000,8.38578000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG").addGeometry(Part.LineSegment(App.Vector(7.47594000000000,8.38578000000000,0.00000000000000),App.Vector(18.18929000000000,8.38578000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG").addGeometry(Part.LineSegment(App.Vector(7.47594000000000,21.76892000000000,0.00000000000000),App.Vector(7.47594000000000,8.38578000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkvooWkJSO485yR_0").newObject("PartDesign::Pocket","Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG")
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").Profile = App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG")
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7Z0HOypYzbQtBH_1_JTG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").Type = 4
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7Z0HOypYzbQtBH_1_F97xj4uzQFlvigQ_1_JTG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00342755")
App.ActiveDocument.addObject("PartDesign::Body","Body_FJ1C18y24bcmu4D_0")
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").Label = "Body_FJ1C18y24bcmu4D_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Plane", "plane_Sketch_FJ1C18y24bcmu4D_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ1C18y24bcmu4D_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("Sketcher::SketchObject","Sketch_FJ1C18y24bcmu4D_0_JGC")
App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ1C18y24bcmu4D_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,60.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,60.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,60.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Pad","Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC")
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC")
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ1C18y24bcmu4D_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ1C18y24bcmu4D_0_F2P1V45MSIcAmDB_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Plane", "plane_Sketch_F5miM5HbSSuLF6Y_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5miM5HbSSuLF6Y_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("Sketcher::SketchObject","Sketch_F5miM5HbSSuLF6Y_1_JJC")
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5miM5HbSSuLF6Y_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,60.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-45.00000000000000,60.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,45.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,60.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Pad","Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC")
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC")
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").Length = 20.0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Plane", "plane_Sketch_F5miM5HbSSuLF6Y_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5miM5HbSSuLF6Y_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("Sketcher::SketchObject","Sketch_F5miM5HbSSuLF6Y_1_JJG")
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5miM5HbSSuLF6Y_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG").addGeometry(Part.LineSegment(App.Vector(-45.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-45.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Pad","Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG")
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG")
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").Length = 20.0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Plane", "plane_Sketch_F5miM5HbSSuLF6Y_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5miM5HbSSuLF6Y_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("Sketcher::SketchObject","Sketch_F5miM5HbSSuLF6Y_1_JJK")
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5miM5HbSSuLF6Y_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(45.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(45.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-45.00000000000000,0.00000000000000),App.Vector(45.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Pad","Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK")
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK")
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").Length = 20.0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Plane", "plane_Sketch_F5miM5HbSSuLF6Y_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5miM5HbSSuLF6Y_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("Sketcher::SketchObject","Sketch_F5miM5HbSSuLF6Y_1_JJO")
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5miM5HbSSuLF6Y_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,60.00000000000000,0.00000000000000),App.Vector(45.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,60.00000000000000,0.00000000000000),App.Vector(45.00000000000000,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,45.00000000000000,0.00000000000000),App.Vector(45.00000000000000,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,60.00000000000000,0.00000000000000),App.Vector(60.00000000000000,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Pad","Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO")
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO")
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").Length = 20.0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5miM5HbSSuLF6Y_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5miM5HbSSuLF6Y_1_FqMQsd4balZoGCD_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Plane", "plane_Sketch_Fta4dM4lqAOvcva_1_JOC")
origin = App.Vector(-52.50000000000000,-52.50000000000000,23.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fta4dM4lqAOvcva_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("Sketcher::SketchObject","Sketch_Fta4dM4lqAOvcva_1_JOC")
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fta4dM4lqAOvcva_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,5.00000000000000,0.00000000000000),App.Vector(110.00000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC").addGeometry(Part.LineSegment(App.Vector(110.00000000000000,5.00000000000000,0.00000000000000),App.Vector(110.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(110.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,5.00000000000000,0.00000000000000),App.Vector(100.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Pad","Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC")
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC")
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Plane", "plane_Sketch_Fta4dM4lqAOvcva_1_JOG")
origin = App.Vector(-52.50000000000000,-52.50000000000000,23.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fta4dM4lqAOvcva_1_JOG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("Sketcher::SketchObject","Sketch_Fta4dM4lqAOvcva_1_JOG")
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fta4dM4lqAOvcva_1_JOG"), [""])
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,100.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,100.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,110.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,110.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,110.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,100.00000000000000,0.00000000000000),App.Vector(5.00000000000000,110.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Pad","Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG")
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").Profile = App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG")
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").Type = 4
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Plane", "plane_Sketch_Fta4dM4lqAOvcva_1_JOK")
origin = App.Vector(-52.50000000000000,-52.50000000000000,23.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fta4dM4lqAOvcva_1_JOK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("Sketcher::SketchObject","Sketch_Fta4dM4lqAOvcva_1_JOK")
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fta4dM4lqAOvcva_1_JOK"), [""])
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK").addGeometry(Part.LineSegment(App.Vector(110.00000000000000,100.00000000000000,0.00000000000000),App.Vector(100.00000000000000,100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,100.00000000000000,0.00000000000000),App.Vector(100.00000000000000,110.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK").addGeometry(Part.LineSegment(App.Vector(110.00000000000000,110.00000000000000,0.00000000000000),App.Vector(100.00000000000000,110.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK").addGeometry(Part.LineSegment(App.Vector(110.00000000000000,100.00000000000000,0.00000000000000),App.Vector(110.00000000000000,110.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Pad","Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK")
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").Profile = App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK")
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").Type = 4
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Plane", "plane_Sketch_Fta4dM4lqAOvcva_1_JOO")
origin = App.Vector(-52.50000000000000,-52.50000000000000,23.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fta4dM4lqAOvcva_1_JOO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("Sketcher::SketchObject","Sketch_Fta4dM4lqAOvcva_1_JOO")
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fta4dM4lqAOvcva_1_JOO"), [""])
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ1C18y24bcmu4D_0").newObject("PartDesign::Pad","Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO")
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").Profile = App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO")
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fta4dM4lqAOvcva_1_JOO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").Type = 4
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fta4dM4lqAOvcva_1_FUT5cPzbmTmggkv_1_JOO").Offset = 0
App.ActiveDocument.recompute()

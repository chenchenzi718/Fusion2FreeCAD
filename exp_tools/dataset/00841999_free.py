import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00841999")
App.ActiveDocument.addObject("PartDesign::Body","Body_FphDYkms1USRifU_0")
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").Label = "Body_FphDYkms1USRifU_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Plane", "plane_Sketch_FphDYkms1USRifU_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FphDYkms1USRifU_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("Sketcher::SketchObject","Sketch_FphDYkms1USRifU_0_JGC")
App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FphDYkms1USRifU_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-77.17443000000000,-61.66789000000000,0.00000000000000),App.Vector(0.00000000000000,-61.66789000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-61.66789000000000,0.00000000000000),App.Vector(0.00000000000000,34.94061000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-77.17443000000000,34.94061000000000,0.00000000000000),App.Vector(0.00000000000000,34.94061000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-77.17443000000000,-61.66789000000000,0.00000000000000),App.Vector(-77.17443000000000,34.94061000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Pad","Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC")
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC")
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").Length = 5.588
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FphDYkms1USRifU_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FphDYkms1USRifU_0_FlalIqnMN8SEvc9_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Plane", "plane_Sketch_FhFc91sMHMmYGAO_1_JJC")
origin = App.Vector(-38.58721999999999,-13.36364000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhFc91sMHMmYGAO_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("Sketcher::SketchObject","Sketch_FhFc91sMHMmYGAO_1_JJC")
App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhFc91sMHMmYGAO_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC").addGeometry(Part.LineSegment(App.Vector(33.78317999999999,-43.54378000000001,0.00000000000000),App.Vector(-34.51801000000000,-43.54378000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC").addGeometry(Part.LineSegment(App.Vector(-34.51801000000000,-43.54378000000001,0.00000000000000),App.Vector(-34.51801000000000,-36.00417000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC").addGeometry(Part.LineSegment(App.Vector(33.78317999999999,-36.00417000000000,0.00000000000000),App.Vector(-34.51801000000000,-36.00417000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC").addGeometry(Part.LineSegment(App.Vector(33.78317999999999,-43.54378000000001,0.00000000000000),App.Vector(33.78317999999999,-36.00417000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Pad","Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC")
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC")
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").Length = 8.89
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhFc91sMHMmYGAO_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhFc91sMHMmYGAO_1_Ff6nzJ8PCZKboGo_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Plane", "plane_Sketch_F3jzVJqhPgdRCxo_1_JPC")
origin = App.Vector(-38.58721999999999,-13.36364000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3jzVJqhPgdRCxo_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("Sketcher::SketchObject","Sketch_F3jzVJqhPgdRCxo_1_JPC")
App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3jzVJqhPgdRCxo_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").addGeometry(Part.LineSegment(App.Vector(-38.89083000000001,-40.26010000000000,0.00000000000000),App.Vector(-38.58721000000001,-40.26010000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").addGeometry(Part.LineSegment(App.Vector(-38.58721000000001,48.30425000000001,0.00000000000000),App.Vector(-38.58721000000001,-40.26010000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").addGeometry(Part.LineSegment(App.Vector(-38.58721000000001,48.30425000000001,0.00000000000000),App.Vector(-29.93929000000000,48.30425000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").addGeometry(Part.LineSegment(App.Vector(-29.93929000000000,48.84943999999999,0.00000000000000),App.Vector(-29.93929000000000,48.30425000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").addGeometry(Part.LineSegment(App.Vector(-29.93929000000000,48.84943999999999,0.00000000000000),App.Vector(-38.89083000000001,48.84943999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").addGeometry(Part.LineSegment(App.Vector(-38.89083000000001,-40.26010000000000,0.00000000000000),App.Vector(-38.89083000000001,48.84943999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Pad","Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC")
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC")
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").Length = 9.652000000000001
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Plane", "plane_Sketch_F3jzVJqhPgdRCxo_1_JPG")
origin = App.Vector(-38.58721999999999,-13.36364000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3jzVJqhPgdRCxo_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("Sketcher::SketchObject","Sketch_F3jzVJqhPgdRCxo_1_JPG")
App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3jzVJqhPgdRCxo_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG").addGeometry(Part.LineSegment(App.Vector(-29.93929000000000,-40.26010000000000,0.00000000000000),App.Vector(-34.51801000000000,-40.26010000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG").addGeometry(Part.LineSegment(App.Vector(-34.51801000000000,-36.00417000000000,0.00000000000000),App.Vector(-34.51801000000000,-40.26010000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG").addGeometry(Part.LineSegment(App.Vector(-34.51801000000000,-36.00417000000000,0.00000000000000),App.Vector(-29.93929000000000,-36.00417000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG").addGeometry(Part.LineSegment(App.Vector(-29.93929000000000,-40.26010000000000,0.00000000000000),App.Vector(-29.93929000000000,-36.00417000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Pad","Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG")
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG")
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").Length = 9.652000000000001
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Plane", "plane_Sketch_F3jzVJqhPgdRCxo_1_JPS")
origin = App.Vector(-38.58721999999999,-13.36364000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3jzVJqhPgdRCxo_1_JPS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("Sketcher::SketchObject","Sketch_F3jzVJqhPgdRCxo_1_JPS")
App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3jzVJqhPgdRCxo_1_JPS"), [""])
App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").addGeometry(Part.LineSegment(App.Vector(-38.58721000000001,-40.26010000000000,0.00000000000000),App.Vector(-34.51801000000000,-40.26010000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").addGeometry(Part.LineSegment(App.Vector(-34.51801000000000,-36.00417000000000,0.00000000000000),App.Vector(-34.51801000000000,-40.26010000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").addGeometry(Part.LineSegment(App.Vector(-34.51801000000000,-36.00417000000000,0.00000000000000),App.Vector(-29.93929000000000,-36.00417000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").addGeometry(Part.LineSegment(App.Vector(-29.93929000000000,48.30425000000001,0.00000000000000),App.Vector(-29.93929000000000,-36.00417000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").addGeometry(Part.LineSegment(App.Vector(-38.58721000000001,48.30425000000001,0.00000000000000),App.Vector(-29.93929000000000,48.30425000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").addGeometry(Part.LineSegment(App.Vector(-38.58721000000001,48.30425000000001,0.00000000000000),App.Vector(-38.58721000000001,-40.26010000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Pad","Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS")
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").Profile = App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS")
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").Length = 9.652000000000001
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3jzVJqhPgdRCxo_1_JPS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").Type = 4
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3jzVJqhPgdRCxo_1_FmAJmPT1tvemkY8_1_JPS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Plane", "plane_Sketch_FqYa8XCzDhcr71G_1_JVC")
origin = App.Vector(-38.58721999999999,-13.36364000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqYa8XCzDhcr71G_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("Sketcher::SketchObject","Sketch_FqYa8XCzDhcr71G_1_JVC")
App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqYa8XCzDhcr71G_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC").addGeometry(Part.LineSegment(App.Vector(-27.44994000000000,37.78127000000001,0.00000000000000),App.Vector(34.92133000000000,37.78127000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC").addGeometry(Part.LineSegment(App.Vector(34.92133000000000,37.78127000000001,0.00000000000000),App.Vector(34.92133000000000,46.49262000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC").addGeometry(Part.LineSegment(App.Vector(-27.44994000000000,46.49262000000000,0.00000000000000),App.Vector(34.92133000000000,46.49262000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC").addGeometry(Part.LineSegment(App.Vector(-27.44994000000000,37.78127000000001,0.00000000000000),App.Vector(-27.44994000000000,46.49262000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Pad","Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC")
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC")
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").Length = 10.921999999999999
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqYa8XCzDhcr71G_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqYa8XCzDhcr71G_1_F7vGv9lHmfw2xf7_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Plane", "plane_Sketch_FinOTCcMw5A0hH6_1_JZC")
origin = App.Vector(-38.58721999999999,-13.36364000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FinOTCcMw5A0hH6_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("Sketcher::SketchObject","Sketch_FinOTCcMw5A0hH6_1_JZC")
App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FinOTCcMw5A0hH6_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC").addGeometry(Part.LineSegment(App.Vector(20.87892000000000,-32.56607000000000,0.00000000000000),App.Vector(31.48193000000000,-32.56607000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC").addGeometry(Part.LineSegment(App.Vector(31.48193000000000,-32.56607000000000,0.00000000000000),App.Vector(31.48193000000000,39.06709000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC").addGeometry(Part.LineSegment(App.Vector(20.87892000000000,39.06709000000000,0.00000000000000),App.Vector(31.48193000000000,39.06709000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC").addGeometry(Part.LineSegment(App.Vector(20.87892000000000,-32.56607000000000,0.00000000000000),App.Vector(20.87892000000000,39.06709000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Pad","Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC")
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC")
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").Length = 12.446
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FinOTCcMw5A0hH6_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FinOTCcMw5A0hH6_1_FZ4tcN0g6vZgCeS_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Plane", "plane_Sketch_FDrAhIpo3UJsl1N_1_JdC")
origin = App.Vector(-73.00228000000000,-18.24984000000000,-9.65200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDrAhIpo3UJsl1N_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("Sketcher::SketchObject","Sketch_FDrAhIpo3UJsl1N_1_JdC")
App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDrAhIpo3UJsl1N_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC").addGeometry(Part.LineSegment(App.Vector(-4.47577000000000,36.00325000000000,0.00000000000000),App.Vector(4.47577000000000,36.00325000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC").addGeometry(Part.LineSegment(App.Vector(4.47577000000000,43.96324000000000,0.00000000000000),App.Vector(4.47577000000000,36.00325000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC").addGeometry(Part.LineSegment(App.Vector(4.47577000000000,43.96324000000000,0.00000000000000),App.Vector(-4.47577000000000,43.96324000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC").addGeometry(Part.LineSegment(App.Vector(-4.47577000000000,43.96324000000000,0.00000000000000),App.Vector(-4.47577000000000,36.00325000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FphDYkms1USRifU_0").newObject("PartDesign::Pad","Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC")
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC")
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").Length = 65.278
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDrAhIpo3UJsl1N_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDrAhIpo3UJsl1N_1_FTPjY9V7biIkve2_1_JdC").Offset = 0
App.ActiveDocument.recompute()

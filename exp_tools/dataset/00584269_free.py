import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00584269")
App.ActiveDocument.addObject("PartDesign::Body","Body_FsdXNH7v5B7X45W_0")
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").Label = "Body_FsdXNH7v5B7X45W_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Plane", "plane_Sketch_FsdXNH7v5B7X45W_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsdXNH7v5B7X45W_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("Sketcher::SketchObject","Sketch_FsdXNH7v5B7X45W_0_JGC")
App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsdXNH7v5B7X45W_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(60.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,0.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").addGeometry(Part.LineSegment(App.Vector(3.00000000000000,-3.00000000000000,0.00000000000000),App.Vector(57.00000000000000,-3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").addGeometry(Part.LineSegment(App.Vector(57.00000000000000,-3.00000000000000,0.00000000000000),App.Vector(57.00000000000000,-57.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").addGeometry(Part.LineSegment(App.Vector(3.00000000000000,-57.00000000000000,0.00000000000000),App.Vector(57.00000000000000,-57.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").addGeometry(Part.LineSegment(App.Vector(3.00000000000000,-3.00000000000000,0.00000000000000),App.Vector(3.00000000000000,-57.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Pad","Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC")
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC")
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").Length = 2300.0000000000005
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsdXNH7v5B7X45W_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsdXNH7v5B7X45W_0_FxqxJE2BxbDdm9r_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Plane", "plane_Sketch_FVM17cfIL81Cm2G_1_JLW")
origin = App.Vector(30.00000000000000,-250.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("Sketcher::SketchObject","Sketch_FVM17cfIL81Cm2G_1_JLW")
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLW"), [""])
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLW").addGeometry(Part.Circle(App.Vector(0.00000000000000,360.00151999999997,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Pocket","Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").Profile = App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLW")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").Length = 100.0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").Type = 4
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Plane", "plane_Sketch_FVM17cfIL81Cm2G_1_JLS")
origin = App.Vector(30.00000000000000,-250.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("Sketcher::SketchObject","Sketch_FVM17cfIL81Cm2G_1_JLS")
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLS"), [""])
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLS").addGeometry(Part.Circle(App.Vector(0.00000000000000,420.00152000000003,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Pocket","Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").Profile = App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLS")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").Length = 100.0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").Type = 4
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Plane", "plane_Sketch_FVM17cfIL81Cm2G_1_JLK")
origin = App.Vector(30.00000000000000,-250.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("Sketcher::SketchObject","Sketch_FVM17cfIL81Cm2G_1_JLK")
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLK").addGeometry(Part.Circle(App.Vector(0.00000000000000,1180.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Pocket","Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLK")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").Length = 100.0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Plane", "plane_Sketch_FVM17cfIL81Cm2G_1_JLO")
origin = App.Vector(30.00000000000000,-250.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("Sketcher::SketchObject","Sketch_FVM17cfIL81Cm2G_1_JLO")
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLO").addGeometry(Part.Circle(App.Vector(0.42690000000000,1120.00152000000003,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Pocket","Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLO")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").Length = 100.0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Plane", "plane_Sketch_FVM17cfIL81Cm2G_1_JLC")
origin = App.Vector(30.00000000000000,-250.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("Sketcher::SketchObject","Sketch_FVM17cfIL81Cm2G_1_JLC")
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLC").addGeometry(Part.Circle(App.Vector(0.00000000000000,1970.00000000000023,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Pocket","Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLC")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Plane", "plane_Sketch_FVM17cfIL81Cm2G_1_JLG")
origin = App.Vector(30.00000000000000,-250.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("Sketcher::SketchObject","Sketch_FVM17cfIL81Cm2G_1_JLG")
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVM17cfIL81Cm2G_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLG").addGeometry(Part.Circle(App.Vector(0.00000000000000,1910.00000000000023,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Pocket","Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLG")
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").Length = 100.0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVM17cfIL81Cm2G_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVM17cfIL81Cm2G_1_FTnirqd26djSqyn_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Plane", "plane_Sketch_F4ZV8UVyWHggrrG_1_JPa")
origin = App.Vector(30.00000000000000,-250.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ZV8UVyWHggrrG_1_JPa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("Sketcher::SketchObject","Sketch_F4ZV8UVyWHggrrG_1_JPa")
App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ZV8UVyWHggrrG_1_JPa"), [""])
App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa").addGeometry(Part.LineSegment(App.Vector(288.08219000000003,290.00000000000006,0.00000000000000),App.Vector(30.00000000000000,290.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,290.00000000000006,0.00000000000000),App.Vector(30.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa").addGeometry(Part.LineSegment(App.Vector(288.08219000000003,250.00000000000000,0.00000000000000),App.Vector(30.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa").addGeometry(Part.LineSegment(App.Vector(288.08219000000003,290.00000000000006,0.00000000000000),App.Vector(288.08219000000003,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Pad","Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa")
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").Profile = App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa")
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").Length = 20.0
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").Type = 4
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Plane", "plane_Sketch_F4ZV8UVyWHggrrG_1_JPe")
origin = App.Vector(30.00000000000000,-250.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ZV8UVyWHggrrG_1_JPe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("Sketcher::SketchObject","Sketch_F4ZV8UVyWHggrrG_1_JPe")
App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ZV8UVyWHggrrG_1_JPe"), [""])
App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,290.00000000000006,0.00000000000000),App.Vector(30.00000000000000,290.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,290.00000000000006,0.00000000000000),App.Vector(30.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,250.00000000000000,0.00000000000000),App.Vector(30.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,290.00000000000006,0.00000000000000),App.Vector(-30.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FsdXNH7v5B7X45W_0").newObject("PartDesign::Pad","Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe")
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").Profile = App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe")
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").Length = 20.0
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ZV8UVyWHggrrG_1_JPe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").Type = 4
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ZV8UVyWHggrrG_1_FiBMhLnnB7vYEZc_1_JPe").Offset = 0
App.ActiveDocument.recompute()

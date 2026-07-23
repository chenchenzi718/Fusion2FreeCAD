import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00314343")
App.ActiveDocument.addObject("PartDesign::Body","Body_FQcus0ttLpvNsKp_0")
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").Label = "Body_FQcus0ttLpvNsKp_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Plane", "plane_Sketch_FQcus0ttLpvNsKp_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQcus0ttLpvNsKp_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("Sketcher::SketchObject","Sketch_FQcus0ttLpvNsKp_0_JGC")
App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQcus0ttLpvNsKp_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC").addGeometry(Part.LineSegment(App.Vector(-149.74914000000001,153.03170999999998,0.00000000000000),App.Vector(150.25086000000002,153.03170999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC").addGeometry(Part.LineSegment(App.Vector(150.25086000000002,153.03170999999998,0.00000000000000),App.Vector(150.25086000000002,-146.96829000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC").addGeometry(Part.LineSegment(App.Vector(-149.74914000000001,-146.96829000000000,0.00000000000000),App.Vector(150.25086000000002,-146.96829000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC").addGeometry(Part.LineSegment(App.Vector(-149.74914000000001,153.03170999999998,0.00000000000000),App.Vector(-149.74914000000001,-146.96829000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Pad","Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC")
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC")
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQcus0ttLpvNsKp_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQcus0ttLpvNsKp_0_FhOt9hPo6TUmdeo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Plane", "plane_Sketch_Fk0vrT5bj0RtFmk_1_JLC")
origin = App.Vector(0.25086000000000,3.03171000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk0vrT5bj0RtFmk_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("Sketcher::SketchObject","Sketch_Fk0vrT5bj0RtFmk_1_JLC")
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk0vrT5bj0RtFmk_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC").addGeometry(Part.LineSegment(App.Vector(-148.72837999999999,-149.66077999999999,0.00000000000000),App.Vector(-128.72838000000002,-149.66077999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC").addGeometry(Part.LineSegment(App.Vector(-128.72838000000002,-149.66077999999999,0.00000000000000),App.Vector(-128.72838000000002,-129.66078000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC").addGeometry(Part.LineSegment(App.Vector(-148.72837999999999,-129.66078000000002,0.00000000000000),App.Vector(-128.72838000000002,-129.66078000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC").addGeometry(Part.LineSegment(App.Vector(-148.72837999999999,-149.66077999999999,0.00000000000000),App.Vector(-148.72837999999999,-129.66078000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Pad","Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC")
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC")
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").Length = 350.00000000000006
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Plane", "plane_Sketch_Fk0vrT5bj0RtFmk_1_JLG")
origin = App.Vector(0.25086000000000,3.03171000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk0vrT5bj0RtFmk_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("Sketcher::SketchObject","Sketch_Fk0vrT5bj0RtFmk_1_JLG")
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk0vrT5bj0RtFmk_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG").addGeometry(Part.LineSegment(App.Vector(-150.00000000000000,130.00000000000000,0.00000000000000),App.Vector(-130.00000000000000,130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG").addGeometry(Part.LineSegment(App.Vector(-130.00000000000000,130.00000000000000,0.00000000000000),App.Vector(-130.00000000000000,150.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG").addGeometry(Part.LineSegment(App.Vector(-150.00000000000000,150.00000000000000,0.00000000000000),App.Vector(-130.00000000000000,150.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG").addGeometry(Part.LineSegment(App.Vector(-150.00000000000000,150.00000000000000,0.00000000000000),App.Vector(-150.00000000000000,130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Pad","Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG")
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG")
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").Length = 350.00000000000006
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Plane", "plane_Sketch_Fk0vrT5bj0RtFmk_1_JLK")
origin = App.Vector(0.25086000000000,3.03171000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk0vrT5bj0RtFmk_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("Sketcher::SketchObject","Sketch_Fk0vrT5bj0RtFmk_1_JLK")
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk0vrT5bj0RtFmk_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK").addGeometry(Part.LineSegment(App.Vector(150.00000000000003,-150.00000000000000,0.00000000000000),App.Vector(130.00000000000000,-150.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK").addGeometry(Part.LineSegment(App.Vector(130.00000000000000,-150.00000000000000,0.00000000000000),App.Vector(130.00000000000000,-130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK").addGeometry(Part.LineSegment(App.Vector(130.00000000000000,-130.00000000000000,0.00000000000000),App.Vector(150.00000000000003,-130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK").addGeometry(Part.LineSegment(App.Vector(150.00000000000003,-150.00000000000000,0.00000000000000),App.Vector(150.00000000000003,-130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Pad","Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK")
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK")
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").Length = 350.00000000000006
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Plane", "plane_Sketch_Fk0vrT5bj0RtFmk_1_JLO")
origin = App.Vector(0.25086000000000,3.03171000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk0vrT5bj0RtFmk_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("Sketcher::SketchObject","Sketch_Fk0vrT5bj0RtFmk_1_JLO")
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk0vrT5bj0RtFmk_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO").addGeometry(Part.LineSegment(App.Vector(130.00000000000000,130.00000000000000,0.00000000000000),App.Vector(150.00000000000003,130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO").addGeometry(Part.LineSegment(App.Vector(150.00000000000003,150.00000000000000,0.00000000000000),App.Vector(150.00000000000003,130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO").addGeometry(Part.LineSegment(App.Vector(150.00000000000003,150.00000000000000,0.00000000000000),App.Vector(130.00000000000000,150.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO").addGeometry(Part.LineSegment(App.Vector(130.00000000000000,130.00000000000000,0.00000000000000),App.Vector(130.00000000000000,150.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Pad","Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO")
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO")
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").Length = 350.00000000000006
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk0vrT5bj0RtFmk_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk0vrT5bj0RtFmk_1_FBD69Ia98MjXee6_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Plane", "plane_Sketch_FJgRazIibv5cd5Y_1_JPC")
origin = App.Vector(0.25086000000000,3.03171000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJgRazIibv5cd5Y_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("Sketcher::SketchObject","Sketch_FJgRazIibv5cd5Y_1_JPC")
App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJgRazIibv5cd5Y_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC").addGeometry(Part.LineSegment(App.Vector(150.00000000000003,-150.00000000000000,0.00000000000000),App.Vector(130.00000000000000,-150.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC").addGeometry(Part.LineSegment(App.Vector(130.00000000000000,-150.00000000000000,0.00000000000000),App.Vector(130.00000000000000,-130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC").addGeometry(Part.LineSegment(App.Vector(150.00000000000003,-130.00000000000000,0.00000000000000),App.Vector(130.00000000000000,-130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC").addGeometry(Part.LineSegment(App.Vector(150.00000000000003,-150.00000000000000,0.00000000000000),App.Vector(150.00000000000003,-130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Pad","Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC")
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC")
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").Length = 250.0
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Plane", "plane_Sketch_FJgRazIibv5cd5Y_1_JPG")
origin = App.Vector(0.25086000000000,3.03171000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJgRazIibv5cd5Y_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("Sketcher::SketchObject","Sketch_FJgRazIibv5cd5Y_1_JPG")
App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJgRazIibv5cd5Y_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG").addGeometry(Part.LineSegment(App.Vector(-150.00000000000000,-150.00000000000000,0.00000000000000),App.Vector(-130.00000000000000,-150.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG").addGeometry(Part.LineSegment(App.Vector(-130.00000000000000,-150.00000000000000,0.00000000000000),App.Vector(-130.00000000000000,-130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG").addGeometry(Part.LineSegment(App.Vector(-130.00000000000000,-130.00000000000000,0.00000000000000),App.Vector(-150.00000000000000,-130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG").addGeometry(Part.LineSegment(App.Vector(-150.00000000000000,-150.00000000000000,0.00000000000000),App.Vector(-150.00000000000000,-130.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Pad","Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG")
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG")
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").Length = 250.0
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJgRazIibv5cd5Y_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJgRazIibv5cd5Y_1_FHGlUQ3eqXiRYh2_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Plane", "plane_Sketch_F7Am5MxmXkN3nho_1_JTC")
origin = App.Vector(130.25085999999999,-136.96829000000000,150.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7Am5MxmXkN3nho_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("Sketcher::SketchObject","Sketch_F7Am5MxmXkN3nho_1_JTC")
App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7Am5MxmXkN3nho_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC").addGeometry(Part.LineSegment(App.Vector(10.00000000000001,130.00000000000003,0.00000000000000),App.Vector(-9.99999999999998,130.00000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC").addGeometry(Part.LineSegment(App.Vector(-9.99999999999998,130.00000000000003,0.00000000000000),App.Vector(-9.99999999999998,120.00000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC").addGeometry(Part.LineSegment(App.Vector(-9.99999999999998,120.00000000000003,0.00000000000000),App.Vector(10.00000000000001,120.00000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC").addGeometry(Part.LineSegment(App.Vector(10.00000000000001,130.00000000000003,0.00000000000000),App.Vector(10.00000000000001,120.00000000000003,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQcus0ttLpvNsKp_0").newObject("PartDesign::Pad","Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC")
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC")
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").Length = 260.0
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7Am5MxmXkN3nho_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7Am5MxmXkN3nho_1_F2uBUWsd7kJxlyr_1_JTC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00410883")
App.ActiveDocument.addObject("PartDesign::Body","Body_Frv9xE36Hocqnpk_0")
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").Label = "Body_Frv9xE36Hocqnpk_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_Frv9xE36Hocqnpk_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Frv9xE36Hocqnpk_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_Frv9xE36Hocqnpk_0_JGC")
App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Frv9xE36Hocqnpk_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1970.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC").addGeometry(Part.LineSegment(App.Vector(1970.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1970.00000000000000,1560.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,1560.00000000000000,0.00000000000000),App.Vector(1970.00000000000000,1560.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1560.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pad","Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC")
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC")
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").Length = 50.0
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Frv9xE36Hocqnpk_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Frv9xE36Hocqnpk_0_F7LXdwBwf2OX1HB_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_Fh2YYnsi8u2c8uK_1_JLC")
origin = App.Vector(1970.00000000000000,155.00000000000000,25.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh2YYnsi8u2c8uK_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_Fh2YYnsi8u2c8uK_1_JLC")
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh2YYnsi8u2c8uK_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC").addGeometry(Part.LineSegment(App.Vector(155.00000000000000,75.00000000000001,0.00000000000000),App.Vector(215.00000000000000,75.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC").addGeometry(Part.LineSegment(App.Vector(215.00000000000000,75.00000000000001,0.00000000000000),App.Vector(215.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC").addGeometry(Part.LineSegment(App.Vector(155.00000000000000,25.00000000000000,0.00000000000000),App.Vector(215.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC").addGeometry(Part.LineSegment(App.Vector(155.00000000000000,75.00000000000001,0.00000000000000),App.Vector(155.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pad","Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC")
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC")
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_Fh2YYnsi8u2c8uK_1_JLG")
origin = App.Vector(1970.00000000000000,155.00000000000000,25.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh2YYnsi8u2c8uK_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_Fh2YYnsi8u2c8uK_1_JLG")
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh2YYnsi8u2c8uK_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG").addGeometry(Part.LineSegment(App.Vector(1035.00000000000000,75.00000000000001,0.00000000000000),App.Vector(1095.00000000000000,75.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG").addGeometry(Part.LineSegment(App.Vector(1095.00000000000000,75.00000000000001,0.00000000000000),App.Vector(1095.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG").addGeometry(Part.LineSegment(App.Vector(1035.00000000000000,25.00000000000000,0.00000000000000),App.Vector(1095.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG").addGeometry(Part.LineSegment(App.Vector(1035.00000000000000,75.00000000000001,0.00000000000000),App.Vector(1035.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pad","Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG")
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG")
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_Fh2YYnsi8u2c8uK_1_JLK")
origin = App.Vector(1970.00000000000000,155.00000000000000,25.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh2YYnsi8u2c8uK_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_Fh2YYnsi8u2c8uK_1_JLK")
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh2YYnsi8u2c8uK_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK").addGeometry(Part.LineSegment(App.Vector(155.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(215.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK").addGeometry(Part.LineSegment(App.Vector(215.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(215.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK").addGeometry(Part.LineSegment(App.Vector(155.00000000000000,25.00000000000000,0.00000000000000),App.Vector(215.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK").addGeometry(Part.LineSegment(App.Vector(155.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(155.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pad","Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK")
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK")
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_Fh2YYnsi8u2c8uK_1_JLO")
origin = App.Vector(1970.00000000000000,155.00000000000000,25.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh2YYnsi8u2c8uK_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_Fh2YYnsi8u2c8uK_1_JLO")
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh2YYnsi8u2c8uK_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO").addGeometry(Part.LineSegment(App.Vector(1035.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(1095.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO").addGeometry(Part.LineSegment(App.Vector(1095.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(1095.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO").addGeometry(Part.LineSegment(App.Vector(1035.00000000000000,25.00000000000000,0.00000000000000),App.Vector(1095.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO").addGeometry(Part.LineSegment(App.Vector(1035.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(1035.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pad","Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO")
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO")
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh2YYnsi8u2c8uK_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh2YYnsi8u2c8uK_1_FxjVSvpUYVtR9D9_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_FZt8ABDoJHx8Fd5_1_JPC")
origin = App.Vector(985.00000000000000,780.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZt8ABDoJHx8Fd5_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_FZt8ABDoJHx8Fd5_1_JPC")
App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZt8ABDoJHx8Fd5_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC").addGeometry(Part.LineSegment(App.Vector(-965.00000000000000,760.00000000000000,0.00000000000000),App.Vector(965.00000000000000,760.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC").addGeometry(Part.LineSegment(App.Vector(965.00000000000000,760.00000000000000,0.00000000000000),App.Vector(965.00000000000000,-760.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC").addGeometry(Part.LineSegment(App.Vector(-965.00000000000000,-760.00000000000000,0.00000000000000),App.Vector(965.00000000000000,-760.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC").addGeometry(Part.LineSegment(App.Vector(-965.00000000000000,760.00000000000000,0.00000000000000),App.Vector(-965.00000000000000,-760.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pocket","Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC")
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC")
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZt8ABDoJHx8Fd5_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZt8ABDoJHx8Fd5_1_FwNmhn2gAxsMqoa_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_FrAvjyPQX67KTRP_1_JTC")
origin = App.Vector(985.00000000000000,1560.00000000000000,25.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrAvjyPQX67KTRP_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_FrAvjyPQX67KTRP_1_JTC")
App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrAvjyPQX67KTRP_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTC").addGeometry(Part.Circle(App.Vector(-805.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pocket","Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC")
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTC")
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_FrAvjyPQX67KTRP_1_JTG")
origin = App.Vector(985.00000000000000,1560.00000000000000,25.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrAvjyPQX67KTRP_1_JTG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_FrAvjyPQX67KTRP_1_JTG")
App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrAvjyPQX67KTRP_1_JTG"), [""])
App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTG").addGeometry(Part.Circle(App.Vector(-684.99999999999989,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pocket","Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG")
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").Profile = App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTG")
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").Length = 20.0
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrAvjyPQX67KTRP_1_JTG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").Type = 4
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrAvjyPQX67KTRP_1_FKgNgSW9X2bXs3K_1_JTG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_FTMtAc5j6Dkv3cj_1_JYC")
origin = App.Vector(985.00000000000000,0.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTMtAc5j6Dkv3cj_1_JYC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_FTMtAc5j6Dkv3cj_1_JYC")
App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTMtAc5j6Dkv3cj_1_JYC"), [""])
App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYC").addGeometry(Part.Circle(App.Vector(684.99999999999989,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pocket","Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC")
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").Profile = App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYC")
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").Type = 4
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Plane", "plane_Sketch_FTMtAc5j6Dkv3cj_1_JYG")
origin = App.Vector(985.00000000000000,0.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTMtAc5j6Dkv3cj_1_JYG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("Sketcher::SketchObject","Sketch_FTMtAc5j6Dkv3cj_1_JYG")
App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTMtAc5j6Dkv3cj_1_JYG"), [""])
App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYG").addGeometry(Part.Circle(App.Vector(805.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Frv9xE36Hocqnpk_0").newObject("PartDesign::Pocket","Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG")
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").Profile = App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYG")
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").Length = 20.0
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTMtAc5j6Dkv3cj_1_JYG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").Type = 4
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTMtAc5j6Dkv3cj_1_FbX96nwvzKOVZcE_1_JYG").Offset = 0
App.ActiveDocument.recompute()

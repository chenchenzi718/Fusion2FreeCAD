import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00242801")
App.ActiveDocument.addObject("PartDesign::Body","Body_FSZjF9qoGW7p5W1_0")
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").Label = "Body_FSZjF9qoGW7p5W1_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Plane", "plane_Sketch_FSZjF9qoGW7p5W1_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSZjF9qoGW7p5W1_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("Sketcher::SketchObject","Sketch_FSZjF9qoGW7p5W1_0_JGC")
App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSZjF9qoGW7p5W1_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-76.13670999999999,0.00000000000000),App.Vector(127.00000000000000,-76.13670999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").addGeometry(Part.LineSegment(App.Vector(127.00000000000000,-76.13670999999999,0.00000000000000),App.Vector(127.00000000000000,-25.33671000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").addGeometry(Part.LineSegment(App.Vector(85.72499999999999,-25.33671000000000,0.00000000000000),App.Vector(127.00000000000000,-25.33671000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").addGeometry(Part.LineSegment(App.Vector(85.72499999999999,25.46329000000000,0.00000000000000),App.Vector(85.72499999999999,-25.33671000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").addGeometry(Part.LineSegment(App.Vector(127.00000000000000,25.46329000000000,0.00000000000000),App.Vector(85.72499999999999,25.46329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").addGeometry(Part.LineSegment(App.Vector(127.00000000000000,76.26329000000000,0.00000000000000),App.Vector(127.00000000000000,25.46329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,76.26329000000000,0.00000000000000),App.Vector(127.00000000000000,76.26329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-76.13670999999999,0.00000000000000),App.Vector(0.00000000000000,76.26329000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Pad","Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC")
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC")
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").Length = 31.75
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Plane", "plane_Sketch_FSZjF9qoGW7p5W1_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSZjF9qoGW7p5W1_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("Sketcher::SketchObject","Sketch_FSZjF9qoGW7p5W1_0_JGG")
App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSZjF9qoGW7p5W1_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-76.13670999999999,0.00000000000000),App.Vector(-127.00000000000000,-76.13670999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").addGeometry(Part.LineSegment(App.Vector(-127.00000000000000,-76.13670999999999,0.00000000000000),App.Vector(-127.00000000000000,-25.33671000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").addGeometry(Part.LineSegment(App.Vector(-127.00000000000000,-25.33671000000000,0.00000000000000),App.Vector(-85.72499999999999,-25.33671000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").addGeometry(Part.LineSegment(App.Vector(-85.72499999999999,-25.33671000000000,0.00000000000000),App.Vector(-85.72499999999999,25.46329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").addGeometry(Part.LineSegment(App.Vector(-85.72499999999999,25.46329000000000,0.00000000000000),App.Vector(-127.00000000000000,25.46329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").addGeometry(Part.LineSegment(App.Vector(-127.00000000000000,25.46329000000000,0.00000000000000),App.Vector(-127.00000000000000,76.26329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").addGeometry(Part.LineSegment(App.Vector(-127.00000000000000,76.26329000000000,0.00000000000000),App.Vector(0.00000000000000,76.26329000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-76.13670999999999,0.00000000000000),App.Vector(0.00000000000000,76.26329000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Pad","Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG")
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG")
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").Length = 31.75
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSZjF9qoGW7p5W1_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSZjF9qoGW7p5W1_0_FKhfhIbjz6fUdqR_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Plane", "plane_Sketch_FcTBnQ5QZjfDIyv_1_JJa")
origin = App.Vector(98.42500000000000,0.06329000000000,31.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("Sketcher::SketchObject","Sketch_FcTBnQ5QZjfDIyv_1_JJa")
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,76.20000000000000,0.00000000000000),App.Vector(-60.32500000000000,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,76.20000000000000,0.00000000000000),App.Vector(-60.32500000000000,44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,44.45000000000000,0.00000000000000),App.Vector(-60.32500000000000,44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,76.20000000000000,0.00000000000000),App.Vector(-28.57500000000000,44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Pad","Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").Length = 60.325
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FRlaQbP9amY9708_1_JJa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Plane", "plane_Sketch_FcTBnQ5QZjfDIyv_1_JJW")
origin = App.Vector(98.42500000000000,0.06329000000000,31.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("Sketcher::SketchObject","Sketch_FcTBnQ5QZjfDIyv_1_JJW")
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,-76.19999999999999,0.00000000000000),App.Vector(-60.32500000000000,-76.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,-76.19999999999999,0.00000000000000),App.Vector(-60.32500000000000,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,-44.45000000000000,0.00000000000000),App.Vector(-28.57500000000000,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,-76.19999999999999,0.00000000000000),App.Vector(-28.57500000000000,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Pad","Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").Length = 60.325
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FtjBDvs31TGv3Yw_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Plane", "plane_Sketch_FcTBnQ5QZjfDIyv_1_JJK")
origin = App.Vector(98.42500000000000,0.06329000000000,31.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("Sketcher::SketchObject","Sketch_FcTBnQ5QZjfDIyv_1_JJK")
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,-76.19999999999999,0.00000000000000),App.Vector(-136.52500000000001,-76.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK").addGeometry(Part.LineSegment(App.Vector(-136.52500000000001,-76.19999999999999,0.00000000000000),App.Vector(-136.52500000000001,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,-44.45000000000000,0.00000000000000),App.Vector(-136.52500000000001,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,-76.19999999999999,0.00000000000000),App.Vector(-168.27500000000001,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Pad","Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").Length = 60.325
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_F10xAa47cYSrDol_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Plane", "plane_Sketch_FcTBnQ5QZjfDIyv_1_JJO")
origin = App.Vector(98.42500000000000,0.06329000000000,31.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("Sketcher::SketchObject","Sketch_FcTBnQ5QZjfDIyv_1_JJO")
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,76.20000000000000,0.00000000000000),App.Vector(-136.52500000000001,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO").addGeometry(Part.LineSegment(App.Vector(-136.52500000000001,76.20000000000000,0.00000000000000),App.Vector(-136.52500000000001,44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,44.45000000000000,0.00000000000000),App.Vector(-136.52500000000001,44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,76.20000000000000,0.00000000000000),App.Vector(-168.27500000000001,44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Pad","Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").Length = 60.325
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FcllRj49EW46sNk_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Plane", "plane_Sketch_FcTBnQ5QZjfDIyv_1_JJi")
origin = App.Vector(98.42500000000000,0.06329000000000,31.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("Sketcher::SketchObject","Sketch_FcTBnQ5QZjfDIyv_1_JJi")
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJi"), [""])
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,44.45000000000000,0.00000000000000),App.Vector(-28.57500000000000,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,-44.45000000000000,0.00000000000000),App.Vector(-28.57500000000000,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,-44.45000000000000,0.00000000000000),App.Vector(-60.32500000000000,44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,44.45000000000000,0.00000000000000),App.Vector(-60.32500000000000,44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Pad","Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").Profile = App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").Length = 44.45
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").Type = 4
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_FwLzRWsJfibQX4B_1_JJi").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Plane", "plane_Sketch_FcTBnQ5QZjfDIyv_1_JJe")
origin = App.Vector(98.42500000000000,0.06329000000000,31.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("Sketcher::SketchObject","Sketch_FcTBnQ5QZjfDIyv_1_JJe")
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcTBnQ5QZjfDIyv_1_JJe"), [""])
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,44.45000000000000,0.00000000000000),App.Vector(-168.27500000000001,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,-44.45000000000000,0.00000000000000),App.Vector(-136.52500000000001,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe").addGeometry(Part.LineSegment(App.Vector(-136.52500000000001,44.45000000000000,0.00000000000000),App.Vector(-136.52500000000001,-44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,44.45000000000000,0.00000000000000),App.Vector(-136.52500000000001,44.45000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZjF9qoGW7p5W1_0").newObject("PartDesign::Pad","Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").Profile = App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe")
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").Length = 44.45
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcTBnQ5QZjfDIyv_1_JJe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").Type = 4
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcTBnQ5QZjfDIyv_1_Fjhs5ub2Grharsr_1_JJe").Offset = 0
App.ActiveDocument.recompute()

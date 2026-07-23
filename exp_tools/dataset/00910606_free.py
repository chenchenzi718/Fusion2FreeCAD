import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00910606")
App.ActiveDocument.addObject("PartDesign::Body","Body_FJ17AxElGgz9dRH_0")
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").Label = "Body_FJ17AxElGgz9dRH_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Plane", "plane_Sketch_FJ17AxElGgz9dRH_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ17AxElGgz9dRH_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("Sketcher::SketchObject","Sketch_FJ17AxElGgz9dRH_0_JGC")
App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ17AxElGgz9dRH_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-9000.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC").addGeometry(Part.LineSegment(App.Vector(-9000.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-9000.00000000000000,17000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,17000.00000000000000,0.00000000000000),App.Vector(-9000.00000000000000,17000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,17000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Pad","Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC")
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC")
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ17AxElGgz9dRH_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ17AxElGgz9dRH_0_Fqxn1cyqHSg4J35_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Plane", "plane_Sketch_Ff6ta67jsVSbPU8_1_KJuB")
origin = App.Vector(-4500.00000000000000,375.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJuB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("Sketcher::SketchObject","Sketch_Ff6ta67jsVSbPU8_1_KJuB")
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJuB"), [""])
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB").addGeometry(Part.LineSegment(App.Vector(-2500.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(-2500.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB").addGeometry(Part.LineSegment(App.Vector(-2500.00000000000000,15875.00000000000000,0.00000000000000),App.Vector(-3500.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB").addGeometry(Part.LineSegment(App.Vector(-3500.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(-3500.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB").addGeometry(Part.LineSegment(App.Vector(-2500.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(-3500.00000000000000,8875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Pad","Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").Profile = App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJuB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").Type = 4
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJuB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Plane", "plane_Sketch_Ff6ta67jsVSbPU8_1_KJWB")
origin = App.Vector(-4500.00000000000000,375.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJWB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("Sketcher::SketchObject","Sketch_Ff6ta67jsVSbPU8_1_KJWB")
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJWB"), [""])
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(0.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,15875.00000000000000,0.00000000000000),App.Vector(-1000.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB").addGeometry(Part.LineSegment(App.Vector(-1000.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(-1000.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(-1000.00000000000000,8875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Pad","Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").Profile = App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJWB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").Type = 4
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJWB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Plane", "plane_Sketch_Ff6ta67jsVSbPU8_1_KJKB")
origin = App.Vector(-4500.00000000000000,375.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJKB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("Sketcher::SketchObject","Sketch_Ff6ta67jsVSbPU8_1_KJKB")
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJKB"), [""])
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB").addGeometry(Part.LineSegment(App.Vector(1000.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(1000.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB").addGeometry(Part.LineSegment(App.Vector(1000.00000000000000,15875.00000000000000,0.00000000000000),App.Vector(0.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(0.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB").addGeometry(Part.LineSegment(App.Vector(1000.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(0.00000000000000,8875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Pad","Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").Profile = App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJKB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").Type = 4
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJKB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Plane", "plane_Sketch_Ff6ta67jsVSbPU8_1_JJy")
origin = App.Vector(-4500.00000000000000,375.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_JJy").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("Sketcher::SketchObject","Sketch_Ff6ta67jsVSbPU8_1_JJy")
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_JJy"), [""])
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy").addGeometry(Part.LineSegment(App.Vector(3500.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(3500.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy").addGeometry(Part.LineSegment(App.Vector(3500.00000000000000,15875.00000000000000,0.00000000000000),App.Vector(2500.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy").addGeometry(Part.LineSegment(App.Vector(2500.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(2500.00000000000000,15875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy").addGeometry(Part.LineSegment(App.Vector(3500.00000000000000,8875.00000000000000,0.00000000000000),App.Vector(2500.00000000000000,8875.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Pad","Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").Profile = App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJy"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").Type = 4
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJy").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Plane", "plane_Sketch_Ff6ta67jsVSbPU8_1_KJmB")
origin = App.Vector(-4500.00000000000000,375.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJmB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("Sketcher::SketchObject","Sketch_Ff6ta67jsVSbPU8_1_KJmB")
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJmB"), [""])
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB").addGeometry(Part.LineSegment(App.Vector(-2500.00000000000000,375.00000000000000,0.00000000000000),App.Vector(-2500.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB").addGeometry(Part.LineSegment(App.Vector(-2500.00000000000000,7375.00000000000000,0.00000000000000),App.Vector(-3500.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB").addGeometry(Part.LineSegment(App.Vector(-3500.00000000000000,375.00000000000000,0.00000000000000),App.Vector(-3500.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB").addGeometry(Part.LineSegment(App.Vector(-2500.00000000000000,375.00000000000000,0.00000000000000),App.Vector(-3500.00000000000000,375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Pad","Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").Profile = App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJmB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").Type = 4
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJmB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Plane", "plane_Sketch_Ff6ta67jsVSbPU8_1_KJOB")
origin = App.Vector(-4500.00000000000000,375.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJOB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("Sketcher::SketchObject","Sketch_Ff6ta67jsVSbPU8_1_KJOB")
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJOB"), [""])
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,375.00000000000000,0.00000000000000),App.Vector(0.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,7375.00000000000000,0.00000000000000),App.Vector(-1000.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB").addGeometry(Part.LineSegment(App.Vector(-1000.00000000000000,375.00000000000000,0.00000000000000),App.Vector(-1000.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,375.00000000000000,0.00000000000000),App.Vector(-1000.00000000000000,375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Pad","Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").Profile = App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJOB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").Type = 4
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJOB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Plane", "plane_Sketch_Ff6ta67jsVSbPU8_1_KJCB")
origin = App.Vector(-4500.00000000000000,375.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJCB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("Sketcher::SketchObject","Sketch_Ff6ta67jsVSbPU8_1_KJCB")
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_KJCB"), [""])
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB").addGeometry(Part.LineSegment(App.Vector(1000.00000000000000,375.00000000000000,0.00000000000000),App.Vector(1000.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB").addGeometry(Part.LineSegment(App.Vector(1000.00000000000000,7375.00000000000000,0.00000000000000),App.Vector(0.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,375.00000000000000,0.00000000000000),App.Vector(0.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB").addGeometry(Part.LineSegment(App.Vector(1000.00000000000000,375.00000000000000,0.00000000000000),App.Vector(0.00000000000000,375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Pad","Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").Profile = App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_KJCB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").Type = 4
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_KJCB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Plane", "plane_Sketch_Ff6ta67jsVSbPU8_1_JJq")
origin = App.Vector(-4500.00000000000000,375.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_JJq").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("Sketcher::SketchObject","Sketch_Ff6ta67jsVSbPU8_1_JJq")
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff6ta67jsVSbPU8_1_JJq"), [""])
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq").addGeometry(Part.LineSegment(App.Vector(3500.00000000000000,375.00000000000000,0.00000000000000),App.Vector(3500.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq").addGeometry(Part.LineSegment(App.Vector(3500.00000000000000,7375.00000000000000,0.00000000000000),App.Vector(2500.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq").addGeometry(Part.LineSegment(App.Vector(2500.00000000000000,375.00000000000000,0.00000000000000),App.Vector(2500.00000000000000,7375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq").addGeometry(Part.LineSegment(App.Vector(3500.00000000000000,375.00000000000000,0.00000000000000),App.Vector(2500.00000000000000,375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJ17AxElGgz9dRH_0").newObject("PartDesign::Pad","Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").Profile = App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq")
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff6ta67jsVSbPU8_1_JJq"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").Type = 4
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff6ta67jsVSbPU8_1_FLKU51eRpoQqkj8_1_JJq").Offset = 0
App.ActiveDocument.recompute()

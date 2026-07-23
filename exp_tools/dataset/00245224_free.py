import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00245224")
App.ActiveDocument.addObject("PartDesign::Body","Body_FSz5kd2zxdLJgqC_0")
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").Label = "Body_FSz5kd2zxdLJgqC_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Plane", "plane_Sketch_FSz5kd2zxdLJgqC_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSz5kd2zxdLJgqC_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("Sketcher::SketchObject","Sketch_FSz5kd2zxdLJgqC_0_JGO")
App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSz5kd2zxdLJgqC_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-381.00000000000000,762.00000000000000,0.00000000000000),App.Vector(381.00000000000000,762.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(381.00000000000000,762.00000000000000,0.00000000000000),App.Vector(381.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(381.00000000000000,0.00000000000000,0.00000000000000),App.Vector(349.63972999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,482.83582000000001,0.00000000000000),App.Vector(349.63972999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-349.63972999999999,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,482.83582000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-381.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-349.63972999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-381.00000000000000,762.00000000000000,0.00000000000000),App.Vector(-381.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-355.60000000000002,736.60000000000002,0.00000000000000),App.Vector(-355.60000000000002,35.07619000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-355.60000000000002,35.07619000000000,0.00000000000000),App.Vector(-15.68013000000000,504.48934000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-15.68013000000000,504.48934000000003,0.00000000000000),App.Vector(-183.76026999999999,736.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-355.60000000000002,736.60000000000002,0.00000000000000),App.Vector(-183.76026999999999,736.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(355.60000000000002,736.60000000000002,0.00000000000000),App.Vector(355.60000000000002,35.07619000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(355.60000000000002,35.07619000000000,0.00000000000000),App.Vector(15.68013000000000,504.48934000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(15.68013000000000,504.48934000000003,0.00000000000000),App.Vector(183.76026999999999,736.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(355.60000000000002,736.60000000000002,0.00000000000000),App.Vector(183.76026999999999,736.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,736.60000000000002,0.00000000000000),App.Vector(152.40000000000001,736.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,736.60000000000002,0.00000000000000),App.Vector(0.00000000000000,526.14286000000004,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,736.60000000000002,0.00000000000000),App.Vector(0.00000000000000,526.14286000000004,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Pad","Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO")
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO")
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSz5kd2zxdLJgqC_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSz5kd2zxdLJgqC_0_FeK9V1LcV2O3eIZ_0_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Plane", "plane_Sketch_FXp2lRLwyw0kUT3_1_JKC")
origin = App.Vector(0.00000000000000,-25.40000000000000,381.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXp2lRLwyw0kUT3_1_JKC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("Sketcher::SketchObject","Sketch_FXp2lRLwyw0kUT3_1_JKC")
App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXp2lRLwyw0kUT3_1_JKC"), [""])
App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKC").addGeometry(Part.Circle(App.Vector(-279.39999999999998,368.29999999999995,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Pocket","Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC")
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").Profile = App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKC")
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").Type = 4
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Plane", "plane_Sketch_FXp2lRLwyw0kUT3_1_JKG")
origin = App.Vector(0.00000000000000,-25.40000000000000,381.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXp2lRLwyw0kUT3_1_JKG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("Sketcher::SketchObject","Sketch_FXp2lRLwyw0kUT3_1_JKG")
App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXp2lRLwyw0kUT3_1_JKG"), [""])
App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKG").addGeometry(Part.Circle(App.Vector(0.00000000000000,368.29999999999995,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Pocket","Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG")
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").Profile = App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKG")
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").Type = 4
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Plane", "plane_Sketch_FXp2lRLwyw0kUT3_1_JKK")
origin = App.Vector(0.00000000000000,-25.40000000000000,381.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXp2lRLwyw0kUT3_1_JKK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("Sketcher::SketchObject","Sketch_FXp2lRLwyw0kUT3_1_JKK")
App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXp2lRLwyw0kUT3_1_JKK"), [""])
App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKK").addGeometry(Part.Circle(App.Vector(279.39999999999998,368.29999999999995,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Pocket","Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK")
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").Profile = App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKK")
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXp2lRLwyw0kUT3_1_JKK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").Type = 4
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXp2lRLwyw0kUT3_1_FKwj8xxDXDyVtVU_1_JKK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Plane", "plane_Sketch_F9rLXhJT1DADfU0_1_JPC")
origin = App.Vector(0.00000000000000,-12.70000000000000,762.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9rLXhJT1DADfU0_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("Sketcher::SketchObject","Sketch_F9rLXhJT1DADfU0_1_JPC")
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9rLXhJT1DADfU0_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPC").addGeometry(Part.Circle(App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Pocket","Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC")
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPC")
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Plane", "plane_Sketch_F9rLXhJT1DADfU0_1_JPG")
origin = App.Vector(0.00000000000000,-12.70000000000000,762.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9rLXhJT1DADfU0_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("Sketcher::SketchObject","Sketch_F9rLXhJT1DADfU0_1_JPG")
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9rLXhJT1DADfU0_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPG").addGeometry(Part.Circle(App.Vector(50.80000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Pocket","Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG")
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPG")
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Plane", "plane_Sketch_F9rLXhJT1DADfU0_1_JPK")
origin = App.Vector(0.00000000000000,-12.70000000000000,762.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9rLXhJT1DADfU0_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("Sketcher::SketchObject","Sketch_F9rLXhJT1DADfU0_1_JPK")
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9rLXhJT1DADfU0_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPK").addGeometry(Part.Circle(App.Vector(304.80000000000001,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Pocket","Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK")
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPK")
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Plane", "plane_Sketch_F9rLXhJT1DADfU0_1_JPO")
origin = App.Vector(0.00000000000000,-12.70000000000000,762.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9rLXhJT1DADfU0_1_JPO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("Sketcher::SketchObject","Sketch_F9rLXhJT1DADfU0_1_JPO")
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9rLXhJT1DADfU0_1_JPO"), [""])
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPO").addGeometry(Part.Circle(App.Vector(-304.80000000000001,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSz5kd2zxdLJgqC_0").newObject("PartDesign::Pocket","Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO")
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").Profile = App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPO")
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9rLXhJT1DADfU0_1_JPO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").Type = 4
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9rLXhJT1DADfU0_1_FVayDXf4pxteasQ_1_JPO").Offset = 0
App.ActiveDocument.recompute()

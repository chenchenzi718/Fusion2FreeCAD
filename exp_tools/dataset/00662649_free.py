import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00662649")
App.ActiveDocument.addObject("PartDesign::Body","Body_F6BpljctZ4vODW9_0")
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").Label = "Body_F6BpljctZ4vODW9_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Plane", "plane_Sketch_F6BpljctZ4vODW9_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6BpljctZ4vODW9_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("Sketcher::SketchObject","Sketch_F6BpljctZ4vODW9_0_JGG")
App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6BpljctZ4vODW9_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-580.10130000000004,-235.65837999999999,0.00000000000000),App.Vector(639.09870000000001,-235.65837999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").addGeometry(Part.LineSegment(App.Vector(639.09870000000001,-235.65837999999999,0.00000000000000),App.Vector(639.09870000000001,373.94162000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-580.10130000000004,373.94162000000000,0.00000000000000),App.Vector(639.09870000000001,373.94162000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-580.10130000000004,-235.65837999999999,0.00000000000000),App.Vector(-580.10130000000004,373.94162000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-599.15130000000011,-254.70838000000001,0.00000000000000),App.Vector(658.14870000000008,-254.70838000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").addGeometry(Part.LineSegment(App.Vector(658.14870000000008,-254.70838000000001,0.00000000000000),App.Vector(658.14870000000008,392.99162000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-599.15130000000011,392.99162000000001,0.00000000000000),App.Vector(658.14870000000008,392.99162000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-599.15130000000011,-254.70838000000001,0.00000000000000),App.Vector(-599.15130000000011,392.99162000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Pad","Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG")
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG")
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").Length = 63.5
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").Type = 0
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").Reversed = 1
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FcGFlRsJ9VGDPmr_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Plane", "plane_Sketch_F6BpljctZ4vODW9_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6BpljctZ4vODW9_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("Sketcher::SketchObject","Sketch_F6BpljctZ4vODW9_0_JGC")
App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6BpljctZ4vODW9_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC").addGeometry(Part.LineSegment(App.Vector(-580.10130000000004,-235.65837999999999,0.00000000000000),App.Vector(639.09870000000001,-235.65837999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC").addGeometry(Part.LineSegment(App.Vector(639.09870000000001,-235.65837999999999,0.00000000000000),App.Vector(639.09870000000001,373.94162000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC").addGeometry(Part.LineSegment(App.Vector(-580.10130000000004,373.94162000000000,0.00000000000000),App.Vector(639.09870000000001,373.94162000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC").addGeometry(Part.LineSegment(App.Vector(-580.10130000000004,-235.65837999999999,0.00000000000000),App.Vector(-580.10130000000004,373.94162000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Pad","Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC")
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC")
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").Length = 19.05
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6BpljctZ4vODW9_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6BpljctZ4vODW9_0_FJwj3pMy1Ov427h_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Plane", "plane_Sketch_Fg3mnlWcYcdPvsX_1_JLO")
origin = App.Vector(29.49870000000000,69.14162000000000,-19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg3mnlWcYcdPvsX_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("Sketcher::SketchObject","Sketch_Fg3mnlWcYcdPvsX_1_JLO")
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg3mnlWcYcdPvsX_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO").addGeometry(Part.LineSegment(App.Vector(609.60000000000002,304.80000000000001,0.00000000000000),App.Vector(558.79999999999995,304.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO").addGeometry(Part.LineSegment(App.Vector(558.79999999999995,304.80000000000001,0.00000000000000),App.Vector(558.79999999999995,254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO").addGeometry(Part.LineSegment(App.Vector(609.60000000000002,254.00000000000000,0.00000000000000),App.Vector(558.79999999999995,254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO").addGeometry(Part.LineSegment(App.Vector(609.60000000000002,304.80000000000001,0.00000000000000),App.Vector(609.60000000000002,254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Pad","Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO")
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO")
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").Length = 787.4000000000001
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Plane", "plane_Sketch_Fg3mnlWcYcdPvsX_1_JLK")
origin = App.Vector(29.49870000000000,69.14162000000000,-19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg3mnlWcYcdPvsX_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("Sketcher::SketchObject","Sketch_Fg3mnlWcYcdPvsX_1_JLK")
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg3mnlWcYcdPvsX_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK").addGeometry(Part.LineSegment(App.Vector(609.60000000000002,-304.79999999999995,0.00000000000000),App.Vector(558.79999999999995,-304.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK").addGeometry(Part.LineSegment(App.Vector(558.79999999999995,-304.79999999999995,0.00000000000000),App.Vector(558.79999999999995,-254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK").addGeometry(Part.LineSegment(App.Vector(609.60000000000002,-254.00000000000000,0.00000000000000),App.Vector(558.79999999999995,-254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK").addGeometry(Part.LineSegment(App.Vector(609.60000000000002,-304.79999999999995,0.00000000000000),App.Vector(609.60000000000002,-254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Pad","Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK")
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK")
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").Length = 787.4000000000001
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Plane", "plane_Sketch_Fg3mnlWcYcdPvsX_1_JLG")
origin = App.Vector(29.49870000000000,69.14162000000000,-19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg3mnlWcYcdPvsX_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("Sketcher::SketchObject","Sketch_Fg3mnlWcYcdPvsX_1_JLG")
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg3mnlWcYcdPvsX_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG").addGeometry(Part.LineSegment(App.Vector(-609.60000000000002,-304.79999999999995,0.00000000000000),App.Vector(-558.79999999999995,-304.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG").addGeometry(Part.LineSegment(App.Vector(-558.79999999999995,-304.79999999999995,0.00000000000000),App.Vector(-558.79999999999995,-254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG").addGeometry(Part.LineSegment(App.Vector(-609.60000000000002,-254.00000000000000,0.00000000000000),App.Vector(-558.79999999999995,-254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG").addGeometry(Part.LineSegment(App.Vector(-609.60000000000002,-304.79999999999995,0.00000000000000),App.Vector(-609.60000000000002,-254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Pad","Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG")
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG")
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").Length = 787.4000000000001
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Plane", "plane_Sketch_Fg3mnlWcYcdPvsX_1_JLC")
origin = App.Vector(29.49870000000000,69.14162000000000,-19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg3mnlWcYcdPvsX_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("Sketcher::SketchObject","Sketch_Fg3mnlWcYcdPvsX_1_JLC")
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg3mnlWcYcdPvsX_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC").addGeometry(Part.LineSegment(App.Vector(-609.60000000000002,304.80000000000001,0.00000000000000),App.Vector(-558.79999999999995,304.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC").addGeometry(Part.LineSegment(App.Vector(-558.79999999999995,304.80000000000001,0.00000000000000),App.Vector(-558.79999999999995,254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC").addGeometry(Part.LineSegment(App.Vector(-609.60000000000002,254.00000000000000,0.00000000000000),App.Vector(-558.79999999999995,254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC").addGeometry(Part.LineSegment(App.Vector(-609.60000000000002,304.80000000000001,0.00000000000000),App.Vector(-609.60000000000002,254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Pad","Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC")
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC")
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").Length = 787.4000000000001
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg3mnlWcYcdPvsX_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg3mnlWcYcdPvsX_1_F4GGKHNnN7YMVOJ_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Plane", "plane_Sketch_FPNzdH7SxEQDip7_1_JPC")
origin = App.Vector(-529.30129999999997,348.54162000000002,-412.75000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPNzdH7SxEQDip7_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("Sketcher::SketchObject","Sketch_FPNzdH7SxEQDip7_1_JPC")
App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPNzdH7SxEQDip7_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC").addGeometry(Part.LineSegment(App.Vector(-25.39999999999998,259.78699000000000,0.00000000000000),App.Vector(-6.35000000000002,259.78699000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000002,259.78699000000000,0.00000000000000),App.Vector(-6.35000000000002,196.28699000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC").addGeometry(Part.LineSegment(App.Vector(-25.39999999999998,196.28699000000000,0.00000000000000),App.Vector(-6.35000000000002,196.28699000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC").addGeometry(Part.LineSegment(App.Vector(-25.39999999999998,259.78699000000000,0.00000000000000),App.Vector(-25.39999999999998,196.28699000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Pad","Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC")
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC")
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").Length = 1117.6000000000001
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPNzdH7SxEQDip7_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPNzdH7SxEQDip7_1_Fnuw7c2bfuZOLAp_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Plane", "plane_Sketch_FhnTRhrq3xud15t_1_JVC")
origin = App.Vector(-554.70129999999995,-184.85837999999998,-412.75000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhnTRhrq3xud15t_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("Sketcher::SketchObject","Sketch_FhnTRhrq3xud15t_1_JVC")
App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhnTRhrq3xud15t_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),19.05000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Pad","Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC")
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JVC")
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").Length = 508.0
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Plane", "plane_Sketch_FhnTRhrq3xud15t_1_JTC")
origin = App.Vector(613.69870000000003,-184.85837999999998,-412.75000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhnTRhrq3xud15t_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("Sketcher::SketchObject","Sketch_FhnTRhrq3xud15t_1_JTC")
App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhnTRhrq3xud15t_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JTC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),19.05000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6BpljctZ4vODW9_0").newObject("PartDesign::Pad","Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC")
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JTC")
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").Length = 508.0
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhnTRhrq3xud15t_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhnTRhrq3xud15t_1_FsBEfxF7A4ftgEq_1_JTC").Offset = 0
App.ActiveDocument.recompute()

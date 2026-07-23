import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00389492")
App.ActiveDocument.addObject("PartDesign::Body","Body_F0aTHxziocIopPC_0")
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").Label = "Body_F0aTHxziocIopPC_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGi")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGi")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGi"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.LineSegment(App.Vector(-288.21350999999999,93.22352000000001,0.00000000000000),App.Vector(361.78649000000001,93.22352000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.LineSegment(App.Vector(361.78649000000001,93.22352000000001,0.00000000000000),App.Vector(361.78649000000001,-356.77647999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.LineSegment(App.Vector(-288.21350999999999,-356.77647999999999,0.00000000000000),App.Vector(361.78649000000001,-356.77647999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.LineSegment(App.Vector(-288.21350999999999,93.22352000000001,0.00000000000000),App.Vector(-288.21350999999999,-356.77647999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.LineSegment(App.Vector(-263.28086999999999,45.86319000000000,0.00000000000000),App.Vector(225.71678000000000,45.86319000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.LineSegment(App.Vector(225.71678000000000,45.86319000000000,0.00000000000000),App.Vector(225.71678000000000,-303.80362000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.LineSegment(App.Vector(-263.28086999999999,-303.80362000000002,0.00000000000000),App.Vector(225.71678000000000,-303.80362000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.LineSegment(App.Vector(-263.28086999999999,45.86319000000000,0.00000000000000),App.Vector(-263.28086999999999,-303.80362000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.Circle(App.Vector(296.83303999999998,-33.82764000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.86545000000000),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.Circle(App.Vector(296.83303999999998,-88.08876000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.86545000000000),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.Circle(App.Vector(296.83303999999998,-138.12173999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.86545000000000),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").addGeometry(Part.Circle(App.Vector(296.83303999999998,-190.26877999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.86545000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").Length = 10.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_F9K0bZQKDFlDmTf_0_JGi").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGm")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGm").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGm")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGm"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").addGeometry(Part.LineSegment(App.Vector(-263.28086999999999,45.86319000000000,0.00000000000000),App.Vector(225.71678000000000,45.86319000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").addGeometry(Part.LineSegment(App.Vector(225.71678000000000,45.86319000000000,0.00000000000000),App.Vector(225.71678000000000,-303.80362000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").addGeometry(Part.LineSegment(App.Vector(-263.28086999999999,-303.80362000000002,0.00000000000000),App.Vector(225.71678000000000,-303.80362000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").addGeometry(Part.LineSegment(App.Vector(-263.28086999999999,45.86319000000000,0.00000000000000),App.Vector(-263.28086999999999,-303.80362000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").addGeometry(Part.Circle(App.Vector(-148.59216999999998,-19.20514000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),28.85416000000000),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").addGeometry(Part.Circle(App.Vector(107.13816000000000,-19.20514000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.49126000000000),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").addGeometry(Part.Circle(App.Vector(107.13816000000000,-211.84781000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),37.76934000000000),False)

App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").addGeometry(Part.Circle(App.Vector(-148.59216999999998,-211.84781000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),56.83295000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").Length = 5.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGm"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_Fb1rCvCcf3iG8io_1_JGm").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGC")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGC").addGeometry(Part.Circle(App.Vector(-148.59216999999998,-19.20514000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),28.85416000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGC")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").Length = 10.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGG")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGG").addGeometry(Part.Circle(App.Vector(107.13816000000000,-19.20514000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.49126000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGG")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").Length = 10.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGK")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGK").addGeometry(Part.Circle(App.Vector(107.13816000000000,-211.84781000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),37.76934000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGK")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").Length = 10.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGO")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGO").addGeometry(Part.Circle(App.Vector(-148.59216999999998,-211.84781000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),56.83295000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGO")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").Length = 10.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FcprZbsAM3YAlca_1_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGS")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGS").addGeometry(Part.Circle(App.Vector(296.83303999999998,-33.82764000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.86545000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGS")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGW")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGW"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGW").addGeometry(Part.Circle(App.Vector(296.83303999999998,-88.08876000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.86545000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGW")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGa")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGa"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGa").addGeometry(Part.Circle(App.Vector(296.83303999999998,-138.12173999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.86545000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGa")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Plane", "plane_Sketch_F0aTHxziocIopPC_0_JGe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("Sketcher::SketchObject","Sketch_F0aTHxziocIopPC_0_JGe")
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0aTHxziocIopPC_0_JGe"), [""])
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGe").addGeometry(Part.Circle(App.Vector(296.83303999999998,-190.26877999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),14.86545000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0aTHxziocIopPC_0").newObject("PartDesign::Pad","Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").Profile = App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGe")
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0aTHxziocIopPC_0_JGe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").Type = 4
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0aTHxziocIopPC_0_FHCUVlxw6i2eGHC_1_JGe").Offset = 0
App.ActiveDocument.recompute()

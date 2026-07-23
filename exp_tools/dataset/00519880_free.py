import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00519880")
App.ActiveDocument.addObject("PartDesign::Body","Body_FZxtxxO1ACuLKAA_0")
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").Label = "Body_FZxtxxO1ACuLKAA_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Plane", "plane_Sketch_FZxtxxO1ACuLKAA_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZxtxxO1ACuLKAA_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("Sketcher::SketchObject","Sketch_FZxtxxO1ACuLKAA_0_JGC")
App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZxtxxO1ACuLKAA_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,62.23000000000000,0.00000000000000),App.Vector(22.22500000000000,62.23000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC").addGeometry(Part.LineSegment(App.Vector(22.22500000000000,62.23000000000000,0.00000000000000),App.Vector(22.22500000000000,-62.23000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,-62.23000000000000,0.00000000000000),App.Vector(22.22500000000000,-62.23000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,62.23000000000000,0.00000000000000),App.Vector(-22.22500000000000,-62.23000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Pad","Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC")
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC")
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").Length = 5.943600000000001
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZxtxxO1ACuLKAA_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZxtxxO1ACuLKAA_0_FAk2TcZMedlZjwX_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Plane", "plane_Sketch_FoYiDCTWmjuz5Ke_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoYiDCTWmjuz5Ke_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("Sketcher::SketchObject","Sketch_FoYiDCTWmjuz5Ke_1_JJC")
App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoYiDCTWmjuz5Ke_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC").addGeometry(Part.LineSegment(App.Vector(-9.20750000000000,16.19250000000000,0.00000000000000),App.Vector(9.20750000000000,16.19250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC").addGeometry(Part.LineSegment(App.Vector(9.20750000000000,16.19250000000000,0.00000000000000),App.Vector(9.20750000000000,-16.19250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC").addGeometry(Part.LineSegment(App.Vector(-9.20750000000000,-16.19250000000000,0.00000000000000),App.Vector(9.20750000000000,-16.19250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC").addGeometry(Part.LineSegment(App.Vector(-9.20750000000000,16.19250000000000,0.00000000000000),App.Vector(-9.20750000000000,-16.19250000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Pocket","Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC")
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC")
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoYiDCTWmjuz5Ke_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoYiDCTWmjuz5Ke_1_FZjuyUnDMH12ob3_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Plane", "plane_Sketch_FSw9Ta1XtbqpsqP_1_JNC")
origin = App.Vector(22.17259000000000,0.00000000000000,0.37338000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("Sketcher::SketchObject","Sketch_FSw9Ta1XtbqpsqP_1_JNC")
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-0.05241000000000,69.41636000000000,0.00000000000000),App.Vector(-0.04644000000000,61.85662000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-0.04644000000000,61.85662000000000,0.00000000000000),App.Vector(13.09342000000000,61.85662000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC").addGeometry(Part.LineSegment(App.Vector(13.08745000000000,69.41636000000000,0.00000000000000),App.Vector(13.09342000000000,61.85662000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-0.05241000000000,69.41636000000000,0.00000000000000),App.Vector(13.08745000000000,69.41636000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Pad","Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Plane", "plane_Sketch_FSw9Ta1XtbqpsqP_1_JNK")
origin = App.Vector(22.17259000000000,0.00000000000000,0.37338000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("Sketcher::SketchObject","Sketch_FSw9Ta1XtbqpsqP_1_JNK")
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK").addGeometry(Part.LineSegment(App.Vector(44.39759000000000,69.41636000000000,0.00000000000000),App.Vector(31.68791000000000,69.41636000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK").addGeometry(Part.LineSegment(App.Vector(31.68791000000000,69.41636000000000,0.00000000000000),App.Vector(31.67134000000000,61.85662000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK").addGeometry(Part.LineSegment(App.Vector(44.38102000000000,61.85662000000000,0.00000000000000),App.Vector(31.67134000000000,61.85662000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK").addGeometry(Part.LineSegment(App.Vector(44.39759000000000,69.41636000000000,0.00000000000000),App.Vector(44.38102000000000,61.85662000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Pad","Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Plane", "plane_Sketch_FSw9Ta1XtbqpsqP_1_JNi")
origin = App.Vector(22.17259000000000,0.00000000000000,0.37338000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("Sketcher::SketchObject","Sketch_FSw9Ta1XtbqpsqP_1_JNi")
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNi"), [""])
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi").addGeometry(Part.LineSegment(App.Vector(44.38102000000000,61.85662000000000,0.00000000000000),App.Vector(44.10825999999999,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi").addGeometry(Part.LineSegment(App.Vector(44.10825999999999,-62.60338000000000,0.00000000000000),App.Vector(31.39858000000000,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi").addGeometry(Part.LineSegment(App.Vector(31.67134000000000,61.85662000000000,0.00000000000000),App.Vector(31.39858000000000,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi").addGeometry(Part.LineSegment(App.Vector(44.38102000000000,61.85662000000000,0.00000000000000),App.Vector(31.67134000000000,61.85662000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Pad","Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").Profile = App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").Type = 4
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNi").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Plane", "plane_Sketch_FSw9Ta1XtbqpsqP_1_JNG")
origin = App.Vector(22.17259000000000,0.00000000000000,0.37338000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("Sketcher::SketchObject","Sketch_FSw9Ta1XtbqpsqP_1_JNG")
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG").addGeometry(Part.LineSegment(App.Vector(0.05845000000000,-71.05032000000000,0.00000000000000),App.Vector(0.05179000000000,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG").addGeometry(Part.LineSegment(App.Vector(0.05179000000000,-62.60338000000000,0.00000000000000),App.Vector(13.19165000000000,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG").addGeometry(Part.LineSegment(App.Vector(13.19830000000000,-71.03915000000001,0.00000000000000),App.Vector(13.19165000000000,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG").addGeometry(Part.LineSegment(App.Vector(0.05845000000000,-71.05032000000000,0.00000000000000),App.Vector(13.19830000000000,-71.03915000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Pad","Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Plane", "plane_Sketch_FSw9Ta1XtbqpsqP_1_JNO")
origin = App.Vector(22.17259000000000,0.00000000000000,0.37338000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("Sketcher::SketchObject","Sketch_FSw9Ta1XtbqpsqP_1_JNO")
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO").addGeometry(Part.LineSegment(App.Vector(44.08975000000000,-71.05032000000000,0.00000000000000),App.Vector(44.10825999999999,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO").addGeometry(Part.LineSegment(App.Vector(44.10825999999999,-62.60338000000000,0.00000000000000),App.Vector(31.39858000000000,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO").addGeometry(Part.LineSegment(App.Vector(31.38009000000000,-71.03915000000001,0.00000000000000),App.Vector(31.39858000000000,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO").addGeometry(Part.LineSegment(App.Vector(44.08975000000000,-71.05032000000000,0.00000000000000),App.Vector(31.38009000000000,-71.03915000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Pad","Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Plane", "plane_Sketch_FSw9Ta1XtbqpsqP_1_JNq")
origin = App.Vector(22.17259000000000,0.00000000000000,0.37338000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNq").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("Sketcher::SketchObject","Sketch_FSw9Ta1XtbqpsqP_1_JNq")
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSw9Ta1XtbqpsqP_1_JNq"), [""])
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").addGeometry(Part.LineSegment(App.Vector(-0.04644000000000,61.85662000000000,0.00000000000000),App.Vector(0.05179000000000,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").addGeometry(Part.LineSegment(App.Vector(0.05179000000000,-62.60338000000000,0.00000000000000),App.Vector(13.19165000000000,-62.60338000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").addGeometry(Part.LineSegment(App.Vector(13.19165000000000,-62.60338000000000,0.00000000000000),App.Vector(13.15531000000000,-16.56588000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").addGeometry(Part.LineSegment(App.Vector(12.96509000000000,-16.56588000000000,0.00000000000000),App.Vector(13.15531000000000,-16.56588000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").addGeometry(Part.LineSegment(App.Vector(12.96509000000000,15.81912000000000,0.00000000000000),App.Vector(12.96509000000000,-16.56588000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").addGeometry(Part.LineSegment(App.Vector(12.96509000000000,15.81912000000000,0.00000000000000),App.Vector(13.12975000000000,15.81912000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").addGeometry(Part.LineSegment(App.Vector(13.09342000000000,61.85662000000000,0.00000000000000),App.Vector(13.12975000000000,15.81912000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").addGeometry(Part.LineSegment(App.Vector(-0.04644000000000,61.85662000000000,0.00000000000000),App.Vector(13.09342000000000,61.85662000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZxtxxO1ACuLKAA_0").newObject("PartDesign::Pad","Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").Profile = App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq")
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSw9Ta1XtbqpsqP_1_JNq"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").Type = 4
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSw9Ta1XtbqpsqP_1_FWeFzsd2MDtMvI4_1_JNq").Offset = 0
App.ActiveDocument.recompute()

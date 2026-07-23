import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00316429")
App.ActiveDocument.addObject("PartDesign::Body","Body_FZTxcu23WVn5JFc_0")
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").Label = "Body_FZTxcu23WVn5JFc_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Plane", "plane_Sketch_FZTxcu23WVn5JFc_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZTxcu23WVn5JFc_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("Sketcher::SketchObject","Sketch_FZTxcu23WVn5JFc_0_JGC")
App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZTxcu23WVn5JFc_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,16.00000000000000,0.00000000000000),App.Vector(16.00000000000000,16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,16.00000000000000,0.00000000000000),App.Vector(16.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,-16.00000000000000,0.00000000000000),App.Vector(16.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,16.00000000000000,0.00000000000000),App.Vector(-16.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Pad","Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC")
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC")
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").Length = 1.7
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZTxcu23WVn5JFc_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZTxcu23WVn5JFc_0_FWJwBwxRPXwQUpt_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Plane", "plane_Sketch_F1KwSRyq7ax1fzG_1_JJC")
origin = App.Vector(-14.00000000000000,-1.70000000000000,-14.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1KwSRyq7ax1fzG_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("Sketcher::SketchObject","Sketch_F1KwSRyq7ax1fzG_1_JJC")
App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1KwSRyq7ax1fzG_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,2.00000000000000,0.00000000000000),App.Vector(2.00000000000000,2.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,2.00000000000000,0.00000000000000),App.Vector(2.00000000000000,-2.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,-2.00000000000000,0.00000000000000),App.Vector(26.00000000000000,-2.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(26.00000000000000,2.00000000000000,0.00000000000000),App.Vector(26.00000000000000,-2.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,2.00000000000000,0.00000000000000),App.Vector(26.00000000000000,2.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,2.00000000000000,0.00000000000000),App.Vector(30.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,26.00000000000000,0.00000000000000),App.Vector(26.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(26.00000000000000,26.00000000000000,0.00000000000000),App.Vector(26.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,30.00000000000000,0.00000000000000),App.Vector(26.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,26.00000000000000,0.00000000000000),App.Vector(2.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,26.00000000000000,0.00000000000000),App.Vector(2.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,2.00000000000000,0.00000000000000),App.Vector(-2.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Pad","Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC")
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC")
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").Length = 3.0
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1KwSRyq7ax1fzG_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1KwSRyq7ax1fzG_1_FxQTzNeXAGY331z_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Plane", "plane_Sketch_FzeTtO3niNNOW6r_1_JNC")
origin = App.Vector(0.00000000000000,-4.70000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("Sketcher::SketchObject","Sketch_FzeTtO3niNNOW6r_1_JNC")
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNC").addGeometry(Part.LineSegment(App.Vector(-8.12500000000000,1.07500000000000,0.00000000000000),App.Vector(-8.12500000000000,-1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-8.12500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),1.07500000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Pad","Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNC")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Plane", "plane_Sketch_FzeTtO3niNNOW6r_1_JNG")
origin = App.Vector(0.00000000000000,-4.70000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("Sketcher::SketchObject","Sketch_FzeTtO3niNNOW6r_1_JNG")
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG").addGeometry(Part.LineSegment(App.Vector(-8.12500000000000,1.07500000000000,0.00000000000000),App.Vector(-8.12500000000000,-1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG").addGeometry(Part.LineSegment(App.Vector(-8.12500000000000,-1.07500000000000,0.00000000000000),App.Vector(-10.12500000000000,-1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-10.12500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),1.07500000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG").addGeometry(Part.LineSegment(App.Vector(-8.12500000000000,1.07500000000000,0.00000000000000),App.Vector(-10.12500000000000,1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Pad","Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").Length = 5.0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Plane", "plane_Sketch_FzeTtO3niNNOW6r_1_JNK")
origin = App.Vector(0.00000000000000,-4.70000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("Sketcher::SketchObject","Sketch_FzeTtO3niNNOW6r_1_JNK")
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNK").addGeometry(Part.LineSegment(App.Vector(8.12500000000000,-1.07500000000000,0.00000000000000),App.Vector(8.12500000000000,1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(8.12500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),1.07500000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Pad","Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNK")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").Length = 5.0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Plane", "plane_Sketch_FzeTtO3niNNOW6r_1_JNO")
origin = App.Vector(0.00000000000000,-4.70000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("Sketcher::SketchObject","Sketch_FzeTtO3niNNOW6r_1_JNO")
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO").addGeometry(Part.LineSegment(App.Vector(8.12500000000000,-1.07500000000000,0.00000000000000),App.Vector(8.12500000000000,1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO").addGeometry(Part.LineSegment(App.Vector(8.12500000000000,1.07500000000000,0.00000000000000),App.Vector(10.12500000000000,1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(10.12500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),1.07500000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO").addGeometry(Part.LineSegment(App.Vector(8.12500000000000,-1.07500000000000,0.00000000000000),App.Vector(10.12500000000000,-1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Pad","Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").Length = 5.0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Plane", "plane_Sketch_FzeTtO3niNNOW6r_1_JNS")
origin = App.Vector(0.00000000000000,-4.70000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("Sketcher::SketchObject","Sketch_FzeTtO3niNNOW6r_1_JNS")
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzeTtO3niNNOW6r_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").addGeometry(Part.LineSegment(App.Vector(-8.12500000000000,8.12500000000000,0.00000000000000),App.Vector(8.12500000000000,8.12500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").addGeometry(Part.LineSegment(App.Vector(8.12500000000000,8.12500000000000,0.00000000000000),App.Vector(8.12500000000000,1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(8.12500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),1.07500000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").addGeometry(Part.LineSegment(App.Vector(8.12500000000000,-8.12500000000000,0.00000000000000),App.Vector(8.12500000000000,-1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").addGeometry(Part.LineSegment(App.Vector(-8.12500000000000,-8.12500000000000,0.00000000000000),App.Vector(8.12500000000000,-8.12500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").addGeometry(Part.LineSegment(App.Vector(-8.12500000000000,-8.12500000000000,0.00000000000000),App.Vector(-8.12500000000000,-1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-8.12500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),1.07500000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").addGeometry(Part.LineSegment(App.Vector(-8.12500000000000,8.12500000000000,0.00000000000000),App.Vector(-8.12500000000000,1.07500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Pad","Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS")
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").Length = 5.0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzeTtO3niNNOW6r_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzeTtO3niNNOW6r_1_FYZcqROykT3JAE5_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Plane", "plane_Sketch_Fm1JwaVB9pFkWSj_1_JRC")
origin = App.Vector(0.00000000000000,-9.70000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fm1JwaVB9pFkWSj_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("Sketcher::SketchObject","Sketch_Fm1JwaVB9pFkWSj_1_JRC")
App.ActiveDocument.getObject("Sketch_Fm1JwaVB9pFkWSj_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fm1JwaVB9pFkWSj_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fm1JwaVB9pFkWSj_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fm1JwaVB9pFkWSj_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.85000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fm1JwaVB9pFkWSj_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fm1JwaVB9pFkWSj_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Pad","Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC")
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fm1JwaVB9pFkWSj_1_JRC")
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").Length = 3.0
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fm1JwaVB9pFkWSj_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fm1JwaVB9pFkWSj_1_FLqFjpjLvD6iEcd_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Plane", "plane_Sketch_FQlhsxGwdjMidaT_1_JVC")
origin = App.Vector(0.00000000000000,-12.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQlhsxGwdjMidaT_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("Sketcher::SketchObject","Sketch_FQlhsxGwdjMidaT_1_JVC")
App.ActiveDocument.getObject("Sketch_FQlhsxGwdjMidaT_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQlhsxGwdjMidaT_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FQlhsxGwdjMidaT_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQlhsxGwdjMidaT_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQlhsxGwdjMidaT_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQlhsxGwdjMidaT_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZTxcu23WVn5JFc_0").newObject("PartDesign::Pad","Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC")
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FQlhsxGwdjMidaT_1_JVC")
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").Length = 3.3
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQlhsxGwdjMidaT_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQlhsxGwdjMidaT_1_FAJx3YbdvbbPdeU_1_JVC").Offset = 0
App.ActiveDocument.recompute()

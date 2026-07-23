import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00068838")
App.ActiveDocument.addObject("PartDesign::Body","Body_FzYALM22do8DXHe_0")
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").Label = "Body_FzYALM22do8DXHe_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_FzYALM22do8DXHe_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzYALM22do8DXHe_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_FzYALM22do8DXHe_0_JGC")
App.ActiveDocument.getObject("Sketch_FzYALM22do8DXHe_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzYALM22do8DXHe_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FzYALM22do8DXHe_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzYALM22do8DXHe_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),50.80000000000000),False)

App.ActiveDocument.getObject("Sketch_FzYALM22do8DXHe_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),12.70000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzYALM22do8DXHe_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzYALM22do8DXHe_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pad","Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC")
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FzYALM22do8DXHe_0_JGC")
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzYALM22do8DXHe_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzYALM22do8DXHe_0_FAvU6cLi7s9VvHY_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_FX6S6no4CtA3yXY_1_JJK")
origin = App.Vector(0.00000000000000,-6.35000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FX6S6no4CtA3yXY_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_FX6S6no4CtA3yXY_1_JJK")
App.ActiveDocument.getObject("Sketch_FX6S6no4CtA3yXY_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FX6S6no4CtA3yXY_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FX6S6no4CtA3yXY_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FX6S6no4CtA3yXY_1_JJK").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),18.41500000000000),False)

App.ActiveDocument.getObject("Sketch_FX6S6no4CtA3yXY_1_JJK").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),28.57500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FX6S6no4CtA3yXY_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FX6S6no4CtA3yXY_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pad","Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK")
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FX6S6no4CtA3yXY_1_JJK")
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FX6S6no4CtA3yXY_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FX6S6no4CtA3yXY_1_FZB4e3pp0gGWH7a_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_F9BAnnSeppK0vq3_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9BAnnSeppK0vq3_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_F9BAnnSeppK0vq3_1_JNC")
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9BAnnSeppK0vq3_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,25.40000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pad","Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC")
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNC")
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_F9BAnnSeppK0vq3_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9BAnnSeppK0vq3_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_F9BAnnSeppK0vq3_1_JNG")
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9BAnnSeppK0vq3_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNG").addGeometry(Part.Circle(App.Vector(25.40000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pad","Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG")
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNG")
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_F9BAnnSeppK0vq3_1_JNK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9BAnnSeppK0vq3_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_F9BAnnSeppK0vq3_1_JNK")
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9BAnnSeppK0vq3_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNK").addGeometry(Part.Circle(App.Vector(0.00000000000000,-25.40000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pad","Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK")
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNK")
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_F9BAnnSeppK0vq3_1_JNO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9BAnnSeppK0vq3_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_F9BAnnSeppK0vq3_1_JNO")
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9BAnnSeppK0vq3_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNO").addGeometry(Part.Circle(App.Vector(-25.40000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pad","Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO")
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNO")
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9BAnnSeppK0vq3_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9BAnnSeppK0vq3_1_FLQSJKKfbWfqlCZ_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_FtimWkyWagGs9iy_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtimWkyWagGs9iy_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_FtimWkyWagGs9iy_1_JRC")
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtimWkyWagGs9iy_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRC").addGeometry(Part.Circle(App.Vector(-40.41115000000000,13.47038000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pocket","Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC")
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRC")
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_FtimWkyWagGs9iy_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtimWkyWagGs9iy_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_FtimWkyWagGs9iy_1_JRG")
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtimWkyWagGs9iy_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRG").addGeometry(Part.Circle(App.Vector(13.47038000000000,-40.41115000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pocket","Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG")
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRG")
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_FtimWkyWagGs9iy_1_JRK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtimWkyWagGs9iy_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_FtimWkyWagGs9iy_1_JRK")
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtimWkyWagGs9iy_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRK").addGeometry(Part.Circle(App.Vector(40.41115000000000,-13.47038000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pocket","Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK")
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRK")
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Plane", "plane_Sketch_FtimWkyWagGs9iy_1_JRO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtimWkyWagGs9iy_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("Sketcher::SketchObject","Sketch_FtimWkyWagGs9iy_1_JRO")
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtimWkyWagGs9iy_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRO").addGeometry(Part.Circle(App.Vector(-13.47038000000000,40.41115000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzYALM22do8DXHe_0").newObject("PartDesign::Pocket","Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO")
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRO")
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtimWkyWagGs9iy_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtimWkyWagGs9iy_1_F1Ev0haALlGJDXN_1_JRO").Offset = 0
App.ActiveDocument.recompute()

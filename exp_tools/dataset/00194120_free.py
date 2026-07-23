import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00194120")
App.ActiveDocument.addObject("PartDesign::Body","Body_F6qpihWDVHSL0t1_0")
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").Label = "Body_F6qpihWDVHSL0t1_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Plane", "plane_Sketch_F6qpihWDVHSL0t1_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6qpihWDVHSL0t1_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("Sketcher::SketchObject","Sketch_F6qpihWDVHSL0t1_0_JGC")
App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6qpihWDVHSL0t1_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,101.59999999999999,0.00000000000000),App.Vector(76.20000000000000,101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC").addGeometry(Part.LineSegment(App.Vector(76.20000000000000,101.59999999999999,0.00000000000000),App.Vector(76.20000000000000,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,-101.59999999999999,0.00000000000000),App.Vector(76.20000000000000,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,101.59999999999999,0.00000000000000),App.Vector(-76.20000000000000,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Pad","Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC")
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC")
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6qpihWDVHSL0t1_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6qpihWDVHSL0t1_0_FtOgRm6egMbcRgS_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Plane", "plane_Sketch_FGqj9d98wrddPzV_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGqj9d98wrddPzV_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("Sketcher::SketchObject","Sketch_FGqj9d98wrddPzV_1_JNC")
App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGqj9d98wrddPzV_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNC").addGeometry(Part.Circle(App.Vector(-63.73252000000000,82.91246000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Pocket","Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC")
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNC")
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Plane", "plane_Sketch_FGqj9d98wrddPzV_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGqj9d98wrddPzV_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("Sketcher::SketchObject","Sketch_FGqj9d98wrddPzV_1_JNG")
App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGqj9d98wrddPzV_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNG").addGeometry(Part.Circle(App.Vector(-63.73252000000000,70.18349000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Pocket","Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG")
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNG")
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGqj9d98wrddPzV_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").Type = 0
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGqj9d98wrddPzV_1_FGLlKDH9ovAUHzT_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Plane", "plane_Sketch_FBgkWfZUZgd4unU_1_JPC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBgkWfZUZgd4unU_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("Sketcher::SketchObject","Sketch_FBgkWfZUZgd4unU_1_JPC")
App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBgkWfZUZgd4unU_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JPC").addGeometry(Part.Circle(App.Vector(63.42077000000000,82.79934000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Pocket","Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC")
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JPC")
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").Length = 127.0
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").Type = 0
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Plane", "plane_Sketch_FBgkWfZUZgd4unU_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBgkWfZUZgd4unU_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("Sketcher::SketchObject","Sketch_FBgkWfZUZgd4unU_1_JRC")
App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBgkWfZUZgd4unU_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JRC").addGeometry(Part.Circle(App.Vector(63.42077000000000,70.27178000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Pocket","Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC")
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JRC")
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").Length = 127.0
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBgkWfZUZgd4unU_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBgkWfZUZgd4unU_1_F8dn8INpcrlqEEC_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Plane", "plane_Sketch_FVs8SpmrTJiucOw_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVs8SpmrTJiucOw_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("Sketcher::SketchObject","Sketch_FVs8SpmrTJiucOw_1_JVC")
App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVs8SpmrTJiucOw_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JVC").addGeometry(Part.Circle(App.Vector(-63.42077000000000,-69.48880000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Pocket","Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC")
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JVC")
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").Length = 127.0
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").Type = 0
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Plane", "plane_Sketch_FVs8SpmrTJiucOw_1_JTC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVs8SpmrTJiucOw_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("Sketcher::SketchObject","Sketch_FVs8SpmrTJiucOw_1_JTC")
App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVs8SpmrTJiucOw_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JTC").addGeometry(Part.Circle(App.Vector(-63.81225999999999,-82.01635999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Pocket","Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC")
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JTC")
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").Length = 127.0
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVs8SpmrTJiucOw_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").Type = 0
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVs8SpmrTJiucOw_1_F6wbj6S1t9qfDhN_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Plane", "plane_Sketch_FVp2tDDZA96D2JZ_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVp2tDDZA96D2JZ_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("Sketcher::SketchObject","Sketch_FVp2tDDZA96D2JZ_1_JZC")
App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVp2tDDZA96D2JZ_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JZC").addGeometry(Part.Circle(App.Vector(63.42077000000000,-69.88029000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Pocket","Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC")
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JZC")
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").Type = 0
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Plane", "plane_Sketch_FVp2tDDZA96D2JZ_1_JXC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVp2tDDZA96D2JZ_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("Sketcher::SketchObject","Sketch_FVp2tDDZA96D2JZ_1_JXC")
App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVp2tDDZA96D2JZ_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JXC").addGeometry(Part.Circle(App.Vector(63.81225999999999,-82.01635999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F6qpihWDVHSL0t1_0").newObject("PartDesign::Pocket","Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC")
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JXC")
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVp2tDDZA96D2JZ_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").Type = 0
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVp2tDDZA96D2JZ_1_F3GKqQ3GZHi13fF_1_JXC").Offset = 0
App.ActiveDocument.recompute()

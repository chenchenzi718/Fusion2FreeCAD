import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00412308")
App.ActiveDocument.addObject("PartDesign::Body","Body_FGsgMY5xpoyM0fs_0")
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").Label = "Body_FGsgMY5xpoyM0fs_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FGsgMY5xpoyM0fs_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGsgMY5xpoyM0fs_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("Sketcher::SketchObject","Sketch_FGsgMY5xpoyM0fs_0_JGK")
App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGsgMY5xpoyM0fs_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,7.50000000000000,0.00000000000000),App.Vector(-50.00000000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,7.50000000000000,0.00000000000000),App.Vector(-50.00000000000000,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,-7.50000000000000,0.00000000000000),App.Vector(-50.00000000000000,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,7.50000000000000,0.00000000000000),App.Vector(50.00000000000000,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,4.50000000000000,0.00000000000000),App.Vector(-31.50000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(-31.50000000000000,4.50000000000000,0.00000000000000),App.Vector(-31.50000000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,1.50000000000000,0.00000000000000),App.Vector(-31.50000000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,4.50000000000000,0.00000000000000),App.Vector(31.50000000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,-1.50000000000000,0.00000000000000),App.Vector(-31.50000000000000,-1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(-31.50000000000000,-1.50000000000000,0.00000000000000),App.Vector(-31.50000000000000,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,-4.50000000000000,0.00000000000000),App.Vector(-31.50000000000000,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,-1.50000000000000,0.00000000000000),App.Vector(31.50000000000000,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Pad","Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK")
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK")
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGsgMY5xpoyM0fs_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGsgMY5xpoyM0fs_0_FmVGmZPSNEhzjVS_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FR03lw6MoXv5B9T_1_JJC")
origin = App.Vector(42.25000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR03lw6MoXv5B9T_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("Sketcher::SketchObject","Sketch_FR03lw6MoXv5B9T_1_JJC")
App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR03lw6MoXv5B9T_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,4.50000000000000,0.00000000000000),App.Vector(73.75000000000001,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC").addGeometry(Part.LineSegment(App.Vector(73.75000000000001,4.50000000000000,0.00000000000000),App.Vector(73.75000000000001,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,1.50000000000000,0.00000000000000),App.Vector(73.75000000000001,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,4.50000000000000,0.00000000000000),App.Vector(10.75000000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Pocket","Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC")
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC")
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FR03lw6MoXv5B9T_1_JJG")
origin = App.Vector(42.25000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR03lw6MoXv5B9T_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("Sketcher::SketchObject","Sketch_FR03lw6MoXv5B9T_1_JJG")
App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR03lw6MoXv5B9T_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,-1.50000000000000,0.00000000000000),App.Vector(73.75000000000001,-1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG").addGeometry(Part.LineSegment(App.Vector(73.75000000000001,-1.50000000000000,0.00000000000000),App.Vector(73.75000000000001,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,-4.50000000000000,0.00000000000000),App.Vector(73.75000000000001,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,-1.50000000000000,0.00000000000000),App.Vector(10.75000000000000,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Pocket","Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG")
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG")
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").Length = 2.0
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FR03lw6MoXv5B9T_1_JJK")
origin = App.Vector(42.25000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR03lw6MoXv5B9T_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("Sketcher::SketchObject","Sketch_FR03lw6MoXv5B9T_1_JJK")
App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR03lw6MoXv5B9T_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(7.75000000000000,7.50000000000000,0.00000000000000),App.Vector(76.75000000000001,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(76.75000000000001,7.50000000000000,0.00000000000000),App.Vector(76.75000000000001,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(7.75000000000000,-7.50000000000000,0.00000000000000),App.Vector(76.75000000000001,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(7.75000000000000,7.50000000000000,0.00000000000000),App.Vector(7.75000000000000,-7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,4.50000000000000,0.00000000000000),App.Vector(73.75000000000001,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(73.75000000000001,4.50000000000000,0.00000000000000),App.Vector(73.75000000000001,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,1.50000000000000,0.00000000000000),App.Vector(73.75000000000001,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,4.50000000000000,0.00000000000000),App.Vector(10.75000000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,-1.50000000000000,0.00000000000000),App.Vector(73.75000000000001,-1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(73.75000000000001,-1.50000000000000,0.00000000000000),App.Vector(73.75000000000001,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,-4.50000000000000,0.00000000000000),App.Vector(73.75000000000001,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").addGeometry(Part.LineSegment(App.Vector(10.75000000000000,-1.50000000000000,0.00000000000000),App.Vector(10.75000000000000,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Pocket","Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK")
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK")
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").Length = 2.0
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR03lw6MoXv5B9T_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR03lw6MoXv5B9T_1_Fo0TQ463MumClTr_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FTAvIzcNMT5ZCLh_1_JNC")
origin = App.Vector(42.25000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTAvIzcNMT5ZCLh_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("Sketcher::SketchObject","Sketch_FTAvIzcNMT5ZCLh_1_JNC")
App.ActiveDocument.getObject("Sketch_FTAvIzcNMT5ZCLh_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTAvIzcNMT5ZCLh_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FTAvIzcNMT5ZCLh_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTAvIzcNMT5ZCLh_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTAvIzcNMT5ZCLh_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTAvIzcNMT5ZCLh_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Pocket","Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC")
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FTAvIzcNMT5ZCLh_1_JNC")
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTAvIzcNMT5ZCLh_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTAvIzcNMT5ZCLh_1_FsSfIwtpzaaH3zq_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FOn6RGjoLZNXaRv_1_JRC")
origin = App.Vector(-42.25000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOn6RGjoLZNXaRv_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("Sketcher::SketchObject","Sketch_FOn6RGjoLZNXaRv_1_JRC")
App.ActiveDocument.getObject("Sketch_FOn6RGjoLZNXaRv_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOn6RGjoLZNXaRv_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FOn6RGjoLZNXaRv_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOn6RGjoLZNXaRv_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOn6RGjoLZNXaRv_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOn6RGjoLZNXaRv_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Pocket","Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC")
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FOn6RGjoLZNXaRv_1_JRC")
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOn6RGjoLZNXaRv_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOn6RGjoLZNXaRv_1_F4kqLTKdi13CVpu_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FAPyn3N7w01QqOn_1_JVO")
origin = App.Vector(0.00000000000000,-4.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAPyn3N7w01QqOn_1_JVO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("Sketcher::SketchObject","Sketch_FAPyn3N7w01QqOn_1_JVO")
App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAPyn3N7w01QqOn_1_JVO"), [""])
App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,4.50000000000000,0.00000000000000),App.Vector(22.50000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO").addGeometry(Part.LineSegment(App.Vector(22.50000000000000,4.50000000000000,0.00000000000000),App.Vector(22.50000000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,1.50000000000000,0.00000000000000),App.Vector(22.50000000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,4.50000000000000,0.00000000000000),App.Vector(31.50000000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Pad","Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO")
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").Profile = App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO")
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").Length = 2.0
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAPyn3N7w01QqOn_1_JVO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").Type = 0
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").Reversed = 1
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAPyn3N7w01QqOn_1_FC4YVCnICFJNZKe_1_JVO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FmIhf9QZgcSWELV_1_JaC")
origin = App.Vector(0.00000000000000,-4.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmIhf9QZgcSWELV_1_JaC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("Sketcher::SketchObject","Sketch_FmIhf9QZgcSWELV_1_JaC")
App.ActiveDocument.getObject("Sketch_FmIhf9QZgcSWELV_1_JaC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmIhf9QZgcSWELV_1_JaC"), [""])
App.ActiveDocument.getObject("Sketch_FmIhf9QZgcSWELV_1_JaC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmIhf9QZgcSWELV_1_JaC").addGeometry(Part.Circle(App.Vector(27.00000000000000,3.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmIhf9QZgcSWELV_1_JaC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmIhf9QZgcSWELV_1_JaC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGsgMY5xpoyM0fs_0").newObject("PartDesign::Pocket","Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC")
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").Profile = App.ActiveDocument.getObject("Sketch_FmIhf9QZgcSWELV_1_JaC")
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmIhf9QZgcSWELV_1_JaC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").Type = 4
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmIhf9QZgcSWELV_1_FEuzkGCdVGUUkJv_1_JaC").Offset = 0
App.ActiveDocument.recompute()

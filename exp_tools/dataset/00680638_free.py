import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00680638")
App.ActiveDocument.addObject("PartDesign::Body","Body_FYR05t8ZAMJkqv9_0")
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").Label = "Body_FYR05t8ZAMJkqv9_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Plane", "plane_Sketch_FYR05t8ZAMJkqv9_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYR05t8ZAMJkqv9_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("Sketcher::SketchObject","Sketch_FYR05t8ZAMJkqv9_0_JGO")
App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYR05t8ZAMJkqv9_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(-5.33000000000000,16.51000000000000,0.00000000000000),App.Vector(5.33000000000000,16.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(5.33000000000000,16.51000000000000,0.00000000000000),App.Vector(5.33000000000000,14.89000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(5.33000000000000,14.89000000000000,0.00000000000000),App.Vector(4.53000000000000,14.89000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(4.53000000000000,14.89000000000000,0.00000000000000),App.Vector(4.53000000000000,13.09000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(5.33000000000000,13.09000000000000,0.00000000000000),App.Vector(4.53000000000000,13.09000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(5.33000000000000,0.00000000000000,0.00000000000000),App.Vector(5.33000000000000,13.09000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(-5.33000000000000,0.00000000000000,0.00000000000000),App.Vector(5.33000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(-5.33000000000000,0.00000000000000,0.00000000000000),App.Vector(-5.33000000000000,13.09000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(-5.33000000000000,13.09000000000000,0.00000000000000),App.Vector(-4.53000000000000,13.09000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(-4.53000000000000,14.89000000000000,0.00000000000000),App.Vector(-4.53000000000000,13.09000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(-5.33000000000000,14.89000000000000,0.00000000000000),App.Vector(-4.53000000000000,14.89000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.LineSegment(App.Vector(-5.33000000000000,16.51000000000000,0.00000000000000),App.Vector(-5.33000000000000,14.89000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").addGeometry(Part.Circle(App.Vector(0.00000000000000,13.09000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.04000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Pad","Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO")
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO")
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").Length = 1.4
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYR05t8ZAMJkqv9_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").Type = 0
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").Reversed = 1
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYR05t8ZAMJkqv9_0_FNXvIFJSYHNq35t_0_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Plane", "plane_Sketch_FhDUoKOG7tkQH1x_1_JJC")
origin = App.Vector(-0.00000000000000,0.00000000000000,13.08500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhDUoKOG7tkQH1x_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("Sketcher::SketchObject","Sketch_FhDUoKOG7tkQH1x_1_JJC")
App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhDUoKOG7tkQH1x_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC").addGeometry(Part.LineSegment(App.Vector(-5.33000000000000,-3.42500000000000,0.00000000000000),App.Vector(5.33000000000000,-3.42500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC").addGeometry(Part.LineSegment(App.Vector(5.33000000000000,-13.08500000000000,0.00000000000000),App.Vector(5.33000000000000,-3.42500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC").addGeometry(Part.LineSegment(App.Vector(-5.33000000000000,-13.08500000000000,0.00000000000000),App.Vector(5.33000000000000,-13.08500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC").addGeometry(Part.LineSegment(App.Vector(-5.33000000000000,-13.08500000000000,0.00000000000000),App.Vector(-5.33000000000000,-3.42500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Pad","Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC")
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC")
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").Length = 3.42
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhDUoKOG7tkQH1x_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhDUoKOG7tkQH1x_1_F3FuWqnJ5KB6DXG_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Plane", "plane_Sketch_F97AqmpEfQPuM2A_1_JNC")
origin = App.Vector(0.00000000000000,-1.01000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F97AqmpEfQPuM2A_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("Sketcher::SketchObject","Sketch_F97AqmpEfQPuM2A_1_JNC")
App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F97AqmpEfQPuM2A_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC").addGeometry(Part.LineSegment(App.Vector(-3.67500000000000,0.51000000000000,0.00000000000000),App.Vector(-1.90500000000000,0.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC").addGeometry(Part.LineSegment(App.Vector(-1.90500000000000,0.51000000000000,0.00000000000000),App.Vector(-1.90500000000000,1.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC").addGeometry(Part.LineSegment(App.Vector(-3.67500000000000,1.51000000000000,0.00000000000000),App.Vector(-1.90500000000000,1.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC").addGeometry(Part.LineSegment(App.Vector(-3.67500000000000,0.51000000000000,0.00000000000000),App.Vector(-3.67500000000000,1.51000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Pad","Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC")
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC")
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").Length = 6.35
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Plane", "plane_Sketch_F97AqmpEfQPuM2A_1_JNG")
origin = App.Vector(0.00000000000000,-1.01000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F97AqmpEfQPuM2A_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("Sketcher::SketchObject","Sketch_F97AqmpEfQPuM2A_1_JNG")
App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F97AqmpEfQPuM2A_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG").addGeometry(Part.LineSegment(App.Vector(0.88500000000000,0.51000000000000,0.00000000000000),App.Vector(0.88500000000000,1.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG").addGeometry(Part.LineSegment(App.Vector(0.88500000000000,1.51000000000000,0.00000000000000),App.Vector(-0.88500000000000,1.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG").addGeometry(Part.LineSegment(App.Vector(-0.88500000000000,1.51000000000000,0.00000000000000),App.Vector(-0.88500000000000,0.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG").addGeometry(Part.LineSegment(App.Vector(0.88500000000000,0.51000000000000,0.00000000000000),App.Vector(-0.88500000000000,0.51000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Pad","Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG")
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG")
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").Length = 6.35
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Plane", "plane_Sketch_F97AqmpEfQPuM2A_1_JNK")
origin = App.Vector(0.00000000000000,-1.01000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F97AqmpEfQPuM2A_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("Sketcher::SketchObject","Sketch_F97AqmpEfQPuM2A_1_JNK")
App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F97AqmpEfQPuM2A_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK").addGeometry(Part.LineSegment(App.Vector(3.67500000000000,0.51000000000000,0.00000000000000),App.Vector(3.67500000000000,1.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK").addGeometry(Part.LineSegment(App.Vector(3.67500000000000,1.51000000000000,0.00000000000000),App.Vector(1.90500000000000,1.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK").addGeometry(Part.LineSegment(App.Vector(1.90500000000000,1.51000000000000,0.00000000000000),App.Vector(1.90500000000000,0.51000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK").addGeometry(Part.LineSegment(App.Vector(3.67500000000000,0.51000000000000,0.00000000000000),App.Vector(1.90500000000000,0.51000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Pad","Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK")
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK")
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").Length = 6.35
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F97AqmpEfQPuM2A_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F97AqmpEfQPuM2A_1_FRz8waSczhmH04o_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Plane", "plane_Sketch_FD2xXQqTnFyaF1d_1_JRC")
origin = App.Vector(-3.48500000000000,-2.02000000000000,-6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FD2xXQqTnFyaF1d_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("Sketcher::SketchObject","Sketch_FD2xXQqTnFyaF1d_1_JRC")
App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FD2xXQqTnFyaF1d_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC").addGeometry(Part.LineSegment(App.Vector(2.98000000000000,0.50000000000000,0.00000000000000),App.Vector(3.99000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC").addGeometry(Part.LineSegment(App.Vector(3.99000000000000,0.50000000000000,0.00000000000000),App.Vector(3.99000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC").addGeometry(Part.LineSegment(App.Vector(3.99000000000000,-0.50000000000000,0.00000000000000),App.Vector(2.98000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC").addGeometry(Part.LineSegment(App.Vector(2.98000000000000,0.50000000000000,0.00000000000000),App.Vector(2.98000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Pad","Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC")
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC")
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Plane", "plane_Sketch_FD2xXQqTnFyaF1d_1_JRG")
origin = App.Vector(-3.48500000000000,-2.02000000000000,-6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FD2xXQqTnFyaF1d_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("Sketcher::SketchObject","Sketch_FD2xXQqTnFyaF1d_1_JRG")
App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FD2xXQqTnFyaF1d_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG").addGeometry(Part.LineSegment(App.Vector(5.77000000000000,0.50000000000000,0.00000000000000),App.Vector(6.78000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG").addGeometry(Part.LineSegment(App.Vector(6.78000000000000,0.50000000000000,0.00000000000000),App.Vector(6.78000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG").addGeometry(Part.LineSegment(App.Vector(6.78000000000000,-0.50000000000000,0.00000000000000),App.Vector(5.77000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG").addGeometry(Part.LineSegment(App.Vector(5.77000000000000,0.50000000000000,0.00000000000000),App.Vector(5.77000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Pad","Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG")
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG")
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").Length = 3.0
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Plane", "plane_Sketch_FD2xXQqTnFyaF1d_1_JRK")
origin = App.Vector(-3.48500000000000,-2.02000000000000,-6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FD2xXQqTnFyaF1d_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("Sketcher::SketchObject","Sketch_FD2xXQqTnFyaF1d_1_JRK")
App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FD2xXQqTnFyaF1d_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK").addGeometry(Part.LineSegment(App.Vector(0.19000000000000,0.50000000000000,0.00000000000000),App.Vector(1.20000000000000,0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK").addGeometry(Part.LineSegment(App.Vector(1.20000000000000,0.50000000000000,0.00000000000000),App.Vector(1.20000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK").addGeometry(Part.LineSegment(App.Vector(0.19000000000000,-0.50000000000000,0.00000000000000),App.Vector(1.20000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK").addGeometry(Part.LineSegment(App.Vector(0.19000000000000,0.50000000000000,0.00000000000000),App.Vector(0.19000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYR05t8ZAMJkqv9_0").newObject("PartDesign::Pad","Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK")
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK")
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").Length = 3.0
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FD2xXQqTnFyaF1d_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FD2xXQqTnFyaF1d_1_FVnAzqbLSfX7ie1_1_JRK").Offset = 0
App.ActiveDocument.recompute()

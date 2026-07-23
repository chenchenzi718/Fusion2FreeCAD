import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00798949")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fc1H8KWGOx3kC3T_0")
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").Label = "Body_Fc1H8KWGOx3kC3T_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Plane", "plane_Sketch_Fc1H8KWGOx3kC3T_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fc1H8KWGOx3kC3T_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("Sketcher::SketchObject","Sketch_Fc1H8KWGOx3kC3T_0_JGC")
App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fc1H8KWGOx3kC3T_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC").addGeometry(Part.LineSegment(App.Vector(475.00000000000000,-137.50000000000000,0.00000000000000),App.Vector(-475.00000000000000,-137.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC").addGeometry(Part.LineSegment(App.Vector(-475.00000000000000,-137.50000000000000,0.00000000000000),App.Vector(-475.00000000000000,137.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC").addGeometry(Part.LineSegment(App.Vector(475.00000000000000,137.50000000000000,0.00000000000000),App.Vector(-475.00000000000000,137.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC").addGeometry(Part.LineSegment(App.Vector(475.00000000000000,-137.50000000000000,0.00000000000000),App.Vector(475.00000000000000,137.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Pad","Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC")
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC")
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fc1H8KWGOx3kC3T_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fc1H8KWGOx3kC3T_0_FPgFeTLcRfbF5xn_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Plane", "plane_Sketch_Fa6qYSZEwLQJhR9_1_JJC")
origin = App.Vector(0.00000000000000,-137.50000000000000,-115.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa6qYSZEwLQJhR9_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("Sketcher::SketchObject","Sketch_Fa6qYSZEwLQJhR9_1_JJC")
App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa6qYSZEwLQJhR9_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC").addGeometry(Part.LineSegment(App.Vector(450.00000000000000,115.00000000000000,0.00000000000000),App.Vector(-450.00000000000000,115.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC").addGeometry(Part.LineSegment(App.Vector(-450.00000000000000,115.00000000000000,0.00000000000000),App.Vector(-450.00000000000000,-124.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC").addGeometry(Part.LineSegment(App.Vector(-450.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(450.00000000000000,-124.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC").addGeometry(Part.LineSegment(App.Vector(450.00000000000000,115.00000000000000,0.00000000000000),App.Vector(450.00000000000000,-124.99999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Pad","Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC")
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC")
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa6qYSZEwLQJhR9_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa6qYSZEwLQJhR9_1_FTzYoFBdrCa6PQv_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Plane", "plane_Sketch_FvNg8GwO8cwd3cL_1_JNC")
origin = App.Vector(0.00000000000000,-137.50000000000000,-115.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FvNg8GwO8cwd3cL_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("Sketcher::SketchObject","Sketch_FvNg8GwO8cwd3cL_1_JNC")
App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FvNg8GwO8cwd3cL_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC").addGeometry(Part.LineSegment(App.Vector(-410.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(-210.00000000000000,-124.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC").addGeometry(Part.LineSegment(App.Vector(-210.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(-210.00000000000000,25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC").addGeometry(Part.LineSegment(App.Vector(-410.00000000000000,25.00000000000001,0.00000000000000),App.Vector(-210.00000000000000,25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC").addGeometry(Part.LineSegment(App.Vector(-410.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(-410.00000000000000,25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Pocket","Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC")
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC")
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Plane", "plane_Sketch_FvNg8GwO8cwd3cL_1_JNG")
origin = App.Vector(0.00000000000000,-137.50000000000000,-115.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FvNg8GwO8cwd3cL_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("Sketcher::SketchObject","Sketch_FvNg8GwO8cwd3cL_1_JNG")
App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FvNg8GwO8cwd3cL_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG").addGeometry(Part.LineSegment(App.Vector(-100.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(100.00000000000000,-124.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(100.00000000000000,25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG").addGeometry(Part.LineSegment(App.Vector(-100.00000000000000,25.00000000000001,0.00000000000000),App.Vector(100.00000000000000,25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG").addGeometry(Part.LineSegment(App.Vector(-100.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(-100.00000000000000,25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Pocket","Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG")
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG")
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").Length = 10.0
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Plane", "plane_Sketch_FvNg8GwO8cwd3cL_1_JNK")
origin = App.Vector(0.00000000000000,-137.50000000000000,-115.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FvNg8GwO8cwd3cL_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("Sketcher::SketchObject","Sketch_FvNg8GwO8cwd3cL_1_JNK")
App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FvNg8GwO8cwd3cL_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK").addGeometry(Part.LineSegment(App.Vector(210.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(410.00000000000000,-124.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK").addGeometry(Part.LineSegment(App.Vector(410.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(410.00000000000000,25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK").addGeometry(Part.LineSegment(App.Vector(210.00000000000000,25.00000000000001,0.00000000000000),App.Vector(410.00000000000000,25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK").addGeometry(Part.LineSegment(App.Vector(210.00000000000000,-124.99999999999999,0.00000000000000),App.Vector(210.00000000000000,25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Pocket","Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK")
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK")
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").Length = 10.0
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FvNg8GwO8cwd3cL_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FvNg8GwO8cwd3cL_1_Fuskw0RVGywMzEI_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Plane", "plane_Sketch_F0n5eD5f9ngNok0_1_JRK")
origin = App.Vector(0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0n5eD5f9ngNok0_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("Sketcher::SketchObject","Sketch_F0n5eD5f9ngNok0_1_JRK")
App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0n5eD5f9ngNok0_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK").addGeometry(Part.LineSegment(App.Vector(-265.00000000000000,132.50000000000000,0.00000000000000),App.Vector(-365.00000000000000,132.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK").addGeometry(Part.LineSegment(App.Vector(-365.00000000000000,132.50000000000000,0.00000000000000),App.Vector(-365.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK").addGeometry(Part.LineSegment(App.Vector(-265.00000000000000,32.50000000000000,0.00000000000000),App.Vector(-365.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK").addGeometry(Part.LineSegment(App.Vector(-265.00000000000000,132.50000000000000,0.00000000000000),App.Vector(-265.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Pocket","Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK")
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK")
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").Length = 10.0
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Plane", "plane_Sketch_F0n5eD5f9ngNok0_1_JRG")
origin = App.Vector(0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0n5eD5f9ngNok0_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("Sketcher::SketchObject","Sketch_F0n5eD5f9ngNok0_1_JRG")
App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0n5eD5f9ngNok0_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG").addGeometry(Part.LineSegment(App.Vector(55.00000000000000,132.50000000000000,0.00000000000000),App.Vector(-45.00000000000000,132.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG").addGeometry(Part.LineSegment(App.Vector(-45.00000000000000,132.50000000000000,0.00000000000000),App.Vector(-45.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG").addGeometry(Part.LineSegment(App.Vector(55.00000000000000,32.50000000000000,0.00000000000000),App.Vector(-45.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG").addGeometry(Part.LineSegment(App.Vector(55.00000000000000,132.50000000000000,0.00000000000000),App.Vector(55.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Pocket","Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG")
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG")
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").Length = 10.0
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Plane", "plane_Sketch_F0n5eD5f9ngNok0_1_JRC")
origin = App.Vector(0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0n5eD5f9ngNok0_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("Sketcher::SketchObject","Sketch_F0n5eD5f9ngNok0_1_JRC")
App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0n5eD5f9ngNok0_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC").addGeometry(Part.LineSegment(App.Vector(375.00000000000000,132.50000000000000,0.00000000000000),App.Vector(275.00000000000000,132.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC").addGeometry(Part.LineSegment(App.Vector(275.00000000000000,132.50000000000000,0.00000000000000),App.Vector(275.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC").addGeometry(Part.LineSegment(App.Vector(375.00000000000000,32.50000000000000,0.00000000000000),App.Vector(275.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC").addGeometry(Part.LineSegment(App.Vector(375.00000000000000,132.50000000000000,0.00000000000000),App.Vector(375.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fc1H8KWGOx3kC3T_0").newObject("PartDesign::Pocket","Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC")
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC")
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").Length = 10.0
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0n5eD5f9ngNok0_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0n5eD5f9ngNok0_1_FceNruP18jisVbd_1_JRC").Offset = 0
App.ActiveDocument.recompute()

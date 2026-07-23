import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00154155")
App.ActiveDocument.addObject("PartDesign::Body","Body_FqqWgT7OqQ89mCQ_0")
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").Label = "Body_FqqWgT7OqQ89mCQ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Plane", "plane_Sketch_FqqWgT7OqQ89mCQ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqqWgT7OqQ89mCQ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("Sketcher::SketchObject","Sketch_FqqWgT7OqQ89mCQ_0_JGC")
App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqqWgT7OqQ89mCQ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(507.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-507.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-507.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-507.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(507.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-507.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(507.00000000000000,25.00000000000000,0.00000000000000),App.Vector(507.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Pad","Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC")
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC")
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqqWgT7OqQ89mCQ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqqWgT7OqQ89mCQ_0_FqqXR5GcW550aBo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Plane", "plane_Sketch_FjyfDIClO4TwBmm_1_JJC")
origin = App.Vector(20.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjyfDIClO4TwBmm_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("Sketcher::SketchObject","Sketch_FjyfDIClO4TwBmm_1_JJC")
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjyfDIClO4TwBmm_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJC").addGeometry(Part.Circle(App.Vector(442.00000000000000,10.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Pocket","Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC")
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJC")
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Plane", "plane_Sketch_FjyfDIClO4TwBmm_1_JJG")
origin = App.Vector(20.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjyfDIClO4TwBmm_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("Sketcher::SketchObject","Sketch_FjyfDIClO4TwBmm_1_JJG")
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjyfDIClO4TwBmm_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJG").addGeometry(Part.Circle(App.Vector(442.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Pocket","Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG")
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJG")
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Plane", "plane_Sketch_FjyfDIClO4TwBmm_1_JJK")
origin = App.Vector(20.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjyfDIClO4TwBmm_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("Sketcher::SketchObject","Sketch_FjyfDIClO4TwBmm_1_JJK")
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjyfDIClO4TwBmm_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJK").addGeometry(Part.Circle(App.Vector(472.00000000000000,10.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Pocket","Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK")
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJK")
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Plane", "plane_Sketch_FjyfDIClO4TwBmm_1_JJO")
origin = App.Vector(20.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjyfDIClO4TwBmm_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("Sketcher::SketchObject","Sketch_FjyfDIClO4TwBmm_1_JJO")
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjyfDIClO4TwBmm_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJO").addGeometry(Part.Circle(App.Vector(472.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Pocket","Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO")
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJO")
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjyfDIClO4TwBmm_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjyfDIClO4TwBmm_1_FEnwwsq4RogdzL3_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Plane", "plane_Sketch_FaWOa66qbkszHez_1_JNG")
origin = App.Vector(507.00000000000000,-12.50000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaWOa66qbkszHez_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("Sketcher::SketchObject","Sketch_FaWOa66qbkszHez_1_JNG")
App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaWOa66qbkszHez_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG").addGeometry(Part.LineSegment(App.Vector(-9.50000000000000,22.00000000000000,0.00000000000000),App.Vector(9.50000000000000,22.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG").addGeometry(Part.LineSegment(App.Vector(9.50000000000000,22.00000000000000,0.00000000000000),App.Vector(9.50000000000000,-22.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG").addGeometry(Part.LineSegment(App.Vector(-9.50000000000000,-22.00000000000000,0.00000000000000),App.Vector(9.50000000000000,-22.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG").addGeometry(Part.LineSegment(App.Vector(-9.50000000000000,22.00000000000000,0.00000000000000),App.Vector(-9.50000000000000,-22.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Pocket","Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG")
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG")
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").Length = 1014.0
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaWOa66qbkszHez_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaWOa66qbkszHez_1_FAmu2vHGNdGWdQh_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Plane", "plane_Sketch_FJaiwevElYYfYLu_1_JRi")
origin = App.Vector(20.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJaiwevElYYfYLu_1_JRi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("Sketcher::SketchObject","Sketch_FJaiwevElYYfYLu_1_JRi")
App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJaiwevElYYfYLu_1_JRi"), [""])
App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi").addGeometry(Part.LineSegment(App.Vector(-527.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-487.00000000000006,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi").addGeometry(Part.LineSegment(App.Vector(-487.00000000000006,25.00000000000000,0.00000000000000),App.Vector(-487.00000000000006,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi").addGeometry(Part.LineSegment(App.Vector(-527.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-487.00000000000006,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi").addGeometry(Part.LineSegment(App.Vector(-527.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-527.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Pad","Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi")
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").Profile = App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi")
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").Length = 5.0
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").Type = 4
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRi").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Plane", "plane_Sketch_FJaiwevElYYfYLu_1_JRm")
origin = App.Vector(20.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJaiwevElYYfYLu_1_JRm").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("Sketcher::SketchObject","Sketch_FJaiwevElYYfYLu_1_JRm")
App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJaiwevElYYfYLu_1_JRm"), [""])
App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").addGeometry(Part.LineSegment(App.Vector(-527.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-587.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").addGeometry(Part.LineSegment(App.Vector(-587.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-587.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").addGeometry(Part.LineSegment(App.Vector(-527.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-587.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").addGeometry(Part.LineSegment(App.Vector(-527.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-527.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").addGeometry(Part.Circle(App.Vector(-572.00000000000011,10.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),5.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").addGeometry(Part.Circle(App.Vector(-572.00000000000011,-10.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),5.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").addGeometry(Part.Circle(App.Vector(-542.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),5.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").addGeometry(Part.Circle(App.Vector(-542.00000000000000,10.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqqWgT7OqQ89mCQ_0").newObject("PartDesign::Pad","Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm")
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").Profile = App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm")
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").Length = 5.0
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJaiwevElYYfYLu_1_JRm"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").Type = 4
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJaiwevElYYfYLu_1_F7ZqkfDlJpEcdyl_1_JRm").Offset = 0
App.ActiveDocument.recompute()

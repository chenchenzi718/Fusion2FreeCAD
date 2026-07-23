import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00628233")
App.ActiveDocument.addObject("PartDesign::Body","Body_FqHpiqGlBOHsrMh_0")
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").Label = "Body_FqHpiqGlBOHsrMh_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Plane", "plane_Sketch_FqHpiqGlBOHsrMh_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqHpiqGlBOHsrMh_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("Sketcher::SketchObject","Sketch_FqHpiqGlBOHsrMh_0_JGC")
App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqHpiqGlBOHsrMh_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC").addGeometry(Part.LineSegment(App.Vector(-74.97340000000000,56.26602000000000,0.00000000000000),App.Vector(74.97340000000000,56.26602000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC").addGeometry(Part.LineSegment(App.Vector(74.97340000000000,56.26602000000000,0.00000000000000),App.Vector(74.97340000000000,-55.97822000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC").addGeometry(Part.LineSegment(App.Vector(-74.97340000000000,-55.97822000000000,0.00000000000000),App.Vector(74.97340000000000,-55.97822000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC").addGeometry(Part.LineSegment(App.Vector(-74.97340000000000,56.26602000000000,0.00000000000000),App.Vector(-74.97340000000000,-55.97822000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Pad","Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC")
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC")
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqHpiqGlBOHsrMh_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqHpiqGlBOHsrMh_0_FBeLK0VBKWqLLq3_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Plane", "plane_Sketch_F7PpfMQyoi1U3SF_1_JJC")
origin = App.Vector(-0.00000000000000,0.14390000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7PpfMQyoi1U3SF_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("Sketcher::SketchObject","Sketch_F7PpfMQyoi1U3SF_1_JJC")
App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7PpfMQyoi1U3SF_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,19.99896000000000,0.00000000000000),App.Vector(20.14286000000000,19.99896000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC").addGeometry(Part.LineSegment(App.Vector(20.14286000000000,19.99896000000000,0.00000000000000),App.Vector(20.14286000000000,-20.00104000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC").addGeometry(Part.LineSegment(App.Vector(20.14286000000000,-20.00104000000000,0.00000000000000),App.Vector(-19.85714000000000,-20.00104000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC").addGeometry(Part.LineSegment(App.Vector(-19.85714000000000,-20.00104000000000,0.00000000000000),App.Vector(-19.85714000000000,19.99896000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,19.99896000000000,0.00000000000000),App.Vector(-19.85714000000000,19.99896000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Pad","Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC")
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC")
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7PpfMQyoi1U3SF_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7PpfMQyoi1U3SF_1_FTKguar6LFY4EhA_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Plane", "plane_Sketch_FZaByRBaJsjUuD4_1_JNC")
origin = App.Vector(0.14286000000000,0.14286000000000,35.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZaByRBaJsjUuD4_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("Sketcher::SketchObject","Sketch_FZaByRBaJsjUuD4_1_JNC")
App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZaByRBaJsjUuD4_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNC").addGeometry(Part.LineSegment(App.Vector(-16.14781000000000,7.08061000000000,0.00000000000000),App.Vector(16.14536000000000,-16.43108000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNC").addGeometry(Part.LineSegment(App.Vector(16.14536000000000,-16.43108000000000,0.00000000000000),App.Vector(16.14536000000000,7.08061000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNC").addGeometry(Part.LineSegment(App.Vector(-16.14781000000000,7.08061000000000,0.00000000000000),App.Vector(16.14536000000000,7.08061000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Pocket","Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC")
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNC")
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Plane", "plane_Sketch_FZaByRBaJsjUuD4_1_JNG")
origin = App.Vector(0.14286000000000,0.14286000000000,35.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZaByRBaJsjUuD4_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("Sketcher::SketchObject","Sketch_FZaByRBaJsjUuD4_1_JNG")
App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZaByRBaJsjUuD4_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG").addGeometry(Part.LineSegment(App.Vector(-3.40050000000000,-20.00000000000000,0.00000000000000),App.Vector(-3.40050000000000,-16.43108000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG").addGeometry(Part.LineSegment(App.Vector(-3.40050000000000,-16.43108000000000,0.00000000000000),App.Vector(2.54824000000000,-16.43108000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG").addGeometry(Part.LineSegment(App.Vector(2.54824000000000,-16.43108000000000,0.00000000000000),App.Vector(2.54824000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG").addGeometry(Part.LineSegment(App.Vector(-3.40050000000000,-20.00000000000000,0.00000000000000),App.Vector(2.54824000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Pocket","Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG")
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG")
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").Length = 10.0
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Plane", "plane_Sketch_FZaByRBaJsjUuD4_1_JNK")
origin = App.Vector(0.14286000000000,0.14286000000000,35.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZaByRBaJsjUuD4_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("Sketcher::SketchObject","Sketch_FZaByRBaJsjUuD4_1_JNK")
App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZaByRBaJsjUuD4_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK").addGeometry(Part.LineSegment(App.Vector(-16.14781000000000,7.08061000000000,0.00000000000000),App.Vector(-16.14781000000000,-16.43108000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK").addGeometry(Part.LineSegment(App.Vector(-16.14781000000000,-16.43108000000000,0.00000000000000),App.Vector(-3.40050000000000,-16.43108000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK").addGeometry(Part.LineSegment(App.Vector(-3.40050000000000,-16.43108000000000,0.00000000000000),App.Vector(2.54824000000000,-16.43108000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK").addGeometry(Part.LineSegment(App.Vector(16.14536000000000,-16.43108000000000,0.00000000000000),App.Vector(2.54824000000000,-16.43108000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK").addGeometry(Part.LineSegment(App.Vector(-16.14781000000000,7.08061000000000,0.00000000000000),App.Vector(16.14536000000000,-16.43108000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Pocket","Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK")
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK")
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").Length = 10.0
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZaByRBaJsjUuD4_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZaByRBaJsjUuD4_1_FvGQqkGoRutXPnd_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Plane", "plane_Sketch_Fb0UkJYYs8Iuv3R_1_JRC")
origin = App.Vector(0.24656000000000,-19.85714000000000,22.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb0UkJYYs8Iuv3R_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("Sketcher::SketchObject","Sketch_Fb0UkJYYs8Iuv3R_1_JRC")
App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb0UkJYYs8Iuv3R_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.89630000000000,12.50000000000000,0.00000000000000),App.Vector(74.39597999999998,-12.44379000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.89630000000000,-12.50000000000000,0.00000000000000),App.Vector(74.39597999999998,-12.44379000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.89630000000000,12.50000000000000,0.00000000000000),App.Vector(19.89630000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Pad","Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC")
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRC")
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").Length = 20.0
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Plane", "plane_Sketch_Fb0UkJYYs8Iuv3R_1_JRG")
origin = App.Vector(0.24656000000000,-19.85714000000000,22.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb0UkJYYs8Iuv3R_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("Sketcher::SketchObject","Sketch_Fb0UkJYYs8Iuv3R_1_JRG")
App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb0UkJYYs8Iuv3R_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRG").addGeometry(Part.LineSegment(App.Vector(-20.10370000000000,12.50000000000000,0.00000000000000),App.Vector(-74.88910000000000,-12.72707000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRG").addGeometry(Part.LineSegment(App.Vector(-20.10370000000000,-12.50000000000000,0.00000000000000),App.Vector(-74.88910000000000,-12.72707000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRG").addGeometry(Part.LineSegment(App.Vector(-20.10370000000000,12.50000000000000,0.00000000000000),App.Vector(-20.10370000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Pad","Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG")
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRG")
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").Length = 20.0
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb0UkJYYs8Iuv3R_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").Type = 0
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb0UkJYYs8Iuv3R_1_FR0yT13Q7NM1cIT_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Plane", "plane_Sketch_FYUBubyybu7WMom_1_JVC")
origin = App.Vector(-19.85714000000000,28.18631000000000,22.50000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYUBubyybu7WMom_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("Sketcher::SketchObject","Sketch_FYUBubyybu7WMom_1_JVC")
App.ActiveDocument.getObject("Sketch_FYUBubyybu7WMom_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYUBubyybu7WMom_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FYUBubyybu7WMom_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYUBubyybu7WMom_1_JVC").addGeometry(Part.LineSegment(App.Vector(8.04345000000000,12.50000000000000,0.00000000000000),App.Vector(-28.04346000000000,-12.44379000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYUBubyybu7WMom_1_JVC").addGeometry(Part.LineSegment(App.Vector(8.04345000000000,-12.50000000000000,0.00000000000000),App.Vector(-28.04346000000000,-12.44379000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYUBubyybu7WMom_1_JVC").addGeometry(Part.LineSegment(App.Vector(8.04345000000000,12.50000000000000,0.00000000000000),App.Vector(8.04345000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYUBubyybu7WMom_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYUBubyybu7WMom_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqHpiqGlBOHsrMh_0").newObject("PartDesign::Pad","Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC")
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FYUBubyybu7WMom_1_JVC")
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").Length = 40.0
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYUBubyybu7WMom_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").Type = 0
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYUBubyybu7WMom_1_FlpREubDrHYD1s8_1_JVC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00565137")
App.ActiveDocument.addObject("PartDesign::Body","Body_FIjNGRGE7nFN9zF_0")
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").Label = "Body_FIjNGRGE7nFN9zF_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Plane", "plane_Sketch_FIjNGRGE7nFN9zF_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIjNGRGE7nFN9zF_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("Sketcher::SketchObject","Sketch_FIjNGRGE7nFN9zF_0_JGC")
App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIjNGRGE7nFN9zF_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC").addGeometry(Part.LineSegment(App.Vector(20.00131000000000,24.93357000000000,0.00000000000000),App.Vector(-14.99869000000000,24.93357000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC").addGeometry(Part.LineSegment(App.Vector(-14.99869000000000,24.93357000000000,0.00000000000000),App.Vector(-14.99869000000000,-25.06643000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC").addGeometry(Part.LineSegment(App.Vector(20.00131000000000,-25.06643000000000,0.00000000000000),App.Vector(-14.99869000000000,-25.06643000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC").addGeometry(Part.LineSegment(App.Vector(20.00131000000000,24.93357000000000,0.00000000000000),App.Vector(20.00131000000000,-25.06643000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Pad","Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC")
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC")
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIjNGRGE7nFN9zF_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIjNGRGE7nFN9zF_0_FaysgqUtOVN4lno_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Plane", "plane_Sketch_FVwxqELF5ayXas4_1_JJC")
origin = App.Vector(2.50131000000000,3.00000000000000,-0.06643000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVwxqELF5ayXas4_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("Sketcher::SketchObject","Sketch_FVwxqELF5ayXas4_1_JJC")
App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVwxqELF5ayXas4_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,25.00000000000000,0.00000000000000),App.Vector(9.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC").addGeometry(Part.LineSegment(App.Vector(9.00000000000000,25.00000000000000,0.00000000000000),App.Vector(9.00000000000000,12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC").addGeometry(Part.LineSegment(App.Vector(9.00000000000000,12.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Pad","Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC")
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC")
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").Length = 24.0
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Plane", "plane_Sketch_FVwxqELF5ayXas4_1_JJG")
origin = App.Vector(2.50131000000000,3.00000000000000,-0.06643000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVwxqELF5ayXas4_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("Sketcher::SketchObject","Sketch_FVwxqELF5ayXas4_1_JJG")
App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVwxqELF5ayXas4_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG").addGeometry(Part.LineSegment(App.Vector(9.00000000000000,9.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,9.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,-9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG").addGeometry(Part.LineSegment(App.Vector(9.00000000000000,-9.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,-9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG").addGeometry(Part.LineSegment(App.Vector(9.00000000000000,9.00000000000000,0.00000000000000),App.Vector(9.00000000000000,-9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Pad","Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG")
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG")
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").Length = 24.0
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Plane", "plane_Sketch_FVwxqELF5ayXas4_1_JJK")
origin = App.Vector(2.50131000000000,3.00000000000000,-0.06643000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVwxqELF5ayXas4_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("Sketcher::SketchObject","Sketch_FVwxqELF5ayXas4_1_JJK")
App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVwxqELF5ayXas4_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(9.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK").addGeometry(Part.LineSegment(App.Vector(9.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(9.00000000000000,-12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK").addGeometry(Part.LineSegment(App.Vector(9.00000000000000,-12.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,-12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK").addGeometry(Part.LineSegment(App.Vector(-9.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-9.00000000000000,-12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Pad","Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK")
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK")
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").Length = 24.0
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVwxqELF5ayXas4_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVwxqELF5ayXas4_1_FWA6CSmTH2PPK8q_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Plane", "plane_Sketch_FTVochDcDCc1c4z_1_JNC")
origin = App.Vector(2.50131000000000,13.50000000000000,-25.06643000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTVochDcDCc1c4z_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("Sketcher::SketchObject","Sketch_FTVochDcDCc1c4z_1_JNC")
App.ActiveDocument.getObject("Sketch_FTVochDcDCc1c4z_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTVochDcDCc1c4z_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FTVochDcDCc1c4z_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTVochDcDCc1c4z_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,1.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTVochDcDCc1c4z_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTVochDcDCc1c4z_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Pocket","Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC")
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FTVochDcDCc1c4z_1_JNC")
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTVochDcDCc1c4z_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTVochDcDCc1c4z_1_Fi4FMPCE0tvE64Q_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Plane", "plane_Sketch_FFtyy9pgQQFXUrc_1_JRG")
origin = App.Vector(-6.49869000000000,15.00000000000000,18.43357000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFtyy9pgQQFXUrc_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("Sketcher::SketchObject","Sketch_FFtyy9pgQQFXUrc_1_JRG")
App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFtyy9pgQQFXUrc_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRG").addGeometry(Part.Circle(App.Vector(-8.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Pocket","Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG")
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRG")
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Plane", "plane_Sketch_FFtyy9pgQQFXUrc_1_JRC")
origin = App.Vector(-6.49869000000000,15.00000000000000,18.43357000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFtyy9pgQQFXUrc_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("Sketcher::SketchObject","Sketch_FFtyy9pgQQFXUrc_1_JRC")
App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFtyy9pgQQFXUrc_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRC").addGeometry(Part.Circle(App.Vector(-8.00000000000000,-36.65139000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Pocket","Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC")
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRC")
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFtyy9pgQQFXUrc_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFtyy9pgQQFXUrc_1_FzzdEMMZ1yn0RbM_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Plane", "plane_Sketch_FdnEd4piJIsxBOU_1_JVC")
origin = App.Vector(-2.99869000000000,27.00000000000000,18.43357000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdnEd4piJIsxBOU_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("Sketcher::SketchObject","Sketch_FdnEd4piJIsxBOU_1_JVC")
App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdnEd4piJIsxBOU_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC").addGeometry(Part.LineSegment(App.Vector(-7.50000000000000,6.50000000000000,0.00000000000000),App.Vector(-3.50000000000000,6.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC").addGeometry(Part.LineSegment(App.Vector(-3.50000000000000,6.50000000000000,0.00000000000000),App.Vector(-3.50000000000000,-6.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC").addGeometry(Part.LineSegment(App.Vector(-3.50000000000000,-6.50000000000000,0.00000000000000),App.Vector(-7.50000000000000,-6.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC").addGeometry(Part.LineSegment(App.Vector(-7.50000000000000,6.50000000000000,0.00000000000000),App.Vector(-7.50000000000000,-6.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIjNGRGE7nFN9zF_0").newObject("PartDesign::Pocket","Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC")
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC")
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdnEd4piJIsxBOU_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdnEd4piJIsxBOU_1_Fopg26SI2ZB4Pww_1_JVC").Offset = 0
App.ActiveDocument.recompute()

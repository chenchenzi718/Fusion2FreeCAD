import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00629865")
App.ActiveDocument.addObject("PartDesign::Body","Body_FGqnBx7jbDYTvAk_0")
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").Label = "Body_FGqnBx7jbDYTvAk_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Plane", "plane_Sketch_FGqnBx7jbDYTvAk_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGqnBx7jbDYTvAk_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("Sketcher::SketchObject","Sketch_FGqnBx7jbDYTvAk_0_JGG")
App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGqnBx7jbDYTvAk_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG").addGeometry(Part.LineSegment(App.Vector(-520.70000000000005,254.00000000000000,0.00000000000000),App.Vector(520.70000000000005,254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG").addGeometry(Part.LineSegment(App.Vector(520.70000000000005,254.00000000000000,0.00000000000000),App.Vector(520.70000000000005,-228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG").addGeometry(Part.LineSegment(App.Vector(-520.70000000000005,-228.59999999999999,0.00000000000000),App.Vector(520.70000000000005,-228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG").addGeometry(Part.LineSegment(App.Vector(-520.70000000000005,254.00000000000000,0.00000000000000),App.Vector(-520.70000000000005,-228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Pad","Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG")
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG")
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").Length = 1143.0
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").Type = 0
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FhoOPL6BCfZM5Hp_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Plane", "plane_Sketch_FGqnBx7jbDYTvAk_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGqnBx7jbDYTvAk_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("Sketcher::SketchObject","Sketch_FGqnBx7jbDYTvAk_0_JGC")
App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGqnBx7jbDYTvAk_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").addGeometry(Part.LineSegment(App.Vector(546.10000000000002,254.00000000000000,0.00000000000000),App.Vector(520.70000000000005,254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").addGeometry(Part.LineSegment(App.Vector(520.70000000000005,254.00000000000000,0.00000000000000),App.Vector(520.70000000000005,-228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-520.70000000000005,-228.59999999999999,0.00000000000000),App.Vector(520.70000000000005,-228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-520.70000000000005,254.00000000000000,0.00000000000000),App.Vector(-520.70000000000005,-228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-546.10000000000002,254.00000000000000,0.00000000000000),App.Vector(-520.70000000000005,254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-546.10000000000002,254.00000000000000,0.00000000000000),App.Vector(-546.10000000000002,-254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").addGeometry(Part.LineSegment(App.Vector(546.10000000000002,-254.00000000000000,0.00000000000000),App.Vector(-546.10000000000002,-254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").addGeometry(Part.LineSegment(App.Vector(546.10000000000002,254.00000000000000,0.00000000000000),App.Vector(546.10000000000002,-254.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Pad","Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC")
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").Profile = App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC")
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").Length = 22.860000000000003
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGqnBx7jbDYTvAk_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGqnBx7jbDYTvAk_0_FsAWte0tQnbmeus_1_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Plane", "plane_Sketch_F7SMf2P9qTnFGX9_1_JLC")
origin = App.Vector(0.00000000000000,-228.59999999999999,-582.92999999999995)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("Sketcher::SketchObject","Sketch_F7SMf2P9qTnFGX9_1_JLC")
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,-280.67000000000007,0.00000000000000),App.Vector(495.30000000000001,-280.67000000000007,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC").addGeometry(Part.LineSegment(App.Vector(495.30000000000001,-280.67000000000007,0.00000000000000),App.Vector(495.30000000000001,-458.47000000000014,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,-458.47000000000014,0.00000000000000),App.Vector(495.30000000000001,-458.47000000000014,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,-280.67000000000007,0.00000000000000),App.Vector(-495.30000000000001,-458.47000000000014,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Pad","Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").Length = 15.24
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Plane", "plane_Sketch_F7SMf2P9qTnFGX9_1_JLG")
origin = App.Vector(0.00000000000000,-228.59999999999999,-582.92999999999995)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("Sketcher::SketchObject","Sketch_F7SMf2P9qTnFGX9_1_JLG")
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,-64.77000000000011,0.00000000000000),App.Vector(495.30000000000001,-64.77000000000011,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG").addGeometry(Part.LineSegment(App.Vector(495.30000000000001,-64.77000000000011,0.00000000000000),App.Vector(495.30000000000001,-242.57000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,-242.57000000000005,0.00000000000000),App.Vector(495.30000000000001,-242.57000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,-64.77000000000011,0.00000000000000),App.Vector(-495.30000000000001,-242.57000000000005,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Pad","Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").Length = 15.24
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Plane", "plane_Sketch_F7SMf2P9qTnFGX9_1_JLK")
origin = App.Vector(0.00000000000000,-228.59999999999999,-582.92999999999995)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("Sketcher::SketchObject","Sketch_F7SMf2P9qTnFGX9_1_JLK")
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,151.12999999999994,0.00000000000000),App.Vector(495.30000000000001,151.12999999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK").addGeometry(Part.LineSegment(App.Vector(495.30000000000001,151.12999999999994,0.00000000000000),App.Vector(495.30000000000001,-26.67000000000008,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,-26.67000000000008,0.00000000000000),App.Vector(495.30000000000001,-26.67000000000008,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,151.12999999999994,0.00000000000000),App.Vector(-495.30000000000001,-26.67000000000008,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Pad","Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").Length = 15.24
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Plane", "plane_Sketch_F7SMf2P9qTnFGX9_1_JLO")
origin = App.Vector(0.00000000000000,-228.59999999999999,-582.92999999999995)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("Sketcher::SketchObject","Sketch_F7SMf2P9qTnFGX9_1_JLO")
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,521.96999999999991,0.00000000000000),App.Vector(-12.70000000000000,521.96999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO").addGeometry(Part.LineSegment(App.Vector(-12.70000000000000,521.96999999999991,0.00000000000000),App.Vector(-12.70000000000000,407.66999999999996,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,407.66999999999996,0.00000000000000),App.Vector(-12.70000000000000,407.66999999999996,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,521.96999999999991,0.00000000000000),App.Vector(-495.30000000000001,407.66999999999996,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Pad","Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").Length = 15.24
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Plane", "plane_Sketch_F7SMf2P9qTnFGX9_1_JLS")
origin = App.Vector(0.00000000000000,-228.59999999999999,-582.92999999999995)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("Sketcher::SketchObject","Sketch_F7SMf2P9qTnFGX9_1_JLS")
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLS"), [""])
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,521.96999999999991,0.00000000000000),App.Vector(495.30000000000001,521.96999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS").addGeometry(Part.LineSegment(App.Vector(495.30000000000001,521.96999999999991,0.00000000000000),App.Vector(495.30000000000001,407.66999999999996,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,407.66999999999996,0.00000000000000),App.Vector(495.30000000000001,407.66999999999996,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,521.96999999999991,0.00000000000000),App.Vector(12.70000000000000,407.66999999999996,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Pad","Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").Profile = App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").Length = 15.24
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").Type = 4
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Plane", "plane_Sketch_F7SMf2P9qTnFGX9_1_JLW")
origin = App.Vector(0.00000000000000,-228.59999999999999,-582.92999999999995)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("Sketcher::SketchObject","Sketch_F7SMf2P9qTnFGX9_1_JLW")
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7SMf2P9qTnFGX9_1_JLW"), [""])
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,189.22999999999996,0.00000000000000),App.Vector(495.30000000000001,189.22999999999996,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW").addGeometry(Part.LineSegment(App.Vector(495.30000000000001,189.22999999999996,0.00000000000000),App.Vector(495.30000000000001,367.02999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,367.02999999999997,0.00000000000000),App.Vector(495.30000000000001,367.02999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW").addGeometry(Part.LineSegment(App.Vector(-495.30000000000001,189.22999999999996,0.00000000000000),App.Vector(-495.30000000000001,367.02999999999997,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGqnBx7jbDYTvAk_0").newObject("PartDesign::Pad","Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").Profile = App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW")
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").Length = 15.24
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7SMf2P9qTnFGX9_1_JLW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").Type = 4
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7SMf2P9qTnFGX9_1_F2KlymvC1ku9Fyr_1_JLW").Offset = 0
App.ActiveDocument.recompute()

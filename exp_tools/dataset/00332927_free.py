import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00332927")
App.ActiveDocument.addObject("PartDesign::Body","Body_FMMs4ZpgDirTeZo_0")
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").Label = "Body_FMMs4ZpgDirTeZo_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Plane", "plane_Sketch_FMMs4ZpgDirTeZo_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMMs4ZpgDirTeZo_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("Sketcher::SketchObject","Sketch_FMMs4ZpgDirTeZo_0_JGC")
App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMMs4ZpgDirTeZo_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,9.52500000000000,0.00000000000000),App.Vector(-25.40000000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,9.52500000000000,0.00000000000000),App.Vector(-25.40000000000000,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-9.52500000000000,0.00000000000000),App.Vector(-25.40000000000000,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,9.52500000000000,0.00000000000000),App.Vector(25.40000000000000,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Pad","Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC")
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC")
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").Length = 1111.25
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMMs4ZpgDirTeZo_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMMs4ZpgDirTeZo_0_FtYa24UydzmTKWW_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Plane", "plane_Sketch_F2dbSPU4KJOTJO1_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("Sketcher::SketchObject","Sketch_F2dbSPU4KJOTJO1_1_JJC")
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-38.77126000000001,0.00000000000000,0.00000000000000),App.Vector(83.66431000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC").addGeometry(Part.LineSegment(App.Vector(83.66431000000000,0.00000000000000,0.00000000000000),App.Vector(83.66431000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-38.77126000000001,50.80000000000000,0.00000000000000),App.Vector(83.66431000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-38.77126000000001,0.00000000000000,0.00000000000000),App.Vector(-38.77126000000001,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Pocket","Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Plane", "plane_Sketch_F2dbSPU4KJOTJO1_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("Sketcher::SketchObject","Sketch_F2dbSPU4KJOTJO1_1_JJG")
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG").addGeometry(Part.LineSegment(App.Vector(-44.21286000000000,730.25000000000000,0.00000000000000),App.Vector(49.65441999999999,730.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG").addGeometry(Part.LineSegment(App.Vector(49.65441999999999,730.25000000000000,0.00000000000000),App.Vector(49.65441999999999,781.05000000000007,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG").addGeometry(Part.LineSegment(App.Vector(-44.21286000000000,781.05000000000007,0.00000000000000),App.Vector(49.65441999999999,781.05000000000007,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG").addGeometry(Part.LineSegment(App.Vector(-44.21286000000000,730.25000000000000,0.00000000000000),App.Vector(-44.21286000000000,781.05000000000007,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Pocket","Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Plane", "plane_Sketch_F2dbSPU4KJOTJO1_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("Sketcher::SketchObject","Sketch_F2dbSPU4KJOTJO1_1_JJK")
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK").addGeometry(Part.LineSegment(App.Vector(-210.36203000000000,1060.44999999999982,0.00000000000000),App.Vector(132.79838999999998,1060.44999999999982,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK").addGeometry(Part.LineSegment(App.Vector(132.79838999999998,1060.44999999999982,0.00000000000000),App.Vector(132.79838999999998,1111.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK").addGeometry(Part.LineSegment(App.Vector(-210.36203000000000,1111.25000000000000,0.00000000000000),App.Vector(132.79838999999998,1111.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK").addGeometry(Part.LineSegment(App.Vector(-210.36203000000000,1060.44999999999982,0.00000000000000),App.Vector(-210.36203000000000,1111.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Pocket","Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Plane", "plane_Sketch_F2dbSPU4KJOTJO1_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("Sketcher::SketchObject","Sketch_F2dbSPU4KJOTJO1_1_JJO")
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO").addGeometry(Part.LineSegment(App.Vector(-116.83130000000000,228.59999999999999,0.00000000000000),App.Vector(58.93262000000000,228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO").addGeometry(Part.LineSegment(App.Vector(58.93262000000000,228.59999999999999,0.00000000000000),App.Vector(58.93262000000000,279.39999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO").addGeometry(Part.LineSegment(App.Vector(-116.83130000000000,279.39999999999998,0.00000000000000),App.Vector(58.93262000000000,279.39999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO").addGeometry(Part.LineSegment(App.Vector(-116.83130000000000,228.59999999999999,0.00000000000000),App.Vector(-116.83130000000000,279.39999999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Pocket","Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").Type = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").Reversed = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Plane", "plane_Sketch_F2dbSPU4KJOTJO1_1_JJS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("Sketcher::SketchObject","Sketch_F2dbSPU4KJOTJO1_1_JJS")
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2dbSPU4KJOTJO1_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS").addGeometry(Part.LineSegment(App.Vector(-110.62789000000001,508.00000000000000,0.00000000000000),App.Vector(50.66137000000000,508.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS").addGeometry(Part.LineSegment(App.Vector(50.66137000000000,508.00000000000000,0.00000000000000),App.Vector(50.66137000000000,457.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS").addGeometry(Part.LineSegment(App.Vector(-110.62789000000001,457.19999999999999,0.00000000000000),App.Vector(50.66137000000000,457.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS").addGeometry(Part.LineSegment(App.Vector(-110.62789000000001,508.00000000000000,0.00000000000000),App.Vector(-110.62789000000001,457.19999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Pocket","Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS")
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2dbSPU4KJOTJO1_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").Type = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").Reversed = 1
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2dbSPU4KJOTJO1_1_Fvfy45scU7o7925_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Plane", "plane_Sketch_FQpHLrdhjftHe2C_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQpHLrdhjftHe2C_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("Sketcher::SketchObject","Sketch_FQpHLrdhjftHe2C_1_JNC")
App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQpHLrdhjftHe2C_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNC").addGeometry(Part.Circle(App.Vector(15.87500000000000,254.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Pocket","Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC")
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNC")
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Plane", "plane_Sketch_FQpHLrdhjftHe2C_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQpHLrdhjftHe2C_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("Sketcher::SketchObject","Sketch_FQpHLrdhjftHe2C_1_JNG")
App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQpHLrdhjftHe2C_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNG").addGeometry(Part.Circle(App.Vector(15.87500000000000,482.59999999999997,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMMs4ZpgDirTeZo_0").newObject("PartDesign::Pocket","Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG")
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNG")
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQpHLrdhjftHe2C_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").Type = 0
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQpHLrdhjftHe2C_1_F3XSHtWVrTEx6DV_1_JNG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00464154")
App.ActiveDocument.addObject("PartDesign::Body","Body_FCXklmrZLzzAcq5_0")
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").Label = "Body_FCXklmrZLzzAcq5_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FCXklmrZLzzAcq5_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCXklmrZLzzAcq5_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FCXklmrZLzzAcq5_0_JGC")
App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCXklmrZLzzAcq5_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(28.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC").addGeometry(Part.LineSegment(App.Vector(28.00000000000000,0.00000000000000,0.00000000000000),App.Vector(28.00000000000000,-13.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-13.50000000000000,0.00000000000000),App.Vector(28.00000000000000,-13.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-13.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pad","Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC")
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC")
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCXklmrZLzzAcq5_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCXklmrZLzzAcq5_0_FNh3uRMTpnyAac6_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FbFMxZp1r7mrN4G_1_JJC")
origin = App.Vector(14.00000000000000,-6.75000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbFMxZp1r7mrN4G_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FbFMxZp1r7mrN4G_1_JJC")
App.ActiveDocument.getObject("Sketch_FbFMxZp1r7mrN4G_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbFMxZp1r7mrN4G_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FbFMxZp1r7mrN4G_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbFMxZp1r7mrN4G_1_JJC").addGeometry(Part.Circle(App.Vector(-7.01411000000000,-0.05444000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbFMxZp1r7mrN4G_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbFMxZp1r7mrN4G_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pad","Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC")
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FbFMxZp1r7mrN4G_1_JJC")
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").Length = 9.5
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbFMxZp1r7mrN4G_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbFMxZp1r7mrN4G_1_FSa2m1sWdr4evb5_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FlBvhwJSDXLdREN_1_JNC")
origin = App.Vector(6.98589000000000,-6.80444000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlBvhwJSDXLdREN_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FlBvhwJSDXLdREN_1_JNC")
App.ActiveDocument.getObject("Sketch_FlBvhwJSDXLdREN_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlBvhwJSDXLdREN_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FlBvhwJSDXLdREN_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlBvhwJSDXLdREN_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlBvhwJSDXLdREN_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlBvhwJSDXLdREN_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pocket","Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC")
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FlBvhwJSDXLdREN_1_JNC")
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlBvhwJSDXLdREN_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlBvhwJSDXLdREN_1_FP9Rj1ERxgT6WHk_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FMaJ8IoL7ohBwOa_1_JRG")
origin = App.Vector(14.00000000000000,-6.75000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FMaJ8IoL7ohBwOa_1_JRG")
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG").addGeometry(Part.LineSegment(App.Vector(18.99499000000000,-1.91994000000000,0.00000000000000),App.Vector(14.00000000000000,-1.91994000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG").addGeometry(Part.LineSegment(App.Vector(14.00000000000000,-1.91994000000000,0.00000000000000),App.Vector(14.00000000000000,-0.91994000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG").addGeometry(Part.LineSegment(App.Vector(18.99499000000000,-0.91994000000000,0.00000000000000),App.Vector(14.00000000000000,-0.91994000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG").addGeometry(Part.LineSegment(App.Vector(18.99499000000000,-1.91994000000000,0.00000000000000),App.Vector(18.99499000000000,-0.91994000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pad","Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").Length = 1.0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FMaJ8IoL7ohBwOa_1_JRK")
origin = App.Vector(14.00000000000000,-6.75000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FMaJ8IoL7ohBwOa_1_JRK")
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK").addGeometry(Part.LineSegment(App.Vector(18.99499000000000,0.08006000000000,0.00000000000000),App.Vector(14.00000000000000,0.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK").addGeometry(Part.LineSegment(App.Vector(14.00000000000000,0.08006000000000,0.00000000000000),App.Vector(14.00000000000000,1.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK").addGeometry(Part.LineSegment(App.Vector(18.99499000000000,1.08006000000000,0.00000000000000),App.Vector(14.00000000000000,1.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK").addGeometry(Part.LineSegment(App.Vector(18.99499000000000,0.08006000000000,0.00000000000000),App.Vector(18.99499000000000,1.08006000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pad","Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").Length = 1.0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FMaJ8IoL7ohBwOa_1_JRO")
origin = App.Vector(14.00000000000000,-6.75000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FMaJ8IoL7ohBwOa_1_JRO")
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO").addGeometry(Part.LineSegment(App.Vector(18.99499000000000,2.08006000000000,0.00000000000000),App.Vector(14.00000000000000,2.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO").addGeometry(Part.LineSegment(App.Vector(14.00000000000000,2.08006000000000,0.00000000000000),App.Vector(14.00000000000000,3.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO").addGeometry(Part.LineSegment(App.Vector(18.99499000000000,3.08006000000000,0.00000000000000),App.Vector(14.00000000000000,3.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO").addGeometry(Part.LineSegment(App.Vector(18.99499000000000,2.08006000000000,0.00000000000000),App.Vector(18.99499000000000,3.08006000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pad","Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").Length = 1.0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FMaJ8IoL7ohBwOa_1_JRS")
origin = App.Vector(14.00000000000000,-6.75000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FMaJ8IoL7ohBwOa_1_JRS")
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRS"), [""])
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS").addGeometry(Part.LineSegment(App.Vector(11.99499000000000,-1.91994000000000,0.00000000000000),App.Vector(14.00000000000000,-1.91994000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS").addGeometry(Part.LineSegment(App.Vector(14.00000000000000,-1.91994000000000,0.00000000000000),App.Vector(14.00000000000000,-0.91994000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS").addGeometry(Part.LineSegment(App.Vector(11.99499000000000,-0.91994000000000,0.00000000000000),App.Vector(14.00000000000000,-0.91994000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS").addGeometry(Part.LineSegment(App.Vector(11.99499000000000,-1.91994000000000,0.00000000000000),App.Vector(11.99499000000000,-0.91994000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pad","Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").Profile = App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").Length = 1.0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").Type = 4
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FMaJ8IoL7ohBwOa_1_JRW")
origin = App.Vector(14.00000000000000,-6.75000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FMaJ8IoL7ohBwOa_1_JRW")
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRW"), [""])
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW").addGeometry(Part.LineSegment(App.Vector(11.99499000000000,0.08006000000000,0.00000000000000),App.Vector(14.00000000000000,0.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW").addGeometry(Part.LineSegment(App.Vector(14.00000000000000,0.08006000000000,0.00000000000000),App.Vector(14.00000000000000,1.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW").addGeometry(Part.LineSegment(App.Vector(11.99499000000000,1.08006000000000,0.00000000000000),App.Vector(14.00000000000000,1.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW").addGeometry(Part.LineSegment(App.Vector(11.99499000000000,0.08006000000000,0.00000000000000),App.Vector(11.99499000000000,1.08006000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pad","Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").Profile = App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").Length = 1.0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").Type = 4
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FMaJ8IoL7ohBwOa_1_JRa")
origin = App.Vector(14.00000000000000,-6.75000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FMaJ8IoL7ohBwOa_1_JRa")
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMaJ8IoL7ohBwOa_1_JRa"), [""])
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa").addGeometry(Part.LineSegment(App.Vector(11.99499000000000,2.08006000000000,0.00000000000000),App.Vector(14.00000000000000,2.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa").addGeometry(Part.LineSegment(App.Vector(14.00000000000000,2.08006000000000,0.00000000000000),App.Vector(14.00000000000000,3.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa").addGeometry(Part.LineSegment(App.Vector(11.99499000000000,3.08006000000000,0.00000000000000),App.Vector(14.00000000000000,3.08006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa").addGeometry(Part.LineSegment(App.Vector(11.99499000000000,2.08006000000000,0.00000000000000),App.Vector(11.99499000000000,3.08006000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pad","Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").Profile = App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa")
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").Length = 1.0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMaJ8IoL7ohBwOa_1_JRa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").Type = 4
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMaJ8IoL7ohBwOa_1_Fs6PgldC7fdg97T_1_JRa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Plane", "plane_Sketch_FQ8wEGP4ksRldeP_1_JVC")
origin = App.Vector(14.00000000000000,-6.75000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQ8wEGP4ksRldeP_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("Sketcher::SketchObject","Sketch_FQ8wEGP4ksRldeP_1_JVC")
App.ActiveDocument.getObject("Sketch_FQ8wEGP4ksRldeP_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQ8wEGP4ksRldeP_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FQ8wEGP4ksRldeP_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQ8wEGP4ksRldeP_1_JVC").addGeometry(Part.Circle(App.Vector(5.50000000000000,-0.25000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQ8wEGP4ksRldeP_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQ8wEGP4ksRldeP_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCXklmrZLzzAcq5_0").newObject("PartDesign::Pocket","Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC")
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FQ8wEGP4ksRldeP_1_JVC")
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQ8wEGP4ksRldeP_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQ8wEGP4ksRldeP_1_FQLEpu1iCX9qPSy_1_JVC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00263275")
App.ActiveDocument.addObject("PartDesign::Body","Body_FMJbAiTCoY0yzkn_0")
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").Label = "Body_FMJbAiTCoY0yzkn_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Plane", "plane_Sketch_FMJbAiTCoY0yzkn_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMJbAiTCoY0yzkn_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("Sketcher::SketchObject","Sketch_FMJbAiTCoY0yzkn_0_JGC")
App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMJbAiTCoY0yzkn_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,-50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,50.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(25.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Pad","Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC")
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC")
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMJbAiTCoY0yzkn_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMJbAiTCoY0yzkn_0_FAHmUtIZDpo9qE0_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Plane", "plane_Sketch_FZsGhE01a9YcM7A_1_JJC")
origin = App.Vector(-0.00000000000000,0.00000000000000,-47.50000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZsGhE01a9YcM7A_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("Sketcher::SketchObject","Sketch_FZsGhE01a9YcM7A_1_JJC")
App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZsGhE01a9YcM7A_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,2.50000000000000,0.00000000000000),App.Vector(25.00000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,2.50000000000000,0.00000000000000),App.Vector(25.00000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,4.50000000000000,0.00000000000000),App.Vector(25.00000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,2.50000000000000,0.00000000000000),App.Vector(-25.00000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Pad","Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC")
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC")
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZsGhE01a9YcM7A_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZsGhE01a9YcM7A_1_FQvnTxdvK6fxJCQ_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Plane", "plane_Sketch_FukiJgwtKtDPFpd_1_JNC")
origin = App.Vector(-0.00000000000000,2.50000000000000,-45.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FukiJgwtKtDPFpd_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("Sketcher::SketchObject","Sketch_FukiJgwtKtDPFpd_1_JNC")
App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FukiJgwtKtDPFpd_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-2.50000000000000,0.00000000000000),App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000),App.Vector(0.00000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-0.50000000000000,0.00000000000000),App.Vector(10.00000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-2.50000000000000,0.00000000000000),App.Vector(10.00000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Pad","Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC")
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC")
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").Length = 15.0
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FukiJgwtKtDPFpd_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FukiJgwtKtDPFpd_1_F6W1RRrgSRJEaZn_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Plane", "plane_Sketch_FVUI53addJ26DkJ_1_JRC")
origin = App.Vector(-0.00000000000000,2.50000000000000,-45.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVUI53addJ26DkJ_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("Sketcher::SketchObject","Sketch_FVUI53addJ26DkJ_1_JRC")
App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVUI53addJ26DkJ_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000),App.Vector(-10.00000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-2.50000000000000,0.00000000000000),App.Vector(-10.00000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-0.50000000000000,0.00000000000000),App.Vector(-10.00000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-2.50000000000000,0.00000000000000),App.Vector(0.00000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Pad","Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC")
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC")
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").Length = 15.0
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVUI53addJ26DkJ_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVUI53addJ26DkJ_1_FMDmPd4LBM78JrI_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Plane", "plane_Sketch_FrcLW2gL8HLobl9_1_JVC")
origin = App.Vector(-0.00000000000000,3.00000000000000,-51.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrcLW2gL8HLobl9_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("Sketcher::SketchObject","Sketch_FrcLW2gL8HLobl9_1_JVC")
App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrcLW2gL8HLobl9_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-8.50000000000000,0.00000000000000),App.Vector(-10.00000000000000,-8.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-8.50000000000000,0.00000000000000),App.Vector(-10.00000000000000,-6.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-6.50000000000001,0.00000000000000),App.Vector(10.00000000000000,-6.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-8.50000000000000,0.00000000000000),App.Vector(10.00000000000000,-6.50000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Pad","Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC")
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC")
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrcLW2gL8HLobl9_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrcLW2gL8HLobl9_1_F4A3isHyTyhzKiQ_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Plane", "plane_Sketch_FC90RBjZNrrvIMs_1_JZC")
origin = App.Vector(-0.00000000000000,-1.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FC90RBjZNrrvIMs_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("Sketcher::SketchObject","Sketch_FC90RBjZNrrvIMs_1_JZC")
App.ActiveDocument.getObject("Sketch_FC90RBjZNrrvIMs_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FC90RBjZNrrvIMs_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FC90RBjZNrrvIMs_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FC90RBjZNrrvIMs_1_JZC").addGeometry(Part.Circle(App.Vector(-6.31127000000000,0.08402000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.89336000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FC90RBjZNrrvIMs_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FC90RBjZNrrvIMs_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Pocket","Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC")
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FC90RBjZNrrvIMs_1_JZC")
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FC90RBjZNrrvIMs_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FC90RBjZNrrvIMs_1_FTKbZhCjs3RXeMq_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Plane", "plane_Sketch_FOZrXW5cDzazl3T_1_JdC")
origin = App.Vector(-0.00000000000000,-1.00000000000000,-60.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOZrXW5cDzazl3T_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("Sketcher::SketchObject","Sketch_FOZrXW5cDzazl3T_1_JdC")
App.ActiveDocument.getObject("Sketch_FOZrXW5cDzazl3T_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOZrXW5cDzazl3T_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FOZrXW5cDzazl3T_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOZrXW5cDzazl3T_1_JdC").addGeometry(Part.Circle(App.Vector(6.24409000000000,-0.20955000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.90716000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOZrXW5cDzazl3T_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOZrXW5cDzazl3T_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Pocket","Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC")
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FOZrXW5cDzazl3T_1_JdC")
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOZrXW5cDzazl3T_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOZrXW5cDzazl3T_1_FzDjFBDC0BvZoda_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Plane", "plane_Sketch_Fx4QrltheyahqcO_1_JhC")
origin = App.Vector(-0.00000000000000,0.00000000000000,3.50000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx4QrltheyahqcO_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("Sketcher::SketchObject","Sketch_Fx4QrltheyahqcO_1_JhC")
App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx4QrltheyahqcO_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,-13.50000000000000,0.00000000000000),App.Vector(-1.00000000000000,-13.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC").addGeometry(Part.LineSegment(App.Vector(-1.00000000000000,-13.50000000000000,0.00000000000000),App.Vector(-1.00000000000000,6.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,6.50000000000000,0.00000000000000),App.Vector(-1.00000000000000,6.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,-13.50000000000000,0.00000000000000),App.Vector(1.00000000000000,6.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMJbAiTCoY0yzkn_0").newObject("PartDesign::Pad","Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC")
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC")
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx4QrltheyahqcO_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx4QrltheyahqcO_1_FcGT5VwG3Ph5jBh_1_JhC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00573273")
App.ActiveDocument.addObject("PartDesign::Body","Body_FZBi1RbFseCvkD1_0")
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").Label = "Body_FZBi1RbFseCvkD1_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_FZBi1RbFseCvkD1_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZBi1RbFseCvkD1_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_FZBi1RbFseCvkD1_0_JGC")
App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZBi1RbFseCvkD1_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC").addGeometry(Part.LineSegment(App.Vector(-61.68750000000000,57.06250000000000,0.00000000000000),App.Vector(-11.68750000000000,57.06250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC").addGeometry(Part.LineSegment(App.Vector(-11.68750000000000,57.06250000000000,0.00000000000000),App.Vector(-11.68750000000000,17.06250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC").addGeometry(Part.LineSegment(App.Vector(-61.68750000000000,17.06250000000000,0.00000000000000),App.Vector(-11.68750000000000,17.06250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC").addGeometry(Part.LineSegment(App.Vector(-61.68750000000000,57.06250000000000,0.00000000000000),App.Vector(-61.68750000000000,17.06250000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pad","Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC")
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC")
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZBi1RbFseCvkD1_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZBi1RbFseCvkD1_0_F7vmsp26LrnBswg_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_FEMGlDQvfOnWpEv_1_JMC")
origin = App.Vector(-36.68750000000000,37.06250000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEMGlDQvfOnWpEv_1_JMC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_FEMGlDQvfOnWpEv_1_JMC")
App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEMGlDQvfOnWpEv_1_JMC"), [""])
App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,19.00000000000000,0.00000000000000),App.Vector(24.00000000000000,19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,19.00000000000000,0.00000000000000),App.Vector(24.00000000000000,-19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,-19.00000000000000,0.00000000000000),App.Vector(24.00000000000000,-19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,19.00000000000000,0.00000000000000),App.Vector(-24.00000000000000,-19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pocket","Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC")
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").Profile = App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC")
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").Length = 19.0
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEMGlDQvfOnWpEv_1_JMC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").Type = 4
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEMGlDQvfOnWpEv_1_FCX9DuSCM1Z1BBQ_1_JMC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_FpiqeStuLwkJCmh_1_JQC")
origin = App.Vector(-36.68750000000000,37.06250000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpiqeStuLwkJCmh_1_JQC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_FpiqeStuLwkJCmh_1_JQC")
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpiqeStuLwkJCmh_1_JQC"), [""])
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,19.00000000000000,0.00000000000000),App.Vector(19.00000000000000,19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,19.00000000000000,0.00000000000000),App.Vector(19.00000000000000,14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,14.00000000000000,0.00000000000000),App.Vector(19.00000000000000,14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,19.00000000000000,0.00000000000000),App.Vector(24.00000000000000,14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pad","Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC")
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").Profile = App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC")
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").Length = 19.0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").Type = 4
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_FpiqeStuLwkJCmh_1_JQG")
origin = App.Vector(-36.68750000000000,37.06250000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpiqeStuLwkJCmh_1_JQG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_FpiqeStuLwkJCmh_1_JQG")
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpiqeStuLwkJCmh_1_JQG"), [""])
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,-19.00000000000000,0.00000000000000),App.Vector(19.00000000000000,-19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,-19.00000000000000,0.00000000000000),App.Vector(19.00000000000000,-14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,-14.00000000000000,0.00000000000000),App.Vector(19.00000000000000,-14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,-19.00000000000000,0.00000000000000),App.Vector(24.00000000000000,-14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pad","Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG")
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").Profile = App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG")
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").Length = 19.0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").Type = 4
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_FpiqeStuLwkJCmh_1_JQO")
origin = App.Vector(-36.68750000000000,37.06250000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpiqeStuLwkJCmh_1_JQO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_FpiqeStuLwkJCmh_1_JQO")
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpiqeStuLwkJCmh_1_JQO"), [""])
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,-19.00000000000000,0.00000000000000),App.Vector(-19.00000000000000,-19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,-19.00000000000000,0.00000000000000),App.Vector(-19.00000000000000,-14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,-14.00000000000000,0.00000000000000),App.Vector(-19.00000000000000,-14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,-19.00000000000000,0.00000000000000),App.Vector(-24.00000000000000,-14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pad","Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO")
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").Profile = App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO")
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").Length = 19.0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").Type = 4
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_FpiqeStuLwkJCmh_1_JQK")
origin = App.Vector(-36.68750000000000,37.06250000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpiqeStuLwkJCmh_1_JQK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_FpiqeStuLwkJCmh_1_JQK")
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpiqeStuLwkJCmh_1_JQK"), [""])
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,19.00000000000000,0.00000000000000),App.Vector(-19.00000000000000,19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,19.00000000000000,0.00000000000000),App.Vector(-19.00000000000000,14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,14.00000000000000,0.00000000000000),App.Vector(-19.00000000000000,14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,19.00000000000000,0.00000000000000),App.Vector(-24.00000000000000,14.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pad","Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK")
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").Profile = App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK")
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").Length = 19.0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpiqeStuLwkJCmh_1_JQK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").Type = 4
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpiqeStuLwkJCmh_1_FZ6sUX6PeIqN9BJ_1_JQK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_Fng2T9wWdR5JepC_1_JUO")
origin = App.Vector(-36.68750000000000,37.06250000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fng2T9wWdR5JepC_1_JUO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_Fng2T9wWdR5JepC_1_JUO")
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fng2T9wWdR5JepC_1_JUO"), [""])
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUO").addGeometry(Part.Circle(App.Vector(21.50000000000000,16.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pocket","Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO")
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").Profile = App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUO")
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").Type = 4
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_Fng2T9wWdR5JepC_1_JUK")
origin = App.Vector(-36.68750000000000,37.06250000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fng2T9wWdR5JepC_1_JUK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_Fng2T9wWdR5JepC_1_JUK")
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fng2T9wWdR5JepC_1_JUK"), [""])
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUK").addGeometry(Part.Circle(App.Vector(21.50000000000000,-16.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pocket","Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK")
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").Profile = App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUK")
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").Type = 4
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_Fng2T9wWdR5JepC_1_JUG")
origin = App.Vector(-36.68750000000000,37.06250000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fng2T9wWdR5JepC_1_JUG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_Fng2T9wWdR5JepC_1_JUG")
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fng2T9wWdR5JepC_1_JUG"), [""])
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUG").addGeometry(Part.Circle(App.Vector(-21.50000000000000,-16.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pocket","Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG")
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").Profile = App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUG")
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").Type = 4
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Plane", "plane_Sketch_Fng2T9wWdR5JepC_1_JUC")
origin = App.Vector(-36.68750000000000,37.06250000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fng2T9wWdR5JepC_1_JUC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("Sketcher::SketchObject","Sketch_Fng2T9wWdR5JepC_1_JUC")
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fng2T9wWdR5JepC_1_JUC"), [""])
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUC").addGeometry(Part.Circle(App.Vector(-21.50000000000000,16.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FZBi1RbFseCvkD1_0").newObject("PartDesign::Pocket","Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC")
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").Profile = App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUC")
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fng2T9wWdR5JepC_1_JUC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").Type = 4
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fng2T9wWdR5JepC_1_FfgsnIBRCBAWHL3_1_JUC").Offset = 0
App.ActiveDocument.recompute()

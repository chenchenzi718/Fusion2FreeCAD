import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00708961")
App.ActiveDocument.addObject("PartDesign::Body","Body_F8Fxkmth5T5ihk9_0")
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").Label = "Body_F8Fxkmth5T5ihk9_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Plane", "plane_Sketch_F8Fxkmth5T5ihk9_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8Fxkmth5T5ihk9_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("Sketcher::SketchObject","Sketch_F8Fxkmth5T5ihk9_0_JGG")
App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8Fxkmth5T5ihk9_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-49.09435999999999,38.10000000000000,0.00000000000000),App.Vector(52.50564000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(52.50564000000000,38.10000000000000,0.00000000000000),App.Vector(52.50564000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-49.09435999999999,-38.10000000000000,0.00000000000000),App.Vector(52.50564000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-49.09435999999999,38.10000000000000,0.00000000000000),App.Vector(-49.09435999999999,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-58.61936000000000,47.62500000000000,0.00000000000000),App.Vector(62.03064000000000,47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(62.03064000000000,47.62500000000000,0.00000000000000),App.Vector(62.03064000000000,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-58.61936000000000,-47.62500000000000,0.00000000000000),App.Vector(62.03064000000000,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").addGeometry(Part.LineSegment(App.Vector(-58.61936000000000,47.62500000000000,0.00000000000000),App.Vector(-58.61936000000000,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Pad","Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG")
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG")
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").Length = 152.4
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8Fxkmth5T5ihk9_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8Fxkmth5T5ihk9_0_F3Qsn7b7VnfBTJf_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Plane", "plane_Sketch_FknH9wohTSzNuPE_1_JJC")
origin = App.Vector(-58.61936000000000,-76.20000000000000,-0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FknH9wohTSzNuPE_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("Sketcher::SketchObject","Sketch_FknH9wohTSzNuPE_1_JJC")
App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FknH9wohTSzNuPE_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,47.62500000000000,0.00000000000000),App.Vector(-85.72500000000001,47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC").addGeometry(Part.LineSegment(App.Vector(-85.72500000000001,47.62500000000000,0.00000000000000),App.Vector(-85.72500000000001,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,-47.62500000000000,0.00000000000000),App.Vector(-85.72500000000001,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,47.62500000000000,0.00000000000000),App.Vector(-76.20000000000000,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Pad","Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC")
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC")
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").Length = 120.65
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Plane", "plane_Sketch_FknH9wohTSzNuPE_1_JJG")
origin = App.Vector(-58.61936000000000,-76.20000000000000,-0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FknH9wohTSzNuPE_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("Sketcher::SketchObject","Sketch_FknH9wohTSzNuPE_1_JJG")
App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FknH9wohTSzNuPE_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG").addGeometry(Part.LineSegment(App.Vector(76.20000000000000,47.62500000000000,0.00000000000000),App.Vector(85.72500000000001,47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG").addGeometry(Part.LineSegment(App.Vector(85.72500000000001,47.62500000000000,0.00000000000000),App.Vector(85.72500000000001,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG").addGeometry(Part.LineSegment(App.Vector(76.20000000000000,-47.62500000000000,0.00000000000000),App.Vector(85.72500000000001,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG").addGeometry(Part.LineSegment(App.Vector(76.20000000000000,47.62500000000000,0.00000000000000),App.Vector(76.20000000000000,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Pad","Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG")
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG")
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").Length = 120.65
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FknH9wohTSzNuPE_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FknH9wohTSzNuPE_1_F5RZk4BsY0qa7Ri_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Plane", "plane_Sketch_FuceE24oSlslsxd_1_JNC")
origin = App.Vector(1.70564000000000,-119.69750000000001,47.62500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuceE24oSlslsxd_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("Sketcher::SketchObject","Sketch_FuceE24oSlslsxd_1_JNC")
App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuceE24oSlslsxd_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,43.49750000000000,0.00000000000000),App.Vector(60.32500000000000,43.49750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC").addGeometry(Part.LineSegment(App.Vector(60.32500000000000,43.49750000000000,0.00000000000000),App.Vector(60.32500000000000,42.22750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,42.22750000000000,0.00000000000000),App.Vector(60.32500000000000,42.22750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,43.49750000000000,0.00000000000000),App.Vector(-60.32500000000000,42.22750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Pocket","Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC")
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC")
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").Length = 9.525
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuceE24oSlslsxd_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuceE24oSlslsxd_1_FQVWyuw1rZmKAtu_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Plane", "plane_Sketch_F5SNpukVHajObPV_1_JRC")
origin = App.Vector(1.70564000000000,-33.33750000000000,47.62500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5SNpukVHajObPV_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("Sketcher::SketchObject","Sketch_F5SNpukVHajObPV_1_JRC")
App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5SNpukVHajObPV_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5.70564000000000,-1.58750000000000,0.00000000000000),App.Vector(2.29436000000000,-1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC").addGeometry(Part.LineSegment(App.Vector(2.29436000000000,-1.58750000000000,0.00000000000000),App.Vector(2.29436000000000,-16.58750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5.70564000000000,-16.58750000000000,0.00000000000000),App.Vector(2.29436000000000,-16.58750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5.70564000000000,-1.58750000000000,0.00000000000000),App.Vector(-5.70564000000000,-16.58750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Pocket","Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC")
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC")
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Plane", "plane_Sketch_F5SNpukVHajObPV_1_JRG")
origin = App.Vector(1.70564000000000,-33.33750000000000,47.62500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5SNpukVHajObPV_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("Sketcher::SketchObject","Sketch_F5SNpukVHajObPV_1_JRG")
App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5SNpukVHajObPV_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRG").addGeometry(Part.Circle(App.Vector(-31.10564000000000,-9.08750000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Pocket","Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG")
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRG")
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Plane", "plane_Sketch_F5SNpukVHajObPV_1_JRK")
origin = App.Vector(1.70564000000000,-33.33750000000000,47.62500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5SNpukVHajObPV_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("Sketcher::SketchObject","Sketch_F5SNpukVHajObPV_1_JRK")
App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5SNpukVHajObPV_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRK").addGeometry(Part.Circle(App.Vector(27.69436000000000,-9.08750000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Pocket","Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK")
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRK")
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5SNpukVHajObPV_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5SNpukVHajObPV_1_F8zowhA9p1jgdQ9_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Plane", "plane_Sketch_F4IpeBJOtEXUjpn_1_JVC")
origin = App.Vector(-58.61936000000000,-76.20000000000000,-0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4IpeBJOtEXUjpn_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("Sketcher::SketchObject","Sketch_F4IpeBJOtEXUjpn_1_JVC")
App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4IpeBJOtEXUjpn_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC").addGeometry(Part.LineSegment(App.Vector(1.26999999999999,38.10000000000000,0.00000000000000),App.Vector(76.20000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC").addGeometry(Part.LineSegment(App.Vector(76.20000000000000,38.10000000000000,0.00000000000000),App.Vector(76.20000000000000,39.37000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC").addGeometry(Part.LineSegment(App.Vector(1.26999999999999,39.37000000000000,0.00000000000000),App.Vector(76.20000000000000,39.37000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC").addGeometry(Part.LineSegment(App.Vector(1.26999999999999,38.10000000000000,0.00000000000000),App.Vector(1.26999999999999,39.37000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F8Fxkmth5T5ihk9_0").newObject("PartDesign::Pocket","Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC")
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC")
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").Length = 179.07
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4IpeBJOtEXUjpn_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4IpeBJOtEXUjpn_1_FZIzZ2VbySe6Hiw_1_JVC").Offset = 0
App.ActiveDocument.recompute()

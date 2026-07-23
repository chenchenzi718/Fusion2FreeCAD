import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00695007")
App.ActiveDocument.addObject("PartDesign::Body","Body_FD7oAklnA9Xndx8_0")
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").Label = "Body_FD7oAklnA9Xndx8_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Plane", "plane_Sketch_FD7oAklnA9Xndx8_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FD7oAklnA9Xndx8_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("Sketcher::SketchObject","Sketch_FD7oAklnA9Xndx8_0_JGC")
App.ActiveDocument.getObject("Sketch_FD7oAklnA9Xndx8_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FD7oAklnA9Xndx8_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FD7oAklnA9Xndx8_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FD7oAklnA9Xndx8_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.62718000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FD7oAklnA9Xndx8_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FD7oAklnA9Xndx8_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Pad","Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC")
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FD7oAklnA9Xndx8_0_JGC")
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").Length = 163.99999999999997
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FD7oAklnA9Xndx8_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FD7oAklnA9Xndx8_0_Fezqg5OtnjStmDm_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Plane", "plane_Sketch_FTvbkQjajmoFmXA_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTvbkQjajmoFmXA_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("Sketcher::SketchObject","Sketch_FTvbkQjajmoFmXA_1_JJC")
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTvbkQjajmoFmXA_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJC").addGeometry(Part.Circle(App.Vector(-8.85000000000000,14.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.18904000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Pad","Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC")
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJC")
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").Length = 137.0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Plane", "plane_Sketch_FTvbkQjajmoFmXA_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTvbkQjajmoFmXA_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("Sketcher::SketchObject","Sketch_FTvbkQjajmoFmXA_1_JJG")
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTvbkQjajmoFmXA_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJG").addGeometry(Part.Circle(App.Vector(7.95000000000000,13.20000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.05941000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Pad","Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG")
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJG")
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").Length = 137.0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Plane", "plane_Sketch_FTvbkQjajmoFmXA_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTvbkQjajmoFmXA_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("Sketcher::SketchObject","Sketch_FTvbkQjajmoFmXA_1_JJK")
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTvbkQjajmoFmXA_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJK").addGeometry(Part.Circle(App.Vector(9.75000000000000,-4.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.26380000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Pad","Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK")
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJK")
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").Length = 137.0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Plane", "plane_Sketch_FTvbkQjajmoFmXA_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTvbkQjajmoFmXA_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("Sketcher::SketchObject","Sketch_FTvbkQjajmoFmXA_1_JJO")
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTvbkQjajmoFmXA_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJO").addGeometry(Part.Circle(App.Vector(-4.95000000000000,-7.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.08423000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Pad","Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO")
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJO")
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").Length = 137.0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTvbkQjajmoFmXA_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTvbkQjajmoFmXA_1_FAk9LB8IKyHuwcS_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Plane", "plane_Sketch_FJQ7BHHE18jeUNy_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,164.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJQ7BHHE18jeUNy_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("Sketcher::SketchObject","Sketch_FJQ7BHHE18jeUNy_1_JNC")
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJQ7BHHE18jeUNy_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNC").addGeometry(Part.Circle(App.Vector(-9.45472000000000,15.17511000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.10155000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Pad","Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC")
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNC")
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").Length = 152.0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Plane", "plane_Sketch_FJQ7BHHE18jeUNy_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,164.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJQ7BHHE18jeUNy_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("Sketcher::SketchObject","Sketch_FJQ7BHHE18jeUNy_1_JNG")
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJQ7BHHE18jeUNy_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNG").addGeometry(Part.Circle(App.Vector(6.63290000000000,9.54445000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.87263000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Pad","Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG")
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNG")
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").Length = 152.0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Plane", "plane_Sketch_FJQ7BHHE18jeUNy_1_JNK")
origin = App.Vector(0.00000000000000,0.00000000000000,164.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJQ7BHHE18jeUNy_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("Sketcher::SketchObject","Sketch_FJQ7BHHE18jeUNy_1_JNK")
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJQ7BHHE18jeUNy_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNK").addGeometry(Part.Circle(App.Vector(5.82851000000000,-11.77165000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.28999000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Pad","Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK")
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNK")
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").Length = 152.0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Plane", "plane_Sketch_FJQ7BHHE18jeUNy_1_JNO")
origin = App.Vector(0.00000000000000,0.00000000000000,164.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJQ7BHHE18jeUNy_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("Sketcher::SketchObject","Sketch_FJQ7BHHE18jeUNy_1_JNO")
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJQ7BHHE18jeUNy_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNO").addGeometry(Part.Circle(App.Vector(-15.08540000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.78528000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FD7oAklnA9Xndx8_0").newObject("PartDesign::Pad","Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO")
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNO")
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").Length = 152.0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJQ7BHHE18jeUNy_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJQ7BHHE18jeUNy_1_FolG9PpdplcSoxs_1_JNO").Offset = 0
App.ActiveDocument.recompute()

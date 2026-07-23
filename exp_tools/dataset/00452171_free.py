import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00452171")
App.ActiveDocument.addObject("PartDesign::Body","Body_FYCdQzMioaa2xtT_0")
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").Label = "Body_FYCdQzMioaa2xtT_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Plane", "plane_Sketch_FYCdQzMioaa2xtT_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYCdQzMioaa2xtT_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("Sketcher::SketchObject","Sketch_FYCdQzMioaa2xtT_0_JGC")
App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYCdQzMioaa2xtT_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC").addGeometry(Part.LineSegment(App.Vector(-37.45000000000000,12.45368000000000,0.00000000000000),App.Vector(37.55000000000000,12.45368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC").addGeometry(Part.LineSegment(App.Vector(37.55000000000000,12.45368000000000,0.00000000000000),App.Vector(37.55000000000000,-12.54632000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC").addGeometry(Part.LineSegment(App.Vector(-37.45000000000000,-12.54632000000000,0.00000000000000),App.Vector(37.55000000000000,-12.54632000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC").addGeometry(Part.LineSegment(App.Vector(-37.45000000000000,12.45368000000000,0.00000000000000),App.Vector(-37.45000000000000,-12.54632000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Pad","Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC")
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC")
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYCdQzMioaa2xtT_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYCdQzMioaa2xtT_0_FPL0gPQvVuoPuwV_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Plane", "plane_Sketch_FemUeNrNNQ7H4LR_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FemUeNrNNQ7H4LR_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("Sketcher::SketchObject","Sketch_FemUeNrNNQ7H4LR_1_JJC")
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FemUeNrNNQ7H4LR_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJC").addGeometry(Part.Circle(App.Vector(-24.99943000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Pad","Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC")
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJC")
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Plane", "plane_Sketch_FemUeNrNNQ7H4LR_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FemUeNrNNQ7H4LR_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("Sketcher::SketchObject","Sketch_FemUeNrNNQ7H4LR_1_JJG")
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FemUeNrNNQ7H4LR_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJG").addGeometry(Part.Circle(App.Vector(-8.30582000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Pad","Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG")
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJG")
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").Length = 5.0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Plane", "plane_Sketch_FemUeNrNNQ7H4LR_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FemUeNrNNQ7H4LR_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("Sketcher::SketchObject","Sketch_FemUeNrNNQ7H4LR_1_JJK")
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FemUeNrNNQ7H4LR_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJK").addGeometry(Part.Circle(App.Vector(8.38825000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Pad","Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK")
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJK")
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").Length = 5.0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Plane", "plane_Sketch_FemUeNrNNQ7H4LR_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FemUeNrNNQ7H4LR_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("Sketcher::SketchObject","Sketch_FemUeNrNNQ7H4LR_1_JJO")
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FemUeNrNNQ7H4LR_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJO").addGeometry(Part.Circle(App.Vector(25.08342000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Pad","Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO")
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJO")
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").Length = 5.0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FemUeNrNNQ7H4LR_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FemUeNrNNQ7H4LR_1_FJF0W5Zs7SsTOtr_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Plane", "plane_Sketch_FjoKpL0GscVKvv1_1_JPO")
origin = App.Vector(-24.99943000000000,0.00000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjoKpL0GscVKvv1_1_JPO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("Sketcher::SketchObject","Sketch_FjoKpL0GscVKvv1_1_JPO")
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjoKpL0GscVKvv1_1_JPO"), [""])
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPO").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Pocket","Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO")
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").Profile = App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPO")
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").Length = 3.0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").Type = 4
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Plane", "plane_Sketch_FjoKpL0GscVKvv1_1_JPC")
origin = App.Vector(-24.99943000000000,0.00000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjoKpL0GscVKvv1_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("Sketcher::SketchObject","Sketch_FjoKpL0GscVKvv1_1_JPC")
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjoKpL0GscVKvv1_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPC").addGeometry(Part.Circle(App.Vector(16.69457000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Pocket","Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC")
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPC")
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Plane", "plane_Sketch_FjoKpL0GscVKvv1_1_JPG")
origin = App.Vector(-24.99943000000000,0.00000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjoKpL0GscVKvv1_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("Sketcher::SketchObject","Sketch_FjoKpL0GscVKvv1_1_JPG")
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjoKpL0GscVKvv1_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPG").addGeometry(Part.Circle(App.Vector(33.40599000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Pocket","Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG")
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPG")
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").Length = 3.0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Plane", "plane_Sketch_FjoKpL0GscVKvv1_1_JPK")
origin = App.Vector(-24.99943000000000,0.00000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjoKpL0GscVKvv1_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("Sketcher::SketchObject","Sketch_FjoKpL0GscVKvv1_1_JPK")
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjoKpL0GscVKvv1_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPK").addGeometry(Part.Circle(App.Vector(50.10122999999999,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYCdQzMioaa2xtT_0").newObject("PartDesign::Pocket","Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK")
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPK")
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").Length = 3.0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjoKpL0GscVKvv1_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjoKpL0GscVKvv1_1_FcLD9ag2F1WCGOY_1_JPK").Offset = 0
App.ActiveDocument.recompute()

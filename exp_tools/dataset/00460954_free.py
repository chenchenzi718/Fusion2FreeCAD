import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00460954")
App.ActiveDocument.addObject("PartDesign::Body","Body_FXHGHjKn395nVft_0")
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").Label = "Body_FXHGHjKn395nVft_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Plane", "plane_Sketch_FXHGHjKn395nVft_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXHGHjKn395nVft_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("Sketcher::SketchObject","Sketch_FXHGHjKn395nVft_0_JGC")
App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXHGHjKn395nVft_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC").addGeometry(Part.LineSegment(App.Vector(-31.61358000000000,85.61298000000001,0.00000000000000),App.Vector(108.38642000000000,85.61298000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC").addGeometry(Part.LineSegment(App.Vector(108.38642000000000,85.61298000000001,0.00000000000000),App.Vector(108.38642000000000,-14.38702000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC").addGeometry(Part.LineSegment(App.Vector(-31.61358000000000,-14.38702000000000,0.00000000000000),App.Vector(108.38642000000000,-14.38702000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC").addGeometry(Part.LineSegment(App.Vector(-31.61358000000000,85.61298000000001,0.00000000000000),App.Vector(-31.61358000000000,-14.38702000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Pad","Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC")
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC")
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").Length = 80.0
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXHGHjKn395nVft_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXHGHjKn395nVft_0_FHNxOBdLbjcXMAE_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Plane", "plane_Sketch_F4UdwJVjJDe0fZ8_1_JJC")
origin = App.Vector(38.38641999999999,49.61502000000000,80.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("Sketcher::SketchObject","Sketch_F4UdwJVjJDe0fZ8_1_JJC")
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-59.87757000000000,25.90582000000000,0.00000000000000),App.Vector(-9.87757000000000,25.90582000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-9.87757000000000,25.90582000000000,0.00000000000000),App.Vector(-9.87757000000000,-9.09418000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-59.87757000000000,-9.09418000000000,0.00000000000000),App.Vector(-9.87757000000000,-9.09418000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-59.87757000000000,25.90582000000000,0.00000000000000),App.Vector(-59.87757000000000,-9.09418000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Pocket","Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").Profile = App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").Length = 50.0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Plane", "plane_Sketch_F4UdwJVjJDe0fZ8_1_JJG")
origin = App.Vector(38.38641999999999,49.61502000000000,80.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("Sketcher::SketchObject","Sketch_F4UdwJVjJDe0fZ8_1_JJG")
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJG").addGeometry(Part.Circle(App.Vector(13.23061000000000,9.03836000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Pocket","Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").Profile = App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJG")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").Length = 50.0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Plane", "plane_Sketch_F4UdwJVjJDe0fZ8_1_JJK")
origin = App.Vector(38.38641999999999,49.61502000000000,80.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("Sketcher::SketchObject","Sketch_F4UdwJVjJDe0fZ8_1_JJK")
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJK").addGeometry(Part.Circle(App.Vector(45.74893000000000,9.03836000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Pocket","Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").Profile = App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJK")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").Length = 50.0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Plane", "plane_Sketch_F4UdwJVjJDe0fZ8_1_JJO")
origin = App.Vector(38.38641999999999,49.61502000000000,80.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("Sketcher::SketchObject","Sketch_F4UdwJVjJDe0fZ8_1_JJO")
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJO").addGeometry(Part.Circle(App.Vector(-45.82265000000000,-22.95966000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Pocket","Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").Profile = App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJO")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").Length = 50.0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Plane", "plane_Sketch_F4UdwJVjJDe0fZ8_1_JJS")
origin = App.Vector(38.38641999999999,49.61502000000000,80.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("Sketcher::SketchObject","Sketch_F4UdwJVjJDe0fZ8_1_JJS")
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJS").addGeometry(Part.Circle(App.Vector(-21.36887000000000,-22.95966000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Pocket","Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").Profile = App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJS")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").Length = 50.0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Plane", "plane_Sketch_F4UdwJVjJDe0fZ8_1_JJW")
origin = App.Vector(38.38641999999999,49.61502000000000,80.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("Sketcher::SketchObject","Sketch_F4UdwJVjJDe0fZ8_1_JJW")
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW").addGeometry(Part.LineSegment(App.Vector(-6.80066999999999,-17.49659000000000,0.00000000000000),App.Vector(58.23597000000000,-17.49659000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW").addGeometry(Part.LineSegment(App.Vector(58.23597000000000,-17.49659000000000,0.00000000000000),App.Vector(58.23597000000000,-29.20318000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW").addGeometry(Part.LineSegment(App.Vector(-6.80066999999999,-29.20318000000000,0.00000000000000),App.Vector(58.23597000000000,-29.20318000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW").addGeometry(Part.LineSegment(App.Vector(-6.80066999999999,-17.49659000000000,0.00000000000000),App.Vector(-6.80066999999999,-29.20318000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Pocket","Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").Profile = App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").Length = 50.0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Plane", "plane_Sketch_F4UdwJVjJDe0fZ8_1_JJa")
origin = App.Vector(38.38641999999999,49.61502000000000,80.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("Sketcher::SketchObject","Sketch_F4UdwJVjJDe0fZ8_1_JJa")
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4UdwJVjJDe0fZ8_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa").addGeometry(Part.LineSegment(App.Vector(-70.00000000000000,-35.99797000000000,0.00000000000000),App.Vector(70.00000000000000,-35.99797000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,-35.99797000000000,0.00000000000000),App.Vector(70.00000000000000,-36.80875000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa").addGeometry(Part.LineSegment(App.Vector(-70.00000000000000,-36.80875000000000,0.00000000000000),App.Vector(70.00000000000000,-36.80875000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa").addGeometry(Part.LineSegment(App.Vector(-70.00000000000000,-35.99797000000000,0.00000000000000),App.Vector(-70.00000000000000,-36.80875000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXHGHjKn395nVft_0").newObject("PartDesign::Pocket","Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").Profile = App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa")
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").Length = 50.0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4UdwJVjJDe0fZ8_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4UdwJVjJDe0fZ8_1_FFwIHUrx2HBkHwV_2_JJa").Offset = 0
App.ActiveDocument.recompute()

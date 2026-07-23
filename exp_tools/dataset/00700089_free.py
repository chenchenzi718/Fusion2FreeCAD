import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00700089")
App.ActiveDocument.addObject("PartDesign::Body","Body_FIOSIDFivz5a72u_0")
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").Label = "Body_FIOSIDFivz5a72u_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Plane", "plane_Sketch_FIOSIDFivz5a72u_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIOSIDFivz5a72u_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("Sketcher::SketchObject","Sketch_FIOSIDFivz5a72u_0_JGK")
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIOSIDFivz5a72u_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,500.00000000000000,0.00000000000000),App.Vector(250.00000000000000,500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK").addGeometry(Part.LineSegment(App.Vector(250.00000000000000,500.00000000000000,0.00000000000000),App.Vector(250.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,250.00000000000000,0.00000000000000),App.Vector(250.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,500.00000000000000,0.00000000000000),App.Vector(0.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Pad","Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK")
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK")
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").Length = 600.0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FMVBREY6hbLY39F_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Plane", "plane_Sketch_FIOSIDFivz5a72u_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIOSIDFivz5a72u_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("Sketcher::SketchObject","Sketch_FIOSIDFivz5a72u_0_JGO")
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIOSIDFivz5a72u_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO").addGeometry(Part.LineSegment(App.Vector(500.00000000000000,500.00000000000000,0.00000000000000),App.Vector(250.00000000000000,500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO").addGeometry(Part.LineSegment(App.Vector(250.00000000000000,500.00000000000000,0.00000000000000),App.Vector(250.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO").addGeometry(Part.LineSegment(App.Vector(500.00000000000000,250.00000000000000,0.00000000000000),App.Vector(250.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO").addGeometry(Part.LineSegment(App.Vector(500.00000000000000,500.00000000000000,0.00000000000000),App.Vector(500.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Pad","Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO")
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").Profile = App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO")
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").Length = 500.0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FzNP5RAPHsG3h7H_1_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Plane", "plane_Sketch_FIOSIDFivz5a72u_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIOSIDFivz5a72u_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("Sketcher::SketchObject","Sketch_FIOSIDFivz5a72u_0_JGG")
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIOSIDFivz5a72u_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG").addGeometry(Part.LineSegment(App.Vector(500.00000000000000,0.00000000000000,0.00000000000000),App.Vector(250.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG").addGeometry(Part.LineSegment(App.Vector(250.00000000000000,0.00000000000000,0.00000000000000),App.Vector(250.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG").addGeometry(Part.LineSegment(App.Vector(500.00000000000000,250.00000000000000,0.00000000000000),App.Vector(250.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG").addGeometry(Part.LineSegment(App.Vector(500.00000000000000,0.00000000000000,0.00000000000000),App.Vector(500.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Pad","Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG")
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").Profile = App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG")
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").Length = 400.0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_FgV0nvwPHFABIqT_1_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Plane", "plane_Sketch_FIOSIDFivz5a72u_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIOSIDFivz5a72u_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("Sketcher::SketchObject","Sketch_FIOSIDFivz5a72u_0_JGC")
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIOSIDFivz5a72u_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(250.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC").addGeometry(Part.LineSegment(App.Vector(250.00000000000000,0.00000000000000,0.00000000000000),App.Vector(250.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,250.00000000000000,0.00000000000000),App.Vector(250.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Pad","Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC")
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").Profile = App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC")
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").Length = 300.0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIOSIDFivz5a72u_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIOSIDFivz5a72u_0_F9Cm7rQG70gq233_1_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Plane", "plane_Sketch_FnM5piejTBSgDiR_1_JPC")
origin = App.Vector(125.00000000000000,375.00000000000000,600.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnM5piejTBSgDiR_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("Sketcher::SketchObject","Sketch_FnM5piejTBSgDiR_1_JPC")
App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnM5piejTBSgDiR_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC").addGeometry(Part.LineSegment(App.Vector(-100.00000000000000,-99.99999999999997,0.00000000000000),App.Vector(100.00000000000000,-99.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,-99.99999999999997,0.00000000000000),App.Vector(100.00000000000000,99.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC").addGeometry(Part.LineSegment(App.Vector(-100.00000000000000,99.99999999999997,0.00000000000000),App.Vector(100.00000000000000,99.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC").addGeometry(Part.LineSegment(App.Vector(-100.00000000000000,-99.99999999999997,0.00000000000000),App.Vector(-100.00000000000000,99.99999999999997,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Pocket","Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC")
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC")
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").Length = 575.0000000000001
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnM5piejTBSgDiR_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnM5piejTBSgDiR_1_F6hzOW83gyd5Vm5_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Plane", "plane_Sketch_FQxxDwWZYL1Wcvs_1_JTC")
origin = App.Vector(375.00000000000000,375.00000000000000,500.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQxxDwWZYL1Wcvs_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("Sketcher::SketchObject","Sketch_FQxxDwWZYL1Wcvs_1_JTC")
App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQxxDwWZYL1Wcvs_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC").addGeometry(Part.LineSegment(App.Vector(-99.99999999999997,-99.99999999999997,0.00000000000000),App.Vector(99.99999999999997,-99.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC").addGeometry(Part.LineSegment(App.Vector(99.99999999999997,-99.99999999999997,0.00000000000000),App.Vector(99.99999999999997,99.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC").addGeometry(Part.LineSegment(App.Vector(-99.99999999999997,99.99999999999997,0.00000000000000),App.Vector(99.99999999999997,99.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC").addGeometry(Part.LineSegment(App.Vector(-99.99999999999997,-99.99999999999997,0.00000000000000),App.Vector(-99.99999999999997,99.99999999999997,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Pocket","Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC")
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC")
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").Length = 475.00000000000006
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQxxDwWZYL1Wcvs_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQxxDwWZYL1Wcvs_1_FBcKVpzUP99gt3F_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Plane", "plane_Sketch_FR2G9IeL5LdjHpc_1_JXC")
origin = App.Vector(375.00000000000000,125.00000000000000,400.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR2G9IeL5LdjHpc_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("Sketcher::SketchObject","Sketch_FR2G9IeL5LdjHpc_1_JXC")
App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR2G9IeL5LdjHpc_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC").addGeometry(Part.LineSegment(App.Vector(99.99999999999997,100.00000000000000,0.00000000000000),App.Vector(-99.99999999999997,100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC").addGeometry(Part.LineSegment(App.Vector(-99.99999999999997,100.00000000000000,0.00000000000000),App.Vector(-99.99999999999997,-100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC").addGeometry(Part.LineSegment(App.Vector(99.99999999999997,-100.00000000000000,0.00000000000000),App.Vector(-99.99999999999997,-100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC").addGeometry(Part.LineSegment(App.Vector(99.99999999999997,100.00000000000000,0.00000000000000),App.Vector(99.99999999999997,-100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Pocket","Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC")
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC")
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").Length = 375.0
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR2G9IeL5LdjHpc_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR2G9IeL5LdjHpc_1_Fc5KDsQOJ535ej7_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Plane", "plane_Sketch_FcY2X8TpbfBIbGB_1_JbC")
origin = App.Vector(125.00000000000000,125.00000000000000,300.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcY2X8TpbfBIbGB_1_JbC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("Sketcher::SketchObject","Sketch_FcY2X8TpbfBIbGB_1_JbC")
App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcY2X8TpbfBIbGB_1_JbC"), [""])
App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,-100.00000000000000,0.00000000000000),App.Vector(100.00000000000000,100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,100.00000000000000,0.00000000000000),App.Vector(-100.00000000000000,100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC").addGeometry(Part.LineSegment(App.Vector(-100.00000000000000,-100.00000000000000,0.00000000000000),App.Vector(-100.00000000000000,100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC").addGeometry(Part.LineSegment(App.Vector(100.00000000000000,-100.00000000000000,0.00000000000000),App.Vector(-100.00000000000000,-100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIOSIDFivz5a72u_0").newObject("PartDesign::Pocket","Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC")
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").Profile = App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC")
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").Length = 275.0
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcY2X8TpbfBIbGB_1_JbC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").Type = 4
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcY2X8TpbfBIbGB_1_Fy4HNY2EhGpVeeU_1_JbC").Offset = 0
App.ActiveDocument.recompute()

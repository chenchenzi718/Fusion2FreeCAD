import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00342296")
App.ActiveDocument.addObject("PartDesign::Body","Body_FBmEon6vKsqdptO_0")
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").Label = "Body_FBmEon6vKsqdptO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Plane", "plane_Sketch_FBmEon6vKsqdptO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBmEon6vKsqdptO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("Sketcher::SketchObject","Sketch_FBmEon6vKsqdptO_0_JGC")
App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBmEon6vKsqdptO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").addGeometry(Part.LineSegment(App.Vector(5.00909000000000,210.00000000000000,0.00000000000000),App.Vector(-4.99091000000000,210.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-4.99091000000000,210.00000000000000,0.00000000000000),App.Vector(-4.99091000000000,-182.83300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(15.00909000000000,-182.83300000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),20.00000000000000),3.14159265358979,3.31986239051211),False)

App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-4.67395000000000,-186.37954000000002,0.00000000000000),App.Vector(-0.49208000000000,-209.58866000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,-209.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),6.10415109957129,3.31985408288744),False)

App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.49201000000000,-209.58904000000001,0.00000000000000),App.Vector(4.68943000000000,-186.39447000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-14.99091000000000,-182.83300000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),20.00000000000000),6.10415696143941,0.0),False)

App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").addGeometry(Part.LineSegment(App.Vector(5.00909000000000,210.00000000000000,0.00000000000000),App.Vector(5.00909000000000,-182.83300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Pad","Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC")
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC")
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").Length = 250.0
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Plane", "plane_Sketch_FBmEon6vKsqdptO_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBmEon6vKsqdptO_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("Sketcher::SketchObject","Sketch_FBmEon6vKsqdptO_0_JGG")
App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBmEon6vKsqdptO_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGG").addGeometry(Part.Circle(App.Vector(0.00000000000000,-209.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Pad","Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG")
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGG")
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").Length = 250.0
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBmEon6vKsqdptO_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").Type = 0
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").Midplane = 1
App.ActiveDocument.getObject("Extrude_FBmEon6vKsqdptO_0_FjVowHqJN2ReMVk_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Plane", "plane_Sketch_Ft3BxSWDLCRaKov_1_JLC")
origin = App.Vector(-0.00000000000000,5.00909000000000,-4.41650000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("Sketcher::SketchObject","Sketch_Ft3BxSWDLCRaKov_1_JLC")
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLC").addGeometry(Part.Circle(App.Vector(0.00000000000000,202.41649999999998,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Pocket","Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLC")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Plane", "plane_Sketch_Ft3BxSWDLCRaKov_1_JLG")
origin = App.Vector(-0.00000000000000,5.00909000000000,-4.41650000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("Sketcher::SketchObject","Sketch_Ft3BxSWDLCRaKov_1_JLG")
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLG").addGeometry(Part.Circle(App.Vector(0.00000000000000,184.41649999999998,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Pocket","Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLG")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Plane", "plane_Sketch_Ft3BxSWDLCRaKov_1_JLK")
origin = App.Vector(-0.00000000000000,5.00909000000000,-4.41650000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("Sketcher::SketchObject","Sketch_Ft3BxSWDLCRaKov_1_JLK")
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK").addGeometry(Part.LineSegment(App.Vector(-121.00000000000000,-205.58350000000002,0.00000000000000),App.Vector(-124.88103000000001,-178.41650000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK").addGeometry(Part.LineSegment(App.Vector(-125.00000000000000,-178.41650000000001,0.00000000000000),App.Vector(-124.88103000000001,-178.41650000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK").addGeometry(Part.LineSegment(App.Vector(-125.00000000000000,-178.41650000000001,0.00000000000000),App.Vector(-125.00000000000000,-177.58369000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK").addGeometry(Part.LineSegment(App.Vector(-125.00000000000000,-177.58369000000002,0.00000000000000),App.Vector(-125.10335000000001,-205.58350000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK").addGeometry(Part.LineSegment(App.Vector(-121.00000000000000,-205.58350000000002,0.00000000000000),App.Vector(-125.10335000000001,-205.58350000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Pocket","Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Plane", "plane_Sketch_Ft3BxSWDLCRaKov_1_JLO")
origin = App.Vector(-0.00000000000000,5.00909000000000,-4.41650000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("Sketcher::SketchObject","Sketch_Ft3BxSWDLCRaKov_1_JLO")
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO").addGeometry(Part.LineSegment(App.Vector(121.00000000000000,-205.58350000000002,0.00000000000000),App.Vector(124.88103000000001,-178.41650000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO").addGeometry(Part.LineSegment(App.Vector(125.00000000000000,-178.41650000000001,0.00000000000000),App.Vector(124.88103000000001,-178.41650000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO").addGeometry(Part.LineSegment(App.Vector(125.00000000000000,-178.41650000000001,0.00000000000000),App.Vector(125.00000000000000,-177.58369000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO").addGeometry(Part.LineSegment(App.Vector(125.00000000000000,-177.58369000000002,0.00000000000000),App.Vector(125.10335000000001,-205.58350000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO").addGeometry(Part.LineSegment(App.Vector(121.00000000000000,-205.58350000000002,0.00000000000000),App.Vector(125.10335000000001,-205.58350000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Pocket","Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Plane", "plane_Sketch_Ft3BxSWDLCRaKov_1_JLS")
origin = App.Vector(-0.00000000000000,5.00909000000000,-4.41650000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("Sketcher::SketchObject","Sketch_Ft3BxSWDLCRaKov_1_JLS")
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLS"), [""])
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLS").addGeometry(Part.LineSegment(App.Vector(-125.00000000000000,-177.58369000000002,0.00000000000000),App.Vector(-124.88103000000001,-178.41650000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLS").addGeometry(Part.LineSegment(App.Vector(-125.00000000000000,-178.41650000000001,0.00000000000000),App.Vector(-124.88103000000001,-178.41650000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLS").addGeometry(Part.LineSegment(App.Vector(-125.00000000000000,-178.41650000000001,0.00000000000000),App.Vector(-125.00000000000000,-177.58369000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Pocket","Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").Profile = App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLS")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").Type = 4
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Plane", "plane_Sketch_Ft3BxSWDLCRaKov_1_JLW")
origin = App.Vector(-0.00000000000000,5.00909000000000,-4.41650000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("Sketcher::SketchObject","Sketch_Ft3BxSWDLCRaKov_1_JLW")
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft3BxSWDLCRaKov_1_JLW"), [""])
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLW").addGeometry(Part.LineSegment(App.Vector(125.00000000000000,-177.58369000000002,0.00000000000000),App.Vector(124.88103000000001,-178.41650000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLW").addGeometry(Part.LineSegment(App.Vector(125.00000000000000,-178.41650000000001,0.00000000000000),App.Vector(124.88103000000001,-178.41650000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLW").addGeometry(Part.LineSegment(App.Vector(125.00000000000000,-178.41650000000001,0.00000000000000),App.Vector(125.00000000000000,-177.58369000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBmEon6vKsqdptO_0").newObject("PartDesign::Pocket","Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").Profile = App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLW")
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft3BxSWDLCRaKov_1_JLW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").Type = 4
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft3BxSWDLCRaKov_1_FPghfRbtqydHPm8_1_JLW").Offset = 0
App.ActiveDocument.recompute()

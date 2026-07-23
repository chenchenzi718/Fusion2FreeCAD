import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00080957")
App.ActiveDocument.addObject("PartDesign::Body","Body_FBa9wpDfQYvs6G7_0")
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").Label = "Body_FBa9wpDfQYvs6G7_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Plane", "plane_Sketch_FBa9wpDfQYvs6G7_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBa9wpDfQYvs6G7_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("Sketcher::SketchObject","Sketch_FBa9wpDfQYvs6G7_0_JGK")
App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBa9wpDfQYvs6G7_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,-9.52500000000000,0.00000000000000),App.Vector(60.32500000000000,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK").addGeometry(Part.LineSegment(App.Vector(60.32500000000000,-9.52500000000000,0.00000000000000),App.Vector(60.32500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,9.52500000000000,0.00000000000000),App.Vector(60.32500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,-9.52500000000000,0.00000000000000),App.Vector(-60.32500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Pad","Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK")
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK")
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").Length = 21.844
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_FW7xzqLT7UZpiQI_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Plane", "plane_Sketch_FBa9wpDfQYvs6G7_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBa9wpDfQYvs6G7_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("Sketcher::SketchObject","Sketch_FBa9wpDfQYvs6G7_0_JGC")
App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBa9wpDfQYvs6G7_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC").addGeometry(Part.LineSegment(App.Vector(-88.90000000000001,9.52500000000000,0.00000000000000),App.Vector(-60.32500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,-9.52500000000000,0.00000000000000),App.Vector(-60.32500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC").addGeometry(Part.LineSegment(App.Vector(-88.90000000000001,-9.52500000000000,0.00000000000000),App.Vector(-60.32500000000000,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC").addGeometry(Part.LineSegment(App.Vector(-88.90000000000001,9.52500000000000,0.00000000000000),App.Vector(-88.90000000000001,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Pad","Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC")
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").Profile = App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC")
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").Length = 13.208
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Plane", "plane_Sketch_FBa9wpDfQYvs6G7_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBa9wpDfQYvs6G7_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("Sketcher::SketchObject","Sketch_FBa9wpDfQYvs6G7_0_JGG")
App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBa9wpDfQYvs6G7_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG").addGeometry(Part.LineSegment(App.Vector(88.90000000000001,9.52500000000000,0.00000000000000),App.Vector(60.32500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG").addGeometry(Part.LineSegment(App.Vector(60.32500000000000,-9.52500000000000,0.00000000000000),App.Vector(60.32500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG").addGeometry(Part.LineSegment(App.Vector(88.90000000000001,-9.52500000000000,0.00000000000000),App.Vector(60.32500000000000,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG").addGeometry(Part.LineSegment(App.Vector(88.90000000000001,9.52500000000000,0.00000000000000),App.Vector(88.90000000000001,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Pad","Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG")
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").Profile = App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG")
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").Length = 13.208
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBa9wpDfQYvs6G7_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBa9wpDfQYvs6G7_0_F9y1yFTb8okqRIR_1_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Plane", "plane_Sketch_FS3k39FokMUaRpT_1_JLG")
origin = App.Vector(-74.61250000000000,-0.00000000000000,13.20800000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS3k39FokMUaRpT_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("Sketcher::SketchObject","Sketch_FS3k39FokMUaRpT_1_JLG")
App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS3k39FokMUaRpT_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLG").addGeometry(Part.Circle(App.Vector(-1.58750000000001,-5.08000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),2.42570000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Pocket","Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG")
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLG")
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Plane", "plane_Sketch_FS3k39FokMUaRpT_1_JLC")
origin = App.Vector(-74.61250000000000,-0.00000000000000,13.20800000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS3k39FokMUaRpT_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("Sketcher::SketchObject","Sketch_FS3k39FokMUaRpT_1_JLC")
App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS3k39FokMUaRpT_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLC").addGeometry(Part.Circle(App.Vector(150.81250000000003,-5.08000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),2.42570000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Pocket","Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC")
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLC")
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS3k39FokMUaRpT_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS3k39FokMUaRpT_1_Fm3c7QkgHz0vBk5_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Plane", "plane_Sketch_FSlBewbGtj98C9u_1_JPC")
origin = App.Vector(0.00000000000000,-0.00000000000000,21.84400000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSlBewbGtj98C9u_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("Sketcher::SketchObject","Sketch_FSlBewbGtj98C9u_1_JPC")
App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSlBewbGtj98C9u_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPC").addGeometry(Part.Circle(App.Vector(-53.97500000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),2.42570000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Pocket","Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC")
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPC")
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Plane", "plane_Sketch_FSlBewbGtj98C9u_1_JPG")
origin = App.Vector(0.00000000000000,-0.00000000000000,21.84400000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSlBewbGtj98C9u_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("Sketcher::SketchObject","Sketch_FSlBewbGtj98C9u_1_JPG")
App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSlBewbGtj98C9u_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPG").addGeometry(Part.Circle(App.Vector(53.97500000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),2.42570000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Pocket","Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG")
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPG")
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSlBewbGtj98C9u_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSlBewbGtj98C9u_1_FvO1EepI4R940qe_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Plane", "plane_Sketch_FmZbdnbNjLeyZdS_1_JTC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmZbdnbNjLeyZdS_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("Sketcher::SketchObject","Sketch_FmZbdnbNjLeyZdS_1_JTC")
App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmZbdnbNjLeyZdS_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTC").addGeometry(Part.Circle(App.Vector(-53.97500000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),4.03860000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Pocket","Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC")
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTC")
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").Length = 5.2324
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").Type = 0
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Plane", "plane_Sketch_FmZbdnbNjLeyZdS_1_JTG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmZbdnbNjLeyZdS_1_JTG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("Sketcher::SketchObject","Sketch_FmZbdnbNjLeyZdS_1_JTG")
App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmZbdnbNjLeyZdS_1_JTG"), [""])
App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTG").addGeometry(Part.Circle(App.Vector(53.97500000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),4.03860000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBa9wpDfQYvs6G7_0").newObject("PartDesign::Pocket","Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG")
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").Profile = App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTG")
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").Length = 5.2324
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmZbdnbNjLeyZdS_1_JTG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").Type = 0
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmZbdnbNjLeyZdS_1_FBH8ZKBgaz0TEhY_1_JTG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00816795")
App.ActiveDocument.addObject("PartDesign::Body","Body_FPH950ln0y0PLxA_0")
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").Label = "Body_FPH950ln0y0PLxA_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_FPH950ln0y0PLxA_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPH950ln0y0PLxA_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_FPH950ln0y0PLxA_0_JGC")
App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPH950ln0y0PLxA_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-140.00000000000000,110.00000000000000,0.00000000000000),App.Vector(140.00000000000000,110.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(140.00000000000000,100.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").addGeometry(Part.LineSegment(App.Vector(150.00000000000000,100.00000000000000,0.00000000000000),App.Vector(150.00000000000000,-100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(140.00000000000000,-100.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-140.00000000000000,-110.00000000000000,0.00000000000000),App.Vector(140.00000000000000,-110.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-140.00000000000000,-100.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-150.00000000000000,100.00000000000000,0.00000000000000),App.Vector(-150.00000000000000,-100.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-140.00000000000000,100.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pad","Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC")
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC")
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPH950ln0y0PLxA_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPH950ln0y0PLxA_0_F1veohRFNWI4pv7_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_F02niV7hzGeh1BO_1_JJy")
origin = App.Vector(-0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJy").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_F02niV7hzGeh1BO_1_JJy")
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJy").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJy"), [""])
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJy").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJy").addGeometry(Part.Circle(App.Vector(-83.84011000000000,16.04264000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJy").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJy").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pocket","Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").Profile = App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJy")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").Length = 10.0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJy"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").Type = 4
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJy").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_F02niV7hzGeh1BO_1_JJu")
origin = App.Vector(-0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJu").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_F02niV7hzGeh1BO_1_JJu")
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJu").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJu"), [""])
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJu").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJu").addGeometry(Part.Circle(App.Vector(-18.84011000000000,41.04264000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJu").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJu").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pocket","Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").Profile = App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJu")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").Length = 10.0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJu"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").Type = 4
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJu").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_F02niV7hzGeh1BO_1_JJm")
origin = App.Vector(-0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJm").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_F02niV7hzGeh1BO_1_JJm")
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJm").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJm"), [""])
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJm").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJm").addGeometry(Part.Circle(App.Vector(16.15989000000000,63.04264000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJm").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJm").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pocket","Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").Profile = App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJm")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").Length = 10.0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJm"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").Type = 4
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJm").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_F02niV7hzGeh1BO_1_JJa")
origin = App.Vector(-0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_F02niV7hzGeh1BO_1_JJa")
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJa").addGeometry(Part.Circle(App.Vector(56.15989000000000,61.04264000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pocket","Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJa")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").Length = 10.0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_F02niV7hzGeh1BO_1_JJW")
origin = App.Vector(-0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_F02niV7hzGeh1BO_1_JJW")
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJW").addGeometry(Part.Circle(App.Vector(96.15989000000000,59.04264000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pocket","Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJW")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").Length = 10.0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_F02niV7hzGeh1BO_1_JJS")
origin = App.Vector(-0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_F02niV7hzGeh1BO_1_JJS")
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJS").addGeometry(Part.Circle(App.Vector(96.15989000000000,19.04264000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pocket","Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJS")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").Length = 10.0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_F02niV7hzGeh1BO_1_JJe")
origin = App.Vector(-0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_F02niV7hzGeh1BO_1_JJe")
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJe"), [""])
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJe").addGeometry(Part.Circle(App.Vector(56.15989000000000,21.04264000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pocket","Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").Profile = App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJe")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").Length = 10.0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").Type = 4
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_F02niV7hzGeh1BO_1_JJi")
origin = App.Vector(-0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_F02niV7hzGeh1BO_1_JJi")
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJi"), [""])
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJi").addGeometry(Part.Circle(App.Vector(16.15989000000000,23.04264000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pocket","Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").Profile = App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJi")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").Length = 10.0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").Type = 4
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJi").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Plane", "plane_Sketch_F02niV7hzGeh1BO_1_JJq")
origin = App.Vector(-0.00000000000000,-0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJq").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("Sketcher::SketchObject","Sketch_F02niV7hzGeh1BO_1_JJq")
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJq").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02niV7hzGeh1BO_1_JJq"), [""])
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJq").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJq").addGeometry(Part.Circle(App.Vector(-18.84011000000000,1.04264000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJq").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJq").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FPH950ln0y0PLxA_0").newObject("PartDesign::Pocket","Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").Profile = App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJq")
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").Length = 10.0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02niV7hzGeh1BO_1_JJq"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").Type = 4
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02niV7hzGeh1BO_1_FupLM4ow248T6KD_1_JJq").Offset = 0
App.ActiveDocument.recompute()

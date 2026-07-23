import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00633158")
App.ActiveDocument.addObject("PartDesign::Body","Body_FeWXxJv84B3tuH0_0")
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").Label = "Body_FeWXxJv84B3tuH0_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Plane", "plane_Sketch_FeWXxJv84B3tuH0_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeWXxJv84B3tuH0_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("Sketcher::SketchObject","Sketch_FeWXxJv84B3tuH0_0_JGC")
App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeWXxJv84B3tuH0_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").addGeometry(Part.LineSegment(App.Vector(43.40808000000000,-44.81285000000000,0.00000000000000),App.Vector(43.40808000000000,-3.08741000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").addGeometry(Part.LineSegment(App.Vector(43.40808000000000,-3.08741000000000,0.00000000000000),App.Vector(43.40808000000000,3.18346000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").addGeometry(Part.LineSegment(App.Vector(43.40808000000000,23.92559000000000,0.00000000000000),App.Vector(43.40808000000000,3.18346000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").addGeometry(Part.LineSegment(App.Vector(43.40808000000000,23.92559000000000,0.00000000000000),App.Vector(-9.41197000000000,23.92559000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").addGeometry(Part.LineSegment(App.Vector(-16.64760000000000,23.92559000000000,0.00000000000000),App.Vector(-9.41197000000000,23.92559000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").addGeometry(Part.LineSegment(App.Vector(-16.64760000000000,23.92559000000000,0.00000000000000),App.Vector(-16.64760000000000,34.53784000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").addGeometry(Part.LineSegment(App.Vector(-16.64760000000000,34.53784000000000,0.00000000000000),App.Vector(53.77915000000000,34.53784000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").addGeometry(Part.LineSegment(App.Vector(53.77915000000000,34.53784000000000,0.00000000000000),App.Vector(53.77915000000000,-44.57166000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").addGeometry(Part.LineSegment(App.Vector(43.40808000000000,-44.81285000000000,0.00000000000000),App.Vector(53.77915000000000,-44.57166000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Pad","Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC")
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC")
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").Length = 71.8
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Plane", "plane_Sketch_FeWXxJv84B3tuH0_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeWXxJv84B3tuH0_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("Sketcher::SketchObject","Sketch_FeWXxJv84B3tuH0_0_JGG")
App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeWXxJv84B3tuH0_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").addGeometry(Part.LineSegment(App.Vector(43.40808000000000,-3.08741000000000,0.00000000000000),App.Vector(43.40808000000000,3.18346000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").addGeometry(Part.LineSegment(App.Vector(43.40808000000000,3.18346000000000,0.00000000000000),App.Vector(-9.41197000000000,3.18346000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").addGeometry(Part.LineSegment(App.Vector(-9.41197000000000,3.18346000000000,0.00000000000000),App.Vector(-9.41197000000000,23.92559000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").addGeometry(Part.LineSegment(App.Vector(-16.64760000000000,23.92559000000000,0.00000000000000),App.Vector(-9.41197000000000,23.92559000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").addGeometry(Part.LineSegment(App.Vector(-16.64760000000000,23.92559000000000,0.00000000000000),App.Vector(-16.64760000000000,-3.08741000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").addGeometry(Part.LineSegment(App.Vector(43.40808000000000,-3.08741000000000,0.00000000000000),App.Vector(-16.64760000000000,-3.08741000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Pad","Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG")
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG")
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").Length = 71.8
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeWXxJv84B3tuH0_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeWXxJv84B3tuH0_0_FS0iM9rs7IJQKVB_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Plane", "plane_Sketch_FEl2olQGKmDgZAG_1_JJC")
origin = App.Vector(-14.13260000000000,-2.51500000000000,34.53784000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEl2olQGKmDgZAG_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("Sketcher::SketchObject","Sketch_FEl2olQGKmDgZAG_1_JJC")
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEl2olQGKmDgZAG_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJC").addGeometry(Part.Circle(App.Vector(2.48500000000000,-64.28500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Pad","Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC")
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJC")
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").Length = 39.4
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Plane", "plane_Sketch_FEl2olQGKmDgZAG_1_JJG")
origin = App.Vector(-14.13260000000000,-2.51500000000000,34.53784000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEl2olQGKmDgZAG_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("Sketcher::SketchObject","Sketch_FEl2olQGKmDgZAG_1_JJG")
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEl2olQGKmDgZAG_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJG").addGeometry(Part.Circle(App.Vector(62.91175000000000,-64.28500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Pad","Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG")
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJG")
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").Length = 39.4
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Plane", "plane_Sketch_FEl2olQGKmDgZAG_1_JJK")
origin = App.Vector(-14.13260000000000,-2.51500000000000,34.53784000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEl2olQGKmDgZAG_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("Sketcher::SketchObject","Sketch_FEl2olQGKmDgZAG_1_JJK")
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEl2olQGKmDgZAG_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJK").addGeometry(Part.Circle(App.Vector(62.91175000000000,-2.48500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Pad","Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK")
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJK")
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").Length = 39.4
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Plane", "plane_Sketch_FEl2olQGKmDgZAG_1_JJO")
origin = App.Vector(-14.13260000000000,-2.51500000000000,34.53784000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEl2olQGKmDgZAG_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("Sketcher::SketchObject","Sketch_FEl2olQGKmDgZAG_1_JJO")
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEl2olQGKmDgZAG_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJO").addGeometry(Part.Circle(App.Vector(2.48500000000000,-2.48500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Pad","Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO")
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJO")
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").Length = 39.4
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEl2olQGKmDgZAG_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEl2olQGKmDgZAG_1_FkT776Tlnj2TJm8_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Plane", "plane_Sketch_FaUCNV1zcTKZmCK_1_JNC")
origin = App.Vector(18.56578000000000,-71.80000000000000,14.76046000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaUCNV1zcTKZmCK_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("Sketcher::SketchObject","Sketch_FaUCNV1zcTKZmCK_1_JNC")
App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaUCNV1zcTKZmCK_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC").addGeometry(Part.LineSegment(App.Vector(35.21336999999999,-19.77737000000000,0.00000000000000),App.Vector(26.21337000000000,-19.77737000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC").addGeometry(Part.LineSegment(App.Vector(26.21337000000000,-19.77737000000000,0.00000000000000),App.Vector(26.21337000000000,-29.77737000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC").addGeometry(Part.LineSegment(App.Vector(35.21336999999999,-29.77737000000000,0.00000000000000),App.Vector(26.21337000000000,-29.77737000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC").addGeometry(Part.LineSegment(App.Vector(35.21336999999999,-19.77737000000000,0.00000000000000),App.Vector(35.21336999999999,-29.77737000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Pad","Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC")
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC")
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").Length = 7.0
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaUCNV1zcTKZmCK_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaUCNV1zcTKZmCK_1_F5SPMll7PeaUQ15_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Plane", "plane_Sketch_FabSLn6umaE0gq4_1_JRC")
origin = App.Vector(18.56578000000000,0.00000000000000,14.76046000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FabSLn6umaE0gq4_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("Sketcher::SketchObject","Sketch_FabSLn6umaE0gq4_1_JRC")
App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FabSLn6umaE0gq4_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC").addGeometry(Part.LineSegment(App.Vector(-35.21336999999999,-19.77737000000000,0.00000000000000),App.Vector(-26.21337000000000,-19.77737000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC").addGeometry(Part.LineSegment(App.Vector(-26.21337000000000,-19.77737000000000,0.00000000000000),App.Vector(-26.21337000000000,-29.77737000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC").addGeometry(Part.LineSegment(App.Vector(-35.21336999999999,-29.77737000000000,0.00000000000000),App.Vector(-26.21337000000000,-29.77737000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC").addGeometry(Part.LineSegment(App.Vector(-35.21336999999999,-19.77737000000000,0.00000000000000),App.Vector(-35.21336999999999,-29.77737000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeWXxJv84B3tuH0_0").newObject("PartDesign::Pad","Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC")
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC")
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").Length = 7.0
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FabSLn6umaE0gq4_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FabSLn6umaE0gq4_1_Fn1a32IbPDJGdGp_1_JRC").Offset = 0
App.ActiveDocument.recompute()

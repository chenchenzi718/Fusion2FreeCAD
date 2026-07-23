import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00787772")
App.ActiveDocument.addObject("PartDesign::Body","Body_F4OSNgTCQnCW7ey_0")
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").Label = "Body_F4OSNgTCQnCW7ey_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Plane", "plane_Sketch_F4OSNgTCQnCW7ey_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4OSNgTCQnCW7ey_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("Sketcher::SketchObject","Sketch_F4OSNgTCQnCW7ey_0_JGC")
App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4OSNgTCQnCW7ey_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.25000000000000,0.00000000000000,0.00000000000000),App.Vector(16.25000000000000,-29.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.25000000000000,-29.50000000000000,0.00000000000000),App.Vector(-16.25000000000000,-29.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC").addGeometry(Part.LineSegment(App.Vector(-16.25000000000000,0.00000000000000,0.00000000000000),App.Vector(-16.25000000000000,-29.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),16.25000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Pad","Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC")
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC")
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").Length = 40.0
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Plane", "plane_Sketch_F4OSNgTCQnCW7ey_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4OSNgTCQnCW7ey_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("Sketcher::SketchObject","Sketch_F4OSNgTCQnCW7ey_0_JGG")
App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4OSNgTCQnCW7ey_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG").addGeometry(Part.LineSegment(App.Vector(16.25000000000000,-29.50000000000000,0.00000000000000),App.Vector(-16.25000000000000,-29.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG").addGeometry(Part.LineSegment(App.Vector(-16.25000000000000,-29.50000000000000,0.00000000000000),App.Vector(-16.25000000000000,-59.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG").addGeometry(Part.LineSegment(App.Vector(-16.25000000000000,-59.50000000000000,0.00000000000000),App.Vector(16.25000000000000,-59.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG").addGeometry(Part.LineSegment(App.Vector(16.25000000000000,-29.50000000000000,0.00000000000000),App.Vector(16.25000000000000,-59.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Pad","Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG")
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG")
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").Length = 40.0
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4OSNgTCQnCW7ey_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4OSNgTCQnCW7ey_0_Fvyn3PCJ0i3fHTi_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Plane", "plane_Sketch_F6pT0CutA7q7GYX_1_JJG")
origin = App.Vector(-16.25000000000000,-29.75000000000000,20.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6pT0CutA7q7GYX_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("Sketcher::SketchObject","Sketch_F6pT0CutA7q7GYX_1_JJG")
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6pT0CutA7q7GYX_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG").addGeometry(Part.LineSegment(App.Vector(29.75000000000000,20.00000000000000,0.00000000000000),App.Vector(29.75000000000000,12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG").addGeometry(Part.LineSegment(App.Vector(29.75000000000000,12.00000000000000,0.00000000000000),App.Vector(7.75000000000000,12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(7.75000000000000,20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG").addGeometry(Part.LineSegment(App.Vector(29.75000000000000,20.00000000000000,0.00000000000000),App.Vector(-0.25000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Pocket","Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG")
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG")
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").Length = 32.5
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Plane", "plane_Sketch_F6pT0CutA7q7GYX_1_JJC")
origin = App.Vector(-16.25000000000000,-29.75000000000000,20.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6pT0CutA7q7GYX_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("Sketcher::SketchObject","Sketch_F6pT0CutA7q7GYX_1_JJC")
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6pT0CutA7q7GYX_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC").addGeometry(Part.LineSegment(App.Vector(29.75000000000000,-20.00000000000000,0.00000000000000),App.Vector(29.75000000000000,-12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC").addGeometry(Part.LineSegment(App.Vector(29.75000000000000,-12.00000000000000,0.00000000000000),App.Vector(7.75000000000000,-12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(7.75000000000000,-20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC").addGeometry(Part.LineSegment(App.Vector(29.75000000000000,-20.00000000000000,0.00000000000000),App.Vector(-0.25000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Pocket","Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC")
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC")
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").Length = 32.5
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Plane", "plane_Sketch_F6pT0CutA7q7GYX_1_JJK")
origin = App.Vector(-16.25000000000000,-29.75000000000000,20.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6pT0CutA7q7GYX_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("Sketcher::SketchObject","Sketch_F6pT0CutA7q7GYX_1_JJK")
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6pT0CutA7q7GYX_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJK").addGeometry(Part.Circle(App.Vector(-0.25000000000000,0.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Pocket","Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK")
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJK")
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").Length = 32.5
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Plane", "plane_Sketch_F6pT0CutA7q7GYX_1_JJO")
origin = App.Vector(-16.25000000000000,-29.75000000000000,20.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6pT0CutA7q7GYX_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("Sketcher::SketchObject","Sketch_F6pT0CutA7q7GYX_1_JJO")
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6pT0CutA7q7GYX_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJO").addGeometry(Part.Circle(App.Vector(19.75000000000000,0.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Pocket","Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO")
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJO")
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").Length = 32.5
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6pT0CutA7q7GYX_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6pT0CutA7q7GYX_1_FSbObPLbJrYcbIf_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Plane", "plane_Sketch_F7vZjSwZ3InshoU_1_JNC")
origin = App.Vector(0.00000000000000,-6.48775000000000,40.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7vZjSwZ3InshoU_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("Sketcher::SketchObject","Sketch_F7vZjSwZ3InshoU_1_JNC")
App.ActiveDocument.getObject("Sketch_F7vZjSwZ3InshoU_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7vZjSwZ3InshoU_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F7vZjSwZ3InshoU_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7vZjSwZ3InshoU_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,6.48775000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7vZjSwZ3InshoU_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7vZjSwZ3InshoU_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Pocket","Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC")
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F7vZjSwZ3InshoU_1_JNC")
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").Length = 40.0
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7vZjSwZ3InshoU_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7vZjSwZ3InshoU_1_FyLAO3oeT95bLsy_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Plane", "plane_Sketch_F6nYuL3wzLnN9mU_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6nYuL3wzLnN9mU_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("Sketcher::SketchObject","Sketch_F6nYuL3wzLnN9mU_1_JRG")
App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6nYuL3wzLnN9mU_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG").addGeometry(Part.LineSegment(App.Vector(14.75000000000000,29.00000000000000,0.00000000000000),App.Vector(14.75000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG").addGeometry(Part.LineSegment(App.Vector(14.75000000000000,35.00000000000000,0.00000000000000),App.Vector(0.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,35.00000000000000,0.00000000000000),App.Vector(-14.75000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG").addGeometry(Part.LineSegment(App.Vector(-14.75000000000000,35.00000000000000,0.00000000000000),App.Vector(-14.75000000000000,29.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG").addGeometry(Part.LineSegment(App.Vector(14.75000000000000,29.00000000000000,0.00000000000000),App.Vector(-14.75000000000000,29.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Pocket","Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG")
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG")
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").Length = 12.0
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").Type = 0
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").Midplane = 1
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Plane", "plane_Sketch_F6nYuL3wzLnN9mU_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6nYuL3wzLnN9mU_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("Sketcher::SketchObject","Sketch_F6nYuL3wzLnN9mU_1_JRC")
App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6nYuL3wzLnN9mU_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC").addGeometry(Part.LineSegment(App.Vector(14.75000000000000,5.00000000000000,0.00000000000000),App.Vector(14.75000000000000,11.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC").addGeometry(Part.LineSegment(App.Vector(14.75000000000000,11.00000000000000,0.00000000000000),App.Vector(-14.75000000000000,11.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC").addGeometry(Part.LineSegment(App.Vector(-14.75000000000000,11.00000000000000,0.00000000000000),App.Vector(-14.75000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC").addGeometry(Part.LineSegment(App.Vector(14.75000000000000,5.00000000000000,0.00000000000000),App.Vector(-14.75000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4OSNgTCQnCW7ey_0").newObject("PartDesign::Pocket","Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC")
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC")
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").Length = 12.0
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6nYuL3wzLnN9mU_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F6nYuL3wzLnN9mU_1_Fe940D7qcgQ3MGH_1_JRC").Offset = 0
App.ActiveDocument.recompute()

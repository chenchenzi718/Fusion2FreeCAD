import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00868499")
App.ActiveDocument.addObject("PartDesign::Body","Body_FfZMKXQibG1OLrP_0")
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").Label = "Body_FfZMKXQibG1OLrP_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_FfZMKXQibG1OLrP_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfZMKXQibG1OLrP_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_FfZMKXQibG1OLrP_0_JGC")
App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfZMKXQibG1OLrP_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").addGeometry(Part.LineSegment(App.Vector(-46.00000000000000,35.00000000000000,0.00000000000000),App.Vector(46.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(46.00000000000000,33.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").addGeometry(Part.LineSegment(App.Vector(48.00000000000000,33.00000000000000,0.00000000000000),App.Vector(48.00000000000000,-33.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(46.00000000000000,-33.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").addGeometry(Part.LineSegment(App.Vector(-46.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(46.00000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-46.00000000000000,-33.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").addGeometry(Part.LineSegment(App.Vector(-48.00000000000000,33.00000000000000,0.00000000000000),App.Vector(-48.00000000000000,-33.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-46.00000000000000,33.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pad","Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC")
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC")
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").Length = 26.000000000000004
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfZMKXQibG1OLrP_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfZMKXQibG1OLrP_0_FQwVqdkywc8rgMZ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_F8A5iT8oXTY2rCT_2_JLC")
origin = App.Vector(0.00000000000000,0.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8A5iT8oXTY2rCT_2_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_F8A5iT8oXTY2rCT_2_JLC")
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8A5iT8oXTY2rCT_2_JLC"), [""])
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLC").addGeometry(Part.Circle(App.Vector(-41.50000000000000,-28.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pocket","Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC")
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").Profile = App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLC")
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").Length = 2.0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_F8A5iT8oXTY2rCT_2_JLG")
origin = App.Vector(0.00000000000000,0.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8A5iT8oXTY2rCT_2_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_F8A5iT8oXTY2rCT_2_JLG")
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8A5iT8oXTY2rCT_2_JLG"), [""])
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLG").addGeometry(Part.Circle(App.Vector(-41.50000000000000,28.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pocket","Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG")
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").Profile = App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLG")
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").Length = 2.0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_F8A5iT8oXTY2rCT_2_JLK")
origin = App.Vector(0.00000000000000,0.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8A5iT8oXTY2rCT_2_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_F8A5iT8oXTY2rCT_2_JLK")
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8A5iT8oXTY2rCT_2_JLK"), [""])
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLK").addGeometry(Part.Circle(App.Vector(41.50000000000000,28.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pocket","Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK")
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").Profile = App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLK")
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").Length = 2.0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_F8A5iT8oXTY2rCT_2_JLO")
origin = App.Vector(0.00000000000000,0.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8A5iT8oXTY2rCT_2_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_F8A5iT8oXTY2rCT_2_JLO")
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8A5iT8oXTY2rCT_2_JLO"), [""])
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLO").addGeometry(Part.Circle(App.Vector(41.50000000000000,-28.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pocket","Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO")
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").Profile = App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLO")
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").Length = 2.0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8A5iT8oXTY2rCT_2_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8A5iT8oXTY2rCT_2_FwIZePNAPBvbzvK_2_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_FKgLPXXGR9pUbE0_2_JPa")
origin = App.Vector(0.00000000000000,0.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_FKgLPXXGR9pUbE0_2_JPa")
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPa"), [""])
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-43.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa").addGeometry(Part.LineSegment(App.Vector(-43.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-43.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-43.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-38.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pocket","Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").Profile = App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").Length = 22.0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").Type = 4
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_FKgLPXXGR9pUbE0_2_JPS")
origin = App.Vector(0.00000000000000,0.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_FKgLPXXGR9pUbE0_2_JPS")
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPS"), [""])
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(38.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS").addGeometry(Part.LineSegment(App.Vector(38.00000000000000,-30.00000000000000,0.00000000000000),App.Vector(38.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,-30.00000000000000,0.00000000000000),App.Vector(38.00000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-38.00000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pocket","Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").Profile = App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").Length = 22.0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").Type = 4
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_FKgLPXXGR9pUbE0_2_JPi")
origin = App.Vector(0.00000000000000,0.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_FKgLPXXGR9pUbE0_2_JPi")
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPi"), [""])
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(38.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi").addGeometry(Part.LineSegment(App.Vector(38.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(38.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,25.00000000000000,0.00000000000000),App.Vector(38.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-38.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pocket","Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").Profile = App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").Length = 22.0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").Type = 4
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPi").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_FKgLPXXGR9pUbE0_2_JPe")
origin = App.Vector(0.00000000000000,0.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_FKgLPXXGR9pUbE0_2_JPe")
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPe"), [""])
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,25.00000000000000,0.00000000000000),App.Vector(38.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe").addGeometry(Part.LineSegment(App.Vector(38.00000000000000,30.00000000000000,0.00000000000000),App.Vector(38.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,30.00000000000000,0.00000000000000),App.Vector(38.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-38.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pocket","Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").Profile = App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").Length = 22.0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").Type = 4
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Plane", "plane_Sketch_FKgLPXXGR9pUbE0_2_JPW")
origin = App.Vector(0.00000000000000,0.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("Sketcher::SketchObject","Sketch_FKgLPXXGR9pUbE0_2_JPW")
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKgLPXXGR9pUbE0_2_JPW"), [""])
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW").addGeometry(Part.LineSegment(App.Vector(43.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(38.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW").addGeometry(Part.LineSegment(App.Vector(38.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(38.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW").addGeometry(Part.LineSegment(App.Vector(43.00000000000000,25.00000000000000,0.00000000000000),App.Vector(38.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW").addGeometry(Part.LineSegment(App.Vector(43.00000000000000,25.00000000000000,0.00000000000000),App.Vector(43.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfZMKXQibG1OLrP_0").newObject("PartDesign::Pocket","Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").Profile = App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW")
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").Length = 22.0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKgLPXXGR9pUbE0_2_JPW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").Type = 4
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKgLPXXGR9pUbE0_2_FMWNTsVH72SFmze_2_JPW").Offset = 0
App.ActiveDocument.recompute()

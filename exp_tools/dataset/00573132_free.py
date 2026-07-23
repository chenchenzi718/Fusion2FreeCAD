import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00573132")
App.ActiveDocument.addObject("PartDesign::Body","Body_F7LWj89CHoNdoY4_0")
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").Label = "Body_F7LWj89CHoNdoY4_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Plane", "plane_Sketch_F7LWj89CHoNdoY4_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7LWj89CHoNdoY4_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("Sketcher::SketchObject","Sketch_F7LWj89CHoNdoY4_0_JGC")
App.ActiveDocument.getObject("Sketch_F7LWj89CHoNdoY4_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7LWj89CHoNdoY4_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F7LWj89CHoNdoY4_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7LWj89CHoNdoY4_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.65000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7LWj89CHoNdoY4_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7LWj89CHoNdoY4_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Pad","Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC")
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F7LWj89CHoNdoY4_0_JGC")
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").Length = 2.2
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7LWj89CHoNdoY4_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7LWj89CHoNdoY4_0_FtXurVn311WkeE4_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Plane", "plane_Sketch_F0VrhnPd0m2r12e_1_KJWB")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJWB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("Sketcher::SketchObject","Sketch_F0VrhnPd0m2r12e_1_KJWB")
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJWB"), [""])
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.65000000000000),3.92699081698724,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-8.65000000000000,0.00000000000000),App.Vector(0.00000000000000,-6.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.65000000000000),3.92699081698724,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB").addGeometry(Part.LineSegment(App.Vector(-6.11647000000000,-6.11647000000000,0.00000000000000),App.Vector(-4.70226000000000,-4.70226000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Pocket","Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").Profile = App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").Type = 4
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Plane", "plane_Sketch_F0VrhnPd0m2r12e_1_KJWC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("Sketcher::SketchObject","Sketch_F0VrhnPd0m2r12e_1_KJWC")
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJWC"), [""])
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.65000000000000),3.92699081698724,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-4.65000000000000,0.00000000000000),App.Vector(0.00000000000000,-2.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.65000000000000),3.92699081698724,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC").addGeometry(Part.LineSegment(App.Vector(-3.28805000000000,-3.28805000000000,0.00000000000000),App.Vector(-1.87383000000000,-1.87383000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Pocket","Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").Profile = App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").Type = 4
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Plane", "plane_Sketch_F0VrhnPd0m2r12e_1_KJeB")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJeB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("Sketcher::SketchObject","Sketch_F0VrhnPd0m2r12e_1_KJeB")
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJeB"), [""])
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.65000000000000),5.49778714378214,0.0),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB").addGeometry(Part.LineSegment(App.Vector(6.11647000000000,-6.11647000000000,0.00000000000000),App.Vector(4.70226000000000,-4.70226000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.65000000000000),5.49778714378214,0.0),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB").addGeometry(Part.LineSegment(App.Vector(8.65000000000000,0.00000000000000,0.00000000000000),App.Vector(6.65000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Pocket","Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").Profile = App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").Type = 4
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Plane", "plane_Sketch_F0VrhnPd0m2r12e_1_KJeC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJeC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("Sketcher::SketchObject","Sketch_F0VrhnPd0m2r12e_1_KJeC")
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJeC"), [""])
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.65000000000000),5.49778714378214,0.0),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC").addGeometry(Part.LineSegment(App.Vector(3.28805000000000,-3.28805000000000,0.00000000000000),App.Vector(1.87383000000000,-1.87383000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.65000000000000),5.49778714378214,0.0),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC").addGeometry(Part.LineSegment(App.Vector(4.65000000000000,0.00000000000000,0.00000000000000),App.Vector(2.65000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Pocket","Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").Profile = App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJeC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").Type = 4
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJeC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Plane", "plane_Sketch_F0VrhnPd0m2r12e_1_KJGB")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJGB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("Sketcher::SketchObject","Sketch_F0VrhnPd0m2r12e_1_KJGB")
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJGB"), [""])
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.65000000000000),0.78539816339745,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,8.65000000000000,0.00000000000000),App.Vector(0.00000000000000,6.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.65000000000000),0.78539816339745,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB").addGeometry(Part.LineSegment(App.Vector(6.11647000000000,6.11647000000000,0.00000000000000),App.Vector(4.70226000000000,4.70226000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Pocket","Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").Profile = App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").Type = 4
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Plane", "plane_Sketch_F0VrhnPd0m2r12e_1_KJGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("Sketcher::SketchObject","Sketch_F0VrhnPd0m2r12e_1_KJGC")
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJGC"), [""])
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.65000000000000),0.78539816339745,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,4.65000000000000,0.00000000000000),App.Vector(0.00000000000000,2.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.65000000000000),0.78539816339745,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC").addGeometry(Part.LineSegment(App.Vector(3.28805000000000,3.28805000000000,0.00000000000000),App.Vector(1.87383000000000,1.87383000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Pocket","Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").Profile = App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").Type = 4
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Plane", "plane_Sketch_F0VrhnPd0m2r12e_1_KJOC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("Sketcher::SketchObject","Sketch_F0VrhnPd0m2r12e_1_KJOC")
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJOC"), [""])
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.65000000000000),2.35619449019234,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC").addGeometry(Part.LineSegment(App.Vector(-4.65000000000000,0.00000000000000,0.00000000000000),App.Vector(-2.65000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.65000000000000),2.35619449019234,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC").addGeometry(Part.LineSegment(App.Vector(-3.28805000000000,3.28805000000000,0.00000000000000),App.Vector(-1.87383000000000,1.87383000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Pocket","Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").Profile = App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").Type = 4
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Plane", "plane_Sketch_F0VrhnPd0m2r12e_1_KJOB")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJOB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("Sketcher::SketchObject","Sketch_F0VrhnPd0m2r12e_1_KJOB")
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0VrhnPd0m2r12e_1_KJOB"), [""])
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.65000000000000),2.35619449019234,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB").addGeometry(Part.LineSegment(App.Vector(-8.65000000000000,0.00000000000000,0.00000000000000),App.Vector(-6.65000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.65000000000000),2.35619449019234,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB").addGeometry(Part.LineSegment(App.Vector(-6.11647000000000,6.11647000000000,0.00000000000000),App.Vector(-4.70226000000000,4.70226000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F7LWj89CHoNdoY4_0").newObject("PartDesign::Pocket","Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").Profile = App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB")
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0VrhnPd0m2r12e_1_KJOB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").Type = 4
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0VrhnPd0m2r12e_1_FePjb3VfQmXARdd_1_KJOB").Offset = 0
App.ActiveDocument.recompute()

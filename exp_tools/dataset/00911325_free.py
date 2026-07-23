import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00911325")
App.ActiveDocument.addObject("PartDesign::Body","Body_FiHGxFxl5HExUXh_0")
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").Label = "Body_FiHGxFxl5HExUXh_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Plane", "plane_Sketch_FiHGxFxl5HExUXh_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiHGxFxl5HExUXh_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("Sketcher::SketchObject","Sketch_FiHGxFxl5HExUXh_0_JGG")
App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiHGxFxl5HExUXh_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-8.00000000000000,0.00000000000000),App.Vector(-37.50000000000000,-8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,-8.00000000000000,0.00000000000000),App.Vector(-37.50000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,8.00000000000000,0.00000000000000),App.Vector(-37.50000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-8.00000000000000,0.00000000000000),App.Vector(37.50000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").addGeometry(Part.LineSegment(App.Vector(42.12098000000000,-20.42229000000000,0.00000000000000),App.Vector(-42.12098000000000,-20.42229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").addGeometry(Part.LineSegment(App.Vector(-42.12098000000000,-20.42229000000000,0.00000000000000),App.Vector(-42.12098000000000,20.42229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").addGeometry(Part.LineSegment(App.Vector(42.12098000000000,20.42229000000000,0.00000000000000),App.Vector(-42.12098000000000,20.42229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").addGeometry(Part.LineSegment(App.Vector(42.12098000000000,-20.42229000000000,0.00000000000000),App.Vector(42.12098000000000,20.42229000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Pad","Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG")
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG")
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").Length = 15.0
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").Type = 0
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").Midplane = 1
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Plane", "plane_Sketch_FiHGxFxl5HExUXh_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiHGxFxl5HExUXh_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("Sketcher::SketchObject","Sketch_FiHGxFxl5HExUXh_0_JGC")
App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiHGxFxl5HExUXh_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-8.00000000000000,0.00000000000000),App.Vector(-37.50000000000000,-8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC").addGeometry(Part.LineSegment(App.Vector(-37.50000000000000,-8.00000000000000,0.00000000000000),App.Vector(-37.50000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,8.00000000000000,0.00000000000000),App.Vector(-37.50000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-8.00000000000000,0.00000000000000),App.Vector(37.50000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Pad","Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC")
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC")
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").Length = 15.0
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiHGxFxl5HExUXh_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FiHGxFxl5HExUXh_0_FXMNIQcMIJsuQJO_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Plane", "plane_Sketch_F7YWbCASFvVTKBE_1_JJC")
origin = App.Vector(-42.12098000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7YWbCASFvVTKBE_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("Sketcher::SketchObject","Sketch_F7YWbCASFvVTKBE_1_JJC")
App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7YWbCASFvVTKBE_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC").addGeometry(Part.LineSegment(App.Vector(8.15000000000000,3.00000000000000,0.00000000000000),App.Vector(-8.15000000000000,3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC").addGeometry(Part.LineSegment(App.Vector(-8.15000000000000,3.00000000000000,0.00000000000000),App.Vector(-8.15000000000000,-3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC").addGeometry(Part.LineSegment(App.Vector(8.15000000000000,-3.00000000000000,0.00000000000000),App.Vector(-8.15000000000000,-3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC").addGeometry(Part.LineSegment(App.Vector(8.15000000000000,3.00000000000000,0.00000000000000),App.Vector(8.15000000000000,-3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Pocket","Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC")
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC")
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").Length = 73.5
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7YWbCASFvVTKBE_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7YWbCASFvVTKBE_1_FeSYfK9opNfKIff_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Plane", "plane_Sketch_F7KDXjkCgknLvy9_1_JNC")
origin = App.Vector(-42.11500000000000,-15.21115000000000,7.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7KDXjkCgknLvy9_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("Sketcher::SketchObject","Sketch_F7KDXjkCgknLvy9_1_JNC")
App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7KDXjkCgknLvy9_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC").addGeometry(Part.LineSegment(App.Vector(-57.02351999999999,5.21115000000000,0.00000000000000),App.Vector(-0.00598000000000,5.21115000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC").addGeometry(Part.LineSegment(App.Vector(-0.00598000000000,5.21115000000000,0.00000000000000),App.Vector(-0.00598000000000,25.21115000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC").addGeometry(Part.LineSegment(App.Vector(-57.02351999999999,25.21115000000000,0.00000000000000),App.Vector(-0.00598000000000,25.21115000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC").addGeometry(Part.LineSegment(App.Vector(-57.02351999999999,5.21115000000000,0.00000000000000),App.Vector(-57.02351999999999,25.21115000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Pad","Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC")
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC")
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").Length = 20.0
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Plane", "plane_Sketch_F7KDXjkCgknLvy9_1_JNG")
origin = App.Vector(-42.11500000000000,-15.21115000000000,7.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7KDXjkCgknLvy9_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("Sketcher::SketchObject","Sketch_F7KDXjkCgknLvy9_1_JNG")
App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7KDXjkCgknLvy9_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG").addGeometry(Part.LineSegment(App.Vector(84.23598000000000,5.21115000000000,0.00000000000000),App.Vector(-0.00598000000000,5.21115000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG").addGeometry(Part.LineSegment(App.Vector(-0.00598000000000,5.21115000000000,0.00000000000000),App.Vector(-0.00598000000000,25.21115000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG").addGeometry(Part.LineSegment(App.Vector(84.23598000000000,25.21115000000000,0.00000000000000),App.Vector(-0.00598000000000,25.21115000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG").addGeometry(Part.LineSegment(App.Vector(84.23598000000000,5.21115000000000,0.00000000000000),App.Vector(84.23598000000000,25.21115000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Pad","Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG")
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG")
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").Length = 20.0
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7KDXjkCgknLvy9_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7KDXjkCgknLvy9_1_Fuz9kXcbZLQRdmm_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Plane", "plane_Sketch_F3udZaSCckibGCz_1_JRC")
origin = App.Vector(-99.13852000000000,0.00000000000000,17.50000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3udZaSCckibGCz_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("Sketcher::SketchObject","Sketch_F3udZaSCckibGCz_1_JRC")
App.ActiveDocument.getObject("Sketch_F3udZaSCckibGCz_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3udZaSCckibGCz_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F3udZaSCckibGCz_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3udZaSCckibGCz_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3udZaSCckibGCz_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3udZaSCckibGCz_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Pocket","Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC")
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F3udZaSCckibGCz_1_JRC")
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").Length = 134.3
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3udZaSCckibGCz_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3udZaSCckibGCz_1_FQX7NumXPochYPD_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Plane", "plane_Sketch_FDIo3jblH7T0A0c_1_JVC")
origin = App.Vector(42.12098000000000,0.00000000000000,10.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDIo3jblH7T0A0c_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("Sketcher::SketchObject","Sketch_FDIo3jblH7T0A0c_1_JVC")
App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDIo3jblH7T0A0c_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVC").addGeometry(Part.LineSegment(App.Vector(-20.42229000000000,-2.50000000000000,0.00000000000000),App.Vector(-10.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,17.50000000000000,0.00000000000000),App.Vector(-10.00000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVC").addGeometry(Part.LineSegment(App.Vector(-20.42229000000000,-2.50000000000000,0.00000000000000),App.Vector(-10.00000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Pad","Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC")
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVC")
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").Length = 84.23
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").Type = 0
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Plane", "plane_Sketch_FDIo3jblH7T0A0c_1_JVG")
origin = App.Vector(42.12098000000000,0.00000000000000,10.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDIo3jblH7T0A0c_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("Sketcher::SketchObject","Sketch_FDIo3jblH7T0A0c_1_JVG")
App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDIo3jblH7T0A0c_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVG").addGeometry(Part.LineSegment(App.Vector(20.42229000000000,-2.50000000000000,0.00000000000000),App.Vector(10.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVG").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,17.50000000000000,0.00000000000000),App.Vector(10.00000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVG").addGeometry(Part.LineSegment(App.Vector(20.42229000000000,-2.50000000000000,0.00000000000000),App.Vector(10.00000000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Pad","Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG")
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVG")
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").Length = 84.23
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDIo3jblH7T0A0c_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").Type = 0
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDIo3jblH7T0A0c_1_FGjQ8mC7hi1U1K2_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Plane", "plane_Sketch_FGULyIeSLEajP9y_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,-7.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGULyIeSLEajP9y_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("Sketcher::SketchObject","Sketch_FGULyIeSLEajP9y_1_JZC")
App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGULyIeSLEajP9y_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC").addGeometry(Part.LineSegment(App.Vector(14.10713000000000,-6.70000000000000,0.00000000000000),App.Vector(21.30713000000000,-6.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC").addGeometry(Part.LineSegment(App.Vector(21.30713000000000,-6.70000000000000,0.00000000000000),App.Vector(21.30713000000000,6.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC").addGeometry(Part.LineSegment(App.Vector(14.10713000000000,6.70000000000000,0.00000000000000),App.Vector(21.30713000000000,6.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC").addGeometry(Part.LineSegment(App.Vector(14.10713000000000,-6.70000000000000,0.00000000000000),App.Vector(14.10713000000000,6.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiHGxFxl5HExUXh_0").newObject("PartDesign::Pocket","Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC")
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC")
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").Length = 31.8
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGULyIeSLEajP9y_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGULyIeSLEajP9y_1_FctWr5IOzNtfTd6_1_JZC").Offset = 0
App.ActiveDocument.recompute()

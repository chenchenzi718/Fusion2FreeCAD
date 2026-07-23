import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00610557")
App.ActiveDocument.addObject("PartDesign::Body","Body_F5WBieiSXpT8AVM_0")
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").Label = "Body_F5WBieiSXpT8AVM_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Plane", "plane_Sketch_F5WBieiSXpT8AVM_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5WBieiSXpT8AVM_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("Sketcher::SketchObject","Sketch_F5WBieiSXpT8AVM_0_JGC")
App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5WBieiSXpT8AVM_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC").addGeometry(Part.LineSegment(App.Vector(-180.88602000000000,75.23179000000000,0.00000000000000),App.Vector(39.11398000000000,75.23179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC").addGeometry(Part.LineSegment(App.Vector(39.11398000000000,75.23179000000000,0.00000000000000),App.Vector(39.11398000000000,-84.76821000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC").addGeometry(Part.LineSegment(App.Vector(-180.88602000000000,-84.76821000000000,0.00000000000000),App.Vector(39.11398000000000,-84.76821000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC").addGeometry(Part.LineSegment(App.Vector(-180.88602000000000,75.23179000000000,0.00000000000000),App.Vector(-180.88602000000000,-84.76821000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Pad","Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC")
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC")
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5WBieiSXpT8AVM_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5WBieiSXpT8AVM_0_FBjZ2rkh8zKiG8Q_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Plane", "plane_Sketch_FMw2rzaEtzryvvc_1_JJC")
origin = App.Vector(-70.88601999999999,-4.76821000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMw2rzaEtzryvvc_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("Sketcher::SketchObject","Sketch_FMw2rzaEtzryvvc_1_JJC")
App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMw2rzaEtzryvvc_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC").addGeometry(Part.LineSegment(App.Vector(83.16376000000000,9.76821000000000,0.00000000000000),App.Vector(-76.83624000000000,9.76821000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-76.83624000000000,4.76821000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC").addGeometry(Part.LineSegment(App.Vector(83.16376000000000,-0.23179000000000,0.00000000000000),App.Vector(-76.83624000000000,-0.23179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC").addGeometry(Part.LineSegment(App.Vector(83.16376000000000,9.76821000000000,0.00000000000000),App.Vector(83.16376000000000,-0.23179000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Pocket","Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC")
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC")
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMw2rzaEtzryvvc_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMw2rzaEtzryvvc_1_F8wgt5WJgJExJDV_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Plane", "plane_Sketch_FXyHbMN8IEnd0tP_1_JNC")
origin = App.Vector(-70.88601999999999,-4.76821000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXyHbMN8IEnd0tP_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("Sketcher::SketchObject","Sketch_FXyHbMN8IEnd0tP_1_JNC")
App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXyHbMN8IEnd0tP_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-8.83624000000001,-2.23179000000000,0.00000000000000),App.Vector(15.16375999999999,-2.23179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC").addGeometry(Part.LineSegment(App.Vector(15.16375999999999,-2.23179000000000,0.00000000000000),App.Vector(15.16375999999999,-7.23179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-8.83624000000001,-7.23179000000000,0.00000000000000),App.Vector(15.16375999999999,-7.23179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-8.83624000000001,-2.23179000000000,0.00000000000000),App.Vector(-8.83624000000001,-7.23179000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Pad","Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC")
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC")
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").Length = 60.0
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Plane", "plane_Sketch_FXyHbMN8IEnd0tP_1_JNG")
origin = App.Vector(-70.88601999999999,-4.76821000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXyHbMN8IEnd0tP_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("Sketcher::SketchObject","Sketch_FXyHbMN8IEnd0tP_1_JNG")
App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXyHbMN8IEnd0tP_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG").addGeometry(Part.LineSegment(App.Vector(15.16375999999999,11.76821000000000,0.00000000000000),App.Vector(15.16375999999999,16.76821000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG").addGeometry(Part.LineSegment(App.Vector(15.16375999999999,16.76821000000000,0.00000000000000),App.Vector(-8.83624000000001,16.76821000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-8.83624000000001,11.76821000000000,0.00000000000000),App.Vector(-8.83624000000001,16.76821000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG").addGeometry(Part.LineSegment(App.Vector(15.16375999999999,11.76821000000000,0.00000000000000),App.Vector(-8.83624000000001,11.76821000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Pad","Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG")
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG")
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").Length = 60.0
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXyHbMN8IEnd0tP_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXyHbMN8IEnd0tP_1_FIgkgFLbLc7ixNh_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Plane", "plane_Sketch_FPXTuQoJ46us2mg_1_JRC")
origin = App.Vector(-67.72226000000001,-12.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPXTuQoJ46us2mg_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("Sketcher::SketchObject","Sketch_FPXTuQoJ46us2mg_1_JRC")
App.ActiveDocument.getObject("Sketch_FPXTuQoJ46us2mg_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPXTuQoJ46us2mg_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FPXTuQoJ46us2mg_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPXTuQoJ46us2mg_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,19.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPXTuQoJ46us2mg_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPXTuQoJ46us2mg_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Pocket","Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC")
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FPXTuQoJ46us2mg_1_JRC")
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPXTuQoJ46us2mg_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPXTuQoJ46us2mg_1_F0gR7WPFMqYAxg1_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Plane", "plane_Sketch_FlJzTOEFETiKaWV_1_JWC")
origin = App.Vector(-70.88601999999999,-4.76821000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlJzTOEFETiKaWV_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("Sketcher::SketchObject","Sketch_FlJzTOEFETiKaWV_1_JWC")
App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlJzTOEFETiKaWV_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC").addGeometry(Part.LineSegment(App.Vector(39.16375999999999,-11.73179000000000,0.00000000000000),App.Vector(63.16376000000000,-11.73179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC").addGeometry(Part.LineSegment(App.Vector(63.16376000000000,-11.73179000000000,0.00000000000000),App.Vector(63.16376000000000,-16.73179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC").addGeometry(Part.LineSegment(App.Vector(39.16375999999999,-16.73179000000000,0.00000000000000),App.Vector(63.16376000000000,-16.73179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC").addGeometry(Part.LineSegment(App.Vector(39.16375999999999,-11.73179000000000,0.00000000000000),App.Vector(39.16375999999999,-16.73179000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Pad","Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC")
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC")
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").Length = 60.0
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Plane", "plane_Sketch_FlJzTOEFETiKaWV_1_JWG")
origin = App.Vector(-70.88601999999999,-4.76821000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlJzTOEFETiKaWV_1_JWG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("Sketcher::SketchObject","Sketch_FlJzTOEFETiKaWV_1_JWG")
App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlJzTOEFETiKaWV_1_JWG"), [""])
App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG").addGeometry(Part.LineSegment(App.Vector(39.16375999999999,-60.23179000000000,0.00000000000000),App.Vector(63.16376000000000,-60.23179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG").addGeometry(Part.LineSegment(App.Vector(63.16376000000000,-60.23179000000000,0.00000000000000),App.Vector(63.16376000000000,-65.23179000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG").addGeometry(Part.LineSegment(App.Vector(39.16375999999999,-65.23179000000002,0.00000000000000),App.Vector(63.16376000000000,-65.23179000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG").addGeometry(Part.LineSegment(App.Vector(39.16375999999999,-60.23179000000000,0.00000000000000),App.Vector(39.16375999999999,-65.23179000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Pad","Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG")
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").Profile = App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG")
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").Length = 60.0
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlJzTOEFETiKaWV_1_JWG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").Type = 4
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlJzTOEFETiKaWV_1_Fiw5d3fHUJQ8qJn_1_JWG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Plane", "plane_Sketch_F1QlbnVdfrGVzf6_1_JaC")
origin = App.Vector(-19.72226000000000,-21.50000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1QlbnVdfrGVzf6_1_JaC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("Sketcher::SketchObject","Sketch_F1QlbnVdfrGVzf6_1_JaC")
App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1QlbnVdfrGVzf6_1_JaC"), [""])
App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").addGeometry(Part.Circle(App.Vector(0.00000000000000,19.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Pocket","Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC")
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").Profile = App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC")
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").Type = 4
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FArpHXRTZgh16Yt_1_JaC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Plane", "plane_Sketch_F1QlbnVdfrGVzf6_1_JaC")
origin = App.Vector(-19.72226000000000,-21.50000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1QlbnVdfrGVzf6_1_JaC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("Sketcher::SketchObject","Sketch_F1QlbnVdfrGVzf6_1_JaC")
App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1QlbnVdfrGVzf6_1_JaC"), [""])
App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").addGeometry(Part.Circle(App.Vector(0.00000000000000,19.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5WBieiSXpT8AVM_0").newObject("PartDesign::Pocket","Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC")
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").Profile = App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC")
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").Length = 100.0
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1QlbnVdfrGVzf6_1_JaC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").Type = 0
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1QlbnVdfrGVzf6_1_FFjR2duXw9qb6qy_1_JaC").Offset = 0
App.ActiveDocument.recompute()

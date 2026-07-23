import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00318206")
App.ActiveDocument.addObject("PartDesign::Body","Body_F0E7jNkCMwxwhm7_0")
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").Label = "Body_F0E7jNkCMwxwhm7_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Plane", "plane_Sketch_F0E7jNkCMwxwhm7_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0E7jNkCMwxwhm7_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("Sketcher::SketchObject","Sketch_F0E7jNkCMwxwhm7_0_JGC")
App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0E7jNkCMwxwhm7_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").addGeometry(Part.LineSegment(App.Vector(3.00000000000000,0.00000000000000,0.00000000000000),App.Vector(282.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(282.00000000000000,-3.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").addGeometry(Part.LineSegment(App.Vector(285.00000000000000,-3.00000000000000,0.00000000000000),App.Vector(285.00000000000000,-148.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(282.00000000000000,-148.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").addGeometry(Part.LineSegment(App.Vector(3.00000000000000,-151.00000000000000,0.00000000000000),App.Vector(282.00000000000000,-151.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(3.00000000000000,-148.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-3.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-148.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(3.00000000000000,-3.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Pad","Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC")
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC")
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0E7jNkCMwxwhm7_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0E7jNkCMwxwhm7_0_FaAHmTedfQNv1FD_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Plane", "plane_Sketch_FItub9pEefrP7nX_1_JJC")
origin = App.Vector(142.50000000000000,-75.50000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("Sketcher::SketchObject","Sketch_FItub9pEefrP7nX_1_JJC")
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJC").addGeometry(Part.Circle(App.Vector(-133.99999999999997,67.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Pocket","Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJC")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Plane", "plane_Sketch_FItub9pEefrP7nX_1_JJW")
origin = App.Vector(142.50000000000000,-75.50000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("Sketcher::SketchObject","Sketch_FItub9pEefrP7nX_1_JJW")
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJW").addGeometry(Part.Circle(App.Vector(-133.99999999999997,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Pocket","Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJW")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").Length = 2.0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Plane", "plane_Sketch_FItub9pEefrP7nX_1_JJS")
origin = App.Vector(142.50000000000000,-75.50000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("Sketcher::SketchObject","Sketch_FItub9pEefrP7nX_1_JJS")
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJS").addGeometry(Part.Circle(App.Vector(-133.99999999999997,-66.99999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Pocket","Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJS")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").Length = 2.0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Plane", "plane_Sketch_FItub9pEefrP7nX_1_JJO")
origin = App.Vector(142.50000000000000,-75.50000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("Sketcher::SketchObject","Sketch_FItub9pEefrP7nX_1_JJO")
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJO").addGeometry(Part.Circle(App.Vector(134.00000000000003,-66.99999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Pocket","Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJO")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").Length = 2.0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Plane", "plane_Sketch_FItub9pEefrP7nX_1_JJK")
origin = App.Vector(142.50000000000000,-75.50000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("Sketcher::SketchObject","Sketch_FItub9pEefrP7nX_1_JJK")
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJK").addGeometry(Part.Circle(App.Vector(134.00000000000003,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Pocket","Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJK")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").Length = 2.0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Plane", "plane_Sketch_FItub9pEefrP7nX_1_JJG")
origin = App.Vector(142.50000000000000,-75.50000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("Sketcher::SketchObject","Sketch_FItub9pEefrP7nX_1_JJG")
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FItub9pEefrP7nX_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJG").addGeometry(Part.Circle(App.Vector(134.00000000000003,67.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Pocket","Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJG")
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").Length = 2.0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FItub9pEefrP7nX_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FItub9pEefrP7nX_1_FxKwTFInx4DVp5r_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Plane", "plane_Sketch_Fm2X9zrN7F6IUxW_1_JNG")
origin = App.Vector(142.50000000000000,-75.50000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fm2X9zrN7F6IUxW_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("Sketcher::SketchObject","Sketch_Fm2X9zrN7F6IUxW_1_JNG")
App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fm2X9zrN7F6IUxW_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNG").addGeometry(Part.Circle(App.Vector(13.50000000000001,12.40000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.52500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Pocket","Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG")
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNG")
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Plane", "plane_Sketch_Fm2X9zrN7F6IUxW_1_JNC")
origin = App.Vector(142.50000000000000,-75.50000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fm2X9zrN7F6IUxW_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("Sketcher::SketchObject","Sketch_Fm2X9zrN7F6IUxW_1_JNC")
App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fm2X9zrN7F6IUxW_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNC").addGeometry(Part.Circle(App.Vector(13.50000000000001,50.49999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.52500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0E7jNkCMwxwhm7_0").newObject("PartDesign::Pocket","Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC")
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNC")
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fm2X9zrN7F6IUxW_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fm2X9zrN7F6IUxW_1_Fiq2tWcXSxZXmvt_1_JNC").Offset = 0
App.ActiveDocument.recompute()

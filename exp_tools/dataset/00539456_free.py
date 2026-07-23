import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00539456")
App.ActiveDocument.addObject("PartDesign::Body","Body_FybsqRizQo7p8bF_0")
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").Label = "Body_FybsqRizQo7p8bF_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_FybsqRizQo7p8bF_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FybsqRizQo7p8bF_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_FybsqRizQo7p8bF_0_JGC")
App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FybsqRizQo7p8bF_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(102.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC").addGeometry(Part.LineSegment(App.Vector(102.00000000000000,0.00000000000000,0.00000000000000),App.Vector(102.00000000000000,145.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,145.00000000000000,0.00000000000000),App.Vector(102.00000000000000,145.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,145.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC")
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC")
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FybsqRizQo7p8bF_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FybsqRizQo7p8bF_0_F70dPHh2joVrD8H_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_Fh4F4yOH4IYQXds_1_JJC")
origin = App.Vector(51.00000000000000,-2.00000000000000,35.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh4F4yOH4IYQXds_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_Fh4F4yOH4IYQXds_1_JJC")
App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh4F4yOH4IYQXds_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC").addGeometry(Part.LineSegment(App.Vector(51.00000000000000,35.00000000000000,0.00000000000000),App.Vector(-51.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC").addGeometry(Part.LineSegment(App.Vector(-51.00000000000000,35.00000000000000,0.00000000000000),App.Vector(-51.00000000000000,52.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC").addGeometry(Part.LineSegment(App.Vector(51.00000000000000,52.99999999999999,0.00000000000000),App.Vector(-51.00000000000000,52.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC").addGeometry(Part.LineSegment(App.Vector(51.00000000000000,35.00000000000000,0.00000000000000),App.Vector(51.00000000000000,52.99999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC")
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC")
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").Length = 62.0
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh4F4yOH4IYQXds_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh4F4yOH4IYQXds_1_FToJvXgcmRiyuG8_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_FDnhiTyshr42Ng2_1_JNG")
origin = App.Vector(51.00000000000000,0.00000000000000,72.50000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDnhiTyshr42Ng2_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_FDnhiTyshr42Ng2_1_JNG")
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDnhiTyshr42Ng2_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNG").addGeometry(Part.Circle(App.Vector(-46.00000000000001,67.50000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG")
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNG")
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").Length = 12.0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_FDnhiTyshr42Ng2_1_JNK")
origin = App.Vector(51.00000000000000,0.00000000000000,72.50000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDnhiTyshr42Ng2_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_FDnhiTyshr42Ng2_1_JNK")
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDnhiTyshr42Ng2_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNK").addGeometry(Part.Circle(App.Vector(46.00000000000000,67.50000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK")
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNK")
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").Length = 12.0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_FDnhiTyshr42Ng2_1_JNO")
origin = App.Vector(51.00000000000000,0.00000000000000,72.50000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDnhiTyshr42Ng2_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_FDnhiTyshr42Ng2_1_JNO")
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDnhiTyshr42Ng2_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNO").addGeometry(Part.Circle(App.Vector(46.00000000000000,-67.49999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO")
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNO")
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").Length = 12.0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_FDnhiTyshr42Ng2_1_JNC")
origin = App.Vector(51.00000000000000,0.00000000000000,72.50000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDnhiTyshr42Ng2_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_FDnhiTyshr42Ng2_1_JNC")
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDnhiTyshr42Ng2_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNC").addGeometry(Part.Circle(App.Vector(-46.00000000000001,-67.49999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC")
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNC")
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDnhiTyshr42Ng2_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDnhiTyshr42Ng2_1_F8DjAvLjROHBJ4h_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_Ffvl7rY8eXVNfBI_1_JRC")
origin = App.Vector(51.00000000000000,-2.00000000000000,116.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ffvl7rY8eXVNfBI_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_Ffvl7rY8eXVNfBI_1_JRC")
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ffvl7rY8eXVNfBI_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRC").addGeometry(Part.Circle(App.Vector(-39.40470999999999,-14.22880000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),9.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC")
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRC")
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").Length = 31.0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_Ffvl7rY8eXVNfBI_1_JRG")
origin = App.Vector(51.00000000000000,-2.00000000000000,116.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ffvl7rY8eXVNfBI_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_Ffvl7rY8eXVNfBI_1_JRG")
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ffvl7rY8eXVNfBI_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRG").addGeometry(Part.Circle(App.Vector(-10.84110999999999,-9.11368000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),9.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG")
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRG")
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").Length = 31.0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_Ffvl7rY8eXVNfBI_1_JRK")
origin = App.Vector(51.00000000000000,-2.00000000000000,116.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ffvl7rY8eXVNfBI_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_Ffvl7rY8eXVNfBI_1_JRK")
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ffvl7rY8eXVNfBI_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRK").addGeometry(Part.Circle(App.Vector(7.71741000000000,-13.30344000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),9.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK")
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRK")
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").Length = 31.0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Plane", "plane_Sketch_Ffvl7rY8eXVNfBI_1_JRO")
origin = App.Vector(51.00000000000000,-2.00000000000000,116.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ffvl7rY8eXVNfBI_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("Sketcher::SketchObject","Sketch_Ffvl7rY8eXVNfBI_1_JRO")
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ffvl7rY8eXVNfBI_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRO").addGeometry(Part.Circle(App.Vector(41.05513999999999,-10.67203000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),9.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FybsqRizQo7p8bF_0").newObject("PartDesign::Pad","Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO")
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRO")
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").Length = 31.0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ffvl7rY8eXVNfBI_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ffvl7rY8eXVNfBI_1_F9GcChDWMDsdysX_1_JRO").Offset = 0
App.ActiveDocument.recompute()

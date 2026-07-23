import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00193665")
App.ActiveDocument.addObject("PartDesign::Body","Body_F39M013ED00BXmf_0")
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").Label = "Body_F39M013ED00BXmf_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_F39M013ED00BXmf_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F39M013ED00BXmf_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_F39M013ED00BXmf_0_JGC")
App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F39M013ED00BXmf_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC").addGeometry(Part.LineSegment(App.Vector(76.20000000000000,101.59999999999999,0.00000000000000),App.Vector(-76.20000000000000,101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,101.59999999999999,0.00000000000000),App.Vector(-76.20000000000000,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC").addGeometry(Part.LineSegment(App.Vector(76.20000000000000,-101.59999999999999,0.00000000000000),App.Vector(-76.20000000000000,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC").addGeometry(Part.LineSegment(App.Vector(76.20000000000000,101.59999999999999,0.00000000000000),App.Vector(76.20000000000000,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pad","Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC")
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC")
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F39M013ED00BXmf_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F39M013ED00BXmf_0_FzGtLBWkbQ8NUgV_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_FsI185ZoeM7kNm2_1_JNC")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsI185ZoeM7kNm2_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_FsI185ZoeM7kNm2_1_JNC")
App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsI185ZoeM7kNm2_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNC").addGeometry(Part.Circle(App.Vector(-64.64465000000000,79.63106000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pocket","Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC")
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").Profile = App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNC")
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_FsI185ZoeM7kNm2_1_JNG")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsI185ZoeM7kNm2_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_FsI185ZoeM7kNm2_1_JNG")
App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsI185ZoeM7kNm2_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNG").addGeometry(Part.Circle(App.Vector(-64.56748000000000,72.93249999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.15000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pocket","Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG")
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").Profile = App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNG")
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsI185ZoeM7kNm2_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsI185ZoeM7kNm2_1_FBxqrLxeJMTSclS_2_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_FIIBngFJS0nKIQp_1_JPC")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIIBngFJS0nKIQp_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_FIIBngFJS0nKIQp_1_JPC")
App.ActiveDocument.getObject("Sketch_FIIBngFJS0nKIQp_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIIBngFJS0nKIQp_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FIIBngFJS0nKIQp_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIIBngFJS0nKIQp_1_JPC").addGeometry(Part.Circle(App.Vector(-64.86683000000001,72.63315000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIIBngFJS0nKIQp_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIIBngFJS0nKIQp_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pocket","Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC")
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").Profile = App.ActiveDocument.getObject("Sketch_FIIBngFJS0nKIQp_1_JPC")
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIIBngFJS0nKIQp_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIIBngFJS0nKIQp_1_FqsE77suUE2hkPF_2_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_FYIFtG9CvHtylUz_2_JYC")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYIFtG9CvHtylUz_2_JYC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_FYIFtG9CvHtylUz_2_JYC")
App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYIFtG9CvHtylUz_2_JYC"), [""])
App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYC").addGeometry(Part.Circle(App.Vector(62.73730000000000,82.70856000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pocket","Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC")
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").Profile = App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYC")
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").Type = 4
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_FYIFtG9CvHtylUz_2_JYG")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYIFtG9CvHtylUz_2_JYG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_FYIFtG9CvHtylUz_2_JYG")
App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYIFtG9CvHtylUz_2_JYG"), [""])
App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYG").addGeometry(Part.Circle(App.Vector(62.79693000000000,75.01027000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pocket","Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG")
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").Profile = App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYG")
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYIFtG9CvHtylUz_2_JYG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").Type = 4
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYIFtG9CvHtylUz_2_F1whiJnyUFxt94r_2_JYG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_FyohCHLB6zmjWBB_2_JeC")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyohCHLB6zmjWBB_2_JeC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_FyohCHLB6zmjWBB_2_JeC")
App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyohCHLB6zmjWBB_2_JeC"), [""])
App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeC").addGeometry(Part.Circle(App.Vector(-63.81985000000000,-77.53820999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pocket","Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC")
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").Profile = App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeC")
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").Type = 4
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_FyohCHLB6zmjWBB_2_JeG")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyohCHLB6zmjWBB_2_JeG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_FyohCHLB6zmjWBB_2_JeG")
App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyohCHLB6zmjWBB_2_JeG"), [""])
App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeG").addGeometry(Part.Circle(App.Vector(-64.11967000000000,-83.98429000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pocket","Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG")
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").Profile = App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeG")
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyohCHLB6zmjWBB_2_JeG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").Type = 4
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyohCHLB6zmjWBB_2_FUzcL5G0wHgYQ8a_2_JeG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_FXVEQVfvlSRd5RZ_2_JkC")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXVEQVfvlSRd5RZ_2_JkC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_FXVEQVfvlSRd5RZ_2_JkC")
App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXVEQVfvlSRd5RZ_2_JkC"), [""])
App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkC").addGeometry(Part.Circle(App.Vector(64.74137000000000,-75.92073000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pocket","Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC")
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").Profile = App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkC")
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").Type = 4
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Plane", "plane_Sketch_FXVEQVfvlSRd5RZ_2_JkG")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXVEQVfvlSRd5RZ_2_JkG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("Sketcher::SketchObject","Sketch_FXVEQVfvlSRd5RZ_2_JkG")
App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXVEQVfvlSRd5RZ_2_JkG"), [""])
App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkG").addGeometry(Part.Circle(App.Vector(64.95336999999999,-82.70482000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F39M013ED00BXmf_0").newObject("PartDesign::Pocket","Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG")
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").Profile = App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkG")
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXVEQVfvlSRd5RZ_2_JkG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").Type = 4
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXVEQVfvlSRd5RZ_2_FxmcXJ1TZFsZGwB_2_JkG").Offset = 0
App.ActiveDocument.recompute()

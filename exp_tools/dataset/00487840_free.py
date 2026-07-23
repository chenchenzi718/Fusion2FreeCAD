import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00487840")
App.ActiveDocument.addObject("PartDesign::Body","Body_FXLoCLyhm9zRz8X_0")
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").Label = "Body_FXLoCLyhm9zRz8X_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Plane", "plane_Sketch_FXLoCLyhm9zRz8X_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXLoCLyhm9zRz8X_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("Sketcher::SketchObject","Sketch_FXLoCLyhm9zRz8X_0_JGC")
App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXLoCLyhm9zRz8X_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC").addGeometry(Part.LineSegment(App.Vector(-42.50000000000000,60.00000000000000,0.00000000000000),App.Vector(42.50000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC").addGeometry(Part.LineSegment(App.Vector(42.50000000000000,60.00000000000000,0.00000000000000),App.Vector(42.50000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC").addGeometry(Part.LineSegment(App.Vector(-42.50000000000000,-60.00000000000000,0.00000000000000),App.Vector(42.50000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC").addGeometry(Part.LineSegment(App.Vector(-42.50000000000000,60.00000000000000,0.00000000000000),App.Vector(-42.50000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Pad","Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC")
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC")
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").Length = 8.75
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXLoCLyhm9zRz8X_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXLoCLyhm9zRz8X_0_FxRLQkuIXg5SMQc_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Plane", "plane_Sketch_ForxfyVuO2BGHXd_1_JJC")
origin = App.Vector(-26.25000000000000,-0.00000000000000,8.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_ForxfyVuO2BGHXd_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("Sketcher::SketchObject","Sketch_ForxfyVuO2BGHXd_1_JJC")
App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_ForxfyVuO2BGHXd_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC").addGeometry(Part.LineSegment(App.Vector(-14.25000000000000,60.00000000000000,0.00000000000000),App.Vector(66.75000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC").addGeometry(Part.LineSegment(App.Vector(66.75000000000000,60.00000000000000,0.00000000000000),App.Vector(66.75000000000000,-58.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC").addGeometry(Part.LineSegment(App.Vector(-14.25000000000000,-58.00000000000000,0.00000000000000),App.Vector(66.75000000000000,-58.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC").addGeometry(Part.LineSegment(App.Vector(-14.25000000000000,60.00000000000000,0.00000000000000),App.Vector(-14.25000000000000,-58.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Pocket","Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC")
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC")
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").Length = 6.75
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_ForxfyVuO2BGHXd_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_ForxfyVuO2BGHXd_1_FFZlqEU1oesPAT5_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Plane", "plane_Sketch_F0qdCmCoTy7IgMN_1_JNC")
origin = App.Vector(-26.25000000000000,-0.00000000000000,8.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0qdCmCoTy7IgMN_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("Sketcher::SketchObject","Sketch_F0qdCmCoTy7IgMN_1_JNC")
App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0qdCmCoTy7IgMN_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC").addGeometry(Part.LineSegment(App.Vector(16.25000000000000,-10.00000000000000,0.00000000000000),App.Vector(16.25000000000000,-58.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC").addGeometry(Part.LineSegment(App.Vector(16.25000000000000,-58.00000000000000,0.00000000000000),App.Vector(36.25000000000000,-58.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC").addGeometry(Part.LineSegment(App.Vector(36.25000000000000,-10.00000000000000,0.00000000000000),App.Vector(36.25000000000000,-58.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(26.25000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Pocket","Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC")
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC")
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Plane", "plane_Sketch_F0qdCmCoTy7IgMN_1_JNG")
origin = App.Vector(-26.25000000000000,-0.00000000000000,8.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0qdCmCoTy7IgMN_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("Sketcher::SketchObject","Sketch_F0qdCmCoTy7IgMN_1_JNG")
App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0qdCmCoTy7IgMN_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG").addGeometry(Part.LineSegment(App.Vector(16.25000000000000,-60.00000000000000,0.00000000000000),App.Vector(36.25000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG").addGeometry(Part.LineSegment(App.Vector(36.25000000000000,-60.00000000000000,0.00000000000000),App.Vector(36.25000000000000,-58.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG").addGeometry(Part.LineSegment(App.Vector(16.25000000000000,-58.00000000000000,0.00000000000000),App.Vector(36.25000000000000,-58.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG").addGeometry(Part.LineSegment(App.Vector(16.25000000000000,-60.00000000000000,0.00000000000000),App.Vector(16.25000000000000,-58.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Pocket","Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG")
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG")
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0qdCmCoTy7IgMN_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0qdCmCoTy7IgMN_1_FLtpypVt7zKRBgh_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Plane", "plane_Sketch_FOZkmdbfyXGytLu_1_JRC")
origin = App.Vector(-26.25000000000000,-0.00000000000000,8.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOZkmdbfyXGytLu_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("Sketcher::SketchObject","Sketch_FOZkmdbfyXGytLu_1_JRC")
App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOZkmdbfyXGytLu_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC").addGeometry(Part.LineSegment(App.Vector(-14.25000000000000,45.00000000000000,0.00000000000000),App.Vector(-15.25000000000000,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC").addGeometry(Part.LineSegment(App.Vector(-15.25000000000000,45.00000000000000,0.00000000000000),App.Vector(-15.25000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC").addGeometry(Part.LineSegment(App.Vector(-14.25000000000000,35.00000000000000,0.00000000000000),App.Vector(-15.25000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC").addGeometry(Part.LineSegment(App.Vector(-14.25000000000000,45.00000000000000,0.00000000000000),App.Vector(-14.25000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Pocket","Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC")
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC")
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").Length = 6.75
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOZkmdbfyXGytLu_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOZkmdbfyXGytLu_1_FauPmDxJvVgtCtO_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Plane", "plane_Sketch_FOQrMvwsO8ubOEK_1_JVC")
origin = App.Vector(26.25000000000000,0.00000000000000,8.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOQrMvwsO8ubOEK_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("Sketcher::SketchObject","Sketch_FOQrMvwsO8ubOEK_1_JVC")
App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOQrMvwsO8ubOEK_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC").addGeometry(Part.LineSegment(App.Vector(14.25000000000000,-35.00000000000000,0.00000000000000),App.Vector(15.25000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC").addGeometry(Part.LineSegment(App.Vector(15.25000000000000,-35.00000000000000,0.00000000000000),App.Vector(15.25000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC").addGeometry(Part.LineSegment(App.Vector(14.25000000000000,-45.00000000000000,0.00000000000000),App.Vector(15.25000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC").addGeometry(Part.LineSegment(App.Vector(14.25000000000000,-35.00000000000000,0.00000000000000),App.Vector(14.25000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Pocket","Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC")
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC")
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").Length = 6.75
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOQrMvwsO8ubOEK_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOQrMvwsO8ubOEK_1_FxDCkIY4ZS917uE_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Plane", "plane_Sketch_FrFcshKSr0sV3Gl_1_JZC")
origin = App.Vector(-26.25000000000000,-0.00000000000000,8.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrFcshKSr0sV3Gl_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("Sketcher::SketchObject","Sketch_FrFcshKSr0sV3Gl_1_JZC")
App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrFcshKSr0sV3Gl_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC").addGeometry(Part.LineSegment(App.Vector(-14.25000000000000,-45.00000000000000,0.00000000000000),App.Vector(-15.25000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC").addGeometry(Part.LineSegment(App.Vector(-15.25000000000000,-45.00000000000000,0.00000000000000),App.Vector(-15.25000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC").addGeometry(Part.LineSegment(App.Vector(-14.25000000000000,-35.00000000000000,0.00000000000000),App.Vector(-15.25000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC").addGeometry(Part.LineSegment(App.Vector(-14.25000000000000,-45.00000000000000,0.00000000000000),App.Vector(-14.25000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Pad","Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC")
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC")
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").Length = 6.75
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrFcshKSr0sV3Gl_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrFcshKSr0sV3Gl_1_F7xZbKSUyVZ9rQm_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Plane", "plane_Sketch_FZSESkhkpLX8H0F_1_JdC")
origin = App.Vector(26.25000000000000,0.00000000000000,8.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZSESkhkpLX8H0F_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("Sketcher::SketchObject","Sketch_FZSESkhkpLX8H0F_1_JdC")
App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZSESkhkpLX8H0F_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC").addGeometry(Part.LineSegment(App.Vector(14.25000000000000,45.00000000000000,0.00000000000000),App.Vector(15.25000000000000,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC").addGeometry(Part.LineSegment(App.Vector(15.25000000000000,45.00000000000000,0.00000000000000),App.Vector(15.25000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC").addGeometry(Part.LineSegment(App.Vector(14.25000000000000,35.00000000000000,0.00000000000000),App.Vector(15.25000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC").addGeometry(Part.LineSegment(App.Vector(14.25000000000000,45.00000000000000,0.00000000000000),App.Vector(14.25000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXLoCLyhm9zRz8X_0").newObject("PartDesign::Pad","Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC")
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC")
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").Length = 6.75
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZSESkhkpLX8H0F_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZSESkhkpLX8H0F_1_FdtmUxAa9XBFaIL_1_JdC").Offset = 0
App.ActiveDocument.recompute()

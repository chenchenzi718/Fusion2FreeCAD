import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00589485")
App.ActiveDocument.addObject("PartDesign::Body","Body_FtFI9n5le5p65Mv_0")
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").Label = "Body_FtFI9n5le5p65Mv_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Plane", "plane_Sketch_FtFI9n5le5p65Mv_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtFI9n5le5p65Mv_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("Sketcher::SketchObject","Sketch_FtFI9n5le5p65Mv_0_JGC")
App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtFI9n5le5p65Mv_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-1000.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1000.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-1000.00000000000000,530.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,530.00000000000000,0.00000000000000),App.Vector(-1000.00000000000000,530.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,530.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Pad","Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC")
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC")
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtFI9n5le5p65Mv_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtFI9n5le5p65Mv_0_Fx30FqNPp4EFZJ3_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Plane", "plane_Sketch_FUVQnbhcSUAgDHW_1_JJC")
origin = App.Vector(-500.00000000000000,265.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUVQnbhcSUAgDHW_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("Sketcher::SketchObject","Sketch_FUVQnbhcSUAgDHW_1_JJC")
App.ActiveDocument.getObject("Sketch_FUVQnbhcSUAgDHW_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUVQnbhcSUAgDHW_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FUVQnbhcSUAgDHW_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUVQnbhcSUAgDHW_1_JJC").addGeometry(Part.Circle(App.Vector(300.00000000000000,-135.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUVQnbhcSUAgDHW_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUVQnbhcSUAgDHW_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Pocket","Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC")
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FUVQnbhcSUAgDHW_1_JJC")
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUVQnbhcSUAgDHW_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUVQnbhcSUAgDHW_1_FVh1vpgX7OB9YvW_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Plane", "plane_Sketch_F5NxVwJnOW3Y4C4_1_JNC")
origin = App.Vector(-500.00000000000000,265.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5NxVwJnOW3Y4C4_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("Sketcher::SketchObject","Sketch_F5NxVwJnOW3Y4C4_1_JNC")
App.ActiveDocument.getObject("Sketch_F5NxVwJnOW3Y4C4_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5NxVwJnOW3Y4C4_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F5NxVwJnOW3Y4C4_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5NxVwJnOW3Y4C4_1_JNC").addGeometry(Part.Circle(App.Vector(-300.00000000000006,-135.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5NxVwJnOW3Y4C4_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5NxVwJnOW3Y4C4_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Pocket","Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC")
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F5NxVwJnOW3Y4C4_1_JNC")
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").Length = 12.0
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5NxVwJnOW3Y4C4_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5NxVwJnOW3Y4C4_1_FirWIkXfqBVNlf7_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Plane", "plane_Sketch_F80VuiRbDCQqASZ_1_JRG")
origin = App.Vector(-500.00000000000000,265.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F80VuiRbDCQqASZ_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("Sketcher::SketchObject","Sketch_F80VuiRbDCQqASZ_1_JRG")
App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F80VuiRbDCQqASZ_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRG").addGeometry(Part.Circle(App.Vector(300.00000000000000,135.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Pocket","Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG")
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRG")
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").Length = 12.0
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Plane", "plane_Sketch_F80VuiRbDCQqASZ_1_JRC")
origin = App.Vector(-500.00000000000000,265.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F80VuiRbDCQqASZ_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("Sketcher::SketchObject","Sketch_F80VuiRbDCQqASZ_1_JRC")
App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F80VuiRbDCQqASZ_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRC").addGeometry(Part.Circle(App.Vector(-300.00000000000006,135.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Pocket","Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC")
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRC")
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").Length = 12.0
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F80VuiRbDCQqASZ_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F80VuiRbDCQqASZ_1_FIiMAIN0RmwUbMo_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Plane", "plane_Sketch_Fu6NF6SgwpQQLnm_1_JXC")
origin = App.Vector(-500.00000000000000,265.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu6NF6SgwpQQLnm_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("Sketcher::SketchObject","Sketch_Fu6NF6SgwpQQLnm_1_JXC")
App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu6NF6SgwpQQLnm_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JXC").addGeometry(Part.Circle(App.Vector(-485.00000000000000,-135.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Pocket","Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC")
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JXC")
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").Length = 12.0
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Plane", "plane_Sketch_Fu6NF6SgwpQQLnm_1_JVC")
origin = App.Vector(-500.00000000000000,265.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu6NF6SgwpQQLnm_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("Sketcher::SketchObject","Sketch_Fu6NF6SgwpQQLnm_1_JVC")
App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu6NF6SgwpQQLnm_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JVC").addGeometry(Part.Circle(App.Vector(-485.00000000000000,135.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Pocket","Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC")
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JVC")
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").Length = 12.0
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu6NF6SgwpQQLnm_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu6NF6SgwpQQLnm_1_FCRhDwGQovrjURd_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Plane", "plane_Sketch_F76D8uCGWb90rBS_1_JbC")
origin = App.Vector(-500.00000000000000,265.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F76D8uCGWb90rBS_1_JbC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("Sketcher::SketchObject","Sketch_F76D8uCGWb90rBS_1_JbC")
App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F76D8uCGWb90rBS_1_JbC"), [""])
App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbC").addGeometry(Part.Circle(App.Vector(485.00000000000000,135.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Pocket","Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC")
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").Profile = App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbC")
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").Length = 12.0
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").Type = 4
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Plane", "plane_Sketch_F76D8uCGWb90rBS_1_JbG")
origin = App.Vector(-500.00000000000000,265.00000000000000,30.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F76D8uCGWb90rBS_1_JbG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("Sketcher::SketchObject","Sketch_F76D8uCGWb90rBS_1_JbG")
App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F76D8uCGWb90rBS_1_JbG"), [""])
App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbG").addGeometry(Part.Circle(App.Vector(485.00000000000000,-135.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FtFI9n5le5p65Mv_0").newObject("PartDesign::Pocket","Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG")
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").Profile = App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbG")
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").Length = 12.0
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F76D8uCGWb90rBS_1_JbG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").Type = 4
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F76D8uCGWb90rBS_1_FLmJKru5yRUFz3y_1_JbG").Offset = 0
App.ActiveDocument.recompute()

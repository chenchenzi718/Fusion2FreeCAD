import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00196428")
App.ActiveDocument.addObject("PartDesign::Body","Body_FglNFq84tYgQw1Q_0")
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").Label = "Body_FglNFq84tYgQw1Q_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FglNFq84tYgQw1Q_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FglNFq84tYgQw1Q_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("Sketcher::SketchObject","Sketch_FglNFq84tYgQw1Q_0_JGK")
App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FglNFq84tYgQw1Q_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").addGeometry(Part.LineSegment(App.Vector(64.50000000000000,22.50000000000000,0.00000000000000),App.Vector(-64.50000000000000,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-64.50000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),22.50000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").addGeometry(Part.LineSegment(App.Vector(64.50000000000000,-22.50000000000000,0.00000000000000),App.Vector(-64.50000000000000,-22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(64.50000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),22.50000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").addGeometry(Part.Circle(App.Vector(64.50000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").addGeometry(Part.Circle(App.Vector(-64.50000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Pad","Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK")
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK")
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").Length = 2.0
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FglNFq84tYgQw1Q_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FglNFq84tYgQw1Q_0_FW0IqVCouGkKcZE_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Plane", "plane_Sketch_F5H5fjpVpwNS1MD_1_JJK")
origin = App.Vector(0.52200000000000,-2.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5H5fjpVpwNS1MD_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("Sketcher::SketchObject","Sketch_F5H5fjpVpwNS1MD_1_JJK")
App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5H5fjpVpwNS1MD_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJK").addGeometry(Part.LineSegment(App.Vector(-65.02199999999999,-22.50000000000000,0.00000000000000),App.Vector(-87.52199999999999,-22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJK").addGeometry(Part.LineSegment(App.Vector(-87.52199999999999,-22.50000000000000,0.00000000000000),App.Vector(-87.52199999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-65.02199999999999,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),22.50000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Pad","Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK")
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJK")
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").Length = 2.0
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Plane", "plane_Sketch_F5H5fjpVpwNS1MD_1_JJO")
origin = App.Vector(0.52200000000000,-2.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5H5fjpVpwNS1MD_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("Sketcher::SketchObject","Sketch_F5H5fjpVpwNS1MD_1_JJO")
App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5H5fjpVpwNS1MD_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").addGeometry(Part.LineSegment(App.Vector(-87.52199999999999,0.00000000000000,0.00000000000000),App.Vector(-81.39918999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").addGeometry(Part.LineSegment(App.Vector(-81.39918999999999,0.00000000000000,0.00000000000000),App.Vector(-78.79024000000000,-9.46308000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").addGeometry(Part.LineSegment(App.Vector(-78.79024000000000,-9.46308000000000,0.00000000000000),App.Vector(-71.07025999999999,-14.76173000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").addGeometry(Part.LineSegment(App.Vector(-71.07025999999999,-14.76173000000000,0.00000000000000),App.Vector(-65.02199999999999,-17.43136000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").addGeometry(Part.LineSegment(App.Vector(-65.02199999999999,-22.50000000000000,0.00000000000000),App.Vector(-65.02199999999999,-17.43136000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-65.02199999999999,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),22.50000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Pad","Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO")
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO")
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").Length = 2.0
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5H5fjpVpwNS1MD_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").Type = 0
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").Reversed = 1
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5H5fjpVpwNS1MD_1_FFEzTE6kJYh85gp_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FpgIvhbShttXgzH_1_JNC")
origin = App.Vector(0.52200000000000,-2.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpgIvhbShttXgzH_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("Sketcher::SketchObject","Sketch_FpgIvhbShttXgzH_1_JNC")
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpgIvhbShttXgzH_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNC").addGeometry(Part.Circle(App.Vector(-54.02200000000000,16.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Pocket","Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC")
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNC")
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FpgIvhbShttXgzH_1_JNG")
origin = App.Vector(0.52200000000000,-2.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpgIvhbShttXgzH_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("Sketcher::SketchObject","Sketch_FpgIvhbShttXgzH_1_JNG")
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpgIvhbShttXgzH_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNG").addGeometry(Part.Circle(App.Vector(-54.02200000000000,-9.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Pocket","Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG")
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNG")
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FpgIvhbShttXgzH_1_JNK")
origin = App.Vector(0.52200000000000,-2.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpgIvhbShttXgzH_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("Sketcher::SketchObject","Sketch_FpgIvhbShttXgzH_1_JNK")
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpgIvhbShttXgzH_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNK").addGeometry(Part.Circle(App.Vector(52.97799999999999,16.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Pocket","Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK")
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNK")
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FpgIvhbShttXgzH_1_JNO")
origin = App.Vector(0.52200000000000,-2.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpgIvhbShttXgzH_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("Sketcher::SketchObject","Sketch_FpgIvhbShttXgzH_1_JNO")
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpgIvhbShttXgzH_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNO").addGeometry(Part.Circle(App.Vector(52.97799999999999,-9.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Pocket","Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO")
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNO")
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpgIvhbShttXgzH_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpgIvhbShttXgzH_1_FVAcxgl37h20NpI_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FrPoRcKpg8uuB65_1_JRa")
origin = App.Vector(0.52200000000000,-2.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrPoRcKpg8uuB65_1_JRa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("Sketcher::SketchObject","Sketch_FrPoRcKpg8uuB65_1_JRa")
App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrPoRcKpg8uuB65_1_JRa"), [""])
App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa").addGeometry(Part.LineSegment(App.Vector(41.47800000000000,36.50000000000000,0.00000000000000),App.Vector(-42.52200000000001,36.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa").addGeometry(Part.LineSegment(App.Vector(-42.52200000000001,36.50000000000000,0.00000000000000),App.Vector(-42.52200000000001,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa").addGeometry(Part.LineSegment(App.Vector(41.47800000000000,22.50000000000000,0.00000000000000),App.Vector(-42.52200000000001,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa").addGeometry(Part.LineSegment(App.Vector(41.47800000000000,36.50000000000000,0.00000000000000),App.Vector(41.47800000000000,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Pocket","Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa")
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").Profile = App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa")
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").Length = 25.0
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").Type = 4
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FrPoRcKpg8uuB65_1_JRe")
origin = App.Vector(0.52200000000000,-2.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrPoRcKpg8uuB65_1_JRe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("Sketcher::SketchObject","Sketch_FrPoRcKpg8uuB65_1_JRe")
App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrPoRcKpg8uuB65_1_JRe"), [""])
App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe").addGeometry(Part.LineSegment(App.Vector(41.47800000000000,8.50000000000000,0.00000000000000),App.Vector(-42.52200000000001,8.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe").addGeometry(Part.LineSegment(App.Vector(-42.52200000000001,8.50000000000000,0.00000000000000),App.Vector(-42.52200000000001,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe").addGeometry(Part.LineSegment(App.Vector(41.47800000000000,22.50000000000000,0.00000000000000),App.Vector(-42.52200000000001,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe").addGeometry(Part.LineSegment(App.Vector(41.47800000000000,8.50000000000000,0.00000000000000),App.Vector(41.47800000000000,22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FglNFq84tYgQw1Q_0").newObject("PartDesign::Pocket","Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe")
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").Profile = App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe")
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").Length = 25.0
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrPoRcKpg8uuB65_1_JRe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").Type = 4
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrPoRcKpg8uuB65_1_FixpMGRBVbZvjOJ_1_JRe").Offset = 0
App.ActiveDocument.recompute()

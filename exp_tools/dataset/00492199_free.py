import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00492199")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fa0nMAPcnrDl1V0_0")
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").Label = "Body_Fa0nMAPcnrDl1V0_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Plane", "plane_Sketch_Fa0nMAPcnrDl1V0_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa0nMAPcnrDl1V0_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("Sketcher::SketchObject","Sketch_Fa0nMAPcnrDl1V0_0_JGC")
App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa0nMAPcnrDl1V0_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(60.00000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(60.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,12.50000000000000,0.00000000000000),App.Vector(30.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,12.50000000000000,0.00000000000000),App.Vector(30.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,12.50000000000000,0.00000000000000),App.Vector(-30.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(-60.00000000000000,12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Pad","Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC")
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC")
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").Length = 50.0
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa0nMAPcnrDl1V0_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa0nMAPcnrDl1V0_0_F0TAeO8GYEhLpg6_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Plane", "plane_Sketch_FVXwRMBSQvg0jNx_1_JJC")
origin = App.Vector(-0.00000000000000,-50.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVXwRMBSQvg0jNx_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("Sketcher::SketchObject","Sketch_FVXwRMBSQvg0jNx_1_JJC")
App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVXwRMBSQvg0jNx_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),18.00000000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJC").addGeometry(Part.LineSegment(App.Vector(-18.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(18.00000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Pocket","Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC")
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJC")
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").Length = 60.0
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Plane", "plane_Sketch_FVXwRMBSQvg0jNx_1_JJG")
origin = App.Vector(-0.00000000000000,-50.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVXwRMBSQvg0jNx_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("Sketcher::SketchObject","Sketch_FVXwRMBSQvg0jNx_1_JJG")
App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVXwRMBSQvg0jNx_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),18.00000000000000),0.0,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJG").addGeometry(Part.LineSegment(App.Vector(-18.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(18.00000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Pocket","Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG")
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJG")
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").Length = 60.0
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVXwRMBSQvg0jNx_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVXwRMBSQvg0jNx_1_FXVnfbGUzsRPUTd_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Plane", "plane_Sketch_FKWVc1epFNInB4T_1_JNC")
origin = App.Vector(-30.00000000000000,-25.00000000000000,12.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKWVc1epFNInB4T_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("Sketcher::SketchObject","Sketch_FKWVc1epFNInB4T_1_JNC")
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKWVc1epFNInB4T_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,-13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,13.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Pocket","Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC")
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC")
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Plane", "plane_Sketch_FKWVc1epFNInB4T_1_JNG")
origin = App.Vector(-30.00000000000000,-25.00000000000000,12.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKWVc1epFNInB4T_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("Sketcher::SketchObject","Sketch_FKWVc1epFNInB4T_1_JNG")
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKWVc1epFNInB4T_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG").addGeometry(Part.LineSegment(App.Vector(110.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(90.00000000000000,-13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG").addGeometry(Part.LineSegment(App.Vector(90.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(90.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG").addGeometry(Part.LineSegment(App.Vector(110.00000000000000,13.00000000000000,0.00000000000000),App.Vector(90.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG").addGeometry(Part.LineSegment(App.Vector(110.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(110.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Pocket","Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG")
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG")
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Plane", "plane_Sketch_FKWVc1epFNInB4T_1_JNK")
origin = App.Vector(-30.00000000000000,-25.00000000000000,12.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKWVc1epFNInB4T_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("Sketcher::SketchObject","Sketch_FKWVc1epFNInB4T_1_JNK")
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKWVc1epFNInB4T_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,-13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,13.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Pocket","Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK")
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK")
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Plane", "plane_Sketch_FKWVc1epFNInB4T_1_JNO")
origin = App.Vector(-30.00000000000000,-25.00000000000000,12.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKWVc1epFNInB4T_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("Sketcher::SketchObject","Sketch_FKWVc1epFNInB4T_1_JNO")
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKWVc1epFNInB4T_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(90.00000000000000,-13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO").addGeometry(Part.LineSegment(App.Vector(90.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(90.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,13.00000000000000,0.00000000000000),App.Vector(90.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,-13.00000000000000,0.00000000000000),App.Vector(70.00000000000000,13.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Pocket","Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO")
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO")
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKWVc1epFNInB4T_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKWVc1epFNInB4T_1_FBfDLdjzP3XYJOL_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Plane", "plane_Sketch_FpP0zs1pRofzQ7o_1_JRC")
origin = App.Vector(-30.00000000000000,-25.00000000000000,12.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpP0zs1pRofzQ7o_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("Sketcher::SketchObject","Sketch_FpP0zs1pRofzQ7o_1_JRC")
App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpP0zs1pRofzQ7o_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(30.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(60.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,25.00000000000000,0.00000000000000),App.Vector(60.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Pad","Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC")
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC")
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpP0zs1pRofzQ7o_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpP0zs1pRofzQ7o_1_Ffq4kUsCHQpW0oQ_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Plane", "plane_Sketch_FmlGjc2ccwapAXI_1_JVC")
origin = App.Vector(0.00000000000000,-25.00000000000000,42.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmlGjc2ccwapAXI_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("Sketcher::SketchObject","Sketch_FmlGjc2ccwapAXI_1_JVC")
App.ActiveDocument.getObject("Sketch_FmlGjc2ccwapAXI_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmlGjc2ccwapAXI_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FmlGjc2ccwapAXI_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmlGjc2ccwapAXI_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmlGjc2ccwapAXI_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmlGjc2ccwapAXI_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fa0nMAPcnrDl1V0_0").newObject("PartDesign::Pocket","Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC")
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FmlGjc2ccwapAXI_1_JVC")
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").Length = 40.0
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmlGjc2ccwapAXI_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmlGjc2ccwapAXI_1_Fs0rc4TJJFCeaD2_1_JVC").Offset = 0
App.ActiveDocument.recompute()

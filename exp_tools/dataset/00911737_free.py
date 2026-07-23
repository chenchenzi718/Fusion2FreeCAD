import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00911737")
App.ActiveDocument.addObject("PartDesign::Body","Body_FWGhvUZohhkd8Kn_0")
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").Label = "Body_FWGhvUZohhkd8Kn_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Plane", "plane_Sketch_FWGhvUZohhkd8Kn_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWGhvUZohhkd8Kn_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("Sketcher::SketchObject","Sketch_FWGhvUZohhkd8Kn_0_JGC")
App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWGhvUZohhkd8Kn_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-41.30013000000000,32.09034000000000,0.00000000000000),App.Vector(39.28548000000000,32.09034000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC").addGeometry(Part.LineSegment(App.Vector(39.28548000000000,32.09034000000000,0.00000000000000),App.Vector(39.28548000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-41.30013000000000,0.00000000000000,0.00000000000000),App.Vector(39.28548000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-41.30013000000000,0.00000000000000,0.00000000000000),App.Vector(-62.02214000000000,17.12444000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-41.30013000000000,32.09034000000000,0.00000000000000),App.Vector(-62.02214000000000,17.12444000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Pad","Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC")
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC")
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").Length = 18.034000000000002
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWGhvUZohhkd8Kn_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWGhvUZohhkd8Kn_0_FJ5UfxTtleyvLrE_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Plane", "plane_Sketch_Fu64vjiefolEsaP_1_JJC")
origin = App.Vector(9.01700000000000,39.28548000000000,16.04517000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu64vjiefolEsaP_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("Sketcher::SketchObject","Sketch_Fu64vjiefolEsaP_1_JJC")
App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu64vjiefolEsaP_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJC").addGeometry(Part.Circle(App.Vector(-0.50058000000000,7.87102000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.04502000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Pocket","Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC")
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJC")
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").Length = 11.938
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Plane", "plane_Sketch_Fu64vjiefolEsaP_1_JJG")
origin = App.Vector(9.01700000000000,39.28548000000000,16.04517000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu64vjiefolEsaP_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("Sketcher::SketchObject","Sketch_Fu64vjiefolEsaP_1_JJG")
App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu64vjiefolEsaP_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJG").addGeometry(Part.Circle(App.Vector(0.00213000000000,-6.48817000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.27730000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Pocket","Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG")
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJG")
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").Length = 11.938
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu64vjiefolEsaP_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu64vjiefolEsaP_1_F8D54h36LSgPSqg_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Plane", "plane_Sketch_FFaTAKhxj5duIAY_1_JNC")
origin = App.Vector(9.01700000000000,-56.84164000000000,20.86592000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.81067922000000,0.58549056000000)
z_axis=App.Vector(0.00000000000000,-0.58549056000000,0.81067922000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFaTAKhxj5duIAY_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("Sketcher::SketchObject","Sketch_FFaTAKhxj5duIAY_1_JNC")
App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFaTAKhxj5duIAY_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC").addGeometry(Part.LineSegment(App.Vector(-9.01700000000000,19.17097115589740,-0.00000334259320),App.Vector(9.01700000000000,19.17097115589740,-0.00000334259320)),False)

App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC").addGeometry(Part.LineSegment(App.Vector(9.01700000000000,19.17097115589740,-0.00000334259320),App.Vector(9.01700000000000,6.39032717152540,-0.00000771973220)),False)

App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC").addGeometry(Part.LineSegment(App.Vector(-9.01700000000000,6.39032717152540,-0.00000771973220),App.Vector(9.01700000000000,6.39032717152540,-0.00000771973220)),False)

App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC").addGeometry(Part.LineSegment(App.Vector(-9.01700000000000,19.17097115589740,-0.00000334259320),App.Vector(-9.01700000000000,6.39032717152540,-0.00000771973220)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Pocket","Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC")
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC")
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").Length = 4.572
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFaTAKhxj5duIAY_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFaTAKhxj5duIAY_1_FSicIEsSrjXNN3d_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Plane", "plane_Sketch_FpxN5PXdDHvGfDm_1_JRC")
origin = App.Vector(9.01700000000000,-1.00732000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpxN5PXdDHvGfDm_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("Sketcher::SketchObject","Sketch_FpxN5PXdDHvGfDm_1_JRC")
App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpxN5PXdDHvGfDm_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC").addGeometry(Part.LineSegment(App.Vector(-4.97375000000000,-25.91615000000000,0.00000000000000),App.Vector(5.63705000000000,-25.87305000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC").addGeometry(Part.LineSegment(App.Vector(5.63705000000000,-25.87305000000000,0.00000000000000),App.Vector(5.63705000000000,25.86829000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC").addGeometry(Part.LineSegment(App.Vector(-4.97375000000000,25.86829000000000,0.00000000000000),App.Vector(5.63705000000000,25.86829000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC").addGeometry(Part.LineSegment(App.Vector(-4.97375000000000,-25.91615000000000,0.00000000000000),App.Vector(-4.97375000000000,25.86829000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Pocket","Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC")
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC")
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").Length = 6.096
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpxN5PXdDHvGfDm_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpxN5PXdDHvGfDm_1_FL8OMJabpMn5eDf_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Plane", "plane_Sketch_FEQOauBN4EW6kui_1_JVC")
origin = App.Vector(9.01700000000000,32.85512000000000,32.09034000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEQOauBN4EW6kui_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("Sketcher::SketchObject","Sketch_FEQOauBN4EW6kui_1_JVC")
App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEQOauBN4EW6kui_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC").addGeometry(Part.LineSegment(App.Vector(9.01700000000000,-48.31612000000001,0.00000000000000),App.Vector(-9.01700000000000,-48.31612000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC").addGeometry(Part.LineSegment(App.Vector(-9.01700000000000,-48.31612000000001,0.00000000000000),App.Vector(-9.01700000000000,-6.43036000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC").addGeometry(Part.LineSegment(App.Vector(9.01700000000000,-6.43036000000000,0.00000000000000),App.Vector(-9.01700000000000,-6.43036000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC").addGeometry(Part.LineSegment(App.Vector(9.01700000000000,-48.31612000000001,0.00000000000000),App.Vector(9.01700000000000,-6.43036000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Pocket","Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC")
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC")
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").Length = 2.286
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEQOauBN4EW6kui_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEQOauBN4EW6kui_1_FHdhrjKNLjnQGaE_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Plane", "plane_Sketch_FlhMroDHPdbzXg8_1_JZC")
origin = App.Vector(9.01700000000000,5.48188000000000,29.80434000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlhMroDHPdbzXg8_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("Sketcher::SketchObject","Sketch_FlhMroDHPdbzXg8_1_JZC")
App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlhMroDHPdbzXg8_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC").addGeometry(Part.LineSegment(App.Vector(3.39380000000000,15.31496000000000,0.00000000000000),App.Vector(-2.24474000000000,15.31496000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC").addGeometry(Part.LineSegment(App.Vector(-2.24474000000000,15.31496000000000,0.00000000000000),App.Vector(-2.24474000000000,9.02177000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC").addGeometry(Part.LineSegment(App.Vector(3.39380000000000,9.02177000000000,0.00000000000000),App.Vector(-2.24474000000000,9.02177000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC").addGeometry(Part.LineSegment(App.Vector(3.39380000000000,15.31496000000000,0.00000000000000),App.Vector(3.39380000000000,9.02177000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Pad","Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC")
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC")
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").Length = 9.652000000000001
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlhMroDHPdbzXg8_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlhMroDHPdbzXg8_1_FfHlnArb1o3mddO_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Plane", "plane_Sketch_FyL0r18COQfk3nI_1_JdC")
origin = App.Vector(9.59153000000000,14.50365000000000,37.04334000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyL0r18COQfk3nI_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("Sketcher::SketchObject","Sketch_FyL0r18COQfk3nI_1_JdC")
App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyL0r18COQfk3nI_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC").addGeometry(Part.LineSegment(App.Vector(-2.81927000000000,-2.41300000000000,0.00000000000000),App.Vector(2.81927000000000,-2.41300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC").addGeometry(Part.LineSegment(App.Vector(2.81927000000000,-7.23900000000000,0.00000000000000),App.Vector(2.81927000000000,-2.41300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC").addGeometry(Part.LineSegment(App.Vector(2.81927000000000,-7.23900000000000,0.00000000000000),App.Vector(-2.81927000000000,-7.23900000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC").addGeometry(Part.LineSegment(App.Vector(-2.81927000000000,-7.23900000000000,0.00000000000000),App.Vector(-2.81927000000000,-2.41300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FWGhvUZohhkd8Kn_0").newObject("PartDesign::Pad","Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC")
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC")
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").Length = 5.3340000000000005
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyL0r18COQfk3nI_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyL0r18COQfk3nI_1_FnB7Cbhr80XoTpC_1_JdC").Offset = 0
App.ActiveDocument.recompute()

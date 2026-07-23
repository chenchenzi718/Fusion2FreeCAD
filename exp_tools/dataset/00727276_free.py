import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00727276")
App.ActiveDocument.addObject("PartDesign::Body","Body_FR3fHeYvqKDGPzO_0")
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").Label = "Body_FR3fHeYvqKDGPzO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Plane", "plane_Sketch_FR3fHeYvqKDGPzO_0_JGi")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("Sketcher::SketchObject","Sketch_FR3fHeYvqKDGPzO_0_JGi")
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGi"), [""])
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").addGeometry(Part.LineSegment(App.Vector(-175.00000000000000,175.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").addGeometry(Part.LineSegment(App.Vector(-90.00000000000000,190.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").addGeometry(Part.LineSegment(App.Vector(-190.00000000000000,190.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,190.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").addGeometry(Part.LineSegment(App.Vector(-190.00000000000000,190.00000000000000,0.00000000000000),App.Vector(-190.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").addGeometry(Part.LineSegment(App.Vector(-190.00000000000000,90.00000000000000,0.00000000000000),App.Vector(-175.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").addGeometry(Part.LineSegment(App.Vector(-175.00000000000000,175.00000000000000,0.00000000000000),App.Vector(-175.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Pad","Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").Profile = App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").Length = 10.0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").Type = 4
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3Kat8pISn4Tpa7_0_JGi").Offset = 0
App.ActiveDocument.recompute()
App.ActiveDocument.addObject("PartDesign::Body","Body_FR3fHeYvqKDGPzO_0")
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").Label = "Body_FR3fHeYvqKDGPzO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Plane", "plane_Sketch_FR3fHeYvqKDGPzO_0_JGe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("Sketcher::SketchObject","Sketch_FR3fHeYvqKDGPzO_0_JGe")
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGe"), [""])
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe").addGeometry(Part.LineSegment(App.Vector(90.00000000000000,175.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe").addGeometry(Part.LineSegment(App.Vector(-90.00000000000000,190.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe").addGeometry(Part.LineSegment(App.Vector(-90.00000000000000,190.00000000000000,0.00000000000000),App.Vector(90.00000000000000,190.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe").addGeometry(Part.LineSegment(App.Vector(90.00000000000000,190.00000000000000,0.00000000000000),App.Vector(90.00000000000000,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Pad","Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").Profile = App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").Length = 10.0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").Type = 4
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FL4pMuWpPnJ2jHt_1_JGe").Offset = 0
App.ActiveDocument.recompute()
App.ActiveDocument.addObject("PartDesign::Body","Body_FR3fHeYvqKDGPzO_0")
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").Label = "Body_FR3fHeYvqKDGPzO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Plane", "plane_Sketch_FR3fHeYvqKDGPzO_0_JGW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("Sketcher::SketchObject","Sketch_FR3fHeYvqKDGPzO_0_JGW")
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGW"), [""])
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").addGeometry(Part.LineSegment(App.Vector(175.00000000000000,175.00000000000000,0.00000000000000),App.Vector(90.00000000000000,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").addGeometry(Part.LineSegment(App.Vector(90.00000000000000,190.00000000000000,0.00000000000000),App.Vector(90.00000000000000,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").addGeometry(Part.LineSegment(App.Vector(190.00000000000000,190.00000000000000,0.00000000000000),App.Vector(90.00000000000000,190.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").addGeometry(Part.LineSegment(App.Vector(190.00000000000000,190.00000000000000,0.00000000000000),App.Vector(190.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").addGeometry(Part.LineSegment(App.Vector(190.00000000000000,90.00000000000000,0.00000000000000),App.Vector(175.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").addGeometry(Part.LineSegment(App.Vector(175.00000000000000,175.00000000000000,0.00000000000000),App.Vector(175.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Pad","Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").Profile = App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").Length = 20.0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").Type = 4
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FM02K2wy5tZP6hS_2_JGW").Offset = 0
App.ActiveDocument.recompute()
App.ActiveDocument.addObject("PartDesign::Body","Body_FR3fHeYvqKDGPzO_0")
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").Label = "Body_FR3fHeYvqKDGPzO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Plane", "plane_Sketch_FR3fHeYvqKDGPzO_0_JGu")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGu").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("Sketcher::SketchObject","Sketch_FR3fHeYvqKDGPzO_0_JGu")
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGu"), [""])
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu").addGeometry(Part.LineSegment(App.Vector(-175.00000000000000,-90.00000000000000,0.00000000000000),App.Vector(-175.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu").addGeometry(Part.LineSegment(App.Vector(-190.00000000000000,90.00000000000000,0.00000000000000),App.Vector(-175.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu").addGeometry(Part.LineSegment(App.Vector(-190.00000000000000,90.00000000000000,0.00000000000000),App.Vector(-190.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu").addGeometry(Part.LineSegment(App.Vector(-190.00000000000000,-90.00000000000000,0.00000000000000),App.Vector(-175.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Pad","Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").Profile = App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").Length = 20.0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGu"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").Type = 4
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_F3q7DH85YIJFSDS_3_JGu").Offset = 0
App.ActiveDocument.recompute()
App.ActiveDocument.addObject("PartDesign::Body","Body_FR3fHeYvqKDGPzO_0")
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").Label = "Body_FR3fHeYvqKDGPzO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Plane", "plane_Sketch_FR3fHeYvqKDGPzO_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("Sketcher::SketchObject","Sketch_FR3fHeYvqKDGPzO_0_JGO")
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").addGeometry(Part.LineSegment(App.Vector(-175.00000000000000,-175.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").addGeometry(Part.LineSegment(App.Vector(-90.00000000000000,-190.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").addGeometry(Part.LineSegment(App.Vector(-190.00000000000000,-190.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,-190.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").addGeometry(Part.LineSegment(App.Vector(-190.00000000000000,-190.00000000000000,0.00000000000000),App.Vector(-190.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").addGeometry(Part.LineSegment(App.Vector(-190.00000000000000,-90.00000000000000,0.00000000000000),App.Vector(-175.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").addGeometry(Part.LineSegment(App.Vector(-175.00000000000000,-175.00000000000000,0.00000000000000),App.Vector(-175.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Pad","Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").Profile = App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").Length = 20.0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FzW5uY5X38CHt6x_4_JGO").Offset = 0
App.ActiveDocument.recompute()
App.ActiveDocument.addObject("PartDesign::Body","Body_FR3fHeYvqKDGPzO_0")
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").Label = "Body_FR3fHeYvqKDGPzO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Plane", "plane_Sketch_FR3fHeYvqKDGPzO_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("Sketcher::SketchObject","Sketch_FR3fHeYvqKDGPzO_0_JGK")
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK").addGeometry(Part.LineSegment(App.Vector(90.00000000000000,-175.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK").addGeometry(Part.LineSegment(App.Vector(-90.00000000000000,-190.00000000000000,0.00000000000000),App.Vector(-90.00000000000000,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK").addGeometry(Part.LineSegment(App.Vector(-90.00000000000000,-190.00000000000000,0.00000000000000),App.Vector(90.00000000000000,-190.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK").addGeometry(Part.LineSegment(App.Vector(90.00000000000000,-190.00000000000000,0.00000000000000),App.Vector(90.00000000000000,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Pad","Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").Profile = App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").Length = 20.0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FbnOzX1Y5tfRzw5_5_JGK").Offset = 0
App.ActiveDocument.recompute()
App.ActiveDocument.addObject("PartDesign::Body","Body_FR3fHeYvqKDGPzO_0")
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").Label = "Body_FR3fHeYvqKDGPzO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Plane", "plane_Sketch_FR3fHeYvqKDGPzO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("Sketcher::SketchObject","Sketch_FR3fHeYvqKDGPzO_0_JGC")
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").addGeometry(Part.LineSegment(App.Vector(175.00000000000000,-175.00000000000000,0.00000000000000),App.Vector(90.00000000000000,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").addGeometry(Part.LineSegment(App.Vector(90.00000000000000,-190.00000000000000,0.00000000000000),App.Vector(90.00000000000000,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").addGeometry(Part.LineSegment(App.Vector(190.00000000000000,-190.00000000000000,0.00000000000000),App.Vector(90.00000000000000,-190.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").addGeometry(Part.LineSegment(App.Vector(190.00000000000000,-190.00000000000000,0.00000000000000),App.Vector(190.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").addGeometry(Part.LineSegment(App.Vector(190.00000000000000,-90.00000000000000,0.00000000000000),App.Vector(175.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").addGeometry(Part.LineSegment(App.Vector(175.00000000000000,-175.00000000000000,0.00000000000000),App.Vector(175.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Pad","Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").Profile = App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FExf0bHW0cxA5VN_6_JGC").Offset = 0
App.ActiveDocument.recompute()
App.ActiveDocument.addObject("PartDesign::Body","Body_FR3fHeYvqKDGPzO_0")
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").Label = "Body_FR3fHeYvqKDGPzO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Plane", "plane_Sketch_FR3fHeYvqKDGPzO_0_JGq")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGq").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("Sketcher::SketchObject","Sketch_FR3fHeYvqKDGPzO_0_JGq")
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR3fHeYvqKDGPzO_0_JGq"), [""])
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq").addGeometry(Part.LineSegment(App.Vector(175.00000000000000,-90.00000000000000,0.00000000000000),App.Vector(175.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq").addGeometry(Part.LineSegment(App.Vector(190.00000000000000,90.00000000000000,0.00000000000000),App.Vector(175.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq").addGeometry(Part.LineSegment(App.Vector(190.00000000000000,90.00000000000000,0.00000000000000),App.Vector(190.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq").addGeometry(Part.LineSegment(App.Vector(190.00000000000000,-90.00000000000000,0.00000000000000),App.Vector(175.00000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR3fHeYvqKDGPzO_0").newObject("PartDesign::Pad","Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").Profile = App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq")
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").Length = 20.0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR3fHeYvqKDGPzO_0_JGq"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").Type = 4
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR3fHeYvqKDGPzO_0_FgCsc1yczxtPR89_7_JGq").Offset = 0
App.ActiveDocument.recompute()

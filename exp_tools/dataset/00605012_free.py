import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00605012")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fi75vtOKEhxnTHN_0")
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").Label = "Body_Fi75vtOKEhxnTHN_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Plane", "plane_Sketch_Fi75vtOKEhxnTHN_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fi75vtOKEhxnTHN_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("Sketcher::SketchObject","Sketch_Fi75vtOKEhxnTHN_0_JGC")
App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fi75vtOKEhxnTHN_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC").addGeometry(Part.LineSegment(App.Vector(-19.13650000000000,3.36450000000000,0.00000000000000),App.Vector(19.13650000000000,3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC").addGeometry(Part.LineSegment(App.Vector(19.13650000000000,3.36450000000000,0.00000000000000),App.Vector(19.13650000000000,-3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC").addGeometry(Part.LineSegment(App.Vector(-19.13650000000000,-3.36450000000000,0.00000000000000),App.Vector(19.13650000000000,-3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC").addGeometry(Part.LineSegment(App.Vector(-19.13650000000000,3.36450000000000,0.00000000000000),App.Vector(-19.13650000000000,-3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Pad","Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC")
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC")
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").Length = 2.5
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fi75vtOKEhxnTHN_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fi75vtOKEhxnTHN_0_FZQ0Uq8eQeY9Iyz_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Plane", "plane_Sketch_Fh7YCQUB2Y5Eux1_1_JJC")
origin = App.Vector(0.00000000000000,-3.36450000000000,1.25000000000000)
x_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh7YCQUB2Y5Eux1_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("Sketcher::SketchObject","Sketch_Fh7YCQUB2Y5Eux1_1_JJC")
App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh7YCQUB2Y5Eux1_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-19.13650000000000,1.25000000000000,0.00000000000000),App.Vector(-17.63650000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-17.63650000000000,1.25000000000000,0.00000000000000),App.Vector(-17.63650000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-19.13650000000000,0.25000000000000,0.00000000000000),App.Vector(-17.63650000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-19.13650000000000,1.25000000000000,0.00000000000000),App.Vector(-19.13650000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Pocket","Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC")
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC")
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Plane", "plane_Sketch_Fh7YCQUB2Y5Eux1_1_JJG")
origin = App.Vector(0.00000000000000,-3.36450000000000,1.25000000000000)
x_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh7YCQUB2Y5Eux1_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("Sketcher::SketchObject","Sketch_Fh7YCQUB2Y5Eux1_1_JJG")
App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh7YCQUB2Y5Eux1_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG").addGeometry(Part.LineSegment(App.Vector(19.13650000000000,1.25000000000000,0.00000000000000),App.Vector(17.63650000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG").addGeometry(Part.LineSegment(App.Vector(17.63650000000000,1.25000000000000,0.00000000000000),App.Vector(17.63650000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG").addGeometry(Part.LineSegment(App.Vector(19.13650000000000,0.25000000000000,0.00000000000000),App.Vector(17.63650000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG").addGeometry(Part.LineSegment(App.Vector(19.13650000000000,1.25000000000000,0.00000000000000),App.Vector(19.13650000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Pocket","Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG")
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG")
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh7YCQUB2Y5Eux1_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh7YCQUB2Y5Eux1_1_FjiRXx5WIoX2Ww7_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Plane", "plane_Sketch_FApfwpb4aMfz0Qj_1_JNC")
origin = App.Vector(-18.38650000000000,0.00000000000000,1.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FApfwpb4aMfz0Qj_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("Sketcher::SketchObject","Sketch_FApfwpb4aMfz0Qj_1_JNC")
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FApfwpb4aMfz0Qj_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC").addGeometry(Part.LineSegment(App.Vector(37.52300000000000,3.36450000000000,0.00000000000000),App.Vector(37.52300000000000,1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC").addGeometry(Part.LineSegment(App.Vector(37.52300000000000,1.96450000000000,0.00000000000000),App.Vector(36.02300000000000,1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC").addGeometry(Part.LineSegment(App.Vector(36.02300000000000,3.36450000000000,0.00000000000000),App.Vector(36.02300000000000,1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC").addGeometry(Part.LineSegment(App.Vector(37.52300000000000,3.36450000000000,0.00000000000000),App.Vector(36.02300000000000,3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Pocket","Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC")
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC")
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Plane", "plane_Sketch_FApfwpb4aMfz0Qj_1_JNG")
origin = App.Vector(-18.38650000000000,0.00000000000000,1.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FApfwpb4aMfz0Qj_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("Sketcher::SketchObject","Sketch_FApfwpb4aMfz0Qj_1_JNG")
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FApfwpb4aMfz0Qj_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG").addGeometry(Part.LineSegment(App.Vector(37.52300000000000,-1.96450000000000,0.00000000000000),App.Vector(36.02300000000000,-1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG").addGeometry(Part.LineSegment(App.Vector(36.02300000000000,-1.96450000000000,0.00000000000000),App.Vector(36.02300000000000,-3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG").addGeometry(Part.LineSegment(App.Vector(36.02300000000000,-3.36450000000000,0.00000000000000),App.Vector(37.52300000000000,-3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG").addGeometry(Part.LineSegment(App.Vector(37.52300000000000,-1.96450000000000,0.00000000000000),App.Vector(37.52300000000000,-3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Pocket","Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG")
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG")
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Plane", "plane_Sketch_FApfwpb4aMfz0Qj_1_JNK")
origin = App.Vector(-18.38650000000000,0.00000000000000,1.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FApfwpb4aMfz0Qj_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("Sketcher::SketchObject","Sketch_FApfwpb4aMfz0Qj_1_JNK")
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FApfwpb4aMfz0Qj_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK").addGeometry(Part.LineSegment(App.Vector(-0.75000000000000,3.36450000000000,0.00000000000000),App.Vector(0.75000000000000,3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK").addGeometry(Part.LineSegment(App.Vector(0.75000000000000,3.36450000000000,0.00000000000000),App.Vector(0.75000000000000,1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK").addGeometry(Part.LineSegment(App.Vector(-0.75000000000000,1.96450000000000,0.00000000000000),App.Vector(0.75000000000000,1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK").addGeometry(Part.LineSegment(App.Vector(-0.75000000000000,3.36450000000000,0.00000000000000),App.Vector(-0.75000000000000,1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Pocket","Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK")
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK")
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Plane", "plane_Sketch_FApfwpb4aMfz0Qj_1_JNO")
origin = App.Vector(-18.38650000000000,0.00000000000000,1.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FApfwpb4aMfz0Qj_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("Sketcher::SketchObject","Sketch_FApfwpb4aMfz0Qj_1_JNO")
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FApfwpb4aMfz0Qj_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO").addGeometry(Part.LineSegment(App.Vector(-0.75000000000000,-1.96450000000000,0.00000000000000),App.Vector(0.75000000000000,-1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO").addGeometry(Part.LineSegment(App.Vector(0.75000000000000,-3.36450000000000,0.00000000000000),App.Vector(0.75000000000000,-1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO").addGeometry(Part.LineSegment(App.Vector(-0.75000000000000,-3.36450000000000,0.00000000000000),App.Vector(0.75000000000000,-3.36450000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO").addGeometry(Part.LineSegment(App.Vector(-0.75000000000000,-3.36450000000000,0.00000000000000),App.Vector(-0.75000000000000,-1.96450000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Pocket","Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO")
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO")
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FApfwpb4aMfz0Qj_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FApfwpb4aMfz0Qj_1_FkKDO9TzaOlro50_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Plane", "plane_Sketch_FT10l1e7dDdkCpA_1_JRC")
origin = App.Vector(0.00000000000000,3.36450000000000,1.25000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FT10l1e7dDdkCpA_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("Sketcher::SketchObject","Sketch_FT10l1e7dDdkCpA_1_JRC")
App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FT10l1e7dDdkCpA_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,-1.25000000000000,0.00000000000000),App.Vector(-2.00000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,-1.25000000000000,0.00000000000000),App.Vector(-2.00000000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,0.25000000000000,0.00000000000000),App.Vector(2.00000000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,-1.25000000000000,0.00000000000000),App.Vector(2.00000000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Pad","Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC")
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC")
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").Length = 1.5
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FT10l1e7dDdkCpA_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FT10l1e7dDdkCpA_1_FU2zKWlVrzghkuU_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Plane", "plane_Sketch_FgfulZIedbKlNnS_1_JVC")
origin = App.Vector(0.00000000000000,-3.36450000000000,1.25000000000000)
x_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgfulZIedbKlNnS_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("Sketcher::SketchObject","Sketch_FgfulZIedbKlNnS_1_JVC")
App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgfulZIedbKlNnS_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,-1.25000000000000,0.00000000000000),App.Vector(2.00000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC").addGeometry(Part.LineSegment(App.Vector(2.00000000000000,-1.25000000000000,0.00000000000000),App.Vector(2.00000000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,0.25000000000000,0.00000000000000),App.Vector(2.00000000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC").addGeometry(Part.LineSegment(App.Vector(-2.00000000000000,-1.25000000000000,0.00000000000000),App.Vector(-2.00000000000000,0.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fi75vtOKEhxnTHN_0").newObject("PartDesign::Pad","Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC")
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC")
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").Length = 1.5
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgfulZIedbKlNnS_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgfulZIedbKlNnS_1_F8QPGMx7vo666WP_1_JVC").Offset = 0
App.ActiveDocument.recompute()

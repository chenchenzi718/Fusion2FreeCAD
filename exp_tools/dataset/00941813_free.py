import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00941813")
App.ActiveDocument.addObject("PartDesign::Body","Body_FBYrVIW2h4cXsjn_0")
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").Label = "Body_FBYrVIW2h4cXsjn_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Plane", "plane_Sketch_FBYrVIW2h4cXsjn_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBYrVIW2h4cXsjn_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("Sketcher::SketchObject","Sketch_FBYrVIW2h4cXsjn_0_JGC")
App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBYrVIW2h4cXsjn_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-17.00000000000000,23.50000000000000,0.00000000000000),App.Vector(17.00000000000000,23.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(17.00000000000000,20.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,20.50000000000000,0.00000000000000),App.Vector(20.00000000000000,-20.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(17.00000000000000,-20.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-17.00000000000000,-23.50000000000000,0.00000000000000),App.Vector(17.00000000000000,-23.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-17.00000000000000,-20.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,20.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,-20.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-17.00000000000000,20.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Pad","Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC")
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC")
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").Length = 21.8
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBYrVIW2h4cXsjn_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBYrVIW2h4cXsjn_0_FVFgDPddZbR0SaX_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Plane", "plane_Sketch_FXmfei0eUVnhzGO_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXmfei0eUVnhzGO_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("Sketcher::SketchObject","Sketch_FXmfei0eUVnhzGO_1_JJC")
App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXmfei0eUVnhzGO_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC").addGeometry(Part.LineSegment(App.Vector(-17.50000000000000,20.00000000000000,0.00000000000000),App.Vector(17.50000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC").addGeometry(Part.LineSegment(App.Vector(17.50000000000000,20.00000000000000,0.00000000000000),App.Vector(17.50000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC").addGeometry(Part.LineSegment(App.Vector(-17.50000000000000,-20.00000000000000,0.00000000000000),App.Vector(17.50000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC").addGeometry(Part.LineSegment(App.Vector(-17.50000000000000,20.00000000000000,0.00000000000000),App.Vector(-17.50000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Pocket","Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC")
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC")
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").Length = 14.3
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXmfei0eUVnhzGO_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXmfei0eUVnhzGO_1_FzuM4ue9nuOKByN_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Plane", "plane_Sketch_FYFFkFRTJy6rpUI_1_JNC")
origin = App.Vector(-0.00000000000000,-23.50000000000000,-10.90000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYFFkFRTJy6rpUI_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("Sketcher::SketchObject","Sketch_FYFFkFRTJy6rpUI_1_JNC")
App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYFFkFRTJy6rpUI_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-11.00000000000000,5.40000000000000,0.00000000000000),App.Vector(0.00000000000000,5.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,5.40000000000000,0.00000000000000),App.Vector(0.00000000000000,-2.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-11.00000000000000,-2.10000000000000,0.00000000000000),App.Vector(0.00000000000000,-2.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-11.00000000000000,5.40000000000000,0.00000000000000),App.Vector(-11.00000000000000,-2.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Pocket","Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC")
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC")
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").Length = 4.0
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYFFkFRTJy6rpUI_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYFFkFRTJy6rpUI_1_FaatSb0aFUfZbiK_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Plane", "plane_Sketch_FeNJRBI7iNS13xi_1_JRC")
origin = App.Vector(20.00000000000000,0.00000000000000,-10.90000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeNJRBI7iNS13xi_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("Sketcher::SketchObject","Sketch_FeNJRBI7iNS13xi_1_JRC")
App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeNJRBI7iNS13xi_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC").addGeometry(Part.LineSegment(App.Vector(-16.50000000000000,7.90000000000000,0.00000000000000),App.Vector(-7.85000000000000,7.90000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC").addGeometry(Part.LineSegment(App.Vector(-7.85000000000000,7.90000000000000,0.00000000000000),App.Vector(-7.85000000000000,4.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC").addGeometry(Part.LineSegment(App.Vector(-16.50000000000000,4.05000000000000,0.00000000000000),App.Vector(-7.85000000000000,4.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC").addGeometry(Part.LineSegment(App.Vector(-16.50000000000000,7.90000000000000,0.00000000000000),App.Vector(-16.50000000000000,4.05000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Pocket","Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC")
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC")
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeNJRBI7iNS13xi_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeNJRBI7iNS13xi_1_FtHPLWyT0T4tKbe_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Plane", "plane_Sketch_Fmc688hTa32h5fZ_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,-21.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fmc688hTa32h5fZ_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("Sketcher::SketchObject","Sketch_Fmc688hTa32h5fZ_1_JVC")
App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fmc688hTa32h5fZ_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-11.15000000000000,4.50000000000000,0.00000000000000),App.Vector(-15.50000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-15.50000000000000,4.50000000000000,0.00000000000000),App.Vector(-15.50000000000000,19.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-11.15000000000000,19.50000000000000,0.00000000000000),App.Vector(-15.50000000000000,19.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-11.15000000000000,4.50000000000000,0.00000000000000),App.Vector(-11.15000000000000,19.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Pocket","Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC")
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC")
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").Length = 8.0
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fmc688hTa32h5fZ_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fmc688hTa32h5fZ_1_FMVxf1NgaACYW4w_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Plane", "plane_Sketch_Fsl7RLGKEzrRJm2_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fsl7RLGKEzrRJm2_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("Sketcher::SketchObject","Sketch_Fsl7RLGKEzrRJm2_1_JZC")
App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fsl7RLGKEzrRJm2_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC").addGeometry(Part.LineSegment(App.Vector(-18.50000000000000,21.00000000000000,0.00000000000000),App.Vector(18.50000000000000,21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC").addGeometry(Part.LineSegment(App.Vector(18.50000000000000,21.00000000000000,0.00000000000000),App.Vector(18.50000000000000,-21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC").addGeometry(Part.LineSegment(App.Vector(-18.50000000000000,-21.00000000000000,0.00000000000000),App.Vector(18.50000000000000,-21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC").addGeometry(Part.LineSegment(App.Vector(-18.50000000000000,21.00000000000000,0.00000000000000),App.Vector(-18.50000000000000,-21.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Pocket","Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC")
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC")
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").Length = 1.5
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fsl7RLGKEzrRJm2_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fsl7RLGKEzrRJm2_1_FjDvCC5ZWFemXJs_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Plane", "plane_Sketch_FReedIes5OxeIMH_1_JdC")
origin = App.Vector(0.00000000000000,0.00000000000000,-21.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FReedIes5OxeIMH_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("Sketcher::SketchObject","Sketch_FReedIes5OxeIMH_1_JdC")
App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FReedIes5OxeIMH_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdC").addGeometry(Part.Circle(App.Vector(0.00000000000000,11.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Pad","Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC")
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdC")
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Plane", "plane_Sketch_FReedIes5OxeIMH_1_JdG")
origin = App.Vector(0.00000000000000,0.00000000000000,-21.80000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FReedIes5OxeIMH_1_JdG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("Sketcher::SketchObject","Sketch_FReedIes5OxeIMH_1_JdG")
App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FReedIes5OxeIMH_1_JdG"), [""])
App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdG").addGeometry(Part.Circle(App.Vector(0.00000000000000,-11.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Pad","Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG")
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").Profile = App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdG")
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").Length = 3.0
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FReedIes5OxeIMH_1_JdG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").Type = 4
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FReedIes5OxeIMH_1_FKqtrmrwBflcF4H_1_JdG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Plane", "plane_Sketch_FNdwFj2t1eE0v12_1_JnC")
origin = App.Vector(-20.00000000000000,0.00000000000000,-10.90000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNdwFj2t1eE0v12_1_JnC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("Sketcher::SketchObject","Sketch_FNdwFj2t1eE0v12_1_JnC")
App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNdwFj2t1eE0v12_1_JnC"), [""])
App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC").addGeometry(Part.LineSegment(App.Vector(-17.50000000000000,-6.70000000000000,0.00000000000000),App.Vector(17.50000000000000,-6.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC").addGeometry(Part.LineSegment(App.Vector(17.50000000000000,-6.70000000000000,0.00000000000000),App.Vector(17.50000000000000,-9.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC").addGeometry(Part.LineSegment(App.Vector(-17.50000000000000,-9.40000000000000,0.00000000000000),App.Vector(17.50000000000000,-9.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC").addGeometry(Part.LineSegment(App.Vector(-17.50000000000000,-6.70000000000000,0.00000000000000),App.Vector(-17.50000000000000,-9.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBYrVIW2h4cXsjn_0").newObject("PartDesign::Pocket","Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC")
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").Profile = App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC")
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").Length = 41.0
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNdwFj2t1eE0v12_1_JnC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").Type = 4
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNdwFj2t1eE0v12_1_FNXtaOduyrMmp36_1_JnC").Offset = 0
App.ActiveDocument.recompute()

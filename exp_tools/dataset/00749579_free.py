import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00749579")
App.ActiveDocument.addObject("PartDesign::Body","Body_FLpDq4Kpb0gU9Qn_0")
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").Label = "Body_FLpDq4Kpb0gU9Qn_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Plane", "plane_Sketch_FLpDq4Kpb0gU9Qn_0_JIC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLpDq4Kpb0gU9Qn_0_JIC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("Sketcher::SketchObject","Sketch_FLpDq4Kpb0gU9Qn_0_JIC")
App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLpDq4Kpb0gU9Qn_0_JIC"), [""])
App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC").addGeometry(Part.LineSegment(App.Vector(-60.20662000000000,52.81318000000000,0.00000000000000),App.Vector(-34.44801000000000,52.81318000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC").addGeometry(Part.LineSegment(App.Vector(-34.44801000000000,52.81318000000000,0.00000000000000),App.Vector(-34.44801000000000,39.57412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC").addGeometry(Part.LineSegment(App.Vector(-60.20662000000000,39.57412000000000,0.00000000000000),App.Vector(-34.44801000000000,39.57412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC").addGeometry(Part.LineSegment(App.Vector(-60.20662000000000,52.81318000000000,0.00000000000000),App.Vector(-60.20662000000000,39.57412000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Pad","Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC")
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").Profile = App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC")
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").Length = 13.462
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLpDq4Kpb0gU9Qn_0_JIC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").Type = 4
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLpDq4Kpb0gU9Qn_0_FEcilRnV0z88whX_0_JIC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Plane", "plane_Sketch_FyuWkAwwBfX7GFh_1_JLC")
origin = App.Vector(-47.32732000000000,46.19365000000001,13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("Sketcher::SketchObject","Sketch_FyuWkAwwBfX7GFh_1_JLC")
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLC").addGeometry(Part.Circle(App.Vector(-8.41203000000000,2.99824000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.19186000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Pad","Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLC")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").Length = 5.842
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Plane", "plane_Sketch_FyuWkAwwBfX7GFh_1_JLG")
origin = App.Vector(-47.32732000000000,46.19365000000001,13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("Sketcher::SketchObject","Sketch_FyuWkAwwBfX7GFh_1_JLG")
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLG").addGeometry(Part.Circle(App.Vector(-8.41203000000000,-3.60576000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.19186000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Pad","Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLG")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").Length = 5.842
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Plane", "plane_Sketch_FyuWkAwwBfX7GFh_1_JLK")
origin = App.Vector(-47.32732000000000,46.19365000000001,13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("Sketcher::SketchObject","Sketch_FyuWkAwwBfX7GFh_1_JLK")
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLK").addGeometry(Part.Circle(App.Vector(-2.57003000000000,2.99824000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.19186000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Pad","Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLK")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").Length = 5.842
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Plane", "plane_Sketch_FyuWkAwwBfX7GFh_1_JLO")
origin = App.Vector(-47.32732000000000,46.19365000000001,13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("Sketcher::SketchObject","Sketch_FyuWkAwwBfX7GFh_1_JLO")
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLO").addGeometry(Part.Circle(App.Vector(-2.57003000000000,-3.60576000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.19186000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Pad","Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLO")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").Length = 5.842
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Plane", "plane_Sketch_FyuWkAwwBfX7GFh_1_JLS")
origin = App.Vector(-47.32732000000000,46.19365000000001,13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("Sketcher::SketchObject","Sketch_FyuWkAwwBfX7GFh_1_JLS")
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLS"), [""])
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLS").addGeometry(Part.Circle(App.Vector(3.27197000000000,2.99824000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.19186000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Pad","Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").Profile = App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLS")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").Length = 5.842
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").Type = 4
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Plane", "plane_Sketch_FyuWkAwwBfX7GFh_1_JLW")
origin = App.Vector(-47.32732000000000,46.19365000000001,13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("Sketcher::SketchObject","Sketch_FyuWkAwwBfX7GFh_1_JLW")
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLW"), [""])
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLW").addGeometry(Part.Circle(App.Vector(3.27197000000000,-3.60576000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.19186000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Pad","Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").Profile = App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLW")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").Length = 5.842
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").Type = 4
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Plane", "plane_Sketch_FyuWkAwwBfX7GFh_1_JLa")
origin = App.Vector(-47.32732000000000,46.19365000000001,13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("Sketcher::SketchObject","Sketch_FyuWkAwwBfX7GFh_1_JLa")
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLa"), [""])
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLa").addGeometry(Part.Circle(App.Vector(9.11397000000000,2.99824000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.19186000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Pad","Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").Profile = App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLa")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").Length = 5.842
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").Type = 4
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Plane", "plane_Sketch_FyuWkAwwBfX7GFh_1_JLe")
origin = App.Vector(-47.32732000000000,46.19365000000001,13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("Sketcher::SketchObject","Sketch_FyuWkAwwBfX7GFh_1_JLe")
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyuWkAwwBfX7GFh_1_JLe"), [""])
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLe").addGeometry(Part.Circle(App.Vector(9.11397000000000,-3.60576000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.19186000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLpDq4Kpb0gU9Qn_0").newObject("PartDesign::Pad","Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").Profile = App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLe")
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").Length = 5.842
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyuWkAwwBfX7GFh_1_JLe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").Type = 4
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyuWkAwwBfX7GFh_1_FpJyuaKJfeD9uEH_1_JLe").Offset = 0
App.ActiveDocument.recompute()

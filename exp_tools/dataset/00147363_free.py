import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00147363")
App.ActiveDocument.addObject("PartDesign::Body","Body_FarlXj9y4gltcQN_0")
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").Label = "Body_FarlXj9y4gltcQN_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Plane", "plane_Sketch_FarlXj9y4gltcQN_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FarlXj9y4gltcQN_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("Sketcher::SketchObject","Sketch_FarlXj9y4gltcQN_0_JGC")
App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FarlXj9y4gltcQN_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(406.39999999999998,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC").addGeometry(Part.LineSegment(App.Vector(406.39999999999998,0.00000000000000,0.00000000000000),App.Vector(406.39999999999998,406.39999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,406.39999999999998,0.00000000000000),App.Vector(406.39999999999998,406.39999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,406.39999999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Pad","Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC")
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC")
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").Length = 152.4
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FarlXj9y4gltcQN_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FarlXj9y4gltcQN_0_FQx0HDA8rYyzmwk_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Plane", "plane_Sketch_F7fkzhqrvlOUZnd_1_JJC")
origin = App.Vector(203.19999999999999,203.19999999999999,152.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7fkzhqrvlOUZnd_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("Sketcher::SketchObject","Sketch_F7fkzhqrvlOUZnd_1_JJC")
App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7fkzhqrvlOUZnd_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC").addGeometry(Part.LineSegment(App.Vector(-190.50000000000000,-190.50000000000000,0.00000000000000),App.Vector(190.50000000000000,-190.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC").addGeometry(Part.LineSegment(App.Vector(190.50000000000000,-190.50000000000000,0.00000000000000),App.Vector(190.50000000000000,190.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC").addGeometry(Part.LineSegment(App.Vector(-190.50000000000000,190.50000000000000,0.00000000000000),App.Vector(190.50000000000000,190.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC").addGeometry(Part.LineSegment(App.Vector(-190.50000000000000,-190.50000000000000,0.00000000000000),App.Vector(-190.50000000000000,190.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Pocket","Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC")
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC")
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").Length = 127.0
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7fkzhqrvlOUZnd_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7fkzhqrvlOUZnd_1_Fj95jTWCCrs4Snl_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Plane", "plane_Sketch_FkrF97lXbv2Dsv0_1_JNC")
origin = App.Vector(0.00000000000000,203.19999999999999,76.20000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkrF97lXbv2Dsv0_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("Sketcher::SketchObject","Sketch_FkrF97lXbv2Dsv0_1_JNC")
App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkrF97lXbv2Dsv0_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC").addGeometry(Part.LineSegment(App.Vector(-38.09999999999999,19.05000000000000,0.00000000000000),App.Vector(-38.09999999999999,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC").addGeometry(Part.LineSegment(App.Vector(-38.09999999999999,-19.05000000000000,0.00000000000000),App.Vector(-50.80000000000001,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.80000000000001,19.05000000000000,0.00000000000000),App.Vector(-50.80000000000001,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC").addGeometry(Part.LineSegment(App.Vector(-38.09999999999999,19.05000000000000,0.00000000000000),App.Vector(-50.80000000000001,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Pad","Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC")
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC")
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkrF97lXbv2Dsv0_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkrF97lXbv2Dsv0_1_FJjHulaIX4UFqyy_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Plane", "plane_Sketch_F9ZrMxt3l9AnReF_1_JRC")
origin = App.Vector(-25.40000000000000,241.29999999999998,76.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9ZrMxt3l9AnReF_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("Sketcher::SketchObject","Sketch_F9ZrMxt3l9AnReF_1_JRC")
App.ActiveDocument.getObject("Sketch_F9ZrMxt3l9AnReF_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9ZrMxt3l9AnReF_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F9ZrMxt3l9AnReF_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9ZrMxt3l9AnReF_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9ZrMxt3l9AnReF_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9ZrMxt3l9AnReF_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Pocket","Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC")
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F9ZrMxt3l9AnReF_1_JRC")
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9ZrMxt3l9AnReF_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9ZrMxt3l9AnReF_1_FwzBRi7C8D1GqlW_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Plane", "plane_Sketch_Fp0mYTtIHzay5Hi_1_JVC")
origin = App.Vector(0.00000000000000,203.19999999999999,76.20000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fp0mYTtIHzay5Hi_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("Sketcher::SketchObject","Sketch_Fp0mYTtIHzay5Hi_1_JVC")
App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fp0mYTtIHzay5Hi_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC").addGeometry(Part.LineSegment(App.Vector(38.09999999999999,-19.05000000000000,0.00000000000000),App.Vector(50.79999999999998,-19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC").addGeometry(Part.LineSegment(App.Vector(50.79999999999998,-19.05000000000000,0.00000000000000),App.Vector(50.79999999999998,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC").addGeometry(Part.LineSegment(App.Vector(38.09999999999999,19.05000000000000,0.00000000000000),App.Vector(50.79999999999998,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC").addGeometry(Part.LineSegment(App.Vector(38.09999999999999,-19.05000000000000,0.00000000000000),App.Vector(38.09999999999999,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Pad","Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC")
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC")
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fp0mYTtIHzay5Hi_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fp0mYTtIHzay5Hi_1_FpfOonXE9GQEYIm_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Plane", "plane_Sketch_FMcZmg0So449myc_1_JZC")
origin = App.Vector(-25.40000000000000,152.40000000000001,76.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMcZmg0So449myc_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("Sketcher::SketchObject","Sketch_FMcZmg0So449myc_1_JZC")
App.ActiveDocument.getObject("Sketch_FMcZmg0So449myc_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMcZmg0So449myc_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FMcZmg0So449myc_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMcZmg0So449myc_1_JZC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMcZmg0So449myc_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMcZmg0So449myc_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Pocket","Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC")
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FMcZmg0So449myc_1_JZC")
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMcZmg0So449myc_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMcZmg0So449myc_1_FajXSVOMpuXkXoE_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Plane", "plane_Sketch_FrfXEIEUd8hq7Sa_1_JdC")
origin = App.Vector(0.00000000000000,203.19999999999999,76.20000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrfXEIEUd8hq7Sa_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("Sketcher::SketchObject","Sketch_FrfXEIEUd8hq7Sa_1_JdC")
App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrfXEIEUd8hq7Sa_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC").addGeometry(Part.LineSegment(App.Vector(-6.34999999999999,12.70000000000000,0.00000000000000),App.Vector(6.34999999999999,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC").addGeometry(Part.LineSegment(App.Vector(6.34999999999999,12.70000000000000,0.00000000000000),App.Vector(6.34999999999999,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC").addGeometry(Part.LineSegment(App.Vector(-6.34999999999999,-12.70000000000000,0.00000000000000),App.Vector(6.34999999999999,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC").addGeometry(Part.LineSegment(App.Vector(-6.34999999999999,12.70000000000000,0.00000000000000),App.Vector(-6.34999999999999,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Pad","Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC")
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC")
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").Length = 457.20000000000005
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrfXEIEUd8hq7Sa_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrfXEIEUd8hq7Sa_1_FF1EZL7EWdpWuS2_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Plane", "plane_Sketch_FxLCq0ibTbYIBgC_1_JhC")
origin = App.Vector(-228.59999999999999,196.84999999999999,76.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxLCq0ibTbYIBgC_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("Sketcher::SketchObject","Sketch_FxLCq0ibTbYIBgC_1_JhC")
App.ActiveDocument.getObject("Sketch_FxLCq0ibTbYIBgC_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxLCq0ibTbYIBgC_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_FxLCq0ibTbYIBgC_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxLCq0ibTbYIBgC_1_JhC").addGeometry(Part.Circle(App.Vector(203.19999999999999,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxLCq0ibTbYIBgC_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxLCq0ibTbYIBgC_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FarlXj9y4gltcQN_0").newObject("PartDesign::Pocket","Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC")
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_FxLCq0ibTbYIBgC_1_JhC")
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxLCq0ibTbYIBgC_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxLCq0ibTbYIBgC_1_FdrobMdMj0VZRuh_1_JhC").Offset = 0
App.ActiveDocument.recompute()

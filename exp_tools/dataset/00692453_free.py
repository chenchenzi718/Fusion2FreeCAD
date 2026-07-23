import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00692453")
App.ActiveDocument.addObject("PartDesign::Body","Body_FuS2SKfNy6XVZjO_0")
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").Label = "Body_FuS2SKfNy6XVZjO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FuS2SKfNy6XVZjO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuS2SKfNy6XVZjO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FuS2SKfNy6XVZjO_0_JGC")
App.ActiveDocument.getObject("Sketch_FuS2SKfNy6XVZjO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuS2SKfNy6XVZjO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FuS2SKfNy6XVZjO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuS2SKfNy6XVZjO_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),75.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuS2SKfNy6XVZjO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuS2SKfNy6XVZjO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pad","Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC")
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FuS2SKfNy6XVZjO_0_JGC")
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuS2SKfNy6XVZjO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuS2SKfNy6XVZjO_0_FXeIOw3apPUlvWB_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FArk2fb7DJlvBDR_1_JLG")
origin = App.Vector(0.00000000000000,0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FArk2fb7DJlvBDR_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FArk2fb7DJlvBDR_1_JLG")
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FArk2fb7DJlvBDR_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLG").addGeometry(Part.Circle(App.Vector(-33.64153000000000,36.98983000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pocket","Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG")
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLG")
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").Length = 20.0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FArk2fb7DJlvBDR_1_JLC")
origin = App.Vector(0.00000000000000,0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FArk2fb7DJlvBDR_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FArk2fb7DJlvBDR_1_JLC")
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FArk2fb7DJlvBDR_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLC").addGeometry(Part.Circle(App.Vector(36.98983000000000,33.64153000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pocket","Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC")
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLC")
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FArk2fb7DJlvBDR_1_JLO")
origin = App.Vector(0.00000000000000,0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FArk2fb7DJlvBDR_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FArk2fb7DJlvBDR_1_JLO")
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FArk2fb7DJlvBDR_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLO").addGeometry(Part.Circle(App.Vector(33.64153000000000,-36.98983000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pocket","Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO")
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLO")
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").Length = 20.0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FArk2fb7DJlvBDR_1_JLK")
origin = App.Vector(0.00000000000000,0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FArk2fb7DJlvBDR_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FArk2fb7DJlvBDR_1_JLK")
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FArk2fb7DJlvBDR_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLK").addGeometry(Part.Circle(App.Vector(-36.98983000000000,-33.64153000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pocket","Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK")
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLK")
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").Length = 20.0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FArk2fb7DJlvBDR_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FArk2fb7DJlvBDR_1_F4kZ5W2O2gDfsRC_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FycnbE0EerBAP7W_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FycnbE0EerBAP7W_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FycnbE0EerBAP7W_1_JJC")
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FycnbE0EerBAP7W_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,50.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pocket","Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC")
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJC")
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FycnbE0EerBAP7W_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FycnbE0EerBAP7W_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FycnbE0EerBAP7W_1_JJO")
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FycnbE0EerBAP7W_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJO").addGeometry(Part.Circle(App.Vector(50.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pocket","Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO")
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJO")
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").Length = 20.0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FycnbE0EerBAP7W_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FycnbE0EerBAP7W_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FycnbE0EerBAP7W_1_JJK")
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FycnbE0EerBAP7W_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJK").addGeometry(Part.Circle(App.Vector(0.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pocket","Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK")
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJK")
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").Length = 20.0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FycnbE0EerBAP7W_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FycnbE0EerBAP7W_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FycnbE0EerBAP7W_1_JJG")
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FycnbE0EerBAP7W_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJG").addGeometry(Part.Circle(App.Vector(-50.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pocket","Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG")
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJG")
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").Length = 20.0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FycnbE0EerBAP7W_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FycnbE0EerBAP7W_1_FKmmQ9njFc6etwE_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Plane", "plane_Sketch_FWxMhhNtmGCi3CV_1_JdC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWxMhhNtmGCi3CV_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("Sketcher::SketchObject","Sketch_FWxMhhNtmGCi3CV_1_JdC")
App.ActiveDocument.getObject("Sketch_FWxMhhNtmGCi3CV_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWxMhhNtmGCi3CV_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FWxMhhNtmGCi3CV_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWxMhhNtmGCi3CV_1_JdC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWxMhhNtmGCi3CV_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWxMhhNtmGCi3CV_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuS2SKfNy6XVZjO_0").newObject("PartDesign::Pocket","Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC")
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FWxMhhNtmGCi3CV_1_JdC")
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWxMhhNtmGCi3CV_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWxMhhNtmGCi3CV_1_Fg3hNLgx77isNZI_1_JdC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00884648")
App.ActiveDocument.addObject("PartDesign::Body","Body_FBThfQTyxhsrd9i_0")
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").Label = "Body_FBThfQTyxhsrd9i_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Plane", "plane_Sketch_FBThfQTyxhsrd9i_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBThfQTyxhsrd9i_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("Sketcher::SketchObject","Sketch_FBThfQTyxhsrd9i_0_JGC")
App.ActiveDocument.getObject("Sketch_FBThfQTyxhsrd9i_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBThfQTyxhsrd9i_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FBThfQTyxhsrd9i_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBThfQTyxhsrd9i_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),76.20000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBThfQTyxhsrd9i_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBThfQTyxhsrd9i_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Pad","Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC")
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FBThfQTyxhsrd9i_0_JGC")
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBThfQTyxhsrd9i_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FBThfQTyxhsrd9i_0_FFTPZsf0t6cPqMZ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Plane", "plane_Sketch_FbA34PhHmWRQ3nA_0_JIC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("Sketcher::SketchObject","Sketch_FbA34PhHmWRQ3nA_0_JIC")
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIC"), [""])
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIC").addGeometry(Part.Circle(App.Vector(0.00000000000000,63.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Pocket","Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").Profile = App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIC")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").Type = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Plane", "plane_Sketch_FbA34PhHmWRQ3nA_0_JIG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("Sketcher::SketchObject","Sketch_FbA34PhHmWRQ3nA_0_JIG")
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIG"), [""])
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIG").addGeometry(Part.Circle(App.Vector(63.50000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Pocket","Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").Profile = App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIG")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").Type = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").Midplane = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Plane", "plane_Sketch_FbA34PhHmWRQ3nA_0_JIK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("Sketcher::SketchObject","Sketch_FbA34PhHmWRQ3nA_0_JIK")
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIK"), [""])
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIK").addGeometry(Part.Circle(App.Vector(-63.50000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Pocket","Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").Profile = App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIK")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").Type = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").Midplane = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Plane", "plane_Sketch_FbA34PhHmWRQ3nA_0_JIO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("Sketcher::SketchObject","Sketch_FbA34PhHmWRQ3nA_0_JIO")
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIO"), [""])
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIO").addGeometry(Part.Circle(App.Vector(0.00000000000000,-63.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Pocket","Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").Profile = App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIO")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").Type = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").Midplane = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Plane", "plane_Sketch_FbA34PhHmWRQ3nA_0_JIS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("Sketcher::SketchObject","Sketch_FbA34PhHmWRQ3nA_0_JIS")
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIS"), [""])
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIS").addGeometry(Part.Circle(App.Vector(-44.90128000000000,44.90128000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Pocket","Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").Profile = App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIS")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").Type = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").Midplane = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Plane", "plane_Sketch_FbA34PhHmWRQ3nA_0_JIW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("Sketcher::SketchObject","Sketch_FbA34PhHmWRQ3nA_0_JIW")
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIW"), [""])
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIW").addGeometry(Part.Circle(App.Vector(44.90128000000000,44.90128000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Pocket","Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").Profile = App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIW")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").Type = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").Midplane = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Plane", "plane_Sketch_FbA34PhHmWRQ3nA_0_JIa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("Sketcher::SketchObject","Sketch_FbA34PhHmWRQ3nA_0_JIa")
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIa"), [""])
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIa").addGeometry(Part.Circle(App.Vector(44.90128000000000,-44.90128000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Pocket","Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").Profile = App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIa")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").Type = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").Midplane = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Plane", "plane_Sketch_FbA34PhHmWRQ3nA_0_JIe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("Sketcher::SketchObject","Sketch_FbA34PhHmWRQ3nA_0_JIe")
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbA34PhHmWRQ3nA_0_JIe"), [""])
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIe").addGeometry(Part.Circle(App.Vector(-44.90128000000000,-44.90128000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBThfQTyxhsrd9i_0").newObject("PartDesign::Pocket","Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").Profile = App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIe")
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbA34PhHmWRQ3nA_0_JIe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").Type = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").Midplane = 1
App.ActiveDocument.getObject("Extrude_FbA34PhHmWRQ3nA_0_F0K1kuBRLze8xrv_1_JIe").Offset = 0
App.ActiveDocument.recompute()

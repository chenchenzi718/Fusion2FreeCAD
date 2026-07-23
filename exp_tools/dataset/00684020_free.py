import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00684020")
App.ActiveDocument.addObject("PartDesign::Body","Body_F1sZ971wsy3dCdw_0")
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").Label = "Body_F1sZ971wsy3dCdw_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Plane", "plane_Sketch_F1sZ971wsy3dCdw_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1sZ971wsy3dCdw_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("Sketcher::SketchObject","Sketch_F1sZ971wsy3dCdw_0_JGC")
App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1sZ971wsy3dCdw_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1200.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC").addGeometry(Part.LineSegment(App.Vector(1200.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1200.00000000000000,900.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,900.00000000000000,0.00000000000000),App.Vector(1200.00000000000000,900.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,900.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Pad","Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC")
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC")
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").Length = 22.0
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1sZ971wsy3dCdw_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1sZ971wsy3dCdw_0_F83J3m163qSdbqv_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Plane", "plane_Sketch_FTvzJTvKsXauKSW_1_JJC")
origin = App.Vector(600.00000000000000,450.00000000000000,22.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTvzJTvKsXauKSW_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("Sketcher::SketchObject","Sketch_FTvzJTvKsXauKSW_1_JJC")
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTvzJTvKsXauKSW_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJC").addGeometry(Part.Circle(App.Vector(-540.00000000000000,394.99999999999994,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Pocket","Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC")
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJC")
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Plane", "plane_Sketch_FTvzJTvKsXauKSW_1_JJK")
origin = App.Vector(600.00000000000000,450.00000000000000,22.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTvzJTvKsXauKSW_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("Sketcher::SketchObject","Sketch_FTvzJTvKsXauKSW_1_JJK")
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTvzJTvKsXauKSW_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJK").addGeometry(Part.Circle(App.Vector(539.99999999999989,394.99999999999994,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Pocket","Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK")
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJK")
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Plane", "plane_Sketch_FTvzJTvKsXauKSW_1_JJO")
origin = App.Vector(600.00000000000000,450.00000000000000,22.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTvzJTvKsXauKSW_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("Sketcher::SketchObject","Sketch_FTvzJTvKsXauKSW_1_JJO")
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTvzJTvKsXauKSW_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJO").addGeometry(Part.Circle(App.Vector(539.99999999999989,-425.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Pocket","Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO")
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJO")
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Plane", "plane_Sketch_FTvzJTvKsXauKSW_1_JJG")
origin = App.Vector(600.00000000000000,450.00000000000000,22.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTvzJTvKsXauKSW_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("Sketcher::SketchObject","Sketch_FTvzJTvKsXauKSW_1_JJG")
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTvzJTvKsXauKSW_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJG").addGeometry(Part.Circle(App.Vector(-540.00000000000000,-425.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Pocket","Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG")
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJG")
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTvzJTvKsXauKSW_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTvzJTvKsXauKSW_1_F8zwMsFvyMe4JZt_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Plane", "plane_Sketch_FF4R89GqRDTBNVq_1_JNO")
origin = App.Vector(600.00000000000000,450.00000000000000,22.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FF4R89GqRDTBNVq_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("Sketcher::SketchObject","Sketch_FF4R89GqRDTBNVq_1_JNO")
App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FF4R89GqRDTBNVq_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO").addGeometry(Part.LineSegment(App.Vector(477.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(515.00000000000000,-450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO").addGeometry(Part.LineSegment(App.Vector(515.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(515.00000000000000,-408.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO").addGeometry(Part.LineSegment(App.Vector(515.00000000000000,-408.00000000000006,0.00000000000000),App.Vector(477.00000000000000,-408.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO").addGeometry(Part.LineSegment(App.Vector(477.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(477.00000000000000,-408.00000000000006,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Pad","Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO")
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO")
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").Length = 1.0
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Plane", "plane_Sketch_FF4R89GqRDTBNVq_1_JNK")
origin = App.Vector(600.00000000000000,450.00000000000000,22.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FF4R89GqRDTBNVq_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("Sketcher::SketchObject","Sketch_FF4R89GqRDTBNVq_1_JNK")
App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FF4R89GqRDTBNVq_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK").addGeometry(Part.LineSegment(App.Vector(-515.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(-477.00000000000000,-450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK").addGeometry(Part.LineSegment(App.Vector(-477.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(-477.00000000000000,-408.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK").addGeometry(Part.LineSegment(App.Vector(-515.00000000000000,-408.00000000000006,0.00000000000000),App.Vector(-477.00000000000000,-408.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK").addGeometry(Part.LineSegment(App.Vector(-515.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(-515.00000000000000,-408.00000000000006,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Pad","Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK")
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK")
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").Length = 1.0
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FF4R89GqRDTBNVq_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FF4R89GqRDTBNVq_1_F5txp7yqytTBPF2_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Plane", "plane_Sketch_FGNwIcR3Ah9S19z_1_JRC")
origin = App.Vector(600.00000000000000,450.00000000000000,22.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGNwIcR3Ah9S19z_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("Sketcher::SketchObject","Sketch_FGNwIcR3Ah9S19z_1_JRC")
App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGNwIcR3Ah9S19z_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC").addGeometry(Part.LineSegment(App.Vector(-600.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(-559.99999999999989,-450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC").addGeometry(Part.LineSegment(App.Vector(-559.99999999999989,-450.00000000000000,0.00000000000000),App.Vector(-559.99999999999989,450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC").addGeometry(Part.LineSegment(App.Vector(-600.00000000000000,450.00000000000000,0.00000000000000),App.Vector(-559.99999999999989,450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC").addGeometry(Part.LineSegment(App.Vector(-600.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(-600.00000000000000,450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Pocket","Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC")
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC")
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Plane", "plane_Sketch_FGNwIcR3Ah9S19z_1_JRG")
origin = App.Vector(600.00000000000000,450.00000000000000,22.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGNwIcR3Ah9S19z_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("Sketcher::SketchObject","Sketch_FGNwIcR3Ah9S19z_1_JRG")
App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGNwIcR3Ah9S19z_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG").addGeometry(Part.LineSegment(App.Vector(600.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(559.99999999999989,-450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG").addGeometry(Part.LineSegment(App.Vector(559.99999999999989,-450.00000000000000,0.00000000000000),App.Vector(559.99999999999989,450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG").addGeometry(Part.LineSegment(App.Vector(600.00000000000000,450.00000000000000,0.00000000000000),App.Vector(559.99999999999989,450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG").addGeometry(Part.LineSegment(App.Vector(600.00000000000000,-450.00000000000000,0.00000000000000),App.Vector(600.00000000000000,450.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1sZ971wsy3dCdw_0").newObject("PartDesign::Pocket","Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG")
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG")
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGNwIcR3Ah9S19z_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGNwIcR3Ah9S19z_1_F7GzSWBH92SsECu_1_JRG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00162991")
App.ActiveDocument.addObject("PartDesign::Body","Body_FVuceK08TrvOOwT_0")
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").Label = "Body_FVuceK08TrvOOwT_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Plane", "plane_Sketch_FVuceK08TrvOOwT_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVuceK08TrvOOwT_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("Sketcher::SketchObject","Sketch_FVuceK08TrvOOwT_0_JGC")
App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVuceK08TrvOOwT_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC").addGeometry(Part.LineSegment(App.Vector(330.19999999999999,-152.40000000000001,0.00000000000000),App.Vector(-330.19999999999999,-152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC").addGeometry(Part.LineSegment(App.Vector(-330.19999999999999,-152.40000000000001,0.00000000000000),App.Vector(-330.19999999999999,152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC").addGeometry(Part.LineSegment(App.Vector(330.19999999999999,152.40000000000001,0.00000000000000),App.Vector(-330.19999999999999,152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC").addGeometry(Part.LineSegment(App.Vector(330.19999999999999,-152.40000000000001,0.00000000000000),App.Vector(330.19999999999999,152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Pad","Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC")
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC")
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVuceK08TrvOOwT_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVuceK08TrvOOwT_0_FaskupcGwEAr6UQ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Plane", "plane_Sketch_FjGPbQeuknu55R7_1_JJG")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjGPbQeuknu55R7_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("Sketcher::SketchObject","Sketch_FjGPbQeuknu55R7_1_JJG")
App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjGPbQeuknu55R7_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG").addGeometry(Part.LineSegment(App.Vector(279.39999999999998,-152.40000000000001,0.00000000000000),App.Vector(228.59999999999999,-152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG").addGeometry(Part.LineSegment(App.Vector(228.59999999999999,-152.40000000000001,0.00000000000000),App.Vector(228.59999999999999,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG").addGeometry(Part.LineSegment(App.Vector(228.59999999999999,-101.59999999999999,0.00000000000000),App.Vector(279.39999999999998,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG").addGeometry(Part.LineSegment(App.Vector(279.39999999999998,-152.40000000000001,0.00000000000000),App.Vector(279.39999999999998,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Pad","Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG")
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG")
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Plane", "plane_Sketch_FjGPbQeuknu55R7_1_JJK")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjGPbQeuknu55R7_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("Sketcher::SketchObject","Sketch_FjGPbQeuknu55R7_1_JJK")
App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjGPbQeuknu55R7_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-101.59999999999999,0.00000000000000),App.Vector(-25.40000000000000,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-101.59999999999999,0.00000000000000),App.Vector(-25.40000000000000,-152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-152.40000000000001,0.00000000000000),App.Vector(-25.40000000000000,-152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-101.59999999999999,0.00000000000000),App.Vector(25.40000000000000,-152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Pad","Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK")
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK")
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Plane", "plane_Sketch_FjGPbQeuknu55R7_1_JJC")
origin = App.Vector(-0.00000000000000,-6.35000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjGPbQeuknu55R7_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("Sketcher::SketchObject","Sketch_FjGPbQeuknu55R7_1_JJC")
App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjGPbQeuknu55R7_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-152.40000000000001,0.00000000000000),App.Vector(-203.19999999999999,-152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC").addGeometry(Part.LineSegment(App.Vector(-203.19999999999999,-152.40000000000001,0.00000000000000),App.Vector(-203.19999999999999,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC").addGeometry(Part.LineSegment(App.Vector(-203.19999999999999,-101.59999999999999,0.00000000000000),App.Vector(-152.40000000000001,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-152.40000000000001,0.00000000000000),App.Vector(-152.40000000000001,-101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Pad","Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC")
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC")
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjGPbQeuknu55R7_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjGPbQeuknu55R7_1_FpkcQot1VkVhoAd_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Plane", "plane_Sketch_FSBcSP5Cnmle2BX_1_JNC")
origin = App.Vector(-177.80000000000001,-12.70000000000000,-123.82500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSBcSP5Cnmle2BX_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("Sketcher::SketchObject","Sketch_FSBcSP5Cnmle2BX_1_JNC")
App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSBcSP5Cnmle2BX_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC").addGeometry(Part.LineSegment(App.Vector(-25.39999999999998,-22.22500000000001,0.00000000000000),App.Vector(25.40000000000001,-22.22500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC").addGeometry(Part.LineSegment(App.Vector(25.40000000000001,-28.57500000000000,0.00000000000000),App.Vector(25.40000000000001,-22.22500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC").addGeometry(Part.LineSegment(App.Vector(25.40000000000001,-28.57500000000000,0.00000000000000),App.Vector(-25.39999999999998,-28.57500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC").addGeometry(Part.LineSegment(App.Vector(-25.39999999999998,-28.57500000000000,0.00000000000000),App.Vector(-25.39999999999998,-22.22500000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Pad","Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC")
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC")
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").Length = 44.45
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Plane", "plane_Sketch_FSBcSP5Cnmle2BX_1_JPC")
origin = App.Vector(0.00000000000000,-12.70000000000000,-123.82500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSBcSP5Cnmle2BX_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("Sketcher::SketchObject","Sketch_FSBcSP5Cnmle2BX_1_JPC")
App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSBcSP5Cnmle2BX_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-22.22500000000001,0.00000000000000),App.Vector(25.40000000000000,-22.22500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-28.57500000000000,0.00000000000000),App.Vector(25.40000000000000,-22.22500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-28.57500000000000,0.00000000000000),App.Vector(-25.40000000000000,-28.57500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-28.57500000000000,0.00000000000000),App.Vector(-25.40000000000000,-22.22500000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Pad","Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC")
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC")
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").Length = 44.45
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Plane", "plane_Sketch_FSBcSP5Cnmle2BX_1_JRC")
origin = App.Vector(254.00000000000000,-12.70000000000000,-123.82500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSBcSP5Cnmle2BX_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("Sketcher::SketchObject","Sketch_FSBcSP5Cnmle2BX_1_JRC")
App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSBcSP5Cnmle2BX_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000001,-22.22500000000001,0.00000000000000),App.Vector(25.39999999999998,-22.22500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC").addGeometry(Part.LineSegment(App.Vector(25.39999999999998,-28.57500000000000,0.00000000000000),App.Vector(25.39999999999998,-22.22500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC").addGeometry(Part.LineSegment(App.Vector(25.39999999999998,-28.57500000000000,0.00000000000000),App.Vector(-25.40000000000001,-28.57500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC").addGeometry(Part.LineSegment(App.Vector(-25.40000000000001,-28.57500000000000,0.00000000000000),App.Vector(-25.40000000000001,-22.22500000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Pad","Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC")
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC")
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").Length = 44.45
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSBcSP5Cnmle2BX_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSBcSP5Cnmle2BX_1_FbsbAISdbPBN1jt_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Plane", "plane_Sketch_FKh8s1TCT27FYFO_1_JVC")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKh8s1TCT27FYFO_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("Sketcher::SketchObject","Sketch_FKh8s1TCT27FYFO_1_JVC")
App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKh8s1TCT27FYFO_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-431.80000000000001,76.20000000000000,0.00000000000000),App.Vector(-330.19999999999999,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-330.19999999999999,76.20000000000000,0.00000000000000),App.Vector(-330.19999999999999,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-431.80000000000001,127.00000000000000,0.00000000000000),App.Vector(-330.19999999999999,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-431.80000000000001,76.20000000000000,0.00000000000000),App.Vector(-431.80000000000001,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Pad","Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC")
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC")
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").Length = 9.525
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Plane", "plane_Sketch_FKh8s1TCT27FYFO_1_JVG")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKh8s1TCT27FYFO_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("Sketcher::SketchObject","Sketch_FKh8s1TCT27FYFO_1_JVG")
App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKh8s1TCT27FYFO_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG").addGeometry(Part.LineSegment(App.Vector(-228.59999999999999,76.20000000000000,0.00000000000000),App.Vector(-330.19999999999999,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG").addGeometry(Part.LineSegment(App.Vector(-330.19999999999999,76.20000000000000,0.00000000000000),App.Vector(-330.19999999999999,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG").addGeometry(Part.LineSegment(App.Vector(-228.59999999999999,127.00000000000000,0.00000000000000),App.Vector(-330.19999999999999,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG").addGeometry(Part.LineSegment(App.Vector(-228.59999999999999,76.20000000000000,0.00000000000000),App.Vector(-228.59999999999999,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVuceK08TrvOOwT_0").newObject("PartDesign::Pad","Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG")
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG")
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").Length = 9.525
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKh8s1TCT27FYFO_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKh8s1TCT27FYFO_1_Fi7uyhuNuliSs1E_1_JVG").Offset = 0
App.ActiveDocument.recompute()

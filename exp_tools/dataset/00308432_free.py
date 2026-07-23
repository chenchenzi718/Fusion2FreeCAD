import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00308432")
App.ActiveDocument.addObject("PartDesign::Body","Body_FUI4YXRPis3krwR_0")
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").Label = "Body_FUI4YXRPis3krwR_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Plane", "plane_Sketch_FUI4YXRPis3krwR_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUI4YXRPis3krwR_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("Sketcher::SketchObject","Sketch_FUI4YXRPis3krwR_0_JGC")
App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUI4YXRPis3krwR_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,25.40000000000000,0.00000000000000),App.Vector(6.35000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,25.40000000000000,0.00000000000000),App.Vector(6.35000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(6.35000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Pad","Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC")
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC")
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUI4YXRPis3krwR_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FUI4YXRPis3krwR_0_FPXa01PrH7JaENh_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Plane", "plane_Sketch_F3QRLyNk8rsSKIS_1_JJC")
origin = App.Vector(12.70000000000000,-12.70000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3QRLyNk8rsSKIS_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("Sketcher::SketchObject","Sketch_F3QRLyNk8rsSKIS_1_JJC")
App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3QRLyNk8rsSKIS_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,-3.17500000000000,0.00000000000000),App.Vector(6.35000000000000,-3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-3.17500000000000,0.00000000000000),App.Vector(6.35000000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,3.17500000000000,0.00000000000000),App.Vector(-6.35000000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,-3.17500000000000,0.00000000000000),App.Vector(-6.35000000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Pad","Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC")
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC")
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3QRLyNk8rsSKIS_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3QRLyNk8rsSKIS_1_FisvcoxwMcag9dc_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Plane", "plane_Sketch_FwFATF2oqQNP6gJ_1_JNC")
origin = App.Vector(19.05000000000000,12.70000000000000,12.70000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwFATF2oqQNP6gJ_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("Sketcher::SketchObject","Sketch_FwFATF2oqQNP6gJ_1_JNC")
App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwFATF2oqQNP6gJ_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-12.70000000000000,0.00000000000000),App.Vector(-19.05000000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,-12.70000000000000,0.00000000000000),App.Vector(-19.05000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-12.70000000000000,0.00000000000000),App.Vector(0.00000000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Pad","Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC")
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC")
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwFATF2oqQNP6gJ_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwFATF2oqQNP6gJ_1_FjIFTEBQ8Znr9f6_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Plane", "plane_Sketch_FUps0GII4HWfbmF_1_JRC")
origin = App.Vector(38.10000000000000,6.35000000000000,12.77620000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUps0GII4HWfbmF_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("Sketcher::SketchObject","Sketch_FUps0GII4HWfbmF_1_JRC")
App.ActiveDocument.getObject("Sketch_FUps0GII4HWfbmF_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUps0GII4HWfbmF_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FUps0GII4HWfbmF_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUps0GII4HWfbmF_1_JRC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-0.07620000000000,0.00000000000000),App.Vector(6.35000000000000,12.62380000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUps0GII4HWfbmF_1_JRC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,-0.07620000000000,0.00000000000000),App.Vector(6.35000000000000,12.62380000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUps0GII4HWfbmF_1_JRC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,-0.07620000000000,0.00000000000000),App.Vector(-6.35000000000000,-0.07620000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUps0GII4HWfbmF_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUps0GII4HWfbmF_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Pad","Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC")
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FUps0GII4HWfbmF_1_JRC")
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").Length = 19.05
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUps0GII4HWfbmF_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUps0GII4HWfbmF_1_Fbi2S7mhTnENoS7_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Plane", "plane_Sketch_FmfmzMVedEQ20pJ_1_JVC")
origin = App.Vector(0.00000000000000,-0.07620000000000,12.77620000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmfmzMVedEQ20pJ_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("Sketcher::SketchObject","Sketch_FmfmzMVedEQ20pJ_1_JVC")
App.ActiveDocument.getObject("Sketch_FmfmzMVedEQ20pJ_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmfmzMVedEQ20pJ_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FmfmzMVedEQ20pJ_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmfmzMVedEQ20pJ_1_JVC").addGeometry(Part.LineSegment(App.Vector(12.62380000000000,-12.77620000000000,0.00000000000000),App.Vector(-12.77620000000000,12.62380000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmfmzMVedEQ20pJ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-12.77620000000000,12.62380000000000,0.00000000000000),App.Vector(12.62380000000000,12.62380000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmfmzMVedEQ20pJ_1_JVC").addGeometry(Part.LineSegment(App.Vector(12.62380000000000,-12.77620000000000,0.00000000000000),App.Vector(12.62380000000000,12.62380000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmfmzMVedEQ20pJ_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmfmzMVedEQ20pJ_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Pocket","Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC")
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FmfmzMVedEQ20pJ_1_JVC")
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmfmzMVedEQ20pJ_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmfmzMVedEQ20pJ_1_FxPRMTl9dYYCt5W_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Plane", "plane_Sketch_FLULBYB0nejTObg_1_JZC")
origin = App.Vector(12.70000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLULBYB0nejTObg_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("Sketcher::SketchObject","Sketch_FLULBYB0nejTObg_1_JZC")
App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLULBYB0nejTObg_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZC").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,-6.35000000000000,0.00000000000000),App.Vector(3.17500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,-6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),3.14159265358979,0.0),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Pocket","Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC")
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZC")
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Plane", "plane_Sketch_FLULBYB0nejTObg_1_JZG")
origin = App.Vector(12.70000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLULBYB0nejTObg_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("Sketcher::SketchObject","Sketch_FLULBYB0nejTObg_1_JZG")
App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLULBYB0nejTObg_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZG").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,6.34894000000000,0.00000000000000),App.Vector(3.17500000000000,6.34894000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,6.34894000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),0.0,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Pocket","Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG")
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZG")
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Plane", "plane_Sketch_FLULBYB0nejTObg_1_JZK")
origin = App.Vector(12.70000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLULBYB0nejTObg_1_JZK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("Sketcher::SketchObject","Sketch_FLULBYB0nejTObg_1_JZK")
App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLULBYB0nejTObg_1_JZK"), [""])
App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,6.34894000000000,0.00000000000000),App.Vector(-3.17500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,-6.35000000000000,0.00000000000000),App.Vector(3.17500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,-6.35000000000000,0.00000000000000),App.Vector(3.17500000000000,6.34894000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,6.34894000000000,0.00000000000000),App.Vector(3.17500000000000,6.34894000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUI4YXRPis3krwR_0").newObject("PartDesign::Pocket","Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK")
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").Profile = App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK")
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLULBYB0nejTObg_1_JZK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").Type = 4
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLULBYB0nejTObg_1_F4DnFSqWq0vjATA_1_JZK").Offset = 0
App.ActiveDocument.recompute()

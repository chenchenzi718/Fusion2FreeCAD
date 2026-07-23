import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00087218")
App.ActiveDocument.addObject("PartDesign::Body","Body_FO4EBVPGVf2DGPc_0")
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").Label = "Body_FO4EBVPGVf2DGPc_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Plane", "plane_Sketch_FO4EBVPGVf2DGPc_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FO4EBVPGVf2DGPc_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("Sketcher::SketchObject","Sketch_FO4EBVPGVf2DGPc_0_JGC")
App.ActiveDocument.getObject("Sketch_FO4EBVPGVf2DGPc_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FO4EBVPGVf2DGPc_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FO4EBVPGVf2DGPc_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FO4EBVPGVf2DGPc_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),25.40000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FO4EBVPGVf2DGPc_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FO4EBVPGVf2DGPc_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Pad","Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC")
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FO4EBVPGVf2DGPc_0_JGC")
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FO4EBVPGVf2DGPc_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FO4EBVPGVf2DGPc_0_FZioPluzMRJPoIp_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Plane", "plane_Sketch_FyZqdcBZEkrzVgR_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyZqdcBZEkrzVgR_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("Sketcher::SketchObject","Sketch_FyZqdcBZEkrzVgR_1_JJC")
App.ActiveDocument.getObject("Sketch_FyZqdcBZEkrzVgR_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyZqdcBZEkrzVgR_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FyZqdcBZEkrzVgR_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyZqdcBZEkrzVgR_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyZqdcBZEkrzVgR_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyZqdcBZEkrzVgR_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Pad","Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC")
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FyZqdcBZEkrzVgR_1_JJC")
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyZqdcBZEkrzVgR_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyZqdcBZEkrzVgR_1_FG2pklQ2hNMtWCn_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Plane", "plane_Sketch_Ff3DPQDhS4iq9mb_1_JNu")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff3DPQDhS4iq9mb_1_JNu").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("Sketcher::SketchObject","Sketch_Ff3DPQDhS4iq9mb_1_JNu")
App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff3DPQDhS4iq9mb_1_JNu"), [""])
App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(-24.84495000000000,5.28096000000000,0.00000000000000),App.Vector(-16.99592000000000,18.87588000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(-16.99592000000000,18.87588000000000,0.00000000000000),App.Vector(-2.65502000000000,25.26086000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(-2.65502000000000,25.26086000000000,0.00000000000000),App.Vector(12.70000000000000,21.99705000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(12.70000000000000,21.99705000000000,0.00000000000000),App.Vector(23.20405000000000,10.33111000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(23.20405000000000,10.33111000000000,0.00000000000000),App.Vector(24.84495000000000,-5.28096000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(24.84495000000000,-5.28096000000000,0.00000000000000),App.Vector(16.99592000000000,-18.87588000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(16.99592000000000,-18.87588000000000,0.00000000000000),App.Vector(2.65502000000000,-25.26086000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(2.65502000000000,-25.26086000000000,0.00000000000000),App.Vector(-12.70000000000000,-21.99705000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(-12.70000000000000,-21.99705000000000,0.00000000000000),App.Vector(-23.20405000000000,-10.33111000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(-23.20405000000000,-10.33111000000000,0.00000000000000),App.Vector(-24.28990000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").addGeometry(Part.LineSegment(App.Vector(-24.84495000000000,5.28096000000000,0.00000000000000),App.Vector(-24.28990000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Pad","Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu")
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").Profile = App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu")
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff3DPQDhS4iq9mb_1_JNu"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").Type = 0
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").Reversed = 1
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff3DPQDhS4iq9mb_1_FKHrTggKOxM1FDS_1_JNu").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Plane", "plane_Sketch_FMJkRQJJpRhbJYB_1_JRC")
origin = App.Vector(17.92052000000000,16.19908000000000,-1.58750000000000)
x_axis=App.Vector(-0.66913061000000,0.74314483000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000001159470)
z_axis=App.Vector(0.74314483000000,0.66913061000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMJkRQJJpRhbJYB_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("Sketcher::SketchObject","Sketch_FMJkRQJJpRhbJYB_1_JRC")
App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMJkRQJJpRhbJYB_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(7.80194116211230,1.58750001840659,-0.00000324504990),App.Vector(22.73168466253859,-3.26347003783896,-0.00000558678280)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(22.73168466253859,-3.26347003783896,-0.00000558678280),App.Vector(31.95877272365770,-15.96347018509166,-0.00000963542410)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(31.95877272365770,-15.96347018509166,-0.00000963542410),App.Vector(31.95877272365770,-31.66153036710597,-0.00000963542410)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(31.95877272365770,-31.66153036710597,-0.00000963542410),App.Vector(22.73168466253859,-44.36153051435868,-0.00000558678280)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(22.73168466253859,-44.36153051435868,-0.00000558678280),App.Vector(7.80194116211230,-49.21250057060422,-0.00000324504990)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(7.80194116211230,-49.21250057060422,-0.00000324504990),App.Vector(-7.12780976976230,-44.36153051435868,-0.00000759462310)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(-7.12780976976230,-44.36153051435868,-0.00000759462310),App.Vector(-16.35489783088140,-31.66153036710597,-0.00000354598180)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(-16.35489783088140,-31.66153036710597,-0.00000354598180),App.Vector(-16.35489783088140,-15.96347018509166,-0.00000354598180)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(-16.35489783088140,-15.96347018509166,-0.00000354598180),App.Vector(-7.12780976976230,-3.26347003783896,-0.00000759462310)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(-7.12780976976230,-3.26347003783896,-0.00000759462310),App.Vector(-1.96970799193130,-1.58750001840659,-0.00000254981410)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(7.80194116211230,-1.58750001840659,-0.00000324504990),App.Vector(-1.96970799193130,-1.58750001840659,-0.00000254981410)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").addGeometry(Part.LineSegment(App.Vector(7.80194116211230,-1.58750001840659,-0.00000324504990),App.Vector(7.80194116211230,1.58750001840659,-0.00000324504990)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Pad","Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC")
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC")
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Plane", "plane_Sketch_FMJkRQJJpRhbJYB_1_JRK")
origin = App.Vector(17.92052000000000,16.19908000000000,-1.58750000000000)
x_axis=App.Vector(-0.66913061000000,0.74314483000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000001159470)
z_axis=App.Vector(0.74314483000000,0.66913061000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMJkRQJJpRhbJYB_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("Sketcher::SketchObject","Sketch_FMJkRQJJpRhbJYB_1_JRK")
App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMJkRQJJpRhbJYB_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRK").addGeometry(Part.LineSegment(App.Vector(7.80194116211230,1.58750001840659,-0.00000324504990),App.Vector(-1.96970799193130,-1.58750001840659,-0.00000254981410)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRK").addGeometry(Part.LineSegment(App.Vector(7.80194116211230,-1.58750001840659,-0.00000324504990),App.Vector(-1.96970799193130,-1.58750001840659,-0.00000254981410)),False)

App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRK").addGeometry(Part.LineSegment(App.Vector(7.80194116211230,-1.58750001840659,-0.00000324504990),App.Vector(7.80194116211230,1.58750001840659,-0.00000324504990)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Pad","Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK")
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRK")
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMJkRQJJpRhbJYB_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMJkRQJJpRhbJYB_1_FcO5e1Nd36IN03B_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Plane", "plane_Sketch_FXt1cT9jtTw7hc8_1_JVC")
origin = App.Vector(15.05948000000000,24.12153000000000,-25.40000000000000)
x_axis=App.Vector(-0.66913061000000,0.74314483000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000001159470)
z_axis=App.Vector(0.74314483000000,0.66913061000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXt1cT9jtTw7hc8_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("Sketcher::SketchObject","Sketch_FXt1cT9jtTw7hc8_1_JVC")
App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXt1cT9jtTw7hc8_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").addGeometry(Part.LineSegment(App.Vector(3.17499739326950,1.83309002125413,0.00001065455050),App.Vector(3.17499739326950,-1.83309002125413,0.00001065455050)),False)

App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").addGeometry(Part.LineSegment(App.Vector(3.17499739326950,-1.83309002125413,0.00001065455050),App.Vector(0.00000000000000,-3.66617004250814,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-3.66617004250814,0.00000000000000),App.Vector(-3.17499665312730,-1.83309002125413,0.00000346820390)),False)

App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").addGeometry(Part.LineSegment(App.Vector(-3.17499665312730,-1.83309002125413,0.00000346820390),App.Vector(-3.17499665312730,1.83309002125413,0.00000346820390)),False)

App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").addGeometry(Part.LineSegment(App.Vector(-3.17499665312730,1.83309002125413,0.00000346820390),App.Vector(0.00000000000000,3.66617004250814,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").addGeometry(Part.LineSegment(App.Vector(3.17499739326950,1.83309002125413,0.00001065455050),App.Vector(0.00000000000000,3.66617004250814,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Pad","Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC")
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC")
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXt1cT9jtTw7hc8_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXt1cT9jtTw7hc8_1_FQfdUE4JadXfaLg_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Plane", "plane_Sketch_FnmdhTqweiTOyKD_1_JZC")
origin = App.Vector(40.70670000000000,42.94200000000000,-25.40000000000000)
x_axis=App.Vector(0.74314483000000,0.66913061000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000001159470)
z_axis=App.Vector(0.66913061000000,-0.74314483000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnmdhTqweiTOyKD_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("Sketcher::SketchObject","Sketch_FnmdhTqweiTOyKD_1_JZC")
App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnmdhTqweiTOyKD_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC").addGeometry(Part.LineSegment(App.Vector(44.54705411087330,1.83309002125413,-0.00000384137890),App.Vector(31.65294731011320,1.83309002125413,-0.00000579114761)),False)

App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC").addGeometry(Part.LineSegment(App.Vector(31.65294731011320,1.83309002125413,-0.00000579114761),App.Vector(31.65294731011320,-1.83309002125413,-0.00000579114761)),False)

App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC").addGeometry(Part.LineSegment(App.Vector(44.54705411087330,-1.83309002125413,-0.00000384137890),App.Vector(31.65294731011320,-1.83309002125413,-0.00000579114761)),False)

App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC").addGeometry(Part.LineSegment(App.Vector(44.54705411087330,-1.83309002125413,-0.00000384137890),App.Vector(44.54705411087330,1.83309002125413,-0.00000384137890)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Pad","Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC")
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC")
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnmdhTqweiTOyKD_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnmdhTqweiTOyKD_1_F4k9rflZOtIBTRf_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Plane", "plane_Sketch_FfYWRfItUH9VAVq_1_JdC")
origin = App.Vector(86.10191000000000,59.10004000000000,-25.40000000000000)
x_axis=App.Vector(-0.66913061000000,0.74314483000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000001159470)
z_axis=App.Vector(0.74314483000000,0.66913061000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfYWRfItUH9VAVq_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("Sketcher::SketchObject","Sketch_FfYWRfItUH9VAVq_1_JdC")
App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfYWRfItUH9VAVq_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC").addGeometry(Part.LineSegment(App.Vector(-32.43243395935109,-1.83309002125413,0.00000798312430),App.Vector(-24.71756524852669,-1.83309002125413,0.00000091409709)),False)

App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC").addGeometry(Part.LineSegment(App.Vector(-24.71756524852669,-1.83309002125413,0.00000091409709),App.Vector(-24.71756524852669,1.83309002125413,0.00000091409709)),False)

App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC").addGeometry(Part.LineSegment(App.Vector(-32.43243395935109,1.83309002125413,0.00000798312430),App.Vector(-24.71756524852669,1.83309002125413,0.00000091409709)),False)

App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC").addGeometry(Part.LineSegment(App.Vector(-32.43243395935109,-1.83309002125413,0.00000798312430),App.Vector(-32.43243395935109,1.83309002125413,0.00000798312430)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FO4EBVPGVf2DGPc_0").newObject("PartDesign::Pad","Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC")
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC")
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfYWRfItUH9VAVq_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfYWRfItUH9VAVq_1_Flqb6WBbBrtNyar_1_JdC").Offset = 0
App.ActiveDocument.recompute()

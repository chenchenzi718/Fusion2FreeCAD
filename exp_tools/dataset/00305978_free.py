import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00305978")
App.ActiveDocument.addObject("PartDesign::Body","Body_FCTtaOoQzSP8V2l_0")
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").Label = "Body_FCTtaOoQzSP8V2l_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Plane", "plane_Sketch_FCTtaOoQzSP8V2l_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCTtaOoQzSP8V2l_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("Sketcher::SketchObject","Sketch_FCTtaOoQzSP8V2l_0_JGC")
App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCTtaOoQzSP8V2l_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC").addGeometry(Part.LineSegment(App.Vector(-57.56115000000000,27.63392000000000,0.00000000000000),App.Vector(18.63885000000000,27.63392000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC").addGeometry(Part.LineSegment(App.Vector(18.63885000000000,27.63392000000000,0.00000000000000),App.Vector(18.63885000000000,6.04392000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC").addGeometry(Part.LineSegment(App.Vector(-57.56115000000000,6.04392000000000,0.00000000000000),App.Vector(18.63885000000000,6.04392000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC").addGeometry(Part.LineSegment(App.Vector(-57.56115000000000,27.63392000000000,0.00000000000000),App.Vector(-57.56115000000000,6.04392000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Pad","Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC")
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC")
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").Length = 38.1
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCTtaOoQzSP8V2l_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCTtaOoQzSP8V2l_0_FTiouftNSdItyOA_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Plane", "plane_Sketch_FfLrXhCPSDUuTCd_1_JJS")
origin = App.Vector(-19.46115000000000,-38.10000000000000,16.83892000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("Sketcher::SketchObject","Sketch_FfLrXhCPSDUuTCd_1_JJS")
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS").addGeometry(Part.LineSegment(App.Vector(-2.94460000000000,-6.52412000000000,0.00000000000000),App.Vector(2.13540000000000,-6.52412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS").addGeometry(Part.LineSegment(App.Vector(2.13540000000000,-6.52412000000000,0.00000000000000),App.Vector(2.13540000000000,-9.06412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS").addGeometry(Part.LineSegment(App.Vector(-2.94460000000000,-9.06412000000000,0.00000000000000),App.Vector(2.13540000000000,-9.06412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS").addGeometry(Part.LineSegment(App.Vector(-2.94460000000000,-6.52412000000000,0.00000000000000),App.Vector(-2.94460000000000,-9.06412000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Pocket","Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").Length = 2.5400000000000005
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Plane", "plane_Sketch_FfLrXhCPSDUuTCd_1_JJO")
origin = App.Vector(-19.46115000000000,-38.10000000000000,16.83892000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("Sketcher::SketchObject","Sketch_FfLrXhCPSDUuTCd_1_JJO")
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO").addGeometry(Part.LineSegment(App.Vector(-12.54957000000000,-6.52412000000000,0.00000000000000),App.Vector(-7.46957000000000,-6.52412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO").addGeometry(Part.LineSegment(App.Vector(-7.46957000000000,-6.52412000000000,0.00000000000000),App.Vector(-7.46957000000000,-9.06412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO").addGeometry(Part.LineSegment(App.Vector(-12.54957000000000,-9.06412000000000,0.00000000000000),App.Vector(-7.46957000000000,-9.06412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO").addGeometry(Part.LineSegment(App.Vector(-12.54957000000000,-6.52412000000000,0.00000000000000),App.Vector(-12.54957000000000,-9.06412000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Pocket","Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").Length = 2.5400000000000005
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Plane", "plane_Sketch_FfLrXhCPSDUuTCd_1_JJK")
origin = App.Vector(-19.46115000000000,-38.10000000000000,16.83892000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("Sketcher::SketchObject","Sketch_FfLrXhCPSDUuTCd_1_JJK")
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJK").addGeometry(Part.Circle(App.Vector(-19.09933000000000,-6.52412000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.52400000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Pocket","Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJK")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").Length = 2.5400000000000005
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Plane", "plane_Sketch_FfLrXhCPSDUuTCd_1_JJG")
origin = App.Vector(-19.46115000000000,-38.10000000000000,16.83892000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("Sketcher::SketchObject","Sketch_FfLrXhCPSDUuTCd_1_JJG")
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJG").addGeometry(Part.Circle(App.Vector(-22.78233000000000,-6.52412000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.52400000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Pocket","Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJG")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").Length = 2.5400000000000005
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Plane", "plane_Sketch_FfLrXhCPSDUuTCd_1_JJC")
origin = App.Vector(-19.46115000000000,-38.10000000000000,16.83892000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("Sketcher::SketchObject","Sketch_FfLrXhCPSDUuTCd_1_JJC")
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfLrXhCPSDUuTCd_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJC").addGeometry(Part.Circle(App.Vector(-26.46533000000000,-6.52412000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.52400000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Pocket","Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJC")
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").Length = 2.5400000000000005
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfLrXhCPSDUuTCd_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfLrXhCPSDUuTCd_1_FhjrMDC9ANrmYCY_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Plane", "plane_Sketch_Fourio81O730Cpn_1_JNC")
origin = App.Vector(-42.24348000000000,-35.56000000000000,10.31480000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fourio81O730Cpn_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("Sketcher::SketchObject","Sketch_Fourio81O730Cpn_1_JNC")
App.ActiveDocument.getObject("Sketch_Fourio81O730Cpn_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fourio81O730Cpn_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fourio81O730Cpn_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fourio81O730Cpn_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.25400000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fourio81O730Cpn_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fourio81O730Cpn_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Pocket","Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC")
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fourio81O730Cpn_1_JNC")
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").Length = 0.5080000000000001
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fourio81O730Cpn_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fourio81O730Cpn_1_FitCguza2IBP79K_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Plane", "plane_Sketch_FwrHVtdX4ZDzoFO_1_JRC")
origin = App.Vector(-38.56048000000000,-35.56000000000000,10.31480000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwrHVtdX4ZDzoFO_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("Sketcher::SketchObject","Sketch_FwrHVtdX4ZDzoFO_1_JRC")
App.ActiveDocument.getObject("Sketch_FwrHVtdX4ZDzoFO_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwrHVtdX4ZDzoFO_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FwrHVtdX4ZDzoFO_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwrHVtdX4ZDzoFO_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.25400000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwrHVtdX4ZDzoFO_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwrHVtdX4ZDzoFO_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Pocket","Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC")
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FwrHVtdX4ZDzoFO_1_JRC")
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").Length = 0.5080000000000001
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwrHVtdX4ZDzoFO_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwrHVtdX4ZDzoFO_1_FcRDRU3An8wV4du_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Plane", "plane_Sketch_Fd1w3t1AWldej42_1_JVC")
origin = App.Vector(-45.92648000000000,-35.56000000000000,10.31480000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fd1w3t1AWldej42_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("Sketcher::SketchObject","Sketch_Fd1w3t1AWldej42_1_JVC")
App.ActiveDocument.getObject("Sketch_Fd1w3t1AWldej42_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fd1w3t1AWldej42_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fd1w3t1AWldej42_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fd1w3t1AWldej42_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.25400000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fd1w3t1AWldej42_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fd1w3t1AWldej42_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCTtaOoQzSP8V2l_0").newObject("PartDesign::Pocket","Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC")
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fd1w3t1AWldej42_1_JVC")
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").Length = 0.5080000000000001
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fd1w3t1AWldej42_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fd1w3t1AWldej42_1_F35X7HyyFfYBs2m_1_JVC").Offset = 0
App.ActiveDocument.recompute()

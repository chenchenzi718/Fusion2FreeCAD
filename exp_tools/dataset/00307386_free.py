import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00307386")
App.ActiveDocument.addObject("PartDesign::Body","Body_FVM59GIeoFis0T3_0")
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").Label = "Body_FVM59GIeoFis0T3_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Plane", "plane_Sketch_FVM59GIeoFis0T3_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVM59GIeoFis0T3_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("Sketcher::SketchObject","Sketch_FVM59GIeoFis0T3_0_JGC")
App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVM59GIeoFis0T3_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").addGeometry(Part.LineSegment(App.Vector(-38.31531000000000,-12.85442000000000,0.00000000000000),App.Vector(57.68469000000000,-12.85442000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(57.68469000000000,3.14558000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),16.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").addGeometry(Part.LineSegment(App.Vector(73.68469000000000,3.14558000000000,0.00000000000000),App.Vector(73.68469000000000,36.14558000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(57.68469000000000,36.14558000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),16.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").addGeometry(Part.LineSegment(App.Vector(-38.31531000000000,52.14558000000000,0.00000000000000),App.Vector(57.68469000000000,52.14558000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-38.31531000000000,36.14558000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),16.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").addGeometry(Part.LineSegment(App.Vector(-54.31531000000000,3.14558000000000,0.00000000000000),App.Vector(-54.31531000000000,36.14558000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-38.31531000000000,3.14558000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),16.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Pad","Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC")
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC")
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVM59GIeoFis0T3_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVM59GIeoFis0T3_0_FpeNOFAqHdsNWoN_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Plane", "plane_Sketch_Fh8diO45ifNUGWN_1_JJC")
origin = App.Vector(9.68469000000000,19.64558000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh8diO45ifNUGWN_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("Sketcher::SketchObject","Sketch_Fh8diO45ifNUGWN_1_JJC")
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh8diO45ifNUGWN_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJC").addGeometry(Part.Circle(App.Vector(-48.47155000000000,17.63468000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Pocket","Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC")
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJC")
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").Length = 12.0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Plane", "plane_Sketch_Fh8diO45ifNUGWN_1_JJG")
origin = App.Vector(9.68469000000000,19.64558000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh8diO45ifNUGWN_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("Sketcher::SketchObject","Sketch_Fh8diO45ifNUGWN_1_JJG")
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh8diO45ifNUGWN_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJG").addGeometry(Part.Circle(App.Vector(-48.47155000000000,-15.36532000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Pocket","Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG")
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJG")
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").Length = 12.0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Plane", "plane_Sketch_Fh8diO45ifNUGWN_1_JJO")
origin = App.Vector(9.68469000000000,19.64558000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh8diO45ifNUGWN_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("Sketcher::SketchObject","Sketch_Fh8diO45ifNUGWN_1_JJO")
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh8diO45ifNUGWN_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJO").addGeometry(Part.Circle(App.Vector(47.52845000000000,-15.36532000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Pocket","Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO")
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJO")
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").Length = 12.0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Plane", "plane_Sketch_Fh8diO45ifNUGWN_1_JJK")
origin = App.Vector(9.68469000000000,19.64558000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh8diO45ifNUGWN_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("Sketcher::SketchObject","Sketch_Fh8diO45ifNUGWN_1_JJK")
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh8diO45ifNUGWN_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJK").addGeometry(Part.Circle(App.Vector(47.52845000000000,17.63468000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Pocket","Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK")
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJK")
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").Length = 12.0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh8diO45ifNUGWN_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh8diO45ifNUGWN_1_FDCLWKVsUHrz4CT_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Plane", "plane_Sketch_FIoC1zkMG62JF1k_1_JNC")
origin = App.Vector(9.68469000000000,19.64558000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIoC1zkMG62JF1k_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("Sketcher::SketchObject","Sketch_FIoC1zkMG62JF1k_1_JNC")
App.ActiveDocument.getObject("Sketch_FIoC1zkMG62JF1k_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIoC1zkMG62JF1k_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FIoC1zkMG62JF1k_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIoC1zkMG62JF1k_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),26.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIoC1zkMG62JF1k_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIoC1zkMG62JF1k_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Pad","Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC")
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FIoC1zkMG62JF1k_1_JNC")
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").Length = 46.0
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIoC1zkMG62JF1k_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIoC1zkMG62JF1k_1_Fkg7nWhartlXIuU_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Plane", "plane_Sketch_FnosxwfmxD11NAN_1_JRC")
origin = App.Vector(15.21666000000000,19.64558000000000,58.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnosxwfmxD11NAN_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("Sketcher::SketchObject","Sketch_FnosxwfmxD11NAN_1_JRC")
App.ActiveDocument.getObject("Sketch_FnosxwfmxD11NAN_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnosxwfmxD11NAN_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FnosxwfmxD11NAN_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnosxwfmxD11NAN_1_JRC").addGeometry(Part.Circle(App.Vector(-5.53197000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnosxwfmxD11NAN_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnosxwfmxD11NAN_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Pocket","Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC")
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FnosxwfmxD11NAN_1_JRC")
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnosxwfmxD11NAN_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnosxwfmxD11NAN_1_FdRP11UDaXfKfa5_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Plane", "plane_Sketch_FmYaIm6tgDC6VKX_1_JVC")
origin = App.Vector(9.68469000000000,19.64558000000000,46.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmYaIm6tgDC6VKX_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("Sketcher::SketchObject","Sketch_FmYaIm6tgDC6VKX_1_JVC")
App.ActiveDocument.getObject("Sketch_FmYaIm6tgDC6VKX_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmYaIm6tgDC6VKX_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FmYaIm6tgDC6VKX_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmYaIm6tgDC6VKX_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmYaIm6tgDC6VKX_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmYaIm6tgDC6VKX_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Pocket","Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC")
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FmYaIm6tgDC6VKX_1_JVC")
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").Length = 34.0
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmYaIm6tgDC6VKX_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmYaIm6tgDC6VKX_1_FaO1bkE3FrqLUOq_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Plane", "plane_Sketch_FVYeAyG3sjLlSXI_1_JZC")
origin = App.Vector(15.21666000000000,19.64558000000000,58.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVYeAyG3sjLlSXI_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("Sketcher::SketchObject","Sketch_FVYeAyG3sjLlSXI_1_JZC")
App.ActiveDocument.getObject("Sketch_FVYeAyG3sjLlSXI_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVYeAyG3sjLlSXI_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FVYeAyG3sjLlSXI_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVYeAyG3sjLlSXI_1_JZC").addGeometry(Part.Circle(App.Vector(-5.53197000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),30.00000000000000),False)

App.ActiveDocument.getObject("Sketch_FVYeAyG3sjLlSXI_1_JZC").addGeometry(Part.Circle(App.Vector(-5.53197000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),26.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVYeAyG3sjLlSXI_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVYeAyG3sjLlSXI_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FVM59GIeoFis0T3_0").newObject("PartDesign::Pad","Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC")
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FVYeAyG3sjLlSXI_1_JZC")
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVYeAyG3sjLlSXI_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").Type = 0
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVYeAyG3sjLlSXI_1_F6S3a13y67PwxwC_1_JZC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00299989")
App.ActiveDocument.addObject("PartDesign::Body","Body_FwsRaQMMknjdcMk_0")
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").Label = "Body_FwsRaQMMknjdcMk_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Plane", "plane_Sketch_FwsRaQMMknjdcMk_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwsRaQMMknjdcMk_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("Sketcher::SketchObject","Sketch_FwsRaQMMknjdcMk_0_JGC")
App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwsRaQMMknjdcMk_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-71.27603999999999,277.02661000000001,0.00000000000000),App.Vector(68.72396000000001,277.02661000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC").addGeometry(Part.LineSegment(App.Vector(68.72396000000001,277.02661000000001,0.00000000000000),App.Vector(68.72396000000001,-42.97339000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-71.27603999999999,-42.97339000000000,0.00000000000000),App.Vector(68.72396000000001,-42.97339000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-71.27603999999999,277.02661000000001,0.00000000000000),App.Vector(-71.27603999999999,-42.97339000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Pad","Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC")
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC")
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").Length = 4.826
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwsRaQMMknjdcMk_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwsRaQMMknjdcMk_0_FVyp1SVHdzA3wRa_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Plane", "plane_Sketch_FcHD4XXSMHogDx0_1_JJK")
origin = App.Vector(-1.27604000000000,-42.97339000000000,-13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcHD4XXSMHogDx0_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("Sketcher::SketchObject","Sketch_FcHD4XXSMHogDx0_1_JJK")
App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcHD4XXSMHogDx0_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-69.99999999999999,13.46200000000000,0.00000000000000),App.Vector(-38.25000000000000,13.46200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-38.25000000000000,13.46200000000000,0.00000000000000),App.Vector(-38.25000000000000,-18.28800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-69.99999999999999,-18.28800000000000,0.00000000000000),App.Vector(-38.25000000000000,-18.28800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-69.99999999999999,13.46200000000000,0.00000000000000),App.Vector(-69.99999999999999,-18.28800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-66.82499999999999,10.28700000000000,0.00000000000000),App.Vector(-41.42500000000000,10.28700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-41.42500000000000,10.28700000000000,0.00000000000000),App.Vector(-41.42500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-66.82499999999999,-15.11300000000000,0.00000000000000),App.Vector(-41.42500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").addGeometry(Part.LineSegment(App.Vector(-66.82499999999999,10.28700000000000,0.00000000000000),App.Vector(-66.82499999999999,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Pad","Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK")
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK")
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").Length = 320.0
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Plane", "plane_Sketch_FcHD4XXSMHogDx0_1_JJS")
origin = App.Vector(-1.27604000000000,-42.97339000000000,-13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcHD4XXSMHogDx0_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("Sketcher::SketchObject","Sketch_FcHD4XXSMHogDx0_1_JJS")
App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcHD4XXSMHogDx0_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,13.46200000000000,0.00000000000000),App.Vector(38.25000000000000,13.46200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").addGeometry(Part.LineSegment(App.Vector(38.25000000000000,13.46200000000000,0.00000000000000),App.Vector(38.25000000000000,-18.28800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,-18.28800000000000,0.00000000000000),App.Vector(38.25000000000000,-18.28800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,13.46200000000000,0.00000000000000),App.Vector(70.00000000000000,-18.28800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").addGeometry(Part.LineSegment(App.Vector(66.82500000000000,10.28700000000000,0.00000000000000),App.Vector(41.42500000000000,10.28700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").addGeometry(Part.LineSegment(App.Vector(41.42500000000000,10.28700000000000,0.00000000000000),App.Vector(41.42500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").addGeometry(Part.LineSegment(App.Vector(66.82500000000000,-15.11300000000000,0.00000000000000),App.Vector(41.42500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").addGeometry(Part.LineSegment(App.Vector(66.82500000000000,10.28700000000000,0.00000000000000),App.Vector(66.82500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Pad","Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS")
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS")
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").Length = 320.0
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcHD4XXSMHogDx0_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").Type = 0
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").Reversed = 1
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcHD4XXSMHogDx0_1_FyCMUcWFinGWMpO_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Plane", "plane_Sketch_F56AGmyKeTDHbS0_1_JNO")
origin = App.Vector(-1.27604000000000,-42.97339000000000,-13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F56AGmyKeTDHbS0_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("Sketcher::SketchObject","Sketch_F56AGmyKeTDHbS0_1_JNO")
App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F56AGmyKeTDHbS0_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").addGeometry(Part.LineSegment(App.Vector(-66.82499999999999,10.28700000000000,0.00000000000000),App.Vector(-41.42500000000000,10.28700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").addGeometry(Part.LineSegment(App.Vector(-41.42500000000000,10.28700000000000,0.00000000000000),App.Vector(-41.42500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").addGeometry(Part.LineSegment(App.Vector(-66.82499999999999,-15.11300000000000,0.00000000000000),App.Vector(-41.42500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").addGeometry(Part.LineSegment(App.Vector(-66.82499999999999,10.28700000000000,0.00000000000000),App.Vector(-66.82499999999999,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").addGeometry(Part.LineSegment(App.Vector(-62.06200000000000,5.52400000000000,0.00000000000000),App.Vector(-46.18800000000000,5.52400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").addGeometry(Part.LineSegment(App.Vector(-46.18800000000000,5.52400000000000,0.00000000000000),App.Vector(-46.18800000000000,-10.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").addGeometry(Part.LineSegment(App.Vector(-62.06200000000000,-10.35000000000000,0.00000000000000),App.Vector(-46.18800000000000,-10.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").addGeometry(Part.LineSegment(App.Vector(-62.06200000000000,5.52400000000000,0.00000000000000),App.Vector(-62.06200000000000,-10.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Pad","Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO")
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO")
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").Length = 50.0
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").Type = 0
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").Midplane = 1
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Plane", "plane_Sketch_F56AGmyKeTDHbS0_1_JNS")
origin = App.Vector(-1.27604000000000,-42.97339000000000,-13.46200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F56AGmyKeTDHbS0_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("Sketcher::SketchObject","Sketch_F56AGmyKeTDHbS0_1_JNS")
App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F56AGmyKeTDHbS0_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").addGeometry(Part.LineSegment(App.Vector(66.82500000000000,10.28700000000000,0.00000000000000),App.Vector(41.42500000000000,10.28700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").addGeometry(Part.LineSegment(App.Vector(41.42500000000000,10.28700000000000,0.00000000000000),App.Vector(41.42500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").addGeometry(Part.LineSegment(App.Vector(66.82500000000000,-15.11300000000000,0.00000000000000),App.Vector(41.42500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").addGeometry(Part.LineSegment(App.Vector(66.82500000000000,10.28700000000000,0.00000000000000),App.Vector(66.82500000000000,-15.11300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").addGeometry(Part.LineSegment(App.Vector(46.18800000000000,5.52400000000000,0.00000000000000),App.Vector(62.06200000000000,5.52400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").addGeometry(Part.LineSegment(App.Vector(62.06200000000000,5.52400000000000,0.00000000000000),App.Vector(62.06200000000000,-10.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").addGeometry(Part.LineSegment(App.Vector(46.18800000000000,-10.35000000000000,0.00000000000000),App.Vector(62.06200000000000,-10.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").addGeometry(Part.LineSegment(App.Vector(46.18800000000000,5.52400000000000,0.00000000000000),App.Vector(46.18800000000000,-10.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Pad","Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS")
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS")
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").Length = 50.0
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F56AGmyKeTDHbS0_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").Type = 0
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").Midplane = 1
App.ActiveDocument.getObject("Extrude_F56AGmyKeTDHbS0_1_F7Y96WjW55dkJeH_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Plane", "plane_Sketch_Fv5nH2oDIfIdsCi_1_JRC")
origin = App.Vector(-39.52604000000000,117.02661000000001,-15.87500000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fv5nH2oDIfIdsCi_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("Sketcher::SketchObject","Sketch_Fv5nH2oDIfIdsCi_1_JRC")
App.ActiveDocument.getObject("Sketch_Fv5nH2oDIfIdsCi_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fv5nH2oDIfIdsCi_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fv5nH2oDIfIdsCi_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fv5nH2oDIfIdsCi_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-5.87500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fv5nH2oDIfIdsCi_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fv5nH2oDIfIdsCi_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Pocket","Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC")
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fv5nH2oDIfIdsCi_1_JRC")
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fv5nH2oDIfIdsCi_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fv5nH2oDIfIdsCi_1_FDs7wbiAzZ58FUz_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Plane", "plane_Sketch_FUZYh5SrfuAlo0G_1_JVC")
origin = App.Vector(-1.27604000000000,117.02661000000001,4.82600000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUZYh5SrfuAlo0G_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("Sketcher::SketchObject","Sketch_FUZYh5SrfuAlo0G_1_JVC")
App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUZYh5SrfuAlo0G_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVC").addGeometry(Part.Circle(App.Vector(-35.00000000000000,-140.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Pocket","Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC")
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVC")
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").Length = 4.0
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Plane", "plane_Sketch_FUZYh5SrfuAlo0G_1_JVG")
origin = App.Vector(-1.27604000000000,117.02661000000001,4.82600000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUZYh5SrfuAlo0G_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("Sketcher::SketchObject","Sketch_FUZYh5SrfuAlo0G_1_JVG")
App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUZYh5SrfuAlo0G_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVG").addGeometry(Part.Circle(App.Vector(30.00000000000000,-150.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwsRaQMMknjdcMk_0").newObject("PartDesign::Pocket","Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG")
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVG")
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").Length = 4.0
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUZYh5SrfuAlo0G_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUZYh5SrfuAlo0G_1_FR5qJ7mRxmX35ZF_1_JVG").Offset = 0
App.ActiveDocument.recompute()

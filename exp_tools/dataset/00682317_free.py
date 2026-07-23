import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00682317")
App.ActiveDocument.addObject("PartDesign::Body","Body_F0KujbSxKlCwkfu_399")
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").Label = "Body_F0KujbSxKlCwkfu_399"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Plane", "plane_Sketch_F0KujbSxKlCwkfu_399_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0KujbSxKlCwkfu_399_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("Sketcher::SketchObject","Sketch_F0KujbSxKlCwkfu_399_JGC")
App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0KujbSxKlCwkfu_399_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC").addGeometry(Part.LineSegment(App.Vector(-123.06475000000000,54.68849000000000,0.00000000000000),App.Vector(-29.08475000000000,54.68849000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC").addGeometry(Part.LineSegment(App.Vector(-29.08475000000000,54.68849000000000,0.00000000000000),App.Vector(-29.08475000000000,-13.89151000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC").addGeometry(Part.LineSegment(App.Vector(-123.06475000000000,-13.89151000000000,0.00000000000000),App.Vector(-29.08475000000000,-13.89151000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC").addGeometry(Part.LineSegment(App.Vector(-123.06475000000000,54.68849000000000,0.00000000000000),App.Vector(-123.06475000000000,-13.89151000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Pad","Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC")
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").Profile = App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC")
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").Length = 45.720000000000006
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0KujbSxKlCwkfu_399_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0KujbSxKlCwkfu_399_FaNGMfUFgpofGXh_399_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Plane", "plane_Sketch_FlOPglFVUHGAlpe_400_JJC")
origin = App.Vector(-76.07474999999999,20.39849000000000,45.72000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlOPglFVUHGAlpe_400_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("Sketcher::SketchObject","Sketch_FlOPglFVUHGAlpe_400_JJC")
App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlOPglFVUHGAlpe_400_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC").addGeometry(Part.LineSegment(App.Vector(-41.91000000000000,29.21000000000000,0.00000000000000),App.Vector(41.91000000000000,29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC").addGeometry(Part.LineSegment(App.Vector(41.91000000000000,29.21000000000000,0.00000000000000),App.Vector(41.91000000000000,-29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC").addGeometry(Part.LineSegment(App.Vector(-41.91000000000000,-29.21000000000000,0.00000000000000),App.Vector(41.91000000000000,-29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC").addGeometry(Part.LineSegment(App.Vector(-41.91000000000000,29.21000000000000,0.00000000000000),App.Vector(-41.91000000000000,-29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Pocket","Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC")
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").Profile = App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC")
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").Length = 41.910000000000004
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlOPglFVUHGAlpe_400_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlOPglFVUHGAlpe_400_Fu3OGUerb4HQ5lI_400_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Plane", "plane_Sketch_FJMAJWzdWwvFM1g_400_JNS")
origin = App.Vector(-76.07474999999999,20.39849000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJMAJWzdWwvFM1g_400_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("Sketcher::SketchObject","Sketch_FJMAJWzdWwvFM1g_400_JNS")
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJMAJWzdWwvFM1g_400_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNS").addGeometry(Part.Circle(App.Vector(-33.02000000000001,22.78151000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.55600000000000),False)

App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNS").addGeometry(Part.Circle(App.Vector(-33.02000000000001,22.78151000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.39700000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Pad","Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS")
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").Profile = App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNS")
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").Length = 21.59
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Plane", "plane_Sketch_FJMAJWzdWwvFM1g_400_JNW")
origin = App.Vector(-76.07474999999999,20.39849000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJMAJWzdWwvFM1g_400_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("Sketcher::SketchObject","Sketch_FJMAJWzdWwvFM1g_400_JNW")
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJMAJWzdWwvFM1g_400_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNW").addGeometry(Part.Circle(App.Vector(35.56000000000000,22.78151000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.55600000000000),False)

App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNW").addGeometry(Part.Circle(App.Vector(35.56000000000000,22.78151000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.39700000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Pad","Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW")
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").Profile = App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNW")
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").Length = 21.59
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Plane", "plane_Sketch_FJMAJWzdWwvFM1g_400_JNa")
origin = App.Vector(-76.07474999999999,20.39849000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJMAJWzdWwvFM1g_400_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("Sketcher::SketchObject","Sketch_FJMAJWzdWwvFM1g_400_JNa")
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJMAJWzdWwvFM1g_400_JNa"), [""])
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNa").addGeometry(Part.Circle(App.Vector(-33.02000000000001,-20.39849000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.55600000000000),False)

App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNa").addGeometry(Part.Circle(App.Vector(-33.02000000000001,-20.39849000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.39700000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Pad","Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa")
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").Profile = App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNa")
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").Length = 21.59
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").Type = 4
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Plane", "plane_Sketch_FJMAJWzdWwvFM1g_400_JNe")
origin = App.Vector(-76.07474999999999,20.39849000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJMAJWzdWwvFM1g_400_JNe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("Sketcher::SketchObject","Sketch_FJMAJWzdWwvFM1g_400_JNe")
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJMAJWzdWwvFM1g_400_JNe"), [""])
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNe").addGeometry(Part.Circle(App.Vector(35.56000000000000,-20.39849000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.55600000000000),False)

App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNe").addGeometry(Part.Circle(App.Vector(35.56000000000000,-20.39849000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.39700000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Pad","Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe")
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").Profile = App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNe")
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").Length = 21.59
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJMAJWzdWwvFM1g_400_JNe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").Type = 4
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJMAJWzdWwvFM1g_400_FLBkR7YX1SM23IG_400_JNe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Plane", "plane_Sketch_FatjWWqJ50eQmen_400_JSG")
origin = App.Vector(-76.07474999999999,20.39849000000000,45.72000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FatjWWqJ50eQmen_400_JSG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("Sketcher::SketchObject","Sketch_FatjWWqJ50eQmen_400_JSG")
App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FatjWWqJ50eQmen_400_JSG"), [""])
App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG").addGeometry(Part.LineSegment(App.Vector(-41.91000000000000,29.21000000000000,0.00000000000000),App.Vector(41.91000000000000,29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG").addGeometry(Part.LineSegment(App.Vector(41.91000000000000,29.21000000000000,0.00000000000000),App.Vector(41.91000000000000,-29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG").addGeometry(Part.LineSegment(App.Vector(-41.91000000000000,-29.21000000000000,0.00000000000000),App.Vector(41.91000000000000,-29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG").addGeometry(Part.LineSegment(App.Vector(-41.91000000000000,29.21000000000000,0.00000000000000),App.Vector(-41.91000000000000,-29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Pocket","Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG")
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").Profile = App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG")
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").Length = 20.320000000000004
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").Type = 4
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Plane", "plane_Sketch_FatjWWqJ50eQmen_400_JSK")
origin = App.Vector(-76.07474999999999,20.39849000000000,45.72000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FatjWWqJ50eQmen_400_JSK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("Sketcher::SketchObject","Sketch_FatjWWqJ50eQmen_400_JSK")
App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FatjWWqJ50eQmen_400_JSK"), [""])
App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,31.75000000000000,0.00000000000000),App.Vector(44.45000000000000,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,31.75000000000000,0.00000000000000),App.Vector(44.45000000000000,-31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,-31.75000000000000,0.00000000000000),App.Vector(44.45000000000000,-31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,31.75000000000000,0.00000000000000),App.Vector(-44.45000000000000,-31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").addGeometry(Part.LineSegment(App.Vector(-41.91000000000000,29.21000000000000,0.00000000000000),App.Vector(41.91000000000000,29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").addGeometry(Part.LineSegment(App.Vector(41.91000000000000,29.21000000000000,0.00000000000000),App.Vector(41.91000000000000,-29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").addGeometry(Part.LineSegment(App.Vector(-41.91000000000000,-29.21000000000000,0.00000000000000),App.Vector(41.91000000000000,-29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").addGeometry(Part.LineSegment(App.Vector(-41.91000000000000,29.21000000000000,0.00000000000000),App.Vector(-41.91000000000000,-29.21000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0KujbSxKlCwkfu_399").newObject("PartDesign::Pocket","Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK")
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").Profile = App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK")
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").Length = 20.320000000000004
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FatjWWqJ50eQmen_400_JSK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").Type = 4
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FatjWWqJ50eQmen_400_F132XlPfXDtOeRn_400_JSK").Offset = 0
App.ActiveDocument.recompute()

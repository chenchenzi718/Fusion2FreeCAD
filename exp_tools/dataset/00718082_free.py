import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00718082")
App.ActiveDocument.addObject("PartDesign::Body","Body_FTSweTy36ehuRnb_0")
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").Label = "Body_FTSweTy36ehuRnb_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_FTSweTy36ehuRnb_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTSweTy36ehuRnb_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_FTSweTy36ehuRnb_0_JGC")
App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTSweTy36ehuRnb_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC").addGeometry(Part.LineSegment(App.Vector(2070.09999999999991,-2070.09999999999991,0.00000000000000),App.Vector(-2070.09999999999991,-2070.09999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC").addGeometry(Part.LineSegment(App.Vector(-2070.09999999999991,-2070.09999999999991,0.00000000000000),App.Vector(-2070.09999999999991,2070.09999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC").addGeometry(Part.LineSegment(App.Vector(2070.09999999999991,2070.09999999999991,0.00000000000000),App.Vector(-2070.09999999999991,2070.09999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC").addGeometry(Part.LineSegment(App.Vector(2070.09999999999991,-2070.09999999999991,0.00000000000000),App.Vector(2070.09999999999991,2070.09999999999991,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pad","Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC")
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC")
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").Length = 3048.0000000000005
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTSweTy36ehuRnb_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTSweTy36ehuRnb_0_FquT74Vp28mWfNs_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_FgojSK9Fz6A4LKG_1_JJC")
origin = App.Vector(0.00000000000000,-2070.09999999999991,1524.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgojSK9Fz6A4LKG_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_FgojSK9Fz6A4LKG_1_JJC")
App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgojSK9Fz6A4LKG_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC").addGeometry(Part.LineSegment(App.Vector(762.00000000000000,-202.48668000000004,0.00000000000000),App.Vector(-762.00000000000000,-202.48668000000004,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC").addGeometry(Part.LineSegment(App.Vector(-762.00000000000000,-202.48668000000004,0.00000000000000),App.Vector(-762.00000000000000,1067.51331999999979,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC").addGeometry(Part.LineSegment(App.Vector(762.00000000000000,1067.51331999999979,0.00000000000000),App.Vector(-762.00000000000000,1067.51331999999979,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC").addGeometry(Part.LineSegment(App.Vector(762.00000000000000,-202.48668000000004,0.00000000000000),App.Vector(762.00000000000000,1067.51331999999979,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pocket","Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC")
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC")
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").Length = 152.4
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgojSK9Fz6A4LKG_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgojSK9Fz6A4LKG_1_F04j3aSAm4MQ6OV_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_F8cyBgO29BZuGVK_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8cyBgO29BZuGVK_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_F8cyBgO29BZuGVK_1_JNC")
App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8cyBgO29BZuGVK_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC").addGeometry(Part.LineSegment(App.Vector(1917.70000000000005,-1917.70000000000005,0.00000000000000),App.Vector(-1917.70000000000005,-1917.70000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC").addGeometry(Part.LineSegment(App.Vector(-1917.70000000000005,-1917.70000000000005,0.00000000000000),App.Vector(-1917.70000000000005,1917.70000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC").addGeometry(Part.LineSegment(App.Vector(1917.70000000000005,1917.70000000000005,0.00000000000000),App.Vector(-1917.70000000000005,1917.70000000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC").addGeometry(Part.LineSegment(App.Vector(1917.70000000000005,-1917.70000000000005,0.00000000000000),App.Vector(1917.70000000000005,1917.70000000000005,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pocket","Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC")
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC")
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").Length = 2895.6000000000004
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8cyBgO29BZuGVK_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8cyBgO29BZuGVK_1_FwIwqYCFjpmYlPD_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_FOtAtay79SPTw6k_1_JRC")
origin = App.Vector(0.00000000000000,-1993.90000000000009,1321.51332000000002)
x_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(-0.00000000000000,-0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_FOtAtay79SPTw6k_1_JRC")
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRC").addGeometry(Part.Circle(App.Vector(-508.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.40000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pad","Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRC")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").Length = 1270.0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_FOtAtay79SPTw6k_1_JRG")
origin = App.Vector(0.00000000000000,-1993.90000000000009,1321.51332000000002)
x_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(-0.00000000000000,-0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_FOtAtay79SPTw6k_1_JRG")
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRG").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.40000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pad","Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRG")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").Length = 1270.0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_FOtAtay79SPTw6k_1_JRK")
origin = App.Vector(0.00000000000000,-1993.90000000000009,1321.51332000000002)
x_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(-0.00000000000000,-0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_FOtAtay79SPTw6k_1_JRK")
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRK").addGeometry(Part.Circle(App.Vector(508.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.40000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pad","Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRK")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").Length = 1270.0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_FOtAtay79SPTw6k_1_JRO")
origin = App.Vector(0.00000000000000,-1993.90000000000009,1321.51332000000002)
x_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(-0.00000000000000,-0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_FOtAtay79SPTw6k_1_JRO")
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRO").addGeometry(Part.Circle(App.Vector(-254.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.40000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pad","Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRO")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").Length = 1270.0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_FOtAtay79SPTw6k_1_JRS")
origin = App.Vector(0.00000000000000,-1993.90000000000009,1321.51332000000002)
x_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(-0.00000000000000,-0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_FOtAtay79SPTw6k_1_JRS")
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOtAtay79SPTw6k_1_JRS"), [""])
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRS").addGeometry(Part.Circle(App.Vector(254.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.40000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pad","Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").Profile = App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRS")
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").Length = 1270.0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOtAtay79SPTw6k_1_JRS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").Type = 4
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOtAtay79SPTw6k_1_FZAUPFGncRKWmNn_1_JRS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_FiEcl6f1ZFVgWlZ_1_JVC")
origin = App.Vector(2070.09999999999991,0.00000000000000,1524.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiEcl6f1ZFVgWlZ_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_FiEcl6f1ZFVgWlZ_1_JVC")
App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiEcl6f1ZFVgWlZ_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(457.19999999999999,-3352.80000000000018,0.00000000000000),App.Vector(-457.19999999999999,-3352.80000000000018,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-457.19999999999999,-3352.80000000000018,0.00000000000000),App.Vector(-457.19999999999999,-1524.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(457.19999999999999,-1524.00000000000000,0.00000000000000),App.Vector(-457.19999999999999,-1524.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(457.19999999999999,-3352.80000000000018,0.00000000000000),App.Vector(457.19999999999999,-1524.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pocket","Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC")
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC")
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").Length = 152.4
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Plane", "plane_Sketch_FiEcl6f1ZFVgWlZ_1_JVG")
origin = App.Vector(2070.09999999999991,0.00000000000000,1524.00000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiEcl6f1ZFVgWlZ_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("Sketcher::SketchObject","Sketch_FiEcl6f1ZFVgWlZ_1_JVG")
App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiEcl6f1ZFVgWlZ_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG").addGeometry(Part.LineSegment(App.Vector(457.19999999999999,304.79999999999995,0.00000000000000),App.Vector(-457.19999999999999,304.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG").addGeometry(Part.LineSegment(App.Vector(-457.19999999999999,304.79999999999995,0.00000000000000),App.Vector(-457.19999999999999,-1524.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG").addGeometry(Part.LineSegment(App.Vector(457.19999999999999,-1524.00000000000000,0.00000000000000),App.Vector(-457.19999999999999,-1524.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG").addGeometry(Part.LineSegment(App.Vector(457.19999999999999,304.79999999999995,0.00000000000000),App.Vector(457.19999999999999,-1524.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FTSweTy36ehuRnb_0").newObject("PartDesign::Pocket","Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG")
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG")
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").Length = 152.4
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiEcl6f1ZFVgWlZ_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiEcl6f1ZFVgWlZ_1_FcWW4oCnmQUKyQ2_1_JVG").Offset = 0
App.ActiveDocument.recompute()

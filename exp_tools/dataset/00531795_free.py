import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00531795")
App.ActiveDocument.addObject("PartDesign::Body","Body_FXlE8IeXBDp2Yvc_0")
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").Label = "Body_FXlE8IeXBDp2Yvc_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Plane", "plane_Sketch_FXlE8IeXBDp2Yvc_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXlE8IeXBDp2Yvc_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("Sketcher::SketchObject","Sketch_FXlE8IeXBDp2Yvc_0_JGC")
App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXlE8IeXBDp2Yvc_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,20.00000000000000,0.00000000000000),App.Vector(50.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Pad","Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC")
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC")
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXlE8IeXBDp2Yvc_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXlE8IeXBDp2Yvc_0_F8BhwJF0ZTyZV8q_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Plane", "plane_Sketch_FLgxEWJCuMUwGaL_1_JJC")
origin = App.Vector(0.00000000000000,-26.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLgxEWJCuMUwGaL_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("Sketcher::SketchObject","Sketch_FLgxEWJCuMUwGaL_1_JJC")
App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLgxEWJCuMUwGaL_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,46.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,46.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,46.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,44.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,44.00000000000000,0.00000000000000),App.Vector(50.00000000000000,44.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,46.00000000000000,0.00000000000000),App.Vector(50.00000000000000,44.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Pad","Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC")
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC")
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLgxEWJCuMUwGaL_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLgxEWJCuMUwGaL_1_FyCpvVsM5SPjpI3_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Plane", "plane_Sketch_FZ6hVR1Zdn97rDU_1_JNC")
origin = App.Vector(-0.00000000000000,18.00000000000000,26.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZ6hVR1Zdn97rDU_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("Sketcher::SketchObject","Sketch_FZ6hVR1Zdn97rDU_1_JNC")
App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZ6hVR1Zdn97rDU_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,26.00000000000000,0.00000000000000),App.Vector(50.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,26.00000000000000,0.00000000000000),App.Vector(50.00000000000000,24.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,24.00000000000000,0.00000000000000),App.Vector(50.00000000000000,24.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,26.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,24.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Pad","Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC")
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC")
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZ6hVR1Zdn97rDU_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZ6hVR1Zdn97rDU_1_FB2gHSmM8gqeTAY_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Plane", "plane_Sketch_FJSxUkBsA12tVJQ_1_JRC")
origin = App.Vector(0.00000000000000,4.00000000000000,52.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJSxUkBsA12tVJQ_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("Sketcher::SketchObject","Sketch_FJSxUkBsA12tVJQ_1_JRC")
App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJSxUkBsA12tVJQ_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRC").addGeometry(Part.Circle(App.Vector(30.00000000000000,-4.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Pocket","Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC")
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRC")
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Plane", "plane_Sketch_FJSxUkBsA12tVJQ_1_JRG")
origin = App.Vector(0.00000000000000,4.00000000000000,52.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJSxUkBsA12tVJQ_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("Sketcher::SketchObject","Sketch_FJSxUkBsA12tVJQ_1_JRG")
App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJSxUkBsA12tVJQ_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRG").addGeometry(Part.Circle(App.Vector(-30.00000000000000,-4.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Pocket","Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG")
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRG")
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").Length = 100.0
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJSxUkBsA12tVJQ_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJSxUkBsA12tVJQ_1_FZX6QdizoaKohSa_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Plane", "plane_Sketch_FaVLZyDKLltNTDw_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaVLZyDKLltNTDw_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("Sketcher::SketchObject","Sketch_FaVLZyDKLltNTDw_1_JVC")
App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaVLZyDKLltNTDw_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,18.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,18.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,18.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,20.00000000000000,0.00000000000000),App.Vector(-30.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,18.00000000000000,0.00000000000000),App.Vector(30.00000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Pad","Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC")
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC")
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaVLZyDKLltNTDw_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaVLZyDKLltNTDw_1_Fo0bAZx8j5Ykka8_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Plane", "plane_Sketch_FBSLsaHyaCd51hm_1_JZC")
origin = App.Vector(40.00000000000000,-20.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBSLsaHyaCd51hm_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("Sketcher::SketchObject","Sketch_FBSLsaHyaCd51hm_1_JZC")
App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBSLsaHyaCd51hm_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-26.00000000000000,0.00000000000000),App.Vector(-70.00000000000000,-26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC").addGeometry(Part.LineSegment(App.Vector(-70.00000000000000,-26.00000000000000,0.00000000000000),App.Vector(-70.00000000000000,-24.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC").addGeometry(Part.LineSegment(App.Vector(-70.00000000000000,-24.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,-24.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,-26.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,-24.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Pad","Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC")
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC")
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBSLsaHyaCd51hm_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBSLsaHyaCd51hm_1_FRu5tN5mMZoY3jd_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Plane", "plane_Sketch_FcgEAIMJKLexwLG_1_JdC")
origin = App.Vector(0.00000000000000,-45.00000000000000,-23.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcgEAIMJKLexwLG_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("Sketcher::SketchObject","Sketch_FcgEAIMJKLexwLG_1_JdC")
App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcgEAIMJKLexwLG_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-28.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC").addGeometry(Part.LineSegment(App.Vector(-28.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-28.00000000000000,-25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,-25.00000000000001,0.00000000000000),App.Vector(-28.00000000000000,-25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC").addGeometry(Part.LineSegment(App.Vector(-30.00000000000000,-25.00000000000001,0.00000000000000),App.Vector(-30.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Pad","Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC")
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC")
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Plane", "plane_Sketch_FcgEAIMJKLexwLG_1_JdG")
origin = App.Vector(0.00000000000000,-45.00000000000000,-23.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcgEAIMJKLexwLG_1_JdG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("Sketcher::SketchObject","Sketch_FcgEAIMJKLexwLG_1_JdG")
App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcgEAIMJKLexwLG_1_JdG"), [""])
App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,25.00000000000000,0.00000000000000),App.Vector(28.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG").addGeometry(Part.LineSegment(App.Vector(28.00000000000000,25.00000000000000,0.00000000000000),App.Vector(28.00000000000000,-25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,-25.00000000000001,0.00000000000000),App.Vector(28.00000000000000,-25.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,-25.00000000000001,0.00000000000000),App.Vector(30.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FXlE8IeXBDp2Yvc_0").newObject("PartDesign::Pad","Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG")
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").Profile = App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG")
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcgEAIMJKLexwLG_1_JdG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").Type = 4
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcgEAIMJKLexwLG_1_FtkPUEGJHtiZS0Y_1_JdG").Offset = 0
App.ActiveDocument.recompute()

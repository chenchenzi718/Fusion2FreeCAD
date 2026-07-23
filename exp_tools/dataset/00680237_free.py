import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00680237")
App.ActiveDocument.addObject("PartDesign::Body","Body_F2NSP6V0BRRwhqp_0")
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").Label = "Body_F2NSP6V0BRRwhqp_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Plane", "plane_Sketch_F2NSP6V0BRRwhqp_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2NSP6V0BRRwhqp_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("Sketcher::SketchObject","Sketch_F2NSP6V0BRRwhqp_0_JGC")
App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2NSP6V0BRRwhqp_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-76.20000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,0.00000000000000,0.00000000000000),App.Vector(-76.20000000000000,-85.85200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-85.85200000000000,0.00000000000000),App.Vector(-76.20000000000000,-85.85200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-85.85200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC").addGeometry(Part.Circle(App.Vector(-38.10000000000000,-42.92600000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Pad","Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC")
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC")
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2NSP6V0BRRwhqp_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2NSP6V0BRRwhqp_0_FCgOBEjjLLjq2rt_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Plane", "plane_Sketch_FaE6S26TXNQrVj3_1_JJC")
origin = App.Vector(-34.92500000000000,-42.92600000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaE6S26TXNQrVj3_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("Sketcher::SketchObject","Sketch_FaE6S26TXNQrVj3_1_JJC")
App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaE6S26TXNQrVj3_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-41.27500000000001,42.92600000000000,0.00000000000000),App.Vector(-34.92500000000000,42.92600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,42.92600000000000,0.00000000000000),App.Vector(-34.92500000000000,-42.92600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-41.27500000000001,-42.92600000000000,0.00000000000000),App.Vector(-34.92500000000000,-42.92600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC").addGeometry(Part.LineSegment(App.Vector(-41.27500000000001,-42.92600000000000,0.00000000000000),App.Vector(-41.27500000000001,42.92600000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Pad","Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC")
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC")
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").Length = 38.1
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaE6S26TXNQrVj3_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaE6S26TXNQrVj3_1_FG3DsDu7f7tQNa4_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Plane", "plane_Sketch_FXK4wxG2Z3UTagY_1_JNC")
origin = App.Vector(-76.20000000000000,-42.92600000000000,-15.87500000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXK4wxG2Z3UTagY_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("Sketcher::SketchObject","Sketch_FXK4wxG2Z3UTagY_1_JNC")
App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXK4wxG2Z3UTagY_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC").addGeometry(Part.LineSegment(App.Vector(-38.09999999999999,12.57300000000000,0.00000000000000),App.Vector(38.10000000000000,12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,12.57300000000000,0.00000000000000),App.Vector(38.10000000000000,2.92100000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,2.92100000000000,0.00000000000000),App.Vector(-38.09999999999999,2.92100000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC").addGeometry(Part.LineSegment(App.Vector(-38.09999999999999,12.57300000000000,0.00000000000000),App.Vector(-38.09999999999999,2.92100000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Pad","Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC")
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC")
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXK4wxG2Z3UTagY_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXK4wxG2Z3UTagY_1_FaEJUUYExSw2VqJ_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Plane", "plane_Sketch_FblMeijNv5lRpxj_1_JRO")
origin = App.Vector(-114.30000000000000,-42.92600000000000,-3.30200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FblMeijNv5lRpxj_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("Sketcher::SketchObject","Sketch_FblMeijNv5lRpxj_1_JRO")
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FblMeijNv5lRpxj_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRO").addGeometry(Part.Circle(App.Vector(-15.74800000000000,0.03274000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Pocket","Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO")
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRO")
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").Length = 10.160000000000002
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Plane", "plane_Sketch_FblMeijNv5lRpxj_1_JRG")
origin = App.Vector(-114.30000000000000,-42.92600000000000,-3.30200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FblMeijNv5lRpxj_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("Sketcher::SketchObject","Sketch_FblMeijNv5lRpxj_1_JRG")
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FblMeijNv5lRpxj_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-3.04800000000000,0.03274000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-15.74800000000000,0.03274000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),0.0,1.56919790044213),False)

App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRG").addGeometry(Part.LineSegment(App.Vector(-15.73785000000001,6.38273000000000,0.00000000000000),App.Vector(-3.04800000000000,6.38274000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Pocket","Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG")
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRG")
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").Length = 10.160000000000002
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Plane", "plane_Sketch_FblMeijNv5lRpxj_1_JRC")
origin = App.Vector(-114.30000000000000,-42.92600000000000,-3.30200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FblMeijNv5lRpxj_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("Sketcher::SketchObject","Sketch_FblMeijNv5lRpxj_1_JRC")
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FblMeijNv5lRpxj_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRC").addGeometry(Part.Circle(App.Vector(-3.04800000000000,0.03274000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Pocket","Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC")
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRC")
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").Length = 10.160000000000002
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Plane", "plane_Sketch_FblMeijNv5lRpxj_1_JRK")
origin = App.Vector(-114.30000000000000,-42.92600000000000,-3.30200000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FblMeijNv5lRpxj_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("Sketcher::SketchObject","Sketch_FblMeijNv5lRpxj_1_JRK")
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FblMeijNv5lRpxj_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-3.04800000000000,0.03274000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-15.74800000000000,0.03274000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),4.71335748554408,4e-14),False)

App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRK").addGeometry(Part.LineSegment(App.Vector(-15.74184999999999,-6.31725000000000,0.00000000000000),App.Vector(-3.04800000000000,-6.31726000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Pocket","Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK")
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRK")
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").Length = 10.160000000000002
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FblMeijNv5lRpxj_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FblMeijNv5lRpxj_1_FhdtbxikJFjAHrQ_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Plane", "plane_Sketch_FPUU87YbMLvxmCh_1_JVC")
origin = App.Vector(-114.30000000000000,-81.02600000000000,-20.66653000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPUU87YbMLvxmCh_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("Sketcher::SketchObject","Sketch_FPUU87YbMLvxmCh_1_JVC")
App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPUU87YbMLvxmCh_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC").addGeometry(Part.LineSegment(App.Vector(-38.10000000000001,7.71253000000000,0.00000000000000),App.Vector(-38.10000000000001,1.36253000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC").addGeometry(Part.LineSegment(App.Vector(-38.10000000000001,1.36253000000000,0.00000000000000),App.Vector(38.51705000000000,-17.25875000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC").addGeometry(Part.LineSegment(App.Vector(38.09999999999999,7.71253000000000,0.00000000000000),App.Vector(38.51705000000000,-17.25875000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC").addGeometry(Part.LineSegment(App.Vector(-38.10000000000001,7.71253000000000,0.00000000000000),App.Vector(38.09999999999999,7.71253000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Pad","Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC")
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC")
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").Length = 9.652000000000001
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPUU87YbMLvxmCh_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").Type = 0
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPUU87YbMLvxmCh_1_FwPb656f0Ny1o0w_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Plane", "plane_Sketch_FnaF6ovReBDRdAi_2_JZC")
origin = App.Vector(-114.30000000000000,-4.82600000000000,-20.52958000000000)
x_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnaF6ovReBDRdAi_2_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("Sketcher::SketchObject","Sketch_FnaF6ovReBDRdAi_2_JZC")
App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnaF6ovReBDRdAi_2_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC").addGeometry(Part.LineSegment(App.Vector(38.10000000000001,7.57558000000000,0.00000000000000),App.Vector(38.10000000000001,1.22558000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC").addGeometry(Part.LineSegment(App.Vector(38.10000000000001,1.22558000000000,0.00000000000000),App.Vector(-38.35524000000000,-17.08320000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC").addGeometry(Part.LineSegment(App.Vector(-38.09999999999999,7.57558000000000,0.00000000000000),App.Vector(-38.35524000000000,-17.08320000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC").addGeometry(Part.LineSegment(App.Vector(38.10000000000001,7.57558000000000,0.00000000000000),App.Vector(-38.09999999999999,7.57558000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2NSP6V0BRRwhqp_0").newObject("PartDesign::Pad","Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC")
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").Profile = App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC")
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").Length = 9.652000000000001
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnaF6ovReBDRdAi_2_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").Type = 0
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnaF6ovReBDRdAi_2_F0Lsl6caht4AWP3_2_JZC").Offset = 0
App.ActiveDocument.recompute()

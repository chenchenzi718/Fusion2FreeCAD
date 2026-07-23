import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00262475")
App.ActiveDocument.addObject("PartDesign::Body","Body_FwKFk49NxrBs52o_0")
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").Label = "Body_FwKFk49NxrBs52o_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Plane", "plane_Sketch_FwKFk49NxrBs52o_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwKFk49NxrBs52o_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("Sketcher::SketchObject","Sketch_FwKFk49NxrBs52o_0_JGK")
App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwKFk49NxrBs52o_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(-42.86835000000000,56.11968000000000,0.00000000000000),App.Vector(-13.41681000000000,56.11968000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(-13.41681000000000,41.06667000000000,0.00000000000000),App.Vector(-13.41681000000000,56.11968000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(-13.41681000000000,41.06667000000000,0.00000000000000),App.Vector(12.76233000000000,41.06667000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(12.76233000000000,41.06667000000000,0.00000000000000),App.Vector(12.76233000000000,56.11968000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(42.21387000000000,56.11968000000000,0.00000000000000),App.Vector(12.76233000000000,56.11968000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(42.21387000000000,56.11968000000000,0.00000000000000),App.Vector(42.21387000000000,-55.79615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(42.21387000000000,-55.79615000000000,0.00000000000000),App.Vector(12.76233000000000,-55.79615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(12.76233000000000,-55.79615000000000,0.00000000000000),App.Vector(12.76233000000000,-41.07039000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(-13.41681000000000,-41.07039000000000,0.00000000000000),App.Vector(12.76233000000000,-41.07039000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(-13.41681000000000,-55.79615000000000,0.00000000000000),App.Vector(-13.41681000000000,-41.07039000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(-42.86835000000000,-55.79615000000000,0.00000000000000),App.Vector(-13.41681000000000,-55.79615000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").addGeometry(Part.LineSegment(App.Vector(-42.86835000000000,56.11968000000000,0.00000000000000),App.Vector(-42.86835000000000,-55.79615000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Pad","Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK")
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK")
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").Length = 25.908000000000005
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwKFk49NxrBs52o_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwKFk49NxrBs52o_0_FFhm9m7vOcufi1L_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Plane", "plane_Sketch_F6C4BI0KzkBpzPF_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6C4BI0KzkBpzPF_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("Sketcher::SketchObject","Sketch_F6C4BI0KzkBpzPF_1_JJC")
App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6C4BI0KzkBpzPF_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC").addGeometry(Part.LineSegment(App.Vector(-42.86835000000000,23.39575000000000,0.00000000000000),App.Vector(41.88663000000000,23.39575000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC").addGeometry(Part.LineSegment(App.Vector(41.88663000000000,23.39575000000000,0.00000000000000),App.Vector(41.88663000000000,-22.74499000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC").addGeometry(Part.LineSegment(App.Vector(-42.86835000000000,-22.74499000000000,0.00000000000000),App.Vector(41.88663000000000,-22.74499000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC").addGeometry(Part.LineSegment(App.Vector(-42.86835000000000,23.39575000000000,0.00000000000000),App.Vector(-42.86835000000000,-22.74499000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Pad","Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC")
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC")
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").Length = 35.306
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6C4BI0KzkBpzPF_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6C4BI0KzkBpzPF_1_FseQPyecJXJlvDB_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Plane", "plane_Sketch_FNSHd07fA5Hms13_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNSHd07fA5Hms13_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("Sketcher::SketchObject","Sketch_FNSHd07fA5Hms13_1_JNC")
App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNSHd07fA5Hms13_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC").addGeometry(Part.LineSegment(App.Vector(-43.19558000000000,23.39575000000000,0.00000000000000),App.Vector(42.21387000000000,23.39575000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC").addGeometry(Part.LineSegment(App.Vector(42.21387000000000,23.39575000000000,0.00000000000000),App.Vector(42.21387000000000,10.96066000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC").addGeometry(Part.LineSegment(App.Vector(-43.19558000000000,10.96066000000000,0.00000000000000),App.Vector(42.21387000000000,10.96066000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC").addGeometry(Part.LineSegment(App.Vector(-43.19558000000000,23.39575000000000,0.00000000000000),App.Vector(-43.19558000000000,10.96066000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Pad","Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC")
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC")
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").Length = 44.45
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Plane", "plane_Sketch_FNSHd07fA5Hms13_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNSHd07fA5Hms13_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("Sketcher::SketchObject","Sketch_FNSHd07fA5Hms13_1_JNG")
App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNSHd07fA5Hms13_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG").addGeometry(Part.LineSegment(App.Vector(-43.19558000000000,-22.41775000000000,0.00000000000000),App.Vector(42.21387000000000,-22.41775000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG").addGeometry(Part.LineSegment(App.Vector(42.21387000000000,-22.41775000000000,0.00000000000000),App.Vector(42.21387000000000,-8.67370000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG").addGeometry(Part.LineSegment(App.Vector(-43.19558000000000,-8.67370000000000,0.00000000000000),App.Vector(42.21387000000000,-8.67370000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG").addGeometry(Part.LineSegment(App.Vector(-43.19558000000000,-22.41775000000000,0.00000000000000),App.Vector(-43.19558000000000,-8.67370000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Pad","Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG")
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG")
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").Length = 44.45
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNSHd07fA5Hms13_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNSHd07fA5Hms13_1_Fce3QbQ25T5KSrp_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Plane", "plane_Sketch_Fb6iTGB3JYdXt6i_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb6iTGB3JYdXt6i_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("Sketcher::SketchObject","Sketch_Fb6iTGB3JYdXt6i_1_JRC")
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb6iTGB3JYdXt6i_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC").addGeometry(Part.LineSegment(App.Vector(-42.86835000000000,23.39575000000000,0.00000000000000),App.Vector(-24.54294000000000,23.39575000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC").addGeometry(Part.LineSegment(App.Vector(-24.54294000000000,23.39575000000000,0.00000000000000),App.Vector(-24.54294000000000,10.96066000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC").addGeometry(Part.LineSegment(App.Vector(-42.86835000000000,10.96066000000000,0.00000000000000),App.Vector(-24.54294000000000,10.96066000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC").addGeometry(Part.LineSegment(App.Vector(-42.86835000000000,23.39575000000000,0.00000000000000),App.Vector(-42.86835000000000,10.96066000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Pad","Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC")
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC")
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").Length = 58.674
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Plane", "plane_Sketch_Fb6iTGB3JYdXt6i_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb6iTGB3JYdXt6i_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("Sketcher::SketchObject","Sketch_Fb6iTGB3JYdXt6i_1_JRG")
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb6iTGB3JYdXt6i_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG").addGeometry(Part.LineSegment(App.Vector(42.21387000000000,23.39575000000000,0.00000000000000),App.Vector(24.21571000000000,23.39575000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG").addGeometry(Part.LineSegment(App.Vector(24.21571000000000,23.39575000000000,0.00000000000000),App.Vector(24.21571000000000,11.28790000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG").addGeometry(Part.LineSegment(App.Vector(42.21387000000000,11.28790000000000,0.00000000000000),App.Vector(24.21571000000000,11.28790000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG").addGeometry(Part.LineSegment(App.Vector(42.21387000000000,23.39575000000000,0.00000000000000),App.Vector(42.21387000000000,11.28790000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Pad","Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG")
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG")
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").Length = 58.674
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Plane", "plane_Sketch_Fb6iTGB3JYdXt6i_1_JRK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb6iTGB3JYdXt6i_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("Sketcher::SketchObject","Sketch_Fb6iTGB3JYdXt6i_1_JRK")
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb6iTGB3JYdXt6i_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK").addGeometry(Part.LineSegment(App.Vector(-43.52282000000000,-8.67370000000000,0.00000000000000),App.Vector(-24.21571000000000,-8.67370000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK").addGeometry(Part.LineSegment(App.Vector(-24.21571000000000,-8.67370000000000,0.00000000000000),App.Vector(-24.21571000000000,-22.41775000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK").addGeometry(Part.LineSegment(App.Vector(-43.52282000000000,-22.41775000000000,0.00000000000000),App.Vector(-24.21571000000000,-22.41775000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK").addGeometry(Part.LineSegment(App.Vector(-43.52282000000000,-8.67370000000000,0.00000000000000),App.Vector(-43.52282000000000,-22.41775000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Pad","Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK")
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK")
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").Length = 58.674
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Plane", "plane_Sketch_Fb6iTGB3JYdXt6i_1_JRO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb6iTGB3JYdXt6i_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("Sketcher::SketchObject","Sketch_Fb6iTGB3JYdXt6i_1_JRO")
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb6iTGB3JYdXt6i_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO").addGeometry(Part.LineSegment(App.Vector(24.21571000000000,-22.41775000000000,0.00000000000000),App.Vector(42.21387000000000,-22.41775000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO").addGeometry(Part.LineSegment(App.Vector(42.21387000000000,-22.41775000000000,0.00000000000000),App.Vector(42.21387000000000,-8.67370000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO").addGeometry(Part.LineSegment(App.Vector(24.21571000000000,-8.67370000000000,0.00000000000000),App.Vector(42.21387000000000,-8.67370000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO").addGeometry(Part.LineSegment(App.Vector(24.21571000000000,-22.41775000000000,0.00000000000000),App.Vector(24.21571000000000,-8.67370000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Pad","Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO")
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO")
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").Length = 58.674
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb6iTGB3JYdXt6i_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb6iTGB3JYdXt6i_1_FT77A8UcgVR0tOg_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Plane", "plane_Sketch_FuuWv6L69VgRYi5_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuuWv6L69VgRYi5_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("Sketcher::SketchObject","Sketch_FuuWv6L69VgRYi5_1_JVC")
App.ActiveDocument.getObject("Sketch_FuuWv6L69VgRYi5_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuuWv6L69VgRYi5_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FuuWv6L69VgRYi5_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuuWv6L69VgRYi5_1_JVC").addGeometry(Part.Circle(App.Vector(6.05579000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.90312000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuuWv6L69VgRYi5_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuuWv6L69VgRYi5_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwKFk49NxrBs52o_0").newObject("PartDesign::Pocket","Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC")
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FuuWv6L69VgRYi5_1_JVC")
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").Length = 43.942
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuuWv6L69VgRYi5_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").Type = 0
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuuWv6L69VgRYi5_1_F953dnxuN6DsjNO_1_JVC").Offset = 0
App.ActiveDocument.recompute()

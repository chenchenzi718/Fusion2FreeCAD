import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00599733")
App.ActiveDocument.addObject("PartDesign::Body","Body_FdWgRYRZhxpsmoG_0")
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").Label = "Body_FdWgRYRZhxpsmoG_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Plane", "plane_Sketch_FdWgRYRZhxpsmoG_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdWgRYRZhxpsmoG_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("Sketcher::SketchObject","Sketch_FdWgRYRZhxpsmoG_0_JGC")
App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdWgRYRZhxpsmoG_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.86000000000000,41.65600000000000,0.00000000000000),App.Vector(22.86000000000000,41.65600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC").addGeometry(Part.LineSegment(App.Vector(22.86000000000000,41.65600000000000,0.00000000000000),App.Vector(22.86000000000000,-41.65600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.86000000000000,-41.65600000000000,0.00000000000000),App.Vector(22.86000000000000,-41.65600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.86000000000000,41.65600000000000,0.00000000000000),App.Vector(-22.86000000000000,-41.65600000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Pad","Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC")
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC")
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").Length = 2.5400000000000005
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdWgRYRZhxpsmoG_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdWgRYRZhxpsmoG_0_F5PtneCKqLlGCkx_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Plane", "plane_Sketch_FWRcQxY6u6510D8_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,2.54000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWRcQxY6u6510D8_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("Sketcher::SketchObject","Sketch_FWRcQxY6u6510D8_1_JJC")
App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWRcQxY6u6510D8_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-22.86000000000000,41.65600000000000,0.00000000000000),App.Vector(22.86000000000000,41.65600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").addGeometry(Part.LineSegment(App.Vector(22.86000000000000,41.65600000000000,0.00000000000000),App.Vector(22.86000000000000,-41.65600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-22.86000000000000,-41.65600000000000,0.00000000000000),App.Vector(22.86000000000000,-41.65600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-22.86000000000000,41.65600000000000,0.00000000000000),App.Vector(-22.86000000000000,-41.65600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-20.32000000000000,39.11600000000000,0.00000000000000),App.Vector(20.32000000000000,39.11600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").addGeometry(Part.LineSegment(App.Vector(20.32000000000000,39.11600000000000,0.00000000000000),App.Vector(20.32000000000000,-39.11600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-20.32000000000000,-39.11600000000000,0.00000000000000),App.Vector(20.32000000000000,-39.11600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").addGeometry(Part.LineSegment(App.Vector(-20.32000000000000,39.11600000000000,0.00000000000000),App.Vector(-20.32000000000000,-39.11600000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Pad","Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC")
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC")
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").Length = 20.320000000000004
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWRcQxY6u6510D8_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWRcQxY6u6510D8_1_FFlRXixKsCdCAHu_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Plane", "plane_Sketch_F2ixQbCnFUYtp0u_1_JOC")
origin = App.Vector(0.00000000000000,0.00000000000000,2.54000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("Sketcher::SketchObject","Sketch_F2ixQbCnFUYtp0u_1_JOC")
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOC").addGeometry(Part.Circle(App.Vector(0.00000000000000,28.70200000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.27000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Pocket","Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOC")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Plane", "plane_Sketch_F2ixQbCnFUYtp0u_1_JOG")
origin = App.Vector(0.00000000000000,0.00000000000000,2.54000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("Sketcher::SketchObject","Sketch_F2ixQbCnFUYtp0u_1_JOG")
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOG"), [""])
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOG").addGeometry(Part.Circle(App.Vector(0.00000000000000,-28.70200000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.27000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Pocket","Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").Profile = App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOG")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").Type = 4
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Plane", "plane_Sketch_F2ixQbCnFUYtp0u_1_JOK")
origin = App.Vector(0.00000000000000,0.00000000000000,2.54000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("Sketcher::SketchObject","Sketch_F2ixQbCnFUYtp0u_1_JOK")
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOK"), [""])
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOK").addGeometry(Part.Circle(App.Vector(17.78000000000000,28.70200000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.54000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Pocket","Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").Profile = App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOK")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").Type = 4
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Plane", "plane_Sketch_F2ixQbCnFUYtp0u_1_JOO")
origin = App.Vector(0.00000000000000,0.00000000000000,2.54000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("Sketcher::SketchObject","Sketch_F2ixQbCnFUYtp0u_1_JOO")
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOO"), [""])
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOO").addGeometry(Part.Circle(App.Vector(-17.78000000000000,-28.70200000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.54000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Pocket","Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").Profile = App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOO")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").Type = 4
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Plane", "plane_Sketch_F2ixQbCnFUYtp0u_1_JOS")
origin = App.Vector(0.00000000000000,0.00000000000000,2.54000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("Sketcher::SketchObject","Sketch_F2ixQbCnFUYtp0u_1_JOS")
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOS"), [""])
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS").addGeometry(Part.LineSegment(App.Vector(-15.87500000000000,39.11600000000000,0.00000000000000),App.Vector(15.87500000000000,39.11600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS").addGeometry(Part.LineSegment(App.Vector(15.87500000000000,39.11600000000000,0.00000000000000),App.Vector(15.87500000000000,35.94100000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS").addGeometry(Part.LineSegment(App.Vector(-15.87500000000000,35.94100000000000,0.00000000000000),App.Vector(15.87500000000000,35.94100000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS").addGeometry(Part.LineSegment(App.Vector(-15.87500000000000,39.11600000000000,0.00000000000000),App.Vector(-15.87500000000000,35.94100000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Pocket","Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").Profile = App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").Type = 4
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Plane", "plane_Sketch_F2ixQbCnFUYtp0u_1_JOW")
origin = App.Vector(0.00000000000000,0.00000000000000,2.54000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("Sketcher::SketchObject","Sketch_F2ixQbCnFUYtp0u_1_JOW")
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2ixQbCnFUYtp0u_1_JOW"), [""])
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW").addGeometry(Part.LineSegment(App.Vector(-15.87500000000000,-35.94100000000000,0.00000000000000),App.Vector(15.87500000000000,-35.94100000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW").addGeometry(Part.LineSegment(App.Vector(15.87500000000000,-35.94100000000000,0.00000000000000),App.Vector(15.87500000000000,-39.11600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW").addGeometry(Part.LineSegment(App.Vector(-15.87500000000000,-39.11600000000000,0.00000000000000),App.Vector(15.87500000000000,-39.11600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW").addGeometry(Part.LineSegment(App.Vector(-15.87500000000000,-35.94100000000000,0.00000000000000),App.Vector(-15.87500000000000,-39.11600000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdWgRYRZhxpsmoG_0").newObject("PartDesign::Pocket","Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").Profile = App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW")
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2ixQbCnFUYtp0u_1_JOW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").Type = 4
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2ixQbCnFUYtp0u_1_Fp2ItnkW0jnC2t0_1_JOW").Offset = 0
App.ActiveDocument.recompute()

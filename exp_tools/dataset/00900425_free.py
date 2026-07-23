import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00900425")
App.ActiveDocument.addObject("PartDesign::Body","Body_FKj4K35xYq72SmO_0")
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").Label = "Body_FKj4K35xYq72SmO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Plane", "plane_Sketch_FKj4K35xYq72SmO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKj4K35xYq72SmO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("Sketcher::SketchObject","Sketch_FKj4K35xYq72SmO_0_JGC")
App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKj4K35xYq72SmO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-6.65000000000000,-6.65000000000000,0.00000000000000),App.Vector(6.65000000000000,-6.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC").addGeometry(Part.LineSegment(App.Vector(6.65000000000000,-6.65000000000000,0.00000000000000),App.Vector(6.65000000000000,6.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-6.65000000000000,6.65000000000000,0.00000000000000),App.Vector(6.65000000000000,6.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-6.65000000000000,-6.65000000000000,0.00000000000000),App.Vector(-6.65000000000000,6.65000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Pad","Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC")
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC")
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").Length = 11.0
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKj4K35xYq72SmO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKj4K35xYq72SmO_0_Fi3dqiIBCi4wZlP_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Plane", "plane_Sketch_Fn6iDWDD1MfUpPg_1_JJC")
origin = App.Vector(6.65000000000000,-5.72500000000000,5.50000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fn6iDWDD1MfUpPg_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("Sketcher::SketchObject","Sketch_Fn6iDWDD1MfUpPg_1_JJC")
App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fn6iDWDD1MfUpPg_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.92500000000000,5.50000000000000,0.00000000000000),App.Vector(10.52500000000000,5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC").addGeometry(Part.LineSegment(App.Vector(10.52500000000000,5.50000000000000,0.00000000000000),App.Vector(10.52500000000000,-5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.92500000000000,-5.50000000000000,0.00000000000000),App.Vector(10.52500000000000,-5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.92500000000000,5.50000000000000,0.00000000000000),App.Vector(0.92500000000000,-5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Pad","Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC")
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC")
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").Length = 2.4
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fn6iDWDD1MfUpPg_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fn6iDWDD1MfUpPg_1_FgqQYh80JGY2D5g_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Plane", "plane_Sketch_FnnsPEH6vRAiv0h_1_JNC")
origin = App.Vector(0.70000000000000,6.65000000000000,4.75000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnnsPEH6vRAiv0h_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("Sketcher::SketchObject","Sketch_FnnsPEH6vRAiv0h_1_JNC")
App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnnsPEH6vRAiv0h_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC").addGeometry(Part.LineSegment(App.Vector(5.50000000000000,-4.75000000000000,0.00000000000000),App.Vector(-4.10000000000000,-4.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC").addGeometry(Part.LineSegment(App.Vector(-4.10000000000000,-4.75000000000000,0.00000000000000),App.Vector(-4.10000000000000,6.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC").addGeometry(Part.LineSegment(App.Vector(5.50000000000000,6.25000000000000,0.00000000000000),App.Vector(-4.10000000000000,6.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC").addGeometry(Part.LineSegment(App.Vector(5.50000000000000,-4.75000000000000,0.00000000000000),App.Vector(5.50000000000000,6.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Pad","Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC")
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC")
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").Length = 2.4
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnnsPEH6vRAiv0h_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnnsPEH6vRAiv0h_1_FpxOKSZIKrpvBB4_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Plane", "plane_Sketch_Fk0A0sEGDgTTEjx_1_JRC")
origin = App.Vector(1.20000000000000,1.20000000000000,11.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk0A0sEGDgTTEjx_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("Sketcher::SketchObject","Sketch_Fk0A0sEGDgTTEjx_1_JRC")
App.ActiveDocument.getObject("Sketch_Fk0A0sEGDgTTEjx_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk0A0sEGDgTTEjx_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fk0A0sEGDgTTEjx_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk0A0sEGDgTTEjx_1_JRC").addGeometry(Part.Circle(App.Vector(-1.20000000000000,-1.20000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk0A0sEGDgTTEjx_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk0A0sEGDgTTEjx_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Pad","Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC")
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fk0A0sEGDgTTEjx_1_JRC")
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").Length = 7.200000000000001
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk0A0sEGDgTTEjx_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk0A0sEGDgTTEjx_1_FNd3rZmyZ3cVRCX_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Plane", "plane_Sketch_FCV36M7C5aUm3xZ_1_JVC")
origin = App.Vector(0.00000000000000,7.85000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCV36M7C5aUm3xZ_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("Sketcher::SketchObject","Sketch_FCV36M7C5aUm3xZ_1_JVC")
App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCV36M7C5aUm3xZ_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-19.65000000000000,15.70000000000000,0.00000000000000),App.Vector(21.05000000000000,15.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(21.05000000000000,15.70000000000000,0.00000000000000),App.Vector(21.05000000000000,1.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(6.65000000000000,1.20000000000000,0.00000000000000),App.Vector(21.05000000000000,1.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(6.65000000000000,1.20000000000000,0.00000000000000),App.Vector(6.65000000000000,3.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(9.05000000000000,3.05000000000000,0.00000000000000),App.Vector(6.65000000000000,3.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(9.05000000000000,12.65000000000000,0.00000000000000),App.Vector(9.05000000000000,3.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(9.05000000000000,12.65000000000000,0.00000000000000),App.Vector(6.65000000000000,12.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(6.65000000000000,14.50000000000000,0.00000000000000),App.Vector(6.65000000000000,12.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-6.65000000000000,14.50000000000000,0.00000000000000),App.Vector(6.65000000000000,14.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-6.65000000000000,14.50000000000000,0.00000000000000),App.Vector(-6.65000000000000,1.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-6.65000000000000,1.20000000000000,0.00000000000000),App.Vector(-19.65000000000000,1.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").addGeometry(Part.LineSegment(App.Vector(-19.65000000000000,15.70000000000000,0.00000000000000),App.Vector(-19.65000000000000,1.20000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Pad","Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC")
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC")
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").Length = 1.5
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Plane", "plane_Sketch_FCV36M7C5aUm3xZ_1_JVK")
origin = App.Vector(0.00000000000000,7.85000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCV36M7C5aUm3xZ_1_JVK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("Sketcher::SketchObject","Sketch_FCV36M7C5aUm3xZ_1_JVK")
App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCV36M7C5aUm3xZ_1_JVK"), [""])
App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(-6.65000000000000,1.20000000000000,0.00000000000000),App.Vector(-4.80000000000000,1.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(-4.80000000000000,1.20000000000000,0.00000000000000),App.Vector(4.80000000000000,1.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(6.65000000000000,1.20000000000000,0.00000000000000),App.Vector(4.80000000000000,1.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(6.65000000000000,1.20000000000000,0.00000000000000),App.Vector(6.65000000000000,3.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(9.05000000000000,3.05000000000000,0.00000000000000),App.Vector(6.65000000000000,3.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(9.05000000000000,12.65000000000000,0.00000000000000),App.Vector(9.05000000000000,3.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(9.05000000000000,12.65000000000000,0.00000000000000),App.Vector(6.65000000000000,12.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(6.65000000000000,14.50000000000000,0.00000000000000),App.Vector(6.65000000000000,12.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(-6.65000000000000,14.50000000000000,0.00000000000000),App.Vector(6.65000000000000,14.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").addGeometry(Part.LineSegment(App.Vector(-6.65000000000000,14.50000000000000,0.00000000000000),App.Vector(-6.65000000000000,1.20000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Pad","Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK")
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").Profile = App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK")
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").Length = 1.5
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCV36M7C5aUm3xZ_1_JVK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").Type = 4
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCV36M7C5aUm3xZ_1_Fr8O7P5zbUPNDuO_1_JVK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Plane", "plane_Sketch_Fb4FYP1VxY1ZXfk_1_JZC")
origin = App.Vector(0.70000000000000,-0.60000000000000,-1.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb4FYP1VxY1ZXfk_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("Sketcher::SketchObject","Sketch_Fb4FYP1VxY1ZXfk_1_JZC")
App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb4FYP1VxY1ZXfk_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZC").addGeometry(Part.Circle(App.Vector(-14.55000000000000,-1.25000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Pocket","Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC")
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZC")
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Plane", "plane_Sketch_Fb4FYP1VxY1ZXfk_1_JZG")
origin = App.Vector(0.70000000000000,-0.60000000000000,-1.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb4FYP1VxY1ZXfk_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("Sketcher::SketchObject","Sketch_Fb4FYP1VxY1ZXfk_1_JZG")
App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb4FYP1VxY1ZXfk_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZG").addGeometry(Part.Circle(App.Vector(15.45000000000000,-1.25000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FKj4K35xYq72SmO_0").newObject("PartDesign::Pocket","Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG")
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZG")
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb4FYP1VxY1ZXfk_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb4FYP1VxY1ZXfk_1_Fs8FwjYxLt2ZGbd_1_JZG").Offset = 0
App.ActiveDocument.recompute()

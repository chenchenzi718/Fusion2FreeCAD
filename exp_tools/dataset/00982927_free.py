import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00982927")
App.ActiveDocument.addObject("PartDesign::Body","Body_FoFjJsrX11lhDqO_0")
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").Label = "Body_FoFjJsrX11lhDqO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Plane", "plane_Sketch_FoFjJsrX11lhDqO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoFjJsrX11lhDqO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("Sketcher::SketchObject","Sketch_FoFjJsrX11lhDqO_0_JGC")
App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoFjJsrX11lhDqO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(609.60000000000002,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC").addGeometry(Part.LineSegment(App.Vector(609.60000000000002,0.00000000000000,0.00000000000000),App.Vector(609.60000000000002,206.37500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,206.37500000000000,0.00000000000000),App.Vector(609.60000000000002,206.37500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,206.37500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Pad","Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC")
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC")
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").Length = 19.05
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoFjJsrX11lhDqO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoFjJsrX11lhDqO_0_Fyy17QlgOOsnLS4_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Plane", "plane_Sketch_FBmuWaBHdmJQ0M4_1_JJC")
origin = App.Vector(304.80000000000001,103.18750000000000,19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBmuWaBHdmJQ0M4_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("Sketcher::SketchObject","Sketch_FBmuWaBHdmJQ0M4_1_JJC")
App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBmuWaBHdmJQ0M4_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC").addGeometry(Part.LineSegment(App.Vector(-215.90000000000001,-84.13750000000000,0.00000000000000),App.Vector(215.90000000000003,-84.13750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC").addGeometry(Part.LineSegment(App.Vector(215.90000000000003,-84.13750000000000,0.00000000000000),App.Vector(215.90000000000003,84.13749999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC").addGeometry(Part.LineSegment(App.Vector(-215.90000000000001,84.13749999999999,0.00000000000000),App.Vector(215.90000000000003,84.13749999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC").addGeometry(Part.LineSegment(App.Vector(-215.90000000000001,-84.13750000000000,0.00000000000000),App.Vector(-215.90000000000001,84.13749999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Pad","Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC")
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC")
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").Length = 63.5
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBmuWaBHdmJQ0M4_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBmuWaBHdmJQ0M4_1_FbvWHG0CAyRAVvE_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Plane", "plane_Sketch_F7PTV7oWngdrXSI_1_JNC")
origin = App.Vector(304.80000000000001,103.18750000000000,19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7PTV7oWngdrXSI_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("Sketcher::SketchObject","Sketch_F7PTV7oWngdrXSI_1_JNC")
App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7PTV7oWngdrXSI_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-304.80000000000001,-103.18750000000000,0.00000000000000),App.Vector(-285.75000000000000,-103.18750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-285.75000000000000,-103.18750000000000,0.00000000000000),App.Vector(-285.75000000000000,103.18750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-304.80000000000001,103.18750000000000,0.00000000000000),App.Vector(-285.75000000000000,103.18750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-304.80000000000001,-103.18750000000000,0.00000000000000),App.Vector(-304.80000000000001,103.18750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Pad","Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC")
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC")
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").Length = 203.20000000000002
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Plane", "plane_Sketch_F7PTV7oWngdrXSI_1_JNG")
origin = App.Vector(304.80000000000001,103.18750000000000,19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7PTV7oWngdrXSI_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("Sketcher::SketchObject","Sketch_F7PTV7oWngdrXSI_1_JNG")
App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7PTV7oWngdrXSI_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG").addGeometry(Part.LineSegment(App.Vector(304.80000000000001,-103.18750000000000,0.00000000000000),App.Vector(285.75000000000000,-103.18750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG").addGeometry(Part.LineSegment(App.Vector(285.75000000000000,-103.18750000000000,0.00000000000000),App.Vector(285.75000000000000,103.18750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG").addGeometry(Part.LineSegment(App.Vector(304.80000000000001,103.18750000000000,0.00000000000000),App.Vector(285.75000000000000,103.18750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG").addGeometry(Part.LineSegment(App.Vector(304.80000000000001,-103.18750000000000,0.00000000000000),App.Vector(304.80000000000001,103.18750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Pad","Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG")
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG")
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").Length = 203.20000000000002
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7PTV7oWngdrXSI_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7PTV7oWngdrXSI_1_FEQbUypIVRy89EZ_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Plane", "plane_Sketch_FGkiJQALUwrLzGO_1_JRC")
origin = App.Vector(304.80000000000001,103.18750000000000,19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGkiJQALUwrLzGO_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("Sketcher::SketchObject","Sketch_FGkiJQALUwrLzGO_1_JRC")
App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGkiJQALUwrLzGO_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC").addGeometry(Part.LineSegment(App.Vector(-285.75000000000000,-65.08749999999999,0.00000000000000),App.Vector(-234.95000000000002,-65.08749999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC").addGeometry(Part.LineSegment(App.Vector(-234.95000000000002,-65.08749999999999,0.00000000000000),App.Vector(-234.95000000000002,65.08750000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC").addGeometry(Part.LineSegment(App.Vector(-285.75000000000000,65.08750000000001,0.00000000000000),App.Vector(-234.95000000000002,65.08750000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC").addGeometry(Part.LineSegment(App.Vector(-285.75000000000000,-65.08749999999999,0.00000000000000),App.Vector(-285.75000000000000,65.08750000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Pad","Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC")
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC")
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Plane", "plane_Sketch_FGkiJQALUwrLzGO_1_JRG")
origin = App.Vector(304.80000000000001,103.18750000000000,19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGkiJQALUwrLzGO_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("Sketcher::SketchObject","Sketch_FGkiJQALUwrLzGO_1_JRG")
App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGkiJQALUwrLzGO_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG").addGeometry(Part.LineSegment(App.Vector(285.75000000000000,-65.08749999999999,0.00000000000000),App.Vector(234.94999999999993,-65.08749999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG").addGeometry(Part.LineSegment(App.Vector(234.94999999999993,-65.08749999999999,0.00000000000000),App.Vector(234.94999999999993,65.08750000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG").addGeometry(Part.LineSegment(App.Vector(285.75000000000000,65.08750000000001,0.00000000000000),App.Vector(234.94999999999993,65.08750000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG").addGeometry(Part.LineSegment(App.Vector(285.75000000000000,-65.08749999999999,0.00000000000000),App.Vector(285.75000000000000,65.08750000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Pad","Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG")
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG")
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGkiJQALUwrLzGO_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGkiJQALUwrLzGO_1_F44ZqSkNrN5FdZW_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Plane", "plane_Sketch_FSUFxr4JKLNpjEL_1_JVC")
origin = App.Vector(19.05000000000000,9.52500000000000,120.64999999999999)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSUFxr4JKLNpjEL_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("Sketcher::SketchObject","Sketch_FSUFxr4JKLNpjEL_1_JVC")
App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSUFxr4JKLNpjEL_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC").addGeometry(Part.LineSegment(App.Vector(28.57500000000000,101.60000000000001,0.00000000000000),App.Vector(158.75000000000000,101.60000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC").addGeometry(Part.LineSegment(App.Vector(158.75000000000000,101.60000000000001,0.00000000000000),App.Vector(158.75000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC").addGeometry(Part.LineSegment(App.Vector(158.75000000000000,50.80000000000000,0.00000000000000),App.Vector(28.57500000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC").addGeometry(Part.LineSegment(App.Vector(28.57500000000000,101.60000000000001,0.00000000000000),App.Vector(28.57500000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Pad","Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC")
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC")
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSUFxr4JKLNpjEL_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSUFxr4JKLNpjEL_1_FofShpTOt9CXyaL_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Plane", "plane_Sketch_F1bvItwIWWm7Ukh_1_JZC")
origin = App.Vector(590.55000000000007,9.52500000000000,120.64999999999999)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1bvItwIWWm7Ukh_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("Sketcher::SketchObject","Sketch_F1bvItwIWWm7Ukh_1_JZC")
App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1bvItwIWWm7Ukh_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,101.60000000000001,0.00000000000000),App.Vector(-158.75000000000000,101.60000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC").addGeometry(Part.LineSegment(App.Vector(-158.75000000000000,101.60000000000001,0.00000000000000),App.Vector(-158.75000000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC").addGeometry(Part.LineSegment(App.Vector(-158.75000000000000,50.80000000000000,0.00000000000000),App.Vector(-28.57500000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,101.60000000000001,0.00000000000000),App.Vector(-28.57500000000000,50.80000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoFjJsrX11lhDqO_0").newObject("PartDesign::Pad","Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC")
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC")
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1bvItwIWWm7Ukh_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1bvItwIWWm7Ukh_1_F5LpuSy1zwd7Ygz_1_JZC").Offset = 0
App.ActiveDocument.recompute()

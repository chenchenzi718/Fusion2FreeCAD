import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00810940")
App.ActiveDocument.addObject("PartDesign::Body","Body_FIssq21zIJiOjq5_0")
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").Label = "Body_FIssq21zIJiOjq5_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Plane", "plane_Sketch_FIssq21zIJiOjq5_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIssq21zIJiOjq5_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("Sketcher::SketchObject","Sketch_FIssq21zIJiOjq5_0_JGC")
App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIssq21zIJiOjq5_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,25.00000000000000,0.00000000000000),App.Vector(148.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(148.00000000000000,27.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,29.00000000000000,0.00000000000000),App.Vector(148.00000000000000,29.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),29.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-29.00000000000000,0.00000000000000),App.Vector(148.00000000000000,-29.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(148.00000000000000,-27.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").addGeometry(Part.LineSegment(App.Vector(148.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Pad","Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC")
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC")
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").Length = 218.0
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIssq21zIJiOjq5_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FIssq21zIJiOjq5_0_FwPmCYj8AZMwVmj_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Plane", "plane_Sketch_F0Fss6RHkjcZwIM_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0Fss6RHkjcZwIM_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("Sketcher::SketchObject","Sketch_F0Fss6RHkjcZwIM_1_JJC")
App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0Fss6RHkjcZwIM_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,25.00000000000000,0.00000000000000),App.Vector(144.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC").addGeometry(Part.LineSegment(App.Vector(144.00000000000000,25.00000000000000,0.00000000000000),App.Vector(144.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC").addGeometry(Part.LineSegment(App.Vector(144.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Pad","Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC")
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC")
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").Length = 214.0
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0Fss6RHkjcZwIM_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F0Fss6RHkjcZwIM_1_FvphWJpA4to4CIg_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Plane", "plane_Sketch_FANOcXvvexChPMA_1_JNC")
origin = App.Vector(74.00000000000000,0.00000000000000,29.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("Sketcher::SketchObject","Sketch_FANOcXvvexChPMA_1_JNC")
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC").addGeometry(Part.LineSegment(App.Vector(-68.99999999999999,104.00000000000000,0.00000000000000),App.Vector(-1.00000000000000,104.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC").addGeometry(Part.LineSegment(App.Vector(-1.00000000000000,104.00000000000000,0.00000000000000),App.Vector(-1.00000000000000,36.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC").addGeometry(Part.LineSegment(App.Vector(-68.99999999999999,36.00000000000000,0.00000000000000),App.Vector(-1.00000000000000,36.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC").addGeometry(Part.LineSegment(App.Vector(-68.99999999999999,104.00000000000000,0.00000000000000),App.Vector(-68.99999999999999,36.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Pad","Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").Length = 1.5
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Plane", "plane_Sketch_FANOcXvvexChPMA_1_JNG")
origin = App.Vector(74.00000000000000,0.00000000000000,29.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("Sketcher::SketchObject","Sketch_FANOcXvvexChPMA_1_JNG")
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG").addGeometry(Part.LineSegment(App.Vector(-68.99999999999999,34.00000000000000,0.00000000000000),App.Vector(-1.00000000000000,34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG").addGeometry(Part.LineSegment(App.Vector(-1.00000000000000,34.00000000000000,0.00000000000000),App.Vector(-1.00000000000000,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG").addGeometry(Part.LineSegment(App.Vector(-68.99999999999999,-34.00000000000000,0.00000000000000),App.Vector(-1.00000000000000,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG").addGeometry(Part.LineSegment(App.Vector(-68.99999999999999,34.00000000000000,0.00000000000000),App.Vector(-68.99999999999999,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Pad","Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").Length = 1.5
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Plane", "plane_Sketch_FANOcXvvexChPMA_1_JNK")
origin = App.Vector(74.00000000000000,0.00000000000000,29.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("Sketcher::SketchObject","Sketch_FANOcXvvexChPMA_1_JNK")
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK").addGeometry(Part.LineSegment(App.Vector(-68.99999999999999,-36.00000000000000,0.00000000000000),App.Vector(-1.00000000000000,-36.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK").addGeometry(Part.LineSegment(App.Vector(-1.00000000000000,-36.00000000000000,0.00000000000000),App.Vector(-1.00000000000000,-104.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK").addGeometry(Part.LineSegment(App.Vector(-68.99999999999999,-104.00000000000000,0.00000000000000),App.Vector(-1.00000000000000,-104.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK").addGeometry(Part.LineSegment(App.Vector(-68.99999999999999,-36.00000000000000,0.00000000000000),App.Vector(-68.99999999999999,-104.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Pad","Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").Length = 1.5
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Plane", "plane_Sketch_FANOcXvvexChPMA_1_JNO")
origin = App.Vector(74.00000000000000,0.00000000000000,29.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("Sketcher::SketchObject","Sketch_FANOcXvvexChPMA_1_JNO")
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,104.00000000000000,0.00000000000000),App.Vector(68.99999999999999,104.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO").addGeometry(Part.LineSegment(App.Vector(68.99999999999999,104.00000000000000,0.00000000000000),App.Vector(68.99999999999999,36.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,36.00000000000000,0.00000000000000),App.Vector(68.99999999999999,36.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,104.00000000000000,0.00000000000000),App.Vector(1.00000000000000,36.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Pad","Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").Length = 1.5
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Plane", "plane_Sketch_FANOcXvvexChPMA_1_JNS")
origin = App.Vector(74.00000000000000,0.00000000000000,29.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("Sketcher::SketchObject","Sketch_FANOcXvvexChPMA_1_JNS")
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,34.00000000000000,0.00000000000000),App.Vector(68.99999999999999,34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS").addGeometry(Part.LineSegment(App.Vector(68.99999999999999,34.00000000000000,0.00000000000000),App.Vector(68.99999999999999,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,-34.00000000000000,0.00000000000000),App.Vector(68.99999999999999,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,34.00000000000000,0.00000000000000),App.Vector(1.00000000000000,-34.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Pad","Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").Length = 1.5
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Plane", "plane_Sketch_FANOcXvvexChPMA_1_JNW")
origin = App.Vector(74.00000000000000,0.00000000000000,29.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("Sketcher::SketchObject","Sketch_FANOcXvvexChPMA_1_JNW")
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FANOcXvvexChPMA_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,-36.00000000000000,0.00000000000000),App.Vector(68.99999999999999,-36.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW").addGeometry(Part.LineSegment(App.Vector(68.99999999999999,-36.00000000000000,0.00000000000000),App.Vector(68.99999999999999,-104.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,-104.00000000000000,0.00000000000000),App.Vector(68.99999999999999,-104.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,-36.00000000000000,0.00000000000000),App.Vector(1.00000000000000,-104.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIssq21zIJiOjq5_0").newObject("PartDesign::Pad","Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW")
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").Length = 1.5
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FANOcXvvexChPMA_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FANOcXvvexChPMA_1_FseVmek223HJjfj_1_JNW").Offset = 0
App.ActiveDocument.recompute()

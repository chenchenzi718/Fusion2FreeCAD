import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00501540")
App.ActiveDocument.addObject("PartDesign::Body","Body_FdG6YbVh1Rz75XQ_0")
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").Label = "Body_FdG6YbVh1Rz75XQ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Plane", "plane_Sketch_FdG6YbVh1Rz75XQ_0_JGa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdG6YbVh1Rz75XQ_0_JGa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("Sketcher::SketchObject","Sketch_FdG6YbVh1Rz75XQ_0_JGa")
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdG6YbVh1Rz75XQ_0_JGa"), [""])
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,9.07619000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(30.47943000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").addGeometry(Part.LineSegment(App.Vector(30.47943000000000,0.00000000000000,0.00000000000000),App.Vector(30.47943000000000,8.89000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,9.07619000000000,0.00000000000000),App.Vector(30.47943000000000,8.89000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").addGeometry(Part.Circle(App.Vector(7.62000000000000,5.71500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.91927000000000),False)

App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").addGeometry(Part.Circle(App.Vector(15.24000000000000,5.71500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.91927000000000),False)

App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").addGeometry(Part.Circle(App.Vector(22.86000000000000,5.71500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.91927000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Pad","Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa")
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").Profile = App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa")
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").Length = 7.62
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").Type = 4
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Plane", "plane_Sketch_FdG6YbVh1Rz75XQ_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdG6YbVh1Rz75XQ_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("Sketcher::SketchObject","Sketch_FdG6YbVh1Rz75XQ_0_JGS")
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdG6YbVh1Rz75XQ_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGS").addGeometry(Part.Circle(App.Vector(15.24000000000000,5.71500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.91927000000000),False)

App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGS").addGeometry(Part.Circle(App.Vector(15.24000000000000,5.71500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50492000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Pad","Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS")
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").Profile = App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGS")
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").Length = 7.62
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Plane", "plane_Sketch_FdG6YbVh1Rz75XQ_0_JGW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdG6YbVh1Rz75XQ_0_JGW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("Sketcher::SketchObject","Sketch_FdG6YbVh1Rz75XQ_0_JGW")
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdG6YbVh1Rz75XQ_0_JGW"), [""])
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGW").addGeometry(Part.Circle(App.Vector(22.86000000000000,5.71500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.91927000000000),False)

App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGW").addGeometry(Part.Circle(App.Vector(22.86000000000000,5.71500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50492000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Pad","Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW")
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").Profile = App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGW")
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").Length = 7.62
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").Type = 4
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Plane", "plane_Sketch_FdG6YbVh1Rz75XQ_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdG6YbVh1Rz75XQ_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("Sketcher::SketchObject","Sketch_FdG6YbVh1Rz75XQ_0_JGO")
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdG6YbVh1Rz75XQ_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGO").addGeometry(Part.Circle(App.Vector(7.62000000000000,5.71500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.91927000000000),False)

App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGO").addGeometry(Part.Circle(App.Vector(7.62000000000000,5.71500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50492000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Pad","Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO")
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGO")
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").Length = 7.62
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdG6YbVh1Rz75XQ_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdG6YbVh1Rz75XQ_0_FbIHbKgDedp5UV6_0_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Plane", "plane_Sketch_FASH99KUReRpQsS_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FASH99KUReRpQsS_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("Sketcher::SketchObject","Sketch_FASH99KUReRpQsS_1_JJC")
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FASH99KUReRpQsS_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJC").addGeometry(Part.Circle(App.Vector(4.26795000000000,-3.81000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.41300000000000),False)

App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJC").addGeometry(Part.Circle(App.Vector(4.26795000000000,-3.81000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Pad","Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC")
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJC")
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").Length = 1.905
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Plane", "plane_Sketch_FASH99KUReRpQsS_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FASH99KUReRpQsS_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("Sketcher::SketchObject","Sketch_FASH99KUReRpQsS_1_JJK")
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FASH99KUReRpQsS_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJK").addGeometry(Part.Circle(App.Vector(11.88795000000000,-3.81000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.41300000000000),False)

App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJK").addGeometry(Part.Circle(App.Vector(11.88795000000000,-3.81000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Pad","Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK")
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJK")
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").Length = 1.905
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Plane", "plane_Sketch_FASH99KUReRpQsS_1_JJS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FASH99KUReRpQsS_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("Sketcher::SketchObject","Sketch_FASH99KUReRpQsS_1_JJS")
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FASH99KUReRpQsS_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJS").addGeometry(Part.Circle(App.Vector(19.50795000000000,-3.81000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.41300000000000),False)

App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJS").addGeometry(Part.Circle(App.Vector(19.50795000000000,-3.81000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Pad","Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS")
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJS")
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").Length = 1.905
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").Type = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").Reversed = 1
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Plane", "plane_Sketch_FASH99KUReRpQsS_1_JJa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FASH99KUReRpQsS_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("Sketcher::SketchObject","Sketch_FASH99KUReRpQsS_1_JJa")
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FASH99KUReRpQsS_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJa").addGeometry(Part.Circle(App.Vector(27.12795000000000,-3.81000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.41300000000000),False)

App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJa").addGeometry(Part.Circle(App.Vector(27.12795000000000,-3.81000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FdG6YbVh1Rz75XQ_0").newObject("PartDesign::Pad","Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa")
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJa")
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").Length = 1.905
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FASH99KUReRpQsS_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").Type = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").Reversed = 1
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FASH99KUReRpQsS_1_FNmYsg7Ohl0UJQl_1_JJa").Offset = 0
App.ActiveDocument.recompute()

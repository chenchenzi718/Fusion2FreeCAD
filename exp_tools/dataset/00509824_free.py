import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00509824")
App.ActiveDocument.addObject("PartDesign::Body","Body_FmyNfuUsTM31kPO_0")
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").Label = "Body_FmyNfuUsTM31kPO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Plane", "plane_Sketch_FmyNfuUsTM31kPO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmyNfuUsTM31kPO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("Sketcher::SketchObject","Sketch_FmyNfuUsTM31kPO_0_JGC")
App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmyNfuUsTM31kPO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").addGeometry(Part.LineSegment(App.Vector(72.50000000000000,-43.25000000000000,0.00000000000000),App.Vector(-72.50000000000000,-43.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-72.50000000000000,-38.25000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-77.50000000000000,-38.25000000000000,0.00000000000000),App.Vector(-77.50000000000000,38.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-72.50000000000000,38.25000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").addGeometry(Part.LineSegment(App.Vector(72.50000000000000,43.25000000000000,0.00000000000000),App.Vector(-72.50000000000000,43.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(72.50000000000000,38.25000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").addGeometry(Part.LineSegment(App.Vector(77.50000000000000,-38.25000000000000,0.00000000000000),App.Vector(77.50000000000000,38.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(72.50000000000000,-38.25000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Pad","Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC")
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC")
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").Length = 21.0
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmyNfuUsTM31kPO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmyNfuUsTM31kPO_0_FLgSEKxhEmlDxLO_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Plane", "plane_Sketch_FJW35rJ7AAFTRB0_1_JLC")
origin = App.Vector(-0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJW35rJ7AAFTRB0_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("Sketcher::SketchObject","Sketch_FJW35rJ7AAFTRB0_1_JLC")
App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJW35rJ7AAFTRB0_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-58.47038999999999,0.00000000000000,0.00000000000000),App.Vector(-48.47039000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-48.47039000000000,0.00000000000000,0.00000000000000),App.Vector(-48.47039000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-48.47039000000000,-5.00000000000000,0.00000000000000),App.Vector(-58.47038999999999,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-58.47038999999999,-5.00000000000000,0.00000000000000),App.Vector(-58.47038999999999,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-58.47038999999999,-15.00000000000000,0.00000000000000),App.Vector(-63.47039000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-63.47039000000000,-15.00000000000000,0.00000000000000),App.Vector(-63.47039000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-63.47039000000000,-5.00000000000000,0.00000000000000),App.Vector(-73.47038999999999,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-73.47038999999999,-5.00000000000000,0.00000000000000),App.Vector(-73.47038999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-73.47038999999999,0.00000000000000,0.00000000000000),App.Vector(-63.47039000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-63.47039000000000,0.00000000000000,0.00000000000000),App.Vector(-63.47039000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-63.47039000000000,10.00000000000000,0.00000000000000),App.Vector(-58.47038999999999,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").addGeometry(Part.LineSegment(App.Vector(-58.47038999999999,0.00000000000000,0.00000000000000),App.Vector(-58.47038999999999,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Pad","Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC")
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC")
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJW35rJ7AAFTRB0_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJW35rJ7AAFTRB0_1_FMxiLHAtpxlTKHg_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Plane", "plane_Sketch_F2vEbdoygeypFWM_1_JPC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2vEbdoygeypFWM_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("Sketcher::SketchObject","Sketch_F2vEbdoygeypFWM_1_JPC")
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2vEbdoygeypFWM_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPC").addGeometry(Part.Circle(App.Vector(60.57566000000001,10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Pad","Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC")
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPC")
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").Length = 5.0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Plane", "plane_Sketch_F2vEbdoygeypFWM_1_JPG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2vEbdoygeypFWM_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("Sketcher::SketchObject","Sketch_F2vEbdoygeypFWM_1_JPG")
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2vEbdoygeypFWM_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPG").addGeometry(Part.Circle(App.Vector(70.57566000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Pad","Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG")
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPG")
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").Length = 5.0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Plane", "plane_Sketch_F2vEbdoygeypFWM_1_JPK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2vEbdoygeypFWM_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("Sketcher::SketchObject","Sketch_F2vEbdoygeypFWM_1_JPK")
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2vEbdoygeypFWM_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPK").addGeometry(Part.Circle(App.Vector(60.57566000000001,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Pad","Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK")
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPK")
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").Length = 5.0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Plane", "plane_Sketch_F2vEbdoygeypFWM_1_JPO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2vEbdoygeypFWM_1_JPO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("Sketcher::SketchObject","Sketch_F2vEbdoygeypFWM_1_JPO")
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2vEbdoygeypFWM_1_JPO"), [""])
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPO").addGeometry(Part.Circle(App.Vector(50.57566000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Pad","Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO")
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").Profile = App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPO")
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").Length = 5.0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2vEbdoygeypFWM_1_JPO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").Type = 4
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2vEbdoygeypFWM_1_FUzOnMOmXLUxBKX_1_JPO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Plane", "plane_Sketch_F50kjDgSWbUFTYi_1_JJC")
origin = App.Vector(-0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F50kjDgSWbUFTYi_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("Sketcher::SketchObject","Sketch_F50kjDgSWbUFTYi_1_JJC")
App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F50kjDgSWbUFTYi_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC").addGeometry(Part.LineSegment(App.Vector(42.50000000000000,-32.50000000000000,0.00000000000000),App.Vector(-42.50000000000000,-32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC").addGeometry(Part.LineSegment(App.Vector(-42.50000000000000,-32.50000000000000,0.00000000000000),App.Vector(-42.50000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC").addGeometry(Part.LineSegment(App.Vector(42.50000000000000,32.50000000000000,0.00000000000000),App.Vector(-42.50000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC").addGeometry(Part.LineSegment(App.Vector(42.50000000000000,-32.50000000000000,0.00000000000000),App.Vector(42.50000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Pocket","Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC")
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC")
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").Length = 1.0
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F50kjDgSWbUFTYi_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F50kjDgSWbUFTYi_1_FoEDMev81Vj6fgX_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Plane", "plane_Sketch_FjjMgP65sMnBwOh_1_JVC")
origin = App.Vector(-0.00000000000000,10.50000000000000,43.25000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjjMgP65sMnBwOh_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("Sketcher::SketchObject","Sketch_FjjMgP65sMnBwOh_1_JVC")
App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjjMgP65sMnBwOh_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").addGeometry(Part.LineSegment(App.Vector(1.67676000000000,-0.92500000000000,0.00000000000000),App.Vector(-1.67676000000000,-0.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").addGeometry(Part.LineSegment(App.Vector(-1.67676000000000,-0.92500000000000,0.00000000000000),App.Vector(-3.45000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").addGeometry(Part.LineSegment(App.Vector(-3.45000000000000,0.92500000000000,0.00000000000000),App.Vector(-3.45000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").addGeometry(Part.LineSegment(App.Vector(3.45000000000000,0.92500000000000,0.00000000000000),App.Vector(-3.45000000000000,0.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").addGeometry(Part.LineSegment(App.Vector(3.45000000000000,0.92500000000000,0.00000000000000),App.Vector(3.45000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").addGeometry(Part.LineSegment(App.Vector(1.67676000000000,-0.92500000000000,0.00000000000000),App.Vector(3.45000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmyNfuUsTM31kPO_0").newObject("PartDesign::Pocket","Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC")
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC")
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").Length = 11.0
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjjMgP65sMnBwOh_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjjMgP65sMnBwOh_1_FDhLkOmVvwFFjj2_1_JVC").Offset = 0
App.ActiveDocument.recompute()

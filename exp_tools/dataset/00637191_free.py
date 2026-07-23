import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00637191")
App.ActiveDocument.addObject("PartDesign::Body","Body_FALHGauBLYbMX33_0")
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").Label = "Body_FALHGauBLYbMX33_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_FALHGauBLYbMX33_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FALHGauBLYbMX33_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_FALHGauBLYbMX33_0_JGC")
App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FALHGauBLYbMX33_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.00000000000000,32.50000000000000,0.00000000000000),App.Vector(22.00000000000000,32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC").addGeometry(Part.LineSegment(App.Vector(22.00000000000000,32.50000000000000,0.00000000000000),App.Vector(22.00000000000000,-32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.00000000000000,-32.50000000000000,0.00000000000000),App.Vector(22.00000000000000,-32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.00000000000000,32.50000000000000,0.00000000000000),App.Vector(-22.00000000000000,-32.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pad","Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC")
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC")
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").Length = 11.5
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FALHGauBLYbMX33_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FALHGauBLYbMX33_0_FWVY2jmLvPda923_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_F5MLXCLKeBcc8lG_1_JJC")
origin = App.Vector(-0.00000000000000,0.00000000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5MLXCLKeBcc8lG_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_F5MLXCLKeBcc8lG_1_JJC")
App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5MLXCLKeBcc8lG_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,30.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,-30.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-30.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,-30.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(20.00000000000000,-30.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pocket","Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC")
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC")
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").Length = 10.25
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5MLXCLKeBcc8lG_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5MLXCLKeBcc8lG_1_F6QFUtQQm6ONmjb_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_FEIoQRBRsHnPU9B_1_JNa")
origin = App.Vector(-0.00000000000000,0.00000000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEIoQRBRsHnPU9B_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_FEIoQRBRsHnPU9B_1_JNa")
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEIoQRBRsHnPU9B_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNa").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(20.00000000000000,-30.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNa").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-30.50000000000000,0.00000000000000),App.Vector(18.00000000000000,-30.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNa").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-30.50000000000000,0.00000000000000),App.Vector(20.00000000000000,-28.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pad","Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa")
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNa")
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").Length = 11.0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").Type = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").Reversed = 1
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_FEIoQRBRsHnPU9B_1_JNW")
origin = App.Vector(-0.00000000000000,0.00000000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEIoQRBRsHnPU9B_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_FEIoQRBRsHnPU9B_1_JNW")
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEIoQRBRsHnPU9B_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNW").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-20.00000000000000,-30.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNW").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-30.50000000000000,0.00000000000000),App.Vector(-18.00000000000000,-30.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNW").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-30.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,-28.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pad","Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW")
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNW")
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").Length = 11.0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").Type = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").Reversed = 1
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_FEIoQRBRsHnPU9B_1_JNe")
origin = App.Vector(-0.00000000000000,0.00000000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEIoQRBRsHnPU9B_1_JNe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_FEIoQRBRsHnPU9B_1_JNe")
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEIoQRBRsHnPU9B_1_JNe"), [""])
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNe").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNe").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(20.00000000000000,28.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNe").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(18.00000000000000,30.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pad","Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe")
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").Profile = App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNe")
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").Length = 11.0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").Type = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").Reversed = 1
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_FEIoQRBRsHnPU9B_1_JNS")
origin = App.Vector(-0.00000000000000,0.00000000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEIoQRBRsHnPU9B_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_FEIoQRBRsHnPU9B_1_JNS")
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEIoQRBRsHnPU9B_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNS").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,28.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNS").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(-18.00000000000000,30.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pad","Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS")
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNS")
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").Length = 11.0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEIoQRBRsHnPU9B_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").Type = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").Reversed = 1
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEIoQRBRsHnPU9B_1_FbwWUm4F6MDJpcv_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_FT2e8oNXIokyNre_1_JRG")
origin = App.Vector(-0.00000000000000,0.00000000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FT2e8oNXIokyNre_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_FT2e8oNXIokyNre_1_JRG")
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FT2e8oNXIokyNre_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRG").addGeometry(Part.Circle(App.Vector(-20.00000000000000,-30.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.32500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pocket","Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG")
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRG")
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").Length = 7.0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_FT2e8oNXIokyNre_1_JRC")
origin = App.Vector(-0.00000000000000,0.00000000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FT2e8oNXIokyNre_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_FT2e8oNXIokyNre_1_JRC")
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FT2e8oNXIokyNre_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRC").addGeometry(Part.Circle(App.Vector(-20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.32500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pocket","Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC")
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRC")
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").Length = 7.0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_FT2e8oNXIokyNre_1_JRO")
origin = App.Vector(-0.00000000000000,0.00000000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FT2e8oNXIokyNre_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_FT2e8oNXIokyNre_1_JRO")
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FT2e8oNXIokyNre_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRO").addGeometry(Part.Circle(App.Vector(20.00000000000000,30.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.32500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pocket","Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO")
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRO")
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").Length = 7.0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Plane", "plane_Sketch_FT2e8oNXIokyNre_1_JRK")
origin = App.Vector(-0.00000000000000,0.00000000000000,11.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FT2e8oNXIokyNre_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("Sketcher::SketchObject","Sketch_FT2e8oNXIokyNre_1_JRK")
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FT2e8oNXIokyNre_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRK").addGeometry(Part.Circle(App.Vector(20.00000000000000,-30.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.32500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FALHGauBLYbMX33_0").newObject("PartDesign::Pocket","Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK")
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRK")
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").Length = 7.0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FT2e8oNXIokyNre_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FT2e8oNXIokyNre_1_FI005SPvyd7TpRv_1_JRK").Offset = 0
App.ActiveDocument.recompute()

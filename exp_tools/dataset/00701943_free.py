import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00701943")
App.ActiveDocument.addObject("PartDesign::Body","Body_FSmjRuTLlkcZhs5_0")
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").Label = "Body_FSmjRuTLlkcZhs5_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Plane", "plane_Sketch_FSmjRuTLlkcZhs5_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSmjRuTLlkcZhs5_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("Sketcher::SketchObject","Sketch_FSmjRuTLlkcZhs5_0_JGC")
App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSmjRuTLlkcZhs5_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,10.00000000000000,0.00000000000000),App.Vector(-20.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(30.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,0.00000000000000,0.00000000000000),App.Vector(30.00000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,10.00000000000000,0.00000000000000),App.Vector(30.00000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Pad","Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC")
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC")
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").Length = 1.0
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSmjRuTLlkcZhs5_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSmjRuTLlkcZhs5_0_F64E40u5zymgi1C_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Plane", "plane_Sketch_FoDU1ITdx0CmdMn_1_JLu")
origin = App.Vector(5.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLu").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("Sketcher::SketchObject","Sketch_FoDU1ITdx0CmdMn_1_JLu")
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLu"), [""])
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,1.00000000000000,0.00000000000000),App.Vector(-24.00000000000000,1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,1.00000000000000,0.00000000000000),App.Vector(-24.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,9.00000000000000,0.00000000000000),App.Vector(-16.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,1.00000000000000,0.00000000000000),App.Vector(-16.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Pad","Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").Profile = App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").Length = 1.0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLu"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").Type = 4
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLu").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Plane", "plane_Sketch_FoDU1ITdx0CmdMn_1_JL2")
origin = App.Vector(5.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JL2").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("Sketcher::SketchObject","Sketch_FoDU1ITdx0CmdMn_1_JL2")
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JL2"), [""])
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,-9.00000000000000,0.00000000000000),App.Vector(-16.00000000000000,-9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,-9.00000000000000,0.00000000000000),App.Vector(-16.00000000000000,-1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,-1.00000000000000,0.00000000000000),App.Vector(-16.00000000000000,-1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,-9.00000000000000,0.00000000000000),App.Vector(-24.00000000000000,-1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Pad","Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").Profile = App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").Length = 1.0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JL2"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").Type = 4
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JL2").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Plane", "plane_Sketch_FoDU1ITdx0CmdMn_1_JLy")
origin = App.Vector(5.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLy").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("Sketcher::SketchObject","Sketch_FoDU1ITdx0CmdMn_1_JLy")
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLy"), [""])
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,-9.00000000000000,0.00000000000000),App.Vector(-6.00000000000000,-1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,-1.00000000000000,0.00000000000000),App.Vector(-14.00000000000000,-1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy").addGeometry(Part.LineSegment(App.Vector(-14.00000000000000,-9.00000000000000,0.00000000000000),App.Vector(-14.00000000000000,-1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,-9.00000000000000,0.00000000000000),App.Vector(-14.00000000000000,-9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Pad","Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").Profile = App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").Length = 1.0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLy"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").Type = 4
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLy").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Plane", "plane_Sketch_FoDU1ITdx0CmdMn_1_JLe")
origin = App.Vector(5.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("Sketcher::SketchObject","Sketch_FoDU1ITdx0CmdMn_1_JLe")
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLe"), [""])
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,1.00000000000000,0.00000000000000),App.Vector(-14.00000000000000,1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe").addGeometry(Part.LineSegment(App.Vector(-14.00000000000000,1.00000000000000,0.00000000000000),App.Vector(-14.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,9.00000000000000,0.00000000000000),App.Vector(-14.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,1.00000000000000,0.00000000000000),App.Vector(-6.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Pad","Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").Profile = App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").Length = 1.0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").Type = 4
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Plane", "plane_Sketch_FoDU1ITdx0CmdMn_1_JLS")
origin = App.Vector(5.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("Sketcher::SketchObject","Sketch_FoDU1ITdx0CmdMn_1_JLS")
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLS"), [""])
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS").addGeometry(Part.LineSegment(App.Vector(4.00000000000000,1.00000000000000,0.00000000000000),App.Vector(-4.00000000000000,1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,1.00000000000000,0.00000000000000),App.Vector(-4.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,9.00000000000000,0.00000000000000),App.Vector(4.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS").addGeometry(Part.LineSegment(App.Vector(4.00000000000000,1.00000000000000,0.00000000000000),App.Vector(4.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Pad","Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").Profile = App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").Length = 1.0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").Type = 4
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Plane", "plane_Sketch_FoDU1ITdx0CmdMn_1_JLK")
origin = App.Vector(5.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("Sketcher::SketchObject","Sketch_FoDU1ITdx0CmdMn_1_JLK")
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK").addGeometry(Part.LineSegment(App.Vector(14.00000000000000,1.00000000000000,0.00000000000000),App.Vector(6.00000000000000,1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK").addGeometry(Part.LineSegment(App.Vector(6.00000000000000,1.00000000000000,0.00000000000000),App.Vector(6.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK").addGeometry(Part.LineSegment(App.Vector(6.00000000000000,9.00000000000000,0.00000000000000),App.Vector(14.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK").addGeometry(Part.LineSegment(App.Vector(14.00000000000000,1.00000000000000,0.00000000000000),App.Vector(14.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Pad","Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").Length = 1.0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Plane", "plane_Sketch_FoDU1ITdx0CmdMn_1_JLC")
origin = App.Vector(5.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("Sketcher::SketchObject","Sketch_FoDU1ITdx0CmdMn_1_JLC")
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoDU1ITdx0CmdMn_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,1.00000000000000,0.00000000000000),App.Vector(16.00000000000000,1.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,1.00000000000000,0.00000000000000),App.Vector(16.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,9.00000000000000,0.00000000000000),App.Vector(24.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,1.00000000000000,0.00000000000000),App.Vector(24.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSmjRuTLlkcZhs5_0").newObject("PartDesign::Pad","Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC")
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").Length = 1.0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoDU1ITdx0CmdMn_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoDU1ITdx0CmdMn_1_FbLgNI3qOluMANj_1_JLC").Offset = 0
App.ActiveDocument.recompute()

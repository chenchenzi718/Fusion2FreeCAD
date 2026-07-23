import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00229444")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fbt18DMA3dWmtrw_0")
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").Label = "Body_Fbt18DMA3dWmtrw_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Plane", "plane_Sketch_Fbt18DMA3dWmtrw_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fbt18DMA3dWmtrw_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("Sketcher::SketchObject","Sketch_Fbt18DMA3dWmtrw_0_JGC")
App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fbt18DMA3dWmtrw_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC").addGeometry(Part.LineSegment(App.Vector(550.00000000000000,550.00000000000000,0.00000000000000),App.Vector(-550.00000000000000,550.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC").addGeometry(Part.LineSegment(App.Vector(-550.00000000000000,550.00000000000000,0.00000000000000),App.Vector(-550.00000000000000,-550.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC").addGeometry(Part.LineSegment(App.Vector(550.00000000000000,-550.00000000000000,0.00000000000000),App.Vector(-550.00000000000000,-550.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC").addGeometry(Part.LineSegment(App.Vector(550.00000000000000,550.00000000000000,0.00000000000000),App.Vector(550.00000000000000,-550.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Pad","Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC")
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC")
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fbt18DMA3dWmtrw_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fbt18DMA3dWmtrw_0_FS5w2JBCiic7kaK_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Plane", "plane_Sketch_Fyhn728IvavsYT0_1_JJC")
origin = App.Vector(-0.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fyhn728IvavsYT0_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("Sketcher::SketchObject","Sketch_Fyhn728IvavsYT0_1_JJC")
App.ActiveDocument.getObject("Sketch_Fyhn728IvavsYT0_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fyhn728IvavsYT0_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fyhn728IvavsYT0_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fyhn728IvavsYT0_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),36.01007000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fyhn728IvavsYT0_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fyhn728IvavsYT0_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Pad","Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC")
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fyhn728IvavsYT0_1_JJC")
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").Length = 82.0
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fyhn728IvavsYT0_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fyhn728IvavsYT0_1_FldG1d0z6AK8H5K_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Plane", "plane_Sketch_FW9qfg6z5O4edD0_1_JNC")
origin = App.Vector(-0.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FW9qfg6z5O4edD0_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("Sketcher::SketchObject","Sketch_FW9qfg6z5O4edD0_1_JNC")
App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FW9qfg6z5O4edD0_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-250.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Pad","Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC")
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNC")
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_FAJTDkvjaoRJALg_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Plane", "plane_Sketch_FW9qfg6z5O4edD0_1_JNK")
origin = App.Vector(-0.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FW9qfg6z5O4edD0_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("Sketcher::SketchObject","Sketch_FW9qfg6z5O4edD0_1_JNK")
App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FW9qfg6z5O4edD0_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNK").addGeometry(Part.Circle(App.Vector(-216.50635000000000,125.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Pad","Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK")
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNK")
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Plane", "plane_Sketch_FW9qfg6z5O4edD0_1_JNG")
origin = App.Vector(-0.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FW9qfg6z5O4edD0_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("Sketcher::SketchObject","Sketch_FW9qfg6z5O4edD0_1_JNG")
App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FW9qfg6z5O4edD0_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNG").addGeometry(Part.Circle(App.Vector(216.50635000000000,125.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Pad","Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG")
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNG")
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FW9qfg6z5O4edD0_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FW9qfg6z5O4edD0_1_F0UWwCYbawD4ObP_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Plane", "plane_Sketch_Fxrp5TDWEL64SiK_1_JTC")
origin = App.Vector(-0.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fxrp5TDWEL64SiK_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("Sketcher::SketchObject","Sketch_Fxrp5TDWEL64SiK_1_JTC")
App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fxrp5TDWEL64SiK_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC").addGeometry(Part.LineSegment(App.Vector(77.86158000000000,215.61451000000000,0.00000000000000),App.Vector(102.86157999999999,172.31324000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC").addGeometry(Part.LineSegment(App.Vector(102.86157999999999,172.31324000000001,0.00000000000000),App.Vector(146.16285000000002,197.31324000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC").addGeometry(Part.LineSegment(App.Vector(146.16285000000002,197.31324000000001,0.00000000000000),App.Vector(121.16285000000001,240.61451000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC").addGeometry(Part.LineSegment(App.Vector(77.86158000000000,215.61451000000000,0.00000000000000),App.Vector(121.16285000000001,240.61451000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Pad","Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC")
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC")
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").Length = 50.0
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Plane", "plane_Sketch_Fxrp5TDWEL64SiK_1_JTK")
origin = App.Vector(-0.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fxrp5TDWEL64SiK_1_JTK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("Sketcher::SketchObject","Sketch_Fxrp5TDWEL64SiK_1_JTK")
App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fxrp5TDWEL64SiK_1_JTK"), [""])
App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK").addGeometry(Part.LineSegment(App.Vector(147.79685000000001,-175.23736000000000,0.00000000000000),App.Vector(97.79685000000001,-175.23736000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK").addGeometry(Part.LineSegment(App.Vector(97.79685000000001,-175.23736000000000,0.00000000000000),App.Vector(97.79685000000001,-225.23736000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK").addGeometry(Part.LineSegment(App.Vector(97.79685000000001,-225.23736000000000,0.00000000000000),App.Vector(147.79685000000001,-225.23736000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK").addGeometry(Part.LineSegment(App.Vector(147.79685000000001,-175.23736000000000,0.00000000000000),App.Vector(147.79685000000001,-225.23736000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Pad","Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK")
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").Profile = App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK")
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").Length = 50.0
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").Type = 4
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Plane", "plane_Sketch_Fxrp5TDWEL64SiK_1_JTG")
origin = App.Vector(-0.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fxrp5TDWEL64SiK_1_JTG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("Sketcher::SketchObject","Sketch_Fxrp5TDWEL64SiK_1_JTG")
App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fxrp5TDWEL64SiK_1_JTG"), [""])
App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG").addGeometry(Part.LineSegment(App.Vector(-225.65842999999998,-40.37715000000000,0.00000000000000),App.Vector(-200.65843000000001,2.92412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG").addGeometry(Part.LineSegment(App.Vector(-200.65843000000001,2.92412000000000,0.00000000000000),App.Vector(-243.95970000000000,27.92412000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG").addGeometry(Part.LineSegment(App.Vector(-243.95970000000000,27.92412000000000,0.00000000000000),App.Vector(-268.95970000000000,-15.37715000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG").addGeometry(Part.LineSegment(App.Vector(-225.65842999999998,-40.37715000000000,0.00000000000000),App.Vector(-268.95970000000000,-15.37715000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Pad","Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG")
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").Profile = App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG")
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").Length = 50.0
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fxrp5TDWEL64SiK_1_JTG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").Type = 4
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fxrp5TDWEL64SiK_1_FW20wrpu6LSC5ZV_1_JTG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Plane", "plane_Sketch_FNtkEt4fSTSHy6a_1_JXC")
origin = App.Vector(-0.00000000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNtkEt4fSTSHy6a_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("Sketcher::SketchObject","Sketch_FNtkEt4fSTSHy6a_1_JXC")
App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNtkEt4fSTSHy6a_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC").addGeometry(Part.LineSegment(App.Vector(310.00000000000000,290.00000000000000,0.00000000000000),App.Vector(366.56853999999998,233.43146000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC").addGeometry(Part.LineSegment(App.Vector(366.56853999999998,233.43146000000002,0.00000000000000),App.Vector(401.92388000000000,268.78679999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC").addGeometry(Part.LineSegment(App.Vector(401.92388000000000,268.78679999999997,0.00000000000000),App.Vector(345.35534000000001,325.35534000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC").addGeometry(Part.LineSegment(App.Vector(310.00000000000000,290.00000000000000,0.00000000000000),App.Vector(345.35534000000001,325.35534000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fbt18DMA3dWmtrw_0").newObject("PartDesign::Pad","Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC")
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC")
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNtkEt4fSTSHy6a_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNtkEt4fSTSHy6a_1_F2wxw8vhZLfVrxy_1_JXC").Offset = 0
App.ActiveDocument.recompute()

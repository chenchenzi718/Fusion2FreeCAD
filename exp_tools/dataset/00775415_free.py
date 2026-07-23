import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00775415")
App.ActiveDocument.addObject("PartDesign::Body","Body_FiIYkpUOmB6ARdQ_0")
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").Label = "Body_FiIYkpUOmB6ARdQ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Plane", "plane_Sketch_FiIYkpUOmB6ARdQ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiIYkpUOmB6ARdQ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("Sketcher::SketchObject","Sketch_FiIYkpUOmB6ARdQ_0_JGC")
App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiIYkpUOmB6ARdQ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(1524.00000000000000,-838.19999999999993,0.00000000000000),App.Vector(-1524.00000000000000,-838.19999999999993,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1524.00000000000000,-838.19999999999993,0.00000000000000),App.Vector(-1524.00000000000000,838.19999999999993,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(1524.00000000000000,838.19999999999993,0.00000000000000),App.Vector(-1524.00000000000000,838.19999999999993,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC").addGeometry(Part.LineSegment(App.Vector(1524.00000000000000,-838.19999999999993,0.00000000000000),App.Vector(1524.00000000000000,838.19999999999993,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Pad","Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC")
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC")
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").Length = 1676.4
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiIYkpUOmB6ARdQ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiIYkpUOmB6ARdQ_0_FE16o6Wv39QiLzW_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Plane", "plane_Sketch_FElhT64tU122wxK_1_JJG")
origin = App.Vector(0.00000000000000,-1676.39999999999986,-723.89999999999998)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FElhT64tU122wxK_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("Sketcher::SketchObject","Sketch_FElhT64tU122wxK_1_JJG")
App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FElhT64tU122wxK_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG").addGeometry(Part.LineSegment(App.Vector(1524.00000000000000,1562.10000000000014,0.00000000000000),App.Vector(1524.00000000000000,190.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG").addGeometry(Part.LineSegment(App.Vector(-1524.00000000000000,190.50000000000000,0.00000000000000),App.Vector(1524.00000000000000,190.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG").addGeometry(Part.LineSegment(App.Vector(-1524.00000000000000,1562.10000000000014,0.00000000000000),App.Vector(-1524.00000000000000,190.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG").addGeometry(Part.LineSegment(App.Vector(1524.00000000000000,1562.10000000000014,0.00000000000000),App.Vector(-1524.00000000000000,1562.10000000000014,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Pocket","Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG")
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG")
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FElhT64tU122wxK_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FElhT64tU122wxK_1_FPdlS1PcCyV3DeV_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Plane", "plane_Sketch_FR9qkEYGLebv1OH_1_JNG")
origin = App.Vector(1524.00000000000000,-838.19999999999993,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR9qkEYGLebv1OH_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("Sketcher::SketchObject","Sketch_FR9qkEYGLebv1OH_1_JNG")
App.ActiveDocument.getObject("Sketch_FR9qkEYGLebv1OH_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR9qkEYGLebv1OH_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FR9qkEYGLebv1OH_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR9qkEYGLebv1OH_1_JNG").addGeometry(Part.LineSegment(App.Vector(-838.19999999999993,-609.60000000000002,0.00000000000000),App.Vector(-533.39999999999998,-533.39999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR9qkEYGLebv1OH_1_JNG").addGeometry(Part.LineSegment(App.Vector(-838.19999999999993,-533.39999999999998,0.00000000000000),App.Vector(-533.39999999999998,-533.39999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR9qkEYGLebv1OH_1_JNG").addGeometry(Part.LineSegment(App.Vector(-838.19999999999993,-533.39999999999998,0.00000000000000),App.Vector(-838.19999999999993,-609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR9qkEYGLebv1OH_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR9qkEYGLebv1OH_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Pocket","Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG")
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FR9qkEYGLebv1OH_1_JNG")
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").Length = 3048.0000000000005
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR9qkEYGLebv1OH_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR9qkEYGLebv1OH_1_F2IeXSrBVzjRswb_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Plane", "plane_Sketch_FSff58dwlyIyR9a_1_JRG")
origin = App.Vector(1524.00000000000000,-838.19999999999993,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSff58dwlyIyR9a_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("Sketcher::SketchObject","Sketch_FSff58dwlyIyR9a_1_JRG")
App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSff58dwlyIyR9a_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG").addGeometry(Part.LineSegment(App.Vector(380.99999999999994,-838.19999999999993,0.00000000000000),App.Vector(380.99999999999994,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG").addGeometry(Part.LineSegment(App.Vector(380.99999999999994,609.60000000000002,0.00000000000000),App.Vector(838.19999999999993,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG").addGeometry(Part.LineSegment(App.Vector(838.19999999999993,-838.19999999999993,0.00000000000000),App.Vector(838.19999999999993,609.60000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG").addGeometry(Part.LineSegment(App.Vector(838.19999999999993,-838.19999999999993,0.00000000000000),App.Vector(380.99999999999994,-838.19999999999993,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Pocket","Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG")
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG")
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").Length = 3048.0000000000005
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSff58dwlyIyR9a_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSff58dwlyIyR9a_1_FcT4lL018yXq9vE_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Plane", "plane_Sketch_Fh6Sb4XosDsmJ5K_1_JVG")
origin = App.Vector(0.00000000000000,-1676.39999999999986,-723.89999999999998)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh6Sb4XosDsmJ5K_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("Sketcher::SketchObject","Sketch_Fh6Sb4XosDsmJ5K_1_JVG")
App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh6Sb4XosDsmJ5K_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG").addGeometry(Part.LineSegment(App.Vector(-381.00000000000000,-114.29999999999995,0.00000000000000),App.Vector(-381.00000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG").addGeometry(Part.LineSegment(App.Vector(-381.00000000000000,-38.10000000000002,0.00000000000000),App.Vector(381.00000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG").addGeometry(Part.LineSegment(App.Vector(381.00000000000000,-38.10000000000002,0.00000000000000),App.Vector(381.00000000000000,-114.29999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG").addGeometry(Part.LineSegment(App.Vector(-381.00000000000000,-114.29999999999995,0.00000000000000),App.Vector(381.00000000000000,-114.29999999999995,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Pocket","Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG")
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG")
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").Length = 1219.2
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh6Sb4XosDsmJ5K_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh6Sb4XosDsmJ5K_1_FJzPvtR4nqmnhem_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Plane", "plane_Sketch_FJTZKoVmuTMvg3v_1_JZG")
origin = App.Vector(1524.00000000000000,-838.19999999999993,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJTZKoVmuTMvg3v_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("Sketcher::SketchObject","Sketch_FJTZKoVmuTMvg3v_1_JZG")
App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJTZKoVmuTMvg3v_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG").addGeometry(Part.LineSegment(App.Vector(380.99999999999994,-228.59999999999999,0.00000000000000),App.Vector(304.79999999999995,-228.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG").addGeometry(Part.LineSegment(App.Vector(304.79999999999995,-228.59999999999999,0.00000000000000),App.Vector(304.79999999999995,381.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG").addGeometry(Part.LineSegment(App.Vector(304.79999999999995,381.00000000000000,0.00000000000000),App.Vector(380.99999999999994,381.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG").addGeometry(Part.LineSegment(App.Vector(380.99999999999994,-228.59999999999999,0.00000000000000),App.Vector(380.99999999999994,381.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Pocket","Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG")
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG")
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").Length = 3048.0000000000005
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJTZKoVmuTMvg3v_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJTZKoVmuTMvg3v_1_FhksLGzchZY2edw_1_JZG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Plane", "plane_Sketch_FSr77D1mxODh3Ix_1_JdG")
origin = App.Vector(0.00000000000000,-762.00000000000000,152.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSr77D1mxODh3Ix_1_JdG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("Sketcher::SketchObject","Sketch_FSr77D1mxODh3Ix_1_JdG")
App.ActiveDocument.getObject("Sketch_FSr77D1mxODh3Ix_1_JdG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSr77D1mxODh3Ix_1_JdG"), [""])
App.ActiveDocument.getObject("Sketch_FSr77D1mxODh3Ix_1_JdG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSr77D1mxODh3Ix_1_JdG").addGeometry(Part.Circle(App.Vector(-762.00000000000000,-76.20000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),177.80000000000001),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSr77D1mxODh3Ix_1_JdG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSr77D1mxODh3Ix_1_JdG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Pocket","Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG")
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").Profile = App.ActiveDocument.getObject("Sketch_FSr77D1mxODh3Ix_1_JdG")
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").Length = 304.8
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSr77D1mxODh3Ix_1_JdG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").Type = 4
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSr77D1mxODh3Ix_1_FFbL06AgEkH4NYU_1_JdG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Plane", "plane_Sketch_FRQNZvd7rKWk8CX_1_JhC")
origin = App.Vector(0.00000000000000,-762.00000000000000,152.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRQNZvd7rKWk8CX_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("Sketcher::SketchObject","Sketch_FRQNZvd7rKWk8CX_1_JhC")
App.ActiveDocument.getObject("Sketch_FRQNZvd7rKWk8CX_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRQNZvd7rKWk8CX_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_FRQNZvd7rKWk8CX_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRQNZvd7rKWk8CX_1_JhC").addGeometry(Part.Circle(App.Vector(762.00000000000000,-76.20000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),177.80000000000001),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRQNZvd7rKWk8CX_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRQNZvd7rKWk8CX_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiIYkpUOmB6ARdQ_0").newObject("PartDesign::Pocket","Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC")
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_FRQNZvd7rKWk8CX_1_JhC")
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").Length = 304.8
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRQNZvd7rKWk8CX_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRQNZvd7rKWk8CX_1_FoIgWIhqtLjsfkw_1_JhC").Offset = 0
App.ActiveDocument.recompute()

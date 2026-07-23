import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00202007")
App.ActiveDocument.addObject("PartDesign::Body","Body_FSZBBYNCFnVhvBk_0")
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").Label = "Body_FSZBBYNCFnVhvBk_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Plane", "plane_Sketch_FSZBBYNCFnVhvBk_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSZBBYNCFnVhvBk_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("Sketcher::SketchObject","Sketch_FSZBBYNCFnVhvBk_0_JGC")
App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSZBBYNCFnVhvBk_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC").addGeometry(Part.LineSegment(App.Vector(4.00050000000000,3.17500000000000,0.00000000000000),App.Vector(4.00050000000000,-3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.43656000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.38956000000000),3.87593997691801,5.54883798385137),False)

App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-4.00050000000000,3.17500000000000,0.00000000000000),App.Vector(-4.00050000000000,-3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,-0.43656000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.38956000000000),0.73434732332822,2.40724533026158),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Pad","Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC")
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC")
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").Length = 14.986
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSZBBYNCFnVhvBk_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSZBBYNCFnVhvBk_0_F4SWHKcXBo1j2ad_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Plane", "plane_Sketch_Fzt5XDFEEKTVSxC_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fzt5XDFEEKTVSxC_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("Sketcher::SketchObject","Sketch_Fzt5XDFEEKTVSxC_1_JJC")
App.ActiveDocument.getObject("Sketch_Fzt5XDFEEKTVSxC_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fzt5XDFEEKTVSxC_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fzt5XDFEEKTVSxC_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fzt5XDFEEKTVSxC_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50800000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fzt5XDFEEKTVSxC_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fzt5XDFEEKTVSxC_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Pad","Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC")
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fzt5XDFEEKTVSxC_1_JJC")
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").Length = 8.382000000000001
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fzt5XDFEEKTVSxC_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fzt5XDFEEKTVSxC_1_FRG0vyBO4z4PNUF_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Plane", "plane_Sketch_FwS87FEihg9aH1Z_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwS87FEihg9aH1Z_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("Sketcher::SketchObject","Sketch_FwS87FEihg9aH1Z_1_JNC")
App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwS87FEihg9aH1Z_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,3.49250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.63500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Pocket","Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC")
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNC")
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Plane", "plane_Sketch_FwS87FEihg9aH1Z_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwS87FEihg9aH1Z_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("Sketcher::SketchObject","Sketch_FwS87FEihg9aH1Z_1_JNG")
App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwS87FEihg9aH1Z_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNG").addGeometry(Part.Circle(App.Vector(0.00000000000000,-3.49250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.63500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Pocket","Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG")
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNG")
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwS87FEihg9aH1Z_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwS87FEihg9aH1Z_1_FyaBQNJVoe12i7i_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Plane", "plane_Sketch_FTNU4DykV5rdmub_1_JRO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTNU4DykV5rdmub_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("Sketcher::SketchObject","Sketch_FTNU4DykV5rdmub_1_JRO")
App.ActiveDocument.getObject("Sketch_FTNU4DykV5rdmub_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTNU4DykV5rdmub_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FTNU4DykV5rdmub_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTNU4DykV5rdmub_1_JRO").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.96850000000000),False)

App.ActiveDocument.getObject("Sketch_FTNU4DykV5rdmub_1_JRO").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50800000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTNU4DykV5rdmub_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTNU4DykV5rdmub_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Pad","Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO")
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FTNU4DykV5rdmub_1_JRO")
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTNU4DykV5rdmub_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTNU4DykV5rdmub_1_FR40qY1TfKTOfzt_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Plane", "plane_Sketch_F3E8l3xQIb2mVVR_1_JVC")
origin = App.Vector(0.00000000000000,14.98600000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3E8l3xQIb2mVVR_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("Sketcher::SketchObject","Sketch_F3E8l3xQIb2mVVR_1_JVC")
App.ActiveDocument.getObject("Sketch_F3E8l3xQIb2mVVR_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3E8l3xQIb2mVVR_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F3E8l3xQIb2mVVR_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3E8l3xQIb2mVVR_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.90500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3E8l3xQIb2mVVR_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3E8l3xQIb2mVVR_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Pad","Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC")
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F3E8l3xQIb2mVVR_1_JVC")
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").Length = 1.1430000000000002
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3E8l3xQIb2mVVR_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3E8l3xQIb2mVVR_1_FDAchN4Okqi7qBX_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Plane", "plane_Sketch_FluEpa1P175LKAS_1_JZC")
origin = App.Vector(0.00000000000000,14.98600000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FluEpa1P175LKAS_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("Sketcher::SketchObject","Sketch_FluEpa1P175LKAS_1_JZC")
App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FluEpa1P175LKAS_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC").addGeometry(Part.LineSegment(App.Vector(-2.13069000000000,-3.12454000000000,0.00000000000000),App.Vector(-0.85100000000000,-3.68489000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC").addGeometry(Part.LineSegment(App.Vector(-0.85100000000000,-3.68489000000000,0.00000000000000),App.Vector(-0.74911000000000,-3.45222000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC").addGeometry(Part.LineSegment(App.Vector(-2.02881000000000,-2.89187000000000,0.00000000000000),App.Vector(-0.74911000000000,-3.45222000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC").addGeometry(Part.LineSegment(App.Vector(-2.13069000000000,-3.12454000000000,0.00000000000000),App.Vector(-2.02881000000000,-2.89187000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Pad","Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC")
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC")
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").Length = 1.5240000000000002
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Plane", "plane_Sketch_FluEpa1P175LKAS_1_JZG")
origin = App.Vector(0.00000000000000,14.98600000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FluEpa1P175LKAS_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("Sketcher::SketchObject","Sketch_FluEpa1P175LKAS_1_JZG")
App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FluEpa1P175LKAS_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG").addGeometry(Part.LineSegment(App.Vector(0.74911000000000,3.45222000000000,0.00000000000000),App.Vector(0.85100000000000,3.68489000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG").addGeometry(Part.LineSegment(App.Vector(0.85100000000000,3.68489000000000,0.00000000000000),App.Vector(2.13069000000000,3.12454000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG").addGeometry(Part.LineSegment(App.Vector(2.02881000000000,2.89187000000000,0.00000000000000),App.Vector(2.13069000000000,3.12454000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG").addGeometry(Part.LineSegment(App.Vector(0.74911000000000,3.45222000000000,0.00000000000000),App.Vector(2.02881000000000,2.89187000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FSZBBYNCFnVhvBk_0").newObject("PartDesign::Pad","Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG")
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG")
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").Length = 1.5240000000000002
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FluEpa1P175LKAS_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FluEpa1P175LKAS_1_FpIZN7Sdhi0c0KK_1_JZG").Offset = 0
App.ActiveDocument.recompute()

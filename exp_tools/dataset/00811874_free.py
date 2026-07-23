import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00811874")
App.ActiveDocument.addObject("PartDesign::Body","Body_F38P1NgxNxC8ssm_0")
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").Label = "Body_F38P1NgxNxC8ssm_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Plane", "plane_Sketch_F38P1NgxNxC8ssm_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F38P1NgxNxC8ssm_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("Sketcher::SketchObject","Sketch_F38P1NgxNxC8ssm_0_JGC")
App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F38P1NgxNxC8ssm_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(7.62000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC").addGeometry(Part.LineSegment(App.Vector(7.62000000000000,0.00000000000000,0.00000000000000),App.Vector(1.52400000000000,-10.16000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000),App.Vector(1.52400000000000,-10.16000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Pad","Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC")
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC")
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Plane", "plane_Sketch_F38P1NgxNxC8ssm_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F38P1NgxNxC8ssm_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("Sketcher::SketchObject","Sketch_F38P1NgxNxC8ssm_0_JGG")
App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F38P1NgxNxC8ssm_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-7.62000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG").addGeometry(Part.LineSegment(App.Vector(-7.62000000000000,0.00000000000000,0.00000000000000),App.Vector(-1.52400000000000,-10.16000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000),App.Vector(-1.52400000000000,-10.16000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-10.16000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Pad","Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG")
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG")
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F38P1NgxNxC8ssm_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F38P1NgxNxC8ssm_0_FQqeDDRNeyhnh9B_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Plane", "plane_Sketch_FsixjdvxifeEeZK_0_JKC")
origin = App.Vector(3.83286000000000,-5.08000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsixjdvxifeEeZK_0_JKC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("Sketcher::SketchObject","Sketch_FsixjdvxifeEeZK_0_JKC")
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsixjdvxifeEeZK_0_JKC"), [""])
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-2.54000000000000,0.00000000000000),App.Vector(-4.84886000000000,-2.54000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC").addGeometry(Part.LineSegment(App.Vector(-4.84886000000000,-2.54000000000000,0.00000000000000),App.Vector(-4.08686000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,0.00000000000000,0.00000000000000),App.Vector(-4.08686000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-2.54000000000000,0.00000000000000),App.Vector(-3.83286000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Pocket","Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC")
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").Profile = App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC")
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").Type = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Plane", "plane_Sketch_FsixjdvxifeEeZK_0_JKG")
origin = App.Vector(3.83286000000000,-5.08000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsixjdvxifeEeZK_0_JKG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("Sketcher::SketchObject","Sketch_FsixjdvxifeEeZK_0_JKG")
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsixjdvxifeEeZK_0_JKG"), [""])
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-2.54000000000000,0.00000000000000),App.Vector(-2.81686000000000,-2.54000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG").addGeometry(Part.LineSegment(App.Vector(-2.81686000000000,-2.54000000000000,0.00000000000000),App.Vector(-3.57886000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,0.00000000000000,0.00000000000000),App.Vector(-3.57886000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-2.54000000000000,0.00000000000000),App.Vector(-3.83286000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Pocket","Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG")
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").Profile = App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG")
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").Type = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Plane", "plane_Sketch_FsixjdvxifeEeZK_0_JKK")
origin = App.Vector(3.83286000000000,-5.08000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsixjdvxifeEeZK_0_JKK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("Sketcher::SketchObject","Sketch_FsixjdvxifeEeZK_0_JKK")
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsixjdvxifeEeZK_0_JKK"), [""])
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-2.54000000000000,0.00000000000000),App.Vector(-4.84886000000000,-2.54000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").addGeometry(Part.LineSegment(App.Vector(-4.84886000000000,-2.54000000000000,0.00000000000000),App.Vector(-5.91152000000000,-6.08220000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").addGeometry(Part.LineSegment(App.Vector(-1.75420000000000,-6.08220000000000,0.00000000000000),App.Vector(-5.91152000000000,-6.08220000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").addGeometry(Part.LineSegment(App.Vector(-1.75420000000000,-6.08220000000000,0.00000000000000),App.Vector(-2.13953000000000,-4.79778000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").addGeometry(Part.LineSegment(App.Vector(-2.30886000000000,-5.08000000000000,0.00000000000000),App.Vector(-2.13953000000000,-4.79778000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-5.08000000000000,0.00000000000000),App.Vector(-2.30886000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-5.08000000000000,0.00000000000000),App.Vector(-3.83286000000000,-2.54000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Pocket","Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK")
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").Profile = App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK")
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").Type = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Plane", "plane_Sketch_FsixjdvxifeEeZK_0_JKS")
origin = App.Vector(3.83286000000000,-5.08000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FsixjdvxifeEeZK_0_JKS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("Sketcher::SketchObject","Sketch_FsixjdvxifeEeZK_0_JKS")
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FsixjdvxifeEeZK_0_JKS"), [""])
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-2.54000000000000,0.00000000000000),App.Vector(-2.81686000000000,-2.54000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS").addGeometry(Part.LineSegment(App.Vector(-2.81686000000000,-2.54000000000000,0.00000000000000),App.Vector(-2.13953000000000,-4.79778000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS").addGeometry(Part.LineSegment(App.Vector(-2.30886000000000,-5.08000000000000,0.00000000000000),App.Vector(-2.13953000000000,-4.79778000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-5.08000000000000,0.00000000000000),App.Vector(-2.30886000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,-5.08000000000000,0.00000000000000),App.Vector(-3.83286000000000,-2.54000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Pocket","Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS")
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").Profile = App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS")
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FsixjdvxifeEeZK_0_JKS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").Type = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").Reversed = 1
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FsixjdvxifeEeZK_0_FzlqqpnJTwhviqK_0_JKS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Plane", "plane_Sketch_FCDTixAlu72CJpZ_0_JIC")
origin = App.Vector(3.83286000000000,-5.08000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCDTixAlu72CJpZ_0_JIC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("Sketcher::SketchObject","Sketch_FCDTixAlu72CJpZ_0_JIC")
App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCDTixAlu72CJpZ_0_JIC"), [""])
App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-3.83286000000000,0.62346000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIC").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,3.79846000000000,0.00000000000000),App.Vector(-3.83286000000000,-2.55154000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Pocket","Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC")
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").Profile = App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIC")
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").Type = 0
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Plane", "plane_Sketch_FCDTixAlu72CJpZ_0_JIG")
origin = App.Vector(3.83286000000000,-5.08000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCDTixAlu72CJpZ_0_JIG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("Sketcher::SketchObject","Sketch_FCDTixAlu72CJpZ_0_JIG")
App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCDTixAlu72CJpZ_0_JIG"), [""])
App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-3.83286000000000,0.62346000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIG").addGeometry(Part.LineSegment(App.Vector(-3.83286000000000,3.79846000000000,0.00000000000000),App.Vector(-3.83286000000000,-2.55154000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F38P1NgxNxC8ssm_0").newObject("PartDesign::Pocket","Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG")
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").Profile = App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIG")
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCDTixAlu72CJpZ_0_JIG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").Type = 0
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCDTixAlu72CJpZ_0_F9vjH4uw5BAxSy4_0_JIG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00145942")
App.ActiveDocument.addObject("PartDesign::Body","Body_FmxBeGXe5ov6gXD_0")
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").Label = "Body_FmxBeGXe5ov6gXD_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Plane", "plane_Sketch_FmxBeGXe5ov6gXD_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("Sketcher::SketchObject","Sketch_FmxBeGXe5ov6gXD_0_JGO")
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,35.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,5.00000000000000,0.00000000000000),App.Vector(12.50000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,35.00000000000000,0.00000000000000),App.Vector(12.50000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,35.00000000000000,0.00000000000000),App.Vector(-25.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Pad","Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").Profile = App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").Length = 40.0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Plane", "plane_Sketch_FmxBeGXe5ov6gXD_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("Sketcher::SketchObject","Sketch_FmxBeGXe5ov6gXD_0_JGC")
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,35.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-75.00000000000000,35.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,35.00000000000000,0.00000000000000),App.Vector(-75.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Pad","Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGC")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").Length = 40.0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_Fo4jeRERiVqY8zk_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Plane", "plane_Sketch_FmxBeGXe5ov6gXD_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("Sketcher::SketchObject","Sketch_FmxBeGXe5ov6gXD_0_JGS")
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,35.00000000000000,0.00000000000000),App.Vector(25.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,35.00000000000000,0.00000000000000),App.Vector(25.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(12.50000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,35.00000000000000,0.00000000000000),App.Vector(12.50000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Pad","Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").Profile = App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").Length = 55.0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FoHVuG8qLf3ddLi_1_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Plane", "plane_Sketch_FmxBeGXe5ov6gXD_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("Sketcher::SketchObject","Sketch_FmxBeGXe5ov6gXD_0_JGG")
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,35.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,35.00000000000000,0.00000000000000),App.Vector(25.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,35.00000000000000,0.00000000000000),App.Vector(25.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Pad","Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").Profile = App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").Length = 80.0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FTZdelRjpUzWgUg_1_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Plane", "plane_Sketch_FmxBeGXe5ov6gXD_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("Sketcher::SketchObject","Sketch_FmxBeGXe5ov6gXD_0_JGK")
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmxBeGXe5ov6gXD_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").addGeometry(Part.LineSegment(App.Vector(60.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(60.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").addGeometry(Part.LineSegment(App.Vector(25.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(12.50000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,5.00000000000000,0.00000000000000),App.Vector(12.50000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").addGeometry(Part.LineSegment(App.Vector(-25.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").addGeometry(Part.LineSegment(App.Vector(-60.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(-60.00000000000000,26.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Pad","Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").Profile = App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK")
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").Length = 20.0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmxBeGXe5ov6gXD_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmxBeGXe5ov6gXD_0_FZQRXWH1zWNbi9t_1_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Plane", "plane_Sketch_FORtQ1g3i5EnkO1_1_JPC")
origin = App.Vector(60.00000000000000,-40.00000000000000,-0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FORtQ1g3i5EnkO1_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("Sketcher::SketchObject","Sketch_FORtQ1g3i5EnkO1_1_JPC")
App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FORtQ1g3i5EnkO1_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(40.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(40.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Pad","Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC")
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC")
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").Length = 35.0
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").Type = 0
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Plane", "plane_Sketch_FORtQ1g3i5EnkO1_1_JPG")
origin = App.Vector(60.00000000000000,-40.00000000000000,-0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FORtQ1g3i5EnkO1_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("Sketcher::SketchObject","Sketch_FORtQ1g3i5EnkO1_1_JPG")
App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FORtQ1g3i5EnkO1_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG").addGeometry(Part.LineSegment(App.Vector(-40.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG").addGeometry(Part.LineSegment(App.Vector(-40.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Pad","Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG")
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG")
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").Length = 35.0
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FORtQ1g3i5EnkO1_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").Type = 0
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FORtQ1g3i5EnkO1_1_FKPaHcksqwBVJM1_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Plane", "plane_Sketch_FzkVoYRtCIUrZr0_1_JVC")
origin = App.Vector(0.00000000000000,-17.50000000000000,-35.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzkVoYRtCIUrZr0_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("Sketcher::SketchObject","Sketch_FzkVoYRtCIUrZr0_1_JVC")
App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzkVoYRtCIUrZr0_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,57.49999999999999,0.00000000000000),App.Vector(50.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,17.50000000000000,0.00000000000000),App.Vector(35.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,57.49999999999999,0.00000000000000),App.Vector(35.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,57.49999999999999,0.00000000000000),App.Vector(35.00000000000000,57.49999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Pocket","Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC")
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC")
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Plane", "plane_Sketch_FzkVoYRtCIUrZr0_1_JVG")
origin = App.Vector(0.00000000000000,-17.50000000000000,-35.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzkVoYRtCIUrZr0_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("Sketcher::SketchObject","Sketch_FzkVoYRtCIUrZr0_1_JVG")
App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzkVoYRtCIUrZr0_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(50.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,17.50000000000000,0.00000000000000),App.Vector(35.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(35.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,-12.50000000000000,0.00000000000000),App.Vector(35.00000000000000,-12.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmxBeGXe5ov6gXD_0").newObject("PartDesign::Pocket","Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG")
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG")
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzkVoYRtCIUrZr0_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzkVoYRtCIUrZr0_1_F4YhDV5iMTm8YCT_1_JVG").Offset = 0
App.ActiveDocument.recompute()

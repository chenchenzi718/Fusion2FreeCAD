import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00704877")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fh9tr3PsTtlUyHU_0")
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").Label = "Body_Fh9tr3PsTtlUyHU_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Plane", "plane_Sketch_Fh9tr3PsTtlUyHU_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh9tr3PsTtlUyHU_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("Sketcher::SketchObject","Sketch_Fh9tr3PsTtlUyHU_0_JGC")
App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh9tr3PsTtlUyHU_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-2400.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-2400.00000000000000,100.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),100.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-2500.00000000000000,100.00000000000000,0.00000000000000),App.Vector(-2500.00000000000000,550.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-2400.00000000000000,550.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),100.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-2400.00000000000000,650.00000000000000,0.00000000000000),App.Vector(-650.00000000000000,650.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-650.00000000000000,650.00000000000000,0.00000000000000),App.Vector(-650.00000000000000,1250.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-550.00000000000000,1250.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),100.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-550.00000000000000,1350.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1350.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1350.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Pad","Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC")
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC")
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").Length = 850.0
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh9tr3PsTtlUyHU_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh9tr3PsTtlUyHU_0_FDXiZ7tErJ2jgWN_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Plane", "plane_Sketch_FUGTQGOKhmmKw0G_1_JJK")
origin = App.Vector(-1525.00000000000000,650.00000000000000,425.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("Sketcher::SketchObject","Sketch_FUGTQGOKhmmKw0G_1_JJK")
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK").addGeometry(Part.LineSegment(App.Vector(-274.99999999999989,375.00000000000006,0.00000000000000),App.Vector(-825.00000000000000,375.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,375.00000000000006,0.00000000000000),App.Vector(-825.00000000000000,225.00000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK").addGeometry(Part.LineSegment(App.Vector(-274.99999999999989,225.00000000000003,0.00000000000000),App.Vector(-825.00000000000000,225.00000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK").addGeometry(Part.LineSegment(App.Vector(-274.99999999999989,375.00000000000006,0.00000000000000),App.Vector(-274.99999999999989,225.00000000000003,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Pocket","Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").Length = 600.0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Plane", "plane_Sketch_FUGTQGOKhmmKw0G_1_JJO")
origin = App.Vector(-1525.00000000000000,650.00000000000000,425.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("Sketcher::SketchObject","Sketch_FUGTQGOKhmmKw0G_1_JJO")
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,175.00000000000000,0.00000000000000),App.Vector(-274.99999999999989,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO").addGeometry(Part.LineSegment(App.Vector(-274.99999999999989,175.00000000000000,0.00000000000000),App.Vector(-274.99999999999989,25.00000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,25.00000000000002,0.00000000000000),App.Vector(-274.99999999999989,25.00000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,175.00000000000000,0.00000000000000),App.Vector(-825.00000000000000,25.00000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Pocket","Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").Length = 600.0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Plane", "plane_Sketch_FUGTQGOKhmmKw0G_1_JJS")
origin = App.Vector(-1525.00000000000000,650.00000000000000,425.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("Sketcher::SketchObject","Sketch_FUGTQGOKhmmKw0G_1_JJS")
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,-24.99999999999997,0.00000000000000),App.Vector(-274.99999999999989,-24.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS").addGeometry(Part.LineSegment(App.Vector(-274.99999999999989,-24.99999999999997,0.00000000000000),App.Vector(-274.99999999999989,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,-175.00000000000000,0.00000000000000),App.Vector(-274.99999999999989,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,-24.99999999999997,0.00000000000000),App.Vector(-825.00000000000000,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Pocket","Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").Length = 600.0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Plane", "plane_Sketch_FUGTQGOKhmmKw0G_1_JJW")
origin = App.Vector(-1525.00000000000000,650.00000000000000,425.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("Sketcher::SketchObject","Sketch_FUGTQGOKhmmKw0G_1_JJW")
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,-224.99999999999997,0.00000000000000),App.Vector(-274.99999999999989,-224.99999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW").addGeometry(Part.LineSegment(App.Vector(-274.99999999999989,-224.99999999999997,0.00000000000000),App.Vector(-274.99999999999989,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,-375.00000000000000,0.00000000000000),App.Vector(-274.99999999999989,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW").addGeometry(Part.LineSegment(App.Vector(-825.00000000000000,-224.99999999999997,0.00000000000000),App.Vector(-825.00000000000000,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Pocket","Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").Length = 600.0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_F0mzLZmBXl4XBr1_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Plane", "plane_Sketch_FUGTQGOKhmmKw0G_1_JJC")
origin = App.Vector(-1525.00000000000000,650.00000000000000,425.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("Sketcher::SketchObject","Sketch_FUGTQGOKhmmKw0G_1_JJC")
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC").addGeometry(Part.LineSegment(App.Vector(-224.99999999999986,375.00000000000006,0.00000000000000),App.Vector(275.00000000000011,375.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC").addGeometry(Part.LineSegment(App.Vector(275.00000000000011,375.00000000000006,0.00000000000000),App.Vector(275.00000000000011,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC").addGeometry(Part.LineSegment(App.Vector(-224.99999999999986,-375.00000000000000,0.00000000000000),App.Vector(275.00000000000011,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC").addGeometry(Part.LineSegment(App.Vector(-224.99999999999986,375.00000000000006,0.00000000000000),App.Vector(-224.99999999999986,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Pad","Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Plane", "plane_Sketch_FUGTQGOKhmmKw0G_1_JJG")
origin = App.Vector(-1525.00000000000000,650.00000000000000,425.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("Sketcher::SketchObject","Sketch_FUGTQGOKhmmKw0G_1_JJG")
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUGTQGOKhmmKw0G_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG").addGeometry(Part.LineSegment(App.Vector(325.00000000000017,375.00000000000006,0.00000000000000),App.Vector(825.00000000000023,375.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG").addGeometry(Part.LineSegment(App.Vector(825.00000000000023,375.00000000000006,0.00000000000000),App.Vector(825.00000000000023,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG").addGeometry(Part.LineSegment(App.Vector(325.00000000000017,-375.00000000000000,0.00000000000000),App.Vector(825.00000000000023,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG").addGeometry(Part.LineSegment(App.Vector(325.00000000000017,375.00000000000006,0.00000000000000),App.Vector(325.00000000000017,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Pad","Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG")
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").Length = 10.0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUGTQGOKhmmKw0G_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUGTQGOKhmmKw0G_1_FQgE0XVKQsNDqR4_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Plane", "plane_Sketch_FLDTQZGI3ZWRSxf_1_JMC")
origin = App.Vector(-650.00000000000000,950.00000000000000,425.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLDTQZGI3ZWRSxf_1_JMC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("Sketcher::SketchObject","Sketch_FLDTQZGI3ZWRSxf_1_JMC")
App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLDTQZGI3ZWRSxf_1_JMC"), [""])
App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC").addGeometry(Part.LineSegment(App.Vector(-250.00000000000000,375.00000000000006,0.00000000000000),App.Vector(250.00000000000000,375.00000000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC").addGeometry(Part.LineSegment(App.Vector(250.00000000000000,375.00000000000006,0.00000000000000),App.Vector(250.00000000000000,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC").addGeometry(Part.LineSegment(App.Vector(-250.00000000000000,-375.00000000000000,0.00000000000000),App.Vector(250.00000000000000,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC").addGeometry(Part.LineSegment(App.Vector(-250.00000000000000,375.00000000000006,0.00000000000000),App.Vector(-250.00000000000000,-375.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh9tr3PsTtlUyHU_0").newObject("PartDesign::Pad","Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC")
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").Profile = App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC")
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLDTQZGI3ZWRSxf_1_JMC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").Type = 4
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLDTQZGI3ZWRSxf_1_FMuVad6QrWN5idB_1_JMC").Offset = 0
App.ActiveDocument.recompute()

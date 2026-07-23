import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00743061")
App.ActiveDocument.addObject("PartDesign::Body","Body_F3rNnDVg98zemLh_0")
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").Label = "Body_F3rNnDVg98zemLh_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Plane", "plane_Sketch_F3rNnDVg98zemLh_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3rNnDVg98zemLh_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("Sketcher::SketchObject","Sketch_F3rNnDVg98zemLh_0_JGS")
App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3rNnDVg98zemLh_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").addGeometry(Part.LineSegment(App.Vector(-69.97559000000001,27.13442000000000,0.00000000000000),App.Vector(31.62441000000000,27.13442000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").addGeometry(Part.LineSegment(App.Vector(31.62441000000000,27.13442000000000,0.00000000000000),App.Vector(31.62441000000000,-23.66558000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").addGeometry(Part.LineSegment(App.Vector(-69.97559000000001,-23.66558000000000,0.00000000000000),App.Vector(31.62441000000000,-23.66558000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").addGeometry(Part.LineSegment(App.Vector(-69.97559000000001,27.13442000000000,0.00000000000000),App.Vector(-69.97559000000001,-23.66558000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").addGeometry(Part.Circle(App.Vector(-66.80059000000001,23.55942000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.65000000000000),False)

App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").addGeometry(Part.Circle(App.Vector(-66.80059000000001,-20.89058000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.65000000000000),False)

App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").addGeometry(Part.Circle(App.Vector(28.44941000000000,-20.89058000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.65000000000000),False)

App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").addGeometry(Part.Circle(App.Vector(28.44941000000000,23.55942000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.65000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Pad","Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS")
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").Profile = App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS")
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").Length = 1.6
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3rNnDVg98zemLh_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3rNnDVg98zemLh_0_FBW9Ag3mGNcAqvY_0_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Plane", "plane_Sketch_FuDKHXn8FdSyqoG_1_JJC")
origin = App.Vector(-19.17559000000000,1.73442000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("Sketcher::SketchObject","Sketch_FuDKHXn8FdSyqoG_1_JJC")
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC").addGeometry(Part.LineSegment(App.Vector(-38.63621000000001,20.03607000000000,0.00000000000000),App.Vector(-23.13447000000000,20.03607000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC").addGeometry(Part.LineSegment(App.Vector(-23.13447000000000,20.03607000000000,0.00000000000000),App.Vector(-23.13447000000000,7.41838000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC").addGeometry(Part.LineSegment(App.Vector(-38.63621000000001,7.41838000000000,0.00000000000000),App.Vector(-23.13447000000000,7.41838000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC").addGeometry(Part.LineSegment(App.Vector(-38.63621000000001,20.03607000000000,0.00000000000000),App.Vector(-38.63621000000001,7.41838000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Pad","Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").Length = 27.0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Plane", "plane_Sketch_FuDKHXn8FdSyqoG_1_JJG")
origin = App.Vector(-19.17559000000000,1.73442000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("Sketcher::SketchObject","Sketch_FuDKHXn8FdSyqoG_1_JJG")
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG").addGeometry(Part.LineSegment(App.Vector(-17.99726000000000,20.12620000000000,0.00000000000000),App.Vector(15.89025000000000,20.12620000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG").addGeometry(Part.LineSegment(App.Vector(15.89025000000000,20.12620000000000,0.00000000000000),App.Vector(15.89025000000000,4.71459000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG").addGeometry(Part.LineSegment(App.Vector(-17.99726000000000,4.71459000000000,0.00000000000000),App.Vector(15.89025000000000,4.71459000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG").addGeometry(Part.LineSegment(App.Vector(-17.99726000000000,20.12620000000000,0.00000000000000),App.Vector(-17.99726000000000,4.71459000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Pad","Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").Length = 27.0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Plane", "plane_Sketch_FuDKHXn8FdSyqoG_1_JJK")
origin = App.Vector(-19.17559000000000,1.73442000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("Sketcher::SketchObject","Sketch_FuDKHXn8FdSyqoG_1_JJK")
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK").addGeometry(Part.LineSegment(App.Vector(-29.62357000000000,-0.33249000000000,0.00000000000000),App.Vector(11.38393000000000,-0.33249000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK").addGeometry(Part.LineSegment(App.Vector(11.38393000000000,-0.33249000000000,0.00000000000000),App.Vector(11.38393000000000,-23.58509000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK").addGeometry(Part.LineSegment(App.Vector(-29.62357000000000,-23.58509000000000,0.00000000000000),App.Vector(11.38393000000000,-23.58509000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK").addGeometry(Part.LineSegment(App.Vector(-29.62357000000000,-0.33249000000000,0.00000000000000),App.Vector(-29.62357000000000,-23.58509000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Pad","Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").Length = 27.0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Plane", "plane_Sketch_FuDKHXn8FdSyqoG_1_JJO")
origin = App.Vector(-19.17559000000000,1.73442000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("Sketcher::SketchObject","Sketch_FuDKHXn8FdSyqoG_1_JJO")
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO").addGeometry(Part.LineSegment(App.Vector(13.45684000000000,3.00219000000000,0.00000000000000),App.Vector(30.31047000000000,3.00219000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO").addGeometry(Part.LineSegment(App.Vector(30.31047000000000,3.00219000000000,0.00000000000000),App.Vector(30.31047000000000,-19.43928000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO").addGeometry(Part.LineSegment(App.Vector(13.45684000000000,-19.43928000000000,0.00000000000000),App.Vector(30.31047000000000,-19.43928000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO").addGeometry(Part.LineSegment(App.Vector(13.45684000000000,3.00219000000000,0.00000000000000),App.Vector(13.45684000000000,-19.43928000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Pad","Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").Length = 27.0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Plane", "plane_Sketch_FuDKHXn8FdSyqoG_1_JJS")
origin = App.Vector(-19.17559000000000,1.73442000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("Sketcher::SketchObject","Sketch_FuDKHXn8FdSyqoG_1_JJS")
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJS").addGeometry(Part.Circle(App.Vector(34.63654000000000,15.98039000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.08761000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Pad","Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJS")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").Length = 27.0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Plane", "plane_Sketch_FuDKHXn8FdSyqoG_1_JJW")
origin = App.Vector(-19.17559000000000,1.73442000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("Sketcher::SketchObject","Sketch_FuDKHXn8FdSyqoG_1_JJW")
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJW").addGeometry(Part.Circle(App.Vector(33.55502000000000,5.88623000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.08016000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Pad","Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJW")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").Length = 27.0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Plane", "plane_Sketch_FuDKHXn8FdSyqoG_1_JJa")
origin = App.Vector(-19.17559000000000,1.73442000000000,1.60000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("Sketcher::SketchObject","Sketch_FuDKHXn8FdSyqoG_1_JJa")
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuDKHXn8FdSyqoG_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJa").addGeometry(Part.Circle(App.Vector(34.45629000000000,-5.01906000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.84577000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3rNnDVg98zemLh_0").newObject("PartDesign::Pad","Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJa")
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").Length = 27.0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuDKHXn8FdSyqoG_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuDKHXn8FdSyqoG_1_FsRJFgoNDfzwByw_1_JJa").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00701544")
App.ActiveDocument.addObject("PartDesign::Body","Body_Ftxl21aTz3w302s_0")
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").Label = "Body_Ftxl21aTz3w302s_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Plane", "plane_Sketch_Ftxl21aTz3w302s_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftxl21aTz3w302s_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("Sketcher::SketchObject","Sketch_Ftxl21aTz3w302s_0_JGC")
App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftxl21aTz3w302s_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.00000000000000,90.00000000000000,0.00000000000000),App.Vector(-0.50000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.50000000000000,90.00000000000000,0.00000000000000),App.Vector(-0.50000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,90.00000000000000,0.00000000000000),App.Vector(0.50000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,0.00000000000000,0.00000000000000),App.Vector(45.00000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Pad","Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC")
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC")
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").Length = 410.00000000000006
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").Length2 = 410.00000000000006
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Plane", "plane_Sketch_Ftxl21aTz3w302s_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftxl21aTz3w302s_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("Sketcher::SketchObject","Sketch_Ftxl21aTz3w302s_0_JGK")
App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftxl21aTz3w302s_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.50000000000000,90.00000000000000,0.00000000000000),App.Vector(-0.50000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK").addGeometry(Part.LineSegment(App.Vector(-0.50000000000000,90.00000000000000,0.00000000000000),App.Vector(-0.50000000000000,2070.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.50000000000000,2070.00000000000000,0.00000000000000),App.Vector(-0.50000000000000,2070.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.50000000000000,90.00000000000000,0.00000000000000),App.Vector(0.50000000000000,2070.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Pad","Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK")
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK")
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").Length = 410.00000000000006
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").Length2 = 410.00000000000006
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Plane", "plane_Sketch_Ftxl21aTz3w302s_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftxl21aTz3w302s_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("Sketcher::SketchObject","Sketch_Ftxl21aTz3w302s_0_JGG")
App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftxl21aTz3w302s_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").addGeometry(Part.LineSegment(App.Vector(-0.50000000000000,2070.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,2070.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,2070.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,2090.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,2090.00000000000000,0.00000000000000),App.Vector(10.00000000000000,2090.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,2070.00000000000000,0.00000000000000),App.Vector(10.00000000000000,2090.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.50000000000000,2070.00000000000000,0.00000000000000),App.Vector(10.00000000000000,2070.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.50000000000000,2070.00000000000000,0.00000000000000),App.Vector(-0.50000000000000,2070.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Pad","Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG")
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG")
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").Length = 410.00000000000006
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").Length2 = 410.00000000000006
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftxl21aTz3w302s_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftxl21aTz3w302s_0_FMmmWkxTKLk7IBX_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Plane", "plane_Sketch_FWVtHavTvqhgMwe_1_JJC")
origin = App.Vector(-340.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("Sketcher::SketchObject","Sketch_FWVtHavTvqhgMwe_1_JJC")
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC").addGeometry(Part.LineSegment(App.Vector(110.00000000000001,-175.00000000000000,0.00000000000000),App.Vector(70.00000000000000,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,-175.00000000000000,0.00000000000000),App.Vector(70.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC").addGeometry(Part.LineSegment(App.Vector(110.00000000000001,-45.00000000000000,0.00000000000000),App.Vector(70.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC").addGeometry(Part.LineSegment(App.Vector(110.00000000000001,-175.00000000000000,0.00000000000000),App.Vector(110.00000000000001,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Pad","Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Plane", "plane_Sketch_FWVtHavTvqhgMwe_1_JJG")
origin = App.Vector(-340.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("Sketcher::SketchObject","Sketch_FWVtHavTvqhgMwe_1_JJG")
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG").addGeometry(Part.LineSegment(App.Vector(570.00000000000011,175.00000000000000,0.00000000000000),App.Vector(570.00000000000011,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG").addGeometry(Part.LineSegment(App.Vector(570.00000000000011,45.00000000000000,0.00000000000000),App.Vector(610.00000000000011,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG").addGeometry(Part.LineSegment(App.Vector(610.00000000000011,175.00000000000000,0.00000000000000),App.Vector(610.00000000000011,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG").addGeometry(Part.LineSegment(App.Vector(570.00000000000011,175.00000000000000,0.00000000000000),App.Vector(610.00000000000011,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Pad","Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").Length = 10.0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Plane", "plane_Sketch_FWVtHavTvqhgMwe_1_JJK")
origin = App.Vector(-340.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("Sketcher::SketchObject","Sketch_FWVtHavTvqhgMwe_1_JJK")
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK").addGeometry(Part.LineSegment(App.Vector(570.00000000000011,-175.00000000000000,0.00000000000000),App.Vector(570.00000000000011,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK").addGeometry(Part.LineSegment(App.Vector(570.00000000000011,-45.00000000000000,0.00000000000000),App.Vector(610.00000000000011,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK").addGeometry(Part.LineSegment(App.Vector(610.00000000000011,-175.00000000000000,0.00000000000000),App.Vector(610.00000000000011,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK").addGeometry(Part.LineSegment(App.Vector(570.00000000000011,-175.00000000000000,0.00000000000000),App.Vector(610.00000000000011,-175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Pad","Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").Length = 10.0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Plane", "plane_Sketch_FWVtHavTvqhgMwe_1_JJO")
origin = App.Vector(-340.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("Sketcher::SketchObject","Sketch_FWVtHavTvqhgMwe_1_JJO")
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO").addGeometry(Part.LineSegment(App.Vector(110.00000000000001,175.00000000000000,0.00000000000000),App.Vector(70.00000000000000,175.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,175.00000000000000,0.00000000000000),App.Vector(70.00000000000000,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,45.00000000000000,0.00000000000000),App.Vector(110.00000000000001,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO").addGeometry(Part.LineSegment(App.Vector(110.00000000000001,175.00000000000000,0.00000000000000),App.Vector(110.00000000000001,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Pad","Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").Length = 10.0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Plane", "plane_Sketch_FWVtHavTvqhgMwe_1_JJm")
origin = App.Vector(-340.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJm").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("Sketcher::SketchObject","Sketch_FWVtHavTvqhgMwe_1_JJm")
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJm"), [""])
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm").addGeometry(Part.LineSegment(App.Vector(110.00000000000001,-45.00000000000000,0.00000000000000),App.Vector(110.00000000000001,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,45.00000000000000,0.00000000000000),App.Vector(110.00000000000001,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm").addGeometry(Part.LineSegment(App.Vector(70.00000000000000,45.00000000000000,0.00000000000000),App.Vector(70.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm").addGeometry(Part.LineSegment(App.Vector(110.00000000000001,-45.00000000000000,0.00000000000000),App.Vector(70.00000000000000,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Pad","Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").Profile = App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").Length = 10.0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJm"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").Type = 4
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJm").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Plane", "plane_Sketch_FWVtHavTvqhgMwe_1_JJq")
origin = App.Vector(-340.00000000000000,-0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJq").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("Sketcher::SketchObject","Sketch_FWVtHavTvqhgMwe_1_JJq")
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWVtHavTvqhgMwe_1_JJq"), [""])
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq").addGeometry(Part.LineSegment(App.Vector(570.00000000000011,45.00000000000000,0.00000000000000),App.Vector(570.00000000000011,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq").addGeometry(Part.LineSegment(App.Vector(570.00000000000011,-45.00000000000000,0.00000000000000),App.Vector(610.00000000000011,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq").addGeometry(Part.LineSegment(App.Vector(610.00000000000011,45.00000000000000,0.00000000000000),App.Vector(610.00000000000011,-45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq").addGeometry(Part.LineSegment(App.Vector(570.00000000000011,45.00000000000000,0.00000000000000),App.Vector(610.00000000000011,45.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ftxl21aTz3w302s_0").newObject("PartDesign::Pad","Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").Profile = App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq")
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").Length = 10.0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWVtHavTvqhgMwe_1_JJq"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").Type = 4
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWVtHavTvqhgMwe_1_Fj72LQ7wFIs5Drq_1_JJq").Offset = 0
App.ActiveDocument.recompute()

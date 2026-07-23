import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00444647")
App.ActiveDocument.addObject("PartDesign::Body","Body_FHKoXs2qpmpUxYS_0")
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").Label = "Body_FHKoXs2qpmpUxYS_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Plane", "plane_Sketch_FHKoXs2qpmpUxYS_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHKoXs2qpmpUxYS_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("Sketcher::SketchObject","Sketch_FHKoXs2qpmpUxYS_0_JGK")
App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHKoXs2qpmpUxYS_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1500.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(1500.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1500.00000000000000,1700.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(1500.00000000000000,1700.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1900.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,1700.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1900.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1700.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,1700.00000000000000,0.00000000000000),App.Vector(1273.00881000000004,1700.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,1865.73451000000000,0.00000000000000),App.Vector(1273.00881000000004,1700.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,1700.00000000000000,0.00000000000000),App.Vector(30.00000000000000,1865.73451000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,30.00000000000000,0.00000000000000),App.Vector(30.00000000000000,1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,1500.00000000000000,0.00000000000000),App.Vector(30.00000000000000,1670.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(1470.00000000000000,1670.00000000000000,0.00000000000000),App.Vector(30.00000000000000,1670.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(1470.00000000000000,30.00000000000000,0.00000000000000),App.Vector(1470.00000000000000,1670.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,30.00000000000000,0.00000000000000),App.Vector(1470.00000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Pad","Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK")
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK")
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").Length = 30.0
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHKoXs2qpmpUxYS_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHKoXs2qpmpUxYS_0_F7vdOWNnHyBiTUg_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Plane", "plane_Sketch_FPzcPSXWq8SQ21V_1_JJC")
origin = App.Vector(750.00000000000000,-30.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("Sketcher::SketchObject","Sketch_FPzcPSXWq8SQ21V_1_JJC")
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC").addGeometry(Part.LineSegment(App.Vector(-750.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(-720.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC").addGeometry(Part.LineSegment(App.Vector(-720.00000000000000,15.00000000000000,0.00000000000000),App.Vector(-720.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC").addGeometry(Part.LineSegment(App.Vector(-720.00000000000000,15.00000000000000,0.00000000000000),App.Vector(-750.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC").addGeometry(Part.LineSegment(App.Vector(-750.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(-750.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Pad","Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").Length = 1440.0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Plane", "plane_Sketch_FPzcPSXWq8SQ21V_1_JJG")
origin = App.Vector(750.00000000000000,-30.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("Sketcher::SketchObject","Sketch_FPzcPSXWq8SQ21V_1_JJG")
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG").addGeometry(Part.LineSegment(App.Vector(750.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(720.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG").addGeometry(Part.LineSegment(App.Vector(720.00000000000000,15.00000000000000,0.00000000000000),App.Vector(720.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG").addGeometry(Part.LineSegment(App.Vector(720.00000000000000,15.00000000000000,0.00000000000000),App.Vector(750.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG").addGeometry(Part.LineSegment(App.Vector(750.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(750.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Pad","Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").Length = 1440.0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Plane", "plane_Sketch_FPzcPSXWq8SQ21V_1_JJK")
origin = App.Vector(750.00000000000000,-30.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("Sketcher::SketchObject","Sketch_FPzcPSXWq8SQ21V_1_JJK")
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK").addGeometry(Part.LineSegment(App.Vector(720.00000000000000,1655.00000000000000,0.00000000000000),App.Vector(750.00000000000000,1655.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK").addGeometry(Part.LineSegment(App.Vector(750.00000000000000,1685.00000000000000,0.00000000000000),App.Vector(750.00000000000000,1655.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK").addGeometry(Part.LineSegment(App.Vector(750.00000000000000,1685.00000000000000,0.00000000000000),App.Vector(720.00000000000000,1685.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK").addGeometry(Part.LineSegment(App.Vector(720.00000000000000,1655.00000000000000,0.00000000000000),App.Vector(720.00000000000000,1685.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Pad","Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").Length = 1440.0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Plane", "plane_Sketch_FPzcPSXWq8SQ21V_1_JJO")
origin = App.Vector(750.00000000000000,-30.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("Sketcher::SketchObject","Sketch_FPzcPSXWq8SQ21V_1_JJO")
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO").addGeometry(Part.LineSegment(App.Vector(-720.00000000000000,1850.73451000000000,0.00000000000000),App.Vector(-750.00000000000000,1850.73451000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO").addGeometry(Part.LineSegment(App.Vector(-750.00000000000000,1850.73451000000000,0.00000000000000),App.Vector(-750.00000000000000,1880.73451000000023,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO").addGeometry(Part.LineSegment(App.Vector(-720.00000000000000,1880.73451000000023,0.00000000000000),App.Vector(-750.00000000000000,1880.73451000000023,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO").addGeometry(Part.LineSegment(App.Vector(-720.00000000000000,1850.73451000000000,0.00000000000000),App.Vector(-720.00000000000000,1880.73451000000023,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Pad","Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").Length = 1440.0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Plane", "plane_Sketch_FPzcPSXWq8SQ21V_1_JJe")
origin = App.Vector(750.00000000000000,-30.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("Sketcher::SketchObject","Sketch_FPzcPSXWq8SQ21V_1_JJe")
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJe"), [""])
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe").addGeometry(Part.LineSegment(App.Vector(-720.00000000000000,1685.00000000000000,0.00000000000000),App.Vector(-750.00000000000000,1685.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe").addGeometry(Part.LineSegment(App.Vector(-750.00000000000000,1685.00000000000000,0.00000000000000),App.Vector(-750.00000000000000,1655.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe").addGeometry(Part.LineSegment(App.Vector(-720.00000000000000,1655.00000000000000,0.00000000000000),App.Vector(-750.00000000000000,1655.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe").addGeometry(Part.LineSegment(App.Vector(-720.00000000000000,1685.00000000000000,0.00000000000000),App.Vector(-720.00000000000000,1655.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Pad","Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").Profile = App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").Length = 1440.0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").Type = 4
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Plane", "plane_Sketch_FPzcPSXWq8SQ21V_1_JJm")
origin = App.Vector(750.00000000000000,-30.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJm").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("Sketcher::SketchObject","Sketch_FPzcPSXWq8SQ21V_1_JJm")
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJm").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJm"), [""])
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJm").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJm").addGeometry(Part.LineSegment(App.Vector(-15.00000000000001,1787.00000000000023,0.00000000000000),App.Vector(15.00000000000001,1787.00000000000023,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJm").addGeometry(Part.LineSegment(App.Vector(15.00000000000001,1787.00000000000023,0.00000000000000),App.Vector(15.00000000000001,1783.00000000000023,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJm").addGeometry(Part.LineSegment(App.Vector(-15.00000000000001,1787.00000000000023,0.00000000000000),App.Vector(15.00000000000001,1783.00000000000023,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJm").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJm").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Pad","Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").Profile = App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJm")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").Length = 1440.0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJm"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").Type = 4
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJm").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Plane", "plane_Sketch_FPzcPSXWq8SQ21V_1_JJq")
origin = App.Vector(750.00000000000000,-30.00000000000000,15.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJq").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("Sketcher::SketchObject","Sketch_FPzcPSXWq8SQ21V_1_JJq")
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPzcPSXWq8SQ21V_1_JJq"), [""])
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq").addGeometry(Part.LineSegment(App.Vector(-15.00000000000001,1757.00000000000023,0.00000000000000),App.Vector(15.00000000000001,1757.00000000000023,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq").addGeometry(Part.LineSegment(App.Vector(15.00000000000001,1757.00000000000023,0.00000000000000),App.Vector(15.00000000000001,1783.00000000000023,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq").addGeometry(Part.LineSegment(App.Vector(-15.00000000000001,1787.00000000000023,0.00000000000000),App.Vector(15.00000000000001,1783.00000000000023,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq").addGeometry(Part.LineSegment(App.Vector(-15.00000000000001,1787.00000000000023,0.00000000000000),App.Vector(-15.00000000000001,1757.00000000000023,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHKoXs2qpmpUxYS_0").newObject("PartDesign::Pad","Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").Profile = App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq")
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").Length = 1440.0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPzcPSXWq8SQ21V_1_JJq"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").Type = 4
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPzcPSXWq8SQ21V_1_FXnsMqbCf0nt5Zl_1_JJq").Offset = 0
App.ActiveDocument.recompute()

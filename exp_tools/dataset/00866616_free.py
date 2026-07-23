import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00866616")
App.ActiveDocument.addObject("PartDesign::Body","Body_F18w95GN5St8LtV_0")
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").Label = "Body_F18w95GN5St8LtV_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Plane", "plane_Sketch_F18w95GN5St8LtV_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F18w95GN5St8LtV_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("Sketcher::SketchObject","Sketch_F18w95GN5St8LtV_0_JGC")
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F18w95GN5St8LtV_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.85000000000000,15.50000000000000,0.00000000000000),App.Vector(25.85000000000000,15.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),13.75000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.85000000000000,-12.00000000000000,0.00000000000000),App.Vector(25.85000000000000,-12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),13.75000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.85000000000000,18.50000000000000,0.00000000000000),App.Vector(25.85000000000000,18.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),16.75000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").addGeometry(Part.LineSegment(App.Vector(-25.85000000000000,-15.00000000000000,0.00000000000000),App.Vector(25.85000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),16.75000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Pad","Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC")
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC")
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").Length = 12.0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_Fr6eUEXdhnoY08e_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Plane", "plane_Sketch_F18w95GN5St8LtV_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F18w95GN5St8LtV_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("Sketcher::SketchObject","Sketch_F18w95GN5St8LtV_0_JGO")
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F18w95GN5St8LtV_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").addGeometry(Part.LineSegment(App.Vector(-25.85000000000000,15.50000000000000,0.00000000000000),App.Vector(25.85000000000000,15.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),13.75000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").addGeometry(Part.LineSegment(App.Vector(-25.85000000000000,-12.00000000000000,0.00000000000000),App.Vector(25.85000000000000,-12.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),13.75000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").addGeometry(Part.Circle(App.Vector(-25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").addGeometry(Part.Circle(App.Vector(25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Pad","Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO")
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").Profile = App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO")
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").Length = 1.0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FSjPYkNHrSjAiaj_1_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Plane", "plane_Sketch_Fgw6U3alvjoX8n5_1_JLC")
origin = App.Vector(0.00000000000000,1.75000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fgw6U3alvjoX8n5_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("Sketcher::SketchObject","Sketch_Fgw6U3alvjoX8n5_1_JLC")
App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fgw6U3alvjoX8n5_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-18.26637000000000,0.00000000000000),App.Vector(12.50000000000000,-18.26637000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,-18.26637000000000,0.00000000000000),App.Vector(12.50000000000000,-16.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-16.75000000000000,0.00000000000000),App.Vector(12.50000000000000,-16.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-18.26637000000000,0.00000000000000),App.Vector(-12.50000000000000,-16.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Pocket","Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC")
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC")
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").Length = 7.8
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Plane", "plane_Sketch_Fgw6U3alvjoX8n5_1_JLG")
origin = App.Vector(0.00000000000000,1.75000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fgw6U3alvjoX8n5_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("Sketcher::SketchObject","Sketch_Fgw6U3alvjoX8n5_1_JLG")
App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fgw6U3alvjoX8n5_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-12.05307000000000,0.00000000000000),App.Vector(12.50000000000000,-12.05307000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,-12.05307000000000,0.00000000000000),App.Vector(12.50000000000000,-13.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-13.75000000000000,0.00000000000000),App.Vector(12.50000000000000,-13.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-12.05307000000000,0.00000000000000),App.Vector(-12.50000000000000,-13.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Pocket","Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG")
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG")
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").Length = 7.8
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Plane", "plane_Sketch_Fgw6U3alvjoX8n5_1_JLO")
origin = App.Vector(0.00000000000000,1.75000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fgw6U3alvjoX8n5_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("Sketcher::SketchObject","Sketch_Fgw6U3alvjoX8n5_1_JLO")
App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fgw6U3alvjoX8n5_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-16.75000000000000,0.00000000000000),App.Vector(-12.50000000000000,-13.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-13.75000000000000,0.00000000000000),App.Vector(12.50000000000000,-13.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,-16.75000000000000,0.00000000000000),App.Vector(12.50000000000000,-13.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,-16.75000000000000,0.00000000000000),App.Vector(12.50000000000000,-16.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Pocket","Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO")
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO")
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").Length = 7.8
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fgw6U3alvjoX8n5_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fgw6U3alvjoX8n5_1_FuGeAXXpDcLPexG_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Plane", "plane_Sketch_F18w95GN5St8LtV_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F18w95GN5St8LtV_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("Sketcher::SketchObject","Sketch_F18w95GN5St8LtV_0_JGG")
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F18w95GN5St8LtV_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGG").addGeometry(Part.Circle(App.Vector(-25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Pad","Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG")
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").Profile = App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGG")
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").Length = 4.1
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Plane", "plane_Sketch_F18w95GN5St8LtV_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F18w95GN5St8LtV_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("Sketcher::SketchObject","Sketch_F18w95GN5St8LtV_0_JGK")
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F18w95GN5St8LtV_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGK").addGeometry(Part.Circle(App.Vector(25.85000000000000,1.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Pad","Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK")
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").Profile = App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGK")
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").Length = 4.1
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F18w95GN5St8LtV_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F18w95GN5St8LtV_0_FoBafmyTl3zplbB_1_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Plane", "plane_Sketch_F6HQbT3MmJSNU7y_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6HQbT3MmJSNU7y_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("Sketcher::SketchObject","Sketch_F6HQbT3MmJSNU7y_1_JRC")
App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6HQbT3MmJSNU7y_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC").addGeometry(Part.LineSegment(App.Vector(18.45499000000000,0.00000000000000,0.00000000000000),App.Vector(23.42096000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(23.42096000000000,5.14383000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.14383000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC").addGeometry(Part.LineSegment(App.Vector(18.45499000000000,10.28766000000000,0.00000000000000),App.Vector(23.42096000000000,10.28766000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC").addGeometry(Part.LineSegment(App.Vector(18.45499000000000,0.00000000000000,0.00000000000000),App.Vector(18.45499000000000,10.28766000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC").addGeometry(Part.Circle(App.Vector(23.42096000000000,5.14383000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Pad","Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC")
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC")
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").Length = 20.0
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6HQbT3MmJSNU7y_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F6HQbT3MmJSNU7y_1_FQDtaIHlDyvUNEV_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Plane", "plane_Sketch_F3CJg8LVbNdmOWe_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3CJg8LVbNdmOWe_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("Sketcher::SketchObject","Sketch_F3CJg8LVbNdmOWe_1_JVC")
App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3CJg8LVbNdmOWe_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC").addGeometry(Part.LineSegment(App.Vector(-7.50000000000000,18.49921000000000,0.00000000000000),App.Vector(7.70000000000000,18.49921000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC").addGeometry(Part.LineSegment(App.Vector(7.70000000000000,18.49921000000000,0.00000000000000),App.Vector(7.70000000000000,33.49921000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC").addGeometry(Part.LineSegment(App.Vector(-7.50000000000000,33.49921000000001,0.00000000000000),App.Vector(7.70000000000000,33.49921000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC").addGeometry(Part.LineSegment(App.Vector(-7.50000000000000,18.49921000000000,0.00000000000000),App.Vector(-7.50000000000000,33.49921000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F18w95GN5St8LtV_0").newObject("PartDesign::Pocket","Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC")
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC")
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").Length = -30.0
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3CJg8LVbNdmOWe_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").Type = 0
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3CJg8LVbNdmOWe_1_FRTzvZoyybXkZHr_1_JVC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00404572")
App.ActiveDocument.addObject("PartDesign::Body","Body_FLJ8xsxf6VFKnhA_0")
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").Label = "Body_FLJ8xsxf6VFKnhA_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Plane", "plane_Sketch_FLJ8xsxf6VFKnhA_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLJ8xsxf6VFKnhA_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("Sketcher::SketchObject","Sketch_FLJ8xsxf6VFKnhA_0_JGC")
App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLJ8xsxf6VFKnhA_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-421.52345000000003,0.00000000000000,0.00000000000000),App.Vector(-421.52345000000003,26.94077000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-421.52345000000003,26.94077000000000,0.00000000000000),App.Vector(162.19318999999999,610.65742000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC").addGeometry(Part.LineSegment(App.Vector(189.13396000000000,610.65742000000000,0.00000000000000),App.Vector(162.19318999999999,610.65742000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-421.52345000000003,0.00000000000000,0.00000000000000),App.Vector(189.13396000000000,610.65742000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Pad","Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC")
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC")
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").Length = 304.8
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLJ8xsxf6VFKnhA_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FLJ8xsxf6VFKnhA_0_FGtlomklGeKllvz_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Plane", "plane_Sketch_F8itC1K8Z2g28tJ_1_JJC")
origin = App.Vector(-129.66512999999998,0.00000000000000,318.79909000000004)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("Sketcher::SketchObject","Sketch_F8itC1K8Z2g28tJ_1_JJC")
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-342.89999904436741,0.00000707106781),App.Vector(0.00000000000000,-342.89999904436741,0.00000707106781)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-342.89999904436741,0.00000707106781),App.Vector(0.00000000000000,-323.84999791894683,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-323.84999791894683,0.00000000000000),App.Vector(0.00000000000000,-323.84999791894683,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-342.89999904436741,0.00000707106781),App.Vector(-152.40000000000001,-323.84999791894683,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Pocket","Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").Length = 19.05
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Plane", "plane_Sketch_F8itC1K8Z2g28tJ_1_JJG")
origin = App.Vector(-129.66512999999998,0.00000000000000,318.79909000000004)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("Sketcher::SketchObject","Sketch_F8itC1K8Z2g28tJ_1_JJG")
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-234.95000209507444,0.00000000000003),App.Vector(0.00000000000000,-234.95000209507444,0.00000000000003)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-234.95000209507444,0.00000000000003),App.Vector(0.00000000000000,-215.89999389858605,0.00000000000001)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-215.89999389858605,0.00000000000001),App.Vector(0.00000000000000,-215.89999389858605,0.00000000000001)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-234.95000209507444,0.00000000000003),App.Vector(-152.40000000000001,-215.89999389858605,0.00000000000001)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Pocket","Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").Length = 19.05
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Plane", "plane_Sketch_F8itC1K8Z2g28tJ_1_JJK")
origin = App.Vector(-129.66512999999998,0.00000000000000,318.79909000000004)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("Sketcher::SketchObject","Sketch_F8itC1K8Z2g28tJ_1_JJK")
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-126.99999807471363,0.00000000000000),App.Vector(0.00000000000000,-126.99999807471363,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-126.99999807471363,0.00000000000000),App.Vector(0.00000000000000,-107.94999694929301,0.00000707106780)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-107.94999694929301,0.00000707106780),App.Vector(0.00000000000000,-107.94999694929301,0.00000707106780)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-126.99999807471363,0.00000000000000),App.Vector(-152.40000000000001,-107.94999694929301,0.00000707106780)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Pocket","Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").Length = 19.05
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Plane", "plane_Sketch_F8itC1K8Z2g28tJ_1_JJO")
origin = App.Vector(-129.66512999999998,0.00000000000000,318.79909000000004)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("Sketcher::SketchObject","Sketch_F8itC1K8Z2g28tJ_1_JJO")
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-19.04999405435281,0.00000000000000),App.Vector(0.00000000000000,-19.04999405435281,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-19.04999405435281,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-19.04999405435281,0.00000000000000),App.Vector(-152.40000000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Pocket","Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").Length = 19.05
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Plane", "plane_Sketch_F8itC1K8Z2g28tJ_1_JJS")
origin = App.Vector(-129.66512999999998,0.00000000000000,318.79909000000004)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("Sketcher::SketchObject","Sketch_F8itC1K8Z2g28tJ_1_JJS")
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,88.90000289494017,0.00000707106779),App.Vector(0.00000000000000,88.90000289494017,0.00000707106779)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,88.90000289494017,0.00000707106779),App.Vector(0.00000000000000,107.95000402036078,-0.00000000000002)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,107.95000402036078,-0.00000000000002),App.Vector(0.00000000000000,107.95000402036078,-0.00000000000002)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,88.90000289494017,0.00000707106779),App.Vector(-152.40000000000001,107.95000402036078,-0.00000000000002)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Pocket","Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").Length = 19.05
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Plane", "plane_Sketch_F8itC1K8Z2g28tJ_1_JJW")
origin = App.Vector(-129.66512999999998,0.00000000000000,318.79909000000004)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("Sketcher::SketchObject","Sketch_F8itC1K8Z2g28tJ_1_JJW")
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,196.84999984423320,0.00000000000000),App.Vector(0.00000000000000,196.84999984423320,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,196.84999984423320,0.00000000000000),App.Vector(0.00000000000000,215.90000096965383,0.00000707106780)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,215.90000096965383,0.00000707106780),App.Vector(0.00000000000000,215.90000096965383,0.00000707106780)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,196.84999984423320,0.00000000000000),App.Vector(-152.40000000000001,215.90000096965383,0.00000707106780)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Pocket","Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").Length = 19.05
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Plane", "plane_Sketch_F8itC1K8Z2g28tJ_1_JJa")
origin = App.Vector(-129.66512999999998,0.00000000000000,318.79909000000004)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.70710678000000,0.00000000000000,0.70710678000000)
z_axis=App.Vector(-0.70710678000000,0.00000000000000,0.70710678000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("Sketcher::SketchObject","Sketch_F8itC1K8Z2g28tJ_1_JJa")
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8itC1K8Z2g28tJ_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,304.80000386459403,0.00000000000003),App.Vector(0.00000000000000,304.80000386459403,0.00000000000003)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,304.80000386459403,0.00000000000003),App.Vector(0.00000000000000,323.84999791894688,0.00000000000003)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,323.84999791894688,0.00000000000003),App.Vector(0.00000000000000,323.84999791894688,0.00000000000003)),False)

App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,304.80000386459403,0.00000000000003),App.Vector(-152.40000000000001,323.84999791894688,0.00000000000003)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLJ8xsxf6VFKnhA_0").newObject("PartDesign::Pocket","Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa")
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").Length = 19.05
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8itC1K8Z2g28tJ_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8itC1K8Z2g28tJ_1_F7bWqLIjksNfqkp_1_JJa").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00273909")
App.ActiveDocument.addObject("PartDesign::Body","Body_FckVi6sz5LDc7fy_0")
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").Label = "Body_FckVi6sz5LDc7fy_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_FckVi6sz5LDc7fy_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FckVi6sz5LDc7fy_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_FckVi6sz5LDc7fy_0_JGC")
App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FckVi6sz5LDc7fy_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC").addGeometry(Part.LineSegment(App.Vector(-15.80000000000000,14.95000000000000,0.00000000000000),App.Vector(15.80000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC").addGeometry(Part.LineSegment(App.Vector(15.80000000000000,14.95000000000000,0.00000000000000),App.Vector(15.80000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC").addGeometry(Part.LineSegment(App.Vector(-15.80000000000000,-14.95000000000000,0.00000000000000),App.Vector(15.80000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC").addGeometry(Part.LineSegment(App.Vector(-15.80000000000000,14.95000000000000,0.00000000000000),App.Vector(-15.80000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC")
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC")
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").Length = 1.2
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FckVi6sz5LDc7fy_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FckVi6sz5LDc7fy_0_FsWrdCBkqoa4CcI_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_FY8qXOos74Gfgf6_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FY8qXOos74Gfgf6_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_FY8qXOos74Gfgf6_1_JJO")
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FY8qXOos74Gfgf6_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,10.30000000000000,0.00000000000000),App.Vector(4.00000000000000,10.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO").addGeometry(Part.LineSegment(App.Vector(4.00000000000000,10.30000000000000,0.00000000000000),App.Vector(4.00000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,14.95000000000000,0.00000000000000),App.Vector(4.00000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,10.30000000000000,0.00000000000000),App.Vector(-4.00000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO")
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO")
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").Length = 3.0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_FY8qXOos74Gfgf6_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FY8qXOos74Gfgf6_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_FY8qXOos74Gfgf6_1_JJK")
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FY8qXOos74Gfgf6_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,16.05000000000000,0.00000000000000),App.Vector(4.00000000000000,16.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK").addGeometry(Part.LineSegment(App.Vector(4.00000000000000,16.05000000000000,0.00000000000000),App.Vector(4.00000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,14.95000000000000,0.00000000000000),App.Vector(4.00000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK").addGeometry(Part.LineSegment(App.Vector(-4.00000000000000,16.05000000000000,0.00000000000000),App.Vector(-4.00000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK")
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK")
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").Length = 3.0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FqwomGqhKZgMdHU_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_FY8qXOos74Gfgf6_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FY8qXOos74Gfgf6_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_FY8qXOos74Gfgf6_1_JJC")
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FY8qXOos74Gfgf6_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.05000000000000,12.15000000000000,0.00000000000000),App.Vector(-12.55000000000000,12.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC").addGeometry(Part.LineSegment(App.Vector(-12.55000000000000,12.15000000000000,0.00000000000000),App.Vector(-12.55000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.05000000000000,-7.35000000000000,0.00000000000000),App.Vector(-12.55000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.05000000000000,12.15000000000000,0.00000000000000),App.Vector(-15.05000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC")
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC")
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").Length = 2.5
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").Length2 = 3.1000000000000005
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_FY8qXOos74Gfgf6_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FY8qXOos74Gfgf6_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_FY8qXOos74Gfgf6_1_JJG")
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FY8qXOos74Gfgf6_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG").addGeometry(Part.LineSegment(App.Vector(12.55000000000000,12.15000000000000,0.00000000000000),App.Vector(15.05000000000000,12.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG").addGeometry(Part.LineSegment(App.Vector(15.05000000000000,12.15000000000000,0.00000000000000),App.Vector(15.05000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG").addGeometry(Part.LineSegment(App.Vector(12.55000000000000,-7.35000000000000,0.00000000000000),App.Vector(15.05000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG").addGeometry(Part.LineSegment(App.Vector(12.55000000000000,12.15000000000000,0.00000000000000),App.Vector(12.55000000000000,-7.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG")
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG")
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").Length = 2.5
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").Length2 = 3.1000000000000005
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FY8qXOos74Gfgf6_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FY8qXOos74Gfgf6_1_FerJm7ai486yZyw_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_Fl4cDzsCQyLw3QB_1_JPG")
origin = App.Vector(0.00000000000000,0.00000000000000,1.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fl4cDzsCQyLw3QB_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_Fl4cDzsCQyLw3QB_1_JPG")
App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fl4cDzsCQyLw3QB_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPG").addGeometry(Part.Circle(App.Vector(-12.60000000000000,11.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG")
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPG")
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").Length = 2.75
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FxRo86FmWKDPiB3_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_Fl4cDzsCQyLw3QB_1_JPK")
origin = App.Vector(0.00000000000000,0.00000000000000,1.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fl4cDzsCQyLw3QB_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_Fl4cDzsCQyLw3QB_1_JPK")
App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fl4cDzsCQyLw3QB_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK").addGeometry(Part.LineSegment(App.Vector(9.30000000000000,13.95000000000000,0.00000000000000),App.Vector(14.30000000000000,13.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK").addGeometry(Part.LineSegment(App.Vector(14.30000000000000,13.95000000000000,0.00000000000000),App.Vector(14.30000000000000,8.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK").addGeometry(Part.LineSegment(App.Vector(9.30000000000000,8.95000000000000,0.00000000000000),App.Vector(14.30000000000000,8.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK").addGeometry(Part.LineSegment(App.Vector(9.30000000000000,13.95000000000000,0.00000000000000),App.Vector(9.30000000000000,8.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK")
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK")
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").Length = 1.75
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_Fptrjg99mcH0vER_1_JPK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_Fl4cDzsCQyLw3QB_1_JPC")
origin = App.Vector(0.00000000000000,0.00000000000000,1.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fl4cDzsCQyLw3QB_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_Fl4cDzsCQyLw3QB_1_JPC")
App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fl4cDzsCQyLw3QB_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC").addGeometry(Part.LineSegment(App.Vector(-8.80000000000000,14.95000000000000,0.00000000000000),App.Vector(7.20000000000000,14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC").addGeometry(Part.LineSegment(App.Vector(7.20000000000000,14.95000000000000,0.00000000000000),App.Vector(7.20000000000000,-9.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC").addGeometry(Part.LineSegment(App.Vector(-8.80000000000000,-9.15000000000000,0.00000000000000),App.Vector(7.20000000000000,-9.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC").addGeometry(Part.LineSegment(App.Vector(-8.80000000000000,14.95000000000000,0.00000000000000),App.Vector(-8.80000000000000,-9.15000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC")
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC")
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").Length = 4.0
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fl4cDzsCQyLw3QB_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fl4cDzsCQyLw3QB_1_FWsZq89VfzBQFLR_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_FNR03K98RMeSE26_1_JXO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNR03K98RMeSE26_1_JXO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_FNR03K98RMeSE26_1_JXO")
App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNR03K98RMeSE26_1_JXO"), [""])
App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO").addGeometry(Part.LineSegment(App.Vector(-5.30000000000000,-12.65000000000000,0.00000000000000),App.Vector(1.70000000000000,-12.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO").addGeometry(Part.LineSegment(App.Vector(1.70000000000000,-12.65000000000000,0.00000000000000),App.Vector(1.70000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO").addGeometry(Part.LineSegment(App.Vector(-5.30000000000000,-14.95000000000000,0.00000000000000),App.Vector(1.70000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO").addGeometry(Part.LineSegment(App.Vector(-5.30000000000000,-12.65000000000000,0.00000000000000),App.Vector(-5.30000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO")
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").Profile = App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO")
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").Length = 4.0
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").Type = 4
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Plane", "plane_Sketch_FNR03K98RMeSE26_1_JXK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNR03K98RMeSE26_1_JXK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("Sketcher::SketchObject","Sketch_FNR03K98RMeSE26_1_JXK")
App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNR03K98RMeSE26_1_JXK"), [""])
App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK").addGeometry(Part.LineSegment(App.Vector(-5.30000000000000,-16.15000000000000,0.00000000000000),App.Vector(1.70000000000000,-16.15000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK").addGeometry(Part.LineSegment(App.Vector(1.70000000000000,-16.15000000000000,0.00000000000000),App.Vector(1.70000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK").addGeometry(Part.LineSegment(App.Vector(-5.30000000000000,-14.95000000000000,0.00000000000000),App.Vector(1.70000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK").addGeometry(Part.LineSegment(App.Vector(-5.30000000000000,-16.15000000000000,0.00000000000000),App.Vector(-5.30000000000000,-14.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FckVi6sz5LDc7fy_0").newObject("PartDesign::Pad","Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK")
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").Profile = App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK")
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").Length = 4.0
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNR03K98RMeSE26_1_JXK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").Type = 4
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNR03K98RMeSE26_1_F5PyaF5XqM0kWOH_1_JXK").Offset = 0
App.ActiveDocument.recompute()

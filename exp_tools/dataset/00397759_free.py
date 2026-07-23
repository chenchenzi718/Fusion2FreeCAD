import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00397759")
App.ActiveDocument.addObject("PartDesign::Body","Body_F31UeRbotNdsgfB_0")
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").Label = "Body_F31UeRbotNdsgfB_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Plane", "plane_Sketch_F31UeRbotNdsgfB_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F31UeRbotNdsgfB_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("Sketcher::SketchObject","Sketch_F31UeRbotNdsgfB_0_JGS")
App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F31UeRbotNdsgfB_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").addGeometry(Part.LineSegment(App.Vector(45.95000000000000,-78.45000000000000,0.00000000000000),App.Vector(-45.95000000000000,-78.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").addGeometry(Part.LineSegment(App.Vector(-45.95000000000000,-78.45000000000000,0.00000000000000),App.Vector(-45.95000000000000,78.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").addGeometry(Part.LineSegment(App.Vector(45.95000000000000,78.45000000000000,0.00000000000000),App.Vector(-45.95000000000000,78.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").addGeometry(Part.LineSegment(App.Vector(45.95000000000000,-78.45000000000000,0.00000000000000),App.Vector(45.95000000000000,78.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").addGeometry(Part.Circle(App.Vector(-41.00000000000000,73.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.80000000000000),False)

App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").addGeometry(Part.Circle(App.Vector(41.00000000000000,73.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.80000000000000),False)

App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").addGeometry(Part.Circle(App.Vector(41.00000000000000,-73.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.80000000000000),False)

App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").addGeometry(Part.Circle(App.Vector(-41.00000000000000,-73.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.80000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Pad","Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS")
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").Profile = App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS")
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").Length = 1.0
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F31UeRbotNdsgfB_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F31UeRbotNdsgfB_0_FrcJFwGf5JxtaQT_0_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Plane", "plane_Sketch_FE3zyJMknQ7WNuD_1_JJO")
origin = App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("Sketcher::SketchObject","Sketch_FE3zyJMknQ7WNuD_1_JJO")
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJO").addGeometry(Part.Circle(App.Vector(20.90000000000000,51.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Pocket","Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJO")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").Length = 2.0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Plane", "plane_Sketch_FE3zyJMknQ7WNuD_1_JJC")
origin = App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("Sketcher::SketchObject","Sketch_FE3zyJMknQ7WNuD_1_JJC")
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJC").addGeometry(Part.Circle(App.Vector(-20.90000000000000,51.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Pocket","Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJC")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Plane", "plane_Sketch_FE3zyJMknQ7WNuD_1_JJK")
origin = App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("Sketcher::SketchObject","Sketch_FE3zyJMknQ7WNuD_1_JJK")
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJK").addGeometry(Part.Circle(App.Vector(6.80000000000000,51.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Pocket","Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJK")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").Length = 2.0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Plane", "plane_Sketch_FE3zyJMknQ7WNuD_1_JJG")
origin = App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("Sketcher::SketchObject","Sketch_FE3zyJMknQ7WNuD_1_JJG")
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJG").addGeometry(Part.Circle(App.Vector(-6.80000000000000,51.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Pocket","Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJG")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").Length = 2.0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Plane", "plane_Sketch_FE3zyJMknQ7WNuD_1_JJS")
origin = App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("Sketcher::SketchObject","Sketch_FE3zyJMknQ7WNuD_1_JJS")
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,-7.30000000000000,0.00000000000000),App.Vector(-37.50000000000000,-7.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-37.50000000000000,-6.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").addGeometry(Part.LineSegment(App.Vector(-38.00000000000000,-6.80000000000000,0.00000000000000),App.Vector(-38.00000000000000,37.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-37.50000000000000,37.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").addGeometry(Part.LineSegment(App.Vector(37.50000000000000,38.20000000000000,0.00000000000000),App.Vector(-37.50000000000000,38.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(37.50000000000000,37.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").addGeometry(Part.LineSegment(App.Vector(38.00000000000000,-6.80000000000000,0.00000000000000),App.Vector(38.00000000000000,37.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(37.50000000000000,-6.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Pocket","Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").Length = 2.0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Plane", "plane_Sketch_FE3zyJMknQ7WNuD_1_JJW")
origin = App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("Sketcher::SketchObject","Sketch_FE3zyJMknQ7WNuD_1_JJW")
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJW").addGeometry(Part.Circle(App.Vector(0.00000000000000,-19.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Pocket","Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJW")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").Length = 2.0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Plane", "plane_Sketch_FE3zyJMknQ7WNuD_1_JJa")
origin = App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("Sketcher::SketchObject","Sketch_FE3zyJMknQ7WNuD_1_JJa")
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE3zyJMknQ7WNuD_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJa").addGeometry(Part.Circle(App.Vector(0.00000000000000,-49.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F31UeRbotNdsgfB_0").newObject("PartDesign::Pocket","Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJa")
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").Length = 2.0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE3zyJMknQ7WNuD_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE3zyJMknQ7WNuD_1_FFQx7l0xjPp6LdC_1_JJa").Offset = 0
App.ActiveDocument.recompute()

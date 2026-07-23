import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00774655")
App.ActiveDocument.addObject("PartDesign::Body","Body_FUIcX8q14BGGGNb_0")
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").Label = "Body_FUIcX8q14BGGGNb_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FUIcX8q14BGGGNb_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUIcX8q14BGGGNb_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FUIcX8q14BGGGNb_0_JGC")
App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUIcX8q14BGGGNb_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,6.35000000000000,0.00000000000000),App.Vector(121.92000000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC").addGeometry(Part.LineSegment(App.Vector(121.92000000000000,3.17500000000000,0.00000000000000),App.Vector(121.92000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(121.92000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pad","Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC")
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC")
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").Length = 92.075
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUIcX8q14BGGGNb_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUIcX8q14BGGGNb_0_F13sqkRjVpSDCXp_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FRe3Q99iQ5WMb5K_0_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FRe3Q99iQ5WMb5K_0_JJG")
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJG").addGeometry(Part.Circle(App.Vector(8.89000000000000,61.91250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pocket","Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").Profile = App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJG")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FRe3Q99iQ5WMb5K_0_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FRe3Q99iQ5WMb5K_0_JJC")
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJC").addGeometry(Part.Circle(App.Vector(8.89000000000000,30.16250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pocket","Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").Profile = App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJC")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FRe3Q99iQ5WMb5K_0_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FRe3Q99iQ5WMb5K_0_JJO")
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJO").addGeometry(Part.Circle(App.Vector(113.03000000000000,30.16250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pocket","Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").Profile = App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJO")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").Type = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FRe3Q99iQ5WMb5K_0_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FRe3Q99iQ5WMb5K_0_JJK")
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJK").addGeometry(Part.Circle(App.Vector(113.03000000000000,61.91250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pocket","Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").Profile = App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJK")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FRe3Q99iQ5WMb5K_0_JJS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FRe3Q99iQ5WMb5K_0_JJS")
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS").addGeometry(Part.LineSegment(App.Vector(19.05000000000000,84.13750000000000,0.00000000000000),App.Vector(102.87000000000000,84.13750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS").addGeometry(Part.LineSegment(App.Vector(102.87000000000000,84.13750000000000,0.00000000000000),App.Vector(102.87000000000000,7.93750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS").addGeometry(Part.LineSegment(App.Vector(19.05000000000000,7.93750000000000,0.00000000000000),App.Vector(102.87000000000000,7.93750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS").addGeometry(Part.LineSegment(App.Vector(19.05000000000000,84.13750000000000,0.00000000000000),App.Vector(19.05000000000000,7.93750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pocket","Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").Profile = App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").Type = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FRe3Q99iQ5WMb5K_0_JJe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FRe3Q99iQ5WMb5K_0_JJe")
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJe"), [""])
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJe").addGeometry(Part.LineSegment(App.Vector(121.92000000000000,92.07500000000000,0.00000000000000),App.Vector(108.44962000000000,92.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJe").addGeometry(Part.LineSegment(App.Vector(121.92000000000000,78.60462000000000,0.00000000000000),App.Vector(108.44962000000000,92.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJe").addGeometry(Part.LineSegment(App.Vector(121.92000000000000,92.07500000000000,0.00000000000000),App.Vector(121.92000000000000,78.60462000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pocket","Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").Profile = App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJe")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").Type = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FRe3Q99iQ5WMb5K_0_JJW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FRe3Q99iQ5WMb5K_0_JJW")
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJW").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,78.60462000000000,0.00000000000000),App.Vector(0.00000000000000,92.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJW").addGeometry(Part.LineSegment(App.Vector(13.47038000000000,92.07500000000000,0.00000000000000),App.Vector(0.00000000000000,92.07500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJW").addGeometry(Part.LineSegment(App.Vector(13.47038000000000,92.07500000000000,0.00000000000000),App.Vector(0.00000000000000,78.60462000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pocket","Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").Profile = App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJW")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").Type = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FRe3Q99iQ5WMb5K_0_JJa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FRe3Q99iQ5WMb5K_0_JJa")
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJa").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,13.47038000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJa").addGeometry(Part.LineSegment(App.Vector(13.47038000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJa").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,13.47038000000000,0.00000000000000),App.Vector(13.47038000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pocket","Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").Profile = App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJa")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").Type = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Plane", "plane_Sketch_FRe3Q99iQ5WMb5K_0_JJi")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("Sketcher::SketchObject","Sketch_FRe3Q99iQ5WMb5K_0_JJi")
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRe3Q99iQ5WMb5K_0_JJi"), [""])
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJi").addGeometry(Part.LineSegment(App.Vector(121.92000000000000,13.47038000000000,0.00000000000000),App.Vector(121.92000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJi").addGeometry(Part.LineSegment(App.Vector(108.44962000000000,0.00000000000000,0.00000000000000),App.Vector(121.92000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJi").addGeometry(Part.LineSegment(App.Vector(108.44962000000000,0.00000000000000,0.00000000000000),App.Vector(121.92000000000000,13.47038000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUIcX8q14BGGGNb_0").newObject("PartDesign::Pocket","Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").Profile = App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJi")
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRe3Q99iQ5WMb5K_0_JJi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").Type = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").Reversed = 1
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRe3Q99iQ5WMb5K_0_FD37g0F0Er07roP_0_JJi").Offset = 0
App.ActiveDocument.recompute()

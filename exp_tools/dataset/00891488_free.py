import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00891488")
App.ActiveDocument.addObject("PartDesign::Body","Body_FI95osfUnkxy8Ly_0")
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").Label = "Body_FI95osfUnkxy8Ly_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Plane", "plane_Sketch_FI95osfUnkxy8Ly_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FI95osfUnkxy8Ly_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("Sketcher::SketchObject","Sketch_FI95osfUnkxy8Ly_0_JGC")
App.ActiveDocument.getObject("Sketch_FI95osfUnkxy8Ly_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FI95osfUnkxy8Ly_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FI95osfUnkxy8Ly_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FI95osfUnkxy8Ly_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),45.63164000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FI95osfUnkxy8Ly_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FI95osfUnkxy8Ly_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Pad","Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC")
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FI95osfUnkxy8Ly_0_JGC")
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FI95osfUnkxy8Ly_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FI95osfUnkxy8Ly_0_FL1YmBuYiypHMpl_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Plane", "plane_Sketch_FPnZTap21CRpIlD_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("Sketcher::SketchObject","Sketch_FPnZTap21CRpIlD_1_JJC")
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,39.53982999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.19660000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Pocket","Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJC")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Plane", "plane_Sketch_FPnZTap21CRpIlD_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("Sketcher::SketchObject","Sketch_FPnZTap21CRpIlD_1_JJG")
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJG").addGeometry(Part.Circle(App.Vector(37.98925000000001,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.19661000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Pocket","Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJG")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Plane", "plane_Sketch_FPnZTap21CRpIlD_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("Sketcher::SketchObject","Sketch_FPnZTap21CRpIlD_1_JJK")
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJK").addGeometry(Part.Circle(App.Vector(0.00000000000000,-36.74878000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.18153000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Pocket","Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJK")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Plane", "plane_Sketch_FPnZTap21CRpIlD_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("Sketcher::SketchObject","Sketch_FPnZTap21CRpIlD_1_JJO")
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJO").addGeometry(Part.Circle(App.Vector(-39.22971000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.19661000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Pocket","Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJO")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").Type = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Plane", "plane_Sketch_FPnZTap21CRpIlD_1_JJS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("Sketcher::SketchObject","Sketch_FPnZTap21CRpIlD_1_JJS")
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJS").addGeometry(Part.Circle(App.Vector(-26.20483000000000,27.75541000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.23771000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Pocket","Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJS")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").Type = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Plane", "plane_Sketch_FPnZTap21CRpIlD_1_JJW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("Sketcher::SketchObject","Sketch_FPnZTap21CRpIlD_1_JJW")
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJW").addGeometry(Part.Circle(App.Vector(-27.75541000000000,-23.41378000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.19284000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Pocket","Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJW")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").Type = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Plane", "plane_Sketch_FPnZTap21CRpIlD_1_JJa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("Sketcher::SketchObject","Sketch_FPnZTap21CRpIlD_1_JJa")
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJa").addGeometry(Part.Circle(App.Vector(23.41378000000000,25.58459000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.23771000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Pocket","Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJa")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").Type = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Plane", "plane_Sketch_FPnZTap21CRpIlD_1_JJe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("Sketcher::SketchObject","Sketch_FPnZTap21CRpIlD_1_JJe")
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPnZTap21CRpIlD_1_JJe"), [""])
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJe").addGeometry(Part.Circle(App.Vector(22.48343000000000,-23.10366000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.19284000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FI95osfUnkxy8Ly_0").newObject("PartDesign::Pocket","Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").Profile = App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJe")
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPnZTap21CRpIlD_1_JJe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").Type = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPnZTap21CRpIlD_1_FsFdPDpK6UjjXNF_1_JJe").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00176497")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fr7Oe9GqAXDwTSV_0")
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").Label = "Body_Fr7Oe9GqAXDwTSV_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_Fr7Oe9GqAXDwTSV_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr7Oe9GqAXDwTSV_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_Fr7Oe9GqAXDwTSV_0_JGC")
App.ActiveDocument.getObject("Sketch_Fr7Oe9GqAXDwTSV_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr7Oe9GqAXDwTSV_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fr7Oe9GqAXDwTSV_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr7Oe9GqAXDwTSV_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),59.56666000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr7Oe9GqAXDwTSV_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr7Oe9GqAXDwTSV_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pad","Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC")
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fr7Oe9GqAXDwTSV_0_JGC")
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").Length = 7.62
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr7Oe9GqAXDwTSV_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fr7Oe9GqAXDwTSV_0_Fm96UWuD54TEoHo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_FA0ZRCNF35WbfRG_1_JJC")
origin = App.Vector(-0.52839000000000,0.63963000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FA0ZRCNF35WbfRG_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_FA0ZRCNF35WbfRG_1_JJC")
App.ActiveDocument.getObject("Sketch_FA0ZRCNF35WbfRG_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FA0ZRCNF35WbfRG_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FA0ZRCNF35WbfRG_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FA0ZRCNF35WbfRG_1_JJC").addGeometry(Part.Circle(App.Vector(0.52839000000000,-0.63963000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),38.83477000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FA0ZRCNF35WbfRG_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FA0ZRCNF35WbfRG_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pocket","Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC")
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FA0ZRCNF35WbfRG_1_JJC")
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FA0ZRCNF35WbfRG_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FA0ZRCNF35WbfRG_1_FiW7fYV2Eo26E1N_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_F3OtuxLEhgHEzi7_1_JNW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_F3OtuxLEhgHEzi7_1_JNW")
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW").addGeometry(Part.LineSegment(App.Vector(-60.53032000000000,-34.87639000000000,0.00000000000000),App.Vector(-33.58955000000000,-61.81715000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW").addGeometry(Part.LineSegment(App.Vector(-33.58955000000000,-61.81715000000000,0.00000000000000),App.Vector(-24.60929000000000,-52.83690000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW").addGeometry(Part.LineSegment(App.Vector(-51.55006000000000,-25.89613000000000,0.00000000000000),App.Vector(-24.60929000000000,-52.83690000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW").addGeometry(Part.LineSegment(App.Vector(-60.53032000000000,-34.87639000000000,0.00000000000000),App.Vector(-51.55006000000000,-25.89613000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pad","Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").Length = 7.62
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").Type = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_F3OtuxLEhgHEzi7_1_JNS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_F3OtuxLEhgHEzi7_1_JNS")
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS").addGeometry(Part.LineSegment(App.Vector(36.11831000000000,-59.54806000000000,0.00000000000000),App.Vector(60.60851000000000,-30.36176000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS").addGeometry(Part.LineSegment(App.Vector(60.60851000000000,-30.36176000000000,0.00000000000000),App.Vector(50.87975000000000,-22.19836000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS").addGeometry(Part.LineSegment(App.Vector(26.38954000000000,-51.38464999999999,0.00000000000000),App.Vector(50.87975000000000,-22.19836000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS").addGeometry(Part.LineSegment(App.Vector(36.11831000000000,-59.54806000000000,0.00000000000000),App.Vector(26.38954000000000,-51.38464999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pad","Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").Length = 7.62
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").Type = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_F3OtuxLEhgHEzi7_1_JNK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_F3OtuxLEhgHEzi7_1_JNK")
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK").addGeometry(Part.LineSegment(App.Vector(53.98890000000000,-18.88314000000000,0.00000000000000),App.Vector(66.68889999999999,-18.88314000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK").addGeometry(Part.LineSegment(App.Vector(66.68889999999999,-18.88314000000000,0.00000000000000),App.Vector(66.68889999999999,19.21686000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK").addGeometry(Part.LineSegment(App.Vector(53.98890000000000,19.21686000000000,0.00000000000000),App.Vector(66.68889999999999,19.21686000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK").addGeometry(Part.LineSegment(App.Vector(53.98890000000000,-18.88314000000000,0.00000000000000),App.Vector(53.98890000000000,19.21686000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pad","Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").Length = 7.62
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").Type = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_F3OtuxLEhgHEzi7_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_F3OtuxLEhgHEzi7_1_JNC")
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC").addGeometry(Part.LineSegment(App.Vector(-18.81825000000000,-66.12343000000000,0.00000000000000),App.Vector(19.28175000000000,-66.12343000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC").addGeometry(Part.LineSegment(App.Vector(19.28175000000000,-66.12343000000000,0.00000000000000),App.Vector(19.28175000000000,-53.42343000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC").addGeometry(Part.LineSegment(App.Vector(-18.81825000000000,-53.42343000000000,0.00000000000000),App.Vector(19.28175000000000,-53.42343000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC").addGeometry(Part.LineSegment(App.Vector(-18.81825000000000,-66.12343000000000,0.00000000000000),App.Vector(-18.81825000000000,-53.42343000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pad","Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").Length = 7.62
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_F3OtuxLEhgHEzi7_1_JNO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_F3OtuxLEhgHEzi7_1_JNO")
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO").addGeometry(Part.LineSegment(App.Vector(-67.74569000000000,-17.45555000000000,0.00000000000000),App.Vector(-55.04569000000000,-17.45555000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO").addGeometry(Part.LineSegment(App.Vector(-55.04569000000000,-17.45555000000000,0.00000000000000),App.Vector(-55.04569000000000,20.64445000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO").addGeometry(Part.LineSegment(App.Vector(-67.74569000000000,20.64445000000000,0.00000000000000),App.Vector(-55.04569000000000,20.64445000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO").addGeometry(Part.LineSegment(App.Vector(-67.74569000000000,-17.45555000000000,0.00000000000000),App.Vector(-67.74569000000000,20.64445000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pad","Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").Length = 7.62
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").Type = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_F3OtuxLEhgHEzi7_1_JNe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_F3OtuxLEhgHEzi7_1_JNe")
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNe"), [""])
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe").addGeometry(Part.LineSegment(App.Vector(-51.59543000000000,26.45841000000000,0.00000000000000),App.Vector(-24.65466000000000,53.39917999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe").addGeometry(Part.LineSegment(App.Vector(-24.65466000000000,53.39917999999999,0.00000000000000),App.Vector(-33.63492000000000,62.37944000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe").addGeometry(Part.LineSegment(App.Vector(-60.57569000000000,35.43867000000000,0.00000000000000),App.Vector(-33.63492000000000,62.37944000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe").addGeometry(Part.LineSegment(App.Vector(-51.59543000000000,26.45841000000000,0.00000000000000),App.Vector(-60.57569000000000,35.43867000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pad","Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").Profile = App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").Length = 7.62
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").Type = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_F3OtuxLEhgHEzi7_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_F3OtuxLEhgHEzi7_1_JNG")
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG").addGeometry(Part.LineSegment(App.Vector(-18.81825000000000,54.70270000000000,0.00000000000000),App.Vector(19.28175000000000,54.70270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG").addGeometry(Part.LineSegment(App.Vector(19.28175000000000,54.70270000000000,0.00000000000000),App.Vector(19.28175000000000,67.40270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG").addGeometry(Part.LineSegment(App.Vector(-18.81825000000000,67.40270000000000,0.00000000000000),App.Vector(19.28175000000000,67.40270000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG").addGeometry(Part.LineSegment(App.Vector(-18.81825000000000,54.70270000000000,0.00000000000000),App.Vector(-18.81825000000000,67.40270000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pad","Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").Length = 7.62
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").Type = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Plane", "plane_Sketch_F3OtuxLEhgHEzi7_1_JNa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("Sketcher::SketchObject","Sketch_F3OtuxLEhgHEzi7_1_JNa")
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3OtuxLEhgHEzi7_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa").addGeometry(Part.LineSegment(App.Vector(25.53857000000000,51.49677000000000,0.00000000000000),App.Vector(52.47934000000000,24.55600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa").addGeometry(Part.LineSegment(App.Vector(52.47934000000000,24.55600000000000,0.00000000000000),App.Vector(61.45959000000000,33.53626000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa").addGeometry(Part.LineSegment(App.Vector(34.51883000000000,60.47703000000000,0.00000000000000),App.Vector(61.45959000000000,33.53626000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa").addGeometry(Part.LineSegment(App.Vector(25.53857000000000,51.49677000000000,0.00000000000000),App.Vector(34.51883000000000,60.47703000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fr7Oe9GqAXDwTSV_0").newObject("PartDesign::Pad","Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa")
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").Length = 7.62
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3OtuxLEhgHEzi7_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").Type = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3OtuxLEhgHEzi7_1_FyVNxXVscLDWI8L_1_JNa").Offset = 0
App.ActiveDocument.recompute()

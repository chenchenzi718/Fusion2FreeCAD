import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00782073")
App.ActiveDocument.addObject("PartDesign::Body","Body_FmmdFLaryPg9EEs_0")
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").Label = "Body_FmmdFLaryPg9EEs_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Plane", "plane_Sketch_FmmdFLaryPg9EEs_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmmdFLaryPg9EEs_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("Sketcher::SketchObject","Sketch_FmmdFLaryPg9EEs_0_JGC")
App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmmdFLaryPg9EEs_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(101.59999999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC").addGeometry(Part.LineSegment(App.Vector(101.59999999999999,0.00000000000000,0.00000000000000),App.Vector(101.59999999999999,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,31.75000000000000,0.00000000000000),App.Vector(101.59999999999999,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Pad","Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC")
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC")
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmmdFLaryPg9EEs_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmmdFLaryPg9EEs_0_FcJt7drUh2bRL3E_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Plane", "plane_Sketch_F3pED6RLg6rl70L_1_JJC")
origin = App.Vector(50.80000000000000,15.87500000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3pED6RLg6rl70L_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("Sketcher::SketchObject","Sketch_F3pED6RLg6rl70L_1_JJC")
App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3pED6RLg6rl70L_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC").addGeometry(Part.LineSegment(App.Vector(-33.96875000000000,6.35000000000000,0.00000000000000),App.Vector(-33.96875000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-30.00000000000000,-6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),3.96875000000000),3.14159265358979,-0.0),False)

App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC").addGeometry(Part.LineSegment(App.Vector(-26.03125000000000,6.35000000000000,0.00000000000000),App.Vector(-26.03125000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-30.00000000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),3.96875000000000),0.0,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Pocket","Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC")
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC")
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Plane", "plane_Sketch_F3pED6RLg6rl70L_1_JJG")
origin = App.Vector(50.80000000000000,15.87500000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3pED6RLg6rl70L_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("Sketcher::SketchObject","Sketch_F3pED6RLg6rl70L_1_JJG")
App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3pED6RLg6rl70L_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG").addGeometry(Part.LineSegment(App.Vector(26.03125000000001,6.35000000000000,0.00000000000000),App.Vector(26.03125000000001,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(30.00000000000000,-6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.96875000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG").addGeometry(Part.LineSegment(App.Vector(33.96875000000001,6.35000000000000,0.00000000000000),App.Vector(33.96875000000001,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(30.00000000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.96875000000000),0.0,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Pocket","Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG")
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG")
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Plane", "plane_Sketch_F3pED6RLg6rl70L_1_JJK")
origin = App.Vector(50.80000000000000,15.87500000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3pED6RLg6rl70L_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("Sketcher::SketchObject","Sketch_F3pED6RLg6rl70L_1_JJK")
App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3pED6RLg6rl70L_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK").addGeometry(Part.LineSegment(App.Vector(-3.96875000000000,6.35000000000000,0.00000000000000),App.Vector(-3.96875000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,-6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),3.96875000000000),3.14159265358979,-0.0),False)

App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK").addGeometry(Part.LineSegment(App.Vector(3.96875000000000,6.35000000000000,0.00000000000000),App.Vector(3.96875000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),3.96875000000000),0.0,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Pocket","Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK")
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK")
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3pED6RLg6rl70L_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3pED6RLg6rl70L_1_FQ4KauSMFFkNTvN_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Plane", "plane_Sketch_FEJaZyMMjYOiaOh_1_JPC")
origin = App.Vector(101.59999999999999,15.87500000000000,6.35000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEJaZyMMjYOiaOh_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("Sketcher::SketchObject","Sketch_FEJaZyMMjYOiaOh_1_JPC")
App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEJaZyMMjYOiaOh_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPC").addGeometry(Part.Circle(App.Vector(-9.52500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.70510000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Pocket","Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC")
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPC")
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Plane", "plane_Sketch_FEJaZyMMjYOiaOh_1_JPG")
origin = App.Vector(101.59999999999999,15.87500000000000,6.35000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEJaZyMMjYOiaOh_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("Sketcher::SketchObject","Sketch_FEJaZyMMjYOiaOh_1_JPG")
App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEJaZyMMjYOiaOh_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPG").addGeometry(Part.Circle(App.Vector(9.52500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.70510000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Pocket","Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG")
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPG")
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEJaZyMMjYOiaOh_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEJaZyMMjYOiaOh_1_FdVPEdkGQlEZWok_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Plane", "plane_Sketch_FKuEefaYiOZKnu8_1_JWC")
origin = App.Vector(0.00000000000000,15.87500000000000,6.35000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKuEefaYiOZKnu8_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("Sketcher::SketchObject","Sketch_FKuEefaYiOZKnu8_1_JWC")
App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKuEefaYiOZKnu8_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWC").addGeometry(Part.Circle(App.Vector(-9.52500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.70510000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Pocket","Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC")
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWC")
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Plane", "plane_Sketch_FKuEefaYiOZKnu8_1_JWG")
origin = App.Vector(0.00000000000000,15.87500000000000,6.35000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKuEefaYiOZKnu8_1_JWG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("Sketcher::SketchObject","Sketch_FKuEefaYiOZKnu8_1_JWG")
App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKuEefaYiOZKnu8_1_JWG"), [""])
App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWG").addGeometry(Part.Circle(App.Vector(9.52500000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.70510000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmmdFLaryPg9EEs_0").newObject("PartDesign::Pocket","Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG")
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").Profile = App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWG")
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKuEefaYiOZKnu8_1_JWG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").Type = 4
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKuEefaYiOZKnu8_1_FBUeM5SsBot0Mfu_1_JWG").Offset = 0
App.ActiveDocument.recompute()

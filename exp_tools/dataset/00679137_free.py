import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00679137")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fh6vxvfs31W87uN_0")
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").Label = "Body_Fh6vxvfs31W87uN_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Plane", "plane_Sketch_Fh6vxvfs31W87uN_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh6vxvfs31W87uN_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("Sketcher::SketchObject","Sketch_Fh6vxvfs31W87uN_0_JGC")
App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh6vxvfs31W87uN_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.45150000000000,-34.21945000000000,0.00000000000000),App.Vector(-1.45150000000000,-34.21945000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1.45150000000000,-34.21945000000000,0.00000000000000),App.Vector(-1.45150000000000,-99.21944999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.45150000000000,-99.21944999999999,0.00000000000000),App.Vector(-1.45150000000000,-99.21944999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.45150000000000,-34.21945000000000,0.00000000000000),App.Vector(-45.45150000000000,-99.21944999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Pad","Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC")
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC")
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").Length = 20.0
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh6vxvfs31W87uN_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh6vxvfs31W87uN_0_FIXxs8OCWZinJvh_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Plane", "plane_Sketch_F3IymhdywRClA3y_1_JJC")
origin = App.Vector(-23.45150000000000,-66.71944999999999,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3IymhdywRClA3y_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("Sketcher::SketchObject","Sketch_F3IymhdywRClA3y_1_JJC")
App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3IymhdywRClA3y_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-20.50000000000000,31.00000000000000,0.00000000000000),App.Vector(20.50000000000000,31.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC").addGeometry(Part.LineSegment(App.Vector(20.50000000000000,31.00000000000000,0.00000000000000),App.Vector(20.50000000000000,-31.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-20.50000000000000,-31.00000000000000,0.00000000000000),App.Vector(20.50000000000000,-31.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-20.50000000000000,31.00000000000000,0.00000000000000),App.Vector(-20.50000000000000,-31.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Pocket","Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC")
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC")
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").Length = 18.5
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3IymhdywRClA3y_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3IymhdywRClA3y_1_FtnA4mWCFBeEVVm_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Plane", "plane_Sketch_Feil6yYh68bx6bk_1_JNC")
origin = App.Vector(-23.45150000000000,-35.71945000000000,10.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Feil6yYh68bx6bk_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("Sketcher::SketchObject","Sketch_Feil6yYh68bx6bk_1_JNC")
App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Feil6yYh68bx6bk_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC").addGeometry(Part.LineSegment(App.Vector(-14.50000000000000,3.75000000000000,0.00000000000000),App.Vector(-12.50000000000000,3.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,3.75000000000000,0.00000000000000),App.Vector(-12.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC").addGeometry(Part.LineSegment(App.Vector(-14.50000000000000,-1.25000000000000,0.00000000000000),App.Vector(-12.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC").addGeometry(Part.LineSegment(App.Vector(-14.50000000000000,3.75000000000000,0.00000000000000),App.Vector(-14.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Pad","Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC")
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC")
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Plane", "plane_Sketch_Feil6yYh68bx6bk_1_JNG")
origin = App.Vector(-23.45150000000000,-35.71945000000000,10.75000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Feil6yYh68bx6bk_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("Sketcher::SketchObject","Sketch_Feil6yYh68bx6bk_1_JNG")
App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Feil6yYh68bx6bk_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,3.75000000000000,0.00000000000000),App.Vector(14.50000000000000,3.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG").addGeometry(Part.LineSegment(App.Vector(14.50000000000000,3.75000000000000,0.00000000000000),App.Vector(14.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,-1.25000000000000,0.00000000000000),App.Vector(14.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,3.75000000000000,0.00000000000000),App.Vector(12.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Pad","Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG")
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG")
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").Length = 5.0
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Feil6yYh68bx6bk_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Feil6yYh68bx6bk_1_FvMLBod9lQtN65c_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Plane", "plane_Sketch_FHtLApwKRu7C1ox_1_JRC")
origin = App.Vector(-37.95150000000000,-36.97695000000000,11.98500000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHtLApwKRu7C1ox_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("Sketcher::SketchObject","Sketch_FHtLApwKRu7C1ox_1_JRC")
App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHtLApwKRu7C1ox_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC").addGeometry(Part.LineSegment(App.Vector(-1.25750000000000,-2.48500000000000,0.00000000000000),App.Vector(1.24250000000000,2.51500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC").addGeometry(Part.LineSegment(App.Vector(3.74250000000000,2.51500000000000,0.00000000000000),App.Vector(1.24250000000000,2.51500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC").addGeometry(Part.LineSegment(App.Vector(3.74250000000000,2.51500000000000,0.00000000000000),App.Vector(3.74250000000000,-2.48500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC").addGeometry(Part.LineSegment(App.Vector(3.74250000000000,-2.48500000000000,0.00000000000000),App.Vector(-1.25750000000000,-2.48500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Pocket","Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC")
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC")
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHtLApwKRu7C1ox_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHtLApwKRu7C1ox_1_FR1A8Yr0vCtDDkG_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Plane", "plane_Sketch_FIh6tZayIb14NxC_1_JVC")
origin = App.Vector(-23.45150000000000,-97.71944999999999,10.75000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIh6tZayIb14NxC_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("Sketcher::SketchObject","Sketch_FIh6tZayIb14NxC_1_JVC")
App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIh6tZayIb14NxC_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,3.75000000000000,0.00000000000000),App.Vector(14.50000000000000,3.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC").addGeometry(Part.LineSegment(App.Vector(14.50000000000000,3.75000000000000,0.00000000000000),App.Vector(14.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,-1.25000000000000,0.00000000000000),App.Vector(14.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,3.75000000000000,0.00000000000000),App.Vector(12.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Pad","Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC")
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC")
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Plane", "plane_Sketch_FIh6tZayIb14NxC_1_JVG")
origin = App.Vector(-23.45150000000000,-97.71944999999999,10.75000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIh6tZayIb14NxC_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("Sketcher::SketchObject","Sketch_FIh6tZayIb14NxC_1_JVG")
App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIh6tZayIb14NxC_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG").addGeometry(Part.LineSegment(App.Vector(-14.50000000000000,3.75000000000000,0.00000000000000),App.Vector(-12.50000000000000,3.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,3.75000000000000,0.00000000000000),App.Vector(-12.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG").addGeometry(Part.LineSegment(App.Vector(-14.50000000000000,-1.25000000000000,0.00000000000000),App.Vector(-12.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG").addGeometry(Part.LineSegment(App.Vector(-14.50000000000000,3.75000000000000,0.00000000000000),App.Vector(-14.50000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Pad","Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG")
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG")
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").Length = 5.0
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIh6tZayIb14NxC_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIh6tZayIb14NxC_1_FSAwKX703FYBHNO_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Plane", "plane_Sketch_FO543YJDSl3t9bt_1_JZC")
origin = App.Vector(-8.95150000000000,-96.46195000000000,11.98500000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FO543YJDSl3t9bt_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("Sketcher::SketchObject","Sketch_FO543YJDSl3t9bt_1_JZC")
App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FO543YJDSl3t9bt_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC").addGeometry(Part.LineSegment(App.Vector(-1.25749999999999,-2.48500000000000,0.00000000000000),App.Vector(1.24250000000001,2.51500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC").addGeometry(Part.LineSegment(App.Vector(3.74250000000001,2.51500000000000,0.00000000000000),App.Vector(1.24250000000001,2.51500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC").addGeometry(Part.LineSegment(App.Vector(3.74250000000001,2.51500000000000,0.00000000000000),App.Vector(3.74250000000001,-2.48500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC").addGeometry(Part.LineSegment(App.Vector(3.74250000000001,-2.48500000000000,0.00000000000000),App.Vector(-1.25749999999999,-2.48500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fh6vxvfs31W87uN_0").newObject("PartDesign::Pocket","Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC")
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC")
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FO543YJDSl3t9bt_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FO543YJDSl3t9bt_1_F3BpXxObs6AH8Ji_1_JZC").Offset = 0
App.ActiveDocument.recompute()

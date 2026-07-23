import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00948571")
App.ActiveDocument.addObject("PartDesign::Body","Body_FMagXdADTK2jLrl_0")
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").Label = "Body_FMagXdADTK2jLrl_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Plane", "plane_Sketch_FMagXdADTK2jLrl_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMagXdADTK2jLrl_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("Sketcher::SketchObject","Sketch_FMagXdADTK2jLrl_0_JGC")
App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMagXdADTK2jLrl_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC").addGeometry(Part.LineSegment(App.Vector(247.65000000000001,244.47499999999999,0.00000000000000),App.Vector(-247.65000000000001,244.47499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC").addGeometry(Part.LineSegment(App.Vector(-247.65000000000001,244.47499999999999,0.00000000000000),App.Vector(-247.65000000000001,-244.47499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC").addGeometry(Part.LineSegment(App.Vector(247.65000000000001,-244.47499999999999,0.00000000000000),App.Vector(-247.65000000000001,-244.47499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC").addGeometry(Part.LineSegment(App.Vector(247.65000000000001,244.47499999999999,0.00000000000000),App.Vector(247.65000000000001,-244.47499999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Pad","Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC")
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC")
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").Length = 215.9
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMagXdADTK2jLrl_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FMagXdADTK2jLrl_0_FOxmq5Y2LJP09Ai_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Plane", "plane_Sketch_Fu6x3kBcA5JkL0O_1_JJC")
origin = App.Vector(-0.00000000000000,-107.95000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu6x3kBcA5JkL0O_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("Sketcher::SketchObject","Sketch_Fu6x3kBcA5JkL0O_1_JJC")
App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu6x3kBcA5JkL0O_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC").addGeometry(Part.LineSegment(App.Vector(-203.19999999999999,180.97499999999999,0.00000000000000),App.Vector(50.80000000000000,180.97499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC").addGeometry(Part.LineSegment(App.Vector(50.80000000000000,180.97499999999999,0.00000000000000),App.Vector(50.80000000000000,-206.37500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC").addGeometry(Part.LineSegment(App.Vector(-203.19999999999999,-206.37500000000000,0.00000000000000),App.Vector(50.80000000000000,-206.37500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC").addGeometry(Part.LineSegment(App.Vector(-203.19999999999999,180.97499999999999,0.00000000000000),App.Vector(-203.19999999999999,-206.37500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Pocket","Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC")
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC")
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu6x3kBcA5JkL0O_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu6x3kBcA5JkL0O_1_F0JRXZ6dMYmc9jf_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Plane", "plane_Sketch_FY7okrYmVSVzhVU_1_JNO")
origin = App.Vector(-0.00000000000000,0.00000000000000,-244.47499999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FY7okrYmVSVzhVU_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("Sketcher::SketchObject","Sketch_FY7okrYmVSVzhVU_1_JNO")
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FY7okrYmVSVzhVU_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO").addGeometry(Part.LineSegment(App.Vector(-228.59999999999999,105.41000000000000,0.00000000000000),App.Vector(-177.80000000000001,105.41000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO").addGeometry(Part.LineSegment(App.Vector(-177.80000000000001,105.41000000000000,0.00000000000000),App.Vector(-177.80000000000001,86.36000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO").addGeometry(Part.LineSegment(App.Vector(-228.59999999999999,86.36000000000000,0.00000000000000),App.Vector(-177.80000000000001,86.36000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO").addGeometry(Part.LineSegment(App.Vector(-228.59999999999999,105.41000000000000,0.00000000000000),App.Vector(-228.59999999999999,86.36000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Pad","Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO")
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO")
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Plane", "plane_Sketch_FY7okrYmVSVzhVU_1_JNK")
origin = App.Vector(-0.00000000000000,0.00000000000000,-244.47499999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FY7okrYmVSVzhVU_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("Sketcher::SketchObject","Sketch_FY7okrYmVSVzhVU_1_JNK")
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FY7okrYmVSVzhVU_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,105.41000000000000,0.00000000000000),App.Vector(203.19999999999999,105.41000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK").addGeometry(Part.LineSegment(App.Vector(203.19999999999999,105.41000000000000,0.00000000000000),App.Vector(203.19999999999999,86.36000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,86.36000000000000,0.00000000000000),App.Vector(203.19999999999999,86.36000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,105.41000000000000,0.00000000000000),App.Vector(152.40000000000001,86.36000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Pad","Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK")
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK")
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Plane", "plane_Sketch_FY7okrYmVSVzhVU_1_JNG")
origin = App.Vector(-0.00000000000000,0.00000000000000,-244.47499999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FY7okrYmVSVzhVU_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("Sketcher::SketchObject","Sketch_FY7okrYmVSVzhVU_1_JNG")
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FY7okrYmVSVzhVU_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,-86.99500000000000,0.00000000000000),App.Vector(203.19999999999999,-86.99500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG").addGeometry(Part.LineSegment(App.Vector(203.19999999999999,-86.99500000000000,0.00000000000000),App.Vector(203.19999999999999,-105.41000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,-105.41000000000000,0.00000000000000),App.Vector(203.19999999999999,-105.41000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,-86.99500000000000,0.00000000000000),App.Vector(152.40000000000001,-105.41000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Pad","Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG")
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG")
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Plane", "plane_Sketch_FY7okrYmVSVzhVU_1_JNC")
origin = App.Vector(-0.00000000000000,0.00000000000000,-244.47499999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FY7okrYmVSVzhVU_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("Sketcher::SketchObject","Sketch_FY7okrYmVSVzhVU_1_JNC")
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FY7okrYmVSVzhVU_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC").addGeometry(Part.LineSegment(App.Vector(-228.59999999999999,-86.36000000000000,0.00000000000000),App.Vector(-177.80000000000001,-86.36000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC").addGeometry(Part.LineSegment(App.Vector(-177.80000000000001,-86.36000000000000,0.00000000000000),App.Vector(-177.80000000000001,-105.41000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC").addGeometry(Part.LineSegment(App.Vector(-228.59999999999999,-105.41000000000000,0.00000000000000),App.Vector(-177.80000000000001,-105.41000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC").addGeometry(Part.LineSegment(App.Vector(-228.59999999999999,-86.36000000000000,0.00000000000000),App.Vector(-228.59999999999999,-105.41000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Pad","Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC")
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC")
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FY7okrYmVSVzhVU_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FY7okrYmVSVzhVU_1_F5vK17TE6v1ceHg_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Plane", "plane_Sketch_FTUhPAI9BV364ZS_1_JRG")
origin = App.Vector(-247.65000000000001,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTUhPAI9BV364ZS_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("Sketcher::SketchObject","Sketch_FTUhPAI9BV364ZS_1_JRG")
App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTUhPAI9BV364ZS_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG").addGeometry(Part.LineSegment(App.Vector(-54.36034000000000,-31.50821000000000,0.00000000000000),App.Vector(52.28284000000000,-31.50821000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG").addGeometry(Part.LineSegment(App.Vector(52.28284000000000,-31.50821000000000,0.00000000000000),App.Vector(52.28284000000000,-136.76642000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG").addGeometry(Part.LineSegment(App.Vector(-54.36034000000000,-136.76642000000001,0.00000000000000),App.Vector(52.28284000000000,-136.76642000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG").addGeometry(Part.LineSegment(App.Vector(-54.36034000000000,-31.50821000000000,0.00000000000000),App.Vector(-54.36034000000000,-136.76642000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Pocket","Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG")
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG")
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Plane", "plane_Sketch_FTUhPAI9BV364ZS_1_JRC")
origin = App.Vector(-247.65000000000001,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTUhPAI9BV364ZS_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("Sketcher::SketchObject","Sketch_FTUhPAI9BV364ZS_1_JRC")
App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTUhPAI9BV364ZS_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC").addGeometry(Part.LineSegment(App.Vector(-82.05988000000001,201.86032000000000,0.00000000000000),App.Vector(-34.27819000000000,201.86032000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC").addGeometry(Part.LineSegment(App.Vector(-34.27819000000000,201.86032000000000,0.00000000000000),App.Vector(-34.27819000000000,10.04108000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC").addGeometry(Part.LineSegment(App.Vector(-82.05988000000001,10.04108000000000,0.00000000000000),App.Vector(-34.27819000000000,10.04108000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC").addGeometry(Part.LineSegment(App.Vector(-82.05988000000001,201.86032000000000,0.00000000000000),App.Vector(-82.05988000000001,10.04108000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMagXdADTK2jLrl_0").newObject("PartDesign::Pocket","Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC")
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC")
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTUhPAI9BV364ZS_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTUhPAI9BV364ZS_1_FCsKag2AhpSYVI3_1_JRC").Offset = 0
App.ActiveDocument.recompute()

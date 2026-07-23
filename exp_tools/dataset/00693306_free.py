import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00693306")
App.ActiveDocument.addObject("PartDesign::Body","Body_FGdoIw22luOBmUn_0")
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").Label = "Body_FGdoIw22luOBmUn_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Plane", "plane_Sketch_FGdoIw22luOBmUn_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGdoIw22luOBmUn_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("Sketcher::SketchObject","Sketch_FGdoIw22luOBmUn_0_JGC")
App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGdoIw22luOBmUn_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,0.00000000000000,0.00000000000000),App.Vector(-62.50000000000000,67.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,67.00000000000000,0.00000000000000),App.Vector(62.50000000000000,67.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").addGeometry(Part.LineSegment(App.Vector(62.50000000000000,67.00000000000000,0.00000000000000),App.Vector(62.50000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").addGeometry(Part.LineSegment(App.Vector(62.50000000000000,0.00000000000000,0.00000000000000),App.Vector(64.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").addGeometry(Part.LineSegment(App.Vector(64.00000000000000,68.50000000000000,0.00000000000000),App.Vector(64.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").addGeometry(Part.LineSegment(App.Vector(64.00000000000000,68.50000000000000,0.00000000000000),App.Vector(-64.00000000000000,68.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-64.00000000000000,68.50000000000000,0.00000000000000),App.Vector(-64.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,0.00000000000000,0.00000000000000),App.Vector(-64.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Pad","Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC")
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC")
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").Length = 45.0
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGdoIw22luOBmUn_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGdoIw22luOBmUn_0_FpDg0VGsiq1qYRq_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Plane", "plane_Sketch_FiVNFyRPlEwe8ZN_1_JJC")
origin = App.Vector(-64.00000000000000,34.25000000000000,22.50000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiVNFyRPlEwe8ZN_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("Sketcher::SketchObject","Sketch_FiVNFyRPlEwe8ZN_1_JJC")
App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiVNFyRPlEwe8ZN_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC").addGeometry(Part.LineSegment(App.Vector(-28.47142999999999,17.10000000000000,0.00000000000000),App.Vector(-15.07143000000000,17.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.07143000000000,17.10000000000000,0.00000000000000),App.Vector(-15.07143000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC").addGeometry(Part.LineSegment(App.Vector(-28.47142999999999,-2.50000000000000,0.00000000000000),App.Vector(-15.07143000000000,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC").addGeometry(Part.LineSegment(App.Vector(-28.47142999999999,17.10000000000000,0.00000000000000),App.Vector(-28.47142999999999,-2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Pocket","Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC")
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC")
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").Length = 6.0
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiVNFyRPlEwe8ZN_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FiVNFyRPlEwe8ZN_1_FnbGM6R9UBcQ4S9_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Plane", "plane_Sketch_FORpktOPTQp7gXn_1_JNC")
origin = App.Vector(0.00000000000000,34.25000000000000,45.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FORpktOPTQp7gXn_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("Sketcher::SketchObject","Sketch_FORpktOPTQp7gXn_1_JNC")
App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FORpktOPTQp7gXn_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNC").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,32.75000000000000,0.00000000000000),App.Vector(-62.50000000000000,12.37194000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNC").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,12.37194000000000,0.00000000000000),App.Vector(-42.12194000000000,32.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNC").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,32.75000000000000,0.00000000000000),App.Vector(-42.12194000000000,32.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Pad","Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC")
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNC")
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").Length = 1.0
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Plane", "plane_Sketch_FORpktOPTQp7gXn_1_JNG")
origin = App.Vector(0.00000000000000,34.25000000000000,45.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FORpktOPTQp7gXn_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("Sketcher::SketchObject","Sketch_FORpktOPTQp7gXn_1_JNG")
App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FORpktOPTQp7gXn_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNG").addGeometry(Part.LineSegment(App.Vector(62.50000000000000,32.75000000000000,0.00000000000000),App.Vector(42.12194000000000,32.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNG").addGeometry(Part.LineSegment(App.Vector(42.12194000000000,32.75000000000000,0.00000000000000),App.Vector(62.50000000000000,12.37194000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNG").addGeometry(Part.LineSegment(App.Vector(62.50000000000000,32.75000000000000,0.00000000000000),App.Vector(62.50000000000000,12.37194000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Pad","Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG")
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNG")
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").Length = 1.0
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FORpktOPTQp7gXn_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").Type = 0
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FORpktOPTQp7gXn_1_FXFbfG32Zg5AJfX_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Plane", "plane_Sketch_FFqIeRk1D2StxHP_1_JTC")
origin = App.Vector(0.00000000000000,34.25000000000000,45.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFqIeRk1D2StxHP_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("Sketcher::SketchObject","Sketch_FFqIeRk1D2StxHP_1_JTC")
App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFqIeRk1D2StxHP_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC").addGeometry(Part.LineSegment(App.Vector(62.50000000000000,-34.25000000000000,0.00000000000000),App.Vector(62.97890000000000,-34.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC").addGeometry(Part.LineSegment(App.Vector(62.97890000000000,-29.67441000000000,0.00000000000000),App.Vector(62.97890000000000,-34.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC").addGeometry(Part.LineSegment(App.Vector(62.97890000000000,-29.67441000000000,0.00000000000000),App.Vector(62.50000000000000,-29.67441000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC").addGeometry(Part.LineSegment(App.Vector(62.50000000000000,-34.25000000000000,0.00000000000000),App.Vector(62.50000000000000,-29.67441000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Pad","Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC")
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC")
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").Length = 1.5
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").Type = 0
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Plane", "plane_Sketch_FFqIeRk1D2StxHP_1_JTG")
origin = App.Vector(0.00000000000000,34.25000000000000,45.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFqIeRk1D2StxHP_1_JTG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("Sketcher::SketchObject","Sketch_FFqIeRk1D2StxHP_1_JTG")
App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFqIeRk1D2StxHP_1_JTG"), [""])
App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,-34.25000000000000,0.00000000000000),App.Vector(-62.63066000000001,-34.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG").addGeometry(Part.LineSegment(App.Vector(-62.63066000000001,-29.67441000000000,0.00000000000000),App.Vector(-62.63066000000001,-34.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG").addGeometry(Part.LineSegment(App.Vector(-62.63066000000001,-29.67441000000000,0.00000000000000),App.Vector(-62.50000000000000,-29.67441000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,-34.25000000000000,0.00000000000000),App.Vector(-62.50000000000000,-29.67441000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Pad","Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG")
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").Profile = App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG")
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").Length = 1.5
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").Type = 0
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Plane", "plane_Sketch_FFqIeRk1D2StxHP_1_JTO")
origin = App.Vector(0.00000000000000,34.25000000000000,45.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFqIeRk1D2StxHP_1_JTO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("Sketcher::SketchObject","Sketch_FFqIeRk1D2StxHP_1_JTO")
App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFqIeRk1D2StxHP_1_JTO"), [""])
App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,-34.25000000000000,0.00000000000000),App.Vector(62.50000000000000,-34.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO").addGeometry(Part.LineSegment(App.Vector(62.50000000000000,-34.25000000000000,0.00000000000000),App.Vector(62.50000000000000,-29.67441000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,-29.67441000000000,0.00000000000000),App.Vector(62.50000000000000,-29.67441000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO").addGeometry(Part.LineSegment(App.Vector(-62.50000000000000,-34.25000000000000,0.00000000000000),App.Vector(-62.50000000000000,-29.67441000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Pad","Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO")
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").Profile = App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO")
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").Length = 1.5
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFqIeRk1D2StxHP_1_JTO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").Type = 0
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").Reversed = 1
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFqIeRk1D2StxHP_1_FLi0uyyrCKgqSYq_1_JTO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Plane", "plane_Sketch_F9reUaF7yynb6Kw_1_JXC")
origin = App.Vector(0.00000000000000,67.00000000000000,22.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9reUaF7yynb6Kw_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("Sketcher::SketchObject","Sketch_F9reUaF7yynb6Kw_1_JXC")
App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9reUaF7yynb6Kw_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC").addGeometry(Part.LineSegment(App.Vector(58.51284000000000,-22.50000000000000,0.00000000000000),App.Vector(60.50000000000000,-22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC").addGeometry(Part.LineSegment(App.Vector(60.50000000000000,-22.50000000000000,0.00000000000000),App.Vector(60.50000000000000,3.69655000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC").addGeometry(Part.LineSegment(App.Vector(60.50000000000000,3.69655000000000,0.00000000000000),App.Vector(58.51284000000000,3.69655000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC").addGeometry(Part.LineSegment(App.Vector(58.51284000000000,-22.50000000000000,0.00000000000000),App.Vector(58.51284000000000,3.69655000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Pad","Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC")
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC")
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").Length = 16.0
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9reUaF7yynb6Kw_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9reUaF7yynb6Kw_1_FgNJ3CPAVu3rg7k_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Plane", "plane_Sketch_F3vP1Z0yIpZSwZP_1_JRC")
origin = App.Vector(64.00000000000000,34.25000000000000,22.50000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3vP1Z0yIpZSwZP_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("Sketcher::SketchObject","Sketch_F3vP1Z0yIpZSwZP_1_JRC")
App.ActiveDocument.getObject("Sketch_F3vP1Z0yIpZSwZP_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3vP1Z0yIpZSwZP_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F3vP1Z0yIpZSwZP_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3vP1Z0yIpZSwZP_1_JRC").addGeometry(Part.Circle(App.Vector(24.25000000000000,-7.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3vP1Z0yIpZSwZP_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3vP1Z0yIpZSwZP_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FGdoIw22luOBmUn_0").newObject("PartDesign::Pocket","Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC")
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F3vP1Z0yIpZSwZP_1_JRC")
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").Length = 18.8
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3vP1Z0yIpZSwZP_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3vP1Z0yIpZSwZP_1_FBEDFEUjZ8LR83F_1_JRC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00529880")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fnt5PoRQouj3kR3_0")
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").Label = "Body_Fnt5PoRQouj3kR3_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Plane", "plane_Sketch_Fnt5PoRQouj3kR3_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fnt5PoRQouj3kR3_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("Sketcher::SketchObject","Sketch_Fnt5PoRQouj3kR3_0_JGC")
App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fnt5PoRQouj3kR3_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,-34.92500000000000,0.00000000000000),App.Vector(38.10000000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,-15.87500000000000,0.00000000000000),App.Vector(38.10000000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,-34.92500000000000,0.00000000000000),App.Vector(-38.10000000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,-34.92500000000000,0.00000000000000),App.Vector(-38.10000000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Pad","Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC")
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC")
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Plane", "plane_Sketch_Fnt5PoRQouj3kR3_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fnt5PoRQouj3kR3_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("Sketcher::SketchObject","Sketch_Fnt5PoRQouj3kR3_0_JGG")
App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fnt5PoRQouj3kR3_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,34.92500000000000,0.00000000000000),App.Vector(38.10000000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,-15.87500000000000,0.00000000000000),App.Vector(38.10000000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,34.92500000000000,0.00000000000000),App.Vector(-38.10000000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,34.92500000000000,0.00000000000000),App.Vector(-14.27480000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").addGeometry(Part.LineSegment(App.Vector(-14.27480000000000,34.92500000000000,0.00000000000000),App.Vector(-14.27480000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").addGeometry(Part.LineSegment(App.Vector(-14.27480000000000,6.35000000000000,0.00000000000000),App.Vector(14.30020000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").addGeometry(Part.LineSegment(App.Vector(14.30020000000000,34.92500000000000,0.00000000000000),App.Vector(14.30020000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,34.92500000000000,0.00000000000000),App.Vector(14.30020000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Pad","Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG")
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").Profile = App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG")
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fnt5PoRQouj3kR3_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").Type = 0
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fnt5PoRQouj3kR3_0_FXuf22JGDls2XTQ_1_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Plane", "plane_Sketch_FAwTDMcBwKZnXKF_2_JJC")
origin = App.Vector(0.00000000000000,3.17500000000000,-34.92500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAwTDMcBwKZnXKF_2_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("Sketcher::SketchObject","Sketch_FAwTDMcBwKZnXKF_2_JJC")
App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAwTDMcBwKZnXKF_2_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,-22.22500000000000,0.00000000000000),App.Vector(-38.10000000000000,-22.22500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,-22.22500000000000,0.00000000000000),App.Vector(-38.10000000000000,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,-47.62500000000000,0.00000000000000),App.Vector(38.10000000000000,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,-22.22500000000000,0.00000000000000),App.Vector(38.10000000000000,-47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Pad","Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC")
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").Profile = App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC")
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").Length = 19.05
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Plane", "plane_Sketch_FAwTDMcBwKZnXKF_2_JJG")
origin = App.Vector(0.00000000000000,3.17500000000000,-34.92500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAwTDMcBwKZnXKF_2_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("Sketcher::SketchObject","Sketch_FAwTDMcBwKZnXKF_2_JJG")
App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAwTDMcBwKZnXKF_2_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,3.17500000000000,0.00000000000000),App.Vector(-38.10000000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,3.17500000000000,0.00000000000000),App.Vector(-38.10000000000000,47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,47.62500000000000,0.00000000000000),App.Vector(38.10000000000000,47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,3.17500000000000,0.00000000000000),App.Vector(38.10000000000000,47.62500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Pad","Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG")
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").Profile = App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG")
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").Length = 19.05
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAwTDMcBwKZnXKF_2_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAwTDMcBwKZnXKF_2_F1fPoZUl2vaXSVn_2_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Plane", "plane_Sketch_FBexeYKHTWHLQZK_2_JNC")
origin = App.Vector(0.00000000000000,3.17500000000000,-34.92500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBexeYKHTWHLQZK_2_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("Sketcher::SketchObject","Sketch_FBexeYKHTWHLQZK_2_JNC")
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBexeYKHTWHLQZK_2_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNC").addGeometry(Part.Circle(App.Vector(-25.40000000000000,-34.92500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.69900000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Pocket","Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC")
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").Profile = App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNC")
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").Length = 19.05
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Plane", "plane_Sketch_FBexeYKHTWHLQZK_2_JNG")
origin = App.Vector(0.00000000000000,3.17500000000000,-34.92500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBexeYKHTWHLQZK_2_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("Sketcher::SketchObject","Sketch_FBexeYKHTWHLQZK_2_JNG")
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBexeYKHTWHLQZK_2_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNG").addGeometry(Part.Circle(App.Vector(-25.40000000000000,34.92500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.69900000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Pocket","Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG")
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").Profile = App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNG")
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").Length = 19.05
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Plane", "plane_Sketch_FBexeYKHTWHLQZK_2_JNK")
origin = App.Vector(0.00000000000000,3.17500000000000,-34.92500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBexeYKHTWHLQZK_2_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("Sketcher::SketchObject","Sketch_FBexeYKHTWHLQZK_2_JNK")
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBexeYKHTWHLQZK_2_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNK").addGeometry(Part.Circle(App.Vector(25.40000000000000,-34.92500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.69900000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Pocket","Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK")
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").Profile = App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNK")
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").Length = 19.05
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Plane", "plane_Sketch_FBexeYKHTWHLQZK_2_JNO")
origin = App.Vector(0.00000000000000,3.17500000000000,-34.92500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBexeYKHTWHLQZK_2_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("Sketcher::SketchObject","Sketch_FBexeYKHTWHLQZK_2_JNO")
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBexeYKHTWHLQZK_2_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNO").addGeometry(Part.Circle(App.Vector(25.40000000000000,34.92500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.69900000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fnt5PoRQouj3kR3_0").newObject("PartDesign::Pocket","Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO")
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").Profile = App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNO")
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").Length = 19.05
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBexeYKHTWHLQZK_2_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBexeYKHTWHLQZK_2_FTtt5be03svN903_2_JNO").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00657014")
App.ActiveDocument.addObject("PartDesign::Body","Body_FstOxlB0OP7luz5_0")
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").Label = "Body_FstOxlB0OP7luz5_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Plane", "plane_Sketch_FstOxlB0OP7luz5_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FstOxlB0OP7luz5_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("Sketcher::SketchObject","Sketch_FstOxlB0OP7luz5_0_JGC")
App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FstOxlB0OP7luz5_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-96.20034000000000,52.75098999999999,0.00000000000000),App.Vector(109.80231999999999,52.75098999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC").addGeometry(Part.LineSegment(App.Vector(109.80231999999999,52.75098999999999,0.00000000000000),App.Vector(109.80231999999999,-73.72968000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-96.20034000000000,-73.72968000000000,0.00000000000000),App.Vector(109.80231999999999,-73.72968000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC").addGeometry(Part.LineSegment(App.Vector(-96.20034000000000,52.75098999999999,0.00000000000000),App.Vector(-96.20034000000000,-73.72968000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Pad","Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC")
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC")
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FstOxlB0OP7luz5_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FstOxlB0OP7luz5_0_F93UQWruQ6Y5ZtV_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Plane", "plane_Sketch_FKilE3rGLZx7pyk_1_JJC")
origin = App.Vector(50.80000000000000,6.80099000000000,-10.48934000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKilE3rGLZx7pyk_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("Sketcher::SketchObject","Sketch_FKilE3rGLZx7pyk_1_JJC")
App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKilE3rGLZx7pyk_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC").addGeometry(Part.LineSegment(App.Vector(-79.20343999999999,28.07035000000000,0.00000000000000),App.Vector(-73.39627000000002,28.07035000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC").addGeometry(Part.LineSegment(App.Vector(-73.39627000000002,28.07035000000000,0.00000000000000),App.Vector(-73.39627000000002,21.94055000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC").addGeometry(Part.LineSegment(App.Vector(-79.20343999999999,21.94055000000000,0.00000000000000),App.Vector(-73.39627000000002,21.94055000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC").addGeometry(Part.LineSegment(App.Vector(-79.20343999999999,28.07035000000000,0.00000000000000),App.Vector(-79.20343999999999,21.94055000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Pad","Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC")
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC")
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").Length = 0.025400000000000002
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKilE3rGLZx7pyk_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKilE3rGLZx7pyk_1_FjaxzKgIFNfzEU0_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Plane", "plane_Sketch_FEr2ebIIy4xwtYQ_1_JNC")
origin = App.Vector(50.80000000000000,6.80099000000000,-10.48934000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEr2ebIIy4xwtYQ_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("Sketcher::SketchObject","Sketch_FEr2ebIIy4xwtYQ_1_JNC")
App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEr2ebIIy4xwtYQ_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC").addGeometry(Part.LineSegment(App.Vector(63.60178999999999,28.07035000000000,0.00000000000000),App.Vector(69.40023000000001,28.07035000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC").addGeometry(Part.LineSegment(App.Vector(69.40023000000001,28.07035000000000,0.00000000000000),App.Vector(69.40023000000001,22.45386000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC").addGeometry(Part.LineSegment(App.Vector(63.60178999999999,22.45386000000000,0.00000000000000),App.Vector(69.40023000000001,22.45386000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC").addGeometry(Part.LineSegment(App.Vector(63.60178999999999,28.07035000000000,0.00000000000000),App.Vector(63.60178999999999,22.45386000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Pad","Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC")
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC")
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").Length = 0.025400000000000002
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEr2ebIIy4xwtYQ_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEr2ebIIy4xwtYQ_1_FRgIBHs1o6xT5XB_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Plane", "plane_Sketch_F3EHUUc1sMG9yyn_1_JRC")
origin = App.Vector(50.80000000000000,6.80099000000000,-10.48934000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3EHUUc1sMG9yyn_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("Sketcher::SketchObject","Sketch_F3EHUUc1sMG9yyn_1_JRC")
App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3EHUUc1sMG9yyn_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC").addGeometry(Part.LineSegment(App.Vector(-1.26627000000000,-32.97566000000000,0.00000000000000),App.Vector(-6.80099000000000,-32.97566000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC").addGeometry(Part.LineSegment(App.Vector(-6.80099000000000,-32.97566000000000,0.00000000000000),App.Vector(-6.80099000000000,-26.59660000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC").addGeometry(Part.LineSegment(App.Vector(-1.26627000000000,-26.59660000000000,0.00000000000000),App.Vector(-6.80099000000000,-26.59660000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC").addGeometry(Part.LineSegment(App.Vector(-1.26627000000000,-32.97566000000000,0.00000000000000),App.Vector(-1.26627000000000,-26.59660000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Pad","Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC")
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC")
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").Length = 0.025400000000000002
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3EHUUc1sMG9yyn_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3EHUUc1sMG9yyn_1_FanUyfebSVRgKUl_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Plane", "plane_Sketch_Fad9dnh2y8ahoOH_1_JVC")
origin = App.Vector(25.40000000000000,-96.20034000000000,-10.48934000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fad9dnh2y8ahoOH_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("Sketcher::SketchObject","Sketch_Fad9dnh2y8ahoOH_1_JVC")
App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fad9dnh2y8ahoOH_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC").addGeometry(Part.LineSegment(App.Vector(-7.92031000000000,3.80129000000000,0.00000000000000),App.Vector(0.58131000000000,3.80129000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC").addGeometry(Part.LineSegment(App.Vector(0.58131000000000,3.80129000000000,0.00000000000000),App.Vector(0.58131000000000,-9.74577000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC").addGeometry(Part.LineSegment(App.Vector(-7.92031000000000,-9.74577000000000,0.00000000000000),App.Vector(0.58131000000000,-9.74577000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC").addGeometry(Part.LineSegment(App.Vector(-7.92031000000000,3.80129000000000,0.00000000000000),App.Vector(-7.92031000000000,-9.74577000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Pad","Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC")
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC")
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").Length = 2.54e-19
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fad9dnh2y8ahoOH_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fad9dnh2y8ahoOH_1_FHtxwbYZme7Tr0f_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Plane", "plane_Sketch_FLSrXAN5qfCmyVG_1_JXC")
origin = App.Vector(25.40000000000000,-96.20034000000000,-10.48934000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLSrXAN5qfCmyVG_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("Sketcher::SketchObject","Sketch_FLSrXAN5qfCmyVG_1_JXC")
App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLSrXAN5qfCmyVG_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC").addGeometry(Part.LineSegment(App.Vector(-5.94680000000000,1.76225000000000,0.00000000000000),App.Vector(-13.73448000000000,1.76225000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC").addGeometry(Part.LineSegment(App.Vector(-13.73448000000000,1.76225000000000,0.00000000000000),App.Vector(-13.73448000000000,10.48934000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC").addGeometry(Part.LineSegment(App.Vector(-5.94680000000000,10.48934000000000,0.00000000000000),App.Vector(-13.73448000000000,10.48934000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC").addGeometry(Part.LineSegment(App.Vector(-5.94680000000000,1.76225000000000,0.00000000000000),App.Vector(-5.94680000000000,10.48934000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Pad","Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC")
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC")
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").Length = 0.025400000000000002
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLSrXAN5qfCmyVG_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLSrXAN5qfCmyVG_1_FFIabZHwIYCuR9f_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Plane", "plane_Sketch_FHtCsVS4umyx3yx_1_JbC")
origin = App.Vector(25.40000000000000,109.80231999999999,-10.48934000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHtCsVS4umyx3yx_1_JbC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("Sketcher::SketchObject","Sketch_FHtCsVS4umyx3yx_1_JbC")
App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHtCsVS4umyx3yx_1_JbC"), [""])
App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC").addGeometry(Part.LineSegment(App.Vector(1.16539000000000,10.48934000000000,0.00000000000000),App.Vector(10.28115000000000,10.48934000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC").addGeometry(Part.LineSegment(App.Vector(10.28115000000000,10.48934000000000,0.00000000000000),App.Vector(10.28115000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC").addGeometry(Part.LineSegment(App.Vector(1.16539000000000,0.00000000000000,0.00000000000000),App.Vector(10.28115000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC").addGeometry(Part.LineSegment(App.Vector(1.16539000000000,10.48934000000000,0.00000000000000),App.Vector(1.16539000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Pad","Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC")
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").Profile = App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC")
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").Length = 0.025400000000000002
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHtCsVS4umyx3yx_1_JbC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").Type = 4
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHtCsVS4umyx3yx_1_FNfgTv4FUZlmBkm_1_JbC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Plane", "plane_Sketch_Fm0dWN2D4fKGohn_1_JfC")
origin = App.Vector(25.40000000000000,6.80099000000000,-73.72968000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fm0dWN2D4fKGohn_1_JfC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("Sketcher::SketchObject","Sketch_Fm0dWN2D4fKGohn_1_JfC")
App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fm0dWN2D4fKGohn_1_JfC"), [""])
App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC").addGeometry(Part.LineSegment(App.Vector(-4.68041000000000,48.63403000000000,0.00000000000000),App.Vector(4.91603000000000,48.63403000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC").addGeometry(Part.LineSegment(App.Vector(4.91603000000000,48.63403000000000,0.00000000000000),App.Vector(4.91603000000000,39.03758999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC").addGeometry(Part.LineSegment(App.Vector(-4.68041000000000,39.03758999999999,0.00000000000000),App.Vector(4.91603000000000,39.03758999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC").addGeometry(Part.LineSegment(App.Vector(-4.68041000000000,48.63403000000000,0.00000000000000),App.Vector(-4.68041000000000,39.03758999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Pad","Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC")
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").Profile = App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC")
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").Length = 0.025400000000000002
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fm0dWN2D4fKGohn_1_JfC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").Type = 4
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fm0dWN2D4fKGohn_1_FSyfzXw9cS00orv_1_JfC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Plane", "plane_Sketch_FQ8abI0Wxd9XxSS_1_JjC")
origin = App.Vector(25.40000000000000,6.80099000000000,-73.72968000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQ8abI0Wxd9XxSS_1_JjC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("Sketcher::SketchObject","Sketch_FQ8abI0Wxd9XxSS_1_JjC")
App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQ8abI0Wxd9XxSS_1_JjC"), [""])
App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC").addGeometry(Part.LineSegment(App.Vector(-2.81791000000000,-43.07415000000000,0.00000000000000),App.Vector(6.00057000000000,-43.07415000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC").addGeometry(Part.LineSegment(App.Vector(6.00057000000000,-43.07415000000000,0.00000000000000),App.Vector(6.00057000000000,-53.44884000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC").addGeometry(Part.LineSegment(App.Vector(-2.81791000000000,-53.44884000000000,0.00000000000000),App.Vector(6.00057000000000,-53.44884000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC").addGeometry(Part.LineSegment(App.Vector(-2.81791000000000,-43.07415000000000,0.00000000000000),App.Vector(-2.81791000000000,-53.44884000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FstOxlB0OP7luz5_0").newObject("PartDesign::Pad","Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC")
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").Profile = App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC")
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").Length = 0.025400000000000002
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQ8abI0Wxd9XxSS_1_JjC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").Type = 4
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQ8abI0Wxd9XxSS_1_F8w4GHJtQVwzvVf_1_JjC").Offset = 0
App.ActiveDocument.recompute()

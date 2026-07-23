import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00714515")
App.ActiveDocument.addObject("PartDesign::Body","Body_FiBbzEp9fjSQm9H_0")
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").Label = "Body_FiBbzEp9fjSQm9H_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Plane", "plane_Sketch_FiBbzEp9fjSQm9H_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiBbzEp9fjSQm9H_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("Sketcher::SketchObject","Sketch_FiBbzEp9fjSQm9H_0_JGK")
App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiBbzEp9fjSQm9H_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(38.10000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,0.00000000000000,0.00000000000000),App.Vector(38.10000000000000,80.82825000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,134.70979000000000,0.00000000000000),App.Vector(38.10000000000000,80.82825000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,189.66895000000000,0.00000000000000),App.Vector(38.10000000000000,134.70979000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,189.66895000000000,0.00000000000000),App.Vector(38.10000000000000,189.66895000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,189.66895000000000,0.00000000000000),App.Vector(0.00000000000000,134.70979000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,80.82825000000001,0.00000000000000),App.Vector(0.00000000000000,134.70979000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,80.82825000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Pad","Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK")
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK")
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Plane", "plane_Sketch_FiBbzEp9fjSQm9H_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiBbzEp9fjSQm9H_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("Sketcher::SketchObject","Sketch_FiBbzEp9fjSQm9H_0_JGC")
App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiBbzEp9fjSQm9H_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,80.82825000000001,0.00000000000000),App.Vector(0.00000000000000,134.70979000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC").addGeometry(Part.LineSegment(App.Vector(-134.70979000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,134.70979000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC").addGeometry(Part.LineSegment(App.Vector(-80.82825000000001,0.00000000000000,0.00000000000000),App.Vector(-134.70979000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC").addGeometry(Part.LineSegment(App.Vector(-80.82825000000001,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,80.82825000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Pad","Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC")
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC")
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Plane", "plane_Sketch_FiBbzEp9fjSQm9H_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiBbzEp9fjSQm9H_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("Sketcher::SketchObject","Sketch_FiBbzEp9fjSQm9H_0_JGG")
App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiBbzEp9fjSQm9H_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,134.70979000000000,0.00000000000000),App.Vector(38.10000000000000,80.82825000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG").addGeometry(Part.LineSegment(App.Vector(118.92825000000001,0.00000000000000,0.00000000000000),App.Vector(38.10000000000000,80.82825000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG").addGeometry(Part.LineSegment(App.Vector(172.80978999999999,0.00000000000000,0.00000000000000),App.Vector(118.92825000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,134.70979000000000,0.00000000000000),App.Vector(172.80978999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Pad","Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG")
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG")
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiBbzEp9fjSQm9H_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiBbzEp9fjSQm9H_0_FZMGc0dEkpmQI1f_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Plane", "plane_Sketch_FpVvyNBqnUAlx8N_1_JJK")
origin = App.Vector(105.85902000000000,0.00000000000000,67.75902000000001)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpVvyNBqnUAlx8N_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("Sketcher::SketchObject","Sketch_FpVvyNBqnUAlx8N_1_JJK")
App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpVvyNBqnUAlx8N_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").addGeometry(Part.LineSegment(App.Vector(67.75902000000001,-67.75902000000001,0.00000000000000),App.Vector(70.93402000000000,-67.75902000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").addGeometry(Part.LineSegment(App.Vector(70.93402000000000,-67.75902000000001,0.00000000000000),App.Vector(70.93402000000000,121.90993000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").addGeometry(Part.LineSegment(App.Vector(67.75902000000001,121.90993000000000,0.00000000000000),App.Vector(70.93402000000000,121.90993000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").addGeometry(Part.LineSegment(App.Vector(67.75902000000001,121.90993000000000,0.00000000000000),App.Vector(67.75902000000001,66.95076999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").addGeometry(Part.LineSegment(App.Vector(67.75902000000001,66.95076999999999,0.00000000000000),App.Vector(67.75902000000001,13.06923000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").addGeometry(Part.LineSegment(App.Vector(67.75902000000001,-67.75902000000001,0.00000000000000),App.Vector(67.75902000000001,13.06923000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Pad","Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK")
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK")
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").Length = 34.925000000000004
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpVvyNBqnUAlx8N_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpVvyNBqnUAlx8N_1_FNQvWf6HwEDydlE_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Plane", "plane_Sketch_FTPubD0364HO880_1_JNC")
origin = App.Vector(105.85902000000000,0.00000000000000,67.75902000000001)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTPubD0364HO880_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("Sketcher::SketchObject","Sketch_FTPubD0364HO880_1_JNC")
App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTPubD0364HO880_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC").addGeometry(Part.LineSegment(App.Vector(-13.06923000000000,-67.75902000000001,0.00000000000000),App.Vector(67.75902000000001,13.06923000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC").addGeometry(Part.LineSegment(App.Vector(67.75902000000001,13.06923000000000,0.00000000000000),App.Vector(67.75902000000001,17.55935999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC").addGeometry(Part.LineSegment(App.Vector(67.75902000000001,17.55935999999999,0.00000000000000),App.Vector(-17.55935999999999,-67.75902000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC").addGeometry(Part.LineSegment(App.Vector(-13.06923000000000,-67.75902000000001,0.00000000000000),App.Vector(-17.55935999999999,-67.75902000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Pad","Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC")
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC")
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").Length = 34.925000000000004
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTPubD0364HO880_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTPubD0364HO880_1_FN3Jgwatli4WHnk_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Plane", "plane_Sketch_FcaykLBvmEyeM3a_1_JRC")
origin = App.Vector(-50.40130000000001,0.00000000000000,94.83447000000001)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcaykLBvmEyeM3a_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("Sketcher::SketchObject","Sketch_FcaykLBvmEyeM3a_1_JRC")
App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcaykLBvmEyeM3a_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC").addGeometry(Part.LineSegment(App.Vector(30.42695000000000,-94.83447000000001,0.00000000000000),App.Vector(-50.40130000000001,-14.00622000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC").addGeometry(Part.LineSegment(App.Vector(-50.40130000000001,-14.00622000000000,0.00000000000000),App.Vector(-50.40130000000001,-9.51609000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC").addGeometry(Part.LineSegment(App.Vector(-50.40130000000001,-9.51609000000001,0.00000000000000),App.Vector(34.91708000000000,-94.83447000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC").addGeometry(Part.LineSegment(App.Vector(30.42695000000000,-94.83447000000001,0.00000000000000),App.Vector(34.91708000000000,-94.83447000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Pad","Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC")
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC")
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").Length = 34.925000000000004
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcaykLBvmEyeM3a_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcaykLBvmEyeM3a_1_FZiaRwsxHNDfKgL_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Plane", "plane_Sketch_FgZRuN0QjDbDznP_1_JXC")
origin = App.Vector(19.05000000000000,-3.17500000000000,94.83447000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgZRuN0QjDbDznP_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("Sketcher::SketchObject","Sketch_FgZRuN0QjDbDznP_1_JXC")
App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgZRuN0QjDbDznP_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXC").addGeometry(Part.Circle(App.Vector(-38.10000000000000,-6.11545000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Pocket","Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC")
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXC")
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Plane", "plane_Sketch_FgZRuN0QjDbDznP_1_JXG")
origin = App.Vector(19.05000000000000,-3.17500000000000,94.83447000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgZRuN0QjDbDznP_1_JXG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("Sketcher::SketchObject","Sketch_FgZRuN0QjDbDznP_1_JXG")
App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgZRuN0QjDbDznP_1_JXG"), [""])
App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXG").addGeometry(Part.Circle(App.Vector(38.09999999999999,-6.11545000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Pocket","Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG")
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").Profile = App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXG")
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").Type = 4
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Plane", "plane_Sketch_FgZRuN0QjDbDznP_1_JXK")
origin = App.Vector(19.05000000000000,-3.17500000000000,94.83447000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgZRuN0QjDbDznP_1_JXK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("Sketcher::SketchObject","Sketch_FgZRuN0QjDbDznP_1_JXK")
App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgZRuN0QjDbDznP_1_JXK"), [""])
App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXK").addGeometry(Part.Circle(App.Vector(0.00000000000000,-6.11545000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.76250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FiBbzEp9fjSQm9H_0").newObject("PartDesign::Pocket","Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK")
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").Profile = App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXK")
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgZRuN0QjDbDznP_1_JXK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").Type = 4
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgZRuN0QjDbDznP_1_FPDI29Be4C4vqNQ_1_JXK").Offset = 0
App.ActiveDocument.recompute()

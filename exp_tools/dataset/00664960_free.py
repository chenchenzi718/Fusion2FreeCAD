import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00664960")
App.ActiveDocument.addObject("PartDesign::Body","Body_FFOYd3BJhjlxEtH_0")
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").Label = "Body_FFOYd3BJhjlxEtH_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Plane", "plane_Sketch_FFOYd3BJhjlxEtH_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFOYd3BJhjlxEtH_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("Sketcher::SketchObject","Sketch_FFOYd3BJhjlxEtH_0_JGC")
App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFOYd3BJhjlxEtH_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-342.89999999999998,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC").addGeometry(Part.LineSegment(App.Vector(-342.89999999999998,0.00000000000000,0.00000000000000),App.Vector(-342.89999999999998,266.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,266.69999999999999,0.00000000000000),App.Vector(-342.89999999999998,266.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,266.69999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Pad","Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC")
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC")
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFOYd3BJhjlxEtH_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFOYd3BJhjlxEtH_0_Foimgj8ytfTxtwQ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Plane", "plane_Sketch_FQCle5IuBrwm6Qw_1_JJC")
origin = App.Vector(-171.44999999999999,0.00000000000000,133.34999999999999)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQCle5IuBrwm6Qw_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("Sketcher::SketchObject","Sketch_FQCle5IuBrwm6Qw_1_JJC")
App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQCle5IuBrwm6Qw_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-133.34999999999999,0.00000000000000),App.Vector(114.30000000000001,-133.34999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC").addGeometry(Part.LineSegment(App.Vector(114.30000000000001,-133.34999999999999,0.00000000000000),App.Vector(114.30000000000001,82.55000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,82.55000000000001,0.00000000000000),App.Vector(114.30000000000001,82.55000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-133.34999999999999,0.00000000000000),App.Vector(0.00000000000000,82.55000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Pocket","Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC")
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC")
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Plane", "plane_Sketch_FQCle5IuBrwm6Qw_1_JJG")
origin = App.Vector(-171.44999999999999,0.00000000000000,133.34999999999999)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQCle5IuBrwm6Qw_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("Sketcher::SketchObject","Sketch_FQCle5IuBrwm6Qw_1_JJG")
App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQCle5IuBrwm6Qw_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-133.34999999999999,0.00000000000000),App.Vector(0.00000000000000,82.55000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,82.55000000000001,0.00000000000000),App.Vector(-114.29999999999998,82.55000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG").addGeometry(Part.LineSegment(App.Vector(-114.29999999999998,-133.34999999999999,0.00000000000000),App.Vector(-114.29999999999998,82.55000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-133.34999999999999,0.00000000000000),App.Vector(-114.29999999999998,-133.34999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Pocket","Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG")
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG")
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQCle5IuBrwm6Qw_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQCle5IuBrwm6Qw_1_FqDN2VeP9ZokkC0_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Plane", "plane_Sketch_FF2gePb3gfP7KQO_1_JNC")
origin = App.Vector(-285.75000000000000,-6.35000000000000,107.95000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FF2gePb3gfP7KQO_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("Sketcher::SketchObject","Sketch_FF2gePb3gfP7KQO_1_JNC")
App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FF2gePb3gfP7KQO_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,107.95000000000000,0.00000000000000),App.Vector(-6.35000000000000,107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,107.95000000000000,0.00000000000000),App.Vector(-6.35000000000000,-107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,-107.95000000000000,0.00000000000000),App.Vector(-6.35000000000000,-107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,-107.95000000000000,0.00000000000000),App.Vector(-19.05000000000000,107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Pad","Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC")
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC")
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").Length = 19.05
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FF2gePb3gfP7KQO_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FF2gePb3gfP7KQO_1_FCcFO5KfFRd9tIs_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Plane", "plane_Sketch_FgrjwDpg6jDGsLN_1_JRC")
origin = App.Vector(-57.15000000000000,-6.35000000000000,107.95000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgrjwDpg6jDGsLN_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("Sketcher::SketchObject","Sketch_FgrjwDpg6jDGsLN_1_JRC")
App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgrjwDpg6jDGsLN_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.05000000000000,107.95000000000000,0.00000000000000),App.Vector(6.35000000000000,107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC").addGeometry(Part.LineSegment(App.Vector(6.35000000000000,107.95000000000000,0.00000000000000),App.Vector(6.35000000000000,-107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.05000000000000,-107.95000000000000,0.00000000000000),App.Vector(6.35000000000000,-107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.05000000000000,-107.95000000000000,0.00000000000000),App.Vector(19.05000000000000,107.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Pad","Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC")
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC")
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").Length = 19.05
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgrjwDpg6jDGsLN_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgrjwDpg6jDGsLN_1_FSuKVVZxrRguizx_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Plane", "plane_Sketch_FeJfh5GZhFz9esN_1_JXC")
origin = App.Vector(-171.44999999999999,-25.40000000000000,133.34999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeJfh5GZhFz9esN_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("Sketcher::SketchObject","Sketch_FeJfh5GZhFz9esN_1_JXC")
App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeJfh5GZhFz9esN_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC").addGeometry(Part.LineSegment(App.Vector(-165.10000000000002,130.17500000000001,0.00000000000000),App.Vector(165.09999999999999,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC").addGeometry(Part.LineSegment(App.Vector(165.09999999999999,130.17500000000001,0.00000000000000),App.Vector(165.09999999999999,123.82499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC").addGeometry(Part.LineSegment(App.Vector(-165.10000000000002,123.82499999999999,0.00000000000000),App.Vector(165.09999999999999,123.82499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC").addGeometry(Part.LineSegment(App.Vector(-165.10000000000002,130.17500000000001,0.00000000000000),App.Vector(-165.10000000000002,123.82499999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Pocket","Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC")
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC")
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeJfh5GZhFz9esN_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeJfh5GZhFz9esN_1_FY03qw18pcf5rrD_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Plane", "plane_Sketch_Ftykxl8Sy9fGpCx_1_JbG")
origin = App.Vector(-171.44999999999999,-25.40000000000000,133.34999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftykxl8Sy9fGpCx_1_JbG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("Sketcher::SketchObject","Sketch_Ftykxl8Sy9fGpCx_1_JbG")
App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftykxl8Sy9fGpCx_1_JbG"), [""])
App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,88.90000000000001,0.00000000000000),App.Vector(-168.27500000000001,-107.94999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,-107.94999999999999,0.00000000000000),App.Vector(-161.92499999999998,-107.94999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG").addGeometry(Part.LineSegment(App.Vector(-161.92499999999998,-107.94999999999999,0.00000000000000),App.Vector(-161.92499999999998,88.90000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG").addGeometry(Part.LineSegment(App.Vector(-168.27500000000001,88.90000000000001,0.00000000000000),App.Vector(-161.92499999999998,88.90000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Pocket","Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG")
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").Profile = App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG")
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").Type = 4
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Plane", "plane_Sketch_Ftykxl8Sy9fGpCx_1_JbC")
origin = App.Vector(-171.44999999999999,-25.40000000000000,133.34999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftykxl8Sy9fGpCx_1_JbC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("Sketcher::SketchObject","Sketch_Ftykxl8Sy9fGpCx_1_JbC")
App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftykxl8Sy9fGpCx_1_JbC"), [""])
App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC").addGeometry(Part.LineSegment(App.Vector(168.27499999999998,88.90000000000001,0.00000000000000),App.Vector(161.92499999999998,88.90000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC").addGeometry(Part.LineSegment(App.Vector(161.92499999999998,88.90000000000001,0.00000000000000),App.Vector(161.92499999999998,-107.94999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC").addGeometry(Part.LineSegment(App.Vector(161.92499999999998,-107.94999999999999,0.00000000000000),App.Vector(168.27499999999998,-107.94999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC").addGeometry(Part.LineSegment(App.Vector(168.27499999999998,88.90000000000001,0.00000000000000),App.Vector(168.27499999999998,-107.94999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFOYd3BJhjlxEtH_0").newObject("PartDesign::Pocket","Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC")
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").Profile = App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC")
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftykxl8Sy9fGpCx_1_JbC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").Type = 4
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftykxl8Sy9fGpCx_1_FHpvgp3VDNfmWTT_1_JbC").Offset = 0
App.ActiveDocument.recompute()

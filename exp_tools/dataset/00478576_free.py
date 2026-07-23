import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00478576")
App.ActiveDocument.addObject("PartDesign::Body","Body_FlahRoAxJIO0Tb2_0")
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").Label = "Body_FlahRoAxJIO0Tb2_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Plane", "plane_Sketch_FlahRoAxJIO0Tb2_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlahRoAxJIO0Tb2_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("Sketcher::SketchObject","Sketch_FlahRoAxJIO0Tb2_0_JGC")
App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlahRoAxJIO0Tb2_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Pad","Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC")
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGC")
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").Length = 13.8
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Plane", "plane_Sketch_FlahRoAxJIO0Tb2_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlahRoAxJIO0Tb2_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("Sketcher::SketchObject","Sketch_FlahRoAxJIO0Tb2_0_JGG")
App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlahRoAxJIO0Tb2_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").addGeometry(Part.LineSegment(App.Vector(26.10000000000000,-10.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").addGeometry(Part.LineSegment(App.Vector(28.50000000000000,-12.40000000000000,0.00000000000000),App.Vector(26.10000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,-12.40000000000000,0.00000000000000),App.Vector(28.50000000000000,-12.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,0.00000000000000,0.00000000000000),App.Vector(31.50000000000000,-12.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,12.40000000000000,0.00000000000000),App.Vector(31.50000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").addGeometry(Part.LineSegment(App.Vector(28.50000000000000,12.40000000000000,0.00000000000000),App.Vector(31.50000000000000,12.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").addGeometry(Part.LineSegment(App.Vector(26.10000000000000,10.00000000000000,0.00000000000000),App.Vector(28.50000000000000,12.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,10.00000000000000,0.00000000000000),App.Vector(26.10000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Pad","Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG")
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG")
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").Length = 13.8
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlahRoAxJIO0Tb2_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").Type = 0
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").Midplane = 1
App.ActiveDocument.getObject("Extrude_FlahRoAxJIO0Tb2_0_FdSbUBIZXfEx6Dc_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Plane", "plane_Sketch_FN2xGIvWX7fyfzK_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FN2xGIvWX7fyfzK_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("Sketcher::SketchObject","Sketch_FN2xGIvWX7fyfzK_1_JJC")
App.ActiveDocument.getObject("Sketch_FN2xGIvWX7fyfzK_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FN2xGIvWX7fyfzK_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FN2xGIvWX7fyfzK_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FN2xGIvWX7fyfzK_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FN2xGIvWX7fyfzK_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FN2xGIvWX7fyfzK_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Pad","Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC")
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FN2xGIvWX7fyfzK_1_JJC")
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").Length = 16.6
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FN2xGIvWX7fyfzK_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FN2xGIvWX7fyfzK_1_F41Uccn8GVLwWLZ_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Plane", "plane_Sketch_Fr8gtQXSI9mE6rx_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fr8gtQXSI9mE6rx_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("Sketcher::SketchObject","Sketch_Fr8gtQXSI9mE6rx_1_JNC")
App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fr8gtQXSI9mE6rx_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,-11.25000000000000,0.00000000000000),App.Vector(45.00000000000000,-11.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,-11.25000000000000,0.00000000000000),App.Vector(45.00000000000000,11.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,11.25000000000000,0.00000000000000),App.Vector(45.00000000000000,11.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC").addGeometry(Part.LineSegment(App.Vector(31.50000000000000,-11.25000000000000,0.00000000000000),App.Vector(31.50000000000000,11.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Pad","Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC")
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC")
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").Length = 11.5
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fr8gtQXSI9mE6rx_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fr8gtQXSI9mE6rx_1_FQ2fv8OtsekkGbg_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Plane", "plane_Sketch_FTpJsmvRA75edYk_1_JRC")
origin = App.Vector(45.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FTpJsmvRA75edYk_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("Sketcher::SketchObject","Sketch_FTpJsmvRA75edYk_1_JRC")
App.ActiveDocument.getObject("Sketch_FTpJsmvRA75edYk_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FTpJsmvRA75edYk_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FTpJsmvRA75edYk_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FTpJsmvRA75edYk_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FTpJsmvRA75edYk_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FTpJsmvRA75edYk_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Pad","Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC")
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FTpJsmvRA75edYk_1_JRC")
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").Length = 0.5
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FTpJsmvRA75edYk_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FTpJsmvRA75edYk_1_FiWPBHZxIdxNwdH_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Plane", "plane_Sketch_FRJT1u5s0XhIuHl_1_JVC")
origin = App.Vector(45.50000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRJT1u5s0XhIuHl_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("Sketcher::SketchObject","Sketch_FRJT1u5s0XhIuHl_1_JVC")
App.ActiveDocument.getObject("Sketch_FRJT1u5s0XhIuHl_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRJT1u5s0XhIuHl_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FRJT1u5s0XhIuHl_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRJT1u5s0XhIuHl_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRJT1u5s0XhIuHl_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRJT1u5s0XhIuHl_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Pad","Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC")
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FRJT1u5s0XhIuHl_1_JVC")
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").Length = 4.500000000000001
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRJT1u5s0XhIuHl_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRJT1u5s0XhIuHl_1_FS3KpPVw5B6mFub_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Plane", "plane_Sketch_FRCSLkrBp5KVQZG_1_JZC")
origin = App.Vector(45.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRCSLkrBp5KVQZG_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("Sketcher::SketchObject","Sketch_FRCSLkrBp5KVQZG_1_JZC")
App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRCSLkrBp5KVQZG_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC").addGeometry(Part.LineSegment(App.Vector(-6.90000000000000,1.25000000000000,0.00000000000000),App.Vector(-6.60000000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC").addGeometry(Part.LineSegment(App.Vector(-6.60000000000000,1.25000000000000,0.00000000000000),App.Vector(-6.60000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC").addGeometry(Part.LineSegment(App.Vector(-6.90000000000000,-1.25000000000000,0.00000000000000),App.Vector(-6.60000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC").addGeometry(Part.LineSegment(App.Vector(-6.90000000000000,1.25000000000000,0.00000000000000),App.Vector(-6.90000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Pad","Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC")
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC")
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").Length = 4.0
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Plane", "plane_Sketch_FRCSLkrBp5KVQZG_1_JZG")
origin = App.Vector(45.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRCSLkrBp5KVQZG_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("Sketcher::SketchObject","Sketch_FRCSLkrBp5KVQZG_1_JZG")
App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRCSLkrBp5KVQZG_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG").addGeometry(Part.LineSegment(App.Vector(6.90000000000000,1.25000000000000,0.00000000000000),App.Vector(6.60000000000000,1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG").addGeometry(Part.LineSegment(App.Vector(6.60000000000000,1.25000000000000,0.00000000000000),App.Vector(6.60000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG").addGeometry(Part.LineSegment(App.Vector(6.90000000000000,-1.25000000000000,0.00000000000000),App.Vector(6.60000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG").addGeometry(Part.LineSegment(App.Vector(6.90000000000000,1.25000000000000,0.00000000000000),App.Vector(6.90000000000000,-1.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FlahRoAxJIO0Tb2_0").newObject("PartDesign::Pad","Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG")
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG")
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").Length = 4.0
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRCSLkrBp5KVQZG_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRCSLkrBp5KVQZG_1_FI95Y3CTiRHz7dt_1_JZG").Offset = 0
App.ActiveDocument.recompute()

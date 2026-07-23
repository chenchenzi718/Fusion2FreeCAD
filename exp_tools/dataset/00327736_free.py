import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00327736")
App.ActiveDocument.addObject("PartDesign::Body","Body_FwMdwQ5obfCTch3_0")
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").Label = "Body_FwMdwQ5obfCTch3_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Plane", "plane_Sketch_FwMdwQ5obfCTch3_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwMdwQ5obfCTch3_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("Sketcher::SketchObject","Sketch_FwMdwQ5obfCTch3_0_JGC")
App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwMdwQ5obfCTch3_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-10.25000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),11.25000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC").addGeometry(Part.LineSegment(App.Vector(-10.25000000000000,11.25000000000000,0.00000000000000),App.Vector(10.25000000000000,11.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(10.25000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),11.25000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC").addGeometry(Part.LineSegment(App.Vector(-10.25000000000000,-11.25000000000000,0.00000000000000),App.Vector(10.25000000000000,-11.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Pad","Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC")
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC")
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").Length = 92.0
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwMdwQ5obfCTch3_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwMdwQ5obfCTch3_0_F5dzqkHTbD7Tlj0_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Plane", "plane_Sketch_FLJTPQf0pSfHww7_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLJTPQf0pSfHww7_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("Sketcher::SketchObject","Sketch_FLJTPQf0pSfHww7_1_JJC")
App.ActiveDocument.getObject("Sketch_FLJTPQf0pSfHww7_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLJTPQf0pSfHww7_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FLJTPQf0pSfHww7_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLJTPQf0pSfHww7_1_JJC").addGeometry(Part.Circle(App.Vector(-10.25000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLJTPQf0pSfHww7_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLJTPQf0pSfHww7_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Pocket","Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC")
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FLJTPQf0pSfHww7_1_JJC")
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLJTPQf0pSfHww7_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLJTPQf0pSfHww7_1_FfaHAk24TODOVVI_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Plane", "plane_Sketch_FiXiqR1RsUz5plv_1_JNC")
origin = App.Vector(-10.25000000000000,5.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FiXiqR1RsUz5plv_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("Sketcher::SketchObject","Sketch_FiXiqR1RsUz5plv_1_JNC")
App.ActiveDocument.getObject("Sketch_FiXiqR1RsUz5plv_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FiXiqR1RsUz5plv_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FiXiqR1RsUz5plv_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FiXiqR1RsUz5plv_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FiXiqR1RsUz5plv_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FiXiqR1RsUz5plv_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Pad","Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC")
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FiXiqR1RsUz5plv_1_JNC")
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FiXiqR1RsUz5plv_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FiXiqR1RsUz5plv_1_F4ExpTEINCyDLO2_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Plane", "plane_Sketch_FnJEMcnQJqbSm02_1_JSC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnJEMcnQJqbSm02_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("Sketcher::SketchObject","Sketch_FnJEMcnQJqbSm02_1_JSC")
App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnJEMcnQJqbSm02_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC").addGeometry(Part.LineSegment(App.Vector(0.50000000000000,6.55000000000000,0.00000000000000),App.Vector(13.50000000000000,6.55000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC").addGeometry(Part.LineSegment(App.Vector(13.50000000000000,6.55000000000000,0.00000000000000),App.Vector(13.50000000000000,1.55000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC").addGeometry(Part.LineSegment(App.Vector(0.50000000000000,1.55000000000000,0.00000000000000),App.Vector(13.50000000000000,1.55000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC").addGeometry(Part.LineSegment(App.Vector(0.50000000000000,6.55000000000000,0.00000000000000),App.Vector(0.50000000000000,1.55000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Pocket","Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC")
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC")
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").Type = 4
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Plane", "plane_Sketch_FnJEMcnQJqbSm02_1_JSG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FnJEMcnQJqbSm02_1_JSG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("Sketcher::SketchObject","Sketch_FnJEMcnQJqbSm02_1_JSG")
App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FnJEMcnQJqbSm02_1_JSG"), [""])
App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").addGeometry(Part.LineSegment(App.Vector(2.75000000000000,-5.95000000000000,0.00000000000000),App.Vector(2.75000000000000,-3.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").addGeometry(Part.LineSegment(App.Vector(2.75000000000000,-3.95000000000000,0.00000000000000),App.Vector(4.25000000000000,-2.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").addGeometry(Part.LineSegment(App.Vector(4.25000000000000,-2.45000000000000,0.00000000000000),App.Vector(9.75000000000000,-2.45000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").addGeometry(Part.LineSegment(App.Vector(9.75000000000000,-2.45000000000000,0.00000000000000),App.Vector(11.25000000000000,-3.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").addGeometry(Part.LineSegment(App.Vector(11.25000000000000,-3.95000000000000,0.00000000000000),App.Vector(11.25000000000000,-5.95000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").addGeometry(Part.LineSegment(App.Vector(2.75000000000000,-5.95000000000000,0.00000000000000),App.Vector(11.25000000000000,-5.95000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Pocket","Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG")
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").Profile = App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG")
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FnJEMcnQJqbSm02_1_JSG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").Type = 4
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FnJEMcnQJqbSm02_1_FaTbN3p15HNjaNG_1_JSG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Plane", "plane_Sketch_Fvzq8AFnXuGUhZH_1_JWC")
origin = App.Vector(-0.00000000000000,46.00000000000000,11.25000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fvzq8AFnXuGUhZH_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("Sketcher::SketchObject","Sketch_Fvzq8AFnXuGUhZH_1_JWC")
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fvzq8AFnXuGUhZH_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWC").addGeometry(Part.Circle(App.Vector(-9.25000000000000,-26.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Pocket","Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC")
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWC")
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Plane", "plane_Sketch_Fvzq8AFnXuGUhZH_1_JWG")
origin = App.Vector(-0.00000000000000,46.00000000000000,11.25000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fvzq8AFnXuGUhZH_1_JWG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("Sketcher::SketchObject","Sketch_Fvzq8AFnXuGUhZH_1_JWG")
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fvzq8AFnXuGUhZH_1_JWG"), [""])
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWG").addGeometry(Part.Circle(App.Vector(-9.25000000000000,-29.33333000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Pocket","Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG")
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").Profile = App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWG")
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").Type = 4
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Plane", "plane_Sketch_Fvzq8AFnXuGUhZH_1_JWK")
origin = App.Vector(-0.00000000000000,46.00000000000000,11.25000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fvzq8AFnXuGUhZH_1_JWK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("Sketcher::SketchObject","Sketch_Fvzq8AFnXuGUhZH_1_JWK")
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fvzq8AFnXuGUhZH_1_JWK"), [""])
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWK").addGeometry(Part.Circle(App.Vector(-9.25000000000000,-32.66667000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Pocket","Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK")
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").Profile = App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWK")
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").Type = 4
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Plane", "plane_Sketch_Fvzq8AFnXuGUhZH_1_JWO")
origin = App.Vector(-0.00000000000000,46.00000000000000,11.25000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fvzq8AFnXuGUhZH_1_JWO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("Sketcher::SketchObject","Sketch_Fvzq8AFnXuGUhZH_1_JWO")
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fvzq8AFnXuGUhZH_1_JWO"), [""])
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWO").addGeometry(Part.Circle(App.Vector(-9.25000000000000,-36.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwMdwQ5obfCTch3_0").newObject("PartDesign::Pocket","Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO")
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").Profile = App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWO")
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fvzq8AFnXuGUhZH_1_JWO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").Type = 4
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fvzq8AFnXuGUhZH_1_FzlAloNvNUGVkLd_1_JWO").Offset = 0
App.ActiveDocument.recompute()

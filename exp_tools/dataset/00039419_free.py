import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00039419")
App.ActiveDocument.addObject("PartDesign::Body","Body_FBFawjTzComUAGp_0")
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").Label = "Body_FBFawjTzComUAGp_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_FBFawjTzComUAGp_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBFawjTzComUAGp_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_FBFawjTzComUAGp_0_JGC")
App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBFawjTzComUAGp_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").addGeometry(Part.LineSegment(App.Vector(-29.28500000000000,55.49900000000000,0.00000000000000),App.Vector(-29.28500000000000,-55.49900000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-22.93500000000000,-55.49900000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.35000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.93500000000000,-61.84900000000000,0.00000000000000),App.Vector(22.93500000000000,-61.84900000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(22.93500000000000,-55.49900000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.35000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").addGeometry(Part.LineSegment(App.Vector(29.28500000000000,-55.49900000000000,0.00000000000000),App.Vector(29.28500000000000,55.49900000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(22.93500000000000,55.49900000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.35000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").addGeometry(Part.LineSegment(App.Vector(22.93500000000000,61.84900000000000,0.00000000000000),App.Vector(-22.93500000000000,61.84900000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-22.93500000000000,55.49900000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.35000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pad","Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC")
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC")
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").Length = 7.62
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBFawjTzComUAGp_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBFawjTzComUAGp_0_Fx4874QMg3XcfvB_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_Fa81LtHpwRLbZKM_1_JJC")
origin = App.Vector(-11.88963000000000,52.75082000000000,7.62000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa81LtHpwRLbZKM_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_Fa81LtHpwRLbZKM_1_JJC")
App.ActiveDocument.getObject("Sketch_Fa81LtHpwRLbZKM_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa81LtHpwRLbZKM_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fa81LtHpwRLbZKM_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa81LtHpwRLbZKM_1_JJC").addGeometry(Part.Circle(App.Vector(11.88963000000000,-105.33212000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),4.57144000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa81LtHpwRLbZKM_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa81LtHpwRLbZKM_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pocket","Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC")
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fa81LtHpwRLbZKM_1_JJC")
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa81LtHpwRLbZKM_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa81LtHpwRLbZKM_1_FxNsMiWs6RMVmfn_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_FE9EvWQy1Kd9i5s_1_JLC")
origin = App.Vector(0.00000000000000,0.00000000000000,7.62000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FE9EvWQy1Kd9i5s_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_FE9EvWQy1Kd9i5s_1_JLC")
App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FE9EvWQy1Kd9i5s_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC").addGeometry(Part.LineSegment(App.Vector(-23.57574000000000,-40.27480000000000,0.00000000000000),App.Vector(22.42309000000000,-40.27480000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC").addGeometry(Part.LineSegment(App.Vector(22.42309000000000,-40.27480000000000,0.00000000000000),App.Vector(22.42309000000000,45.53780000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC").addGeometry(Part.LineSegment(App.Vector(22.42309000000000,45.53780000000000,0.00000000000000),App.Vector(-23.37390000000000,45.53780000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC").addGeometry(Part.LineSegment(App.Vector(-23.57574000000000,-40.27480000000000,0.00000000000000),App.Vector(-23.37390000000000,45.53780000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pocket","Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC")
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC")
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FE9EvWQy1Kd9i5s_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FE9EvWQy1Kd9i5s_1_FcLvXAqEMhBkLnZ_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_Ftjr65BINRwETqG_1_JRO")
origin = App.Vector(-11.88963000000000,52.75082000000000,7.62000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftjr65BINRwETqG_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_Ftjr65BINRwETqG_1_JRO")
App.ActiveDocument.getObject("Sketch_Ftjr65BINRwETqG_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftjr65BINRwETqG_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_Ftjr65BINRwETqG_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftjr65BINRwETqG_1_JRO").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.71598000000000),False)

App.ActiveDocument.getObject("Sketch_Ftjr65BINRwETqG_1_JRO").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.65552000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftjr65BINRwETqG_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftjr65BINRwETqG_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pocket","Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO")
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_Ftjr65BINRwETqG_1_JRO")
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftjr65BINRwETqG_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftjr65BINRwETqG_1_FTlbVOpgEkMDU2P_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_FjoGmeTJhS9MZ8z_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,7.62000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjoGmeTJhS9MZ8z_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_FjoGmeTJhS9MZ8z_1_JVC")
App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjoGmeTJhS9MZ8z_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC").addGeometry(Part.LineSegment(App.Vector(-5.71906000000000,53.65383000000000,0.00000000000000),App.Vector(7.67558000000000,53.65383000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC").addGeometry(Part.LineSegment(App.Vector(7.67558000000000,53.65383000000000,0.00000000000000),App.Vector(7.67558000000000,51.54681000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC").addGeometry(Part.LineSegment(App.Vector(7.67558000000000,51.54681000000000,0.00000000000000),App.Vector(-5.71906000000000,51.54681000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC").addGeometry(Part.LineSegment(App.Vector(-5.71906000000000,53.65383000000000,0.00000000000000),App.Vector(-5.71906000000000,51.54681000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pocket","Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC")
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC")
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjoGmeTJhS9MZ8z_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjoGmeTJhS9MZ8z_1_F1DxBAfUQfR0XRg_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_Fi001yDSncfiuUX_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,7.62000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fi001yDSncfiuUX_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_Fi001yDSncfiuUX_1_JZC")
App.ActiveDocument.getObject("Sketch_Fi001yDSncfiuUX_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fi001yDSncfiuUX_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_Fi001yDSncfiuUX_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fi001yDSncfiuUX_1_JZC").addGeometry(Part.Circle(App.Vector(0.00000000000000,58.77089000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.81228000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fi001yDSncfiuUX_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fi001yDSncfiuUX_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pocket","Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC")
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_Fi001yDSncfiuUX_1_JZC")
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fi001yDSncfiuUX_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fi001yDSncfiuUX_1_FYsvRU6vnfM2JF2_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_FcSc3LydK5m5fzk_1_JdC")
origin = App.Vector(-29.28500000000000,0.00000000000000,3.81000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcSc3LydK5m5fzk_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_FcSc3LydK5m5fzk_1_JdC")
App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcSc3LydK5m5fzk_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC").addGeometry(Part.LineSegment(App.Vector(-50.29150000000001,0.41663000000000,0.00000000000000),App.Vector(-43.05408000000000,0.41663000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC").addGeometry(Part.LineSegment(App.Vector(-43.05408000000000,0.41663000000000,0.00000000000000),App.Vector(-43.05408000000000,1.70651000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC").addGeometry(Part.LineSegment(App.Vector(-50.29150000000001,1.70651000000000,0.00000000000000),App.Vector(-43.05408000000000,1.70651000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC").addGeometry(Part.LineSegment(App.Vector(-50.29150000000001,0.41663000000000,0.00000000000000),App.Vector(-50.29150000000001,1.70651000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pad","Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC")
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC")
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcSc3LydK5m5fzk_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcSc3LydK5m5fzk_1_FEYf5tDS24Jzypn_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_F67Esx7rNCADdRJ_1_JhC")
origin = App.Vector(-29.28500000000000,0.00000000000000,3.81000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F67Esx7rNCADdRJ_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_F67Esx7rNCADdRJ_1_JhC")
App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F67Esx7rNCADdRJ_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhC").addGeometry(Part.Circle(App.Vector(-34.13048000000000,0.00822000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.91666000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pad","Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC")
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhC")
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_F67Esx7rNCADdRJ_1_JhG")
origin = App.Vector(-29.28500000000000,0.00000000000000,3.81000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F67Esx7rNCADdRJ_1_JhG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_F67Esx7rNCADdRJ_1_JhG")
App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F67Esx7rNCADdRJ_1_JhG"), [""])
App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhG").addGeometry(Part.Circle(App.Vector(-22.65057000000000,0.04762000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),1.96037000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pad","Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG")
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").Profile = App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhG")
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F67Esx7rNCADdRJ_1_JhG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").Type = 4
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F67Esx7rNCADdRJ_1_FrJExXMdrFO4UrC_1_JhG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Plane", "plane_Sketch_Fh2qjIuUgQvQCMQ_1_JlG")
origin = App.Vector(29.28500000000000,0.00000000000000,3.81000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fh2qjIuUgQvQCMQ_1_JlG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("Sketcher::SketchObject","Sketch_Fh2qjIuUgQvQCMQ_1_JlG")
App.ActiveDocument.getObject("Sketch_Fh2qjIuUgQvQCMQ_1_JlG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fh2qjIuUgQvQCMQ_1_JlG"), [""])
App.ActiveDocument.getObject("Sketch_Fh2qjIuUgQvQCMQ_1_JlG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fh2qjIuUgQvQCMQ_1_JlG").addGeometry(Part.Circle(App.Vector(-6.47819000000000,0.76773000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),0.32067000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fh2qjIuUgQvQCMQ_1_JlG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fh2qjIuUgQvQCMQ_1_JlG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FBFawjTzComUAGp_0").newObject("PartDesign::Pocket","Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG")
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").Profile = App.ActiveDocument.getObject("Sketch_Fh2qjIuUgQvQCMQ_1_JlG")
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fh2qjIuUgQvQCMQ_1_JlG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").Type = 0
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fh2qjIuUgQvQCMQ_1_FMeFbdWF8rpfoKE_1_JlG").Offset = 0
App.ActiveDocument.recompute()

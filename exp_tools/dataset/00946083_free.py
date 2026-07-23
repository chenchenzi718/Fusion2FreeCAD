import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00946083")
App.ActiveDocument.addObject("PartDesign::Body","Body_FbVSDd2SuBvkLWV_0")
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").Label = "Body_FbVSDd2SuBvkLWV_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Plane", "plane_Sketch_FbVSDd2SuBvkLWV_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbVSDd2SuBvkLWV_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("Sketcher::SketchObject","Sketch_FbVSDd2SuBvkLWV_0_JGC")
App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbVSDd2SuBvkLWV_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC").addGeometry(Part.LineSegment(App.Vector(-283.79032000000001,138.94153000000000,0.00000000000000),App.Vector(31.20968000000000,138.94153000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC").addGeometry(Part.LineSegment(App.Vector(31.20968000000000,138.94153000000000,0.00000000000000),App.Vector(31.20968000000000,-16.05847000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC").addGeometry(Part.LineSegment(App.Vector(-283.79032000000001,-16.05847000000000,0.00000000000000),App.Vector(31.20968000000000,-16.05847000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC").addGeometry(Part.LineSegment(App.Vector(-283.79032000000001,138.94153000000000,0.00000000000000),App.Vector(-283.79032000000001,-16.05847000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Pad","Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC")
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC")
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").Length = 105.0
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbVSDd2SuBvkLWV_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbVSDd2SuBvkLWV_0_FDHMbrvNiXsS9xS_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Plane", "plane_Sketch_FYvKXLsGBsFpn7b_1_JJC")
origin = App.Vector(-126.29032000000001,61.44153000000000,105.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYvKXLsGBsFpn7b_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("Sketcher::SketchObject","Sketch_FYvKXLsGBsFpn7b_1_JJC")
App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYvKXLsGBsFpn7b_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC").addGeometry(Part.LineSegment(App.Vector(143.50000000000003,16.49999999999999,0.00000000000000),App.Vector(25.50000000000001,16.49999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC").addGeometry(Part.LineSegment(App.Vector(25.50000000000001,16.49999999999999,0.00000000000000),App.Vector(25.50000000000001,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC").addGeometry(Part.LineSegment(App.Vector(143.50000000000003,-63.50000000000000,0.00000000000000),App.Vector(25.50000000000001,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC").addGeometry(Part.LineSegment(App.Vector(143.50000000000003,16.49999999999999,0.00000000000000),App.Vector(143.50000000000003,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Pocket","Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC")
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC")
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").Length = 70.0
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYvKXLsGBsFpn7b_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYvKXLsGBsFpn7b_1_FImgrOUftknu9kM_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Plane", "plane_Sketch_Fa8bvHZzOMlPQWc_1_JNC")
origin = App.Vector(-126.29032000000001,61.44153000000000,105.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fa8bvHZzOMlPQWc_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("Sketcher::SketchObject","Sketch_Fa8bvHZzOMlPQWc_1_JNC")
App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fa8bvHZzOMlPQWc_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC").addGeometry(Part.LineSegment(App.Vector(-143.49999999999997,44.44287000000000,0.00000000000000),App.Vector(-78.49999999999999,44.44287000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC").addGeometry(Part.LineSegment(App.Vector(-78.49999999999999,44.44287000000000,0.00000000000000),App.Vector(-78.49999999999999,-5.55713000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC").addGeometry(Part.LineSegment(App.Vector(-143.49999999999997,-5.55713000000000,0.00000000000000),App.Vector(-78.49999999999999,-5.55713000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC").addGeometry(Part.LineSegment(App.Vector(-143.49999999999997,44.44287000000000,0.00000000000000),App.Vector(-143.49999999999997,-5.55713000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Pocket","Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC")
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC")
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").Length = 57.0
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fa8bvHZzOMlPQWc_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fa8bvHZzOMlPQWc_1_FiLU2wpsp8QdfPC_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Plane", "plane_Sketch_FFerAbkprNQNavA_1_JRC")
origin = App.Vector(-126.29032000000001,61.44153000000000,105.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFerAbkprNQNavA_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("Sketcher::SketchObject","Sketch_FFerAbkprNQNavA_1_JRC")
App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFerAbkprNQNavA_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC").addGeometry(Part.LineSegment(App.Vector(-143.49999999999997,-48.50000000000000,0.00000000000000),App.Vector(6.50000000000001,-48.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC").addGeometry(Part.LineSegment(App.Vector(6.50000000000001,-48.50000000000000,0.00000000000000),App.Vector(6.50000000000001,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC").addGeometry(Part.LineSegment(App.Vector(-143.49999999999997,-63.50000000000000,0.00000000000000),App.Vector(6.50000000000001,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC").addGeometry(Part.LineSegment(App.Vector(-143.49999999999997,-48.50000000000000,0.00000000000000),App.Vector(-143.49999999999997,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Pocket","Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC")
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC")
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFerAbkprNQNavA_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFerAbkprNQNavA_1_Frakrei7rQ89bqd_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Plane", "plane_Sketch_F25Fz3uYt5K0cKX_1_JWC")
origin = App.Vector(-126.29032000000001,61.44153000000000,105.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F25Fz3uYt5K0cKX_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("Sketcher::SketchObject","Sketch_F25Fz3uYt5K0cKX_1_JWC")
App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F25Fz3uYt5K0cKX_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC").addGeometry(Part.LineSegment(App.Vector(-143.49999999999997,-22.50000000000000,0.00000000000000),App.Vector(6.50000000000001,-22.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC").addGeometry(Part.LineSegment(App.Vector(6.50000000000001,-22.50000000000000,0.00000000000000),App.Vector(6.50000000000001,-34.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC").addGeometry(Part.LineSegment(App.Vector(-143.49999999999997,-34.50000000000000,0.00000000000000),App.Vector(6.50000000000001,-34.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC").addGeometry(Part.LineSegment(App.Vector(-143.49999999999997,-22.50000000000000,0.00000000000000),App.Vector(-143.49999999999997,-34.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Pocket","Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC")
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC")
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").Length = 75.0
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F25Fz3uYt5K0cKX_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F25Fz3uYt5K0cKX_1_FRnPGLmOpc9UpNy_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Plane", "plane_Sketch_F432k74Xu5rHxw7_1_JbC")
origin = App.Vector(-126.29032000000001,61.44153000000000,105.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F432k74Xu5rHxw7_1_JbC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("Sketcher::SketchObject","Sketch_F432k74Xu5rHxw7_1_JbC")
App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F432k74Xu5rHxw7_1_JbC"), [""])
App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC").addGeometry(Part.LineSegment(App.Vector(6.50000000000001,-8.50000000000000,0.00000000000000),App.Vector(-48.49999999999999,-8.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC").addGeometry(Part.LineSegment(App.Vector(-48.49999999999999,-8.50000000000000,0.00000000000000),App.Vector(-48.49999999999999,19.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC").addGeometry(Part.LineSegment(App.Vector(6.50000000000001,19.50000000000000,0.00000000000000),App.Vector(-48.49999999999999,19.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC").addGeometry(Part.LineSegment(App.Vector(6.50000000000001,-8.50000000000000,0.00000000000000),App.Vector(6.50000000000001,19.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Pocket","Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC")
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").Profile = App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC")
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").Length = 55.0
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F432k74Xu5rHxw7_1_JbC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").Type = 4
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F432k74Xu5rHxw7_1_FP8654ajCIubwmr_1_JbC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Plane", "plane_Sketch_FmggwhrUXJvUHOc_1_JfC")
origin = App.Vector(-126.29032000000001,61.44153000000000,105.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmggwhrUXJvUHOc_1_JfC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("Sketcher::SketchObject","Sketch_FmggwhrUXJvUHOc_1_JfC")
App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmggwhrUXJvUHOc_1_JfC"), [""])
App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,63.50000000000000,0.00000000000000),App.Vector(6.50000000000001,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC").addGeometry(Part.LineSegment(App.Vector(6.50000000000001,63.50000000000000,0.00000000000000),App.Vector(6.50000000000001,33.49999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,33.49999999999999,0.00000000000000),App.Vector(6.50000000000001,33.49999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,63.50000000000000,0.00000000000000),App.Vector(-63.50000000000000,33.49999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Pocket","Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC")
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").Profile = App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC")
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmggwhrUXJvUHOc_1_JfC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").Type = 4
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmggwhrUXJvUHOc_1_FMoWZKqWLoAx9Fa_1_JfC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Plane", "plane_Sketch_FL4SVowSvRTCLt4_1_JjC")
origin = App.Vector(-126.29032000000001,61.44153000000000,105.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FL4SVowSvRTCLt4_1_JjC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("Sketcher::SketchObject","Sketch_FL4SVowSvRTCLt4_1_JjC")
App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FL4SVowSvRTCLt4_1_JjC"), [""])
App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC").addGeometry(Part.LineSegment(App.Vector(25.50000000000001,53.50000000000000,0.00000000000000),App.Vector(115.50000000000000,53.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC").addGeometry(Part.LineSegment(App.Vector(115.50000000000000,53.50000000000000,0.00000000000000),App.Vector(115.50000000000000,33.49999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC").addGeometry(Part.LineSegment(App.Vector(25.50000000000001,33.49999999999999,0.00000000000000),App.Vector(115.50000000000000,33.49999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC").addGeometry(Part.LineSegment(App.Vector(25.50000000000001,53.50000000000000,0.00000000000000),App.Vector(25.50000000000001,33.49999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FbVSDd2SuBvkLWV_0").newObject("PartDesign::Pocket","Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC")
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").Profile = App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC")
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").Length = 90.0
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FL4SVowSvRTCLt4_1_JjC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").Type = 4
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FL4SVowSvRTCLt4_1_FDPKMb6Ur1hlFIs_1_JjC").Offset = 0
App.ActiveDocument.recompute()

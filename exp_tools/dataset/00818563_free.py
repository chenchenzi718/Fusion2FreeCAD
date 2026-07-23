import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00818563")
App.ActiveDocument.addObject("PartDesign::Body","Body_FQIceFX989cyJpm_0")
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").Label = "Body_FQIceFX989cyJpm_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Plane", "plane_Sketch_FQIceFX989cyJpm_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQIceFX989cyJpm_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("Sketcher::SketchObject","Sketch_FQIceFX989cyJpm_0_JGC")
App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQIceFX989cyJpm_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-21.72897000000000,20.45041000000000,0.00000000000000),App.Vector(-21.72897000000000,-17.64959000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-21.72897000000000,-17.64959000000000,0.00000000000000),App.Vector(16.37103000000000,-17.64959000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.37103000000000,-17.64959000000000,0.00000000000000),App.Vector(16.37103000000000,-14.47459000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.37103000000000,-14.47459000000000,0.00000000000000),App.Vector(-18.55397000000000,-14.47459000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-18.55397000000000,-14.47459000000000,0.00000000000000),App.Vector(-18.55397000000000,20.45041000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-21.72897000000000,20.45041000000000,0.00000000000000),App.Vector(-18.55397000000000,20.45041000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Pad","Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC")
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC")
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").Length = 1835.1500000000003
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQIceFX989cyJpm_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQIceFX989cyJpm_0_FDXRaWuHepAI2Y9_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Plane", "plane_Sketch_FCTNYW6z02pmT1A_1_JJC")
origin = App.Vector(-21.72897000000000,-917.57500000000005,1.40041000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCTNYW6z02pmT1A_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("Sketcher::SketchObject","Sketch_FCTNYW6z02pmT1A_1_JJC")
App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCTNYW6z02pmT1A_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC").addGeometry(Part.LineSegment(App.Vector(1.98438000000001,19.05000000000000,0.00000000000000),App.Vector(1.98438000000001,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC").addGeometry(Part.LineSegment(App.Vector(1.98438000000001,5.55625000000000,0.00000000000000),App.Vector(-1.98437000000007,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC").addGeometry(Part.LineSegment(App.Vector(-1.98437000000007,5.55625000000000,0.00000000000000),App.Vector(-1.98437000000007,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC").addGeometry(Part.LineSegment(App.Vector(1.98438000000001,19.05000000000000,0.00000000000000),App.Vector(-1.98437000000007,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Pocket","Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC")
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC")
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Plane", "plane_Sketch_FCTNYW6z02pmT1A_1_JJG")
origin = App.Vector(-21.72897000000000,-917.57500000000005,1.40041000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCTNYW6z02pmT1A_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("Sketcher::SketchObject","Sketch_FCTNYW6z02pmT1A_1_JJG")
App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCTNYW6z02pmT1A_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG").addGeometry(Part.LineSegment(App.Vector(917.57500000000005,5.55625000000000,0.00000000000000),App.Vector(913.60624999999993,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG").addGeometry(Part.LineSegment(App.Vector(913.60624999999993,5.55625000000000,0.00000000000000),App.Vector(913.60624999999993,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG").addGeometry(Part.LineSegment(App.Vector(917.57500000000005,19.05000000000000,0.00000000000000),App.Vector(913.60624999999993,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG").addGeometry(Part.LineSegment(App.Vector(917.57500000000005,19.05000000000000,0.00000000000000),App.Vector(917.57500000000005,5.55625000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Pocket","Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG")
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG")
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCTNYW6z02pmT1A_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCTNYW6z02pmT1A_1_FvdVvyHoJudKnCA_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Plane", "plane_Sketch_FKui19rrRfD4GBi_1_JOC")
origin = App.Vector(-22.68147000000000,-918.05124999999998,212.47441000000001)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("Sketcher::SketchObject","Sketch_FKui19rrRfD4GBi_1_JOC")
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOC").addGeometry(Part.Circle(App.Vector(650.39874999999995,-204.72399999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.90500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Pocket","Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOC")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Plane", "plane_Sketch_FKui19rrRfD4GBi_1_JOG")
origin = App.Vector(-22.68147000000000,-918.05124999999998,212.47441000000001)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("Sketcher::SketchObject","Sketch_FKui19rrRfD4GBi_1_JOG")
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOG"), [""])
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOG").addGeometry(Part.Circle(App.Vector(332.89875000000001,-204.72399999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.90500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Pocket","Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").Profile = App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOG")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").Type = 4
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Plane", "plane_Sketch_FKui19rrRfD4GBi_1_JOK")
origin = App.Vector(-22.68147000000000,-918.05124999999998,212.47441000000001)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("Sketcher::SketchObject","Sketch_FKui19rrRfD4GBi_1_JOK")
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOK"), [""])
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOK").addGeometry(Part.Circle(App.Vector(15.39875000000002,-204.72399999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.90500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Pocket","Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").Profile = App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOK")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").Type = 4
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Plane", "plane_Sketch_FKui19rrRfD4GBi_1_JOO")
origin = App.Vector(-22.68147000000000,-918.05124999999998,212.47441000000001)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("Sketcher::SketchObject","Sketch_FKui19rrRfD4GBi_1_JOO")
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOO"), [""])
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOO").addGeometry(Part.Circle(App.Vector(-302.10124999999999,-204.72399999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.90500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Pocket","Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").Profile = App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOO")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").Type = 4
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Plane", "plane_Sketch_FKui19rrRfD4GBi_1_JOS")
origin = App.Vector(-22.68147000000000,-918.05124999999998,212.47441000000001)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("Sketcher::SketchObject","Sketch_FKui19rrRfD4GBi_1_JOS")
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKui19rrRfD4GBi_1_JOS"), [""])
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOS").addGeometry(Part.Circle(App.Vector(-619.60124999999994,-204.72399999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.90500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQIceFX989cyJpm_0").newObject("PartDesign::Pocket","Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").Profile = App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOS")
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKui19rrRfD4GBi_1_JOS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").Type = 4
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKui19rrRfD4GBi_1_F5UZOAhXOvlgI0Z_1_JOS").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00165833")
App.ActiveDocument.addObject("PartDesign::Body","Body_FHnfKEsTocJLpMm_0")
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").Label = "Body_FHnfKEsTocJLpMm_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Plane", "plane_Sketch_FHnfKEsTocJLpMm_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHnfKEsTocJLpMm_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("Sketcher::SketchObject","Sketch_FHnfKEsTocJLpMm_0_JGC")
App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHnfKEsTocJLpMm_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,16.00000000000000,0.00000000000000),App.Vector(-16.00000000000000,16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,16.00000000000000,0.00000000000000),App.Vector(-16.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,-16.00000000000000,0.00000000000000),App.Vector(-16.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,16.00000000000000,0.00000000000000),App.Vector(16.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Pad","Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC")
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC")
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").Length = 1.6
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHnfKEsTocJLpMm_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHnfKEsTocJLpMm_0_FWS9E53NCizbhJZ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Plane", "plane_Sketch_FpRkPkbV1WrCrLI_1_JJC")
origin = App.Vector(0.00000000000000,-1.60000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpRkPkbV1WrCrLI_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("Sketcher::SketchObject","Sketch_FpRkPkbV1WrCrLI_1_JJC")
App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpRkPkbV1WrCrLI_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,9.00000000000000,0.00000000000000),App.Vector(-12.50000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC").addGeometry(Part.LineSegment(App.Vector(-12.50000000000000,9.00000000000000,0.00000000000000),App.Vector(-12.50000000000000,-9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,-9.00000000000000,0.00000000000000),App.Vector(-12.50000000000000,-9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC").addGeometry(Part.LineSegment(App.Vector(12.50000000000000,9.00000000000000,0.00000000000000),App.Vector(12.50000000000000,-9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Pad","Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC")
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC")
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpRkPkbV1WrCrLI_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpRkPkbV1WrCrLI_1_FR3kywL7UPbv8EU_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Plane", "plane_Sketch_Fnz3eYNsCOVwqYT_1_JNC")
origin = App.Vector(0.00000000000000,-11.60000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fnz3eYNsCOVwqYT_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("Sketcher::SketchObject","Sketch_Fnz3eYNsCOVwqYT_1_JNC")
App.ActiveDocument.getObject("Sketch_Fnz3eYNsCOVwqYT_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fnz3eYNsCOVwqYT_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fnz3eYNsCOVwqYT_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fnz3eYNsCOVwqYT_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fnz3eYNsCOVwqYT_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fnz3eYNsCOVwqYT_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Pad","Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC")
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fnz3eYNsCOVwqYT_1_JNC")
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fnz3eYNsCOVwqYT_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fnz3eYNsCOVwqYT_1_FywB5vCekhJeWiM_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Plane", "plane_Sketch_FjnrfvyHhMylqnE_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjnrfvyHhMylqnE_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("Sketcher::SketchObject","Sketch_FjnrfvyHhMylqnE_1_JRC")
App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjnrfvyHhMylqnE_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,12.12000000000000,0.00000000000000),App.Vector(12.00000000000000,12.12000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC").addGeometry(Part.LineSegment(App.Vector(12.00000000000000,12.12000000000000,0.00000000000000),App.Vector(12.00000000000000,1.28000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,1.28000000000000,0.00000000000000),App.Vector(12.00000000000000,1.28000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,12.12000000000000,0.00000000000000),App.Vector(16.00000000000000,1.28000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Pad","Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC")
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC")
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Plane", "plane_Sketch_FjnrfvyHhMylqnE_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjnrfvyHhMylqnE_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("Sketcher::SketchObject","Sketch_FjnrfvyHhMylqnE_1_JRG")
App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjnrfvyHhMylqnE_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,-5.50000000000000,0.00000000000000),App.Vector(12.00000000000000,-5.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG").addGeometry(Part.LineSegment(App.Vector(12.00000000000000,-5.50000000000000,0.00000000000000),App.Vector(12.00000000000000,-11.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,-11.50000000000000,0.00000000000000),App.Vector(12.00000000000000,-11.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG").addGeometry(Part.LineSegment(App.Vector(16.00000000000000,-5.50000000000000,0.00000000000000),App.Vector(16.00000000000000,-11.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Pad","Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG")
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG")
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").Length = 5.0
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjnrfvyHhMylqnE_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjnrfvyHhMylqnE_1_FshnPzQPm3oLp70_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Plane", "plane_Sketch_FzGBbK6kGSGRKRe_1_JVC")
origin = App.Vector(0.00000000000000,-1.60000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzGBbK6kGSGRKRe_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("Sketcher::SketchObject","Sketch_FzGBbK6kGSGRKRe_1_JVC")
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzGBbK6kGSGRKRe_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVC").addGeometry(Part.Circle(App.Vector(14.00000000000000,14.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Pocket","Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC")
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVC")
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Plane", "plane_Sketch_FzGBbK6kGSGRKRe_1_JVG")
origin = App.Vector(0.00000000000000,-1.60000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzGBbK6kGSGRKRe_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("Sketcher::SketchObject","Sketch_FzGBbK6kGSGRKRe_1_JVG")
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzGBbK6kGSGRKRe_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVG").addGeometry(Part.Circle(App.Vector(14.00000000000000,-14.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Pocket","Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG")
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVG")
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Plane", "plane_Sketch_FzGBbK6kGSGRKRe_1_JVK")
origin = App.Vector(0.00000000000000,-1.60000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzGBbK6kGSGRKRe_1_JVK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("Sketcher::SketchObject","Sketch_FzGBbK6kGSGRKRe_1_JVK")
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzGBbK6kGSGRKRe_1_JVK"), [""])
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVK").addGeometry(Part.Circle(App.Vector(-14.00000000000000,-14.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Pocket","Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK")
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").Profile = App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVK")
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").Type = 4
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Plane", "plane_Sketch_FzGBbK6kGSGRKRe_1_JVO")
origin = App.Vector(0.00000000000000,-1.60000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzGBbK6kGSGRKRe_1_JVO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("Sketcher::SketchObject","Sketch_FzGBbK6kGSGRKRe_1_JVO")
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzGBbK6kGSGRKRe_1_JVO"), [""])
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVO").addGeometry(Part.Circle(App.Vector(-14.00000000000000,14.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHnfKEsTocJLpMm_0").newObject("PartDesign::Pocket","Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO")
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").Profile = App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVO")
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzGBbK6kGSGRKRe_1_JVO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").Type = 4
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzGBbK6kGSGRKRe_1_FQvZwBDTgS4SLfw_1_JVO").Offset = 0
App.ActiveDocument.recompute()

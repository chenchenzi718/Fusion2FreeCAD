import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00428733")
App.ActiveDocument.addObject("PartDesign::Body","Body_FgAckMPdBHyTfc0_0")
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").Label = "Body_FgAckMPdBHyTfc0_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Plane", "plane_Sketch_FgAckMPdBHyTfc0_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgAckMPdBHyTfc0_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("Sketcher::SketchObject","Sketch_FgAckMPdBHyTfc0_0_JGC")
App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgAckMPdBHyTfc0_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,38.10000000000000,0.00000000000000),App.Vector(-38.10000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,38.10000000000000,0.00000000000000),App.Vector(-38.10000000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,-38.10000000000000,0.00000000000000),App.Vector(-38.10000000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,38.10000000000000,0.00000000000000),App.Vector(38.10000000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Pad","Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC")
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC")
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").Length = 76.2
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgAckMPdBHyTfc0_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgAckMPdBHyTfc0_0_FzGDOi7a8cUT2iH_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Plane", "plane_Sketch_F4JUBQwpFdBQgOe_1_JLC")
origin = App.Vector(0.00000000000000,0.00000000000000,76.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4JUBQwpFdBQgOe_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("Sketcher::SketchObject","Sketch_F4JUBQwpFdBQgOe_1_JLC")
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4JUBQwpFdBQgOe_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,34.92500000000000,0.00000000000000),App.Vector(-34.92500000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,34.92500000000000,0.00000000000000),App.Vector(-34.92500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,3.17500000000000,0.00000000000000),App.Vector(-34.92500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,34.92500000000000,0.00000000000000),App.Vector(-3.17500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Pocket","Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC")
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC")
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").Length = 102.87
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FDKoMz8NETGc75S_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Plane", "plane_Sketch_F4JUBQwpFdBQgOe_1_JLG")
origin = App.Vector(0.00000000000000,0.00000000000000,76.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4JUBQwpFdBQgOe_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("Sketcher::SketchObject","Sketch_F4JUBQwpFdBQgOe_1_JLG")
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4JUBQwpFdBQgOe_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG").addGeometry(Part.LineSegment(App.Vector(34.92500000000000,34.92500000000000,0.00000000000000),App.Vector(3.17500000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,34.92500000000000,0.00000000000000),App.Vector(3.17500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG").addGeometry(Part.LineSegment(App.Vector(34.92500000000000,3.17500000000000,0.00000000000000),App.Vector(3.17500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG").addGeometry(Part.LineSegment(App.Vector(34.92500000000000,34.92500000000000,0.00000000000000),App.Vector(34.92500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Pocket","Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG")
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG")
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").Length = 134.874
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FVFDFywY4Ru7194_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Plane", "plane_Sketch_F4JUBQwpFdBQgOe_1_JLK")
origin = App.Vector(0.00000000000000,0.00000000000000,76.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4JUBQwpFdBQgOe_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("Sketcher::SketchObject","Sketch_F4JUBQwpFdBQgOe_1_JLK")
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4JUBQwpFdBQgOe_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,-3.17500000000000,0.00000000000000),App.Vector(-34.92500000000000,-3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,-3.17500000000000,0.00000000000000),App.Vector(-34.92500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,-34.92500000000000,0.00000000000000),App.Vector(-34.92500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,-3.17500000000000,0.00000000000000),App.Vector(-3.17500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Pocket","Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK")
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK")
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").Length = 137.922
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FhDEvBiTO6yaIj3_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Plane", "plane_Sketch_F4JUBQwpFdBQgOe_1_JLO")
origin = App.Vector(0.00000000000000,0.00000000000000,76.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4JUBQwpFdBQgOe_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("Sketcher::SketchObject","Sketch_F4JUBQwpFdBQgOe_1_JLO")
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4JUBQwpFdBQgOe_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO").addGeometry(Part.LineSegment(App.Vector(34.92500000000000,-3.17500000000000,0.00000000000000),App.Vector(3.17500000000000,-3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,-3.17500000000000,0.00000000000000),App.Vector(3.17500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO").addGeometry(Part.LineSegment(App.Vector(34.92500000000000,-34.92500000000000,0.00000000000000),App.Vector(3.17500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO").addGeometry(Part.LineSegment(App.Vector(34.92500000000000,-3.17500000000000,0.00000000000000),App.Vector(34.92500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Pocket","Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO")
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO")
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").Length = 121.41199999999999
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4JUBQwpFdBQgOe_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4JUBQwpFdBQgOe_1_FCg3kIVslPnXS8I_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Plane", "plane_Sketch_Fe6mTA5j1v9kl8O_1_JVC")
origin = App.Vector(38.10000000000000,0.00000000000000,38.10000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fe6mTA5j1v9kl8O_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("Sketcher::SketchObject","Sketch_Fe6mTA5j1v9kl8O_1_JVC")
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fe6mTA5j1v9kl8O_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,3.17500000000000,0.00000000000000),App.Vector(-3.17500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,3.17500000000000,0.00000000000000),App.Vector(-3.17500000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,34.92500000000000,0.00000000000000),App.Vector(-3.17500000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,3.17500000000000,0.00000000000000),App.Vector(-34.92500000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Pocket","Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC")
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC")
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").Length = 107.696
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Plane", "plane_Sketch_Fe6mTA5j1v9kl8O_1_JVG")
origin = App.Vector(38.10000000000000,0.00000000000000,38.10000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fe6mTA5j1v9kl8O_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("Sketcher::SketchObject","Sketch_Fe6mTA5j1v9kl8O_1_JVG")
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fe6mTA5j1v9kl8O_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,34.92500000000000,0.00000000000000),App.Vector(34.92500000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG").addGeometry(Part.LineSegment(App.Vector(34.92500000000000,34.92500000000000,0.00000000000000),App.Vector(34.92500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,3.17500000000000,0.00000000000000),App.Vector(34.92500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,34.92500000000000,0.00000000000000),App.Vector(3.17500000000000,3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Pocket","Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG")
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG")
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").Length = 107.696
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Plane", "plane_Sketch_Fe6mTA5j1v9kl8O_1_JVK")
origin = App.Vector(38.10000000000000,0.00000000000000,38.10000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fe6mTA5j1v9kl8O_1_JVK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("Sketcher::SketchObject","Sketch_Fe6mTA5j1v9kl8O_1_JVK")
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fe6mTA5j1v9kl8O_1_JVK"), [""])
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,-3.17500000000000,0.00000000000000),App.Vector(-3.17500000000000,-3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,-3.17500000000000,0.00000000000000),App.Vector(-3.17500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,-34.92500000000000,0.00000000000000),App.Vector(-3.17500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,-3.17500000000000,0.00000000000000),App.Vector(-34.92500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Pocket","Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK")
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").Profile = App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK")
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").Length = 107.696
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").Type = 4
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Plane", "plane_Sketch_Fe6mTA5j1v9kl8O_1_JVO")
origin = App.Vector(38.10000000000000,0.00000000000000,38.10000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fe6mTA5j1v9kl8O_1_JVO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("Sketcher::SketchObject","Sketch_Fe6mTA5j1v9kl8O_1_JVO")
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fe6mTA5j1v9kl8O_1_JVO"), [""])
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,-3.17500000000000,0.00000000000000),App.Vector(34.92500000000000,-3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO").addGeometry(Part.LineSegment(App.Vector(34.92500000000000,-3.17500000000000,0.00000000000000),App.Vector(34.92500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,-34.92500000000000,0.00000000000000),App.Vector(34.92500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,-3.17500000000000,0.00000000000000),App.Vector(3.17500000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgAckMPdBHyTfc0_0").newObject("PartDesign::Pocket","Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO")
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").Profile = App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO")
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").Length = 107.696
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fe6mTA5j1v9kl8O_1_JVO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").Type = 4
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fe6mTA5j1v9kl8O_1_FPEE2BzaBAuXYM5_1_JVO").Offset = 0
App.ActiveDocument.recompute()

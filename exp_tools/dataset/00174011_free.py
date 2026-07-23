import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00174011")
App.ActiveDocument.addObject("PartDesign::Body","Body_FQo69to2OfFRZ7x_0")
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").Label = "Body_FQo69to2OfFRZ7x_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_FQo69to2OfFRZ7x_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQo69to2OfFRZ7x_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_FQo69to2OfFRZ7x_0_JGC")
App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQo69to2OfFRZ7x_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.50000000000000,8.00000000000000,0.00000000000000),App.Vector(-45.50000000000000,8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.50000000000000,8.00000000000000,0.00000000000000),App.Vector(-45.50000000000000,-8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.50000000000000,-8.00000000000000,0.00000000000000),App.Vector(-45.50000000000000,-8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.50000000000000,8.00000000000000,0.00000000000000),App.Vector(45.50000000000000,-8.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pad","Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC")
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC")
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").Length = 70.0
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQo69to2OfFRZ7x_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQo69to2OfFRZ7x_0_FAUQvfFsK9IviZG_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_F0lr1GoikFSCcgo_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_F0lr1GoikFSCcgo_1_JJC")
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJC").addGeometry(Part.Circle(App.Vector(-28.95126000000000,-5.89864000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.45677000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pocket","Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJC")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").Length = 1.0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_F0lr1GoikFSCcgo_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_F0lr1GoikFSCcgo_1_JJG")
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJG").addGeometry(Part.Circle(App.Vector(-19.05950000000000,-5.89864000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.45677000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pocket","Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJG")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").Length = 1.0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_F0lr1GoikFSCcgo_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_F0lr1GoikFSCcgo_1_JJK")
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK").addGeometry(Part.LineSegment(App.Vector(21.03513000000000,5.04825000000000,0.00000000000000),App.Vector(31.71824000000000,5.04825000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK").addGeometry(Part.LineSegment(App.Vector(31.71824000000000,5.04825000000000,0.00000000000000),App.Vector(31.71824000000000,0.16831000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK").addGeometry(Part.LineSegment(App.Vector(21.03513000000000,0.16831000000000,0.00000000000000),App.Vector(31.71824000000000,0.16831000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK").addGeometry(Part.LineSegment(App.Vector(21.03513000000000,5.04825000000000,0.00000000000000),App.Vector(21.03513000000000,0.16831000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pocket","Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").Length = 1.0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_F0lr1GoikFSCcgo_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_F0lr1GoikFSCcgo_1_JJO")
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO").addGeometry(Part.LineSegment(App.Vector(2.04294000000000,-4.05217000000000,0.00000000000000),App.Vector(15.10007000000000,-4.05217000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO").addGeometry(Part.LineSegment(App.Vector(15.10007000000000,-4.05217000000000,0.00000000000000),App.Vector(15.10007000000000,-7.74510000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO").addGeometry(Part.LineSegment(App.Vector(2.04294000000000,-7.74510000000000,0.00000000000000),App.Vector(15.10007000000000,-7.74510000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO").addGeometry(Part.LineSegment(App.Vector(2.04294000000000,-4.05217000000000,0.00000000000000),App.Vector(2.04294000000000,-7.74510000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pocket","Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").Length = 1.0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_F0lr1GoikFSCcgo_1_JJS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_F0lr1GoikFSCcgo_1_JJS")
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS").addGeometry(Part.LineSegment(App.Vector(-31.58907000000000,6.76283000000000,0.00000000000000),App.Vector(-14.57523000000000,6.76283000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS").addGeometry(Part.LineSegment(App.Vector(-14.57523000000000,6.76283000000000,0.00000000000000),App.Vector(-14.57523000000000,3.46557000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS").addGeometry(Part.LineSegment(App.Vector(-31.58907000000000,3.46557000000000,0.00000000000000),App.Vector(-14.57523000000000,3.46557000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS").addGeometry(Part.LineSegment(App.Vector(-31.58907000000000,6.76283000000000,0.00000000000000),App.Vector(-31.58907000000000,3.46557000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pocket","Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").Length = 1.0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_F0lr1GoikFSCcgo_1_JJW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_F0lr1GoikFSCcgo_1_JJW")
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW").addGeometry(Part.LineSegment(App.Vector(-31.45718000000000,1.35533000000000,0.00000000000000),App.Vector(-16.55358000000000,1.35533000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW").addGeometry(Part.LineSegment(App.Vector(-16.55358000000000,1.35533000000000,0.00000000000000),App.Vector(-16.55358000000000,-1.67815000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW").addGeometry(Part.LineSegment(App.Vector(-31.45718000000000,-1.67815000000000,0.00000000000000),App.Vector(-16.55358000000000,-1.67815000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW").addGeometry(Part.LineSegment(App.Vector(-31.45718000000000,1.35533000000000,0.00000000000000),App.Vector(-31.45718000000000,-1.67815000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pocket","Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").Length = 1.0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_F0lr1GoikFSCcgo_1_JJa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_F0lr1GoikFSCcgo_1_JJa")
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa").addGeometry(Part.LineSegment(App.Vector(-10.75041000000000,7.02661000000000,0.00000000000000),App.Vector(0.85593000000000,7.02661000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa").addGeometry(Part.LineSegment(App.Vector(0.85593000000000,7.02661000000000,0.00000000000000),App.Vector(0.85593000000000,4.52069000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa").addGeometry(Part.LineSegment(App.Vector(-10.75041000000000,4.52069000000000,0.00000000000000),App.Vector(0.85593000000000,4.52069000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa").addGeometry(Part.LineSegment(App.Vector(-10.75041000000000,7.02661000000000,0.00000000000000),App.Vector(-10.75041000000000,4.52069000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pocket","Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").Length = 1.0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_F0lr1GoikFSCcgo_1_JJe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_F0lr1GoikFSCcgo_1_JJe")
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJe"), [""])
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe").addGeometry(Part.LineSegment(App.Vector(4.28507000000000,7.55417000000000,0.00000000000000),App.Vector(16.28708000000000,7.55417000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe").addGeometry(Part.LineSegment(App.Vector(16.28708000000000,7.55417000000000,0.00000000000000),App.Vector(16.28708000000000,4.12502000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe").addGeometry(Part.LineSegment(App.Vector(4.28507000000000,4.12502000000000,0.00000000000000),App.Vector(16.28708000000000,4.12502000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe").addGeometry(Part.LineSegment(App.Vector(4.28507000000000,7.55417000000000,0.00000000000000),App.Vector(4.28507000000000,4.12502000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pocket","Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").Profile = App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").Length = 1.0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").Type = 4
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Plane", "plane_Sketch_F0lr1GoikFSCcgo_1_JJi")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("Sketcher::SketchObject","Sketch_F0lr1GoikFSCcgo_1_JJi")
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0lr1GoikFSCcgo_1_JJi"), [""])
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi").addGeometry(Part.LineSegment(App.Vector(-11.54176000000000,3.20179000000000,0.00000000000000),App.Vector(17.07842000000000,3.20179000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi").addGeometry(Part.LineSegment(App.Vector(17.07842000000000,3.20179000000000,0.00000000000000),App.Vector(17.07842000000000,-0.09547000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi").addGeometry(Part.LineSegment(App.Vector(-11.54176000000000,-0.09547000000000,0.00000000000000),App.Vector(17.07842000000000,-0.09547000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi").addGeometry(Part.LineSegment(App.Vector(-11.54176000000000,3.20179000000000,0.00000000000000),App.Vector(-11.54176000000000,-0.09547000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQo69to2OfFRZ7x_0").newObject("PartDesign::Pocket","Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").Profile = App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi")
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").Length = 1.0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0lr1GoikFSCcgo_1_JJi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").Type = 4
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0lr1GoikFSCcgo_1_FFDVCCSJ2gOxg8C_1_JJi").Offset = 0
App.ActiveDocument.recompute()

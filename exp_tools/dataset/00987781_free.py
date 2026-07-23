import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00987781")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fcey7HWsTwngeVD_0")
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").Label = "Body_Fcey7HWsTwngeVD_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_Fcey7HWsTwngeVD_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fcey7HWsTwngeVD_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_Fcey7HWsTwngeVD_0_JGC")
App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fcey7HWsTwngeVD_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-37.29931000000001,-3.41806000000000,0.00000000000000),App.Vector(38.90069000000000,-3.41806000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC").addGeometry(Part.LineSegment(App.Vector(38.90069000000000,-3.41806000000000,0.00000000000000),App.Vector(38.90069000000000,-8.08885000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-37.29931000000001,-8.08885000000000,0.00000000000000),App.Vector(38.90069000000000,-8.08885000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-37.29931000000001,-3.41806000000000,0.00000000000000),App.Vector(-37.29931000000001,-8.08885000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pad","Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC")
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC")
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").Length = 38.1
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FuFJwwmTQtFjiTB_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_Fcey7HWsTwngeVD_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fcey7HWsTwngeVD_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_Fcey7HWsTwngeVD_0_JGG")
App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fcey7HWsTwngeVD_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG").addGeometry(Part.LineSegment(App.Vector(-37.29931000000001,-28.81806000000000,0.00000000000000),App.Vector(38.90069000000000,-28.81806000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG").addGeometry(Part.LineSegment(App.Vector(38.90069000000000,-28.81806000000000,0.00000000000000),App.Vector(38.90069000000000,-8.08885000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG").addGeometry(Part.LineSegment(App.Vector(-37.29931000000001,-8.08885000000000,0.00000000000000),App.Vector(38.90069000000000,-8.08885000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG").addGeometry(Part.LineSegment(App.Vector(-37.29931000000001,-28.81806000000000,0.00000000000000),App.Vector(-37.29931000000001,-8.08885000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pad","Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG")
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG")
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").Length = 19.05
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fcey7HWsTwngeVD_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fcey7HWsTwngeVD_0_FWXpSZixmfnLJVT_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_Fj83ix6dycqiqxX_1_JLC")
origin = App.Vector(-26.60488000000000,-16.11806000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj83ix6dycqiqxX_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_Fj83ix6dycqiqxX_1_JLC")
App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj83ix6dycqiqxX_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC").addGeometry(Part.LineSegment(App.Vector(37.43468000000000,12.70000000000000,0.00000000000000),App.Vector(44.92194000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC").addGeometry(Part.LineSegment(App.Vector(44.92194000000000,12.70000000000000,0.00000000000000),App.Vector(44.92194000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC").addGeometry(Part.LineSegment(App.Vector(37.43468000000000,-12.70000000000000,0.00000000000000),App.Vector(44.92194000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC").addGeometry(Part.LineSegment(App.Vector(37.43468000000000,12.70000000000000,0.00000000000000),App.Vector(37.43468000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pad","Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC")
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC")
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj83ix6dycqiqxX_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").Type = 0
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj83ix6dycqiqxX_1_FNJeZKOQYHLSeS1_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_FNHKBch1nTGALNI_1_JRC")
origin = App.Vector(-26.60488000000000,-16.11806000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNHKBch1nTGALNI_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_FNHKBch1nTGALNI_1_JRC")
App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNHKBch1nTGALNI_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC").addGeometry(Part.LineSegment(App.Vector(10.69444000000000,12.70000000000000,0.00000000000000),App.Vector(17.11210000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC").addGeometry(Part.LineSegment(App.Vector(17.11210000000000,12.70000000000000,0.00000000000000),App.Vector(17.11210000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC").addGeometry(Part.LineSegment(App.Vector(10.69444000000000,-12.70000000000000,0.00000000000000),App.Vector(17.11210000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC").addGeometry(Part.LineSegment(App.Vector(10.69444000000000,12.70000000000000,0.00000000000000),App.Vector(10.69444000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pocket","Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC")
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC")
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_FNHKBch1nTGALNI_1_JRG")
origin = App.Vector(-26.60488000000000,-16.11806000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNHKBch1nTGALNI_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_FNHKBch1nTGALNI_1_JRG")
App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNHKBch1nTGALNI_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG").addGeometry(Part.LineSegment(App.Vector(36.63247000000000,12.70000000000000,0.00000000000000),App.Vector(44.11973000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG").addGeometry(Part.LineSegment(App.Vector(44.11973000000000,12.70000000000000,0.00000000000000),App.Vector(44.11973000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG").addGeometry(Part.LineSegment(App.Vector(36.63247000000000,-12.70000000000000,0.00000000000000),App.Vector(44.11973000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG").addGeometry(Part.LineSegment(App.Vector(36.63247000000000,12.70000000000000,0.00000000000000),App.Vector(36.63247000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pocket","Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG")
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG")
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").Length = 5.0
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNHKBch1nTGALNI_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNHKBch1nTGALNI_1_FMXr70QFqNVHXFn_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_FOcRw83lOpeNmbN_1_JVO")
origin = App.Vector(0.80069000000000,-28.81806000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_FOcRw83lOpeNmbN_1_JVO")
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVO"), [""])
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-13.50230000000000,-4.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.20883000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").addGeometry(Part.LineSegment(App.Vector(-16.71113000000000,-4.52500000000000,0.00000000000000),App.Vector(-10.29347000000000,-4.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pocket","Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").Profile = App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").Type = 4
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FbxpV4WVX8rtdo0_1_JVO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_FOcRw83lOpeNmbN_1_JVC")
origin = App.Vector(0.80069000000000,-28.81806000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_FOcRw83lOpeNmbN_1_JVC")
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-13.50230000000000,-4.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.20883000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVC").addGeometry(Part.LineSegment(App.Vector(-16.71113000000000,-4.52500000000000,0.00000000000000),App.Vector(-10.29347000000000,-4.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pocket","Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVC")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_FOcRw83lOpeNmbN_1_JVG")
origin = App.Vector(0.80069000000000,-28.81806000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_FOcRw83lOpeNmbN_1_JVG")
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVG").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(12.97053000000000,-4.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.74363000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVG").addGeometry(Part.LineSegment(App.Vector(9.22690000000000,-4.52500000000000,0.00000000000000),App.Vector(16.71416000000000,-4.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pocket","Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVG")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_FOcRw83lOpeNmbN_1_JVO")
origin = App.Vector(0.80069000000000,-28.81806000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_FOcRw83lOpeNmbN_1_JVO")
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVO"), [""])
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-13.50230000000000,-4.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.20883000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").addGeometry(Part.LineSegment(App.Vector(-16.71113000000000,-4.52500000000000,0.00000000000000),App.Vector(-10.29347000000000,-4.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pocket","Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").Profile = App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").Type = 4
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Plane", "plane_Sketch_FOcRw83lOpeNmbN_1_JVS")
origin = App.Vector(0.80069000000000,-28.81806000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("Sketcher::SketchObject","Sketch_FOcRw83lOpeNmbN_1_JVS")
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOcRw83lOpeNmbN_1_JVS"), [""])
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(12.97053000000000,-4.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.74363000000000),3.14159265358979,0.0),False)

App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVS").addGeometry(Part.LineSegment(App.Vector(9.22690000000000,-4.52500000000000,0.00000000000000),App.Vector(16.71416000000000,-4.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fcey7HWsTwngeVD_0").newObject("PartDesign::Pocket","Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").Profile = App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVS")
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").Length = 25.0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOcRw83lOpeNmbN_1_JVS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").Type = 4
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOcRw83lOpeNmbN_1_FSIuCSkwvV7kmbP_1_JVS").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00127292")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fwna4OnOiFfc7Ix_0")
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").Label = "Body_Fwna4OnOiFfc7Ix_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Plane", "plane_Sketch_Fwna4OnOiFfc7Ix_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fwna4OnOiFfc7Ix_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("Sketcher::SketchObject","Sketch_Fwna4OnOiFfc7Ix_0_JGC")
App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fwna4OnOiFfc7Ix_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC").addGeometry(Part.LineSegment(App.Vector(53.21300000000000,33.14700000000001,0.00000000000000),App.Vector(-53.21300000000000,33.14700000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC").addGeometry(Part.LineSegment(App.Vector(-53.21300000000000,33.14700000000001,0.00000000000000),App.Vector(-53.21300000000000,-33.14700000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC").addGeometry(Part.LineSegment(App.Vector(53.21300000000000,-33.14700000000001,0.00000000000000),App.Vector(-53.21300000000000,-33.14700000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC").addGeometry(Part.LineSegment(App.Vector(53.21300000000000,33.14700000000001,0.00000000000000),App.Vector(53.21300000000000,-33.14700000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Pad","Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC")
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC")
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").Length = 71.88200000000002
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fwna4OnOiFfc7Ix_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_Fwna4OnOiFfc7Ix_0_FVmRy5aqGJfmhpo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Plane", "plane_Sketch_FhBHzuEHUtEuNJl_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,35.94100000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhBHzuEHUtEuNJl_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("Sketcher::SketchObject","Sketch_FhBHzuEHUtEuNJl_1_JJC")
App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhBHzuEHUtEuNJl_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").addGeometry(Part.LineSegment(App.Vector(-50.67300000000000,30.60700000000000,0.00000000000000),App.Vector(50.67300000000000,30.60700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").addGeometry(Part.LineSegment(App.Vector(50.67300000000000,30.60700000000000,0.00000000000000),App.Vector(50.67300000000000,-12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").addGeometry(Part.LineSegment(App.Vector(50.67300000000000,-12.57300000000000,0.00000000000000),App.Vector(31.87700000000000,-12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").addGeometry(Part.LineSegment(App.Vector(31.87700000000000,-30.60700000000000,0.00000000000000),App.Vector(31.87700000000000,-12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").addGeometry(Part.LineSegment(App.Vector(-12.57300000000000,-30.60700000000000,0.00000000000000),App.Vector(31.87700000000000,-30.60700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").addGeometry(Part.LineSegment(App.Vector(-12.57300000000000,-30.60700000000000,0.00000000000000),App.Vector(-12.57300000000000,-12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").addGeometry(Part.LineSegment(App.Vector(-50.67300000000000,-12.57300000000000,0.00000000000000),App.Vector(-12.57300000000000,-12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").addGeometry(Part.LineSegment(App.Vector(-50.67300000000000,30.60700000000000,0.00000000000000),App.Vector(-50.67300000000000,-12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Pad","Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC")
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC")
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").Length = 12.192000000000002
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Plane", "plane_Sketch_FhBHzuEHUtEuNJl_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,35.94100000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhBHzuEHUtEuNJl_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("Sketcher::SketchObject","Sketch_FhBHzuEHUtEuNJl_1_JJG")
App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhBHzuEHUtEuNJl_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG").addGeometry(Part.LineSegment(App.Vector(-50.67300000000000,-17.65300000000000,0.00000000000000),App.Vector(-37.97300000000000,-17.65300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG").addGeometry(Part.LineSegment(App.Vector(-37.97300000000000,-17.65300000000000,0.00000000000000),App.Vector(-37.97300000000000,-30.60700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG").addGeometry(Part.LineSegment(App.Vector(-50.67300000000000,-30.60700000000000,0.00000000000000),App.Vector(-37.97300000000000,-30.60700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG").addGeometry(Part.LineSegment(App.Vector(-50.67300000000000,-17.65300000000000,0.00000000000000),App.Vector(-50.67300000000000,-30.60700000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Pad","Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG")
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG")
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").Length = 12.192000000000002
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Plane", "plane_Sketch_FhBHzuEHUtEuNJl_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,35.94100000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhBHzuEHUtEuNJl_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("Sketcher::SketchObject","Sketch_FhBHzuEHUtEuNJl_1_JJK")
App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhBHzuEHUtEuNJl_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK").addGeometry(Part.LineSegment(App.Vector(37.97300000000000,-17.65300000000000,0.00000000000000),App.Vector(50.67300000000000,-17.65300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK").addGeometry(Part.LineSegment(App.Vector(50.67300000000000,-17.65300000000000,0.00000000000000),App.Vector(50.67300000000000,-30.60700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK").addGeometry(Part.LineSegment(App.Vector(37.97300000000000,-30.60700000000000,0.00000000000000),App.Vector(50.67300000000000,-30.60700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK").addGeometry(Part.LineSegment(App.Vector(37.97300000000000,-17.65300000000000,0.00000000000000),App.Vector(37.97300000000000,-30.60700000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Pad","Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK")
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK")
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").Length = 12.192000000000002
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhBHzuEHUtEuNJl_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhBHzuEHUtEuNJl_1_Fs55mpWKyNgde3F_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Plane", "plane_Sketch_F7PyEJa2U75vEhc_1_JNC")
origin = App.Vector(-50.67300000000000,-24.13000000000000,42.03700000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7PyEJa2U75vEhc_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("Sketcher::SketchObject","Sketch_F7PyEJa2U75vEhc_1_JNC")
App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7PyEJa2U75vEhc_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC").addGeometry(Part.LineSegment(App.Vector(-5.20700000000000,-4.82600000000000,0.00000000000000),App.Vector(5.20700000000000,-4.82600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC").addGeometry(Part.LineSegment(App.Vector(5.20700000000000,-4.82600000000000,0.00000000000000),App.Vector(5.20700000000000,4.82600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC").addGeometry(Part.LineSegment(App.Vector(-5.20700000000000,4.82600000000000,0.00000000000000),App.Vector(5.20700000000000,4.82600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC").addGeometry(Part.LineSegment(App.Vector(-5.20700000000000,-4.82600000000000,0.00000000000000),App.Vector(-5.20700000000000,4.82600000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Pocket","Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC")
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC")
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7PyEJa2U75vEhc_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7PyEJa2U75vEhc_1_FNSEWq4xQCOa5IO_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Plane", "plane_Sketch_FFomxx4k7dza0TZ_1_JRC")
origin = App.Vector(50.67300000000000,-24.13000000000000,42.03700000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFomxx4k7dza0TZ_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("Sketcher::SketchObject","Sketch_FFomxx4k7dza0TZ_1_JRC")
App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFomxx4k7dza0TZ_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5.20700000000000,-4.82600000000000,0.00000000000000),App.Vector(5.20700000000000,-4.82600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC").addGeometry(Part.LineSegment(App.Vector(5.20700000000000,-4.82600000000000,0.00000000000000),App.Vector(5.20700000000000,4.82600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5.20700000000000,4.82600000000000,0.00000000000000),App.Vector(5.20700000000000,4.82600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5.20700000000000,-4.82600000000000,0.00000000000000),App.Vector(-5.20700000000000,4.82600000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Pocket","Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC")
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC")
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFomxx4k7dza0TZ_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFomxx4k7dza0TZ_1_FwQQZ83SQCeDkjq_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Plane", "plane_Sketch_F1E45FsFyPkmOO4_1_JVC")
origin = App.Vector(-44.32300000000000,-24.13000000000000,48.13300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1E45FsFyPkmOO4_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("Sketcher::SketchObject","Sketch_F1E45FsFyPkmOO4_1_JVC")
App.ActiveDocument.getObject("Sketch_F1E45FsFyPkmOO4_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1E45FsFyPkmOO4_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F1E45FsFyPkmOO4_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1E45FsFyPkmOO4_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1E45FsFyPkmOO4_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1E45FsFyPkmOO4_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Pocket","Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC")
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F1E45FsFyPkmOO4_1_JVC")
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1E45FsFyPkmOO4_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1E45FsFyPkmOO4_1_F487dMcUr5gi8Oh_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Plane", "plane_Sketch_FyFNstAMEL887In_1_JZC")
origin = App.Vector(44.32300000000000,-24.13000000000000,48.13300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyFNstAMEL887In_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("Sketcher::SketchObject","Sketch_FyFNstAMEL887In_1_JZC")
App.ActiveDocument.getObject("Sketch_FyFNstAMEL887In_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyFNstAMEL887In_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FyFNstAMEL887In_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyFNstAMEL887In_1_JZC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyFNstAMEL887In_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyFNstAMEL887In_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fwna4OnOiFfc7Ix_0").newObject("PartDesign::Pocket","Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC")
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FyFNstAMEL887In_1_JZC")
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyFNstAMEL887In_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyFNstAMEL887In_1_Fve9MLyryUplw3J_1_JZC").Offset = 0
App.ActiveDocument.recompute()

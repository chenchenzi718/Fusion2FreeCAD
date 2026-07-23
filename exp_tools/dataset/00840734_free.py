import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00840734")
App.ActiveDocument.addObject("PartDesign::Body","Body_FmksS4SdVyVef5x_0")
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").Label = "Body_FmksS4SdVyVef5x_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_FmksS4SdVyVef5x_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmksS4SdVyVef5x_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_FmksS4SdVyVef5x_0_JGC")
App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmksS4SdVyVef5x_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1524.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC").addGeometry(Part.LineSegment(App.Vector(1524.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1524.00000000000000,152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,152.40000000000001,0.00000000000000),App.Vector(1524.00000000000000,152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pad","Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC")
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC")
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmksS4SdVyVef5x_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmksS4SdVyVef5x_0_FOW5f35YvfPsIPw_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_F3cUyJcnM0nASvN_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3cUyJcnM0nASvN_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_F3cUyJcnM0nASvN_1_JJC")
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3cUyJcnM0nASvN_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-30.93409000000000,0.00000000000000),App.Vector(50.80000000000000,-30.93409000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC").addGeometry(Part.LineSegment(App.Vector(50.80000000000000,-30.93409000000000,0.00000000000000),App.Vector(50.80000000000000,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,184.96598000000000,0.00000000000000),App.Vector(50.80000000000000,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-30.93409000000000,0.00000000000000),App.Vector(25.40000000000000,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pocket","Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC")
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC")
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_F3cUyJcnM0nASvN_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3cUyJcnM0nASvN_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_F3cUyJcnM0nASvN_1_JJG")
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3cUyJcnM0nASvN_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG").addGeometry(Part.LineSegment(App.Vector(508.00000000000000,-30.93409000000000,0.00000000000000),App.Vector(533.39999999999998,-30.93409000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG").addGeometry(Part.LineSegment(App.Vector(533.39999999999998,-30.93409000000000,0.00000000000000),App.Vector(533.39999999999998,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG").addGeometry(Part.LineSegment(App.Vector(508.00000000000000,184.96598000000000,0.00000000000000),App.Vector(533.39999999999998,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG").addGeometry(Part.LineSegment(App.Vector(508.00000000000000,-30.93409000000000,0.00000000000000),App.Vector(508.00000000000000,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pocket","Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG")
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG")
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_F3cUyJcnM0nASvN_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3cUyJcnM0nASvN_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_F3cUyJcnM0nASvN_1_JJK")
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3cUyJcnM0nASvN_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK").addGeometry(Part.LineSegment(App.Vector(990.60000000000002,-30.93409000000000,0.00000000000000),App.Vector(1016.00000000000000,-30.93409000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK").addGeometry(Part.LineSegment(App.Vector(1016.00000000000000,-30.93409000000000,0.00000000000000),App.Vector(1016.00000000000000,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK").addGeometry(Part.LineSegment(App.Vector(990.60000000000002,184.96598000000000,0.00000000000000),App.Vector(1016.00000000000000,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK").addGeometry(Part.LineSegment(App.Vector(990.60000000000002,-30.93409000000000,0.00000000000000),App.Vector(990.60000000000002,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pocket","Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK")
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK")
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_F3cUyJcnM0nASvN_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3cUyJcnM0nASvN_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_F3cUyJcnM0nASvN_1_JJO")
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3cUyJcnM0nASvN_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO").addGeometry(Part.LineSegment(App.Vector(1473.20000000000005,-30.93409000000000,0.00000000000000),App.Vector(1498.59999999999991,-30.93409000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO").addGeometry(Part.LineSegment(App.Vector(1498.59999999999991,-30.93409000000000,0.00000000000000),App.Vector(1498.59999999999991,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO").addGeometry(Part.LineSegment(App.Vector(1473.20000000000005,184.96598000000000,0.00000000000000),App.Vector(1498.59999999999991,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO").addGeometry(Part.LineSegment(App.Vector(1473.20000000000005,-30.93409000000000,0.00000000000000),App.Vector(1473.20000000000005,184.96598000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pocket","Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO")
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO")
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3cUyJcnM0nASvN_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").Type = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").Reversed = 1
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3cUyJcnM0nASvN_1_FFZerM09nHh4GjK_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_FdcfVR0RECATjkn_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_FdcfVR0RECATjkn_1_JNC")
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNC").addGeometry(Part.Circle(App.Vector(101.59999999999999,12.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pocket","Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNC")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_FdcfVR0RECATjkn_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_FdcfVR0RECATjkn_1_JNG")
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNG").addGeometry(Part.Circle(App.Vector(406.39999999999998,12.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pocket","Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNG")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_FdcfVR0RECATjkn_1_JNK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_FdcfVR0RECATjkn_1_JNK")
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNK").addGeometry(Part.Circle(App.Vector(762.00000000000000,12.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pocket","Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNK")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_FdcfVR0RECATjkn_1_JNO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_FdcfVR0RECATjkn_1_JNO")
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNO").addGeometry(Part.Circle(App.Vector(1117.59999999999991,12.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pocket","Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNO")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Plane", "plane_Sketch_FdcfVR0RECATjkn_1_JNS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("Sketcher::SketchObject","Sketch_FdcfVR0RECATjkn_1_JNS")
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdcfVR0RECATjkn_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNS").addGeometry(Part.Circle(App.Vector(1422.40000000000009,12.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FmksS4SdVyVef5x_0").newObject("PartDesign::Pocket","Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNS")
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdcfVR0RECATjkn_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdcfVR0RECATjkn_1_F0iBEpFk780z9Ga_1_JNS").Offset = 0
App.ActiveDocument.recompute()

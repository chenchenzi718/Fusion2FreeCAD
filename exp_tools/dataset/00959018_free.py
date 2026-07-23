import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00959018")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fj1fJp1Ftzk4vNq_0")
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").Label = "Body_Fj1fJp1Ftzk4vNq_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Plane", "plane_Sketch_Fj1fJp1Ftzk4vNq_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj1fJp1Ftzk4vNq_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("Sketcher::SketchObject","Sketch_Fj1fJp1Ftzk4vNq_0_JGC")
App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj1fJp1Ftzk4vNq_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").addGeometry(Part.LineSegment(App.Vector(-23.36594000000000,-17.29706000000000,0.00000000000000),App.Vector(23.36594000000000,17.29706000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").addGeometry(Part.LineSegment(App.Vector(23.36594000000000,17.29706000000000,0.00000000000000),App.Vector(23.36594000000000,23.77406000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").addGeometry(Part.LineSegment(App.Vector(23.36594000000000,23.77406000000000,0.00000000000000),App.Vector(-7.83493000000000,10.19449000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-38.04165000000000,16.08484000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),30.77568000000000),4.15518493961787,6.09060076677683),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").addGeometry(Part.LineSegment(App.Vector(-54.31630000000000,-10.03562000000000,0.00000000000000),App.Vector(-62.65837000000001,-13.66634000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").addGeometry(Part.LineSegment(App.Vector(-62.65837000000001,-13.66634000000000,0.00000000000000),App.Vector(-86.87543000000001,-17.29706000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").addGeometry(Part.LineSegment(App.Vector(-71.00043000000001,-17.29706000000000,0.00000000000000),App.Vector(-86.87543000000001,-17.29706000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").addGeometry(Part.LineSegment(App.Vector(-23.36594000000000,-17.29706000000000,0.00000000000000),App.Vector(-71.00043000000001,-17.29706000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Pad","Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC")
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC")
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").Length = 118.11000000000001
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Plane", "plane_Sketch_Fj1fJp1Ftzk4vNq_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj1fJp1Ftzk4vNq_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("Sketcher::SketchObject","Sketch_Fj1fJp1Ftzk4vNq_0_JGG")
App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj1fJp1Ftzk4vNq_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG").addGeometry(Part.LineSegment(App.Vector(23.36594000000000,17.29706000000000,0.00000000000000),App.Vector(29.71594000000000,17.29706000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG").addGeometry(Part.LineSegment(App.Vector(29.71594000000000,17.29706000000000,0.00000000000000),App.Vector(29.71594000000000,23.77406000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG").addGeometry(Part.LineSegment(App.Vector(23.36594000000000,23.77406000000000,0.00000000000000),App.Vector(29.71594000000000,23.77406000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG").addGeometry(Part.LineSegment(App.Vector(23.36594000000000,17.29706000000000,0.00000000000000),App.Vector(23.36594000000000,23.77406000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Pad","Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG")
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG")
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").Length = 118.11000000000001
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj1fJp1Ftzk4vNq_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj1fJp1Ftzk4vNq_0_FslHxQ3Ea4BSfDC_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Plane", "plane_Sketch_FCqTAXSpSHMiuKo_1_JJC")
origin = App.Vector(26.54094000000000,-59.05500000000001,23.77406000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("Sketcher::SketchObject","Sketch_FCqTAXSpSHMiuKo_1_JJC")
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.77800000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Pocket","Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJC")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Plane", "plane_Sketch_FCqTAXSpSHMiuKo_1_JJG")
origin = App.Vector(26.54094000000000,-59.05500000000001,23.77406000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("Sketcher::SketchObject","Sketch_FCqTAXSpSHMiuKo_1_JJG")
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJG").addGeometry(Part.Circle(App.Vector(0.00000000000000,9.44880000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.77800000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Pocket","Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJG")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Plane", "plane_Sketch_FCqTAXSpSHMiuKo_1_JJK")
origin = App.Vector(26.54094000000000,-59.05500000000001,23.77406000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("Sketcher::SketchObject","Sketch_FCqTAXSpSHMiuKo_1_JJK")
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJK").addGeometry(Part.Circle(App.Vector(0.00000000000000,18.89760000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.77800000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Pocket","Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJK")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Plane", "plane_Sketch_FCqTAXSpSHMiuKo_1_JJO")
origin = App.Vector(26.54094000000000,-59.05500000000001,23.77406000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("Sketcher::SketchObject","Sketch_FCqTAXSpSHMiuKo_1_JJO")
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJO").addGeometry(Part.Circle(App.Vector(0.00000000000000,-9.44880000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.77800000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Pocket","Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJO")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Plane", "plane_Sketch_FCqTAXSpSHMiuKo_1_JJS")
origin = App.Vector(26.54094000000000,-59.05500000000001,23.77406000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("Sketcher::SketchObject","Sketch_FCqTAXSpSHMiuKo_1_JJS")
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJS").addGeometry(Part.Circle(App.Vector(0.00000000000000,-18.89759999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.77800000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Pocket","Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJS")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Plane", "plane_Sketch_FCqTAXSpSHMiuKo_1_JJW")
origin = App.Vector(26.54094000000000,-59.05500000000001,23.77406000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("Sketcher::SketchObject","Sketch_FCqTAXSpSHMiuKo_1_JJW")
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJW").addGeometry(Part.Circle(App.Vector(0.00000000000000,28.34640000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.77800000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Pocket","Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJW")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Plane", "plane_Sketch_FCqTAXSpSHMiuKo_1_JJa")
origin = App.Vector(26.54094000000000,-59.05500000000001,23.77406000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("Sketcher::SketchObject","Sketch_FCqTAXSpSHMiuKo_1_JJa")
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCqTAXSpSHMiuKo_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJa").addGeometry(Part.Circle(App.Vector(0.00000000000000,-28.34640000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.77800000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fj1fJp1Ftzk4vNq_0").newObject("PartDesign::Pocket","Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJa")
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCqTAXSpSHMiuKo_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCqTAXSpSHMiuKo_1_FC4zbt29JuNbBzX_1_JJa").Offset = 0
App.ActiveDocument.recompute()

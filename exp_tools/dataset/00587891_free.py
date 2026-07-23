import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00587891")
App.ActiveDocument.addObject("PartDesign::Body","Body_FqwXtibMPAx4uBD_0")
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").Label = "Body_FqwXtibMPAx4uBD_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Plane", "plane_Sketch_FqwXtibMPAx4uBD_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("Sketcher::SketchObject","Sketch_FqwXtibMPAx4uBD_0_JGS")
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").addGeometry(Part.LineSegment(App.Vector(-22.20373000000000,28.83933000000000,0.00000000000000),App.Vector(30.62584000000000,28.83933000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").addGeometry(Part.LineSegment(App.Vector(30.62584000000000,28.83933000000000,0.00000000000000),App.Vector(30.62584000000000,-21.94852000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").addGeometry(Part.LineSegment(App.Vector(30.62584000000000,-33.17798999999999,0.00000000000000),App.Vector(30.62584000000000,-21.94852000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").addGeometry(Part.LineSegment(App.Vector(-22.20373000000000,-33.17798999999999,0.00000000000000),App.Vector(30.62584000000000,-33.17798999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").addGeometry(Part.LineSegment(App.Vector(-22.20373000000000,-33.17798999999999,0.00000000000000),App.Vector(-22.20373000000000,6.38038000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").addGeometry(Part.LineSegment(App.Vector(-22.20373000000000,28.83933000000000,0.00000000000000),App.Vector(-22.20373000000000,6.38038000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Pad","Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").Profile = App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FyMWa1KGPTXSSYi_0_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Plane", "plane_Sketch_FqwXtibMPAx4uBD_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("Sketcher::SketchObject","Sketch_FqwXtibMPAx4uBD_0_JGG")
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG").addGeometry(Part.LineSegment(App.Vector(30.62584000000000,28.83933000000000,0.00000000000000),App.Vector(72.22594000000001,28.83933000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG").addGeometry(Part.LineSegment(App.Vector(72.22594000000001,28.83933000000000,0.00000000000000),App.Vector(72.22594000000001,-21.94852000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG").addGeometry(Part.LineSegment(App.Vector(30.62584000000000,-21.94852000000000,0.00000000000000),App.Vector(72.22594000000001,-21.94852000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG").addGeometry(Part.LineSegment(App.Vector(30.62584000000000,28.83933000000000,0.00000000000000),App.Vector(30.62584000000000,-21.94852000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Pad","Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").Profile = App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").Length = 38.1
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F2ceG8I8TNtKuCV_1_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Plane", "plane_Sketch_FqwXtibMPAx4uBD_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("Sketcher::SketchObject","Sketch_FqwXtibMPAx4uBD_0_JGC")
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-46.19397000000000,28.83933000000000,0.00000000000000),App.Vector(-22.20373000000000,28.83933000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-22.20373000000000,28.83933000000000,0.00000000000000),App.Vector(-22.20373000000000,6.38038000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-46.19397000000000,6.38038000000000,0.00000000000000),App.Vector(-22.20373000000000,6.38038000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC").addGeometry(Part.LineSegment(App.Vector(-46.19397000000000,28.83933000000000,0.00000000000000),App.Vector(-46.19397000000000,6.38038000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Pad","Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").Profile = App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_F5Q1V6RrU9G5wYn_1_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Plane", "plane_Sketch_FqwXtibMPAx4uBD_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("Sketcher::SketchObject","Sketch_FqwXtibMPAx4uBD_0_JGO")
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO").addGeometry(Part.LineSegment(App.Vector(-46.19397000000000,6.38038000000000,0.00000000000000),App.Vector(-22.20373000000000,6.38038000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO").addGeometry(Part.LineSegment(App.Vector(-22.20373000000000,-33.17798999999999,0.00000000000000),App.Vector(-22.20373000000000,6.38038000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO").addGeometry(Part.LineSegment(App.Vector(-22.20373000000000,-33.17798999999999,0.00000000000000),App.Vector(-46.19397000000000,-33.17798999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO").addGeometry(Part.LineSegment(App.Vector(-46.19397000000000,6.38038000000000,0.00000000000000),App.Vector(-46.19397000000000,-33.17798999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Pad","Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").Profile = App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FrWuRFBLLYLAVEU_1_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Plane", "plane_Sketch_FqwXtibMPAx4uBD_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("Sketcher::SketchObject","Sketch_FqwXtibMPAx4uBD_0_JGK")
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqwXtibMPAx4uBD_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.62584000000000,-21.94852000000000,0.00000000000000),App.Vector(72.22594000000001,-21.94852000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK").addGeometry(Part.LineSegment(App.Vector(72.22594000000001,-21.94852000000000,0.00000000000000),App.Vector(72.22594000000001,-33.17798999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.62584000000000,-33.17798999999999,0.00000000000000),App.Vector(72.22594000000001,-33.17798999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.62584000000000,-33.17798999999999,0.00000000000000),App.Vector(30.62584000000000,-21.94852000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Pad","Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").Profile = App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK")
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").Length = 63.5
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqwXtibMPAx4uBD_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqwXtibMPAx4uBD_0_FkYnZxbU4cnJB3d_1_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Plane", "plane_Sketch_Fhw5pOK6OihRQcy_1_JRC")
origin = App.Vector(51.42589000000000,3.44541000000000,38.10000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fhw5pOK6OihRQcy_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("Sketcher::SketchObject","Sketch_Fhw5pOK6OihRQcy_1_JRC")
App.ActiveDocument.getObject("Sketch_Fhw5pOK6OihRQcy_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fhw5pOK6OihRQcy_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fhw5pOK6OihRQcy_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fhw5pOK6OihRQcy_1_JRC").addGeometry(Part.Circle(App.Vector(-13.14359000000000,15.69574000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.97070000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fhw5pOK6OihRQcy_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fhw5pOK6OihRQcy_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Pad","Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC")
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fhw5pOK6OihRQcy_1_JRC")
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fhw5pOK6OihRQcy_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fhw5pOK6OihRQcy_1_FMcdpUrC497XA8r_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Plane", "plane_Sketch_FSE8NNSzXhBMzHD_1_JVC")
origin = App.Vector(-34.19885000000000,-13.39880000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSE8NNSzXhBMzHD_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("Sketcher::SketchObject","Sketch_FSE8NNSzXhBMzHD_1_JVC")
App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSE8NNSzXhBMzHD_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").addGeometry(Part.LineSegment(App.Vector(1.06852000000000,6.94318000000000,0.00000000000000),App.Vector(-3.11024999999999,3.01021000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").addGeometry(Part.LineSegment(App.Vector(-3.11024999999999,3.01021000000000,0.00000000000000),App.Vector(-8.79058999999999,3.82515000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").addGeometry(Part.LineSegment(App.Vector(-8.79058999999999,3.82515000000000,0.00000000000000),App.Vector(-11.69509000000000,8.77432000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").addGeometry(Part.LineSegment(App.Vector(-11.69509000000000,8.77432000000000,0.00000000000000),App.Vector(-9.63659000000000,14.13091000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").addGeometry(Part.LineSegment(App.Vector(-9.63659000000000,14.13091000000000,0.00000000000000),App.Vector(-4.16519000000000,15.86128000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").addGeometry(Part.LineSegment(App.Vector(-4.16519000000000,15.86128000000000,0.00000000000000),App.Vector(0.59903000000000,12.66244000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").addGeometry(Part.LineSegment(App.Vector(1.06852000000000,6.94318000000000,0.00000000000000),App.Vector(0.59903000000000,12.66244000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Pad","Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC")
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC")
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").Length = 7.62
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_F44YFQVKhmD1BlT_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Plane", "plane_Sketch_FSE8NNSzXhBMzHD_1_JVG")
origin = App.Vector(-34.19885000000000,-13.39880000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSE8NNSzXhBMzHD_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("Sketcher::SketchObject","Sketch_FSE8NNSzXhBMzHD_1_JVG")
App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSE8NNSzXhBMzHD_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(7.11382000000000,-11.06404000000000,0.00000000000000),App.Vector(4.62608000000000,-14.71272000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(4.62608000000000,-14.71272000000000,0.00000000000000),App.Vector(0.46882000000000,-16.20231000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(0.46882000000000,-16.20231000000000,0.00000000000000),App.Vector(-3.77003000000000,-14.96383000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(-3.77003000000000,-14.96383000000000,0.00000000000000),App.Vector(-6.47137000000000,-11.47035000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(-6.47137000000000,-11.47035000000000,0.00000000000000),App.Vector(-6.60338999999999,-7.05626000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(-6.60338999999999,-7.05626000000000,0.00000000000000),App.Vector(-4.11566000000000,-3.40758000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(-4.11566000000000,-3.40758000000000,0.00000000000000),App.Vector(0.04160000000000,-1.91799000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(0.04160000000000,-1.91799000000000,0.00000000000000),App.Vector(4.28045000000000,-3.15646000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(4.28045000000000,-3.15646000000000,0.00000000000000),App.Vector(6.98180000000000,-6.64994000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").addGeometry(Part.LineSegment(App.Vector(7.11382000000000,-11.06404000000000,0.00000000000000),App.Vector(6.98180000000000,-6.64994000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FqwXtibMPAx4uBD_0").newObject("PartDesign::Pad","Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG")
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG")
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSE8NNSzXhBMzHD_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSE8NNSzXhBMzHD_1_FOpDaSwCjf7o7GD_1_JVG").Offset = 0
App.ActiveDocument.recompute()

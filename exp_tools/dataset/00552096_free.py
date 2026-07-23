import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00552096")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fq2WFfuvQrDq2a7_0")
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").Label = "Body_Fq2WFfuvQrDq2a7_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Plane", "plane_Sketch_Fq2WFfuvQrDq2a7_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq2WFfuvQrDq2a7_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("Sketcher::SketchObject","Sketch_Fq2WFfuvQrDq2a7_0_JGC")
App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq2WFfuvQrDq2a7_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC").addGeometry(Part.LineSegment(App.Vector(-65.00000000000000,52.50000000000000,0.00000000000000),App.Vector(65.00000000000000,52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC").addGeometry(Part.LineSegment(App.Vector(65.00000000000000,52.50000000000000,0.00000000000000),App.Vector(65.00000000000000,-52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC").addGeometry(Part.LineSegment(App.Vector(-65.00000000000000,-52.50000000000000,0.00000000000000),App.Vector(65.00000000000000,-52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC").addGeometry(Part.LineSegment(App.Vector(-65.00000000000000,52.50000000000000,0.00000000000000),App.Vector(-65.00000000000000,-52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Pad","Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC")
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC")
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq2WFfuvQrDq2a7_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq2WFfuvQrDq2a7_0_FsmWIMgDS4MawDx_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Plane", "plane_Sketch_F8NubrKPKakmPYj_1_JLK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8NubrKPKakmPYj_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("Sketcher::SketchObject","Sketch_F8NubrKPKakmPYj_1_JLK")
App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8NubrKPKakmPYj_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").addGeometry(Part.LineSegment(App.Vector(65.00000000000000,-52.50000000000000,0.00000000000000),App.Vector(57.50000000000000,-52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").addGeometry(Part.LineSegment(App.Vector(57.50000000000000,-33.84403000000000,0.00000000000000),App.Vector(57.50000000000000,-52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").addGeometry(Part.LineSegment(App.Vector(57.50000000000000,-33.84403000000000,0.00000000000000),App.Vector(57.50000000000000,33.84403000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").addGeometry(Part.LineSegment(App.Vector(57.50000000000000,33.84403000000000,0.00000000000000),App.Vector(57.50000000000000,52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").addGeometry(Part.LineSegment(App.Vector(65.00000000000000,52.50000000000000,0.00000000000000),App.Vector(57.50000000000000,52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").addGeometry(Part.LineSegment(App.Vector(65.00000000000000,-52.50000000000000,0.00000000000000),App.Vector(65.00000000000000,52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Pad","Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK")
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK")
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").Length = 25.0
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Plane", "plane_Sketch_F8NubrKPKakmPYj_1_JLO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8NubrKPKakmPYj_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("Sketcher::SketchObject","Sketch_F8NubrKPKakmPYj_1_JLO")
App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8NubrKPKakmPYj_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").addGeometry(Part.LineSegment(App.Vector(-65.00000000000000,-52.50000000000000,0.00000000000000),App.Vector(-57.50000000000000,-52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").addGeometry(Part.LineSegment(App.Vector(-57.50000000000000,-33.84403000000000,0.00000000000000),App.Vector(-57.50000000000000,-52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").addGeometry(Part.LineSegment(App.Vector(-57.50000000000000,-33.84403000000000,0.00000000000000),App.Vector(-57.50000000000000,33.84403000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").addGeometry(Part.LineSegment(App.Vector(-57.50000000000000,33.84403000000000,0.00000000000000),App.Vector(-57.50000000000000,52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").addGeometry(Part.LineSegment(App.Vector(-65.00000000000000,52.50000000000000,0.00000000000000),App.Vector(-57.50000000000000,52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").addGeometry(Part.LineSegment(App.Vector(-65.00000000000000,-52.50000000000000,0.00000000000000),App.Vector(-65.00000000000000,52.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Pad","Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO")
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO")
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").Length = 25.0
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8NubrKPKakmPYj_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8NubrKPKakmPYj_1_FKtYftnX9ize9BZ_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Plane", "plane_Sketch_FObbrE7WZBSZhAq_1_JPC")
origin = App.Vector(0.00000000000000,0.00000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("Sketcher::SketchObject","Sketch_FObbrE7WZBSZhAq_1_JPC")
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC").addGeometry(Part.LineSegment(App.Vector(-5.71987000000000,47.75631000000001,0.00000000000000),App.Vector(5.71987000000000,47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC").addGeometry(Part.LineSegment(App.Vector(5.71987000000000,47.75631000000001,0.00000000000000),App.Vector(5.71987000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC").addGeometry(Part.LineSegment(App.Vector(-5.71987000000000,-47.75631000000001,0.00000000000000),App.Vector(5.71987000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC").addGeometry(Part.LineSegment(App.Vector(-5.71987000000000,47.75631000000001,0.00000000000000),App.Vector(-5.71987000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Pocket","Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Plane", "plane_Sketch_FObbrE7WZBSZhAq_1_JPG")
origin = App.Vector(0.00000000000000,0.00000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("Sketcher::SketchObject","Sketch_FObbrE7WZBSZhAq_1_JPG")
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG").addGeometry(Part.LineSegment(App.Vector(30.71987000000000,47.75631000000001,0.00000000000000),App.Vector(30.71987000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG").addGeometry(Part.LineSegment(App.Vector(30.71987000000000,-47.75631000000001,0.00000000000000),App.Vector(19.28013000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG").addGeometry(Part.LineSegment(App.Vector(19.28013000000000,47.75631000000001,0.00000000000000),App.Vector(19.28013000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG").addGeometry(Part.LineSegment(App.Vector(30.71987000000000,47.75631000000001,0.00000000000000),App.Vector(19.28013000000000,47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Pocket","Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Plane", "plane_Sketch_FObbrE7WZBSZhAq_1_JPK")
origin = App.Vector(0.00000000000000,0.00000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("Sketcher::SketchObject","Sketch_FObbrE7WZBSZhAq_1_JPK")
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK").addGeometry(Part.LineSegment(App.Vector(55.71987000000000,47.75631000000001,0.00000000000000),App.Vector(55.71987000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK").addGeometry(Part.LineSegment(App.Vector(55.71987000000000,-47.75631000000001,0.00000000000000),App.Vector(44.28013000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK").addGeometry(Part.LineSegment(App.Vector(44.28013000000000,47.75631000000001,0.00000000000000),App.Vector(44.28013000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK").addGeometry(Part.LineSegment(App.Vector(55.71987000000000,47.75631000000001,0.00000000000000),App.Vector(44.28013000000000,47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Pocket","Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Plane", "plane_Sketch_FObbrE7WZBSZhAq_1_JPO")
origin = App.Vector(0.00000000000000,0.00000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("Sketcher::SketchObject","Sketch_FObbrE7WZBSZhAq_1_JPO")
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPO"), [""])
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO").addGeometry(Part.LineSegment(App.Vector(-30.71987000000000,47.75631000000001,0.00000000000000),App.Vector(-30.71987000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO").addGeometry(Part.LineSegment(App.Vector(-30.71987000000000,-47.75631000000001,0.00000000000000),App.Vector(-19.28013000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO").addGeometry(Part.LineSegment(App.Vector(-19.28013000000000,47.75631000000001,0.00000000000000),App.Vector(-19.28013000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO").addGeometry(Part.LineSegment(App.Vector(-30.71987000000000,47.75631000000001,0.00000000000000),App.Vector(-19.28013000000000,47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Pocket","Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").Profile = App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").Type = 4
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Plane", "plane_Sketch_FObbrE7WZBSZhAq_1_JPS")
origin = App.Vector(0.00000000000000,0.00000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("Sketcher::SketchObject","Sketch_FObbrE7WZBSZhAq_1_JPS")
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FObbrE7WZBSZhAq_1_JPS"), [""])
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS").addGeometry(Part.LineSegment(App.Vector(-55.71987000000000,47.75631000000001,0.00000000000000),App.Vector(-55.71987000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS").addGeometry(Part.LineSegment(App.Vector(-55.71987000000000,-47.75631000000001,0.00000000000000),App.Vector(-44.28013000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS").addGeometry(Part.LineSegment(App.Vector(-44.28013000000000,47.75631000000001,0.00000000000000),App.Vector(-44.28013000000000,-47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS").addGeometry(Part.LineSegment(App.Vector(-55.71987000000000,47.75631000000001,0.00000000000000),App.Vector(-44.28013000000000,47.75631000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fq2WFfuvQrDq2a7_0").newObject("PartDesign::Pocket","Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").Profile = App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS")
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").Length = 25.0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FObbrE7WZBSZhAq_1_JPS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").Type = 4
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FObbrE7WZBSZhAq_1_FAQMQNnTSyb1DMe_1_JPS").Offset = 0
App.ActiveDocument.recompute()

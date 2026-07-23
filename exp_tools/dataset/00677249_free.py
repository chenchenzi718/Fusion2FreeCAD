import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00677249")
App.ActiveDocument.addObject("PartDesign::Body","Body_FMvMNnbshraZFIJ_0")
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").Label = "Body_FMvMNnbshraZFIJ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Plane", "plane_Sketch_FMvMNnbshraZFIJ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMvMNnbshraZFIJ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("Sketcher::SketchObject","Sketch_FMvMNnbshraZFIJ_0_JGC")
App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMvMNnbshraZFIJ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(285.00000000000000,16.00000000000000,0.00000000000000),App.Vector(-285.00000000000000,16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-285.00000000000000,16.00000000000000,0.00000000000000),App.Vector(-285.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(285.00000000000000,-16.00000000000000,0.00000000000000),App.Vector(-285.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC").addGeometry(Part.LineSegment(App.Vector(285.00000000000000,16.00000000000000,0.00000000000000),App.Vector(285.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Pad","Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC")
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC")
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").Length = 13.000000000000002
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMvMNnbshraZFIJ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMvMNnbshraZFIJ_0_F1WcqzDWQs4yKA2_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Plane", "plane_Sketch_F76zq5TDWPljO5Y_1_JJC")
origin = App.Vector(-285.00000000000000,-6.00000000000000,17.50000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F76zq5TDWPljO5Y_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("Sketcher::SketchObject","Sketch_F76zq5TDWPljO5Y_1_JJC")
App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F76zq5TDWPljO5Y_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,-4.50000000000000,0.00000000000000),App.Vector(22.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(22.00000000000000,17.50000000000000,0.00000000000000),App.Vector(-22.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-22.00000000000000,-4.50000000000000,0.00000000000000),App.Vector(-22.00000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC").addGeometry(Part.LineSegment(App.Vector(-22.00000000000000,-4.50000000000000,0.00000000000000),App.Vector(10.00000000000000,-4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Pad","Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC")
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC")
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").Length = 570.0000000000001
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F76zq5TDWPljO5Y_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F76zq5TDWPljO5Y_1_FIMfTv8dhUnF8Xb_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Plane", "plane_Sketch_FQlSsAWIPAF5Q3Y_1_JNC")
origin = App.Vector(-285.00000000000000,-6.00000000000000,17.50000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQlSsAWIPAF5Q3Y_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("Sketcher::SketchObject","Sketch_FQlSsAWIPAF5Q3Y_1_JNC")
App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQlSsAWIPAF5Q3Y_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC").addGeometry(Part.LineSegment(App.Vector(-4.50000000000000,17.50000000000000,0.00000000000000),App.Vector(-7.50000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC").addGeometry(Part.LineSegment(App.Vector(-7.50000000000000,17.50000000000000,0.00000000000000),App.Vector(-7.50000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC").addGeometry(Part.LineSegment(App.Vector(-4.50000000000000,-0.50000000000000,0.00000000000000),App.Vector(-7.50000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC").addGeometry(Part.LineSegment(App.Vector(-4.50000000000000,17.50000000000000,0.00000000000000),App.Vector(-4.50000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Pad","Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC")
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC")
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").Length = 8.0
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQlSsAWIPAF5Q3Y_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQlSsAWIPAF5Q3Y_1_FvoepRLJflOJjlX_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Plane", "plane_Sketch_F1KhFu3eczGXKHP_1_JRC")
origin = App.Vector(-0.00000000000000,-6.00000000000000,35.00000000000000)
x_axis=App.Vector(1.00000000000000,-0.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1KhFu3eczGXKHP_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("Sketcher::SketchObject","Sketch_F1KhFu3eczGXKHP_1_JRC")
App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1KhFu3eczGXKHP_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC").addGeometry(Part.LineSegment(App.Vector(-293.00000000000000,4.50000000000000,0.00000000000000),App.Vector(-285.00000000000000,4.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC").addGeometry(Part.LineSegment(App.Vector(-285.00000000000000,4.50000000000000,0.00000000000000),App.Vector(-285.00000000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC").addGeometry(Part.LineSegment(App.Vector(-293.00000000000000,7.50000000000000,0.00000000000000),App.Vector(-285.00000000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC").addGeometry(Part.LineSegment(App.Vector(-293.00000000000000,4.50000000000000,0.00000000000000),App.Vector(-293.00000000000000,7.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Pad","Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC")
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC")
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").Length = 102.00000000000001
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1KhFu3eczGXKHP_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1KhFu3eczGXKHP_1_F92b9SbrZaXjb6G_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Plane", "plane_Sketch_FjVxTXYgDliJFq3_1_JVC")
origin = App.Vector(-285.00000000000000,0.00000000000000,78.50000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjVxTXYgDliJFq3_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("Sketcher::SketchObject","Sketch_FjVxTXYgDliJFq3_1_JVC")
App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjVxTXYgDliJFq3_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC").addGeometry(Part.LineSegment(App.Vector(-1.50000000000000,58.50000000000001,0.00000000000000),App.Vector(1.50000000000000,58.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC").addGeometry(Part.LineSegment(App.Vector(1.50000000000000,58.50000000000001,0.00000000000000),App.Vector(1.50000000000000,43.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC").addGeometry(Part.LineSegment(App.Vector(1.50000000000000,43.50000000000000,0.00000000000000),App.Vector(-1.50000000000000,43.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC").addGeometry(Part.LineSegment(App.Vector(-1.50000000000000,58.50000000000001,0.00000000000000),App.Vector(-1.50000000000000,43.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Pad","Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC")
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC")
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjVxTXYgDliJFq3_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjVxTXYgDliJFq3_1_FPaSWnf92kZb93c_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Plane", "plane_Sketch_FV2sxZJcNNTumN4_1_JZC")
origin = App.Vector(285.00000000000000,-6.00000000000000,17.50000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FV2sxZJcNNTumN4_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("Sketcher::SketchObject","Sketch_FV2sxZJcNNTumN4_1_JZC")
App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FV2sxZJcNNTumN4_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC").addGeometry(Part.LineSegment(App.Vector(7.50000000000000,17.50000000000000,0.00000000000000),App.Vector(4.50000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC").addGeometry(Part.LineSegment(App.Vector(4.50000000000000,17.50000000000000,0.00000000000000),App.Vector(4.50000000000000,119.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC").addGeometry(Part.LineSegment(App.Vector(7.50000000000000,119.50000000000001,0.00000000000000),App.Vector(4.50000000000000,119.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC").addGeometry(Part.LineSegment(App.Vector(7.50000000000000,17.50000000000000,0.00000000000000),App.Vector(7.50000000000000,119.50000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Pad","Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC")
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC")
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").Length = 8.0
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Plane", "plane_Sketch_FV2sxZJcNNTumN4_1_JZG")
origin = App.Vector(285.00000000000000,-6.00000000000000,17.50000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FV2sxZJcNNTumN4_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("Sketcher::SketchObject","Sketch_FV2sxZJcNNTumN4_1_JZG")
App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FV2sxZJcNNTumN4_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG").addGeometry(Part.LineSegment(App.Vector(7.50000000000000,-0.50000000000000,0.00000000000000),App.Vector(4.50000000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG").addGeometry(Part.LineSegment(App.Vector(4.50000000000000,-0.50000000000000,0.00000000000000),App.Vector(4.50000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG").addGeometry(Part.LineSegment(App.Vector(7.50000000000000,17.50000000000000,0.00000000000000),App.Vector(4.50000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG").addGeometry(Part.LineSegment(App.Vector(7.50000000000000,-0.50000000000000,0.00000000000000),App.Vector(7.50000000000000,17.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Pad","Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG")
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG")
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").Length = 8.0
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FV2sxZJcNNTumN4_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FV2sxZJcNNTumN4_1_F3j8goeYCDCzFMU_1_JZG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Plane", "plane_Sketch_FXQYVlZGS6QxIS2_1_JdC")
origin = App.Vector(285.00000000000000,-0.00000000000000,78.50000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXQYVlZGS6QxIS2_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("Sketcher::SketchObject","Sketch_FXQYVlZGS6QxIS2_1_JdC")
App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXQYVlZGS6QxIS2_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC").addGeometry(Part.LineSegment(App.Vector(-1.50000000000000,58.50000000000001,0.00000000000000),App.Vector(1.50000000000000,58.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC").addGeometry(Part.LineSegment(App.Vector(1.50000000000000,58.50000000000001,0.00000000000000),App.Vector(1.50000000000000,43.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC").addGeometry(Part.LineSegment(App.Vector(1.50000000000000,43.50000000000000,0.00000000000000),App.Vector(-1.50000000000000,43.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC").addGeometry(Part.LineSegment(App.Vector(-1.50000000000000,58.50000000000001,0.00000000000000),App.Vector(-1.50000000000000,43.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FMvMNnbshraZFIJ_0").newObject("PartDesign::Pad","Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC")
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC")
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXQYVlZGS6QxIS2_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXQYVlZGS6QxIS2_1_FeOTOjtsBtz0bJu_1_JdC").Offset = 0
App.ActiveDocument.recompute()

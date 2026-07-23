import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00326639")
App.ActiveDocument.addObject("PartDesign::Body","Body_F2qkXWD6qAi4Z2k_0")
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").Label = "Body_F2qkXWD6qAi4Z2k_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Plane", "plane_Sketch_F2qkXWD6qAi4Z2k_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2qkXWD6qAi4Z2k_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("Sketcher::SketchObject","Sketch_F2qkXWD6qAi4Z2k_0_JGC")
App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2qkXWD6qAi4Z2k_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,-152.40000000000001,0.00000000000000),App.Vector(-152.40000000000001,-152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,-152.40000000000001,0.00000000000000),App.Vector(-152.40000000000001,152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,152.40000000000001,0.00000000000000),App.Vector(-152.40000000000001,152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC").addGeometry(Part.LineSegment(App.Vector(152.40000000000001,-152.40000000000001,0.00000000000000),App.Vector(152.40000000000001,152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Pad","Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC")
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC")
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").Length = 19.05
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2qkXWD6qAi4Z2k_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2qkXWD6qAi4Z2k_0_FBTFLEhdvbQJ8Om_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Plane", "plane_Sketch_FybxoNKM4AAVWFQ_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,19.05000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FybxoNKM4AAVWFQ_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("Sketcher::SketchObject","Sketch_FybxoNKM4AAVWFQ_1_JJC")
App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FybxoNKM4AAVWFQ_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC").addGeometry(Part.LineSegment(App.Vector(114.30000000000000,-114.30000000000000,0.00000000000000),App.Vector(-114.30000000000000,-114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC").addGeometry(Part.LineSegment(App.Vector(-114.30000000000000,-114.30000000000000,0.00000000000000),App.Vector(-114.30000000000000,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC").addGeometry(Part.LineSegment(App.Vector(114.30000000000000,114.30000000000000,0.00000000000000),App.Vector(-114.30000000000000,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC").addGeometry(Part.LineSegment(App.Vector(114.30000000000000,-114.30000000000000,0.00000000000000),App.Vector(114.30000000000000,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Pad","Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC")
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC")
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FybxoNKM4AAVWFQ_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FybxoNKM4AAVWFQ_1_FwiBBuxYsz9CJ52_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Plane", "plane_Sketch_Fl64hWR8plXHUSz_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,44.45000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fl64hWR8plXHUSz_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("Sketcher::SketchObject","Sketch_Fl64hWR8plXHUSz_1_JNC")
App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fl64hWR8plXHUSz_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,-22.22500000000000,0.00000000000000),App.Vector(-44.45000000000000,-22.22500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,-22.22500000000000,0.00000000000000),App.Vector(-44.45000000000000,22.22500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,22.22500000000000,0.00000000000000),App.Vector(-44.45000000000000,22.22500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,-22.22500000000000,0.00000000000000),App.Vector(44.45000000000000,22.22500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Pad","Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC")
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC")
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").Length = 1219.2
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fl64hWR8plXHUSz_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fl64hWR8plXHUSz_1_FMsyJFcMjkf1OIm_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Plane", "plane_Sketch_FEbg6ABWsmkjIr1_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,44.45000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEbg6ABWsmkjIr1_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("Sketcher::SketchObject","Sketch_FEbg6ABWsmkjIr1_1_JRC")
App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEbg6ABWsmkjIr1_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.05000000000000,22.22500000000000,0.00000000000000),App.Vector(-19.05000000000000,22.22500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,22.22500000000000,0.00000000000000),App.Vector(-19.05000000000000,101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC").addGeometry(Part.LineSegment(App.Vector(-19.05000000000000,101.59999999999999,0.00000000000000),App.Vector(19.05000000000000,101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC").addGeometry(Part.LineSegment(App.Vector(19.05000000000000,22.22500000000000,0.00000000000000),App.Vector(19.05000000000000,101.59999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Pad","Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC")
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC")
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").Length = 80.01
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEbg6ABWsmkjIr1_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEbg6ABWsmkjIr1_1_FvOOOQ5onwWrKRq_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Plane", "plane_Sketch_F4rpg8II0VCrlUL_1_JVC")
origin = App.Vector(-19.05000000000000,62.15063000000000,84.69503000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4rpg8II0VCrlUL_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("Sketcher::SketchObject","Sketch_F4rpg8II0VCrlUL_1_JVC")
App.ActiveDocument.getObject("Sketch_F4rpg8II0VCrlUL_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4rpg8II0VCrlUL_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F4rpg8II0VCrlUL_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4rpg8II0VCrlUL_1_JVC").addGeometry(Part.LineSegment(App.Vector(39.92563000000000,39.76497000000000,0.00000000000000),App.Vector(-39.44936999999999,-40.24503000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4rpg8II0VCrlUL_1_JVC").addGeometry(Part.LineSegment(App.Vector(-39.44936999999999,39.76497000000000,0.00000000000000),App.Vector(-39.44936999999999,-40.24503000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4rpg8II0VCrlUL_1_JVC").addGeometry(Part.LineSegment(App.Vector(-39.44936999999999,39.76497000000000,0.00000000000000),App.Vector(39.92563000000000,39.76497000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4rpg8II0VCrlUL_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4rpg8II0VCrlUL_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Pocket","Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC")
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F4rpg8II0VCrlUL_1_JVC")
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4rpg8II0VCrlUL_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4rpg8II0VCrlUL_1_FZVbG3yVbcSvUpe_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Plane", "plane_Sketch_FqQo0mVtrZAPfbT_1_JZC")
origin = App.Vector(-0.00000000000000,-22.22500000000000,1225.54999999999995)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqQo0mVtrZAPfbT_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("Sketcher::SketchObject","Sketch_FqQo0mVtrZAPfbT_1_JZC")
App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqQo0mVtrZAPfbT_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC").addGeometry(Part.LineSegment(App.Vector(254.00000000000000,-292.09999999999991,0.00000000000000),App.Vector(44.45000000000000,-292.09999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,-292.09999999999991,0.00000000000000),App.Vector(44.45000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC").addGeometry(Part.LineSegment(App.Vector(254.00000000000000,-38.10000000000002,0.00000000000000),App.Vector(44.45000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC").addGeometry(Part.LineSegment(App.Vector(254.00000000000000,-292.09999999999991,0.00000000000000),App.Vector(254.00000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Pad","Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC")
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC")
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Plane", "plane_Sketch_FqQo0mVtrZAPfbT_1_JZG")
origin = App.Vector(-0.00000000000000,-22.22500000000000,1225.54999999999995)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqQo0mVtrZAPfbT_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("Sketcher::SketchObject","Sketch_FqQo0mVtrZAPfbT_1_JZG")
App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqQo0mVtrZAPfbT_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG").addGeometry(Part.LineSegment(App.Vector(-254.00000000000000,-292.09999999999991,0.00000000000000),App.Vector(-44.45000000000000,-292.09999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,-292.09999999999991,0.00000000000000),App.Vector(-44.45000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG").addGeometry(Part.LineSegment(App.Vector(-254.00000000000000,-38.10000000000002,0.00000000000000),App.Vector(-44.45000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG").addGeometry(Part.LineSegment(App.Vector(-254.00000000000000,-292.09999999999991,0.00000000000000),App.Vector(-254.00000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Pad","Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG")
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG")
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Plane", "plane_Sketch_FqQo0mVtrZAPfbT_1_JZS")
origin = App.Vector(-0.00000000000000,-22.22500000000000,1225.54999999999995)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqQo0mVtrZAPfbT_1_JZS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("Sketcher::SketchObject","Sketch_FqQo0mVtrZAPfbT_1_JZS")
App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqQo0mVtrZAPfbT_1_JZS"), [""])
App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,-292.09999999999991,0.00000000000000),App.Vector(-44.45000000000000,-292.09999999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS").addGeometry(Part.LineSegment(App.Vector(-44.45000000000000,-292.09999999999991,0.00000000000000),App.Vector(-44.45000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,-38.10000000000002,0.00000000000000),App.Vector(-44.45000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS").addGeometry(Part.LineSegment(App.Vector(44.45000000000000,-292.09999999999991,0.00000000000000),App.Vector(44.45000000000000,-38.10000000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2qkXWD6qAi4Z2k_0").newObject("PartDesign::Pad","Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS")
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").Profile = App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS")
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqQo0mVtrZAPfbT_1_JZS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").Type = 4
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqQo0mVtrZAPfbT_1_FQc165In3EgPT3D_1_JZS").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00487758")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fn5qJsJEd6mQXT4_0")
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").Label = "Body_Fn5qJsJEd6mQXT4_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Plane", "plane_Sketch_Fn5qJsJEd6mQXT4_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fn5qJsJEd6mQXT4_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("Sketcher::SketchObject","Sketch_Fn5qJsJEd6mQXT4_0_JGC")
App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fn5qJsJEd6mQXT4_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-69.84999999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC").addGeometry(Part.LineSegment(App.Vector(-69.84999999999999,0.00000000000000,0.00000000000000),App.Vector(-69.84999999999999,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC").addGeometry(Part.LineSegment(App.Vector(-69.84999999999999,146.05000000000001,0.00000000000000),App.Vector(-69.84999999999999,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,146.05000000000001,0.00000000000000),App.Vector(-69.84999999999999,146.05000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,146.05000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Pad","Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC")
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC")
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Plane", "plane_Sketch_Fn5qJsJEd6mQXT4_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fn5qJsJEd6mQXT4_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("Sketcher::SketchObject","Sketch_Fn5qJsJEd6mQXT4_0_JGG")
App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fn5qJsJEd6mQXT4_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG").addGeometry(Part.LineSegment(App.Vector(-69.84999999999999,0.00000000000000,0.00000000000000),App.Vector(-101.59999999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG").addGeometry(Part.LineSegment(App.Vector(-101.59999999999999,0.00000000000000,0.00000000000000),App.Vector(-101.59999999999999,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG").addGeometry(Part.LineSegment(App.Vector(-69.84999999999999,25.40000000000000,0.00000000000000),App.Vector(-101.59999999999999,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG").addGeometry(Part.LineSegment(App.Vector(-69.84999999999999,0.00000000000000,0.00000000000000),App.Vector(-69.84999999999999,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Pad","Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG")
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG")
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fn5qJsJEd6mQXT4_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fn5qJsJEd6mQXT4_0_FtvLNX4ilMXVV3M_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Plane", "plane_Sketch_F4ys7zc6cvxfZMK_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ys7zc6cvxfZMK_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("Sketcher::SketchObject","Sketch_F4ys7zc6cvxfZMK_1_JJC")
App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ys7zc6cvxfZMK_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,6.35000000000000,0.00000000000000),App.Vector(-6.35000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC").addGeometry(Part.LineSegment(App.Vector(-6.35000000000000,6.35000000000000,0.00000000000000),App.Vector(-6.35000000000000,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,139.69999999999999,0.00000000000000),App.Vector(-6.35000000000000,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Pocket","Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC")
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC")
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").Length = 12.446
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ys7zc6cvxfZMK_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ys7zc6cvxfZMK_1_FHLPA9D2ce1miER_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Plane", "plane_Sketch_FHJhworBSV3Lfjt_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHJhworBSV3Lfjt_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("Sketcher::SketchObject","Sketch_FHJhworBSV3Lfjt_1_JNC")
App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHJhworBSV3Lfjt_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,139.69999999999999,0.00000000000000),App.Vector(-69.84999999999999,139.69999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC").addGeometry(Part.LineSegment(App.Vector(-69.84999999999999,139.69999999999999,0.00000000000000),App.Vector(-69.84999999999999,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,31.75000000000000,0.00000000000000),App.Vector(-69.84999999999999,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,139.69999999999999,0.00000000000000),App.Vector(-63.50000000000000,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Pocket","Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC")
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC")
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").Length = 9.906
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHJhworBSV3Lfjt_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHJhworBSV3Lfjt_1_FKl0RdgKDX5h2RG_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Plane", "plane_Sketch_FLFGN13s969dIi0_1_JSC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLFGN13s969dIi0_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("Sketcher::SketchObject","Sketch_FLFGN13s969dIi0_1_JSC")
App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLFGN13s969dIi0_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC").addGeometry(Part.LineSegment(App.Vector(-101.59999999999999,19.05000000000000,0.00000000000000),App.Vector(-95.25000000000000,19.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC").addGeometry(Part.LineSegment(App.Vector(-95.25000000000000,19.05000000000000,0.00000000000000),App.Vector(-95.25000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC").addGeometry(Part.LineSegment(App.Vector(-95.25000000000000,0.00000000000000,0.00000000000000),App.Vector(-95.25000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC").addGeometry(Part.LineSegment(App.Vector(-101.59999999999999,0.00000000000000,0.00000000000000),App.Vector(-95.25000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC").addGeometry(Part.LineSegment(App.Vector(-101.59999999999999,19.05000000000000,0.00000000000000),App.Vector(-101.59999999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Pocket","Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC")
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC")
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").Length = 10.668000000000001
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").Type = 0
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Plane", "plane_Sketch_FLFGN13s969dIi0_1_JSG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLFGN13s969dIi0_1_JSG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("Sketcher::SketchObject","Sketch_FLFGN13s969dIi0_1_JSG")
App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLFGN13s969dIi0_1_JSG"), [""])
App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG").addGeometry(Part.LineSegment(App.Vector(-95.25000000000000,6.35000000000000,0.00000000000000),App.Vector(-87.63000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG").addGeometry(Part.LineSegment(App.Vector(-87.63000000000000,6.35000000000000,0.00000000000000),App.Vector(-87.63000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG").addGeometry(Part.LineSegment(App.Vector(-95.25000000000000,0.00000000000000,0.00000000000000),App.Vector(-87.63000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG").addGeometry(Part.LineSegment(App.Vector(-95.25000000000000,0.00000000000000,0.00000000000000),App.Vector(-95.25000000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Pocket","Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG")
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").Profile = App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG")
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").Length = 10.668000000000001
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLFGN13s969dIi0_1_JSG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").Type = 0
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLFGN13s969dIi0_1_Fh8gG8m3giwhhSj_1_JSG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Plane", "plane_Sketch_F3N3STMJVDB6xoP_1_JWC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3N3STMJVDB6xoP_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("Sketcher::SketchObject","Sketch_F3N3STMJVDB6xoP_1_JWC")
App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3N3STMJVDB6xoP_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC").addGeometry(Part.LineSegment(App.Vector(-69.84999999999999,25.40000000000000,0.00000000000000),App.Vector(-76.20000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,25.40000000000000,0.00000000000000),App.Vector(-76.20000000000000,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC").addGeometry(Part.LineSegment(App.Vector(-69.84999999999999,31.75000000000000,0.00000000000000),App.Vector(-76.20000000000000,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC").addGeometry(Part.LineSegment(App.Vector(-69.84999999999999,25.40000000000000,0.00000000000000),App.Vector(-69.84999999999999,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Pad","Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC")
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC")
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3N3STMJVDB6xoP_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3N3STMJVDB6xoP_1_FzNsYAu4UiSoUPG_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Plane", "plane_Sketch_FYlnLc6CzZUaFmi_1_JaC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYlnLc6CzZUaFmi_1_JaC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("Sketcher::SketchObject","Sketch_FYlnLc6CzZUaFmi_1_JaC")
App.ActiveDocument.getObject("Sketch_FYlnLc6CzZUaFmi_1_JaC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYlnLc6CzZUaFmi_1_JaC"), [""])
App.ActiveDocument.getObject("Sketch_FYlnLc6CzZUaFmi_1_JaC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYlnLc6CzZUaFmi_1_JaC").addGeometry(Part.Circle(App.Vector(-76.20000000000000,31.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYlnLc6CzZUaFmi_1_JaC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYlnLc6CzZUaFmi_1_JaC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fn5qJsJEd6mQXT4_0").newObject("PartDesign::Pocket","Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC")
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").Profile = App.ActiveDocument.getObject("Sketch_FYlnLc6CzZUaFmi_1_JaC")
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").Length = 8.940800000000001
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYlnLc6CzZUaFmi_1_JaC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").Type = 0
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYlnLc6CzZUaFmi_1_FotjqHGtp9wQvEx_1_JaC").Offset = 0
App.ActiveDocument.recompute()

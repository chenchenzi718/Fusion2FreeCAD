import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00685969")
App.ActiveDocument.addObject("PartDesign::Body","Body_FHs3kIZWpuQF9EF_0")
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").Label = "Body_FHs3kIZWpuQF9EF_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Plane", "plane_Sketch_FHs3kIZWpuQF9EF_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHs3kIZWpuQF9EF_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("Sketcher::SketchObject","Sketch_FHs3kIZWpuQF9EF_0_JGC")
App.ActiveDocument.getObject("Sketch_FHs3kIZWpuQF9EF_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHs3kIZWpuQF9EF_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FHs3kIZWpuQF9EF_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHs3kIZWpuQF9EF_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.40000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHs3kIZWpuQF9EF_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHs3kIZWpuQF9EF_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Pad","Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC")
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FHs3kIZWpuQF9EF_0_JGC")
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHs3kIZWpuQF9EF_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHs3kIZWpuQF9EF_0_FXfIpFR01p29Mmo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Plane", "plane_Sketch_F64gyVz0g06AoSj_2_JLC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("Sketcher::SketchObject","Sketch_F64gyVz0g06AoSj_2_JLC")
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLC"), [""])
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLC").addGeometry(Part.Circle(App.Vector(0.00000000000000,19.05000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Pad","Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLC")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Plane", "plane_Sketch_F64gyVz0g06AoSj_2_JLG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("Sketcher::SketchObject","Sketch_F64gyVz0g06AoSj_2_JLG")
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLG"), [""])
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLG").addGeometry(Part.Circle(App.Vector(-16.49778000000000,9.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Pad","Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLG")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Plane", "plane_Sketch_F64gyVz0g06AoSj_2_JLK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("Sketcher::SketchObject","Sketch_F64gyVz0g06AoSj_2_JLK")
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLK"), [""])
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLK").addGeometry(Part.Circle(App.Vector(-16.49778000000000,-9.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Pad","Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLK")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Plane", "plane_Sketch_F64gyVz0g06AoSj_2_JLO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("Sketcher::SketchObject","Sketch_F64gyVz0g06AoSj_2_JLO")
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLO"), [""])
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLO").addGeometry(Part.Circle(App.Vector(0.00000000000000,-19.05000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Pad","Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLO")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Plane", "plane_Sketch_F64gyVz0g06AoSj_2_JLS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("Sketcher::SketchObject","Sketch_F64gyVz0g06AoSj_2_JLS")
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLS"), [""])
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLS").addGeometry(Part.Circle(App.Vector(16.49778000000000,-9.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Pad","Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").Profile = App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLS")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").Type = 4
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Plane", "plane_Sketch_F64gyVz0g06AoSj_2_JLW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("Sketcher::SketchObject","Sketch_F64gyVz0g06AoSj_2_JLW")
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F64gyVz0g06AoSj_2_JLW"), [""])
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLW").addGeometry(Part.Circle(App.Vector(16.49778000000000,9.52500000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Pad","Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").Profile = App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLW")
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F64gyVz0g06AoSj_2_JLW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").Type = 4
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F64gyVz0g06AoSj_2_FZFBEnQ7yz3J3gs_1_JLW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Plane", "plane_Sketch_Fx9XTff4jHfhhfG_1_JJC")
origin = App.Vector(0.00000000000000,-12.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fx9XTff4jHfhhfG_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("Sketcher::SketchObject","Sketch_Fx9XTff4jHfhhfG_1_JJC")
App.ActiveDocument.getObject("Sketch_Fx9XTff4jHfhhfG_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fx9XTff4jHfhhfG_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fx9XTff4jHfhhfG_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fx9XTff4jHfhhfG_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,10.16000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.44500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fx9XTff4jHfhhfG_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fx9XTff4jHfhhfG_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Pad","Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC")
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fx9XTff4jHfhhfG_1_JJC")
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fx9XTff4jHfhhfG_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fx9XTff4jHfhhfG_1_FcvVCcHYGWaVV0R_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Plane", "plane_Sketch_FW2wmERPuQ13b4p_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FW2wmERPuQ13b4p_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("Sketcher::SketchObject","Sketch_FW2wmERPuQ13b4p_1_JRC")
App.ActiveDocument.getObject("Sketch_FW2wmERPuQ13b4p_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FW2wmERPuQ13b4p_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FW2wmERPuQ13b4p_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FW2wmERPuQ13b4p_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.30200000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FW2wmERPuQ13b4p_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FW2wmERPuQ13b4p_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FHs3kIZWpuQF9EF_0").newObject("PartDesign::Pocket","Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC")
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FW2wmERPuQ13b4p_1_JRC")
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FW2wmERPuQ13b4p_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FW2wmERPuQ13b4p_1_FIOJHYQ14FZRAZP_1_JRC").Offset = 0
App.ActiveDocument.recompute()

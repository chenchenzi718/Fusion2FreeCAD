import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00640385")
App.ActiveDocument.addObject("PartDesign::Body","Body_FzMzH9OE5gCskng_0")
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").Label = "Body_FzMzH9OE5gCskng_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_FzMzH9OE5gCskng_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzMzH9OE5gCskng_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_FzMzH9OE5gCskng_0_JGC")
App.ActiveDocument.getObject("Sketch_FzMzH9OE5gCskng_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzMzH9OE5gCskng_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FzMzH9OE5gCskng_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzMzH9OE5gCskng_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),23.27758000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzMzH9OE5gCskng_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzMzH9OE5gCskng_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pad","Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC")
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FzMzH9OE5gCskng_0_JGC")
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzMzH9OE5gCskng_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzMzH9OE5gCskng_0_FZcgxvOQr6ocEuX_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_F0G71qG5pGzhNQM_1_JJC")
origin = App.Vector(0.00000000000000,-12.70000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0G71qG5pGzhNQM_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_F0G71qG5pGzhNQM_1_JJC")
App.ActiveDocument.getObject("Sketch_F0G71qG5pGzhNQM_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0G71qG5pGzhNQM_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F0G71qG5pGzhNQM_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0G71qG5pGzhNQM_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),16.17476000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0G71qG5pGzhNQM_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0G71qG5pGzhNQM_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pocket","Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC")
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F0G71qG5pGzhNQM_1_JJC")
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0G71qG5pGzhNQM_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0G71qG5pGzhNQM_1_FU3PhXsU4fwNOF7_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_FXZCQLqEukk0U0V_1_JNC")
origin = App.Vector(20.40860000000000,0.00000000000000,-1.87704000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FXZCQLqEukk0U0V_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_FXZCQLqEukk0U0V_1_JNC")
App.ActiveDocument.getObject("Sketch_FXZCQLqEukk0U0V_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FXZCQLqEukk0U0V_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FXZCQLqEukk0U0V_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FXZCQLqEukk0U0V_1_JNC").addGeometry(Part.Circle(App.Vector(20.40860000000000,1.87704000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),17.93687000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FXZCQLqEukk0U0V_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FXZCQLqEukk0U0V_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pad","Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC")
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FXZCQLqEukk0U0V_1_JNC")
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FXZCQLqEukk0U0V_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FXZCQLqEukk0U0V_1_F3jWQ1leZPuQt6C_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_FC7rL7bEwq5FB0S_1_JRC")
origin = App.Vector(0.00000000000000,-9.52500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_FC7rL7bEwq5FB0S_1_JRC")
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRC").addGeometry(Part.Circle(App.Vector(-11.61606000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.88121000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pocket","Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRC")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_FC7rL7bEwq5FB0S_1_JRG")
origin = App.Vector(0.00000000000000,-9.52500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_FC7rL7bEwq5FB0S_1_JRG")
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRG").addGeometry(Part.Circle(App.Vector(-3.58956000000000,-11.04753000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.88121000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pocket","Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRG")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_FC7rL7bEwq5FB0S_1_JRK")
origin = App.Vector(0.00000000000000,-9.52500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_FC7rL7bEwq5FB0S_1_JRK")
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRK").addGeometry(Part.Circle(App.Vector(9.39759000000000,-6.82775000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.88121000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pocket","Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRK")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_FC7rL7bEwq5FB0S_1_JRO")
origin = App.Vector(0.00000000000000,-9.52500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_FC7rL7bEwq5FB0S_1_JRO")
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRO").addGeometry(Part.Circle(App.Vector(9.39759000000000,6.82775000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.88121000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pocket","Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRO")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_FC7rL7bEwq5FB0S_1_JRS")
origin = App.Vector(0.00000000000000,-9.52500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_FC7rL7bEwq5FB0S_1_JRS")
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FC7rL7bEwq5FB0S_1_JRS"), [""])
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRS").addGeometry(Part.Circle(App.Vector(-3.58956000000000,11.04753000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.88121000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pocket","Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").Profile = App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRS")
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FC7rL7bEwq5FB0S_1_JRS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").Type = 4
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FC7rL7bEwq5FB0S_1_FwTF7b067W5OJ6d_1_JRS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_FQunqjKWAnEFu8z_1_JWC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQunqjKWAnEFu8z_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_FQunqjKWAnEFu8z_1_JWC")
App.ActiveDocument.getObject("Sketch_FQunqjKWAnEFu8z_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQunqjKWAnEFu8z_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FQunqjKWAnEFu8z_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQunqjKWAnEFu8z_1_JWC").addGeometry(Part.Circle(App.Vector(0.00000000000000,4.65513000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.65513000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQunqjKWAnEFu8z_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQunqjKWAnEFu8z_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pad","Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC")
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FQunqjKWAnEFu8z_1_JWC")
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQunqjKWAnEFu8z_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQunqjKWAnEFu8z_1_FHKnaYpAH2s7uMW_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Plane", "plane_Sketch_Fz3hjLP6F7HMnom_1_JaC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fz3hjLP6F7HMnom_1_JaC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("Sketcher::SketchObject","Sketch_Fz3hjLP6F7HMnom_1_JaC")
App.ActiveDocument.getObject("Sketch_Fz3hjLP6F7HMnom_1_JaC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fz3hjLP6F7HMnom_1_JaC"), [""])
App.ActiveDocument.getObject("Sketch_Fz3hjLP6F7HMnom_1_JaC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fz3hjLP6F7HMnom_1_JaC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-6.52194000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.76786000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fz3hjLP6F7HMnom_1_JaC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fz3hjLP6F7HMnom_1_JaC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FzMzH9OE5gCskng_0").newObject("PartDesign::Pad","Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC")
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").Profile = App.ActiveDocument.getObject("Sketch_Fz3hjLP6F7HMnom_1_JaC")
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fz3hjLP6F7HMnom_1_JaC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").Type = 4
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fz3hjLP6F7HMnom_1_FoFJM6ZDxHBKnMM_1_JaC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00325035")
App.ActiveDocument.addObject("PartDesign::Body","Body_F1D8h885qxbgY6e_0")
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").Label = "Body_F1D8h885qxbgY6e_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_F1D8h885qxbgY6e_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1D8h885qxbgY6e_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_F1D8h885qxbgY6e_0_JGC")
App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1D8h885qxbgY6e_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").addGeometry(Part.LineSegment(App.Vector(-14.28750000000000,12.70000000000000,0.00000000000000),App.Vector(-11.11250000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").addGeometry(Part.LineSegment(App.Vector(-11.11250000000000,12.70000000000000,0.00000000000000),App.Vector(-11.11250000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").addGeometry(Part.LineSegment(App.Vector(14.28750000000000,-12.70000000000000,0.00000000000000),App.Vector(-11.11250000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").addGeometry(Part.LineSegment(App.Vector(14.28750000000000,-12.70000000000000,0.00000000000000),App.Vector(14.28750000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").addGeometry(Part.LineSegment(App.Vector(-14.28750000000000,-15.87500000000000,0.00000000000000),App.Vector(14.28750000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").addGeometry(Part.LineSegment(App.Vector(-14.28750000000000,-12.70000000000000,0.00000000000000),App.Vector(-14.28750000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").addGeometry(Part.LineSegment(App.Vector(-14.28750000000000,12.70000000000000,0.00000000000000),App.Vector(-14.28750000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pad","Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC")
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC")
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").Length = 28.575000000000003
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_F4VOkiXwb8ccahU_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_F1D8h885qxbgY6e_0_JGW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1D8h885qxbgY6e_0_JGW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_F1D8h885qxbgY6e_0_JGW")
App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1D8h885qxbgY6e_0_JGW"), [""])
App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").addGeometry(Part.LineSegment(App.Vector(14.28750000000000,12.70000000000000,0.00000000000000),App.Vector(-11.11250000000000,12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").addGeometry(Part.LineSegment(App.Vector(-11.11250000000000,12.70000000000000,0.00000000000000),App.Vector(-11.11250000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").addGeometry(Part.LineSegment(App.Vector(14.28750000000000,-12.70000000000000,0.00000000000000),App.Vector(-11.11250000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").addGeometry(Part.LineSegment(App.Vector(14.28750000000000,12.70000000000000,0.00000000000000),App.Vector(14.28750000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").addGeometry(Part.Circle(App.Vector(-4.76250000000000,-6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").addGeometry(Part.Circle(App.Vector(-4.76250000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").addGeometry(Part.Circle(App.Vector(7.93750000000000,6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").addGeometry(Part.Circle(App.Vector(7.93750000000000,-6.35000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pad","Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW")
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").Profile = App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW")
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1D8h885qxbgY6e_0_JGW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").Type = 4
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1D8h885qxbgY6e_0_FRk4UJ02QjpnJ11_1_JGW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_FmeW66GMu88aVkK_1_JLC")
origin = App.Vector(-14.28750000000000,-1.58750000000000,14.28750000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmeW66GMu88aVkK_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_FmeW66GMu88aVkK_1_JLC")
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmeW66GMu88aVkK_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLC").addGeometry(Part.Circle(App.Vector(-7.93750000000000,7.93750000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pocket","Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC")
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLC")
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_FmeW66GMu88aVkK_1_JLG")
origin = App.Vector(-14.28750000000000,-1.58750000000000,14.28750000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmeW66GMu88aVkK_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_FmeW66GMu88aVkK_1_JLG")
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmeW66GMu88aVkK_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLG").addGeometry(Part.Circle(App.Vector(4.76250000000000,7.93750000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pocket","Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG")
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLG")
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_FmeW66GMu88aVkK_1_JLK")
origin = App.Vector(-14.28750000000000,-1.58750000000000,14.28750000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmeW66GMu88aVkK_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_FmeW66GMu88aVkK_1_JLK")
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmeW66GMu88aVkK_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLK").addGeometry(Part.Circle(App.Vector(4.76250000000000,-4.76250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pocket","Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK")
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLK")
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_FmeW66GMu88aVkK_1_JLO")
origin = App.Vector(-14.28750000000000,-1.58750000000000,14.28750000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmeW66GMu88aVkK_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_FmeW66GMu88aVkK_1_JLO")
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmeW66GMu88aVkK_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLO").addGeometry(Part.Circle(App.Vector(-7.93750000000000,-4.76250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pocket","Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO")
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLO")
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmeW66GMu88aVkK_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmeW66GMu88aVkK_1_FZA4JMwfIDYtWCB_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_FkcNsH9gMgOSLWz_1_JNG")
origin = App.Vector(-0.00000000000000,-15.87500000000000,14.28750000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkcNsH9gMgOSLWz_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_FkcNsH9gMgOSLWz_1_JNG")
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkcNsH9gMgOSLWz_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNG").addGeometry(Part.Circle(App.Vector(7.93750000000000,7.93750000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pocket","Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG")
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNG")
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_FkcNsH9gMgOSLWz_1_JNK")
origin = App.Vector(-0.00000000000000,-15.87500000000000,14.28750000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkcNsH9gMgOSLWz_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_FkcNsH9gMgOSLWz_1_JNK")
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkcNsH9gMgOSLWz_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNK").addGeometry(Part.Circle(App.Vector(7.93750000000000,-4.76250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pocket","Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK")
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNK")
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_FkcNsH9gMgOSLWz_1_JNO")
origin = App.Vector(-0.00000000000000,-15.87500000000000,14.28750000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkcNsH9gMgOSLWz_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_FkcNsH9gMgOSLWz_1_JNO")
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkcNsH9gMgOSLWz_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNO").addGeometry(Part.Circle(App.Vector(-4.76250000000000,-4.76250000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pocket","Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO")
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNO")
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Plane", "plane_Sketch_FkcNsH9gMgOSLWz_1_JNC")
origin = App.Vector(-0.00000000000000,-15.87500000000000,14.28750000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkcNsH9gMgOSLWz_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("Sketcher::SketchObject","Sketch_FkcNsH9gMgOSLWz_1_JNC")
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkcNsH9gMgOSLWz_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNC").addGeometry(Part.Circle(App.Vector(-4.76250000000000,7.93750000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.98438000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1D8h885qxbgY6e_0").newObject("PartDesign::Pocket","Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC")
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNC")
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkcNsH9gMgOSLWz_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkcNsH9gMgOSLWz_1_FnwBm2ve1ozAXu6_1_JNC").Offset = 0
App.ActiveDocument.recompute()

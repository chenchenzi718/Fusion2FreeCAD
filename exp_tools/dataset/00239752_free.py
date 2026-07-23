import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00239752")
App.ActiveDocument.addObject("PartDesign::Body","Body_FCiNvxUYYLoATHA_0")
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").Label = "Body_FCiNvxUYYLoATHA_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Plane", "plane_Sketch_FCiNvxUYYLoATHA_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCiNvxUYYLoATHA_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("Sketcher::SketchObject","Sketch_FCiNvxUYYLoATHA_0_JGC")
App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCiNvxUYYLoATHA_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-35.81077000000000,30.67423000000000,0.00000000000000),App.Vector(14.27570000000000,30.67423000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC").addGeometry(Part.LineSegment(App.Vector(14.27570000000000,30.67423000000000,0.00000000000000),App.Vector(14.27570000000000,-99.32576999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-35.81077000000000,-99.32576999999999,0.00000000000000),App.Vector(14.27570000000000,-99.32576999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC").addGeometry(Part.LineSegment(App.Vector(-35.81077000000000,30.67423000000000,0.00000000000000),App.Vector(-35.81077000000000,-99.32576999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Pad","Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC")
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC")
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCiNvxUYYLoATHA_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCiNvxUYYLoATHA_0_Fsid67pTBZisGyl_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Plane", "plane_Sketch_FFWSBYiSdTq6Ifk_1_JJK")
origin = App.Vector(-30.31077000000000,-34.32577000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("Sketcher::SketchObject","Sketch_FFWSBYiSdTq6Ifk_1_JJK")
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJK").addGeometry(Part.Circle(App.Vector(19.33065000000000,-55.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Pocket","Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJK")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Plane", "plane_Sketch_FFWSBYiSdTq6Ifk_1_JJC")
origin = App.Vector(-30.31077000000000,-34.32577000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("Sketcher::SketchObject","Sketch_FFWSBYiSdTq6Ifk_1_JJC")
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJC").addGeometry(Part.Circle(App.Vector(38.48728000000000,57.57917999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Pocket","Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJC")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Plane", "plane_Sketch_FFWSBYiSdTq6Ifk_1_JJG")
origin = App.Vector(-30.31077000000000,-34.32577000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("Sketcher::SketchObject","Sketch_FFWSBYiSdTq6Ifk_1_JJG")
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJG").addGeometry(Part.Circle(App.Vector(0.59182000000000,57.57917999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Pocket","Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJG")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FGUwLwKq627DeTG_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Plane", "plane_Sketch_FFWSBYiSdTq6Ifk_1_JJO")
origin = App.Vector(-30.31077000000000,-34.32577000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("Sketcher::SketchObject","Sketch_FFWSBYiSdTq6Ifk_1_JJO")
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").addGeometry(Part.LineSegment(App.Vector(36.43769000000000,61.12918000000000,0.00000000000000),App.Vector(40.53687000000000,61.12918000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").addGeometry(Part.LineSegment(App.Vector(40.53687000000000,61.12918000000000,0.00000000000000),App.Vector(42.58647000000000,57.57917999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").addGeometry(Part.LineSegment(App.Vector(42.58647000000000,57.57917999999999,0.00000000000000),App.Vector(40.53687000000000,54.02918000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").addGeometry(Part.LineSegment(App.Vector(40.53687000000000,54.02918000000000,0.00000000000000),App.Vector(36.43769000000000,54.02918000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").addGeometry(Part.LineSegment(App.Vector(36.43769000000000,54.02918000000000,0.00000000000000),App.Vector(34.38809000000001,57.57917999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").addGeometry(Part.LineSegment(App.Vector(36.43769000000000,61.12918000000000,0.00000000000000),App.Vector(34.38809000000001,57.57917999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").addGeometry(Part.Circle(App.Vector(38.48728000000000,57.57917999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Pocket","Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").Length = 4.0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Plane", "plane_Sketch_FFWSBYiSdTq6Ifk_1_JJS")
origin = App.Vector(-30.31077000000000,-34.32577000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("Sketcher::SketchObject","Sketch_FFWSBYiSdTq6Ifk_1_JJS")
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").addGeometry(Part.LineSegment(App.Vector(-3.50000000000000,57.33358000000000,0.00000000000000),App.Vector(-1.66679000000000,61.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").addGeometry(Part.LineSegment(App.Vector(-1.66679000000000,61.00000000000000,0.00000000000000),App.Vector(2.42503000000000,61.24560000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").addGeometry(Part.LineSegment(App.Vector(2.42503000000000,61.24560000000000,0.00000000000000),App.Vector(4.68364000000000,57.82478000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").addGeometry(Part.LineSegment(App.Vector(4.68364000000000,57.82478000000000,0.00000000000000),App.Vector(2.85043000000000,54.15836000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").addGeometry(Part.LineSegment(App.Vector(2.85043000000000,54.15836000000000,0.00000000000000),App.Vector(-1.24139000000000,53.91276000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").addGeometry(Part.LineSegment(App.Vector(-3.50000000000000,57.33358000000000,0.00000000000000),App.Vector(-1.24139000000000,53.91276000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").addGeometry(Part.Circle(App.Vector(0.59182000000000,57.57917999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Pocket","Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").Length = 4.0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Plane", "plane_Sketch_FFWSBYiSdTq6Ifk_1_JJW")
origin = App.Vector(-30.31077000000000,-34.32577000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("Sketcher::SketchObject","Sketch_FFWSBYiSdTq6Ifk_1_JJW")
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFWSBYiSdTq6Ifk_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").addGeometry(Part.LineSegment(App.Vector(14.37849000000000,-51.50341000000001,0.00000000000000),App.Vector(19.88270000000000,-48.96301000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").addGeometry(Part.LineSegment(App.Vector(19.88270000000000,-48.96301000000001,0.00000000000000),App.Vector(24.83487000000000,-52.45959000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").addGeometry(Part.LineSegment(App.Vector(24.83487000000000,-52.45959000000001,0.00000000000000),App.Vector(24.28282000000000,-58.49658000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").addGeometry(Part.LineSegment(App.Vector(24.28282000000000,-58.49658000000000,0.00000000000000),App.Vector(18.77860000000000,-61.03699000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").addGeometry(Part.LineSegment(App.Vector(18.77860000000000,-61.03699000000000,0.00000000000000),App.Vector(13.82644000000000,-57.54040000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").addGeometry(Part.LineSegment(App.Vector(14.37849000000000,-51.50341000000001,0.00000000000000),App.Vector(13.82644000000000,-57.54040000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").addGeometry(Part.Circle(App.Vector(19.33065000000000,-55.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Pocket","Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW")
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").Length = 4.0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFWSBYiSdTq6Ifk_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFWSBYiSdTq6Ifk_1_FWLI2bBz4noTenG_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Plane", "plane_Sketch_FDJdw3EkaIKN6bA_1_JPO")
origin = App.Vector(-30.31077000000000,-34.32577000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDJdw3EkaIKN6bA_1_JPO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("Sketcher::SketchObject","Sketch_FDJdw3EkaIKN6bA_1_JPO")
App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDJdw3EkaIKN6bA_1_JPO"), [""])
App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO").addGeometry(Part.LineSegment(App.Vector(30.58647000000000,65.00000000000000,0.00000000000000),App.Vector(33.58647000000000,65.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO").addGeometry(Part.LineSegment(App.Vector(33.58647000000000,65.00000000000000,0.00000000000000),App.Vector(33.58647000000000,-65.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO").addGeometry(Part.LineSegment(App.Vector(30.58647000000000,-65.00000000000000,0.00000000000000),App.Vector(33.58647000000000,-65.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO").addGeometry(Part.LineSegment(App.Vector(30.58647000000000,65.00000000000000,0.00000000000000),App.Vector(30.58647000000000,-65.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Pad","Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO")
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").Profile = App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO")
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").Length = 3.0
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").Type = 4
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Plane", "plane_Sketch_FDJdw3EkaIKN6bA_1_JPS")
origin = App.Vector(-30.31077000000000,-34.32577000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDJdw3EkaIKN6bA_1_JPS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("Sketcher::SketchObject","Sketch_FDJdw3EkaIKN6bA_1_JPS")
App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDJdw3EkaIKN6bA_1_JPS"), [""])
App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS").addGeometry(Part.LineSegment(App.Vector(5.50000000000000,65.00000000000000,0.00000000000000),App.Vector(8.50000000000000,65.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS").addGeometry(Part.LineSegment(App.Vector(8.50000000000000,65.00000000000000,0.00000000000000),App.Vector(8.50000000000000,-65.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS").addGeometry(Part.LineSegment(App.Vector(5.50000000000000,-65.00000000000000,0.00000000000000),App.Vector(8.50000000000000,-65.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS").addGeometry(Part.LineSegment(App.Vector(5.50000000000000,65.00000000000000,0.00000000000000),App.Vector(5.50000000000000,-65.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCiNvxUYYLoATHA_0").newObject("PartDesign::Pad","Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS")
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").Profile = App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS")
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").Length = 3.0
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDJdw3EkaIKN6bA_1_JPS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").Type = 4
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDJdw3EkaIKN6bA_1_FNTGAfB6U3bVzxV_1_JPS").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00179056")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fix4DWOj4hVxYb6_0")
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").Label = "Body_Fix4DWOj4hVxYb6_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Plane", "plane_Sketch_Fix4DWOj4hVxYb6_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fix4DWOj4hVxYb6_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("Sketcher::SketchObject","Sketch_Fix4DWOj4hVxYb6_0_JGC")
App.ActiveDocument.getObject("Sketch_Fix4DWOj4hVxYb6_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fix4DWOj4hVxYb6_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fix4DWOj4hVxYb6_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fix4DWOj4hVxYb6_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),21.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fix4DWOj4hVxYb6_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fix4DWOj4hVxYb6_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Pad","Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC")
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fix4DWOj4hVxYb6_0_JGC")
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").Length = 10.0
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fix4DWOj4hVxYb6_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fix4DWOj4hVxYb6_0_FwgiYvmDDWSY6XD_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Plane", "plane_Sketch_FwxRmntAPzE6C9v_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwxRmntAPzE6C9v_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("Sketcher::SketchObject","Sketch_FwxRmntAPzE6C9v_1_JJC")
App.ActiveDocument.getObject("Sketch_FwxRmntAPzE6C9v_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwxRmntAPzE6C9v_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FwxRmntAPzE6C9v_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwxRmntAPzE6C9v_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwxRmntAPzE6C9v_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwxRmntAPzE6C9v_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Pad","Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC")
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FwxRmntAPzE6C9v_1_JJC")
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").Length = 15.0
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwxRmntAPzE6C9v_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwxRmntAPzE6C9v_1_FcVRg7Edy7WZ1yr_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Plane", "plane_Sketch_FckSTECwR14LDd1_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FckSTECwR14LDd1_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("Sketcher::SketchObject","Sketch_FckSTECwR14LDd1_1_JNC")
App.ActiveDocument.getObject("Sketch_FckSTECwR14LDd1_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FckSTECwR14LDd1_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FckSTECwR14LDd1_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FckSTECwR14LDd1_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FckSTECwR14LDd1_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FckSTECwR14LDd1_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Pocket","Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC")
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FckSTECwR14LDd1_1_JNC")
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").Length = 30.0
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FckSTECwR14LDd1_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FckSTECwR14LDd1_1_Fm3hBEPOT2oDLuz_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Plane", "plane_Sketch_Faw4hZIIng0nFZ7_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("Sketcher::SketchObject","Sketch_Faw4hZIIng0nFZ7_1_JRC")
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRC").addGeometry(Part.Circle(App.Vector(17.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Pocket","Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRC")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Plane", "plane_Sketch_Faw4hZIIng0nFZ7_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("Sketcher::SketchObject","Sketch_Faw4hZIIng0nFZ7_1_JRG")
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRG").addGeometry(Part.Circle(App.Vector(8.50000000000000,14.72243000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Pocket","Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRG")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").Length = 25.0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Plane", "plane_Sketch_Faw4hZIIng0nFZ7_1_JRK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("Sketcher::SketchObject","Sketch_Faw4hZIIng0nFZ7_1_JRK")
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRK").addGeometry(Part.Circle(App.Vector(-8.50000000000000,14.72243000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Pocket","Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRK")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").Length = 25.0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Plane", "plane_Sketch_Faw4hZIIng0nFZ7_1_JRO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("Sketcher::SketchObject","Sketch_Faw4hZIIng0nFZ7_1_JRO")
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRO").addGeometry(Part.Circle(App.Vector(-17.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Pocket","Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRO")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").Length = 25.0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Plane", "plane_Sketch_Faw4hZIIng0nFZ7_1_JRS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("Sketcher::SketchObject","Sketch_Faw4hZIIng0nFZ7_1_JRS")
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRS"), [""])
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRS").addGeometry(Part.Circle(App.Vector(-8.50000000000000,-14.72243000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Pocket","Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").Profile = App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRS")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").Length = 25.0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").Type = 4
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").Reversed = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Plane", "plane_Sketch_Faw4hZIIng0nFZ7_1_JRW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("Sketcher::SketchObject","Sketch_Faw4hZIIng0nFZ7_1_JRW")
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Faw4hZIIng0nFZ7_1_JRW"), [""])
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRW").addGeometry(Part.Circle(App.Vector(8.50000000000000,-14.72243000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fix4DWOj4hVxYb6_0").newObject("PartDesign::Pocket","Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").Profile = App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRW")
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").Length = 25.0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Faw4hZIIng0nFZ7_1_JRW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").Type = 4
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").UpToFace = None
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").Reversed = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").Midplane = 0
App.ActiveDocument.getObject("Extrude_Faw4hZIIng0nFZ7_1_FBsgl8IV3CGLLna_1_JRW").Offset = 0
App.ActiveDocument.recompute()

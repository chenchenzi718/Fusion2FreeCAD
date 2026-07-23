import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00571757")
App.ActiveDocument.addObject("PartDesign::Body","Body_F4KkMe6tiqeK68K_0")
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").Label = "Body_F4KkMe6tiqeK68K_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_F4KkMe6tiqeK68K_0_JHC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4KkMe6tiqeK68K_0_JHC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_F4KkMe6tiqeK68K_0_JHC")
App.ActiveDocument.getObject("Sketch_F4KkMe6tiqeK68K_0_JHC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4KkMe6tiqeK68K_0_JHC"), [""])
App.ActiveDocument.getObject("Sketch_F4KkMe6tiqeK68K_0_JHC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4KkMe6tiqeK68K_0_JHC").addGeometry(Part.Circle(App.Vector(0.03780000000000,1.33695000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),139.69999999999999),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4KkMe6tiqeK68K_0_JHC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4KkMe6tiqeK68K_0_JHC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pad","Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC")
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").Profile = App.ActiveDocument.getObject("Sketch_F4KkMe6tiqeK68K_0_JHC")
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4KkMe6tiqeK68K_0_JHC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").Type = 4
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4KkMe6tiqeK68K_0_FmSx72dNJv1OGmQ_0_JHC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_F2sSYYqAJjK8bpL_1_JTe")
origin = App.Vector(0.03780000000000,0.00000000000000,1.33695000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_F2sSYYqAJjK8bpL_1_JTe")
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTe"), [""])
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTe").addGeometry(Part.Circle(App.Vector(-85.31242999999999,85.31244000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.11250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pocket","Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").Profile = App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTe")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").Type = 4
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_F2sSYYqAJjK8bpL_1_JTC")
origin = App.Vector(0.03780000000000,0.00000000000000,1.33695000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_F2sSYYqAJjK8bpL_1_JTC")
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTC").addGeometry(Part.Circle(App.Vector(0.00000000000000,120.64999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.11250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pocket","Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTC")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_F2sSYYqAJjK8bpL_1_JTG")
origin = App.Vector(0.03780000000000,0.00000000000000,1.33695000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_F2sSYYqAJjK8bpL_1_JTG")
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTG"), [""])
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTG").addGeometry(Part.Circle(App.Vector(85.31244000000001,85.31244000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.11250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pocket","Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").Profile = App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTG")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").Type = 4
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_F2sSYYqAJjK8bpL_1_JTK")
origin = App.Vector(0.03780000000000,0.00000000000000,1.33695000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_F2sSYYqAJjK8bpL_1_JTK")
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTK"), [""])
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTK").addGeometry(Part.Circle(App.Vector(120.65000000000001,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.11250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pocket","Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").Profile = App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTK")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").Type = 4
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_F2sSYYqAJjK8bpL_1_JTO")
origin = App.Vector(0.03780000000000,0.00000000000000,1.33695000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_F2sSYYqAJjK8bpL_1_JTO")
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTO"), [""])
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTO").addGeometry(Part.Circle(App.Vector(85.31244000000001,-85.31243000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.11250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pocket","Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").Profile = App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTO")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").Type = 4
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_F2sSYYqAJjK8bpL_1_JTS")
origin = App.Vector(0.03780000000000,0.00000000000000,1.33695000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_F2sSYYqAJjK8bpL_1_JTS")
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTS"), [""])
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTS").addGeometry(Part.Circle(App.Vector(0.00000000000000,-120.65000000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.11250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pocket","Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").Profile = App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTS")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").Type = 4
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_F2sSYYqAJjK8bpL_1_JTW")
origin = App.Vector(0.03780000000000,0.00000000000000,1.33695000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_F2sSYYqAJjK8bpL_1_JTW")
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTW"), [""])
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTW").addGeometry(Part.Circle(App.Vector(-85.31242999999999,-85.31243000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.11250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pocket","Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").Profile = App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTW")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").Type = 4
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_F2sSYYqAJjK8bpL_1_JTa")
origin = App.Vector(0.03780000000000,0.00000000000000,1.33695000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_F2sSYYqAJjK8bpL_1_JTa")
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2sSYYqAJjK8bpL_1_JTa"), [""])
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTa").addGeometry(Part.Circle(App.Vector(-120.64999999999999,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),11.11250000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pocket","Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").Profile = App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTa")
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2sSYYqAJjK8bpL_1_JTa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").Type = 4
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2sSYYqAJjK8bpL_1_F2HlzhxeQebbEAt_1_JTa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Plane", "plane_Sketch_FT3MJFDAUPEhyxq_1_JXC")
origin = App.Vector(0.03780000000000,-101.59999999999999,1.33695000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FT3MJFDAUPEhyxq_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("Sketcher::SketchObject","Sketch_FT3MJFDAUPEhyxq_1_JXC")
App.ActiveDocument.getObject("Sketch_FT3MJFDAUPEhyxq_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FT3MJFDAUPEhyxq_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FT3MJFDAUPEhyxq_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FT3MJFDAUPEhyxq_1_JXC").addGeometry(Part.Circle(App.Vector(-0.33328000000000,-0.70434000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),80.26149000000001),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FT3MJFDAUPEhyxq_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FT3MJFDAUPEhyxq_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F4KkMe6tiqeK68K_0").newObject("PartDesign::Pocket","Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC")
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FT3MJFDAUPEhyxq_1_JXC")
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FT3MJFDAUPEhyxq_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FT3MJFDAUPEhyxq_1_FlIPpGU4VLbNFKF_1_JXC").Offset = 0
App.ActiveDocument.recompute()

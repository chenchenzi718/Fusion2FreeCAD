import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00040108")
App.ActiveDocument.addObject("PartDesign::Body","Body_F2aErfRN5yshqNI_0")
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").Label = "Body_F2aErfRN5yshqNI_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_F2aErfRN5yshqNI_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2aErfRN5yshqNI_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_F2aErfRN5yshqNI_0_JGC")
App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2aErfRN5yshqNI_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,60.00000000000000,0.00000000000000),App.Vector(-40.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-40.00000000000000,50.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),10.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,50.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,-50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-40.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),10.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-40.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(40.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),10.00000000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").addGeometry(Part.LineSegment(App.Vector(50.00000000000000,50.00000000000000,0.00000000000000),App.Vector(50.00000000000000,-50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(40.00000000000000,50.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),10.00000000000000),0.0,1.5707963267949),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC")
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC")
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").Length = 10.0
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2aErfRN5yshqNI_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2aErfRN5yshqNI_0_FcdyxQT5sHlkTsx_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_FmlGtbBIkgz6oXJ_1_JMC")
origin = App.Vector(0.00000000000000,-10.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmlGtbBIkgz6oXJ_1_JMC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_FmlGtbBIkgz6oXJ_1_JMC")
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmlGtbBIkgz6oXJ_1_JMC"), [""])
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMC").addGeometry(Part.Circle(App.Vector(-40.00000000000000,50.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC")
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").Profile = App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMC")
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").Length = 100.0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").Type = 4
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_FmlGtbBIkgz6oXJ_1_JMG")
origin = App.Vector(0.00000000000000,-10.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmlGtbBIkgz6oXJ_1_JMG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_FmlGtbBIkgz6oXJ_1_JMG")
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmlGtbBIkgz6oXJ_1_JMG"), [""])
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMG").addGeometry(Part.Circle(App.Vector(40.00000000000000,50.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG")
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").Profile = App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMG")
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").Length = 100.0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").Type = 4
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_FmlGtbBIkgz6oXJ_1_JMK")
origin = App.Vector(0.00000000000000,-10.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmlGtbBIkgz6oXJ_1_JMK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_FmlGtbBIkgz6oXJ_1_JMK")
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmlGtbBIkgz6oXJ_1_JMK"), [""])
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMK").addGeometry(Part.Circle(App.Vector(40.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK")
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").Profile = App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMK")
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").Length = 100.0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").Type = 4
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_FmlGtbBIkgz6oXJ_1_JMO")
origin = App.Vector(0.00000000000000,-10.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmlGtbBIkgz6oXJ_1_JMO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_FmlGtbBIkgz6oXJ_1_JMO")
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmlGtbBIkgz6oXJ_1_JMO"), [""])
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMO").addGeometry(Part.Circle(App.Vector(-40.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),6.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO")
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").Profile = App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMO")
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").Length = 100.0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmlGtbBIkgz6oXJ_1_JMO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").Type = 4
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmlGtbBIkgz6oXJ_1_FcD3RdPWaqqnW8K_1_JMO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_F9LlK1bWOJ2GDrh_1_JQC")
origin = App.Vector(-0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_F9LlK1bWOJ2GDrh_1_JQC")
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQC"), [""])
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQC").addGeometry(Part.Circle(App.Vector(-37.82391000000001,32.70095000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").Profile = App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQC")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").Length = 100.0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").Type = 4
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_F9LlK1bWOJ2GDrh_1_JQG")
origin = App.Vector(-0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_F9LlK1bWOJ2GDrh_1_JQG")
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQG"), [""])
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQG").addGeometry(Part.Circle(App.Vector(-24.41462000000000,43.63401000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").Profile = App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQG")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").Length = 100.0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").Type = 4
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_F9LlK1bWOJ2GDrh_1_JQK")
origin = App.Vector(-0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_F9LlK1bWOJ2GDrh_1_JQK")
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQK"), [""])
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQK").addGeometry(Part.Circle(App.Vector(0.00000000000000,49.88715000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").Profile = App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQK")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").Length = 100.0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").Type = 4
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_F9LlK1bWOJ2GDrh_1_JQO")
origin = App.Vector(-0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_F9LlK1bWOJ2GDrh_1_JQO")
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQO"), [""])
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQO").addGeometry(Part.Circle(App.Vector(19.31819000000000,46.02326000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").Profile = App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQO")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").Length = 100.0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").Type = 4
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Plane", "plane_Sketch_F9LlK1bWOJ2GDrh_1_JQS")
origin = App.Vector(-0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("Sketcher::SketchObject","Sketch_F9LlK1bWOJ2GDrh_1_JQS")
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F9LlK1bWOJ2GDrh_1_JQS"), [""])
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQS").addGeometry(Part.Circle(App.Vector(37.04545000000000,33.74967000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),7.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F2aErfRN5yshqNI_0").newObject("PartDesign::Pad","Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").Profile = App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQS")
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").Length = 100.0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F9LlK1bWOJ2GDrh_1_JQS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").Type = 4
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F9LlK1bWOJ2GDrh_1_FuPS4xSlCwP4JhC_1_JQS").Offset = 0
App.ActiveDocument.recompute()

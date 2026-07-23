import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00366373")
App.ActiveDocument.addObject("PartDesign::Body","Body_FFMGxltJIhd5ZyH_0")
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").Label = "Body_FFMGxltJIhd5ZyH_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Plane", "plane_Sketch_FFMGxltJIhd5ZyH_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFMGxltJIhd5ZyH_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("Sketcher::SketchObject","Sketch_FFMGxltJIhd5ZyH_0_JGC")
App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFMGxltJIhd5ZyH_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,50.00000000000000,0.00000000000000),App.Vector(-50.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Pad","Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC")
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC")
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").Length = 50.0
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFMGxltJIhd5ZyH_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFMGxltJIhd5ZyH_0_FQe1wmYlUXLyahD_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Plane", "plane_Sketch_FPMWiOKTBlIWaBF_1_JJC")
origin = App.Vector(-25.00000000000000,25.00000000000000,50.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPMWiOKTBlIWaBF_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("Sketcher::SketchObject","Sketch_FPMWiOKTBlIWaBF_1_JJC")
App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPMWiOKTBlIWaBF_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.00000000000000,15.00000000000000,0.00000000000000),App.Vector(15.00000000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC").addGeometry(Part.LineSegment(App.Vector(15.00000000000000,15.00000000000000,0.00000000000000),App.Vector(15.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.00000000000000,-15.00000000000000,0.00000000000000),App.Vector(15.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC").addGeometry(Part.LineSegment(App.Vector(-15.00000000000000,15.00000000000000,0.00000000000000),App.Vector(-15.00000000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Pad","Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC")
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC")
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPMWiOKTBlIWaBF_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPMWiOKTBlIWaBF_1_FlYgxy3YPPATkqi_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Plane", "plane_Sketch_Fw768xBbwnjZQVi_1_JOC")
origin = App.Vector(-25.00000000000000,0.00000000000000,25.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fw768xBbwnjZQVi_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("Sketcher::SketchObject","Sketch_Fw768xBbwnjZQVi_1_JOC")
App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fw768xBbwnjZQVi_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Pad","Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC")
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC")
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").Length = 20.0
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fw768xBbwnjZQVi_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fw768xBbwnjZQVi_1_FfPK6nCUM9X8wSv_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Plane", "plane_Sketch_FmzsijHjkmQIkv8_1_JSC")
origin = App.Vector(-25.00000000000000,50.00000000000000,25.00000000000000)
x_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmzsijHjkmQIkv8_1_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("Sketcher::SketchObject","Sketch_FmzsijHjkmQIkv8_1_JSC")
App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmzsijHjkmQIkv8_1_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000),App.Vector(5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,5.00000000000000,0.00000000000000),App.Vector(-5.00000000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Pad","Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC")
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").Profile = App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC")
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmzsijHjkmQIkv8_1_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").Type = 4
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmzsijHjkmQIkv8_1_FJxUmey3v7A6sAY_1_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Plane", "plane_Sketch_FIv0ArSodMnDqMK_1_JWC")
origin = App.Vector(-25.00000000000000,25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIv0ArSodMnDqMK_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("Sketcher::SketchObject","Sketch_FIv0ArSodMnDqMK_1_JWC")
App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIv0ArSodMnDqMK_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC").addGeometry(Part.LineSegment(App.Vector(-3.96210000000000,15.00000000000000,0.00000000000000),App.Vector(6.03790000000000,15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC").addGeometry(Part.LineSegment(App.Vector(6.03790000000000,15.00000000000000,0.00000000000000),App.Vector(6.03790000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC").addGeometry(Part.LineSegment(App.Vector(-3.96210000000000,5.00000000000000,0.00000000000000),App.Vector(6.03790000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC").addGeometry(Part.LineSegment(App.Vector(-3.96210000000000,15.00000000000000,0.00000000000000),App.Vector(-3.96210000000000,5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Pad","Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC")
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC")
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").Length = 15.0
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Plane", "plane_Sketch_FIv0ArSodMnDqMK_1_JWG")
origin = App.Vector(-25.00000000000000,25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIv0ArSodMnDqMK_1_JWG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("Sketcher::SketchObject","Sketch_FIv0ArSodMnDqMK_1_JWG")
App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIv0ArSodMnDqMK_1_JWG"), [""])
App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG").addGeometry(Part.LineSegment(App.Vector(-3.59390000000000,-5.00000000000000,0.00000000000000),App.Vector(6.40610000000000,-5.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG").addGeometry(Part.LineSegment(App.Vector(6.40610000000000,-5.00000000000000,0.00000000000000),App.Vector(6.40610000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG").addGeometry(Part.LineSegment(App.Vector(-3.59390000000000,-15.00000000000000,0.00000000000000),App.Vector(6.40610000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG").addGeometry(Part.LineSegment(App.Vector(-3.59390000000000,-5.00000000000000,0.00000000000000),App.Vector(-3.59390000000000,-15.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Pad","Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG")
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").Profile = App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG")
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").Length = 15.0
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIv0ArSodMnDqMK_1_JWG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").Type = 4
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIv0ArSodMnDqMK_1_FRgcM1eSGOWWfhp_1_JWG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Plane", "plane_Sketch_FehxvmHFcwCa715_1_JaC")
origin = App.Vector(-10.00000000000000,25.00000000000000,62.50000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FehxvmHFcwCa715_1_JaC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("Sketcher::SketchObject","Sketch_FehxvmHFcwCa715_1_JaC")
App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FehxvmHFcwCa715_1_JaC"), [""])
App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,7.50000000000001,0.00000000000000),App.Vector(-5.00000000000000,7.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC").addGeometry(Part.LineSegment(App.Vector(-5.00000000000000,7.50000000000001,0.00000000000000),App.Vector(-5.00000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,2.50000000000000,0.00000000000000),App.Vector(-5.00000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,7.50000000000001,0.00000000000000),App.Vector(-10.00000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Pad","Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC")
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").Profile = App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC")
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").Type = 4
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Plane", "plane_Sketch_FehxvmHFcwCa715_1_JaG")
origin = App.Vector(-10.00000000000000,25.00000000000000,62.50000000000000)
x_axis=App.Vector(-0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FehxvmHFcwCa715_1_JaG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("Sketcher::SketchObject","Sketch_FehxvmHFcwCa715_1_JaG")
App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FehxvmHFcwCa715_1_JaG"), [""])
App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,7.50000000000001,0.00000000000000),App.Vector(10.00000000000000,7.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,7.50000000000001,0.00000000000000),App.Vector(10.00000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,2.50000000000000,0.00000000000000),App.Vector(10.00000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG").addGeometry(Part.LineSegment(App.Vector(5.00000000000000,7.50000000000001,0.00000000000000),App.Vector(5.00000000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FFMGxltJIhd5ZyH_0").newObject("PartDesign::Pad","Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG")
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").Profile = App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG")
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").Length = 3.0
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FehxvmHFcwCa715_1_JaG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").Type = 4
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FehxvmHFcwCa715_1_FkGl4n23LL6VBuX_1_JaG").Offset = 0
App.ActiveDocument.recompute()

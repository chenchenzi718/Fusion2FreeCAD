import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00249204")
App.ActiveDocument.addObject("PartDesign::Body","Body_FilzCzkkln7wxvf_0")
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").Label = "Body_FilzCzkkln7wxvf_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Plane", "plane_Sketch_FilzCzkkln7wxvf_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FilzCzkkln7wxvf_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("Sketcher::SketchObject","Sketch_FilzCzkkln7wxvf_0_JGC")
App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FilzCzkkln7wxvf_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(7.07107000000000,7.07107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").addGeometry(Part.LineSegment(App.Vector(7.07107000000000,7.07107000000000,0.00000000000000),App.Vector(27.07107000000000,7.07107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").addGeometry(Part.LineSegment(App.Vector(27.07107000000000,7.07107000000000,0.00000000000000),App.Vector(27.07107000000000,1.07107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").addGeometry(Part.LineSegment(App.Vector(27.07107000000000,1.07107000000000,0.00000000000000),App.Vector(9.55635000000000,1.07107000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").addGeometry(Part.LineSegment(App.Vector(9.55635000000000,1.07107000000000,0.00000000000000),App.Vector(6.00000000000000,-2.48528000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").addGeometry(Part.LineSegment(App.Vector(6.00000000000000,-2.48528000000000,0.00000000000000),App.Vector(6.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").addGeometry(Part.LineSegment(App.Vector(6.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Pad","Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC")
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC")
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FilzCzkkln7wxvf_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FilzCzkkln7wxvf_0_Fl06jpySdd8SdDm_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Plane", "plane_Sketch_FxNkTvQp8DMYF84_1_JJK")
origin = App.Vector(16.36396000000000,4.07107000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxNkTvQp8DMYF84_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("Sketcher::SketchObject","Sketch_FxNkTvQp8DMYF84_1_JJK")
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxNkTvQp8DMYF84_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK").addGeometry(Part.LineSegment(App.Vector(1.31371000000000,-14.67767000000000,0.00000000000000),App.Vector(-8.58579000000000,-4.77818000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK").addGeometry(Part.LineSegment(App.Vector(-6.80761000000000,-3.00000000000000,0.00000000000000),App.Vector(-8.58579000000000,-4.77818000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK").addGeometry(Part.LineSegment(App.Vector(-6.80761000000000,-3.00000000000000,0.00000000000000),App.Vector(-6.12132000000000,-3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK").addGeometry(Part.LineSegment(App.Vector(3.43503000000000,-12.55635000000000,0.00000000000000),App.Vector(-6.12132000000000,-3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK").addGeometry(Part.LineSegment(App.Vector(1.31371000000000,-14.67767000000000,0.00000000000000),App.Vector(3.43503000000000,-12.55635000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Pad","Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK")
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK")
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").Length2 = 20.0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Plane", "plane_Sketch_FxNkTvQp8DMYF84_1_JJO")
origin = App.Vector(16.36396000000000,4.07107000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxNkTvQp8DMYF84_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("Sketcher::SketchObject","Sketch_FxNkTvQp8DMYF84_1_JJO")
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxNkTvQp8DMYF84_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO").addGeometry(Part.LineSegment(App.Vector(1.31371000000000,-14.67767000000000,0.00000000000000),App.Vector(-8.58579000000000,-4.77818000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO").addGeometry(Part.LineSegment(App.Vector(-10.36396000000000,-6.55635000000000,0.00000000000000),App.Vector(-8.58579000000000,-4.77818000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO").addGeometry(Part.LineSegment(App.Vector(-10.36396000000000,-6.55635000000000,0.00000000000000),App.Vector(-10.36396000000000,-7.24264000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO").addGeometry(Part.LineSegment(App.Vector(-0.80761000000000,-16.79899000000000,0.00000000000000),App.Vector(-10.36396000000000,-7.24264000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO").addGeometry(Part.LineSegment(App.Vector(1.31371000000000,-14.67767000000000,0.00000000000000),App.Vector(-0.80761000000000,-16.79899000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Pad","Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO")
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO")
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").Length2 = 20.0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Plane", "plane_Sketch_FxNkTvQp8DMYF84_1_JJS")
origin = App.Vector(16.36396000000000,4.07107000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxNkTvQp8DMYF84_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("Sketcher::SketchObject","Sketch_FxNkTvQp8DMYF84_1_JJS")
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxNkTvQp8DMYF84_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS").addGeometry(Part.LineSegment(App.Vector(-12.82843000000000,-0.53554000000000,0.00000000000000),App.Vector(-8.58579000000000,-4.77818000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS").addGeometry(Part.LineSegment(App.Vector(-6.80761000000000,-3.00000000000000,0.00000000000000),App.Vector(-8.58579000000000,-4.77818000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS").addGeometry(Part.LineSegment(App.Vector(-6.80761000000000,-3.00000000000000,0.00000000000000),App.Vector(-6.12132000000000,-3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS").addGeometry(Part.LineSegment(App.Vector(-10.70711000000000,1.58578000000000,0.00000000000000),App.Vector(-6.12132000000000,-3.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS").addGeometry(Part.LineSegment(App.Vector(-12.82843000000000,-0.53554000000000,0.00000000000000),App.Vector(-10.70711000000000,1.58578000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Pad","Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS")
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS")
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").Length = 25.0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").Length2 = 20.0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Plane", "plane_Sketch_FxNkTvQp8DMYF84_1_JJW")
origin = App.Vector(16.36396000000000,4.07107000000000,20.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxNkTvQp8DMYF84_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("Sketcher::SketchObject","Sketch_FxNkTvQp8DMYF84_1_JJW")
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxNkTvQp8DMYF84_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW").addGeometry(Part.LineSegment(App.Vector(-12.82843000000000,-0.53554000000000,0.00000000000000),App.Vector(-8.58579000000000,-4.77818000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW").addGeometry(Part.LineSegment(App.Vector(-10.36396000000000,-6.55635000000000,0.00000000000000),App.Vector(-8.58579000000000,-4.77818000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW").addGeometry(Part.LineSegment(App.Vector(-10.36396000000000,-6.55635000000000,0.00000000000000),App.Vector(-10.36396000000000,-7.24264000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW").addGeometry(Part.LineSegment(App.Vector(-14.94975000000000,-2.65686000000000,0.00000000000000),App.Vector(-10.36396000000000,-7.24264000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW").addGeometry(Part.LineSegment(App.Vector(-12.82843000000000,-0.53554000000000,0.00000000000000),App.Vector(-14.94975000000000,-2.65686000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Pad","Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW")
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW")
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").Length = 25.0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").Length2 = 20.0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").TaperAngle2 = 0.000000
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxNkTvQp8DMYF84_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxNkTvQp8DMYF84_1_FoeElEzBavxHAnV_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Plane", "plane_Sketch_Fnn2ILLdDD8SvNP_1_JNC")
origin = App.Vector(0.00000000000000,-10.00000000000000,10.00000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fnn2ILLdDD8SvNP_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("Sketcher::SketchObject","Sketch_Fnn2ILLdDD8SvNP_1_JNC")
App.ActiveDocument.getObject("Sketch_Fnn2ILLdDD8SvNP_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fnn2ILLdDD8SvNP_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fnn2ILLdDD8SvNP_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fnn2ILLdDD8SvNP_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fnn2ILLdDD8SvNP_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fnn2ILLdDD8SvNP_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Pocket","Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC")
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fnn2ILLdDD8SvNP_1_JNC")
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fnn2ILLdDD8SvNP_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fnn2ILLdDD8SvNP_1_FytmAj1ldXfIerU_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Plane", "plane_Sketch_Fgfsjndpf4O7Ukz_1_JRC")
origin = App.Vector(17.07107000000000,7.07107000000000,10.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fgfsjndpf4O7Ukz_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("Sketcher::SketchObject","Sketch_Fgfsjndpf4O7Ukz_1_JRC")
App.ActiveDocument.getObject("Sketch_Fgfsjndpf4O7Ukz_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fgfsjndpf4O7Ukz_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fgfsjndpf4O7Ukz_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fgfsjndpf4O7Ukz_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fgfsjndpf4O7Ukz_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fgfsjndpf4O7Ukz_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Pocket","Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC")
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fgfsjndpf4O7Ukz_1_JRC")
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fgfsjndpf4O7Ukz_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fgfsjndpf4O7Ukz_1_FCM0yLtgDXv2qXS_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Plane", "plane_Sketch_FHQL5YdGa9L0c8u_1_JVC")
origin = App.Vector(8.48528000000000,-5.65685000000000,22.50000000000000)
x_axis=App.Vector(0.70710678000000,-0.70710678000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,0.99999999664394)
z_axis=App.Vector(-0.70710678000000,-0.70710678000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHQL5YdGa9L0c8u_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("Sketcher::SketchObject","Sketch_FHQL5YdGa9L0c8u_1_JVC")
App.ActiveDocument.getObject("Sketch_FHQL5YdGa9L0c8u_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHQL5YdGa9L0c8u_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FHQL5YdGa9L0c8u_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHQL5YdGa9L0c8u_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,12.49999995804922,0.00000000000000),App.Vector(-0.00000000000000,0.00000000000000,0.99999999664394),4.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHQL5YdGa9L0c8u_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHQL5YdGa9L0c8u_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FilzCzkkln7wxvf_0").newObject("PartDesign::Pocket","Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC")
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FHQL5YdGa9L0c8u_1_JVC")
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHQL5YdGa9L0c8u_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHQL5YdGa9L0c8u_1_FqBmhYR7la9AjUv_1_JVC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00655177")
App.ActiveDocument.addObject("PartDesign::Body","Body_FoKZeATmtdNdotw_0")
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").Label = "Body_FoKZeATmtdNdotw_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_FoKZeATmtdNdotw_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoKZeATmtdNdotw_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_FoKZeATmtdNdotw_0_JGC")
App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoKZeATmtdNdotw_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").addGeometry(Part.LineSegment(App.Vector(-57.82847000000000,37.55280000000000,0.00000000000000),App.Vector(-57.82847000000000,-13.56470000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").addGeometry(Part.LineSegment(App.Vector(-57.82847000000000,-13.56470000000000,0.00000000000000),App.Vector(0.00000000000000,-13.56470000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-13.56470000000000,0.00000000000000),App.Vector(0.00000000000000,-23.84532000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-23.84532000000000,0.00000000000000),App.Vector(61.82649000000000,-23.84532000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").addGeometry(Part.LineSegment(App.Vector(61.82649000000000,-23.84532000000000,0.00000000000000),App.Vector(0.00000000000000,37.55280000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").addGeometry(Part.LineSegment(App.Vector(-57.82847000000000,37.55280000000000,0.00000000000000),App.Vector(0.00000000000000,37.55280000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pad","Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC")
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC")
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").Length = 79.50200000000001
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoKZeATmtdNdotw_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoKZeATmtdNdotw_0_F9jahPYcbUkMsRx_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_Fdm0oe1ZJ3XnCRm_1_JJC")
origin = App.Vector(-28.91423000000000,-11.19296000000000,37.55280000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fdm0oe1ZJ3XnCRm_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_Fdm0oe1ZJ3XnCRm_1_JJC")
App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fdm0oe1ZJ3XnCRm_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC").addGeometry(Part.LineSegment(App.Vector(-59.80412000000000,-5.37420000000000,0.00000000000000),App.Vector(-28.91424000000000,-5.37420000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC").addGeometry(Part.LineSegment(App.Vector(-28.91424000000000,-5.37420000000000,0.00000000000000),App.Vector(-28.91424000000000,-42.91462000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC").addGeometry(Part.LineSegment(App.Vector(-59.80412000000000,-42.91462000000000,0.00000000000000),App.Vector(-28.91424000000000,-42.91462000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC").addGeometry(Part.LineSegment(App.Vector(-59.80412000000000,-5.37420000000000,0.00000000000000),App.Vector(-59.80412000000000,-42.91462000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pocket","Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC")
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC")
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fdm0oe1ZJ3XnCRm_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fdm0oe1ZJ3XnCRm_1_FeWgNgmWstApQ2R_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_F7EQSwrRkqDMnrD_1_JPC")
origin = App.Vector(-28.91423000000000,-11.19296000000000,37.55280000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7EQSwrRkqDMnrD_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_F7EQSwrRkqDMnrD_1_JPC")
App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7EQSwrRkqDMnrD_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC").addGeometry(Part.LineSegment(App.Vector(-28.91424000000000,-38.23517000000000,0.00000000000000),App.Vector(28.91423000000000,-38.23517000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC").addGeometry(Part.LineSegment(App.Vector(28.91423000000000,-38.23517000000000,0.00000000000000),App.Vector(28.91423000000000,-14.07751000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC").addGeometry(Part.LineSegment(App.Vector(-28.91424000000000,-14.07751000000000,0.00000000000000),App.Vector(28.91423000000000,-14.07751000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC").addGeometry(Part.LineSegment(App.Vector(-28.91424000000000,-38.23517000000000,0.00000000000000),App.Vector(-28.91424000000000,-14.07751000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pad","Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC")
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC")
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").Length = 12.446
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7EQSwrRkqDMnrD_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").Type = 0
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7EQSwrRkqDMnrD_1_FlRmiZCF9IGNe8t_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_Fpq0PVALNDstM1O_1_JVC")
origin = App.Vector(-28.91423000000000,-11.19296000000000,37.55280000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fpq0PVALNDstM1O_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_Fpq0PVALNDstM1O_1_JVC")
App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fpq0PVALNDstM1O_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC").addGeometry(Part.LineSegment(App.Vector(43.47788000000000,-34.68983000000000,0.00000000000000),App.Vector(28.91423000000000,-34.68983000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC").addGeometry(Part.LineSegment(App.Vector(28.91423000000000,-34.68983000000000,0.00000000000000),App.Vector(28.91423000000000,-11.19295000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC").addGeometry(Part.LineSegment(App.Vector(43.47788000000000,-11.19295000000000,0.00000000000000),App.Vector(28.91423000000000,-11.19295000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC").addGeometry(Part.LineSegment(App.Vector(43.47788000000000,-34.68983000000000,0.00000000000000),App.Vector(43.47788000000000,-11.19295000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pocket","Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC")
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC")
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").Length = 21.082
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_Fpq0PVALNDstM1O_1_JVG")
origin = App.Vector(-28.91423000000000,-11.19296000000000,37.55280000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fpq0PVALNDstM1O_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_Fpq0PVALNDstM1O_1_JVG")
App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fpq0PVALNDstM1O_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG").addGeometry(Part.LineSegment(App.Vector(-28.91424000000000,-34.68983000000000,0.00000000000000),App.Vector(28.91423000000000,-34.68983000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG").addGeometry(Part.LineSegment(App.Vector(28.91423000000000,-34.68983000000000,0.00000000000000),App.Vector(28.91423000000000,-11.19295000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG").addGeometry(Part.LineSegment(App.Vector(-28.91424000000000,-11.19295000000000,0.00000000000000),App.Vector(28.91423000000000,-11.19295000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG").addGeometry(Part.LineSegment(App.Vector(-28.91424000000000,-34.68983000000000,0.00000000000000),App.Vector(-28.91424000000000,-11.19295000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pocket","Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG")
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG")
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").Length = 21.082
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fpq0PVALNDstM1O_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fpq0PVALNDstM1O_1_Ffjas42V0DGHFUF_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_Fpwv3w4wWOrJjCT_1_JZC")
origin = App.Vector(30.91324000000000,-39.75100000000000,-23.84532000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fpwv3w4wWOrJjCT_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_Fpwv3w4wWOrJjCT_1_JZC")
App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fpwv3w4wWOrJjCT_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC").addGeometry(Part.LineSegment(App.Vector(30.91325000000000,39.75100000000000,0.00000000000000),App.Vector(-19.58338000000000,39.75100000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC").addGeometry(Part.LineSegment(App.Vector(-19.58338000000000,39.75100000000000,0.00000000000000),App.Vector(-19.58338000000000,22.01381000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC").addGeometry(Part.LineSegment(App.Vector(-19.58338000000000,22.01381000000000,0.00000000000000),App.Vector(30.91325000000000,22.01381000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC").addGeometry(Part.LineSegment(App.Vector(30.91325000000000,39.75100000000000,0.00000000000000),App.Vector(30.91325000000000,22.01381000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pocket","Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC")
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC")
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").Length = 56.388
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fpwv3w4wWOrJjCT_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fpwv3w4wWOrJjCT_1_F9QlJjiRXxp8QNl_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_F7PVV2B8c7yykk4_1_JdC")
origin = App.Vector(30.91324000000000,-39.75100000000000,6.85374000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.70956058000000,0.00000000000000,0.70464444000000)
z_axis=App.Vector(0.70464444000000,0.00000000000000,0.70956058000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7PVV2B8c7yykk4_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_F7PVV2B8c7yykk4_1_JdC")
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7PVV2B8c7yykk4_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdC").addGeometry(Part.Circle(App.Vector(-9.09948000000000,5.62112982254340,0.00000301304880),App.Vector(0.00000000000000,-0.00000000000000,1.00000000351285),8.23103000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pocket","Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC")
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdC")
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").Length = 85.34400000000001
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_F7PVV2B8c7yykk4_1_JdG")
origin = App.Vector(30.91324000000000,-39.75100000000000,6.85374000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.70956058000000,0.00000000000000,0.70464444000000)
z_axis=App.Vector(0.70464444000000,0.00000000000000,0.70956058000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7PVV2B8c7yykk4_1_JdG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_F7PVV2B8c7yykk4_1_JdG")
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7PVV2B8c7yykk4_1_JdG"), [""])
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdG").addGeometry(Part.Circle(App.Vector(-10.38258000000000,-28.97612410988400,0.00000658866200),App.Vector(0.00000000000000,-0.00000000000000,1.00000000351285),9.36647000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pocket","Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG")
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").Profile = App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdG")
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").Length = 85.34400000000001
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").Type = 4
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_F7PVV2B8c7yykk4_1_JdK")
origin = App.Vector(30.91324000000000,-39.75100000000000,6.85374000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.70956058000000,0.00000000000000,0.70464444000000)
z_axis=App.Vector(0.70464444000000,0.00000000000000,0.70956058000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7PVV2B8c7yykk4_1_JdK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_F7PVV2B8c7yykk4_1_JdK")
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7PVV2B8c7yykk4_1_JdK"), [""])
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdK").addGeometry(Part.Circle(App.Vector(24.99412000000000,6.92177576903520,-0.00000111821860),App.Vector(0.00000000000000,-0.00000000000000,1.00000000351285),8.11831000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pocket","Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK")
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").Profile = App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdK")
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").Length = 85.34400000000001
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").Type = 4
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Plane", "plane_Sketch_F7PVV2B8c7yykk4_1_JdO")
origin = App.Vector(30.91324000000000,-39.75100000000000,6.85374000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.70956058000000,0.00000000000000,0.70464444000000)
z_axis=App.Vector(0.70464444000000,0.00000000000000,0.70956058000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7PVV2B8c7yykk4_1_JdO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("Sketcher::SketchObject","Sketch_F7PVV2B8c7yykk4_1_JdO")
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7PVV2B8c7yykk4_1_JdO"), [""])
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdO").addGeometry(Part.Circle(App.Vector(25.72732000000000,-27.15521412797540,0.00000082455220),App.Vector(0.00000000000000,-0.00000000000000,1.00000000351285),9.33569000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FoKZeATmtdNdotw_0").newObject("PartDesign::Pocket","Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO")
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").Profile = App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdO")
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").Length = 85.34400000000001
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7PVV2B8c7yykk4_1_JdO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").Type = 4
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7PVV2B8c7yykk4_1_FoE7h6gVUEKThFY_1_JdO").Offset = 0
App.ActiveDocument.recompute()

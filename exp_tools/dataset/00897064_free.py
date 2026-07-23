import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00897064")
App.ActiveDocument.addObject("PartDesign::Body","Body_FLvlrA2eMLDHP05_0")
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").Label = "Body_FLvlrA2eMLDHP05_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Plane", "plane_Sketch_FLvlrA2eMLDHP05_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLvlrA2eMLDHP05_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("Sketcher::SketchObject","Sketch_FLvlrA2eMLDHP05_0_JGS")
App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLvlrA2eMLDHP05_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(122.04700000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").addGeometry(Part.LineSegment(App.Vector(122.04700000000000,0.00000000000000,0.00000000000000),App.Vector(122.04700000000000,25.14600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,25.14600000000000,0.00000000000000),App.Vector(122.04700000000000,25.14600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,25.14600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").addGeometry(Part.Circle(App.Vector(6.85800000000000,21.03120000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.77800000000000),False)

App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").addGeometry(Part.LineSegment(App.Vector(113.15700000000000,22.80920000000000,0.00000000000000),App.Vector(117.09400000000001,22.80920000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(117.09400000000001,21.03120000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),1.77800000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").addGeometry(Part.LineSegment(App.Vector(113.15700000000000,19.25320000000000,0.00000000000000),App.Vector(117.09400000000001,19.25320000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(113.15700000000000,21.03120000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.77800000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Pad","Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS")
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").Profile = App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS")
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").Length = 1.6002000000000003
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLvlrA2eMLDHP05_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLvlrA2eMLDHP05_0_FFPK29o8l83CKM4_0_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Plane", "plane_Sketch_FrRdpag7XeUzs6o_1_JJC")
origin = App.Vector(61.02350000000000,-1.60020000000000,12.57300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrRdpag7XeUzs6o_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("Sketcher::SketchObject","Sketch_FrRdpag7XeUzs6o_1_JJC")
App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrRdpag7XeUzs6o_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC").addGeometry(Part.LineSegment(App.Vector(-48.32350000000000,2.03200000000000,0.00000000000000),App.Vector(-38.16350000000001,2.03200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC").addGeometry(Part.LineSegment(App.Vector(-38.16350000000001,2.03200000000000,0.00000000000000),App.Vector(-38.16350000000001,-6.85800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC").addGeometry(Part.LineSegment(App.Vector(-48.32350000000000,-6.85800000000000,0.00000000000000),App.Vector(-38.16350000000001,-6.85800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC").addGeometry(Part.LineSegment(App.Vector(-48.32350000000000,2.03200000000000,0.00000000000000),App.Vector(-48.32350000000000,-6.85800000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Pad","Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC")
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC")
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Plane", "plane_Sketch_FrRdpag7XeUzs6o_1_JJO")
origin = App.Vector(61.02350000000000,-1.60020000000000,12.57300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrRdpag7XeUzs6o_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("Sketcher::SketchObject","Sketch_FrRdpag7XeUzs6o_1_JJO")
App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrRdpag7XeUzs6o_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO").addGeometry(Part.LineSegment(App.Vector(6.41350000000000,13.84300000000000,0.00000000000000),App.Vector(20.38349999999999,13.84300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO").addGeometry(Part.LineSegment(App.Vector(20.38349999999999,13.84300000000000,0.00000000000000),App.Vector(20.38349999999999,12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO").addGeometry(Part.LineSegment(App.Vector(6.41350000000000,12.57300000000000,0.00000000000000),App.Vector(20.38349999999999,12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO").addGeometry(Part.LineSegment(App.Vector(6.41350000000000,13.84300000000000,0.00000000000000),App.Vector(6.41350000000000,12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Pad","Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO")
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO")
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Plane", "plane_Sketch_FrRdpag7XeUzs6o_1_JJS")
origin = App.Vector(61.02350000000000,-1.60020000000000,12.57300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrRdpag7XeUzs6o_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("Sketcher::SketchObject","Sketch_FrRdpag7XeUzs6o_1_JJS")
App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrRdpag7XeUzs6o_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS").addGeometry(Part.LineSegment(App.Vector(6.41350000000000,7.49300000000000,0.00000000000000),App.Vector(20.38349999999999,7.49300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS").addGeometry(Part.LineSegment(App.Vector(20.38349999999999,7.49300000000000,0.00000000000000),App.Vector(20.38349999999999,12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS").addGeometry(Part.LineSegment(App.Vector(6.41350000000000,12.57300000000000,0.00000000000000),App.Vector(20.38349999999999,12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS").addGeometry(Part.LineSegment(App.Vector(6.41350000000000,7.49300000000000,0.00000000000000),App.Vector(6.41350000000000,12.57300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Pad","Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS")
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS")
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrRdpag7XeUzs6o_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrRdpag7XeUzs6o_1_FfaltSckhRoCMTx_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Plane", "plane_Sketch_FitHnv4OxMajQ6i_1_JNC")
origin = App.Vector(61.02350000000000,-1.60020000000000,12.57300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("Sketcher::SketchObject","Sketch_FitHnv4OxMajQ6i_1_JNC")
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC").addGeometry(Part.LineSegment(App.Vector(-17.71650000000000,6.47700000000000,0.00000000000000),App.Vector(-8.82650000000000,6.47700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC").addGeometry(Part.LineSegment(App.Vector(-8.82650000000000,6.47700000000000,0.00000000000000),App.Vector(-8.82650000000000,-2.41300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC").addGeometry(Part.LineSegment(App.Vector(-17.71650000000000,-2.41300000000000,0.00000000000000),App.Vector(-8.82650000000000,-2.41300000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC").addGeometry(Part.LineSegment(App.Vector(-17.71650000000000,6.47700000000000,0.00000000000000),App.Vector(-17.71650000000000,-2.41300000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Pad","Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").Length = 8.255000000000003
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Plane", "plane_Sketch_FitHnv4OxMajQ6i_1_JNG")
origin = App.Vector(61.02350000000000,-1.60020000000000,12.57300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("Sketcher::SketchObject","Sketch_FitHnv4OxMajQ6i_1_JNG")
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNG").addGeometry(Part.Circle(App.Vector(21.65350000000000,-7.49300000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.85750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Pad","Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNG")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").Length = 8.255000000000003
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Plane", "plane_Sketch_FitHnv4OxMajQ6i_1_JNW")
origin = App.Vector(61.02350000000000,-1.60020000000000,12.57300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("Sketcher::SketchObject","Sketch_FitHnv4OxMajQ6i_1_JNW")
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNW").addGeometry(Part.LineSegment(App.Vector(-30.22600000000000,5.58800000000000,0.00000000000000),App.Vector(-30.22600000000000,-0.12700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNW").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-30.22600000000000,2.73050000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.85750000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Pad","Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNW")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").Length = 8.255000000000003
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Plane", "plane_Sketch_FitHnv4OxMajQ6i_1_JNa")
origin = App.Vector(61.02350000000000,-1.60020000000000,12.57300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("Sketcher::SketchObject","Sketch_FitHnv4OxMajQ6i_1_JNa")
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNa").addGeometry(Part.LineSegment(App.Vector(-24.51100000000000,5.58800000000000,0.00000000000000),App.Vector(-24.51100000000000,-0.12700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNa").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-24.51100000000000,2.73050000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000),2.85750000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Pad","Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNa")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").Length = 8.255000000000003
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").Type = 4
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Plane", "plane_Sketch_FitHnv4OxMajQ6i_1_JNe")
origin = App.Vector(61.02350000000000,-1.60020000000000,12.57300000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("Sketcher::SketchObject","Sketch_FitHnv4OxMajQ6i_1_JNe")
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FitHnv4OxMajQ6i_1_JNe"), [""])
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe").addGeometry(Part.LineSegment(App.Vector(-30.22600000000000,5.58800000000000,0.00000000000000),App.Vector(-24.51100000000000,5.58800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe").addGeometry(Part.LineSegment(App.Vector(-24.51100000000000,5.58800000000000,0.00000000000000),App.Vector(-24.51100000000000,-0.12700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe").addGeometry(Part.LineSegment(App.Vector(-30.22600000000000,-0.12700000000000,0.00000000000000),App.Vector(-24.51100000000000,-0.12700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe").addGeometry(Part.LineSegment(App.Vector(-30.22600000000000,5.58800000000000,0.00000000000000),App.Vector(-30.22600000000000,-0.12700000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLvlrA2eMLDHP05_0").newObject("PartDesign::Pad","Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").Profile = App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe")
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").Length = 8.255000000000003
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FitHnv4OxMajQ6i_1_JNe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").Type = 4
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FitHnv4OxMajQ6i_1_FR8toJ9moIUS8Xu_1_JNe").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00299613")
App.ActiveDocument.addObject("PartDesign::Body","Body_FuuI9zagBH1ot2j_0")
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").Label = "Body_FuuI9zagBH1ot2j_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_FuuI9zagBH1ot2j_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuuI9zagBH1ot2j_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_FuuI9zagBH1ot2j_0_JGC")
App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuuI9zagBH1ot2j_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC").addGeometry(Part.LineSegment(App.Vector(130.00000000000000,10.00000000000000,0.00000000000000),App.Vector(130.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC").addGeometry(Part.LineSegment(App.Vector(130.00000000000000,0.00000000000000,0.00000000000000),App.Vector(95.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC").addGeometry(Part.LineSegment(App.Vector(95.00000000000000,10.00000000000000,0.00000000000000),App.Vector(95.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC").addGeometry(Part.LineSegment(App.Vector(130.00000000000000,10.00000000000000,0.00000000000000),App.Vector(95.00000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pad","Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC")
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC")
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_FuuI9zagBH1ot2j_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuuI9zagBH1ot2j_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_FuuI9zagBH1ot2j_0_JGK")
App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuuI9zagBH1ot2j_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(30.00000000000000,51.96152000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(30.00000000000000,51.96152000000000,0.00000000000000),App.Vector(31.29904000000000,51.21152000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(31.29904000000000,51.21152000000000,0.00000000000000),App.Vector(27.04904000000000,43.85031000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(28.34808000000000,43.10031000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),2.61799450943192,4.18879083622681),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(27.59808000000000,41.80127000000000,0.00000000000000),App.Vector(44.91858000000000,31.80127000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(45.66858000000000,33.10031000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),4.18879083622681,0.20612935047809),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(47.13683000000000,33.40732000000000,0.00000000000000),App.Vector(64.45734000000000,23.40732000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(64.92558000000000,21.98227000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),1.88826094317728,4.18878750288153),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(64.17558000000000,20.68324000000000,0.00000000000000),App.Vector(78.03847999999999,12.67949000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(88.03848000000001,30.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),20.00000000000000),4.18879025289417,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(88.03848000000001,10.00000000000000,0.00000000000000),App.Vector(95.00000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(95.00000000000000,10.00000000000000,0.00000000000000),App.Vector(95.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(95.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(23.04904000000000,36.92211000000000,0.00000000000000),App.Vector(11.29904000000000,16.57051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(15.62917000000000,14.07051000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),2.61799417609912,4.18879050289402),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(13.12917000000000,9.74038000000000,0.00000000000000),App.Vector(27.40192000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(27.40192000000000,1.50000000000000,0.00000000000000),App.Vector(79.40192000000000,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(76.90192000000000,5.83013000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),5.23598745787536,1.04719684930352),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.LineSegment(App.Vector(29.87917000000000,38.75223000000000,0.00000000000000),App.Vector(79.40192000000000,10.16025000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(27.37917000000000,34.42211000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),1.04719684930353,2.61799417609912),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pad","Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK")
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK")
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").Length = 20.0
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuuI9zagBH1ot2j_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").Type = 0
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").Midplane = 1
App.ActiveDocument.getObject("Extrude_FuuI9zagBH1ot2j_0_FPm23ovwZHLcoiP_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_F8KPOYT85OniSNb_1_JJC")
origin = App.Vector(55.79708000000000,0.00000000000000,28.40732000000000)
x_axis=App.Vector(0.86602540000000,0.00000000000000,-0.50000000000000)
y_axis=App.Vector(-0.00000000000000,0.99999999344516,0.00000000000000)
z_axis=App.Vector(0.50000000000000,0.00000000000000,0.86602540000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8KPOYT85OniSNb_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_F8KPOYT85OniSNb_1_JJC")
App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8KPOYT85OniSNb_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(-4.61802636298200,0.00000000000000,-0.00000369114600),App.Vector(0.00000000000000,0.00000000000000,-0.99999999344516),4.00000000000000),4.71238898038469,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC").addGeometry(Part.LineSegment(App.Vector(-4.61802636298200,3.99999997378064,-0.00000369114600),App.Vector(2.38197549639000,3.99999997378064,-0.00000259114600)),False)

App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(2.38197549639000,0.00000000000000,-0.00000259114600),App.Vector(0.00000000000000,0.00000000000000,-0.99999999344516),4.00000000000000),1.5707963267949,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC").addGeometry(Part.LineSegment(App.Vector(-4.61802636298200,-3.99999997378064,-0.00000369114600),App.Vector(2.38197549639000,-3.99999997378064,-0.00000259114600)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pocket","Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC")
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC")
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").Length = 4.0
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8KPOYT85OniSNb_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8KPOYT85OniSNb_1_FTUnfKJwHB6uL84_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_F0jRJO4ZKCUZlOM_1_JNa")
origin = App.Vector(15.00000000000000,0.00000000000000,25.98076000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.50000000000000,0.00000000000000,0.86602540000000)
z_axis=App.Vector(-0.86602540000000,0.00000000000000,0.50000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_F0jRJO4ZKCUZlOM_1_JNa")
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNa").addGeometry(Part.Circle(App.Vector(-5.00000000000000,9.00000115344200,0.00000070000000),App.Vector(0.00000000000000,0.00000000000000,0.99999999344516),1.39500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pocket","Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNa")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").Length = 1.5
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").Type = 4
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_F0jRJO4ZKCUZlOM_1_JNO")
origin = App.Vector(15.00000000000000,0.00000000000000,25.98076000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.50000000000000,0.00000000000000,0.86602540000000)
z_axis=App.Vector(-0.86602540000000,0.00000000000000,0.50000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_F0jRJO4ZKCUZlOM_1_JNO")
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNO").addGeometry(Part.Circle(App.Vector(-5.00000000000000,1.99999929407000,-0.00000040000000),App.Vector(0.00000000000000,0.00000000000000,0.99999999344516),1.39500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pocket","Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNO")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").Length = 1.5
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_F0jRJO4ZKCUZlOM_1_JNK")
origin = App.Vector(15.00000000000000,0.00000000000000,25.98076000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.50000000000000,0.00000000000000,0.86602540000000)
z_axis=App.Vector(-0.86602540000000,0.00000000000000,0.50000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_F0jRJO4ZKCUZlOM_1_JNK")
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNK").addGeometry(Part.Circle(App.Vector(5.00000000000000,-4.99999390504800,0.00000350000000),App.Vector(0.00000000000000,0.00000000000000,0.99999999344516),1.39500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pocket","Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNK")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").Length = 1.5
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_F0jRJO4ZKCUZlOM_1_JNS")
origin = App.Vector(15.00000000000000,0.00000000000000,25.98076000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.50000000000000,0.00000000000000,0.86602540000000)
z_axis=App.Vector(-0.86602540000000,0.00000000000000,0.50000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_F0jRJO4ZKCUZlOM_1_JNS")
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNS").addGeometry(Part.Circle(App.Vector(5.00000000000000,1.99999929407000,-0.00000040000000),App.Vector(0.00000000000000,0.00000000000000,0.99999999344516),1.39500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pocket","Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNS")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").Length = 1.5
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_F0jRJO4ZKCUZlOM_1_JNW")
origin = App.Vector(15.00000000000000,0.00000000000000,25.98076000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.50000000000000,0.00000000000000,0.86602540000000)
z_axis=App.Vector(-0.86602540000000,0.00000000000000,0.50000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_F0jRJO4ZKCUZlOM_1_JNW")
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNW").addGeometry(Part.Circle(App.Vector(5.00000000000000,9.00000115344200,0.00000070000000),App.Vector(0.00000000000000,0.00000000000000,0.99999999344516),1.39500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pocket","Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNW")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").Length = 1.5
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_F0jRJO4ZKCUZlOM_1_JNG")
origin = App.Vector(15.00000000000000,0.00000000000000,25.98076000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.50000000000000,0.00000000000000,0.86602540000000)
z_axis=App.Vector(-0.86602540000000,0.00000000000000,0.50000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_F0jRJO4ZKCUZlOM_1_JNG")
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNG").addGeometry(Part.Circle(App.Vector(-5.00000000000000,-4.99999390504800,0.00000350000000),App.Vector(0.00000000000000,0.00000000000000,0.99999999344516),1.39500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pocket","Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNG")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").Length = 1.5
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FL96SF08HykT3I8_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Plane", "plane_Sketch_F0jRJO4ZKCUZlOM_1_JNe")
origin = App.Vector(15.00000000000000,0.00000000000000,25.98076000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.50000000000000,0.00000000000000,0.86602540000000)
z_axis=App.Vector(-0.86602540000000,0.00000000000000,0.50000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("Sketcher::SketchObject","Sketch_F0jRJO4ZKCUZlOM_1_JNe")
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0jRJO4ZKCUZlOM_1_JNe"), [""])
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNe").addGeometry(Part.Circle(App.Vector(0.00000000000000,-22.49999855347800,0.00000075000000),App.Vector(0.00000000000000,0.00000000000000,0.99999999344516),5.50000000000000),False)

App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNe").addGeometry(Part.Circle(App.Vector(0.00000000000000,-22.49999855347800,0.00000075000000),App.Vector(0.00000000000000,0.00000000000000,0.99999999344516),4.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuuI9zagBH1ot2j_0").newObject("PartDesign::Pocket","Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").Profile = App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNe")
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").Length = 2.0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0jRJO4ZKCUZlOM_1_JNe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").Type = 4
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0jRJO4ZKCUZlOM_1_FvOJrM74sTo0Qts_1_JNe").Offset = 0
App.ActiveDocument.recompute()

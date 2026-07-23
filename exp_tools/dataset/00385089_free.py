import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00385089")
App.ActiveDocument.addObject("PartDesign::Body","Body_FJVvd22GAsoJox7_0")
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").Label = "Body_FJVvd22GAsoJox7_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Plane", "plane_Sketch_FJVvd22GAsoJox7_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJVvd22GAsoJox7_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("Sketcher::SketchObject","Sketch_FJVvd22GAsoJox7_0_JGC")
App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJVvd22GAsoJox7_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC").addGeometry(Part.LineSegment(App.Vector(31.75000000000000,31.75000000000000,0.00000000000000),App.Vector(-31.75000000000000,31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC").addGeometry(Part.LineSegment(App.Vector(-31.75000000000000,31.75000000000000,0.00000000000000),App.Vector(-31.75000000000000,-31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC").addGeometry(Part.LineSegment(App.Vector(31.75000000000000,-31.75000000000000,0.00000000000000),App.Vector(-31.75000000000000,-31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC").addGeometry(Part.LineSegment(App.Vector(31.75000000000000,31.75000000000000,0.00000000000000),App.Vector(31.75000000000000,-31.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Pad","Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC")
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC")
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJVvd22GAsoJox7_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJVvd22GAsoJox7_0_FFD5tH3nKd3k88F_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Plane", "plane_Sketch_FDLtKrNoWVsbn97_1_JJC")
origin = App.Vector(0.00000000000000,-0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDLtKrNoWVsbn97_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("Sketcher::SketchObject","Sketch_FDLtKrNoWVsbn97_1_JJC")
App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDLtKrNoWVsbn97_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC").addGeometry(Part.LineSegment(App.Vector(27.43200000000000,26.06040000000000,0.00000000000000),App.Vector(-27.43200000000000,26.06040000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC").addGeometry(Part.LineSegment(App.Vector(-27.43200000000000,26.06040000000000,0.00000000000000),App.Vector(-27.43200000000000,-26.06040000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC").addGeometry(Part.LineSegment(App.Vector(27.43200000000000,-26.06040000000000,0.00000000000000),App.Vector(-27.43200000000000,-26.06040000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC").addGeometry(Part.LineSegment(App.Vector(27.43200000000000,26.06040000000000,0.00000000000000),App.Vector(27.43200000000000,-26.06040000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Pad","Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC")
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC")
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDLtKrNoWVsbn97_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDLtKrNoWVsbn97_1_Fa8qkH1FL4DGDKf_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Plane", "plane_Sketch_F6AShJQnJ2NUuKc_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,11.43000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6AShJQnJ2NUuKc_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("Sketcher::SketchObject","Sketch_F6AShJQnJ2NUuKc_1_JNC")
App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6AShJQnJ2NUuKc_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC").addGeometry(Part.LineSegment(App.Vector(22.86000000000000,20.57400000000000,0.00000000000000),App.Vector(-22.86000000000000,20.57400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC").addGeometry(Part.LineSegment(App.Vector(-22.86000000000000,20.57400000000000,0.00000000000000),App.Vector(-22.86000000000000,-20.57400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC").addGeometry(Part.LineSegment(App.Vector(22.86000000000000,-20.57400000000000,0.00000000000000),App.Vector(-22.86000000000000,-20.57400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC").addGeometry(Part.LineSegment(App.Vector(22.86000000000000,20.57400000000000,0.00000000000000),App.Vector(22.86000000000000,-20.57400000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Pad","Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC")
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC")
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6AShJQnJ2NUuKc_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6AShJQnJ2NUuKc_1_Fa2gZePrTwaH1V4_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Plane", "plane_Sketch_FNLCkun4FO9Nic5_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,16.51000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNLCkun4FO9Nic5_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("Sketcher::SketchObject","Sketch_FNLCkun4FO9Nic5_1_JRC")
App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNLCkun4FO9Nic5_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC").addGeometry(Part.LineSegment(App.Vector(17.67840000000000,16.30680000000000,0.00000000000000),App.Vector(-17.67840000000000,16.30680000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC").addGeometry(Part.LineSegment(App.Vector(-17.67840000000000,16.30680000000000,0.00000000000000),App.Vector(-17.67840000000000,-16.30680000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC").addGeometry(Part.LineSegment(App.Vector(17.67840000000000,-16.30680000000000,0.00000000000000),App.Vector(-17.67840000000000,-16.30680000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC").addGeometry(Part.LineSegment(App.Vector(17.67840000000000,16.30680000000000,0.00000000000000),App.Vector(17.67840000000000,-16.30680000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Pad","Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC")
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC")
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNLCkun4FO9Nic5_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNLCkun4FO9Nic5_1_F1gncdthZTqOeL6_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Plane", "plane_Sketch_Fjs7PvAuasnxKSX_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,21.59000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fjs7PvAuasnxKSX_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("Sketcher::SketchObject","Sketch_Fjs7PvAuasnxKSX_1_JVC")
App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fjs7PvAuasnxKSX_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC").addGeometry(Part.LineSegment(App.Vector(12.23054000000000,11.33550000000000,0.00000000000000),App.Vector(-12.23054000000000,11.33550000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC").addGeometry(Part.LineSegment(App.Vector(-12.23054000000000,11.33550000000000,0.00000000000000),App.Vector(-12.23054000000000,-11.33550000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC").addGeometry(Part.LineSegment(App.Vector(12.23054000000000,-11.33550000000000,0.00000000000000),App.Vector(-12.23054000000000,-11.33550000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC").addGeometry(Part.LineSegment(App.Vector(12.23054000000000,11.33550000000000,0.00000000000000),App.Vector(12.23054000000000,-11.33550000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Pad","Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC")
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC")
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fjs7PvAuasnxKSX_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fjs7PvAuasnxKSX_1_FpE1LqYNTqizcsM_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Plane", "plane_Sketch_FRWXPULRQFpsOUO_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,26.67000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRWXPULRQFpsOUO_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("Sketcher::SketchObject","Sketch_FRWXPULRQFpsOUO_1_JZC")
App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRWXPULRQFpsOUO_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC").addGeometry(Part.LineSegment(App.Vector(9.44880000000000,7.46760000000000,0.00000000000000),App.Vector(-9.44880000000000,7.46760000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC").addGeometry(Part.LineSegment(App.Vector(-9.44880000000000,7.46760000000000,0.00000000000000),App.Vector(-9.44880000000000,-7.46760000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC").addGeometry(Part.LineSegment(App.Vector(9.44880000000000,-7.46760000000000,0.00000000000000),App.Vector(-9.44880000000000,-7.46760000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC").addGeometry(Part.LineSegment(App.Vector(9.44880000000000,7.46760000000000,0.00000000000000),App.Vector(9.44880000000000,-7.46760000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Pad","Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC")
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC")
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRWXPULRQFpsOUO_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRWXPULRQFpsOUO_1_FlO9guE9lai0b3Y_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Plane", "plane_Sketch_FF3TarTPpuGhgKn_1_JdC")
origin = App.Vector(0.00000000000000,-7.46760000000000,39.37000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FF3TarTPpuGhgKn_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("Sketcher::SketchObject","Sketch_FF3TarTPpuGhgKn_1_JdC")
App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FF3TarTPpuGhgKn_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC").addGeometry(Part.LineSegment(App.Vector(2.48034000000000,-0.36819000000000,0.00000000000000),App.Vector(-2.48034000000000,-0.36819000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC").addGeometry(Part.LineSegment(App.Vector(-2.48034000000000,-0.36819000000000,0.00000000000000),App.Vector(-2.48034000000000,7.12737000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC").addGeometry(Part.LineSegment(App.Vector(2.48034000000000,7.12737000000000,0.00000000000000),App.Vector(-2.48034000000000,7.12737000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC").addGeometry(Part.LineSegment(App.Vector(2.48034000000000,-0.36819000000000,0.00000000000000),App.Vector(2.48034000000000,7.12737000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Pocket","Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC")
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC")
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").Length = 39.370000000000005
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FF3TarTPpuGhgKn_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FF3TarTPpuGhgKn_1_FHDozF8VCLyhhz1_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Plane", "plane_Sketch_FVDdUaVALZFi0vG_1_JhC")
origin = App.Vector(-9.44880000000000,0.00000000000000,39.37000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVDdUaVALZFi0vG_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("Sketcher::SketchObject","Sketch_FVDdUaVALZFi0vG_1_JhC")
App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVDdUaVALZFi0vG_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC").addGeometry(Part.LineSegment(App.Vector(-1.53420000000000,-12.70000000000000,0.00000000000000),App.Vector(1.43834000000000,-12.70000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC").addGeometry(Part.LineSegment(App.Vector(1.43834000000000,-12.70000000000000,0.00000000000000),App.Vector(1.43834000000000,-5.97269000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC").addGeometry(Part.LineSegment(App.Vector(1.43834000000000,-5.97269000000000,0.00000000000000),App.Vector(-1.53420000000000,-5.97269000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC").addGeometry(Part.LineSegment(App.Vector(-1.53420000000000,-12.70000000000000,0.00000000000000),App.Vector(-1.53420000000000,-5.97269000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FJVvd22GAsoJox7_0").newObject("PartDesign::Pocket","Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC")
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC")
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").Length = 2.5400000000000005
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVDdUaVALZFi0vG_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVDdUaVALZFi0vG_1_FZD0HM9zdCQMEQ3_1_JhC").Offset = 0
App.ActiveDocument.recompute()

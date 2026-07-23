import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00940173")
App.ActiveDocument.addObject("PartDesign::Body","Body_FknBhJtB0P5v9zW_0")
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").Label = "Body_FknBhJtB0P5v9zW_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Plane", "plane_Sketch_FknBhJtB0P5v9zW_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FknBhJtB0P5v9zW_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("Sketcher::SketchObject","Sketch_FknBhJtB0P5v9zW_0_JGC")
App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FknBhJtB0P5v9zW_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC").addGeometry(Part.LineSegment(App.Vector(78.30820000000000,-34.92500000000000,0.00000000000000),App.Vector(-78.30820000000000,-34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC").addGeometry(Part.LineSegment(App.Vector(-78.30820000000000,-34.92500000000000,0.00000000000000),App.Vector(-78.30820000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC").addGeometry(Part.LineSegment(App.Vector(78.30820000000000,34.92500000000000,0.00000000000000),App.Vector(-78.30820000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC").addGeometry(Part.LineSegment(App.Vector(78.30820000000000,-34.92500000000000,0.00000000000000),App.Vector(78.30820000000000,34.92500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Pad","Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC")
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC")
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").Length = 50.8
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FknBhJtB0P5v9zW_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FknBhJtB0P5v9zW_0_FLsExgSYAYolodo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Plane", "plane_Sketch_Ft8YoUIsLctV5mR_1_JJC")
origin = App.Vector(0.00000000000000,-34.92500000000000,20.45051000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft8YoUIsLctV5mR_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("Sketcher::SketchObject","Sketch_Ft8YoUIsLctV5mR_1_JJC")
App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft8YoUIsLctV5mR_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-80.43166000000001,-14.96893000000000,0.00000000000000),App.Vector(-78.30820000000000,-13.65238000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-78.30820000000000,30.34949000000000,0.00000000000000),App.Vector(-78.30820000000000,-13.65238000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").addGeometry(Part.LineSegment(App.Vector(78.30820000000000,30.34949000000000,0.00000000000000),App.Vector(-78.30820000000000,30.34949000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").addGeometry(Part.LineSegment(App.Vector(78.30820000000000,30.34949000000000,0.00000000000000),App.Vector(78.30820000000000,20.45052000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").addGeometry(Part.LineSegment(App.Vector(78.30820000000000,20.45052000000000,0.00000000000000),App.Vector(84.01577000000000,32.25699999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").addGeometry(Part.LineSegment(App.Vector(84.01577000000000,32.25699999999999,0.00000000000000),App.Vector(-62.08945000000000,47.22593999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-62.08945000000000,47.22593999999999,0.00000000000000),App.Vector(-96.24392000000000,25.08878000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").addGeometry(Part.LineSegment(App.Vector(-80.43166000000001,-14.96893000000000,0.00000000000000),App.Vector(-96.24392000000000,25.08878000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Pocket","Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC")
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC")
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").Length = 90.424
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Plane", "plane_Sketch_Ft8YoUIsLctV5mR_1_JJK")
origin = App.Vector(0.00000000000000,-34.92500000000000,20.45051000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ft8YoUIsLctV5mR_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("Sketcher::SketchObject","Sketch_Ft8YoUIsLctV5mR_1_JJK")
App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ft8YoUIsLctV5mR_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(-59.34866000000000,-1.89747000000000,0.00000000000000),App.Vector(-78.30820000000000,-13.65238000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(-78.30820000000000,30.34949000000000,0.00000000000000),App.Vector(-78.30820000000000,-13.65238000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(78.30820000000000,30.34949000000000,0.00000000000000),App.Vector(-78.30820000000000,30.34949000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(78.30820000000000,30.34949000000000,0.00000000000000),App.Vector(78.30820000000000,20.45052000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(54.49956000000000,8.01155000000000,0.00000000000000),App.Vector(78.30820000000000,20.45052000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(41.00645000000000,4.84909000000000,0.00000000000000),App.Vector(54.49956000000000,8.01155000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(24.56170000000000,4.84909000000000,0.00000000000000),App.Vector(41.00645000000000,4.84909000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(18.44763000000000,-1.89747000000000,0.00000000000000),App.Vector(24.56170000000000,4.84909000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(-30.25411000000000,-1.89747000000000,0.00000000000000),App.Vector(18.44763000000000,-1.89747000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").addGeometry(Part.LineSegment(App.Vector(-59.34866000000000,-1.89747000000000,0.00000000000000),App.Vector(-30.25411000000000,-1.89747000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Pocket","Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK")
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK")
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").Length = 90.424
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ft8YoUIsLctV5mR_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ft8YoUIsLctV5mR_1_Ftfdrcs7if5w86r_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Plane", "plane_Sketch_FS9IgzOLmxzhEFy_1_JNC")
origin = App.Vector(-20.45051000000000,0.00000000000000,18.55304000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS9IgzOLmxzhEFy_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("Sketcher::SketchObject","Sketch_FS9IgzOLmxzhEFy_1_JNC")
App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS9IgzOLmxzhEFy_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.65974000000000,23.89752000000000,0.00000000000000),App.Vector(0.65974000000000,-20.94979000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.65974000000000,-20.94979000000000,0.00000000000000),App.Vector(29.37220000000000,-20.94979000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC").addGeometry(Part.LineSegment(App.Vector(29.37220000000000,-20.94979000000000,0.00000000000000),App.Vector(29.37220000000000,23.89752000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.65974000000000,23.89752000000000,0.00000000000000),App.Vector(29.37220000000000,23.89752000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Pocket","Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC")
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC")
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").Length = 10.921999999999999
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS9IgzOLmxzhEFy_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS9IgzOLmxzhEFy_1_FA7qia20fz3C7NF_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Plane", "plane_Sketch_FRg9uUMQj1iIUIH_1_JRC")
origin = App.Vector(0.00000000000000,-34.92500000000000,20.45051000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRg9uUMQj1iIUIH_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("Sketcher::SketchObject","Sketch_FRg9uUMQj1iIUIH_1_JRC")
App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRg9uUMQj1iIUIH_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC").addGeometry(Part.LineSegment(App.Vector(-67.39318000000000,-23.73255000000000,0.00000000000000),App.Vector(-65.64058000000000,-23.73255000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC").addGeometry(Part.LineSegment(App.Vector(-65.64058000000000,-23.73255000000000,0.00000000000000),App.Vector(-65.64058000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC").addGeometry(Part.LineSegment(App.Vector(-67.39318000000000,-20.45051000000000,0.00000000000000),App.Vector(-65.64058000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC").addGeometry(Part.LineSegment(App.Vector(-67.39318000000000,-23.73255000000000,0.00000000000000),App.Vector(-67.39318000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Pocket","Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC")
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC")
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").Length = 123.1646
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Plane", "plane_Sketch_FRg9uUMQj1iIUIH_1_JRG")
origin = App.Vector(0.00000000000000,-34.92500000000000,20.45051000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRg9uUMQj1iIUIH_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("Sketcher::SketchObject","Sketch_FRg9uUMQj1iIUIH_1_JRG")
App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRg9uUMQj1iIUIH_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG").addGeometry(Part.LineSegment(App.Vector(-67.39318000000000,-17.09771000000000,0.00000000000000),App.Vector(-65.64058000000000,-17.09771000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG").addGeometry(Part.LineSegment(App.Vector(-65.64058000000000,-17.09771000000000,0.00000000000000),App.Vector(-65.64058000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG").addGeometry(Part.LineSegment(App.Vector(-67.39318000000000,-20.45051000000000,0.00000000000000),App.Vector(-65.64058000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG").addGeometry(Part.LineSegment(App.Vector(-67.39318000000000,-17.09771000000000,0.00000000000000),App.Vector(-67.39318000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Pocket","Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG")
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG")
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").Length = 123.1646
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRg9uUMQj1iIUIH_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRg9uUMQj1iIUIH_1_FIMjnsXYDeS0VAM_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Plane", "plane_Sketch_FWfBldGQek49w5c_1_JVC")
origin = App.Vector(0.00000000000000,-34.92500000000000,20.45051000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWfBldGQek49w5c_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("Sketcher::SketchObject","Sketch_FWfBldGQek49w5c_1_JVC")
App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWfBldGQek49w5c_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC").addGeometry(Part.LineSegment(App.Vector(51.52854000000000,-25.60390000000000,0.00000000000000),App.Vector(53.28114000000000,-25.60390000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC").addGeometry(Part.LineSegment(App.Vector(53.28114000000000,-25.60390000000000,0.00000000000000),App.Vector(53.28114000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC").addGeometry(Part.LineSegment(App.Vector(51.52854000000000,-20.45051000000000,0.00000000000000),App.Vector(53.28114000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC").addGeometry(Part.LineSegment(App.Vector(51.52854000000000,-25.60390000000000,0.00000000000000),App.Vector(51.52854000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Pocket","Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC")
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC")
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").Length = 74.7776
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Plane", "plane_Sketch_FWfBldGQek49w5c_1_JVG")
origin = App.Vector(0.00000000000000,-34.92500000000000,20.45051000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWfBldGQek49w5c_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("Sketcher::SketchObject","Sketch_FWfBldGQek49w5c_1_JVG")
App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWfBldGQek49w5c_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG").addGeometry(Part.LineSegment(App.Vector(51.52854000000000,-17.09771000000000,0.00000000000000),App.Vector(53.28114000000000,-17.09771000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG").addGeometry(Part.LineSegment(App.Vector(53.28114000000000,-17.09771000000000,0.00000000000000),App.Vector(53.28114000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG").addGeometry(Part.LineSegment(App.Vector(51.52854000000000,-20.45051000000000,0.00000000000000),App.Vector(53.28114000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG").addGeometry(Part.LineSegment(App.Vector(51.52854000000000,-17.09771000000000,0.00000000000000),App.Vector(51.52854000000000,-20.45051000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FknBhJtB0P5v9zW_0").newObject("PartDesign::Pocket","Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG")
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG")
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").Length = 74.7776
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWfBldGQek49w5c_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWfBldGQek49w5c_1_Fo1eweAhVBcnmA3_1_JVG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00166524")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fkvi0PtEkz6TVHC_0")
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").Label = "Body_Fkvi0PtEkz6TVHC_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Plane", "plane_Sketch_Fkvi0PtEkz6TVHC_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fkvi0PtEkz6TVHC_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("Sketcher::SketchObject","Sketch_Fkvi0PtEkz6TVHC_0_JGC")
App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fkvi0PtEkz6TVHC_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC").addGeometry(Part.LineSegment(App.Vector(251.30031000000002,-120.00000000000000,0.00000000000000),App.Vector(-248.69969000000000,-120.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC").addGeometry(Part.LineSegment(App.Vector(-248.69969000000000,-120.00000000000000,0.00000000000000),App.Vector(-248.69969000000000,120.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC").addGeometry(Part.LineSegment(App.Vector(251.30031000000002,120.00000000000000,0.00000000000000),App.Vector(-248.69969000000000,120.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC").addGeometry(Part.LineSegment(App.Vector(251.30031000000002,-120.00000000000000,0.00000000000000),App.Vector(251.30031000000002,120.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Pad","Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC")
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC")
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").Length = 220.0
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fkvi0PtEkz6TVHC_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fkvi0PtEkz6TVHC_0_FDw56CmNPAJYTA0_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Plane", "plane_Sketch_FH2iYvMLEsZaKZC_1_JJC")
origin = App.Vector(1.30031000000000,0.00000000000000,220.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH2iYvMLEsZaKZC_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("Sketcher::SketchObject","Sketch_FH2iYvMLEsZaKZC_1_JJC")
App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH2iYvMLEsZaKZC_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJC").addGeometry(Part.Circle(App.Vector(-205.00000000000000,75.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Pad","Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC")
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJC")
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Plane", "plane_Sketch_FH2iYvMLEsZaKZC_1_JJG")
origin = App.Vector(1.30031000000000,0.00000000000000,220.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FH2iYvMLEsZaKZC_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("Sketcher::SketchObject","Sketch_FH2iYvMLEsZaKZC_1_JJG")
App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FH2iYvMLEsZaKZC_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJG").addGeometry(Part.Circle(App.Vector(-205.00000000000000,-75.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Pad","Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG")
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJG")
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").Length = 12.0
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FH2iYvMLEsZaKZC_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FH2iYvMLEsZaKZC_1_FW9BYQN076gh3HH_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Plane", "plane_Sketch_FoIWGsTlHWPmOnk_1_JNC")
origin = App.Vector(-203.69968999999998,75.00000000000000,232.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("Sketcher::SketchObject","Sketch_FoIWGsTlHWPmOnk_1_JNC")
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC").addGeometry(Part.LineSegment(App.Vector(6.13460999999998,-1.76500000000000,0.00000000000000),App.Vector(-6.13461000000001,-1.76500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC").addGeometry(Part.LineSegment(App.Vector(-6.13461000000001,-1.76500000000000,0.00000000000000),App.Vector(-6.13461000000001,1.76500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC").addGeometry(Part.LineSegment(App.Vector(6.13460999999998,1.76500000000000,0.00000000000000),App.Vector(-6.13461000000001,1.76500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC").addGeometry(Part.LineSegment(App.Vector(6.13460999999998,-1.76500000000000,0.00000000000000),App.Vector(6.13460999999998,1.76500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Pocket","Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Plane", "plane_Sketch_FoIWGsTlHWPmOnk_1_JNS")
origin = App.Vector(-203.69968999999998,75.00000000000000,232.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("Sketcher::SketchObject","Sketch_FoIWGsTlHWPmOnk_1_JNS")
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS").addGeometry(Part.LineSegment(App.Vector(-7.00000000000001,-151.25000000000000,0.00000000000000),App.Vector(-1.25000000000000,-151.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS").addGeometry(Part.LineSegment(App.Vector(-1.25000000000000,-151.25000000000000,0.00000000000000),App.Vector(-1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS").addGeometry(Part.LineSegment(App.Vector(-7.00000000000001,-148.75000000000000,0.00000000000000),App.Vector(-1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS").addGeometry(Part.LineSegment(App.Vector(-7.00000000000001,-151.25000000000000,0.00000000000000),App.Vector(-7.00000000000001,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Pocket","Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").Length = 3.0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Plane", "plane_Sketch_FoIWGsTlHWPmOnk_1_JNa")
origin = App.Vector(-203.69968999999998,75.00000000000000,232.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("Sketcher::SketchObject","Sketch_FoIWGsTlHWPmOnk_1_JNa")
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-151.25000000000000,0.00000000000000),App.Vector(-1.25000000000000,-151.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa").addGeometry(Part.LineSegment(App.Vector(-1.25000000000000,-151.25000000000000,0.00000000000000),App.Vector(-1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-148.75000000000000,0.00000000000000),App.Vector(-1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-151.25000000000000,0.00000000000000),App.Vector(1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Pocket","Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").Length = 3.0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").Type = 4
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Plane", "plane_Sketch_FoIWGsTlHWPmOnk_1_JNK")
origin = App.Vector(-203.69968999999998,75.00000000000000,232.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("Sketcher::SketchObject","Sketch_FoIWGsTlHWPmOnk_1_JNK")
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK").addGeometry(Part.LineSegment(App.Vector(6.99999999999998,-151.25000000000000,0.00000000000000),App.Vector(1.25000000000000,-151.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-151.25000000000000,0.00000000000000),App.Vector(1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK").addGeometry(Part.LineSegment(App.Vector(6.99999999999998,-148.75000000000000,0.00000000000000),App.Vector(1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK").addGeometry(Part.LineSegment(App.Vector(6.99999999999998,-151.25000000000000,0.00000000000000),App.Vector(6.99999999999998,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Pocket","Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").Length = 3.0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Plane", "plane_Sketch_FoIWGsTlHWPmOnk_1_JNW")
origin = App.Vector(-203.69968999999998,75.00000000000000,232.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("Sketcher::SketchObject","Sketch_FoIWGsTlHWPmOnk_1_JNW")
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-148.75000000000000,0.00000000000000),App.Vector(-1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW").addGeometry(Part.LineSegment(App.Vector(-1.25000000000000,-143.00000000000003,0.00000000000000),App.Vector(-1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-143.00000000000003,0.00000000000000),App.Vector(-1.25000000000000,-143.00000000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-143.00000000000003,0.00000000000000),App.Vector(1.25000000000000,-148.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Pocket","Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").Length = 3.0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Plane", "plane_Sketch_FoIWGsTlHWPmOnk_1_JNO")
origin = App.Vector(-203.69968999999998,75.00000000000000,232.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("Sketcher::SketchObject","Sketch_FoIWGsTlHWPmOnk_1_JNO")
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoIWGsTlHWPmOnk_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-151.25000000000000,0.00000000000000),App.Vector(-1.25000000000000,-151.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO").addGeometry(Part.LineSegment(App.Vector(-1.25000000000000,-157.00000000000000,0.00000000000000),App.Vector(-1.25000000000000,-151.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-157.00000000000000,0.00000000000000),App.Vector(-1.25000000000000,-157.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO").addGeometry(Part.LineSegment(App.Vector(1.25000000000000,-157.00000000000000,0.00000000000000),App.Vector(1.25000000000000,-151.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fkvi0PtEkz6TVHC_0").newObject("PartDesign::Pocket","Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO")
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").Length = 3.0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoIWGsTlHWPmOnk_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoIWGsTlHWPmOnk_1_FIg5fZeDy6zL9lx_1_JNO").Offset = 0
App.ActiveDocument.recompute()

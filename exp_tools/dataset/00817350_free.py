import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00817350")
App.ActiveDocument.addObject("PartDesign::Body","Body_FeM5MHOl57lMwyi")
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").Label = "Body_FeM5MHOl57lMwyi"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Plane", "plane_Sketch_FeM5MHOl57lMwyi_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeM5MHOl57lMwyi_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("Sketcher::SketchObject","Sketch_FeM5MHOl57lMwyi_JGC")
App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeM5MHOl57lMwyi_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-61.00000000000000,0.00000000000000),App.Vector(47.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(47.00000000000000,-16.00000000000000,0.00000000000000),App.Vector(47.00000000000000,6.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(47.00000000000000,6.50000000000000,0.00000000000000),App.Vector(35.00000000000000,19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,19.00000000000000,0.00000000000000),App.Vector(10.00000000000000,19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,19.00000000000000,0.00000000000000),App.Vector(0.00000000000000,9.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,9.00000000000000,0.00000000000000),App.Vector(-10.00000000000000,19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,19.00000000000000,0.00000000000000),App.Vector(-35.00000000000000,19.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(-35.00000000000000,19.00000000000000,0.00000000000000),App.Vector(-47.00000000000000,6.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(-47.00000000000000,6.50000000000000,0.00000000000000),App.Vector(-47.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-61.00000000000000,0.00000000000000),App.Vector(-47.00000000000000,-16.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Pad","Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC")
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC")
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeM5MHOl57lMwyi_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeM5MHOl57lMwyi_FOnpq21JCZ5RTi8_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Plane", "plane_Sketch_FylgsFJvkRe4LBV_1_JJC")
origin = App.Vector(0.00000000000000,-21.00000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("Sketcher::SketchObject","Sketch_FylgsFJvkRe4LBV_1_JJC")
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC").addGeometry(Part.LineSegment(App.Vector(41.00000000000000,17.86625000000000,0.00000000000000),App.Vector(25.76430000000000,33.73677000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC").addGeometry(Part.LineSegment(App.Vector(25.76430000000000,33.73677000000000,0.00000000000000),App.Vector(23.52800000000000,31.58993000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC").addGeometry(Part.LineSegment(App.Vector(38.76370000000000,15.71940000000000,0.00000000000000),App.Vector(23.52800000000000,31.58993000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC").addGeometry(Part.LineSegment(App.Vector(41.00000000000000,17.86625000000000,0.00000000000000),App.Vector(38.76370000000000,15.71940000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Pocket","Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Plane", "plane_Sketch_FylgsFJvkRe4LBV_1_JJS")
origin = App.Vector(0.00000000000000,-21.00000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("Sketcher::SketchObject","Sketch_FylgsFJvkRe4LBV_1_JJS")
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS").addGeometry(Part.LineSegment(App.Vector(20.10922000000000,-9.31253000000000,0.00000000000000),App.Vector(36.00000000000000,5.90205000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS").addGeometry(Part.LineSegment(App.Vector(36.00000000000000,5.90205000000000,0.00000000000000),App.Vector(33.85613000000000,8.14120000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS").addGeometry(Part.LineSegment(App.Vector(33.85613000000000,8.14120000000000,0.00000000000000),App.Vector(17.96535000000000,-7.07337000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS").addGeometry(Part.LineSegment(App.Vector(20.10922000000000,-9.31253000000000,0.00000000000000),App.Vector(17.96535000000000,-7.07337000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Pocket","Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").Length = 25.0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Plane", "plane_Sketch_FylgsFJvkRe4LBV_1_JJO")
origin = App.Vector(0.00000000000000,-21.00000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("Sketcher::SketchObject","Sketch_FylgsFJvkRe4LBV_1_JJO")
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO").addGeometry(Part.LineSegment(App.Vector(11.00000000000000,-21.16138000000000,0.00000000000000),App.Vector(-11.00000000000000,-21.16138000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO").addGeometry(Part.LineSegment(App.Vector(-11.00000000000000,-21.16138000000000,0.00000000000000),App.Vector(-11.00000000000000,-18.06138000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO").addGeometry(Part.LineSegment(App.Vector(-11.00000000000000,-18.06138000000000,0.00000000000000),App.Vector(11.00000000000000,-18.06138000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO").addGeometry(Part.LineSegment(App.Vector(11.00000000000000,-21.16138000000000,0.00000000000000),App.Vector(11.00000000000000,-18.06138000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Pocket","Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").Length = 25.0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Plane", "plane_Sketch_FylgsFJvkRe4LBV_1_JJW")
origin = App.Vector(0.00000000000000,-21.00000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("Sketcher::SketchObject","Sketch_FylgsFJvkRe4LBV_1_JJW")
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW").addGeometry(Part.LineSegment(App.Vector(-33.85613000000000,8.14120000000000,0.00000000000000),App.Vector(-17.96535000000000,-7.07337000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW").addGeometry(Part.LineSegment(App.Vector(-17.96535000000000,-7.07337000000000,0.00000000000000),App.Vector(-20.10922000000000,-9.31253000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW").addGeometry(Part.LineSegment(App.Vector(-20.10922000000000,-9.31253000000000,0.00000000000000),App.Vector(-36.00000000000000,5.90205000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW").addGeometry(Part.LineSegment(App.Vector(-33.85613000000000,8.14120000000000,0.00000000000000),App.Vector(-36.00000000000000,5.90205000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Pocket","Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").Length = 25.0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Plane", "plane_Sketch_FylgsFJvkRe4LBV_1_JJK")
origin = App.Vector(0.00000000000000,-21.00000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("Sketcher::SketchObject","Sketch_FylgsFJvkRe4LBV_1_JJK")
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK").addGeometry(Part.LineSegment(App.Vector(18.96595000000000,29.84417000000000,0.00000000000000),App.Vector(3.09542000000000,14.60847000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK").addGeometry(Part.LineSegment(App.Vector(3.09542000000000,14.60847000000000,0.00000000000000),App.Vector(0.94858000000000,16.84477000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK").addGeometry(Part.LineSegment(App.Vector(0.94858000000000,16.84477000000000,0.00000000000000),App.Vector(16.81910000000000,32.08047000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK").addGeometry(Part.LineSegment(App.Vector(18.96595000000000,29.84417000000000,0.00000000000000),App.Vector(16.81910000000000,32.08047000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Pocket","Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Plane", "plane_Sketch_FylgsFJvkRe4LBV_1_JJa")
origin = App.Vector(0.00000000000000,-21.00000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("Sketcher::SketchObject","Sketch_FylgsFJvkRe4LBV_1_JJa")
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa").addGeometry(Part.LineSegment(App.Vector(-3.09542000000000,14.60847000000000,0.00000000000000),App.Vector(-0.94858000000000,16.84477000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa").addGeometry(Part.LineSegment(App.Vector(-0.94858000000000,16.84477000000000,0.00000000000000),App.Vector(-16.81910000000000,32.08047000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa").addGeometry(Part.LineSegment(App.Vector(-16.81910000000000,32.08047000000000,0.00000000000000),App.Vector(-18.96595000000000,29.84417000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa").addGeometry(Part.LineSegment(App.Vector(-3.09542000000000,14.60847000000000,0.00000000000000),App.Vector(-18.96595000000000,29.84417000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Pocket","Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").Length = 25.0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Plane", "plane_Sketch_FylgsFJvkRe4LBV_1_JJG")
origin = App.Vector(0.00000000000000,-21.00000000000000,12.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("Sketcher::SketchObject","Sketch_FylgsFJvkRe4LBV_1_JJG")
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FylgsFJvkRe4LBV_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG").addGeometry(Part.LineSegment(App.Vector(-23.52800000000000,31.58993000000000,0.00000000000000),App.Vector(-25.76430000000000,33.73677000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG").addGeometry(Part.LineSegment(App.Vector(-25.76430000000000,33.73677000000000,0.00000000000000),App.Vector(-41.00000000000000,17.86625000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG").addGeometry(Part.LineSegment(App.Vector(-41.00000000000000,17.86625000000000,0.00000000000000),App.Vector(-38.76370000000000,15.71940000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG").addGeometry(Part.LineSegment(App.Vector(-23.52800000000000,31.58993000000000,0.00000000000000),App.Vector(-38.76370000000000,15.71940000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FeM5MHOl57lMwyi").newObject("PartDesign::Pocket","Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG")
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FylgsFJvkRe4LBV_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FylgsFJvkRe4LBV_1_FsMJ1rWloxYFqeX_1_JJG").Offset = 0
App.ActiveDocument.recompute()

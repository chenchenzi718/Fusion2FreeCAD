import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00998920")
App.ActiveDocument.addObject("PartDesign::Body","Body_FgniBRaWwg4Xscs_0")
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").Label = "Body_FgniBRaWwg4Xscs_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Plane", "plane_Sketch_FgniBRaWwg4Xscs_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgniBRaWwg4Xscs_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("Sketcher::SketchObject","Sketch_FgniBRaWwg4Xscs_0_JGC")
App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgniBRaWwg4Xscs_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),63.50000000000000),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),53.97500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Pad","Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC")
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGC")
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").Length = 22.225
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FqYrArvkoPMxTWM_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Plane", "plane_Sketch_FgniBRaWwg4Xscs_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgniBRaWwg4Xscs_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("Sketcher::SketchObject","Sketch_FgniBRaWwg4Xscs_0_JGK")
App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgniBRaWwg4Xscs_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),53.97500000000000),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-25.40000000000000,0.00000000000000),App.Vector(-25.40000000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-25.40000000000000,0.00000000000000),App.Vector(-25.40000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,25.40000000000000,0.00000000000000),App.Vector(-25.40000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-25.40000000000000,0.00000000000000),App.Vector(25.40000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Pad","Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK")
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").Profile = App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK")
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").Length = 11.1125
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_FBV6rfW0iGpNJ3a_1_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Plane", "plane_Sketch_FgniBRaWwg4Xscs_0_JGO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgniBRaWwg4Xscs_0_JGO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("Sketcher::SketchObject","Sketch_FgniBRaWwg4Xscs_0_JGO")
App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgniBRaWwg4Xscs_0_JGO"), [""])
App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-25.40000000000000,0.00000000000000),App.Vector(-25.40000000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").addGeometry(Part.LineSegment(App.Vector(-25.40000000000000,-25.40000000000000,0.00000000000000),App.Vector(-25.40000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,25.40000000000000,0.00000000000000),App.Vector(-25.40000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,-25.40000000000000,0.00000000000000),App.Vector(25.40000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").addGeometry(Part.LineSegment(App.Vector(-15.87500000000000,15.87500000000000,0.00000000000000),App.Vector(15.87500000000000,15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").addGeometry(Part.LineSegment(App.Vector(15.87500000000000,15.87500000000000,0.00000000000000),App.Vector(15.87500000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").addGeometry(Part.LineSegment(App.Vector(-15.87500000000000,-15.87500000000000,0.00000000000000),App.Vector(15.87500000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").addGeometry(Part.LineSegment(App.Vector(-15.87500000000000,15.87500000000000,0.00000000000000),App.Vector(-15.87500000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Pad","Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO")
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").Profile = App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO")
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").Length = 73.025
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgniBRaWwg4Xscs_0_JGO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").Type = 4
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgniBRaWwg4Xscs_0_F3JyWzBKmNDHp9i_1_JGO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Plane", "plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNa")
origin = App.Vector(18.25625000000000,-73.02500000000001,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("Sketcher::SketchObject","Sketch_Fk5SsBcj2ktKlQ1_1_JNa")
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,25.40000000000000,0.00000000000000),App.Vector(-7.14375000000000,15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,15.87500000000000,0.00000000000000),App.Vector(-29.36875000000000,15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa").addGeometry(Part.LineSegment(App.Vector(-29.36875000000000,25.40000000000000,0.00000000000000),App.Vector(-29.36875000000000,15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,25.40000000000000,0.00000000000000),App.Vector(-29.36875000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Pocket","Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").Type = 4
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Plane", "plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNG")
origin = App.Vector(18.25625000000000,-73.02500000000001,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("Sketcher::SketchObject","Sketch_Fk5SsBcj2ktKlQ1_1_JNG")
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,44.58390000000000,0.00000000000000),App.Vector(-29.36875000000000,44.58390000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG").addGeometry(Part.LineSegment(App.Vector(-29.36875000000000,44.58390000000000,0.00000000000000),App.Vector(-29.36875000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,25.40000000000000,0.00000000000000),App.Vector(-29.36875000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,44.58390000000000,0.00000000000000),App.Vector(-7.14375000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Pocket","Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Plane", "plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNW")
origin = App.Vector(18.25625000000000,-73.02500000000001,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("Sketcher::SketchObject","Sketch_Fk5SsBcj2ktKlQ1_1_JNW")
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,-15.87500000000000,0.00000000000000),App.Vector(-7.14375000000000,15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,15.87500000000000,0.00000000000000),App.Vector(-29.36875000000000,15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW").addGeometry(Part.LineSegment(App.Vector(-29.36875000000000,-15.87500000000000,0.00000000000000),App.Vector(-29.36875000000000,15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,-15.87500000000000,0.00000000000000),App.Vector(-29.36875000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Pocket","Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Plane", "plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNS")
origin = App.Vector(18.25625000000000,-73.02500000000001,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("Sketcher::SketchObject","Sketch_Fk5SsBcj2ktKlQ1_1_JNS")
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,-25.40000000000000,0.00000000000000),App.Vector(-7.14375000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,-15.87500000000000,0.00000000000000),App.Vector(-29.36875000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS").addGeometry(Part.LineSegment(App.Vector(-29.36875000000000,-25.40000000000000,0.00000000000000),App.Vector(-29.36875000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,-25.40000000000000,0.00000000000000),App.Vector(-29.36875000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Pocket","Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Plane", "plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNC")
origin = App.Vector(18.25625000000000,-73.02500000000001,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("Sketcher::SketchObject","Sketch_Fk5SsBcj2ktKlQ1_1_JNC")
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk5SsBcj2ktKlQ1_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,-44.58390000000000,0.00000000000000),App.Vector(-29.36875000000000,-44.58390000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC").addGeometry(Part.LineSegment(App.Vector(-29.36875000000000,-44.58390000000000,0.00000000000000),App.Vector(-29.36875000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,-25.40000000000000,0.00000000000000),App.Vector(-29.36875000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC").addGeometry(Part.LineSegment(App.Vector(-7.14375000000000,-44.58390000000000,0.00000000000000),App.Vector(-7.14375000000000,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgniBRaWwg4Xscs_0").newObject("PartDesign::Pocket","Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC")
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk5SsBcj2ktKlQ1_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk5SsBcj2ktKlQ1_1_FRx9tIMEjgHSPfF_1_JNC").Offset = 0
App.ActiveDocument.recompute()

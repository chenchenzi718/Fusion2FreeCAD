import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00079615")
App.ActiveDocument.addObject("PartDesign::Body","Body_FypMTFlHvZb6ue2")
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").Label = "Body_FypMTFlHvZb6ue2"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_FypMTFlHvZb6ue2_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FypMTFlHvZb6ue2_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_FypMTFlHvZb6ue2_JGC")
App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FypMTFlHvZb6ue2_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").addGeometry(Part.LineSegment(App.Vector(-26.81388000000000,-12.21605000000000,0.00000000000000),App.Vector(-24.94738000000000,-12.21605000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").addGeometry(Part.LineSegment(App.Vector(-24.94738000000000,-12.21605000000000,0.00000000000000),App.Vector(14.58810000000000,34.01485000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").addGeometry(Part.LineSegment(App.Vector(14.58810000000000,34.01485000000000,0.00000000000000),App.Vector(17.63612000000000,34.01485000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").addGeometry(Part.LineSegment(App.Vector(-21.89936000000000,-12.21605000000000,0.00000000000000),App.Vector(17.63612000000000,34.01485000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").addGeometry(Part.LineSegment(App.Vector(23.98612000000000,-12.21605000000000,0.00000000000000),App.Vector(-21.89936000000000,-12.21605000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").addGeometry(Part.LineSegment(App.Vector(23.98612000000000,-15.69077000000000,0.00000000000000),App.Vector(23.98612000000000,-12.21605000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").addGeometry(Part.LineSegment(App.Vector(-26.81388000000000,-15.69077000000000,0.00000000000000),App.Vector(23.98612000000000,-15.69077000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").addGeometry(Part.LineSegment(App.Vector(-26.81388000000000,-12.21605000000000,0.00000000000000),App.Vector(-26.81388000000000,-15.69077000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pad","Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC")
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC")
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").Length = 0.8890000000000001
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FypMTFlHvZb6ue2_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FypMTFlHvZb6ue2_FEHJKqOOJus2yNX_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_FN9qAIQrFDMnSzX_1_JJK")
origin = App.Vector(-3.54702000000000,11.02640000000000,0.88900000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FN9qAIQrFDMnSzX_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_FN9qAIQrFDMnSzX_1_JJK")
App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FN9qAIQrFDMnSzX_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK").addGeometry(Part.LineSegment(App.Vector(-21.40036000000000,-23.24245000000000,0.00000000000000),App.Vector(-18.35234000000000,-23.24245000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK").addGeometry(Part.LineSegment(App.Vector(-18.35234000000000,-23.24245000000000,0.00000000000000),App.Vector(-18.13513000000000,-22.98845000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK").addGeometry(Part.LineSegment(App.Vector(-18.13513000000000,-22.98845000000000,0.00000000000000),App.Vector(-21.18315000000000,-22.98845000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK").addGeometry(Part.LineSegment(App.Vector(-21.40036000000000,-23.24245000000000,0.00000000000000),App.Vector(-21.18315000000000,-22.98845000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pocket","Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK")
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK")
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").Length = 0.38100000000000006
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FN9qAIQrFDMnSzX_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FN9qAIQrFDMnSzX_1_F18OEfGWpMSlzNe_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_FGOQ6sECdLDil3U_1_JNC")
origin = App.Vector(-3.54702000000000,11.02640000000000,0.88900000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_FGOQ6sECdLDil3U_1_JNC")
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNC").addGeometry(Part.Circle(App.Vector(-19.83786000000000,-24.97727000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),0.38100000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pad","Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNC")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").Length = 0.25400000000000006
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_FGOQ6sECdLDil3U_1_JNG")
origin = App.Vector(-3.54702000000000,11.02640000000000,0.88900000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_FGOQ6sECdLDil3U_1_JNG")
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNG").addGeometry(Part.Circle(App.Vector(24.10414000000000,-24.96457000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),0.38100000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pad","Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNG")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").Length = 0.25400000000000006
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_FGOQ6sECdLDil3U_1_JNK")
origin = App.Vector(-3.54702000000000,11.02640000000000,0.88900000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_FGOQ6sECdLDil3U_1_JNK")
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNK").addGeometry(Part.Circle(App.Vector(-19.70695000000000,-22.49486000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),0.17780000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pad","Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNK")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").Length = 0.25400000000000006
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_FGOQ6sECdLDil3U_1_JNO")
origin = App.Vector(-3.54702000000000,11.02640000000000,0.88900000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_FGOQ6sECdLDil3U_1_JNO")
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNO").addGeometry(Part.Circle(App.Vector(-18.79004000000000,-21.87845000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),0.17780000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pad","Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNO")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").Length = 0.25400000000000006
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_FGOQ6sECdLDil3U_1_JNS")
origin = App.Vector(-3.54702000000000,11.02640000000000,0.88900000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_FGOQ6sECdLDil3U_1_JNS")
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNS").addGeometry(Part.Circle(App.Vector(19.24666000000000,22.02857000000001,0.00000000000000),App.Vector(0.0,0.0,1.0),0.17780000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pad","Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNS")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").Length = 0.25400000000000006
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_FGOQ6sECdLDil3U_1_JNW")
origin = App.Vector(-3.54702000000000,11.02640000000000,0.88900000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_FGOQ6sECdLDil3U_1_JNW")
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGOQ6sECdLDil3U_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNW").addGeometry(Part.Circle(App.Vector(17.91368000000000,21.42757000000000,0.00000000000000),App.Vector(0.0,0.0,1.0),0.17780000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pad","Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNW")
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").Length = 0.25400000000000006
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGOQ6sECdLDil3U_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGOQ6sECdLDil3U_1_F9AFXEIWrcaF4R1_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_Fosyf2YAwo322ab_1_JRC")
origin = App.Vector(-1.31267000000000,-13.95341000000000,0.88900000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fosyf2YAwo322ab_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_Fosyf2YAwo322ab_1_JRC")
App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fosyf2YAwo322ab_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC").addGeometry(Part.LineSegment(App.Vector(-23.64779000000000,1.73736000000000,0.00000000000000),App.Vector(-24.07443000000000,-1.73736000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC").addGeometry(Part.LineSegment(App.Vector(-25.50121000000000,-1.73736000000000,0.00000000000000),App.Vector(-24.07443000000000,-1.73736000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC").addGeometry(Part.LineSegment(App.Vector(-25.50121000000000,1.73736000000000,0.00000000000000),App.Vector(-25.50121000000000,-1.73736000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC").addGeometry(Part.LineSegment(App.Vector(-25.50121000000000,1.73736000000000,0.00000000000000),App.Vector(-23.64779000000000,1.73736000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pocket","Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC")
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC")
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Plane", "plane_Sketch_Fosyf2YAwo322ab_1_JRG")
origin = App.Vector(-1.31267000000000,-13.95341000000000,0.88900000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fosyf2YAwo322ab_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("Sketcher::SketchObject","Sketch_Fosyf2YAwo322ab_1_JRG")
App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fosyf2YAwo322ab_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG").addGeometry(Part.LineSegment(App.Vector(24.07443000000000,-1.73736000000000,0.00000000000000),App.Vector(23.64779000000000,1.73736000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG").addGeometry(Part.LineSegment(App.Vector(25.29879000000000,1.73736000000000,0.00000000000000),App.Vector(23.64779000000000,1.73736000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG").addGeometry(Part.LineSegment(App.Vector(25.29879000000000,-1.73736000000000,0.00000000000000),App.Vector(25.29879000000000,1.73736000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG").addGeometry(Part.LineSegment(App.Vector(25.29879000000000,-1.73736000000000,0.00000000000000),App.Vector(24.07443000000000,-1.73736000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FypMTFlHvZb6ue2").newObject("PartDesign::Pocket","Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG")
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG")
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fosyf2YAwo322ab_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fosyf2YAwo322ab_1_FZ6rlg44pfIsMUp_1_JRG").Offset = 0
App.ActiveDocument.recompute()

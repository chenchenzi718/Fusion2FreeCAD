import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00556536")
App.ActiveDocument.addObject("PartDesign::Body","Body_F43KKkxfBcuX5qr_0")
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").Label = "Body_F43KKkxfBcuX5qr_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_F43KKkxfBcuX5qr_0_JIC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F43KKkxfBcuX5qr_0_JIC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_F43KKkxfBcuX5qr_0_JIC")
App.ActiveDocument.getObject("Sketch_F43KKkxfBcuX5qr_0_JIC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F43KKkxfBcuX5qr_0_JIC"), [""])
App.ActiveDocument.getObject("Sketch_F43KKkxfBcuX5qr_0_JIC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F43KKkxfBcuX5qr_0_JIC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),18.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F43KKkxfBcuX5qr_0_JIC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F43KKkxfBcuX5qr_0_JIC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pad","Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC")
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").Profile = App.ActiveDocument.getObject("Sketch_F43KKkxfBcuX5qr_0_JIC")
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").Length = 26.4
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F43KKkxfBcuX5qr_0_JIC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").Type = 4
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F43KKkxfBcuX5qr_0_F97nugcDrijyMEX_0_JIC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_FzryOj3jKsbwPnx_0_JKC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzryOj3jKsbwPnx_0_JKC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_FzryOj3jKsbwPnx_0_JKC")
App.ActiveDocument.getObject("Sketch_FzryOj3jKsbwPnx_0_JKC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzryOj3jKsbwPnx_0_JKC"), [""])
App.ActiveDocument.getObject("Sketch_FzryOj3jKsbwPnx_0_JKC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzryOj3jKsbwPnx_0_JKC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),28.40000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzryOj3jKsbwPnx_0_JKC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzryOj3jKsbwPnx_0_JKC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pad","Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC")
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").Profile = App.ActiveDocument.getObject("Sketch_FzryOj3jKsbwPnx_0_JKC")
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").Length = 6.0
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzryOj3jKsbwPnx_0_JKC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").Type = 4
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzryOj3jKsbwPnx_0_FjNSd3WpYgegzCc_1_JKC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_FqelskpIhLMYUo6_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqelskpIhLMYUo6_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_FqelskpIhLMYUo6_0_JGC")
App.ActiveDocument.getObject("Sketch_FqelskpIhLMYUo6_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqelskpIhLMYUo6_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FqelskpIhLMYUo6_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqelskpIhLMYUo6_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),8.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqelskpIhLMYUo6_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqelskpIhLMYUo6_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pocket","Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC")
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").Profile = App.ActiveDocument.getObject("Sketch_FqelskpIhLMYUo6_0_JGC")
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").Length = 26.4
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqelskpIhLMYUo6_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqelskpIhLMYUo6_0_F4botOGOQnApSY1_1_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_F50NP5HXZFKxEsY_0_JMC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_F50NP5HXZFKxEsY_0_JMC")
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMC"), [""])
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMC").addGeometry(Part.Circle(App.Vector(-23.76073000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.60000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pocket","Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").Profile = App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMC")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").Length = 6.0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").Type = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_F50NP5HXZFKxEsY_0_JMG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_F50NP5HXZFKxEsY_0_JMG")
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMG"), [""])
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMG").addGeometry(Part.Circle(App.Vector(-11.88036000000000,-20.57739000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.60000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pocket","Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").Profile = App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMG")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").Length = 6.0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").Type = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").Reversed = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_F50NP5HXZFKxEsY_0_JMK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_F50NP5HXZFKxEsY_0_JMK")
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMK"), [""])
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMK").addGeometry(Part.Circle(App.Vector(11.88036000000000,-20.57739000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.60000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pocket","Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").Profile = App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMK")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").Length = 6.0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").Type = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").Reversed = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_F50NP5HXZFKxEsY_0_JMO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_F50NP5HXZFKxEsY_0_JMO")
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMO"), [""])
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMO").addGeometry(Part.Circle(App.Vector(23.76073000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.60000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pocket","Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").Profile = App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMO")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").Length = 6.0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").Type = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").Reversed = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_F50NP5HXZFKxEsY_0_JMS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_F50NP5HXZFKxEsY_0_JMS")
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMS"), [""])
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMS").addGeometry(Part.Circle(App.Vector(11.88036000000000,20.57739000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.60000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pocket","Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").Profile = App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMS")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").Length = 6.0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").Type = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").Reversed = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_F50NP5HXZFKxEsY_0_JMW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_F50NP5HXZFKxEsY_0_JMW")
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F50NP5HXZFKxEsY_0_JMW"), [""])
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMW").addGeometry(Part.Circle(App.Vector(-11.88036000000000,20.57739000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.60000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pocket","Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").Profile = App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMW")
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").Length = 6.0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F50NP5HXZFKxEsY_0_JMW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").Type = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").Reversed = 1
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F50NP5HXZFKxEsY_0_Fu9GlqgETsiCP9U_1_JMW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Plane", "plane_Sketch_FFSvw9rFmgAbI0B_1_JWC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFSvw9rFmgAbI0B_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("Sketcher::SketchObject","Sketch_FFSvw9rFmgAbI0B_1_JWC")
App.ActiveDocument.getObject("Sketch_FFSvw9rFmgAbI0B_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFSvw9rFmgAbI0B_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FFSvw9rFmgAbI0B_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFSvw9rFmgAbI0B_1_JWC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-16.21300000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFSvw9rFmgAbI0B_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFSvw9rFmgAbI0B_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F43KKkxfBcuX5qr_0").newObject("PartDesign::Pocket","Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC")
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FFSvw9rFmgAbI0B_1_JWC")
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").Length = 28.0
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFSvw9rFmgAbI0B_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFSvw9rFmgAbI0B_1_F5diLSfzIWfgCGV_1_JWC").Offset = 0
App.ActiveDocument.recompute()

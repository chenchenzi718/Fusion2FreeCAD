import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00664952")
App.ActiveDocument.addObject("PartDesign::Body","Body_FY44saUwK3sQy4W_0")
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").Label = "Body_FY44saUwK3sQy4W_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Plane", "plane_Sketch_FY44saUwK3sQy4W_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FY44saUwK3sQy4W_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("Sketcher::SketchObject","Sketch_FY44saUwK3sQy4W_0_JGC")
App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FY44saUwK3sQy4W_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(342.89999999999998,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC").addGeometry(Part.LineSegment(App.Vector(342.89999999999998,0.00000000000000,0.00000000000000),App.Vector(342.89999999999998,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,330.19999999999999,0.00000000000000),App.Vector(342.89999999999998,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,330.19999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Pad","Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC")
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC")
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FY44saUwK3sQy4W_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FY44saUwK3sQy4W_0_FkhczHRIIQjY8SF_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Plane", "plane_Sketch_FPczLuQPJ071U4B_1_JJG")
origin = App.Vector(171.44999999999999,-12.70000000000000,165.09999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPczLuQPJ071U4B_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("Sketcher::SketchObject","Sketch_FPczLuQPJ071U4B_1_JJG")
App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPczLuQPJ071U4B_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG").addGeometry(Part.LineSegment(App.Vector(-146.04999999999998,-152.40000000000001,0.00000000000000),App.Vector(146.05000000000001,-152.40000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG").addGeometry(Part.LineSegment(App.Vector(146.05000000000001,-152.40000000000001,0.00000000000000),App.Vector(146.05000000000001,133.34999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG").addGeometry(Part.LineSegment(App.Vector(146.05000000000001,133.34999999999999,0.00000000000000),App.Vector(-146.04999999999998,133.34999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG").addGeometry(Part.LineSegment(App.Vector(-146.04999999999998,-152.40000000000001,0.00000000000000),App.Vector(-146.04999999999998,133.34999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Pocket","Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG")
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG")
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPczLuQPJ071U4B_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPczLuQPJ071U4B_1_FEgShfpDzLyU7xz_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Plane", "plane_Sketch_FKbjsCUZAKXnlRP_1_JNC")
origin = App.Vector(171.44999999999999,-12.70000000000000,165.09999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKbjsCUZAKXnlRP_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("Sketcher::SketchObject","Sketch_FKbjsCUZAKXnlRP_1_JNC")
App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKbjsCUZAKXnlRP_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-165.09999999999999,161.92500000000001,0.00000000000000),App.Vector(-165.09999999999999,155.57499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-165.09999999999999,155.57499999999999,0.00000000000000),App.Vector(165.10000000000002,155.57499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC").addGeometry(Part.LineSegment(App.Vector(165.10000000000002,155.57499999999999,0.00000000000000),App.Vector(165.10000000000002,161.92500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC").addGeometry(Part.LineSegment(App.Vector(-165.09999999999999,161.92500000000001,0.00000000000000),App.Vector(165.10000000000002,161.92500000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Pocket","Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC")
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC")
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Plane", "plane_Sketch_FKbjsCUZAKXnlRP_1_JNG")
origin = App.Vector(171.44999999999999,-12.70000000000000,165.09999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKbjsCUZAKXnlRP_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("Sketcher::SketchObject","Sketch_FKbjsCUZAKXnlRP_1_JNG")
App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKbjsCUZAKXnlRP_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-165.09999999999999,130.17500000000001,0.00000000000000),App.Vector(-165.09999999999999,-130.17499999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-165.09999999999999,-130.17499999999998,0.00000000000000),App.Vector(-158.75000000000000,-130.17499999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-158.75000000000000,-130.17499999999998,0.00000000000000),App.Vector(-158.75000000000000,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-165.09999999999999,130.17500000000001,0.00000000000000),App.Vector(-158.75000000000000,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Pocket","Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG")
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG")
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Plane", "plane_Sketch_FKbjsCUZAKXnlRP_1_JNK")
origin = App.Vector(171.44999999999999,-12.70000000000000,165.09999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKbjsCUZAKXnlRP_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("Sketcher::SketchObject","Sketch_FKbjsCUZAKXnlRP_1_JNK")
App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKbjsCUZAKXnlRP_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK").addGeometry(Part.LineSegment(App.Vector(165.10000000000002,130.17500000000001,0.00000000000000),App.Vector(158.75000000000000,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK").addGeometry(Part.LineSegment(App.Vector(158.75000000000000,130.17500000000001,0.00000000000000),App.Vector(158.75000000000000,-130.17499999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK").addGeometry(Part.LineSegment(App.Vector(158.75000000000000,-130.17499999999998,0.00000000000000),App.Vector(165.10000000000002,-130.17499999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK").addGeometry(Part.LineSegment(App.Vector(165.10000000000002,130.17500000000001,0.00000000000000),App.Vector(165.10000000000002,-130.17499999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Pocket","Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK")
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK")
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKbjsCUZAKXnlRP_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKbjsCUZAKXnlRP_1_FhglLzytS8iafHI_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Plane", "plane_Sketch_F41JXt7TKYtrxdb_1_JRC")
origin = App.Vector(171.44999999999999,-1.58750000000000,12.70000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F41JXt7TKYtrxdb_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("Sketcher::SketchObject","Sketch_F41JXt7TKYtrxdb_1_JRC")
App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F41JXt7TKYtrxdb_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC").addGeometry(Part.LineSegment(App.Vector(-146.04999999999998,-11.11250000000000,0.00000000000000),App.Vector(146.05000000000001,-11.11250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC").addGeometry(Part.LineSegment(App.Vector(146.05000000000001,-11.11250000000000,0.00000000000000),App.Vector(146.05000000000001,-1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC").addGeometry(Part.LineSegment(App.Vector(-146.04999999999998,-1.58750000000000,0.00000000000000),App.Vector(146.05000000000001,-1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC").addGeometry(Part.LineSegment(App.Vector(-146.04999999999998,-11.11250000000000,0.00000000000000),App.Vector(-146.04999999999998,-1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Pad","Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC")
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC")
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F41JXt7TKYtrxdb_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F41JXt7TKYtrxdb_1_FJ23tJypmW7aoGS_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Plane", "plane_Sketch_FCngjLtaT8olkx8_1_JVC")
origin = App.Vector(171.44999999999999,-1.58750000000000,298.44999999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCngjLtaT8olkx8_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("Sketcher::SketchObject","Sketch_FCngjLtaT8olkx8_1_JVC")
App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCngjLtaT8olkx8_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC").addGeometry(Part.LineSegment(App.Vector(146.05000000000001,11.11250000000000,0.00000000000000),App.Vector(-146.04999999999998,11.11250000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC").addGeometry(Part.LineSegment(App.Vector(-146.04999999999998,11.11250000000000,0.00000000000000),App.Vector(-146.04999999999998,1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC").addGeometry(Part.LineSegment(App.Vector(-146.04999999999998,1.58750000000000,0.00000000000000),App.Vector(146.05000000000001,1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC").addGeometry(Part.LineSegment(App.Vector(146.05000000000001,11.11250000000000,0.00000000000000),App.Vector(146.05000000000001,1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Pad","Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC")
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC")
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCngjLtaT8olkx8_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCngjLtaT8olkx8_1_FSsjUBIRtBdLzQd_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Plane", "plane_Sketch_Ffc1ZcRAZelgtr0_1_JZC")
origin = App.Vector(317.50000000000000,-1.58750000000000,155.57499999999999)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ffc1ZcRAZelgtr0_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("Sketcher::SketchObject","Sketch_Ffc1ZcRAZelgtr0_1_JZC")
App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ffc1ZcRAZelgtr0_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC").addGeometry(Part.LineSegment(App.Vector(11.11250000000000,130.17500000000001,0.00000000000000),App.Vector(1.58750000000000,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC").addGeometry(Part.LineSegment(App.Vector(1.58750000000000,-130.17499999999998,0.00000000000000),App.Vector(1.58750000000000,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC").addGeometry(Part.LineSegment(App.Vector(11.11250000000000,-130.17499999999998,0.00000000000000),App.Vector(1.58750000000000,-130.17499999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC").addGeometry(Part.LineSegment(App.Vector(11.11250000000000,-130.17499999999998,0.00000000000000),App.Vector(11.11250000000000,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Pad","Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC")
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC")
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ffc1ZcRAZelgtr0_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ffc1ZcRAZelgtr0_1_FG30NWIinRPjp3O_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Plane", "plane_Sketch_FD8Lwt2RnfjyEVL_1_JdC")
origin = App.Vector(25.40000000000000,-1.58750000000000,155.57499999999999)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FD8Lwt2RnfjyEVL_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("Sketcher::SketchObject","Sketch_FD8Lwt2RnfjyEVL_1_JdC")
App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FD8Lwt2RnfjyEVL_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC").addGeometry(Part.LineSegment(App.Vector(-11.11250000000000,130.17500000000001,0.00000000000000),App.Vector(-1.58750000000000,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC").addGeometry(Part.LineSegment(App.Vector(-1.58750000000000,-130.17499999999998,0.00000000000000),App.Vector(-1.58750000000000,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC").addGeometry(Part.LineSegment(App.Vector(-11.11250000000000,-130.17499999999998,0.00000000000000),App.Vector(-1.58750000000000,-130.17499999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC").addGeometry(Part.LineSegment(App.Vector(-11.11250000000000,-130.17499999999998,0.00000000000000),App.Vector(-11.11250000000000,130.17500000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FY44saUwK3sQy4W_0").newObject("PartDesign::Pad","Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC")
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC")
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FD8Lwt2RnfjyEVL_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FD8Lwt2RnfjyEVL_1_F0AuZ6zkZ7utMRB_1_JdC").Offset = 0
App.ActiveDocument.recompute()

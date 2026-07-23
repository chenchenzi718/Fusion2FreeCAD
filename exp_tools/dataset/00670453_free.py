import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00670453")
App.ActiveDocument.addObject("PartDesign::Body","Body_FIF7kRbIoES4x27_0")
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").Label = "Body_FIF7kRbIoES4x27_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_FIF7kRbIoES4x27_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIF7kRbIoES4x27_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_FIF7kRbIoES4x27_0_JGC")
App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIF7kRbIoES4x27_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC").addGeometry(Part.LineSegment(App.Vector(46.22973000000000,-3.25000000000000,0.00000000000000),App.Vector(-43.77027000000000,-3.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC").addGeometry(Part.LineSegment(App.Vector(-43.77027000000000,-3.25000000000000,0.00000000000000),App.Vector(-43.77027000000000,3.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC").addGeometry(Part.LineSegment(App.Vector(46.22973000000000,3.25000000000000,0.00000000000000),App.Vector(-43.77027000000000,3.25000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC").addGeometry(Part.LineSegment(App.Vector(46.22973000000000,-3.25000000000000,0.00000000000000),App.Vector(46.22973000000000,3.25000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pad","Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC")
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC")
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIF7kRbIoES4x27_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIF7kRbIoES4x27_0_FsoSLDJeegvVJuu_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_FD0ZT1Qs8VCkIGU_1_JKC")
origin = App.Vector(1.22973000000000,-55.50000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FD0ZT1Qs8VCkIGU_1_JKC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_FD0ZT1Qs8VCkIGU_1_JKC")
App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FD0ZT1Qs8VCkIGU_1_JKC"), [""])
App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKC").addGeometry(Part.Circle(App.Vector(-41.74999999999999,55.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pocket","Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC")
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").Profile = App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKC")
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").Type = 4
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_FD0ZT1Qs8VCkIGU_1_JKG")
origin = App.Vector(1.22973000000000,-55.50000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FD0ZT1Qs8VCkIGU_1_JKG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_FD0ZT1Qs8VCkIGU_1_JKG")
App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FD0ZT1Qs8VCkIGU_1_JKG"), [""])
App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKG").addGeometry(Part.Circle(App.Vector(41.75000000000000,55.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pocket","Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG")
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").Profile = App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKG")
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FD0ZT1Qs8VCkIGU_1_JKG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").Type = 4
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FD0ZT1Qs8VCkIGU_1_Fto0qxFcA9XPG34_1_JKG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_FV0EPcnCZnMNnXd_1_JOC")
origin = App.Vector(36.86486000000000,-3.25000000000000,1.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FV0EPcnCZnMNnXd_1_JOC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_FV0EPcnCZnMNnXd_1_JOC")
App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FV0EPcnCZnMNnXd_1_JOC"), [""])
App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC").addGeometry(Part.LineSegment(App.Vector(-9.36486000000000,1.50000000000000,0.00000000000000),App.Vector(-64.36485999999999,1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC").addGeometry(Part.LineSegment(App.Vector(-64.36485999999999,1.50000000000000,0.00000000000000),App.Vector(-64.36485999999999,-1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC").addGeometry(Part.LineSegment(App.Vector(-9.36486000000000,-1.50000000000000,0.00000000000000),App.Vector(-64.36485999999999,-1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC").addGeometry(Part.LineSegment(App.Vector(-9.36486000000000,1.50000000000000,0.00000000000000),App.Vector(-9.36486000000000,-1.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pad","Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC")
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").Profile = App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC")
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").Length = 111.0
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FV0EPcnCZnMNnXd_1_JOC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").Type = 4
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FV0EPcnCZnMNnXd_1_FBjt47MxIh88KQg_1_JOC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_F59OYx5fqJI1qn5_1_JUC")
origin = App.Vector(1.22973000000000,-55.50000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F59OYx5fqJI1qn5_1_JUC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_F59OYx5fqJI1qn5_1_JUC")
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F59OYx5fqJI1qn5_1_JUC"), [""])
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUC").addGeometry(Part.Circle(App.Vector(-17.97973000000000,-48.74999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pocket","Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC")
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").Profile = App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUC")
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").Type = 4
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_F59OYx5fqJI1qn5_1_JUG")
origin = App.Vector(1.22973000000000,-55.50000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F59OYx5fqJI1qn5_1_JUG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_F59OYx5fqJI1qn5_1_JUG")
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F59OYx5fqJI1qn5_1_JUG"), [""])
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUG").addGeometry(Part.Circle(App.Vector(16.02027000000000,-48.74999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pocket","Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG")
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").Profile = App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUG")
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").Length = 25.0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").Type = 4
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_F59OYx5fqJI1qn5_1_JUK")
origin = App.Vector(1.22973000000000,-55.50000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F59OYx5fqJI1qn5_1_JUK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_F59OYx5fqJI1qn5_1_JUK")
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F59OYx5fqJI1qn5_1_JUK"), [""])
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUK").addGeometry(Part.Circle(App.Vector(19.02027000000000,-19.75000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.57087000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pocket","Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK")
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").Profile = App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUK")
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").Length = 25.0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").Type = 4
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_F59OYx5fqJI1qn5_1_JUO")
origin = App.Vector(1.22973000000000,-55.50000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F59OYx5fqJI1qn5_1_JUO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_F59OYx5fqJI1qn5_1_JUO")
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F59OYx5fqJI1qn5_1_JUO"), [""])
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUO").addGeometry(Part.Circle(App.Vector(-24.97973000000000,-16.74999999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pocket","Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO")
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").Profile = App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUO")
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").Length = 25.0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F59OYx5fqJI1qn5_1_JUO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").Type = 4
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F59OYx5fqJI1qn5_1_Fl5oNEr1lOeLHM3_1_JUO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_F1acjI3ql0H7llO_1_JYC")
origin = App.Vector(1.22973000000000,3.25000000000000,3.50000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1acjI3ql0H7llO_1_JYC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_F1acjI3ql0H7llO_1_JYC")
App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1acjI3ql0H7llO_1_JYC"), [""])
App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC").addGeometry(Part.LineSegment(App.Vector(-0.27027000000000,-0.50000000000000,0.00000000000000),App.Vector(2.72973000000000,-0.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC").addGeometry(Part.LineSegment(App.Vector(2.72973000000000,-0.50000000000000,0.00000000000000),App.Vector(2.72973000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC").addGeometry(Part.LineSegment(App.Vector(-0.27027000000000,2.50000000000000,0.00000000000000),App.Vector(2.72973000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC").addGeometry(Part.LineSegment(App.Vector(-0.27027000000000,-0.50000000000000,0.00000000000000),App.Vector(-0.27027000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pad","Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC")
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").Profile = App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC")
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").Length = 3.0
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1acjI3ql0H7llO_1_JYC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").Type = 0
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1acjI3ql0H7llO_1_FQ3nrH03E9VAhXg_1_JYC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Plane", "plane_Sketch_FtLhFoOhZHooZ9Q_1_JcC")
origin = App.Vector(1.22973000000000,3.25000000000000,3.50000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtLhFoOhZHooZ9Q_1_JcC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("Sketcher::SketchObject","Sketch_FtLhFoOhZHooZ9Q_1_JcC")
App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtLhFoOhZHooZ9Q_1_JcC"), [""])
App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC").addGeometry(Part.LineSegment(App.Vector(-0.27027000000000,2.50000000000000,0.00000000000000),App.Vector(2.72973000000000,2.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC").addGeometry(Part.LineSegment(App.Vector(2.72973000000000,2.50000000000000,0.00000000000000),App.Vector(2.72973000000000,3.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC").addGeometry(Part.LineSegment(App.Vector(-0.27027000000000,3.50000000000000,0.00000000000000),App.Vector(2.72973000000000,3.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC").addGeometry(Part.LineSegment(App.Vector(-0.27027000000000,2.50000000000000,0.00000000000000),App.Vector(-0.27027000000000,3.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FIF7kRbIoES4x27_0").newObject("PartDesign::Pad","Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC")
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").Profile = App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC")
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtLhFoOhZHooZ9Q_1_JcC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").Type = 0
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtLhFoOhZHooZ9Q_1_FHprouKem65uEcY_1_JcC").Offset = 0
App.ActiveDocument.recompute()

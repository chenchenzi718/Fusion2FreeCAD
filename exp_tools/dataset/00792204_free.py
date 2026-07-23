import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00792204")
App.ActiveDocument.addObject("PartDesign::Body","Body_F20uxCWJtzB3vWc_0")
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").Label = "Body_F20uxCWJtzB3vWc_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_F20uxCWJtzB3vWc_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F20uxCWJtzB3vWc_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_F20uxCWJtzB3vWc_0_JGC")
App.ActiveDocument.getObject("Sketch_F20uxCWJtzB3vWc_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F20uxCWJtzB3vWc_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F20uxCWJtzB3vWc_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F20uxCWJtzB3vWc_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),38.10000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F20uxCWJtzB3vWc_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F20uxCWJtzB3vWc_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pad","Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC")
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F20uxCWJtzB3vWc_0_JGC")
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F20uxCWJtzB3vWc_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F20uxCWJtzB3vWc_0_FSXYFoSNH6FZE0r_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_FJPla0icmZlKTmk_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,1.27000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJPla0icmZlKTmk_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_FJPla0icmZlKTmk_1_JJC")
App.ActiveDocument.getObject("Sketch_FJPla0icmZlKTmk_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJPla0icmZlKTmk_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FJPla0icmZlKTmk_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJPla0icmZlKTmk_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.17500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJPla0icmZlKTmk_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJPla0icmZlKTmk_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pocket","Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC")
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FJPla0icmZlKTmk_1_JJC")
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJPla0icmZlKTmk_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJPla0icmZlKTmk_1_FL2MN9ubId547v3_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_F8V1iQZLN1M8jcU_1_JLC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8V1iQZLN1M8jcU_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_F8V1iQZLN1M8jcU_1_JLC")
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8V1iQZLN1M8jcU_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLC").addGeometry(Part.Circle(App.Vector(-25.40000000000000,19.05000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.44500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pad","Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC")
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLC")
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_F8V1iQZLN1M8jcU_1_JLG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8V1iQZLN1M8jcU_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_F8V1iQZLN1M8jcU_1_JLG")
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8V1iQZLN1M8jcU_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLG").addGeometry(Part.Circle(App.Vector(25.40000000000000,19.05000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.44500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pad","Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG")
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLG")
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_F8V1iQZLN1M8jcU_1_JLK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8V1iQZLN1M8jcU_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_F8V1iQZLN1M8jcU_1_JLK")
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8V1iQZLN1M8jcU_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLK").addGeometry(Part.Circle(App.Vector(25.40000000000000,-19.05000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.44500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pad","Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK")
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLK")
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_F8V1iQZLN1M8jcU_1_JLO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F8V1iQZLN1M8jcU_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_F8V1iQZLN1M8jcU_1_JLO")
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F8V1iQZLN1M8jcU_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLO").addGeometry(Part.Circle(App.Vector(-25.40000000000000,-19.05000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.44500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pad","Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO")
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLO")
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").Length = 1.2700000000000002
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F8V1iQZLN1M8jcU_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F8V1iQZLN1M8jcU_1_FAhgB6YZDzDCsZT_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_FtAgUs7yYBoETnD_1_JRC")
origin = App.Vector(-25.40000000000000,-19.05000000000000,-1.27000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FtAgUs7yYBoETnD_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_FtAgUs7yYBoETnD_1_JRC")
App.ActiveDocument.getObject("Sketch_FtAgUs7yYBoETnD_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FtAgUs7yYBoETnD_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FtAgUs7yYBoETnD_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FtAgUs7yYBoETnD_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.30200000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FtAgUs7yYBoETnD_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FtAgUs7yYBoETnD_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pocket","Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC")
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FtAgUs7yYBoETnD_1_JRC")
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FtAgUs7yYBoETnD_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FtAgUs7yYBoETnD_1_FP0keufuOZyqMmN_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_FvlKtAtK5l3g4AK_1_JTC")
origin = App.Vector(-25.40000000000000,19.05000000000000,-1.27000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FvlKtAtK5l3g4AK_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_FvlKtAtK5l3g4AK_1_JTC")
App.ActiveDocument.getObject("Sketch_FvlKtAtK5l3g4AK_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FvlKtAtK5l3g4AK_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FvlKtAtK5l3g4AK_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FvlKtAtK5l3g4AK_1_JTC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.30200000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FvlKtAtK5l3g4AK_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FvlKtAtK5l3g4AK_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pocket","Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC")
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FvlKtAtK5l3g4AK_1_JTC")
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FvlKtAtK5l3g4AK_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FvlKtAtK5l3g4AK_1_FBZocPtS1E0kjHY_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_F02LIsGwI6zcTYw_1_JVC")
origin = App.Vector(25.40000000000000,-19.05000000000000,-1.27000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F02LIsGwI6zcTYw_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_F02LIsGwI6zcTYw_1_JVC")
App.ActiveDocument.getObject("Sketch_F02LIsGwI6zcTYw_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F02LIsGwI6zcTYw_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F02LIsGwI6zcTYw_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F02LIsGwI6zcTYw_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.30200000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F02LIsGwI6zcTYw_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F02LIsGwI6zcTYw_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pocket","Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC")
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F02LIsGwI6zcTYw_1_JVC")
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F02LIsGwI6zcTYw_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F02LIsGwI6zcTYw_1_Fh0XQ4pyHt2reKo_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Plane", "plane_Sketch_FKlv1pXRa762A27_1_JXC")
origin = App.Vector(25.40000000000000,19.05000000000000,-1.27000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FKlv1pXRa762A27_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("Sketcher::SketchObject","Sketch_FKlv1pXRa762A27_1_JXC")
App.ActiveDocument.getObject("Sketch_FKlv1pXRa762A27_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FKlv1pXRa762A27_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FKlv1pXRa762A27_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FKlv1pXRa762A27_1_JXC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.30200000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FKlv1pXRa762A27_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FKlv1pXRa762A27_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F20uxCWJtzB3vWc_0").newObject("PartDesign::Pocket","Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC")
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FKlv1pXRa762A27_1_JXC")
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FKlv1pXRa762A27_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FKlv1pXRa762A27_1_FUTSHu0FIZ3TNCG_1_JXC").Offset = 0
App.ActiveDocument.recompute()

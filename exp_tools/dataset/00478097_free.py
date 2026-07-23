import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00478097")
App.ActiveDocument.addObject("PartDesign::Body","Body_FU4jVLs7VeVbix0_0")
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").Label = "Body_FU4jVLs7VeVbix0_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Plane", "plane_Sketch_FU4jVLs7VeVbix0_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FU4jVLs7VeVbix0_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("Sketcher::SketchObject","Sketch_FU4jVLs7VeVbix0_0_JGC")
App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FU4jVLs7VeVbix0_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC").addGeometry(Part.LineSegment(App.Vector(40.90000000000000,-30.58000000000000,0.00000000000000),App.Vector(-40.90000000000000,-30.58000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC").addGeometry(Part.LineSegment(App.Vector(-40.90000000000000,-30.58000000000000,0.00000000000000),App.Vector(-40.90000000000000,30.58000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC").addGeometry(Part.LineSegment(App.Vector(40.90000000000000,30.58000000000000,0.00000000000000),App.Vector(-40.90000000000000,30.58000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC").addGeometry(Part.LineSegment(App.Vector(40.90000000000000,-30.58000000000000,0.00000000000000),App.Vector(40.90000000000000,30.58000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Pad","Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC")
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC")
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").Length = 24.5
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FU4jVLs7VeVbix0_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FU4jVLs7VeVbix0_0_FoWwx0K3tiLLVhb_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Plane", "plane_Sketch_FRICNVT4gDuEYcu_1_JJC")
origin = App.Vector(0.00000000000000,-0.00000000000000,24.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRICNVT4gDuEYcu_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("Sketcher::SketchObject","Sketch_FRICNVT4gDuEYcu_1_JJC")
App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRICNVT4gDuEYcu_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC").addGeometry(Part.LineSegment(App.Vector(38.90000000000000,-28.58000000000000,0.00000000000000),App.Vector(-38.90000000000000,-28.58000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC").addGeometry(Part.LineSegment(App.Vector(-38.90000000000000,-28.58000000000000,0.00000000000000),App.Vector(-38.90000000000000,28.58000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC").addGeometry(Part.LineSegment(App.Vector(38.90000000000000,28.58000000000000,0.00000000000000),App.Vector(-38.90000000000000,28.58000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC").addGeometry(Part.LineSegment(App.Vector(38.90000000000000,-28.58000000000000,0.00000000000000),App.Vector(38.90000000000000,28.58000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Pocket","Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC")
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC")
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").Length = 2.5
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRICNVT4gDuEYcu_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRICNVT4gDuEYcu_1_Fg3G5popuzpVu7B_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Plane", "plane_Sketch_F91t864GrKZ2hN7_1_JNC")
origin = App.Vector(-38.40000000000000,-4.45000000000000,22.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F91t864GrKZ2hN7_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("Sketcher::SketchObject","Sketch_F91t864GrKZ2hN7_1_JNC")
App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F91t864GrKZ2hN7_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC").addGeometry(Part.LineSegment(App.Vector(76.30000000000001,-22.63000000000000,0.00000000000000),App.Vector(0.49999999999999,-22.63000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.49999999999999,-22.63000000000000,0.00000000000000),App.Vector(0.49999999999999,31.53000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC").addGeometry(Part.LineSegment(App.Vector(76.30000000000001,31.53000000000000,0.00000000000000),App.Vector(0.49999999999999,31.53000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC").addGeometry(Part.LineSegment(App.Vector(76.30000000000001,-22.63000000000000,0.00000000000000),App.Vector(76.30000000000001,31.53000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Pocket","Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC")
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC")
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").Length = 13.5
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F91t864GrKZ2hN7_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F91t864GrKZ2hN7_1_F0TdaHIG1rbZZJy_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Plane", "plane_Sketch_FLj2TOVbHp77OFV_1_JRC")
origin = App.Vector(0.00000000000000,-0.00000000000000,8.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLj2TOVbHp77OFV_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("Sketcher::SketchObject","Sketch_FLj2TOVbHp77OFV_1_JRC")
App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLj2TOVbHp77OFV_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC").addGeometry(Part.LineSegment(App.Vector(-29.26000000000000,26.08000000000000,0.00000000000000),App.Vector(36.90000000000001,26.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC").addGeometry(Part.LineSegment(App.Vector(36.90000000000001,26.08000000000000,0.00000000000000),App.Vector(36.90000000000001,-26.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC").addGeometry(Part.LineSegment(App.Vector(-29.26000000000000,-26.08000000000000,0.00000000000000),App.Vector(36.90000000000001,-26.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC").addGeometry(Part.LineSegment(App.Vector(-29.26000000000000,26.08000000000000,0.00000000000000),App.Vector(-29.26000000000000,-26.08000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Pocket","Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC")
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC")
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").Length = 6.0
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLj2TOVbHp77OFV_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLj2TOVbHp77OFV_1_FFPot2k69TZEBg8_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Plane", "plane_Sketch_Ftrz1BuNiUvwlVm_1_JVG")
origin = App.Vector(0.00000000000000,-0.00000000000000,8.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftrz1BuNiUvwlVm_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("Sketcher::SketchObject","Sketch_Ftrz1BuNiUvwlVm_1_JVG")
App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftrz1BuNiUvwlVm_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").addGeometry(Part.LineSegment(App.Vector(-46.47736000000000,26.91908000000000,0.00000000000000),App.Vector(-37.90000000000001,26.91908000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").addGeometry(Part.LineSegment(App.Vector(-37.90000000000001,-27.08000000000000,0.00000000000000),App.Vector(-37.90000000000001,26.91908000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").addGeometry(Part.LineSegment(App.Vector(-37.90000000000001,-27.08000000000000,0.00000000000000),App.Vector(-31.26000000000000,-27.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").addGeometry(Part.LineSegment(App.Vector(-31.26000000000000,-27.09038000000000,0.00000000000000),App.Vector(-31.26000000000000,-27.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").addGeometry(Part.LineSegment(App.Vector(-46.47736000000000,-27.09038000000000,0.00000000000000),App.Vector(-31.26000000000000,-27.09038000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").addGeometry(Part.LineSegment(App.Vector(-46.47736000000000,26.91908000000000,0.00000000000000),App.Vector(-46.47736000000000,-27.09038000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Pad","Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG")
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG")
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").Length = 1.7
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Plane", "plane_Sketch_Ftrz1BuNiUvwlVm_1_JVK")
origin = App.Vector(0.00000000000000,-0.00000000000000,8.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftrz1BuNiUvwlVm_1_JVK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("Sketcher::SketchObject","Sketch_Ftrz1BuNiUvwlVm_1_JVK")
App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftrz1BuNiUvwlVm_1_JVK"), [""])
App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK").addGeometry(Part.LineSegment(App.Vector(-31.26000000000000,26.91908000000000,0.00000000000000),App.Vector(-37.90000000000001,26.91908000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK").addGeometry(Part.LineSegment(App.Vector(-37.90000000000001,-27.08000000000000,0.00000000000000),App.Vector(-37.90000000000001,26.91908000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK").addGeometry(Part.LineSegment(App.Vector(-37.90000000000001,-27.08000000000000,0.00000000000000),App.Vector(-31.26000000000000,-27.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK").addGeometry(Part.LineSegment(App.Vector(-31.26000000000000,26.91908000000000,0.00000000000000),App.Vector(-31.26000000000000,-27.08000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Pad","Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK")
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").Profile = App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK")
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").Length = 1.7
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftrz1BuNiUvwlVm_1_JVK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").Type = 4
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftrz1BuNiUvwlVm_1_Fp9Ixj1GF7xOx9x_1_JVK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Plane", "plane_Sketch_FEHSw1h5ULnQAOc_1_JZC")
origin = App.Vector(-40.90000000000000,-0.00000000000000,12.25000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEHSw1h5ULnQAOc_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("Sketcher::SketchObject","Sketch_FEHSw1h5ULnQAOc_1_JZC")
App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEHSw1h5ULnQAOc_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC").addGeometry(Part.LineSegment(App.Vector(-18.58000000000000,9.75000000000000,0.00000000000000),App.Vector(-4.42000000000000,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC").addGeometry(Part.LineSegment(App.Vector(-4.42000000000000,9.75000000000000,0.00000000000000),App.Vector(-4.42000000000000,-2.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC").addGeometry(Part.LineSegment(App.Vector(-4.42000000000000,-2.05000000000000,0.00000000000000),App.Vector(-18.58000000000000,-2.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC").addGeometry(Part.LineSegment(App.Vector(-18.58000000000000,9.75000000000000,0.00000000000000),App.Vector(-18.58000000000000,-2.05000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Pocket","Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC")
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC")
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").Length = 4.0
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Plane", "plane_Sketch_FEHSw1h5ULnQAOc_1_JZG")
origin = App.Vector(-40.90000000000000,-0.00000000000000,12.25000000000000)
x_axis=App.Vector(-0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEHSw1h5ULnQAOc_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("Sketcher::SketchObject","Sketch_FEHSw1h5ULnQAOc_1_JZG")
App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEHSw1h5ULnQAOc_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG").addGeometry(Part.LineSegment(App.Vector(13.32000000000000,9.75000000000000,0.00000000000000),App.Vector(24.22000000000000,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG").addGeometry(Part.LineSegment(App.Vector(24.22000000000000,9.75000000000000,0.00000000000000),App.Vector(24.22000000000000,-2.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG").addGeometry(Part.LineSegment(App.Vector(24.22000000000000,-2.05000000000000,0.00000000000000),App.Vector(13.32000000000000,-2.05000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG").addGeometry(Part.LineSegment(App.Vector(13.32000000000000,9.75000000000000,0.00000000000000),App.Vector(13.32000000000000,-2.05000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FU4jVLs7VeVbix0_0").newObject("PartDesign::Pocket","Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG")
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG")
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").Length = 4.0
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEHSw1h5ULnQAOc_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEHSw1h5ULnQAOc_1_F4q3GbFOAIgRuLl_1_JZG").Offset = 0
App.ActiveDocument.recompute()

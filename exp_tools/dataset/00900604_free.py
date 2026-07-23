import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00900604")
App.ActiveDocument.addObject("PartDesign::Body","Body_FS243wIJy57llCw_0")
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").Label = "Body_FS243wIJy57llCw_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Plane", "plane_Sketch_FS243wIJy57llCw_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS243wIJy57llCw_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("Sketcher::SketchObject","Sketch_FS243wIJy57llCw_0_JGC")
App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS243wIJy57llCw_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC").addGeometry(Part.LineSegment(App.Vector(117.47499999999999,117.47499999999999,0.00000000000000),App.Vector(-117.47499999999999,117.47499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC").addGeometry(Part.LineSegment(App.Vector(-117.47499999999999,117.47499999999999,0.00000000000000),App.Vector(-117.47499999999999,-117.47499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC").addGeometry(Part.LineSegment(App.Vector(117.47499999999999,-117.47499999999999,0.00000000000000),App.Vector(-117.47499999999999,-117.47499999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC").addGeometry(Part.LineSegment(App.Vector(117.47499999999999,117.47499999999999,0.00000000000000),App.Vector(117.47499999999999,-117.47499999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Pad","Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC")
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC")
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS243wIJy57llCw_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS243wIJy57llCw_0_FSEDK5FxiiPujxo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Plane", "plane_Sketch_FMBMXH5CES3nnaf_1_JJS")
origin = App.Vector(0.00000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("Sketcher::SketchObject","Sketch_FMBMXH5CES3nnaf_1_JJS")
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,63.50000000000000,0.00000000000000),App.Vector(-63.50000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,38.10000000000000,0.00000000000000),App.Vector(-63.50000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,38.10000000000000,0.00000000000000),App.Vector(-38.10000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,63.50000000000000,0.00000000000000),App.Vector(-38.10000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Pocket","Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Plane", "plane_Sketch_FMBMXH5CES3nnaf_1_JJW")
origin = App.Vector(0.00000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("Sketcher::SketchObject","Sketch_FMBMXH5CES3nnaf_1_JJW")
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,63.50000000000000,0.00000000000000),App.Vector(63.50000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,38.10000000000000,0.00000000000000),App.Vector(63.50000000000000,63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,38.10000000000000,0.00000000000000),App.Vector(38.10000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,63.50000000000000,0.00000000000000),App.Vector(38.10000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Pocket","Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Plane", "plane_Sketch_FMBMXH5CES3nnaf_1_JJa")
origin = App.Vector(0.00000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("Sketcher::SketchObject","Sketch_FMBMXH5CES3nnaf_1_JJa")
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJa"), [""])
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,-63.50000000000000,0.00000000000000),App.Vector(63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,-38.10000000000000,0.00000000000000),App.Vector(63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,-38.10000000000000,0.00000000000000),App.Vector(38.10000000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa").addGeometry(Part.LineSegment(App.Vector(38.10000000000000,-63.50000000000000,0.00000000000000),App.Vector(38.10000000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Pocket","Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").Profile = App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").Type = 4
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Plane", "plane_Sketch_FMBMXH5CES3nnaf_1_JJe")
origin = App.Vector(0.00000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("Sketcher::SketchObject","Sketch_FMBMXH5CES3nnaf_1_JJe")
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJe"), [""])
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,-63.50000000000000,0.00000000000000),App.Vector(-63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,-38.10000000000000,0.00000000000000),App.Vector(-63.50000000000000,-63.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,-38.10000000000000,0.00000000000000),App.Vector(-38.10000000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,-63.50000000000000,0.00000000000000),App.Vector(-38.10000000000000,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Pocket","Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").Profile = App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").Type = 4
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Plane", "plane_Sketch_FMBMXH5CES3nnaf_1_JJq")
origin = App.Vector(0.00000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJq").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("Sketcher::SketchObject","Sketch_FMBMXH5CES3nnaf_1_JJq")
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJq").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJq"), [""])
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJq").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJq").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1.58750000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJq").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),0.0,1.5707963267949),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJq").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJq").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJq").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Pocket","Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").Profile = App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJq")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJq"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").Type = 4
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJq").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Plane", "plane_Sketch_FMBMXH5CES3nnaf_1_JJm")
origin = App.Vector(0.00000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJm").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("Sketcher::SketchObject","Sketch_FMBMXH5CES3nnaf_1_JJm")
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJm").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJm"), [""])
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJm").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJm").addGeometry(Part.LineSegment(App.Vector(-1.58750000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJm").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJm").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJm").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJm").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Pocket","Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").Profile = App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJm")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJm"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").Type = 4
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJm").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Plane", "plane_Sketch_FMBMXH5CES3nnaf_1_JJu")
origin = App.Vector(0.00000000000000,0.00000000000000,6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJu").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("Sketcher::SketchObject","Sketch_FMBMXH5CES3nnaf_1_JJu")
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJu").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FMBMXH5CES3nnaf_1_JJu"), [""])
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJu").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJu").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(1.58750000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJu").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),4.71238898038469,0.0),False)

App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJu").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-1.58750000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJu").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJu").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS243wIJy57llCw_0").newObject("PartDesign::Pocket","Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").Profile = App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJu")
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FMBMXH5CES3nnaf_1_JJu"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").Type = 4
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").UpToFace = None
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").Reversed = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").Midplane = 0
App.ActiveDocument.getObject("Extrude_FMBMXH5CES3nnaf_1_FmfABAJuuXnzVjn_1_JJu").Offset = 0
App.ActiveDocument.recompute()

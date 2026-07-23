import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00328692")
App.ActiveDocument.addObject("PartDesign::Body","Body_FYslZUUXBQUI5jg_0")
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").Label = "Body_FYslZUUXBQUI5jg_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Plane", "plane_Sketch_FYslZUUXBQUI5jg_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYslZUUXBQUI5jg_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("Sketcher::SketchObject","Sketch_FYslZUUXBQUI5jg_0_JGC")
App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYslZUUXBQUI5jg_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC").addGeometry(Part.LineSegment(App.Vector(-64.46189000000000,46.91553000000000,0.00000000000000),App.Vector(46.66311000000000,46.91553000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC").addGeometry(Part.LineSegment(App.Vector(46.66311000000000,46.91553000000000,0.00000000000000),App.Vector(46.66311000000000,-55.70047000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC").addGeometry(Part.LineSegment(App.Vector(-64.46189000000000,-55.70047000000000,0.00000000000000),App.Vector(46.66311000000000,-55.70047000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC").addGeometry(Part.LineSegment(App.Vector(-64.46189000000000,46.91553000000000,0.00000000000000),App.Vector(-64.46189000000000,-55.70047000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Pad","Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC")
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC")
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").Length = 1.9989800000000004
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYslZUUXBQUI5jg_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYslZUUXBQUI5jg_0_FITX0Hcjz7owO1n_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Plane", "plane_Sketch_FoDxddatOSjlk86_1_JJC")
origin = App.Vector(-8.89939000000000,-1.99898000000000,-4.39247000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoDxddatOSjlk86_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("Sketcher::SketchObject","Sketch_FoDxddatOSjlk86_1_JJC")
App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoDxddatOSjlk86_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC").addGeometry(Part.LineSegment(App.Vector(-16.72590000000000,27.30500000000000,0.00000000000000),App.Vector(39.15410000000000,27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC").addGeometry(Part.LineSegment(App.Vector(39.15410000000000,27.30500000000000,0.00000000000000),App.Vector(39.15410000000000,-27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC").addGeometry(Part.LineSegment(App.Vector(-16.72590000000000,-27.30500000000000,0.00000000000000),App.Vector(39.15410000000000,-27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC").addGeometry(Part.LineSegment(App.Vector(-16.72590000000000,27.30500000000000,0.00000000000000),App.Vector(-16.72590000000000,-27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Pocket","Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC")
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC")
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").Length = 1.1099800000000002
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoDxddatOSjlk86_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoDxddatOSjlk86_1_FHgAGUOcBOxPSdB_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Plane", "plane_Sketch_FywuAYt2mRWBYjm_1_JNC")
origin = App.Vector(-8.89939000000000,0.00000000000000,-4.39247000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FywuAYt2mRWBYjm_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("Sketcher::SketchObject","Sketch_FywuAYt2mRWBYjm_1_JNC")
App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FywuAYt2mRWBYjm_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.48250000000000,44.95800000000001,0.00000000000000),App.Vector(26.73350000000000,44.95800000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC").addGeometry(Part.LineSegment(App.Vector(26.73350000000000,44.95800000000001,0.00000000000000),App.Vector(26.73350000000000,-44.95800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.48250000000000,-44.95800000000000,0.00000000000000),App.Vector(26.73350000000000,-44.95800000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC").addGeometry(Part.LineSegment(App.Vector(-50.48250000000000,44.95800000000001,0.00000000000000),App.Vector(-50.48250000000000,-44.95800000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Pocket","Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC")
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC")
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").Length = 0.8890000000000001
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FywuAYt2mRWBYjm_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FywuAYt2mRWBYjm_1_FLwfdjjPIle6tvT_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Plane", "plane_Sketch_FkVf65FPHLUrpaj_1_JRG")
origin = App.Vector(2.97511000000000,-0.88900000000000,-4.39247000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkVf65FPHLUrpaj_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("Sketcher::SketchObject","Sketch_FkVf65FPHLUrpaj_1_JRG")
App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkVf65FPHLUrpaj_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG").addGeometry(Part.LineSegment(App.Vector(28.60040000000000,27.30500000000000,0.00000000000000),App.Vector(-27.27960000000000,27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG").addGeometry(Part.LineSegment(App.Vector(-27.27960000000000,27.30500000000000,0.00000000000000),App.Vector(-27.27960000000000,-27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG").addGeometry(Part.LineSegment(App.Vector(28.60040000000000,-27.30500000000000,0.00000000000000),App.Vector(-27.27960000000000,-27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG").addGeometry(Part.LineSegment(App.Vector(28.60040000000000,27.30500000000000,0.00000000000000),App.Vector(28.60040000000000,-27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Pad","Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG")
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG")
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").Length = 0.65024
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Plane", "plane_Sketch_FkVf65FPHLUrpaj_1_JRK")
origin = App.Vector(2.97511000000000,-0.88900000000000,-4.39247000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkVf65FPHLUrpaj_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("Sketcher::SketchObject","Sketch_FkVf65FPHLUrpaj_1_JRK")
App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkVf65FPHLUrpaj_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").addGeometry(Part.LineSegment(App.Vector(-38.60800000000000,44.95800000000001,0.00000000000000),App.Vector(37.59200000000000,44.95800000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").addGeometry(Part.LineSegment(App.Vector(37.59200000000000,44.95800000000001,0.00000000000000),App.Vector(37.59200000000000,-43.94199999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").addGeometry(Part.LineSegment(App.Vector(-38.60800000000000,-43.94199999999999,0.00000000000000),App.Vector(37.59200000000000,-43.94199999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").addGeometry(Part.LineSegment(App.Vector(-38.60800000000000,44.95800000000001,0.00000000000000),App.Vector(-38.60800000000000,-43.94199999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").addGeometry(Part.LineSegment(App.Vector(28.60040000000000,27.30500000000000,0.00000000000000),App.Vector(-27.27960000000000,27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").addGeometry(Part.LineSegment(App.Vector(-27.27960000000000,27.30500000000000,0.00000000000000),App.Vector(-27.27960000000000,-27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").addGeometry(Part.LineSegment(App.Vector(28.60040000000000,-27.30500000000000,0.00000000000000),App.Vector(-27.27960000000000,-27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").addGeometry(Part.LineSegment(App.Vector(28.60040000000000,27.30500000000000,0.00000000000000),App.Vector(28.60040000000000,-27.30500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Pad","Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK")
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK")
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").Length = 0.65024
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkVf65FPHLUrpaj_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkVf65FPHLUrpaj_1_FsMbB6UkCUslIJW_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Plane", "plane_Sketch_Fhgf4WW8E5t8Zxw_1_JVC")
origin = App.Vector(3.48311000000000,-0.23876000000000,-3.88447000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fhgf4WW8E5t8Zxw_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("Sketcher::SketchObject","Sketch_Fhgf4WW8E5t8Zxw_1_JVC")
App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fhgf4WW8E5t8Zxw_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC").addGeometry(Part.LineSegment(App.Vector(-27.68600000000000,28.19400000000000,0.00000000000000),App.Vector(28.70200000000000,28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC").addGeometry(Part.LineSegment(App.Vector(28.70200000000000,28.19400000000000,0.00000000000000),App.Vector(28.70200000000000,-28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC").addGeometry(Part.LineSegment(App.Vector(-27.68600000000000,-28.19400000000000,0.00000000000000),App.Vector(28.70200000000000,-28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC").addGeometry(Part.LineSegment(App.Vector(-27.68600000000000,28.19400000000000,0.00000000000000),App.Vector(-27.68600000000000,-28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Pocket","Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC")
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC")
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").Length = 0.65024
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fhgf4WW8E5t8Zxw_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fhgf4WW8E5t8Zxw_1_FClXoIjradetUxb_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Plane", "plane_Sketch_FGccFlnQeLWiTJw_1_JZG")
origin = App.Vector(3.48311000000000,-0.23876000000000,-3.88447000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGccFlnQeLWiTJw_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("Sketcher::SketchObject","Sketch_FGccFlnQeLWiTJw_1_JZG")
App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGccFlnQeLWiTJw_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG").addGeometry(Part.LineSegment(App.Vector(-27.68600000000000,28.19400000000000,0.00000000000000),App.Vector(28.70200000000000,28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG").addGeometry(Part.LineSegment(App.Vector(28.70200000000000,28.19400000000000,0.00000000000000),App.Vector(28.70200000000000,-28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG").addGeometry(Part.LineSegment(App.Vector(-27.68600000000000,-28.19400000000000,0.00000000000000),App.Vector(28.70200000000000,-28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG").addGeometry(Part.LineSegment(App.Vector(-27.68600000000000,28.19400000000000,0.00000000000000),App.Vector(-27.68600000000000,-28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Pad","Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG")
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG")
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").Length = 0.59944
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Plane", "plane_Sketch_FGccFlnQeLWiTJw_1_JZK")
origin = App.Vector(3.48311000000000,-0.23876000000000,-3.88447000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGccFlnQeLWiTJw_1_JZK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("Sketcher::SketchObject","Sketch_FGccFlnQeLWiTJw_1_JZK")
App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGccFlnQeLWiTJw_1_JZK"), [""])
App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").addGeometry(Part.LineSegment(App.Vector(-31.48838000000000,31.67126000000000,0.00000000000000),App.Vector(32.50438000000000,31.67126000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").addGeometry(Part.LineSegment(App.Vector(32.50438000000000,31.67126000000000,0.00000000000000),App.Vector(32.50438000000000,-32.68980000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").addGeometry(Part.LineSegment(App.Vector(-31.48838000000000,-32.68980000000000,0.00000000000000),App.Vector(32.50438000000000,-32.68980000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").addGeometry(Part.LineSegment(App.Vector(-31.48838000000000,31.67126000000000,0.00000000000000),App.Vector(-31.48838000000000,-32.68980000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").addGeometry(Part.LineSegment(App.Vector(-27.68600000000000,28.19400000000000,0.00000000000000),App.Vector(28.70200000000000,28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").addGeometry(Part.LineSegment(App.Vector(28.70200000000000,28.19400000000000,0.00000000000000),App.Vector(28.70200000000000,-28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").addGeometry(Part.LineSegment(App.Vector(-27.68600000000000,-28.19400000000000,0.00000000000000),App.Vector(28.70200000000000,-28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").addGeometry(Part.LineSegment(App.Vector(-27.68600000000000,28.19400000000000,0.00000000000000),App.Vector(-27.68600000000000,-28.19400000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FYslZUUXBQUI5jg_0").newObject("PartDesign::Pad","Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK")
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").Profile = App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK")
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").Length = 0.59944
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGccFlnQeLWiTJw_1_JZK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").Type = 4
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGccFlnQeLWiTJw_1_FBraBZ1LpvJnXj1_1_JZK").Offset = 0
App.ActiveDocument.recompute()

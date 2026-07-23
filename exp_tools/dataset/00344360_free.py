import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00344360")
App.ActiveDocument.addObject("PartDesign::Body","Body_FS4t6DN9BwcOfs0_0")
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").Label = "Body_FS4t6DN9BwcOfs0_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_JGK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_JGK")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGK"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGK").addGeometry(Part.LineSegment(App.Vector(-84.42800000000000,0.00000000000000,0.00000000000000),App.Vector(-90.88930000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGK").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-90.88930000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGK").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-84.42800000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGK")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_JGS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_JGS")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGS"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGS").addGeometry(Part.LineSegment(App.Vector(-71.81189000000001,0.00000000000000,0.00000000000000),App.Vector(-77.96648999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGS").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-77.96648999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGS").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-71.81189000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGS")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_JGa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_JGa")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGa"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGa").addGeometry(Part.LineSegment(App.Vector(-59.76853000000000,0.00000000000000,0.00000000000000),App.Vector(-65.64333999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGa").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-65.64333999999999,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGa").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-59.76853000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGa")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_JGi")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGi").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_JGi")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGi").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGi"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGi").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGi").addGeometry(Part.LineSegment(App.Vector(-46.55020000000000,0.00000000000000,0.00000000000000),App.Vector(-53.59997000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGi").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-53.59997000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGi").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-46.55020000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGi").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGi").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGi")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGi"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGi").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_JGq")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGq").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_JGq")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGq").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGq"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGq").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGq").addGeometry(Part.LineSegment(App.Vector(-33.33186000000000,0.00000000000000,0.00000000000000),App.Vector(-40.38164000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGq").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-40.38164000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGq").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-33.33186000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGq").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGq").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGq")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGq"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGq").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_JGy")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGy").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_JGy")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGy").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGy"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGy").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGy").addGeometry(Part.LineSegment(App.Vector(-16.00116000000000,0.00000000000000,0.00000000000000),App.Vector(-24.81339000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGy").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-24.81339000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGy").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-16.00116000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGy").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGy").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGy")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGy"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGy").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_JG6")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JG6").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_JG6")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JG6").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JG6"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JG6").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JG6").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-7.77643000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JG6").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(-7.77643000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JG6").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JG6").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JG6").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JG6")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JG6"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JG6").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_KGCB")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_KGCB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_KGCB")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGCB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_KGCB"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGCB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGCB").addGeometry(Part.LineSegment(App.Vector(17.48527000000000,0.00000000000000,0.00000000000000),App.Vector(8.08557000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGCB").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(8.08557000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGCB").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(17.48527000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGCB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGCB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGCB")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGCB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGCB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_KGKB")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_KGKB").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_KGKB")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGKB").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_KGKB"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGKB").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGKB").addGeometry(Part.LineSegment(App.Vector(37.45964000000000,0.00000000000000,0.00000000000000),App.Vector(27.76619000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGKB").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(27.76619000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGKB").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(37.45964000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGKB").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGKB").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGKB")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_KGKB"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_KGKB").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Plane", "plane_Sketch_FS4t6DN9BwcOfs0_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("Sketcher::SketchObject","Sketch_FS4t6DN9BwcOfs0_0_JGG")
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FS4t6DN9BwcOfs0_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGG").addGeometry(Part.LineSegment(App.Vector(57.12334000000000,0.00000000000000,0.00000000000000),App.Vector(48.03430000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGG").addGeometry(Part.LineSegment(App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000),App.Vector(48.03430000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGG").addGeometry(Part.LineSegment(App.Vector(57.12334000000000,0.00000000000000,0.00000000000000),App.Vector(-22.79000000000000,164.47505000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FS4t6DN9BwcOfs0_0").newObject("PartDesign::Pad","Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGG")
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FS4t6DN9BwcOfs0_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FS4t6DN9BwcOfs0_0_FqV8hwmfDkJ23AO_0_JGG").Offset = 0
App.ActiveDocument.recompute()

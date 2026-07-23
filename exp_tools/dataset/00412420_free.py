import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00412420")
App.ActiveDocument.addObject("PartDesign::Body","Body_FuFQdrhS8tHVTMa_0")
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").Label = "Body_FuFQdrhS8tHVTMa_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Plane", "plane_Sketch_FuFQdrhS8tHVTMa_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuFQdrhS8tHVTMa_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("Sketcher::SketchObject","Sketch_FuFQdrhS8tHVTMa_0_JGC")
App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuFQdrhS8tHVTMa_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC").addGeometry(Part.LineSegment(App.Vector(46.50000000000000,30.00000000000000,0.00000000000000),App.Vector(-46.50000000000000,30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC").addGeometry(Part.LineSegment(App.Vector(-46.50000000000000,30.00000000000000,0.00000000000000),App.Vector(-46.50000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC").addGeometry(Part.LineSegment(App.Vector(46.50000000000000,-30.00000000000000,0.00000000000000),App.Vector(-46.50000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC").addGeometry(Part.LineSegment(App.Vector(46.50000000000000,30.00000000000000,0.00000000000000),App.Vector(46.50000000000000,-30.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Pad","Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC")
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC")
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuFQdrhS8tHVTMa_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuFQdrhS8tHVTMa_0_Fd334l5C1gy61Up_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Plane", "plane_Sketch_FGl8YXTV0gmu3MP_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,2.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FGl8YXTV0gmu3MP_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("Sketcher::SketchObject","Sketch_FGl8YXTV0gmu3MP_1_JJC")
App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FGl8YXTV0gmu3MP_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC").addGeometry(Part.LineSegment(App.Vector(43.50000000000000,-27.00000000000000,0.00000000000000),App.Vector(-43.50000000000000,-27.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC").addGeometry(Part.LineSegment(App.Vector(-43.50000000000000,-27.00000000000000,0.00000000000000),App.Vector(-43.50000000000000,27.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC").addGeometry(Part.LineSegment(App.Vector(43.50000000000000,27.00000000000000,0.00000000000000),App.Vector(-43.50000000000000,27.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC").addGeometry(Part.LineSegment(App.Vector(43.50000000000000,-27.00000000000000,0.00000000000000),App.Vector(43.50000000000000,27.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Pad","Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC")
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC")
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").Length = 4.0
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FGl8YXTV0gmu3MP_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FGl8YXTV0gmu3MP_1_FB12lGMydGWYeN0_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Plane", "plane_Sketch_FjNMI6I0CuMx3Cc_1_JNC")
origin = App.Vector(0.00000000000000,-0.00000000000000,6.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjNMI6I0CuMx3Cc_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("Sketcher::SketchObject","Sketch_FjNMI6I0CuMx3Cc_1_JNC")
App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjNMI6I0CuMx3Cc_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC").addGeometry(Part.LineSegment(App.Vector(41.50000000000000,-25.00000000000000,0.00000000000000),App.Vector(-41.50000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC").addGeometry(Part.LineSegment(App.Vector(-41.50000000000000,-25.00000000000000,0.00000000000000),App.Vector(-41.50000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC").addGeometry(Part.LineSegment(App.Vector(41.50000000000000,25.00000000000000,0.00000000000000),App.Vector(-41.50000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC").addGeometry(Part.LineSegment(App.Vector(41.50000000000000,-25.00000000000000,0.00000000000000),App.Vector(41.50000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Pocket","Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC")
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC")
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").Length = 3.0
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjNMI6I0CuMx3Cc_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjNMI6I0CuMx3Cc_1_FsE2M4SnEU0iTmZ_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Plane", "plane_Sketch_FUr1p1KzTH22Tht_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("Sketcher::SketchObject","Sketch_FUr1p1KzTH22Tht_1_JRC")
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC").addGeometry(Part.LineSegment(App.Vector(-32.03629000000000,20.00000000000000,0.00000000000000),App.Vector(-36.83629000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC").addGeometry(Part.LineSegment(App.Vector(-36.83629000000000,20.00000000000000,0.00000000000000),App.Vector(-36.83629000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC").addGeometry(Part.LineSegment(App.Vector(-32.03629000000000,-20.00000000000000,0.00000000000000),App.Vector(-36.83629000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC").addGeometry(Part.LineSegment(App.Vector(-32.03629000000000,20.00000000000000,0.00000000000000),App.Vector(-32.03629000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Pocket","Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").Length = 4.0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Plane", "plane_Sketch_FUr1p1KzTH22Tht_1_JRG")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("Sketcher::SketchObject","Sketch_FUr1p1KzTH22Tht_1_JRG")
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG").addGeometry(Part.LineSegment(App.Vector(-23.20000000000000,20.00000000000000,0.00000000000000),App.Vector(-23.20000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG").addGeometry(Part.LineSegment(App.Vector(-23.20000000000000,-20.00000000000000,0.00000000000000),App.Vector(-18.40000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG").addGeometry(Part.LineSegment(App.Vector(-18.40000000000000,20.00000000000000,0.00000000000000),App.Vector(-18.40000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG").addGeometry(Part.LineSegment(App.Vector(-23.20000000000000,20.00000000000000,0.00000000000000),App.Vector(-18.40000000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Pocket","Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").Length = 4.0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Plane", "plane_Sketch_FUr1p1KzTH22Tht_1_JRK")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("Sketcher::SketchObject","Sketch_FUr1p1KzTH22Tht_1_JRK")
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK").addGeometry(Part.LineSegment(App.Vector(-9.56371000000000,20.00000000000000,0.00000000000000),App.Vector(-9.56371000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK").addGeometry(Part.LineSegment(App.Vector(-9.56371000000000,-20.00000000000000,0.00000000000000),App.Vector(-4.76371000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK").addGeometry(Part.LineSegment(App.Vector(-4.76371000000000,20.00000000000000,0.00000000000000),App.Vector(-4.76371000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK").addGeometry(Part.LineSegment(App.Vector(-9.56371000000000,20.00000000000000,0.00000000000000),App.Vector(-4.76371000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Pocket","Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").Length = 4.0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Plane", "plane_Sketch_FUr1p1KzTH22Tht_1_JRO")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("Sketcher::SketchObject","Sketch_FUr1p1KzTH22Tht_1_JRO")
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRO"), [""])
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO").addGeometry(Part.LineSegment(App.Vector(4.07257000000000,20.00000000000000,0.00000000000000),App.Vector(4.07257000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO").addGeometry(Part.LineSegment(App.Vector(4.07257000000000,-20.00000000000000,0.00000000000000),App.Vector(8.87257000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO").addGeometry(Part.LineSegment(App.Vector(8.87257000000000,20.00000000000000,0.00000000000000),App.Vector(8.87257000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO").addGeometry(Part.LineSegment(App.Vector(4.07257000000000,20.00000000000000,0.00000000000000),App.Vector(8.87257000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Pocket","Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").Profile = App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").Length = 4.0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").Type = 4
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Plane", "plane_Sketch_FUr1p1KzTH22Tht_1_JRS")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("Sketcher::SketchObject","Sketch_FUr1p1KzTH22Tht_1_JRS")
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRS"), [""])
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS").addGeometry(Part.LineSegment(App.Vector(17.70886000000000,20.00000000000000,0.00000000000000),App.Vector(17.70886000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS").addGeometry(Part.LineSegment(App.Vector(17.70886000000000,-20.00000000000000,0.00000000000000),App.Vector(22.50886000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS").addGeometry(Part.LineSegment(App.Vector(22.50886000000000,20.00000000000000,0.00000000000000),App.Vector(22.50886000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS").addGeometry(Part.LineSegment(App.Vector(17.70886000000000,20.00000000000000,0.00000000000000),App.Vector(22.50886000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Pocket","Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").Profile = App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").Length = 4.0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").Type = 4
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Plane", "plane_Sketch_FUr1p1KzTH22Tht_1_JRW")
origin = App.Vector(0.00000000000000,0.00000000000000,3.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("Sketcher::SketchObject","Sketch_FUr1p1KzTH22Tht_1_JRW")
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUr1p1KzTH22Tht_1_JRW"), [""])
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW").addGeometry(Part.LineSegment(App.Vector(31.34514000000000,20.00000000000000,0.00000000000000),App.Vector(31.34514000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW").addGeometry(Part.LineSegment(App.Vector(31.34514000000000,-20.00000000000000,0.00000000000000),App.Vector(36.14514000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW").addGeometry(Part.LineSegment(App.Vector(36.14514000000000,20.00000000000000,0.00000000000000),App.Vector(36.14514000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW").addGeometry(Part.LineSegment(App.Vector(31.34514000000000,20.00000000000000,0.00000000000000),App.Vector(36.14514000000000,20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FuFQdrhS8tHVTMa_0").newObject("PartDesign::Pocket","Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").Profile = App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW")
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").Length = 4.0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUr1p1KzTH22Tht_1_JRW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").Type = 4
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUr1p1KzTH22Tht_1_FpnxHgV97sg6Nx7_1_JRW").Offset = 0
App.ActiveDocument.recompute()

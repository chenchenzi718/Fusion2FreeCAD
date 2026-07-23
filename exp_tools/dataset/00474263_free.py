import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00474263")
App.ActiveDocument.addObject("PartDesign::Body","Body_FCByKGzRiQePJZk_0")
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").Label = "Body_FCByKGzRiQePJZk_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Plane", "plane_Sketch_FCByKGzRiQePJZk_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCByKGzRiQePJZk_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("Sketcher::SketchObject","Sketch_FCByKGzRiQePJZk_0_JGC")
App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCByKGzRiQePJZk_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC").addGeometry(Part.LineSegment(App.Vector(23.97760000000000,-3.93700000000000,0.00000000000000),App.Vector(-23.97760000000000,-3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC").addGeometry(Part.LineSegment(App.Vector(-23.97760000000000,-3.93700000000000,0.00000000000000),App.Vector(-23.97760000000000,3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC").addGeometry(Part.LineSegment(App.Vector(23.97760000000000,3.93700000000000,0.00000000000000),App.Vector(-23.97760000000000,3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC").addGeometry(Part.LineSegment(App.Vector(23.97760000000000,-3.93700000000000,0.00000000000000),App.Vector(23.97760000000000,3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Pad","Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC")
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC")
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").Length = 3.1750000000000003
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCByKGzRiQePJZk_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCByKGzRiQePJZk_0_F9iQ4qxGZgUkgVi_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Plane", "plane_Sketch_FPbvSvX2A1AldIJ_1_JJu")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJu").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("Sketcher::SketchObject","Sketch_FPbvSvX2A1AldIJ_1_JJu")
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJu"), [""])
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").addGeometry(Part.LineSegment(App.Vector(22.35200000000000,-2.37490000000000,0.00000000000000),App.Vector(-22.35200000000000,-2.37490000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").addGeometry(Part.LineSegment(App.Vector(-22.35200000000000,-2.37490000000000,0.00000000000000),App.Vector(-22.35200000000000,2.37490000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").addGeometry(Part.LineSegment(App.Vector(22.35200000000000,2.37490000000000,0.00000000000000),App.Vector(-22.35200000000000,2.37490000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").addGeometry(Part.LineSegment(App.Vector(22.35200000000000,-2.37490000000000,0.00000000000000),App.Vector(22.35200000000000,2.37490000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.42240000000000),False)

App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").addGeometry(Part.Circle(App.Vector(8.00100000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.42240000000000),False)

App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").addGeometry(Part.Circle(App.Vector(16.00200000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.42240000000000),False)

App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").addGeometry(Part.Circle(App.Vector(-8.00100000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.42240000000000),False)

App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").addGeometry(Part.Circle(App.Vector(-16.00200000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.42240000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Pocket","Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").Profile = App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").Length = 2.0828
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJu"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").Type = 4
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FJXsIBJi6eBdr5m_1_JJu").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Plane", "plane_Sketch_FPbvSvX2A1AldIJ_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("Sketcher::SketchObject","Sketch_FPbvSvX2A1AldIJ_1_JJO")
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJO").addGeometry(Part.Circle(App.Vector(16.00200000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.82550000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Pocket","Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJO")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").Length = 2.0828
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Plane", "plane_Sketch_FPbvSvX2A1AldIJ_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("Sketcher::SketchObject","Sketch_FPbvSvX2A1AldIJ_1_JJK")
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJK").addGeometry(Part.Circle(App.Vector(8.00100000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.82550000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Pocket","Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJK")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").Length = 2.0828
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Plane", "plane_Sketch_FPbvSvX2A1AldIJ_1_JJS")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("Sketcher::SketchObject","Sketch_FPbvSvX2A1AldIJ_1_JJS")
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJS").addGeometry(Part.Circle(App.Vector(-8.00100000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.82550000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Pocket","Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJS")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").Length = 2.0828
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").Type = 4
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Plane", "plane_Sketch_FPbvSvX2A1AldIJ_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("Sketcher::SketchObject","Sketch_FPbvSvX2A1AldIJ_1_JJG")
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJG").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.82550000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Pocket","Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJG")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").Length = 2.0828
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Plane", "plane_Sketch_FPbvSvX2A1AldIJ_1_JJW")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("Sketcher::SketchObject","Sketch_FPbvSvX2A1AldIJ_1_JJW")
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPbvSvX2A1AldIJ_1_JJW"), [""])
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJW").addGeometry(Part.Circle(App.Vector(-16.00200000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),0.82550000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Pocket","Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").Profile = App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJW")
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").Length = 2.0828
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPbvSvX2A1AldIJ_1_JJW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").Type = 4
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPbvSvX2A1AldIJ_1_FCNoHPs6fXJ5dnU_1_JJW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Plane", "plane_Sketch_FoTYjdqCXfcEden_1_JPC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoTYjdqCXfcEden_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("Sketcher::SketchObject","Sketch_FoTYjdqCXfcEden_1_JPC")
App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoTYjdqCXfcEden_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").addGeometry(Part.LineSegment(App.Vector(24.53674000000000,4.67732000000000,0.00000000000000),App.Vector(-24.53674000000000,4.67732000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").addGeometry(Part.LineSegment(App.Vector(-24.53674000000000,4.67732000000000,0.00000000000000),App.Vector(-24.53674000000000,-4.67732000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").addGeometry(Part.LineSegment(App.Vector(24.53674000000000,-4.67732000000000,0.00000000000000),App.Vector(-24.53674000000000,-4.67732000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").addGeometry(Part.LineSegment(App.Vector(24.53674000000000,4.67732000000000,0.00000000000000),App.Vector(24.53674000000000,-4.67732000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").addGeometry(Part.LineSegment(App.Vector(23.97760000000000,-3.93700000000000,0.00000000000000),App.Vector(-23.97760000000000,-3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").addGeometry(Part.LineSegment(App.Vector(-23.97760000000000,-3.93700000000000,0.00000000000000),App.Vector(-23.97760000000000,3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").addGeometry(Part.LineSegment(App.Vector(23.97760000000000,3.93700000000000,0.00000000000000),App.Vector(-23.97760000000000,3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").addGeometry(Part.LineSegment(App.Vector(23.97760000000000,-3.93700000000000,0.00000000000000),App.Vector(23.97760000000000,3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Pocket","Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC")
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC")
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").Length = 0.5080000000000001
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Plane", "plane_Sketch_FoTYjdqCXfcEden_1_JPO")
origin = App.Vector(0.00000000000000,0.00000000000000,3.17500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoTYjdqCXfcEden_1_JPO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("Sketcher::SketchObject","Sketch_FoTYjdqCXfcEden_1_JPO")
App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoTYjdqCXfcEden_1_JPO"), [""])
App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").addGeometry(Part.LineSegment(App.Vector(23.49500000000000,-3.54330000000000,0.00000000000000),App.Vector(-23.49500000000000,-3.54330000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").addGeometry(Part.LineSegment(App.Vector(-23.49500000000000,-3.54330000000000,0.00000000000000),App.Vector(-23.49500000000000,3.54330000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").addGeometry(Part.LineSegment(App.Vector(23.49500000000000,3.54330000000000,0.00000000000000),App.Vector(-23.49500000000000,3.54330000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").addGeometry(Part.LineSegment(App.Vector(23.49500000000000,-3.54330000000000,0.00000000000000),App.Vector(23.49500000000000,3.54330000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").addGeometry(Part.LineSegment(App.Vector(23.97760000000000,-3.93700000000000,0.00000000000000),App.Vector(-23.97760000000000,-3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").addGeometry(Part.LineSegment(App.Vector(-23.97760000000000,-3.93700000000000,0.00000000000000),App.Vector(-23.97760000000000,3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").addGeometry(Part.LineSegment(App.Vector(23.97760000000000,3.93700000000000,0.00000000000000),App.Vector(-23.97760000000000,3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").addGeometry(Part.LineSegment(App.Vector(23.97760000000000,-3.93700000000000,0.00000000000000),App.Vector(23.97760000000000,3.93700000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FCByKGzRiQePJZk_0").newObject("PartDesign::Pocket","Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO")
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").Profile = App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO")
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").Length = 0.5080000000000001
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoTYjdqCXfcEden_1_JPO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").Type = 4
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoTYjdqCXfcEden_1_F9AIZVIcA7YpB0U_1_JPO").Offset = 0
App.ActiveDocument.recompute()

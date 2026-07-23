import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00910912")
App.ActiveDocument.addObject("PartDesign::Body","Body_FUlPN7KJizLNiKI_0")
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").Label = "Body_FUlPN7KJizLNiKI_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Plane", "plane_Sketch_FUlPN7KJizLNiKI_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUlPN7KJizLNiKI_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("Sketcher::SketchObject","Sketch_FUlPN7KJizLNiKI_0_JGC")
App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUlPN7KJizLNiKI_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC").addGeometry(Part.LineSegment(App.Vector(-116.26039000000000,86.07033000000000,0.00000000000000),App.Vector(109.73961000000000,86.07033000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC").addGeometry(Part.LineSegment(App.Vector(109.73961000000000,86.07033000000000,0.00000000000000),App.Vector(109.73961000000000,-83.92967000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC").addGeometry(Part.LineSegment(App.Vector(-116.26039000000000,-83.92967000000000,0.00000000000000),App.Vector(109.73961000000000,-83.92967000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC").addGeometry(Part.LineSegment(App.Vector(-116.26039000000000,86.07033000000000,0.00000000000000),App.Vector(-116.26039000000000,-83.92967000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Pad","Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC")
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC")
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").Length = 1.0
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUlPN7KJizLNiKI_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUlPN7KJizLNiKI_0_FTDuKMzvZ21e9xr_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Plane", "plane_Sketch_FbtYKGrJ15MWaDx_1_JJC")
origin = App.Vector(-3.26039000000000,1.07033000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbtYKGrJ15MWaDx_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("Sketcher::SketchObject","Sketch_FbtYKGrJ15MWaDx_1_JJC")
App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbtYKGrJ15MWaDx_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC").addGeometry(Part.LineSegment(App.Vector(-110.00000000000000,-84.99999999999999,0.00000000000000),App.Vector(39.00000000000000,-84.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC").addGeometry(Part.LineSegment(App.Vector(39.00000000000000,-84.99999999999999,0.00000000000000),App.Vector(39.00000000000000,-57.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC").addGeometry(Part.LineSegment(App.Vector(-110.00000000000000,-57.00000000000000,0.00000000000000),App.Vector(39.00000000000000,-57.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC").addGeometry(Part.LineSegment(App.Vector(-110.00000000000000,-84.99999999999999,0.00000000000000),App.Vector(-110.00000000000000,-57.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Pad","Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC")
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC")
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").Length = 35.0
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbtYKGrJ15MWaDx_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbtYKGrJ15MWaDx_1_FeilgCcyiTj5cch_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Plane", "plane_Sketch_FLqntjIsDzdLdM2_1_JNC")
origin = App.Vector(-3.26039000000000,1.07033000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("Sketcher::SketchObject","Sketch_FLqntjIsDzdLdM2_1_JNC")
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC").addGeometry(Part.LineSegment(App.Vector(-73.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-23.00000000000000,-25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC").addGeometry(Part.LineSegment(App.Vector(-23.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-23.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC").addGeometry(Part.LineSegment(App.Vector(-73.00000000000000,25.00000000000000,0.00000000000000),App.Vector(-23.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC").addGeometry(Part.LineSegment(App.Vector(-73.00000000000000,-25.00000000000000,0.00000000000000),App.Vector(-73.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Pad","Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").Length = 46.0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FMMd9mSyLeazZIH_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Plane", "plane_Sketch_FLqntjIsDzdLdM2_1_JNK")
origin = App.Vector(-3.26039000000000,1.07033000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("Sketcher::SketchObject","Sketch_FLqntjIsDzdLdM2_1_JNK")
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK").addGeometry(Part.LineSegment(App.Vector(-109.00000000000000,65.00000000000000,0.00000000000000),App.Vector(31.00000000000000,65.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK").addGeometry(Part.LineSegment(App.Vector(31.00000000000000,65.00000000000000,0.00000000000000),App.Vector(31.00000000000000,55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK").addGeometry(Part.LineSegment(App.Vector(-109.00000000000000,55.00000000000000,0.00000000000000),App.Vector(31.00000000000000,55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK").addGeometry(Part.LineSegment(App.Vector(-109.00000000000000,65.00000000000000,0.00000000000000),App.Vector(-109.00000000000000,55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Pad","Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").Length = 37.0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FGxlkBs2EqjPjwc_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Plane", "plane_Sketch_FLqntjIsDzdLdM2_1_JNG")
origin = App.Vector(-3.26039000000000,1.07033000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("Sketcher::SketchObject","Sketch_FLqntjIsDzdLdM2_1_JNG")
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG").addGeometry(Part.LineSegment(App.Vector(-109.00000000000000,44.00000000000000,0.00000000000000),App.Vector(31.00000000000000,44.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG").addGeometry(Part.LineSegment(App.Vector(31.00000000000000,44.00000000000000,0.00000000000000),App.Vector(31.00000000000000,54.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG").addGeometry(Part.LineSegment(App.Vector(-109.00000000000000,54.00000000000000,0.00000000000000),App.Vector(31.00000000000000,54.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG").addGeometry(Part.LineSegment(App.Vector(-109.00000000000000,44.00000000000000,0.00000000000000),App.Vector(-109.00000000000000,54.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Pad","Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").Length = 15.0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Plane", "plane_Sketch_FLqntjIsDzdLdM2_1_JNW")
origin = App.Vector(-3.26039000000000,1.07033000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("Sketcher::SketchObject","Sketch_FLqntjIsDzdLdM2_1_JNW")
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,25.00000000000000,0.00000000000000),App.Vector(6.00000000000000,25.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW").addGeometry(Part.LineSegment(App.Vector(6.00000000000000,25.00000000000000,0.00000000000000),App.Vector(6.00000000000000,7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,7.00000000000000,0.00000000000000),App.Vector(6.00000000000000,7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW").addGeometry(Part.LineSegment(App.Vector(24.00000000000000,25.00000000000000,0.00000000000000),App.Vector(24.00000000000000,7.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Pad","Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").Length = 15.0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FdPYvB0umUwHcE6_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Plane", "plane_Sketch_FLqntjIsDzdLdM2_1_JNS")
origin = App.Vector(-3.26039000000000,1.07033000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("Sketcher::SketchObject","Sketch_FLqntjIsDzdLdM2_1_JNS")
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,81.00000000000000,0.00000000000000),App.Vector(-11.00000000000000,81.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS").addGeometry(Part.LineSegment(App.Vector(-11.00000000000000,81.00000000000000,0.00000000000000),App.Vector(-11.00000000000000,71.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,71.00000000000001,0.00000000000000),App.Vector(-11.00000000000000,71.00000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,81.00000000000000,0.00000000000000),App.Vector(40.00000000000000,71.00000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Pad","Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").Length = 10.0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FEoHGckSxr4Azn4_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Plane", "plane_Sketch_FLqntjIsDzdLdM2_1_JNO")
origin = App.Vector(-3.26039000000000,1.07033000000000,1.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("Sketcher::SketchObject","Sketch_FLqntjIsDzdLdM2_1_JNO")
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLqntjIsDzdLdM2_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO").addGeometry(Part.LineSegment(App.Vector(46.00000000000000,-43.00000000000000,0.00000000000000),App.Vector(54.00000000000000,-43.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO").addGeometry(Part.LineSegment(App.Vector(54.00000000000000,-43.00000000000000,0.00000000000000),App.Vector(54.00000000000000,47.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO").addGeometry(Part.LineSegment(App.Vector(46.00000000000000,47.00000000000000,0.00000000000000),App.Vector(54.00000000000000,47.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO").addGeometry(Part.LineSegment(App.Vector(46.00000000000000,-43.00000000000000,0.00000000000000),App.Vector(46.00000000000000,47.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FUlPN7KJizLNiKI_0").newObject("PartDesign::Pad","Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO")
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").Length = 16.5
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLqntjIsDzdLdM2_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLqntjIsDzdLdM2_1_FUznMZulmONsO5a_1_JNO").Offset = 0
App.ActiveDocument.recompute()

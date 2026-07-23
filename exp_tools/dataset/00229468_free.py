import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00229468")
App.ActiveDocument.addObject("PartDesign::Body","Body_FcEDTwqSRvwRu40_0")
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").Label = "Body_FcEDTwqSRvwRu40_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Plane", "plane_Sketch_FcEDTwqSRvwRu40_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FcEDTwqSRvwRu40_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("Sketcher::SketchObject","Sketch_FcEDTwqSRvwRu40_0_JGC")
App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FcEDTwqSRvwRu40_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1457.62791999999990,718.76671999999996,0.00000000000000),App.Vector(1437.97208000000001,718.76671999999996,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC").addGeometry(Part.LineSegment(App.Vector(1437.97208000000001,718.76671999999996,0.00000000000000),App.Vector(1437.97208000000001,-906.83327999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1457.62791999999990,-906.83327999999995,0.00000000000000),App.Vector(1437.97208000000001,-906.83327999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC").addGeometry(Part.LineSegment(App.Vector(-1457.62791999999990,718.76671999999996,0.00000000000000),App.Vector(-1457.62791999999990,-906.83327999999995,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Pad","Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC")
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC")
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").Length = 914.4000000000001
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FcEDTwqSRvwRu40_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FcEDTwqSRvwRu40_0_F9Q7biUW1xhBMFL_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Plane", "plane_Sketch_FIxJTvMCV8SJ2Ww_0_JJC")
origin = App.Vector(-9.82792000000000,-94.03327999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIxJTvMCV8SJ2Ww_0_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("Sketcher::SketchObject","Sketch_FIxJTvMCV8SJ2Ww_0_JJC")
App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIxJTvMCV8SJ2Ww_0_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").addGeometry(Part.LineSegment(App.Vector(1450.10022999999978,-815.74714999999992,0.00000000000000),App.Vector(2.30023000000000,-815.74714999999992,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").addGeometry(Part.LineSegment(App.Vector(2.30023000000000,-815.74714999999992,0.00000000000000),App.Vector(2.30023000000000,-812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").addGeometry(Part.LineSegment(App.Vector(1447.79999999999995,-812.79999999999995,0.00000000000000),App.Vector(2.30023000000000,-812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").addGeometry(Part.LineSegment(App.Vector(1447.79999999999995,-812.79999999999995,0.00000000000000),App.Vector(1447.79999999999995,-409.34715000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").addGeometry(Part.LineSegment(App.Vector(1450.10022999999978,-409.34715000000000,0.00000000000000),App.Vector(1447.79999999999995,-409.34715000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").addGeometry(Part.LineSegment(App.Vector(1450.10022999999978,-815.74714999999992,0.00000000000000),App.Vector(1450.10022999999978,-409.34715000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Pocket","Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC")
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC")
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").Length = 254.0
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Plane", "plane_Sketch_FIxJTvMCV8SJ2Ww_0_JJK")
origin = App.Vector(-9.82792000000000,-94.03327999999999,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIxJTvMCV8SJ2Ww_0_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("Sketcher::SketchObject","Sketch_FIxJTvMCV8SJ2Ww_0_JJK")
App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIxJTvMCV8SJ2Ww_0_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK").addGeometry(Part.LineSegment(App.Vector(2.30023000000000,-409.34715000000000,0.00000000000000),App.Vector(1447.79999999999995,-409.34715000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK").addGeometry(Part.LineSegment(App.Vector(1447.79999999999995,-812.79999999999995,0.00000000000000),App.Vector(1447.79999999999995,-409.34715000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK").addGeometry(Part.LineSegment(App.Vector(1447.79999999999995,-812.79999999999995,0.00000000000000),App.Vector(2.30023000000000,-812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK").addGeometry(Part.LineSegment(App.Vector(2.30023000000000,-409.34715000000000,0.00000000000000),App.Vector(2.30023000000000,-812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Pocket","Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK")
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK")
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").Length = 254.0
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIxJTvMCV8SJ2Ww_0_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIxJTvMCV8SJ2Ww_0_F1Hc7R7og8rAcQl_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Plane", "plane_Sketch_F3hzuz5l0uw9Qxd_0_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3hzuz5l0uw9Qxd_0_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("Sketcher::SketchObject","Sketch_F3hzuz5l0uw9Qxd_0_JNC")
App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3hzuz5l0uw9Qxd_0_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC").addGeometry(Part.LineSegment(App.Vector(-7.72852000000000,-909.52566999999999,0.00000000000000),App.Vector(-7.72852000000000,720.65490000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC").addGeometry(Part.LineSegment(App.Vector(-7.72852000000000,720.65490000000000,0.00000000000000),App.Vector(1452.22699999999986,720.65490000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC").addGeometry(Part.LineSegment(App.Vector(1452.22699999999986,720.65490000000000,0.00000000000000),App.Vector(1452.22699999999986,-902.33611999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC").addGeometry(Part.LineSegment(App.Vector(-7.72852000000000,-909.52566999999999,0.00000000000000),App.Vector(1452.22699999999986,-902.33611999999994,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Pocket","Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC")
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").Profile = App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC")
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").Length = 254.0
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3hzuz5l0uw9Qxd_0_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3hzuz5l0uw9Qxd_0_FZc8y0y6Knb81Lk_0_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Plane", "plane_Sketch_FV6f34Iy8mHEI85_1_JRC")
origin = App.Vector(193.37208000000001,-94.03327999999999,914.39999999999998)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FV6f34Iy8mHEI85_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("Sketcher::SketchObject","Sketch_FV6f34Iy8mHEI85_1_JRC")
App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FV6f34Iy8mHEI85_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC").addGeometry(Part.LineSegment(App.Vector(1244.59999999999991,-406.39999999999998,0.00000000000000),App.Vector(838.19999999999982,-406.39999999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC").addGeometry(Part.LineSegment(App.Vector(838.19999999999982,-406.39999999999998,0.00000000000000),App.Vector(838.19999999999982,-812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC").addGeometry(Part.LineSegment(App.Vector(1244.59999999999991,-812.79999999999995,0.00000000000000),App.Vector(838.19999999999982,-812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC").addGeometry(Part.LineSegment(App.Vector(1244.59999999999991,-812.79999999999995,0.00000000000000),App.Vector(1244.59999999999991,-406.39999999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Pad","Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC")
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC")
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").Length = 558.8000000000001
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FV6f34Iy8mHEI85_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FV6f34Iy8mHEI85_1_FEUZGDEfuY5yU2L_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Plane", "plane_Sketch_Fuf4pAwqDcB1lgh_1_JVC")
origin = App.Vector(193.37208000000001,-94.03327999999999,914.39999999999998)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fuf4pAwqDcB1lgh_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("Sketcher::SketchObject","Sketch_Fuf4pAwqDcB1lgh_1_JVC")
App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fuf4pAwqDcB1lgh_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC").addGeometry(Part.LineSegment(App.Vector(1244.59999999999991,812.79999999999995,0.00000000000000),App.Vector(819.91534999999999,812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC").addGeometry(Part.LineSegment(App.Vector(819.91534999999999,812.79999999999995,0.00000000000000),App.Vector(819.91534999999999,403.02044999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC").addGeometry(Part.LineSegment(App.Vector(1244.59999999999991,403.02044999999998,0.00000000000000),App.Vector(819.91534999999999,403.02044999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC").addGeometry(Part.LineSegment(App.Vector(1244.59999999999991,812.79999999999995,0.00000000000000),App.Vector(1244.59999999999991,403.02044999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Pad","Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC")
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC")
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").Length = 558.8000000000001
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fuf4pAwqDcB1lgh_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fuf4pAwqDcB1lgh_1_F6hyFBJtev0SvYJ_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Plane", "plane_Sketch_Fl6PMeWUnlpvFAl_1_JZC")
origin = App.Vector(193.37208000000001,-94.03327999999999,914.39999999999998)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fl6PMeWUnlpvFAl_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("Sketcher::SketchObject","Sketch_Fl6PMeWUnlpvFAl_1_JZC")
App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fl6PMeWUnlpvFAl_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC").addGeometry(Part.LineSegment(App.Vector(-1651.00000000000000,812.79999999999995,0.00000000000000),App.Vector(-1244.60000000000014,812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC").addGeometry(Part.LineSegment(App.Vector(-1244.60000000000014,812.79999999999995,0.00000000000000),App.Vector(-1244.60000000000014,-812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC").addGeometry(Part.LineSegment(App.Vector(-1651.00000000000000,-812.79999999999995,0.00000000000000),App.Vector(-1244.60000000000014,-812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC").addGeometry(Part.LineSegment(App.Vector(-1651.00000000000000,812.79999999999995,0.00000000000000),App.Vector(-1651.00000000000000,-812.79999999999995,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Pad","Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC")
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC")
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").Length = 279.40000000000003
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fl6PMeWUnlpvFAl_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fl6PMeWUnlpvFAl_1_FDtfuN0AFfdnxLU_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Plane", "plane_Sketch_FZHFdHezqSfCvJw_1_JdC")
origin = App.Vector(193.37208000000001,-94.03327999999999,914.39999999999998)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZHFdHezqSfCvJw_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("Sketcher::SketchObject","Sketch_FZHFdHezqSfCvJw_1_JdC")
App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZHFdHezqSfCvJw_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdC").addGeometry(Part.Circle(App.Vector(-683.16814999999997,79.63547000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),254.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Pocket","Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC")
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdC")
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").Length = 706.12
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Plane", "plane_Sketch_FZHFdHezqSfCvJw_1_JdG")
origin = App.Vector(193.37208000000001,-94.03327999999999,914.39999999999998)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZHFdHezqSfCvJw_1_JdG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("Sketcher::SketchObject","Sketch_FZHFdHezqSfCvJw_1_JdG")
App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZHFdHezqSfCvJw_1_JdG"), [""])
App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdG").addGeometry(Part.Circle(App.Vector(190.33133000000001,67.98881000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),254.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FcEDTwqSRvwRu40_0").newObject("PartDesign::Pocket","Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG")
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").Profile = App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdG")
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").Length = 706.12
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZHFdHezqSfCvJw_1_JdG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").Type = 4
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZHFdHezqSfCvJw_1_FCB0SA41fqA2mwZ_1_JdG").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00483394")
App.ActiveDocument.addObject("PartDesign::Body","Body_FLDxRNLXHD49UpI_0")
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").Label = "Body_FLDxRNLXHD49UpI_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Plane", "plane_Sketch_FLDxRNLXHD49UpI_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLDxRNLXHD49UpI_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("Sketcher::SketchObject","Sketch_FLDxRNLXHD49UpI_0_JGC")
App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLDxRNLXHD49UpI_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(695.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC").addGeometry(Part.LineSegment(App.Vector(695.00000000000000,0.00000000000000,0.00000000000000),App.Vector(695.00000000000000,1945.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,1945.00000000000000,0.00000000000000),App.Vector(695.00000000000000,1945.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,1945.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Pad","Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC")
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC")
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLDxRNLXHD49UpI_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLDxRNLXHD49UpI_0_F3XXwk7qyURParP_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Plane", "plane_Sketch_FjEmWIdS8Afzemb_1_JJC")
origin = App.Vector(294.93288999999999,0.00000000000000,1526.07761000000005)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjEmWIdS8Afzemb_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("Sketcher::SketchObject","Sketch_FjEmWIdS8Afzemb_1_JJC")
App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjEmWIdS8Afzemb_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").addGeometry(Part.LineSegment(App.Vector(294.93288999999999,418.92239000000006,0.00000000000000),App.Vector(-400.06710999999996,418.92239000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").addGeometry(Part.LineSegment(App.Vector(-400.06710999999996,-1526.07761000000005,0.00000000000000),App.Vector(-400.06710999999996,418.92239000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").addGeometry(Part.LineSegment(App.Vector(294.93288999999999,-1526.07761000000005,0.00000000000000),App.Vector(-400.06710999999996,-1526.07761000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").addGeometry(Part.LineSegment(App.Vector(294.93288999999999,-1526.07761000000005,0.00000000000000),App.Vector(294.93288999999999,418.92239000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").addGeometry(Part.LineSegment(App.Vector(250.93289000000001,374.92239000000006,0.00000000000000),App.Vector(-356.06711000000001,374.92239000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").addGeometry(Part.LineSegment(App.Vector(-356.06711000000001,374.92239000000006,0.00000000000000),App.Vector(-356.06711000000001,-1482.07760999999982,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").addGeometry(Part.LineSegment(App.Vector(250.93289000000001,-1482.07760999999982,0.00000000000000),App.Vector(-356.06711000000001,-1482.07760999999982,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").addGeometry(Part.LineSegment(App.Vector(250.93289000000001,374.92239000000006,0.00000000000000),App.Vector(250.93289000000001,-1482.07760999999982,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Pad","Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC")
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC")
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").Length = 58.0
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjEmWIdS8Afzemb_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjEmWIdS8Afzemb_1_FqVtoZcr1CJxslq_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Plane", "plane_Sketch_FJ1vq6zF99SC1ek_1_JNC")
origin = App.Vector(294.93288999999999,0.00000000000000,1526.07761000000005)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ1vq6zF99SC1ek_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("Sketcher::SketchObject","Sketch_FJ1vq6zF99SC1ek_1_JNC")
App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ1vq6zF99SC1ek_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").addGeometry(Part.LineSegment(App.Vector(250.93289000000001,-478.57760999999988,0.00000000000000),App.Vector(142.80544000000000,-478.57760999999988,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").addGeometry(Part.LineSegment(App.Vector(142.80544000000000,-478.57760999999988,0.00000000000000),App.Vector(-356.06711000000001,266.79494000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").addGeometry(Part.LineSegment(App.Vector(-356.06711000000001,374.92239000000006,0.00000000000000),App.Vector(-356.06711000000001,266.79494000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").addGeometry(Part.LineSegment(App.Vector(-356.06711000000001,374.92239000000006,0.00000000000000),App.Vector(-247.93966000000000,374.92239000000006,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").addGeometry(Part.LineSegment(App.Vector(-247.93966000000000,374.92239000000006,0.00000000000000),App.Vector(250.93289000000001,-370.45016000000010,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").addGeometry(Part.LineSegment(App.Vector(250.93289000000001,-478.57760999999988,0.00000000000000),App.Vector(250.93289000000001,-370.45016000000010,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Pad","Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC")
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC")
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Plane", "plane_Sketch_FJ1vq6zF99SC1ek_1_JNK")
origin = App.Vector(294.93288999999999,0.00000000000000,1526.07761000000005)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ1vq6zF99SC1ek_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("Sketcher::SketchObject","Sketch_FJ1vq6zF99SC1ek_1_JNK")
App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ1vq6zF99SC1ek_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").addGeometry(Part.LineSegment(App.Vector(-247.93966000000000,-628.57761000000005,0.00000000000000),App.Vector(250.93289000000001,-628.57761000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").addGeometry(Part.LineSegment(App.Vector(250.93289000000001,-628.57761000000005,0.00000000000000),App.Vector(250.93289000000001,-478.57760999999988,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").addGeometry(Part.LineSegment(App.Vector(250.93289000000001,-478.57760999999988,0.00000000000000),App.Vector(142.80544000000000,-478.57760999999988,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").addGeometry(Part.LineSegment(App.Vector(-356.06711000000001,-478.57760999999988,0.00000000000000),App.Vector(142.80544000000000,-478.57760999999988,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").addGeometry(Part.LineSegment(App.Vector(-356.06711000000001,-478.57760999999988,0.00000000000000),App.Vector(-356.06711000000001,-628.57761000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").addGeometry(Part.LineSegment(App.Vector(-247.93966000000000,-628.57761000000005,0.00000000000000),App.Vector(-356.06711000000001,-628.57761000000005,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Pad","Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK")
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK")
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").Length = 25.0
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Plane", "plane_Sketch_FJ1vq6zF99SC1ek_1_JNG")
origin = App.Vector(294.93288999999999,0.00000000000000,1526.07761000000005)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJ1vq6zF99SC1ek_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("Sketcher::SketchObject","Sketch_FJ1vq6zF99SC1ek_1_JNG")
App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJ1vq6zF99SC1ek_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").addGeometry(Part.LineSegment(App.Vector(-356.06711000000001,-736.70506000000000,0.00000000000000),App.Vector(142.80544000000000,-1482.07760999999982,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").addGeometry(Part.LineSegment(App.Vector(250.93289000000001,-1482.07760999999982,0.00000000000000),App.Vector(142.80544000000000,-1482.07760999999982,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").addGeometry(Part.LineSegment(App.Vector(250.93289000000001,-1482.07760999999982,0.00000000000000),App.Vector(250.93289000000001,-1373.95015999999987,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").addGeometry(Part.LineSegment(App.Vector(-247.93966000000000,-628.57761000000005,0.00000000000000),App.Vector(250.93289000000001,-1373.95015999999987,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").addGeometry(Part.LineSegment(App.Vector(-247.93966000000000,-628.57761000000005,0.00000000000000),App.Vector(-356.06711000000001,-628.57761000000005,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").addGeometry(Part.LineSegment(App.Vector(-356.06711000000001,-628.57761000000005,0.00000000000000),App.Vector(-356.06711000000001,-736.70506000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Pad","Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG")
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG")
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJ1vq6zF99SC1ek_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJ1vq6zF99SC1ek_1_FzFE5V81qvyS47n_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Plane", "plane_Sketch_F0Z2lAnh2VaayHc_1_JRC")
origin = App.Vector(0.00000000000000,23.00000000000000,972.50000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0Z2lAnh2VaayHc_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("Sketcher::SketchObject","Sketch_F0Z2lAnh2VaayHc_1_JRC")
App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0Z2lAnh2VaayHc_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-822.50000000000000,0.00000000000000),App.Vector(1.00000000000000,-822.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,-822.50000000000000,0.00000000000000),App.Vector(1.00000000000000,-747.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-747.50000000000000,0.00000000000000),App.Vector(1.00000000000000,-747.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-822.50000000000000,0.00000000000000),App.Vector(35.00000000000000,-747.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Pocket","Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC")
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC")
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").Length = 2.5
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Plane", "plane_Sketch_F0Z2lAnh2VaayHc_1_JRG")
origin = App.Vector(0.00000000000000,23.00000000000000,972.50000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0Z2lAnh2VaayHc_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("Sketcher::SketchObject","Sketch_F0Z2lAnh2VaayHc_1_JRG")
App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0Z2lAnh2VaayHc_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-22.50000000000007,0.00000000000000),App.Vector(1.00000000000000,-22.50000000000007,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,-22.50000000000007,0.00000000000000),App.Vector(1.00000000000000,52.49999999999988,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,52.49999999999988,0.00000000000000),App.Vector(1.00000000000000,52.49999999999988,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,-22.50000000000007,0.00000000000000),App.Vector(35.00000000000000,52.49999999999988,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Pocket","Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG")
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG")
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").Length = 2.5
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Plane", "plane_Sketch_F0Z2lAnh2VaayHc_1_JRK")
origin = App.Vector(0.00000000000000,23.00000000000000,972.50000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0Z2lAnh2VaayHc_1_JRK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("Sketcher::SketchObject","Sketch_F0Z2lAnh2VaayHc_1_JRK")
App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0Z2lAnh2VaayHc_1_JRK"), [""])
App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,777.50000000000000,0.00000000000000),App.Vector(1.00000000000000,777.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK").addGeometry(Part.LineSegment(App.Vector(1.00000000000000,777.50000000000000,0.00000000000000),App.Vector(1.00000000000000,852.49999999999989,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,852.49999999999989,0.00000000000000),App.Vector(1.00000000000000,852.49999999999989,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,777.50000000000000,0.00000000000000),App.Vector(35.00000000000000,852.49999999999989,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FLDxRNLXHD49UpI_0").newObject("PartDesign::Pocket","Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK")
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").Profile = App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK")
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").Length = 2.5
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0Z2lAnh2VaayHc_1_JRK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").Type = 4
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0Z2lAnh2VaayHc_1_F5wIyp09USOVbju_1_JRK").Offset = 0
App.ActiveDocument.recompute()

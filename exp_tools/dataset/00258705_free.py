import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00258705")
App.ActiveDocument.addObject("PartDesign::Body","Body_F56njblnbbUZcZU_0")
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").Label = "Body_F56njblnbbUZcZU_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Plane", "plane_Sketch_F56njblnbbUZcZU_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F56njblnbbUZcZU_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("Sketcher::SketchObject","Sketch_F56njblnbbUZcZU_0_JGC")
App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F56njblnbbUZcZU_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-72.29199000000000,71.52019000000000,0.00000000000000),App.Vector(71.77746000000000,71.52019000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC").addGeometry(Part.LineSegment(App.Vector(71.77746000000000,71.52019000000000,0.00000000000000),App.Vector(71.77746000000000,-72.29199000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-72.29199000000000,-72.29199000000000,0.00000000000000),App.Vector(71.77746000000000,-72.29199000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC").addGeometry(Part.LineSegment(App.Vector(-72.29199000000000,71.52019000000000,0.00000000000000),App.Vector(-72.29199000000000,-72.29199000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Pad","Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC")
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC")
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").Length = 162.56
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F56njblnbbUZcZU_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F56njblnbbUZcZU_0_F5UacUjY5CW7iTV_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Plane", "plane_Sketch_FelthBK49wS5rJM_1_JJG")
origin = App.Vector(-0.25726000000000,-162.56000000000000,-0.38590000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FelthBK49wS5rJM_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("Sketcher::SketchObject","Sketch_FelthBK49wS5rJM_1_JJG")
App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FelthBK49wS5rJM_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG").addGeometry(Part.LineSegment(App.Vector(44.50716000000001,-5.27397000000000,0.00000000000000),App.Vector(13.37787000000000,-5.27397000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG").addGeometry(Part.LineSegment(App.Vector(13.37787000000000,-5.27397000000000,0.00000000000000),App.Vector(13.37787000000000,-32.02973000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG").addGeometry(Part.LineSegment(App.Vector(44.50716000000001,-32.02973000000000,0.00000000000000),App.Vector(13.37787000000000,-32.02973000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG").addGeometry(Part.LineSegment(App.Vector(44.50716000000001,-5.27397000000000,0.00000000000000),App.Vector(44.50716000000001,-32.02973000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Pad","Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG")
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG")
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Plane", "plane_Sketch_FelthBK49wS5rJM_1_JJC")
origin = App.Vector(-0.25726000000000,-162.56000000000000,-0.38590000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FelthBK49wS5rJM_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("Sketcher::SketchObject","Sketch_FelthBK49wS5rJM_1_JJC")
App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FelthBK49wS5rJM_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC").addGeometry(Part.LineSegment(App.Vector(-56.85599000000000,-71.90609000000001,0.00000000000000),App.Vector(-24.44036000000000,-71.90609000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC").addGeometry(Part.LineSegment(App.Vector(-24.44036000000000,-71.90609000000001,0.00000000000000),App.Vector(-24.44036000000000,-5.27397000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC").addGeometry(Part.LineSegment(App.Vector(-56.85599000000000,-5.27397000000000,0.00000000000000),App.Vector(-24.44036000000000,-5.27397000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC").addGeometry(Part.LineSegment(App.Vector(-56.85599000000000,-71.90609000000001,0.00000000000000),App.Vector(-56.85599000000000,-5.27397000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Pad","Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC")
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC")
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FelthBK49wS5rJM_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FelthBK49wS5rJM_1_F2YEPzlAkISEOml_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Plane", "plane_Sketch_F7t8hiwZ7a8MsPv_1_JLC")
origin = App.Vector(-40.90543000000000,-162.56000000000000,-38.97593000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("Sketcher::SketchObject","Sketch_F7t8hiwZ7a8MsPv_1_JLC")
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLC").addGeometry(Part.Circle(App.Vector(9.96548000000000,-3.19381000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.94824000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Pad","Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLC")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Plane", "plane_Sketch_F7t8hiwZ7a8MsPv_1_JLG")
origin = App.Vector(-40.90543000000000,-162.56000000000000,-38.97593000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("Sketcher::SketchObject","Sketch_F7t8hiwZ7a8MsPv_1_JLG")
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG").addGeometry(Part.LineSegment(App.Vector(-9.65918000000000,26.51575000000000,0.00000000000000),App.Vector(0.69828000000000,26.51575000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG").addGeometry(Part.LineSegment(App.Vector(0.69828000000000,26.51575000000000,0.00000000000000),App.Vector(0.69828000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG").addGeometry(Part.LineSegment(App.Vector(-9.65918000000000,17.79368000000000,0.00000000000000),App.Vector(0.69828000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG").addGeometry(Part.LineSegment(App.Vector(-9.65918000000000,26.51575000000000,0.00000000000000),App.Vector(-9.65918000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Pad","Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Plane", "plane_Sketch_F7t8hiwZ7a8MsPv_1_JLK")
origin = App.Vector(-40.90543000000000,-162.56000000000000,-38.97593000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("Sketcher::SketchObject","Sketch_F7t8hiwZ7a8MsPv_1_JLK")
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK").addGeometry(Part.LineSegment(App.Vector(11.05574000000000,26.51575000000000,0.00000000000000),App.Vector(0.69828000000000,26.51575000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK").addGeometry(Part.LineSegment(App.Vector(0.69828000000000,26.51575000000000,0.00000000000000),App.Vector(0.69828000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK").addGeometry(Part.LineSegment(App.Vector(11.05574000000000,17.79368000000000,0.00000000000000),App.Vector(0.69828000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK").addGeometry(Part.LineSegment(App.Vector(11.05574000000000,26.51575000000000,0.00000000000000),App.Vector(11.05574000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Pad","Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").Type = 4
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Plane", "plane_Sketch_F7t8hiwZ7a8MsPv_1_JLO")
origin = App.Vector(-40.90543000000000,-162.56000000000000,-38.97593000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("Sketcher::SketchObject","Sketch_F7t8hiwZ7a8MsPv_1_JLO")
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLO"), [""])
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO").addGeometry(Part.LineSegment(App.Vector(-9.65918000000000,9.07161000000000,0.00000000000000),App.Vector(0.69828000000000,9.07161000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO").addGeometry(Part.LineSegment(App.Vector(0.69828000000000,9.07161000000000,0.00000000000000),App.Vector(0.69828000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO").addGeometry(Part.LineSegment(App.Vector(-9.65918000000000,17.79368000000000,0.00000000000000),App.Vector(0.69828000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO").addGeometry(Part.LineSegment(App.Vector(-9.65918000000000,9.07161000000000,0.00000000000000),App.Vector(-9.65918000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Pad","Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").Profile = App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").Type = 4
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Plane", "plane_Sketch_F7t8hiwZ7a8MsPv_1_JLS")
origin = App.Vector(-40.90543000000000,-162.56000000000000,-38.97593000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("Sketcher::SketchObject","Sketch_F7t8hiwZ7a8MsPv_1_JLS")
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7t8hiwZ7a8MsPv_1_JLS"), [""])
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS").addGeometry(Part.LineSegment(App.Vector(11.05574000000000,9.07161000000000,0.00000000000000),App.Vector(0.69828000000000,9.07161000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS").addGeometry(Part.LineSegment(App.Vector(0.69828000000000,9.07161000000000,0.00000000000000),App.Vector(0.69828000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS").addGeometry(Part.LineSegment(App.Vector(11.05574000000000,17.79368000000000,0.00000000000000),App.Vector(0.69828000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS").addGeometry(Part.LineSegment(App.Vector(11.05574000000000,9.07161000000000,0.00000000000000),App.Vector(11.05574000000000,17.79368000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F56njblnbbUZcZU_0").newObject("PartDesign::Pad","Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").Profile = App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS")
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").Length = 0.6350000000000001
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7t8hiwZ7a8MsPv_1_JLS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").Type = 4
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7t8hiwZ7a8MsPv_1_F30cPVZObuDLGNs_1_JLS").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00352037")
App.ActiveDocument.addObject("PartDesign::Body","Body_FthjYnLOgOlIIbI_0")
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").Label = "Body_FthjYnLOgOlIIbI_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Plane", "plane_Sketch_FthjYnLOgOlIIbI_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FthjYnLOgOlIIbI_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("Sketcher::SketchObject","Sketch_FthjYnLOgOlIIbI_0_JGC")
App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FthjYnLOgOlIIbI_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(115.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC").addGeometry(Part.LineSegment(App.Vector(115.00000000000000,0.00000000000000,0.00000000000000),App.Vector(115.00000000000000,88.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,88.00000000000000,0.00000000000000),App.Vector(115.00000000000000,88.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,88.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Pad","Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC")
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC")
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").Length = 45.0
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FthjYnLOgOlIIbI_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FthjYnLOgOlIIbI_0_FTW66fZAiOmTFcG_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Plane", "plane_Sketch_FK9sWncthsHM30N_1_JJG")
origin = App.Vector(57.50000000000000,-45.00000000000000,44.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FK9sWncthsHM30N_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("Sketcher::SketchObject","Sketch_FK9sWncthsHM30N_1_JJG")
App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FK9sWncthsHM30N_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG").addGeometry(Part.LineSegment(App.Vector(57.50000000000000,44.00000000000000,0.00000000000000),App.Vector(-47.50000000000000,44.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG").addGeometry(Part.LineSegment(App.Vector(-47.50000000000000,44.00000000000000,0.00000000000000),App.Vector(-47.50000000000000,-33.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG").addGeometry(Part.LineSegment(App.Vector(57.50000000000000,-33.99999999999999,0.00000000000000),App.Vector(-47.50000000000000,-33.99999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG").addGeometry(Part.LineSegment(App.Vector(57.50000000000000,44.00000000000000,0.00000000000000),App.Vector(57.50000000000000,-33.99999999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Pocket","Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG")
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG")
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").Length = 133.5
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FK9sWncthsHM30N_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FK9sWncthsHM30N_1_FFbv0iKrsc6jCKc_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Plane", "plane_Sketch_FCUhVmGufK4DpYJ_1_JNC")
origin = App.Vector(62.50000000000000,-22.50000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCUhVmGufK4DpYJ_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("Sketcher::SketchObject","Sketch_FCUhVmGufK4DpYJ_1_JNC")
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCUhVmGufK4DpYJ_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,9.75000000000000,0.00000000000000),App.Vector(0.00000000000000,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,9.75000000000000,0.00000000000000),App.Vector(-19.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Pad","Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC")
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC")
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").Length = 12.0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Plane", "plane_Sketch_FCUhVmGufK4DpYJ_1_JNG")
origin = App.Vector(62.50000000000000,-22.50000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCUhVmGufK4DpYJ_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("Sketcher::SketchObject","Sketch_FCUhVmGufK4DpYJ_1_JNG")
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCUhVmGufK4DpYJ_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,-9.75000000000000,0.00000000000000),App.Vector(0.00000000000000,-9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,-9.75000000000000,0.00000000000000),App.Vector(-19.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Pad","Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG")
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG")
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").Length = 12.0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Plane", "plane_Sketch_FCUhVmGufK4DpYJ_1_JNO")
origin = App.Vector(62.50000000000000,-22.50000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCUhVmGufK4DpYJ_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("Sketcher::SketchObject","Sketch_FCUhVmGufK4DpYJ_1_JNO")
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCUhVmGufK4DpYJ_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(19.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,-9.75000000000000,0.00000000000000),App.Vector(19.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,-9.75000000000000,0.00000000000000),App.Vector(0.00000000000000,-9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Pad","Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO")
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO")
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").Length = 12.0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Plane", "plane_Sketch_FCUhVmGufK4DpYJ_1_JNK")
origin = App.Vector(62.50000000000000,-22.50000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FCUhVmGufK4DpYJ_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("Sketcher::SketchObject","Sketch_FCUhVmGufK4DpYJ_1_JNK")
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FCUhVmGufK4DpYJ_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(19.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,9.75000000000000,0.00000000000000),App.Vector(19.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,9.75000000000000,0.00000000000000),App.Vector(0.00000000000000,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Pad","Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK")
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK")
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").Length = 12.0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FCUhVmGufK4DpYJ_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FCUhVmGufK4DpYJ_1_F3dwwOK7zmhX9Q2_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Plane", "plane_Sketch_FPG4ugjqYgJAxxt_1_JRC")
origin = App.Vector(62.50000000000000,-22.50000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPG4ugjqYgJAxxt_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("Sketcher::SketchObject","Sketch_FPG4ugjqYgJAxxt_1_JRC")
App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPG4ugjqYgJAxxt_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,9.75000000000000,0.00000000000000),App.Vector(-24.00000000000000,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC").addGeometry(Part.LineSegment(App.Vector(-24.00000000000000,9.75000000000000,0.00000000000000),App.Vector(-24.00000000000000,-9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,-9.75000000000000,0.00000000000000),App.Vector(-24.00000000000000,-9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC").addGeometry(Part.LineSegment(App.Vector(-19.00000000000000,-9.75000000000000,0.00000000000000),App.Vector(-19.00000000000000,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Pad","Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC")
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC")
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Plane", "plane_Sketch_FPG4ugjqYgJAxxt_1_JRG")
origin = App.Vector(62.50000000000000,-22.50000000000000,10.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPG4ugjqYgJAxxt_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("Sketcher::SketchObject","Sketch_FPG4ugjqYgJAxxt_1_JRG")
App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPG4ugjqYgJAxxt_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,9.75000000000000,0.00000000000000),App.Vector(23.99999999999999,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG").addGeometry(Part.LineSegment(App.Vector(23.99999999999999,9.75000000000000,0.00000000000000),App.Vector(23.99999999999999,-9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,-9.75000000000000,0.00000000000000),App.Vector(23.99999999999999,-9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG").addGeometry(Part.LineSegment(App.Vector(19.00000000000000,-9.75000000000000,0.00000000000000),App.Vector(19.00000000000000,9.75000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FthjYnLOgOlIIbI_0").newObject("PartDesign::Pad","Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG")
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG")
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").Length = 20.0
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPG4ugjqYgJAxxt_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPG4ugjqYgJAxxt_1_FfN1LQ7g8rMJKlk_1_JRG").Offset = 0
App.ActiveDocument.recompute()

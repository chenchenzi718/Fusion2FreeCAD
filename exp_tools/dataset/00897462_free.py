import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00897462")
App.ActiveDocument.addObject("PartDesign::Body","Body_Feb6s5ON00lVvWQ_0")
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").Label = "Body_Feb6s5ON00lVvWQ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Plane", "plane_Sketch_Feb6s5ON00lVvWQ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Feb6s5ON00lVvWQ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("Sketcher::SketchObject","Sketch_Feb6s5ON00lVvWQ_0_JGC")
App.ActiveDocument.getObject("Sketch_Feb6s5ON00lVvWQ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Feb6s5ON00lVvWQ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Feb6s5ON00lVvWQ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Feb6s5ON00lVvWQ_0_JGC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),40.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Feb6s5ON00lVvWQ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Feb6s5ON00lVvWQ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Pad","Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC")
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Feb6s5ON00lVvWQ_0_JGC")
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").Length = 20.0
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Feb6s5ON00lVvWQ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Feb6s5ON00lVvWQ_0_FSsfFDocnYyLTr4_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Plane", "plane_Sketch_FAC7r4UMXe8tKNl_1_JJC")
origin = App.Vector(0.00000000000000,-20.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FAC7r4UMXe8tKNl_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("Sketcher::SketchObject","Sketch_FAC7r4UMXe8tKNl_1_JJC")
App.ActiveDocument.getObject("Sketch_FAC7r4UMXe8tKNl_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FAC7r4UMXe8tKNl_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FAC7r4UMXe8tKNl_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FAC7r4UMXe8tKNl_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FAC7r4UMXe8tKNl_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FAC7r4UMXe8tKNl_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Pad","Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC")
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FAC7r4UMXe8tKNl_1_JJC")
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").Length = 40.0
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FAC7r4UMXe8tKNl_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FAC7r4UMXe8tKNl_1_FjQdHwCiYQWofRJ_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Plane", "plane_Sketch_FEhYa8gewby3dfG_1_JNC")
origin = App.Vector(0.00000000000000,-60.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEhYa8gewby3dfG_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("Sketcher::SketchObject","Sketch_FEhYa8gewby3dfG_1_JNC")
App.ActiveDocument.getObject("Sketch_FEhYa8gewby3dfG_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEhYa8gewby3dfG_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FEhYa8gewby3dfG_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEhYa8gewby3dfG_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),20.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEhYa8gewby3dfG_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEhYa8gewby3dfG_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Pocket","Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC")
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FEhYa8gewby3dfG_1_JNC")
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").Length = 40.0
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEhYa8gewby3dfG_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEhYa8gewby3dfG_1_FCOd3IUBvMxRtMu_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Plane", "plane_Sketch_FdHF9I5hvyksY4v_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdHF9I5hvyksY4v_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("Sketcher::SketchObject","Sketch_FdHF9I5hvyksY4v_1_JRC")
App.ActiveDocument.getObject("Sketch_FdHF9I5hvyksY4v_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdHF9I5hvyksY4v_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FdHF9I5hvyksY4v_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdHF9I5hvyksY4v_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),25.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdHF9I5hvyksY4v_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdHF9I5hvyksY4v_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Pad","Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC")
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FdHF9I5hvyksY4v_1_JRC")
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdHF9I5hvyksY4v_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdHF9I5hvyksY4v_1_F1eip8Abf3EbpKa_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Plane", "plane_Sketch_F29bwS9r4aW5yuQ_1_JVC")
origin = App.Vector(0.00000000000000,20.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F29bwS9r4aW5yuQ_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("Sketcher::SketchObject","Sketch_F29bwS9r4aW5yuQ_1_JVC")
App.ActiveDocument.getObject("Sketch_F29bwS9r4aW5yuQ_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F29bwS9r4aW5yuQ_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F29bwS9r4aW5yuQ_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F29bwS9r4aW5yuQ_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),20.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F29bwS9r4aW5yuQ_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F29bwS9r4aW5yuQ_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Pad","Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC")
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F29bwS9r4aW5yuQ_1_JVC")
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").Length = 20.0
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F29bwS9r4aW5yuQ_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F29bwS9r4aW5yuQ_1_FTJDhwsC0SyLOrf_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Plane", "plane_Sketch_FqIklXNwXuyP8h3_1_JZC")
origin = App.Vector(0.00000000000000,40.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqIklXNwXuyP8h3_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("Sketcher::SketchObject","Sketch_FqIklXNwXuyP8h3_1_JZC")
App.ActiveDocument.getObject("Sketch_FqIklXNwXuyP8h3_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqIklXNwXuyP8h3_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FqIklXNwXuyP8h3_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqIklXNwXuyP8h3_1_JZC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqIklXNwXuyP8h3_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqIklXNwXuyP8h3_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Pad","Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC")
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FqIklXNwXuyP8h3_1_JZC")
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqIklXNwXuyP8h3_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqIklXNwXuyP8h3_1_FWfuOrwJM6ZCCAo_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Plane", "plane_Sketch_Fhwvy2I5hHtKbbT_1_JdC")
origin = App.Vector(0.00000000000000,60.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fhwvy2I5hHtKbbT_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("Sketcher::SketchObject","Sketch_Fhwvy2I5hHtKbbT_1_JdC")
App.ActiveDocument.getObject("Sketch_Fhwvy2I5hHtKbbT_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fhwvy2I5hHtKbbT_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_Fhwvy2I5hHtKbbT_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fhwvy2I5hHtKbbT_1_JdC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),10.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fhwvy2I5hHtKbbT_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fhwvy2I5hHtKbbT_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Pad","Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC")
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_Fhwvy2I5hHtKbbT_1_JdC")
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").Length = 20.0
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fhwvy2I5hHtKbbT_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fhwvy2I5hHtKbbT_1_FOmd15Js6BNIQZx_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Plane", "plane_Sketch_FJLFLIo5PuXUXcx_1_JhC")
origin = App.Vector(0.00000000000000,80.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJLFLIo5PuXUXcx_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("Sketcher::SketchObject","Sketch_FJLFLIo5PuXUXcx_1_JhC")
App.ActiveDocument.getObject("Sketch_FJLFLIo5PuXUXcx_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJLFLIo5PuXUXcx_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_FJLFLIo5PuXUXcx_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJLFLIo5PuXUXcx_1_JhC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJLFLIo5PuXUXcx_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJLFLIo5PuXUXcx_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Pad","Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC")
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_FJLFLIo5PuXUXcx_1_JhC")
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJLFLIo5PuXUXcx_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJLFLIo5PuXUXcx_1_FyfkLdSscRRgHQz_1_JhC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Plane", "plane_Sketch_FhyseSiVMWWJUsK_1_JlC")
origin = App.Vector(0.00000000000000,100.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FhyseSiVMWWJUsK_1_JlC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("Sketcher::SketchObject","Sketch_FhyseSiVMWWJUsK_1_JlC")
App.ActiveDocument.getObject("Sketch_FhyseSiVMWWJUsK_1_JlC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FhyseSiVMWWJUsK_1_JlC"), [""])
App.ActiveDocument.getObject("Sketch_FhyseSiVMWWJUsK_1_JlC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FhyseSiVMWWJUsK_1_JlC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FhyseSiVMWWJUsK_1_JlC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FhyseSiVMWWJUsK_1_JlC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Feb6s5ON00lVvWQ_0").newObject("PartDesign::Pad","Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC")
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").Profile = App.ActiveDocument.getObject("Sketch_FhyseSiVMWWJUsK_1_JlC")
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FhyseSiVMWWJUsK_1_JlC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").Type = 4
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FhyseSiVMWWJUsK_1_FrkQa2Dwdvb7axX_1_JlC").Offset = 0
App.ActiveDocument.recompute()

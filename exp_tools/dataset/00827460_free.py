import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00827460")
App.ActiveDocument.addObject("PartDesign::Body","Body_FvYbCmobQ2vDTdZ_0")
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").Label = "Body_FvYbCmobQ2vDTdZ_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Plane", "plane_Sketch_FvYbCmobQ2vDTdZ_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FvYbCmobQ2vDTdZ_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("Sketcher::SketchObject","Sketch_FvYbCmobQ2vDTdZ_0_JGC")
App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FvYbCmobQ2vDTdZ_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC").addGeometry(Part.LineSegment(App.Vector(114.30000000000000,-41.40200000000000,0.00000000000000),App.Vector(-114.30000000000000,-41.40200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC").addGeometry(Part.LineSegment(App.Vector(-114.30000000000000,-41.40200000000000,0.00000000000000),App.Vector(-114.30000000000000,41.40200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC").addGeometry(Part.LineSegment(App.Vector(114.30000000000000,41.40200000000000,0.00000000000000),App.Vector(-114.30000000000000,41.40200000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC").addGeometry(Part.LineSegment(App.Vector(114.30000000000000,-41.40200000000000,0.00000000000000),App.Vector(114.30000000000000,41.40200000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Pad","Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC")
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC")
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").Length = 3.81
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FvYbCmobQ2vDTdZ_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FvYbCmobQ2vDTdZ_0_FPhoydt3Pua7MKZ_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Plane", "plane_Sketch_F0Fyyv1nBGvL5qq_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0Fyyv1nBGvL5qq_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("Sketcher::SketchObject","Sketch_F0Fyyv1nBGvL5qq_1_JJC")
App.ActiveDocument.getObject("Sketch_F0Fyyv1nBGvL5qq_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0Fyyv1nBGvL5qq_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F0Fyyv1nBGvL5qq_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0Fyyv1nBGvL5qq_1_JJC").addGeometry(Part.Circle(App.Vector(-76.31527000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),36.19500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0Fyyv1nBGvL5qq_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0Fyyv1nBGvL5qq_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Pad","Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC")
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F0Fyyv1nBGvL5qq_1_JJC")
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0Fyyv1nBGvL5qq_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0Fyyv1nBGvL5qq_1_FpSRVBZMKgTAot1_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Plane", "plane_Sketch_FBf9vzX7RSNp1Nj_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBf9vzX7RSNp1Nj_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("Sketcher::SketchObject","Sketch_FBf9vzX7RSNp1Nj_1_JNC")
App.ActiveDocument.getObject("Sketch_FBf9vzX7RSNp1Nj_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBf9vzX7RSNp1Nj_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FBf9vzX7RSNp1Nj_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBf9vzX7RSNp1Nj_1_JNC").addGeometry(Part.Circle(App.Vector(76.06045999999999,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),36.19500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBf9vzX7RSNp1Nj_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBf9vzX7RSNp1Nj_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Pad","Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC")
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FBf9vzX7RSNp1Nj_1_JNC")
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBf9vzX7RSNp1Nj_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBf9vzX7RSNp1Nj_1_FsN5rHgaNEUb8v6_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Plane", "plane_Sketch_FDad2Xy7R4O3rfY_1_JRC")
origin = App.Vector(-76.31527000000000,0.00000000000000,16.51000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDad2Xy7R4O3rfY_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("Sketcher::SketchObject","Sketch_FDad2Xy7R4O3rfY_1_JRC")
App.ActiveDocument.getObject("Sketch_FDad2Xy7R4O3rfY_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDad2Xy7R4O3rfY_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FDad2Xy7R4O3rfY_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDad2Xy7R4O3rfY_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),31.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDad2Xy7R4O3rfY_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDad2Xy7R4O3rfY_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Pocket","Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC")
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FDad2Xy7R4O3rfY_1_JRC")
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").Length = 17.78
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDad2Xy7R4O3rfY_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDad2Xy7R4O3rfY_1_FHa2Jm7LRahqdHQ_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Plane", "plane_Sketch_FubtZVEOY2QwsiD_1_JVC")
origin = App.Vector(76.06045999999999,0.00000000000000,16.51000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FubtZVEOY2QwsiD_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("Sketcher::SketchObject","Sketch_FubtZVEOY2QwsiD_1_JVC")
App.ActiveDocument.getObject("Sketch_FubtZVEOY2QwsiD_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FubtZVEOY2QwsiD_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FubtZVEOY2QwsiD_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FubtZVEOY2QwsiD_1_JVC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),31.75000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FubtZVEOY2QwsiD_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FubtZVEOY2QwsiD_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Pocket","Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC")
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FubtZVEOY2QwsiD_1_JVC")
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").Length = 17.78
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FubtZVEOY2QwsiD_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FubtZVEOY2QwsiD_1_FyKlLlW9SNjxB3t_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Plane", "plane_Sketch_FyMizCC83x0FQGY_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FyMizCC83x0FQGY_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("Sketcher::SketchObject","Sketch_FyMizCC83x0FQGY_1_JZC")
App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FyMizCC83x0FQGY_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,-26.08556000000000,0.00000000000000),App.Vector(-3.17500000000000,-26.08556000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC").addGeometry(Part.LineSegment(App.Vector(-3.17500000000000,-26.08556000000000,0.00000000000000),App.Vector(-3.17500000000000,-5.76556000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,-5.76556000000000,0.00000000000000),App.Vector(-3.17500000000000,-5.76556000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC").addGeometry(Part.LineSegment(App.Vector(3.17500000000000,-26.08556000000000,0.00000000000000),App.Vector(3.17500000000000,-5.76556000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Pocket","Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC")
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC")
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").Length = 7.62
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FyMizCC83x0FQGY_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FyMizCC83x0FQGY_1_FRVp7PjCtezg0wR_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Plane", "plane_Sketch_Fg0XMehLcfGZqYQ_1_JdC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg0XMehLcfGZqYQ_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("Sketcher::SketchObject","Sketch_Fg0XMehLcfGZqYQ_1_JdC")
App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg0XMehLcfGZqYQ_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC").addGeometry(Part.LineSegment(App.Vector(-7.53709000000000,-25.35349000000000,0.00000000000000),App.Vector(-13.88709000000000,-25.35349000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC").addGeometry(Part.LineSegment(App.Vector(-13.88709000000000,-25.35349000000000,0.00000000000000),App.Vector(-13.88709000000000,-12.65349000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC").addGeometry(Part.LineSegment(App.Vector(-7.53709000000000,-12.65349000000000,0.00000000000000),App.Vector(-13.88709000000000,-12.65349000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC").addGeometry(Part.LineSegment(App.Vector(-7.53709000000000,-25.35349000000000,0.00000000000000),App.Vector(-7.53709000000000,-12.65349000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Pocket","Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC")
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC")
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").Length = 7.62
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg0XMehLcfGZqYQ_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg0XMehLcfGZqYQ_1_FZAbbOkBVb2xwdA_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Plane", "plane_Sketch_FeJBqG605RrVLmf_1_JhC")
origin = App.Vector(0.00000000000000,0.00000000000000,3.81000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeJBqG605RrVLmf_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("Sketcher::SketchObject","Sketch_FeJBqG605RrVLmf_1_JhC")
App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeJBqG605RrVLmf_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC").addGeometry(Part.LineSegment(App.Vector(13.49476000000000,-25.35349000000000,0.00000000000000),App.Vector(7.14476000000000,-25.35349000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC").addGeometry(Part.LineSegment(App.Vector(7.14476000000000,-25.35349000000000,0.00000000000000),App.Vector(7.14476000000000,-12.65349000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC").addGeometry(Part.LineSegment(App.Vector(13.49476000000000,-12.65349000000000,0.00000000000000),App.Vector(7.14476000000000,-12.65349000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC").addGeometry(Part.LineSegment(App.Vector(13.49476000000000,-25.35349000000000,0.00000000000000),App.Vector(13.49476000000000,-12.65349000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FvYbCmobQ2vDTdZ_0").newObject("PartDesign::Pocket","Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC")
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC")
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").Length = 7.62
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeJBqG605RrVLmf_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeJBqG605RrVLmf_1_FtzKuS9TkPKMT13_1_JhC").Offset = 0
App.ActiveDocument.recompute()

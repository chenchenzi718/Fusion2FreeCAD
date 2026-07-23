import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00714902")
App.ActiveDocument.addObject("PartDesign::Body","Body_FkhEQ7CD7z6E2ax_0")
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").Label = "Body_FkhEQ7CD7z6E2ax_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_FkhEQ7CD7z6E2ax_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkhEQ7CD7z6E2ax_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_FkhEQ7CD7z6E2ax_0_JGC")
App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkhEQ7CD7z6E2ax_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-152.40000000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,0.00000000000000,0.00000000000000),App.Vector(-152.40000000000001,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,76.20000000000000,0.00000000000000),App.Vector(-152.40000000000001,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pad","Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC")
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC")
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").Length = 304.8
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkhEQ7CD7z6E2ax_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkhEQ7CD7z6E2ax_0_FJQR9lTskRLflyr_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_FYC3u2nxtdoDpeq_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYC3u2nxtdoDpeq_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_FYC3u2nxtdoDpeq_1_JJC")
App.ActiveDocument.getObject("Sketch_FYC3u2nxtdoDpeq_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYC3u2nxtdoDpeq_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FYC3u2nxtdoDpeq_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYC3u2nxtdoDpeq_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-304.80000000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYC3u2nxtdoDpeq_1_JJC").addGeometry(Part.LineSegment(App.Vector(-304.80000000000001,0.00000000000000,0.00000000000000),App.Vector(-304.80000000000001,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYC3u2nxtdoDpeq_1_JJC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-304.80000000000001,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYC3u2nxtdoDpeq_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYC3u2nxtdoDpeq_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pocket","Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC")
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FYC3u2nxtdoDpeq_1_JJC")
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").Length = 304.8
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYC3u2nxtdoDpeq_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYC3u2nxtdoDpeq_1_FF4UyhbaMuwCt6E_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_Fvp9w7DR4LdMnas_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fvp9w7DR4LdMnas_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_Fvp9w7DR4LdMnas_1_JNC")
App.ActiveDocument.getObject("Sketch_Fvp9w7DR4LdMnas_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fvp9w7DR4LdMnas_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fvp9w7DR4LdMnas_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fvp9w7DR4LdMnas_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-38.10000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fvp9w7DR4LdMnas_1_JNC").addGeometry(Part.LineSegment(App.Vector(-38.10000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fvp9w7DR4LdMnas_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fvp9w7DR4LdMnas_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fvp9w7DR4LdMnas_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pocket","Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC")
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fvp9w7DR4LdMnas_1_JNC")
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").Length = 304.8
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fvp9w7DR4LdMnas_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fvp9w7DR4LdMnas_1_FZylvHZTRqGlbk8_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_FZhxSlyufCv9Zii_1_JRC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZhxSlyufCv9Zii_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_FZhxSlyufCv9Zii_1_JRC")
App.ActiveDocument.getObject("Sketch_FZhxSlyufCv9Zii_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZhxSlyufCv9Zii_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FZhxSlyufCv9Zii_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZhxSlyufCv9Zii_1_JRC").addGeometry(Part.LineSegment(App.Vector(-114.30000000000000,0.00000000000000,0.00000000000000),App.Vector(-152.40000000000001,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZhxSlyufCv9Zii_1_JRC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,0.00000000000000,0.00000000000000),App.Vector(-152.40000000000001,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZhxSlyufCv9Zii_1_JRC").addGeometry(Part.LineSegment(App.Vector(-114.30000000000000,0.00000000000000,0.00000000000000),App.Vector(-152.40000000000001,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZhxSlyufCv9Zii_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZhxSlyufCv9Zii_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pocket","Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC")
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FZhxSlyufCv9Zii_1_JRC")
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").Length = 304.8
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZhxSlyufCv9Zii_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZhxSlyufCv9Zii_1_FFSz8s189UTZw55_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_F1n0YlXHGvXltBO_1_JVC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1n0YlXHGvXltBO_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_F1n0YlXHGvXltBO_1_JVC")
App.ActiveDocument.getObject("Sketch_F1n0YlXHGvXltBO_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1n0YlXHGvXltBO_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F1n0YlXHGvXltBO_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1n0YlXHGvXltBO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-304.80000000000001,76.20000000000000,0.00000000000000),App.Vector(-304.80000000000001,55.72147000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1n0YlXHGvXltBO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-289.56000000000000,76.20000000000000,0.00000000000000),App.Vector(-304.80000000000001,55.72147000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1n0YlXHGvXltBO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-304.80000000000001,76.20000000000000,0.00000000000000),App.Vector(-289.56000000000000,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1n0YlXHGvXltBO_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1n0YlXHGvXltBO_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pocket","Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC")
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F1n0YlXHGvXltBO_1_JVC")
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").Length = 304.8
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1n0YlXHGvXltBO_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F1n0YlXHGvXltBO_1_FXNeAvhfZAdweDe_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_FzpP9JeVEv3gn2s_1_JZC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzpP9JeVEv3gn2s_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_FzpP9JeVEv3gn2s_1_JZC")
App.ActiveDocument.getObject("Sketch_FzpP9JeVEv3gn2s_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzpP9JeVEv3gn2s_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FzpP9JeVEv3gn2s_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzpP9JeVEv3gn2s_1_JZC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,76.20000000000000,0.00000000000000),App.Vector(0.00000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzpP9JeVEv3gn2s_1_JZC").addGeometry(Part.LineSegment(App.Vector(-12.70000000000000,76.20000000000000,0.00000000000000),App.Vector(0.00000000000000,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FzpP9JeVEv3gn2s_1_JZC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,76.20000000000000,0.00000000000000),App.Vector(-12.70000000000000,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzpP9JeVEv3gn2s_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzpP9JeVEv3gn2s_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pocket","Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC")
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FzpP9JeVEv3gn2s_1_JZC")
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").Length = 304.8
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzpP9JeVEv3gn2s_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").Type = 0
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzpP9JeVEv3gn2s_1_FC74bdMgwSvrRdM_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_FdBDuMHKX7FOV12_1_JdC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdBDuMHKX7FOV12_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_FdBDuMHKX7FOV12_1_JdC")
App.ActiveDocument.getObject("Sketch_FdBDuMHKX7FOV12_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdBDuMHKX7FOV12_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FdBDuMHKX7FOV12_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdBDuMHKX7FOV12_1_JdC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,76.20000000000000,0.00000000000000),App.Vector(-152.40000000000001,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdBDuMHKX7FOV12_1_JdC").addGeometry(Part.LineSegment(App.Vector(-139.69999999999999,76.20000000000000,0.00000000000000),App.Vector(-152.40000000000001,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdBDuMHKX7FOV12_1_JdC").addGeometry(Part.LineSegment(App.Vector(-152.40000000000001,76.20000000000000,0.00000000000000),App.Vector(-139.69999999999999,76.20000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdBDuMHKX7FOV12_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdBDuMHKX7FOV12_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pocket","Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC")
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FdBDuMHKX7FOV12_1_JdC")
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").Length = 304.8
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdBDuMHKX7FOV12_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").Type = 0
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdBDuMHKX7FOV12_1_FKelFTXymNf22n6_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_Fj3RfuXfE2fKfXz_1_JhC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj3RfuXfE2fKfXz_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_Fj3RfuXfE2fKfXz_1_JhC")
App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj3RfuXfE2fKfXz_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,0.00000000000000,0.00000000000000),App.Vector(-76.20000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,25.40000000000000,0.00000000000000),App.Vector(-38.10000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhC").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,0.00000000000000,0.00000000000000),App.Vector(-38.10000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pocket","Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC")
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhC")
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").Length = 304.8
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").Type = 0
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_Fj3RfuXfE2fKfXz_1_JhG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fj3RfuXfE2fKfXz_1_JhG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_Fj3RfuXfE2fKfXz_1_JhG")
App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fj3RfuXfE2fKfXz_1_JhG"), [""])
App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhG").addGeometry(Part.LineSegment(App.Vector(-76.20000000000000,0.00000000000000,0.00000000000000),App.Vector(-76.20000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhG").addGeometry(Part.LineSegment(App.Vector(-114.30000000000000,0.00000000000000,0.00000000000000),App.Vector(-76.20000000000000,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhG").addGeometry(Part.LineSegment(App.Vector(-114.30000000000000,0.00000000000000,0.00000000000000),App.Vector(-76.20000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pocket","Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG")
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").Profile = App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhG")
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").Length = 304.8
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fj3RfuXfE2fKfXz_1_JhG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").Type = 0
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fj3RfuXfE2fKfXz_1_FveTyG9vsQGeDHs_1_JhG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Plane", "plane_Sketch_FlWeSi32qmYGE6r_1_JlC")
origin = App.Vector(-76.20000000000000,-144.78000000000000,76.20000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FlWeSi32qmYGE6r_1_JlC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("Sketcher::SketchObject","Sketch_FlWeSi32qmYGE6r_1_JlC")
App.ActiveDocument.getObject("Sketch_FlWeSi32qmYGE6r_1_JlC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FlWeSi32qmYGE6r_1_JlC"), [""])
App.ActiveDocument.getObject("Sketch_FlWeSi32qmYGE6r_1_JlC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FlWeSi32qmYGE6r_1_JlC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-7.62000000000002,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),50.80000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FlWeSi32qmYGE6r_1_JlC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FlWeSi32qmYGE6r_1_JlC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FkhEQ7CD7z6E2ax_0").newObject("PartDesign::Pocket","Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC")
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").Profile = App.ActiveDocument.getObject("Sketch_FlWeSi32qmYGE6r_1_JlC")
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").Length = 22.860000000000003
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FlWeSi32qmYGE6r_1_JlC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").Type = 4
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FlWeSi32qmYGE6r_1_FRUJAswxQoEfvLq_1_JlC").Offset = 0
App.ActiveDocument.recompute()

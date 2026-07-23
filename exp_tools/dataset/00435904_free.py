import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00435904")
App.ActiveDocument.addObject("PartDesign::Body","Body_F3z20LMPLyD2BiE_0")
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").Label = "Body_F3z20LMPLyD2BiE_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Plane", "plane_Sketch_F3z20LMPLyD2BiE_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3z20LMPLyD2BiE_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("Sketcher::SketchObject","Sketch_F3z20LMPLyD2BiE_0_JGC")
App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3z20LMPLyD2BiE_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC").addGeometry(Part.LineSegment(App.Vector(2750.00000000000000,-600.00000000000000,0.00000000000000),App.Vector(-2750.00000000000000,-600.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC").addGeometry(Part.LineSegment(App.Vector(-2750.00000000000000,-600.00000000000000,0.00000000000000),App.Vector(-2750.00000000000000,600.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC").addGeometry(Part.LineSegment(App.Vector(2750.00000000000000,600.00000000000000,0.00000000000000),App.Vector(-2750.00000000000000,600.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC").addGeometry(Part.LineSegment(App.Vector(2750.00000000000000,-600.00000000000000,0.00000000000000),App.Vector(2750.00000000000000,600.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Pad","Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC")
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC")
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").Length = 40.0
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3z20LMPLyD2BiE_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3z20LMPLyD2BiE_0_Fm3RM6fVSHXXcol_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Plane", "plane_Sketch_FDus1k1NvqjUZUt_1_JJC")
origin = App.Vector(0.00000000000000,-20.42897000000000,40.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FDus1k1NvqjUZUt_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("Sketcher::SketchObject","Sketch_FDus1k1NvqjUZUt_1_JJC")
App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FDus1k1NvqjUZUt_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC").addGeometry(Part.LineSegment(App.Vector(-2745.00000000000000,-574.57102999999995,0.00000000000000),App.Vector(2745.00000000000000,-574.57102999999995,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC").addGeometry(Part.LineSegment(App.Vector(2745.00000000000000,-574.57102999999995,0.00000000000000),App.Vector(2745.00000000000000,615.42896999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC").addGeometry(Part.LineSegment(App.Vector(-2745.00000000000000,615.42896999999994,0.00000000000000),App.Vector(2745.00000000000000,615.42896999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC").addGeometry(Part.LineSegment(App.Vector(-2745.00000000000000,-574.57102999999995,0.00000000000000),App.Vector(-2745.00000000000000,615.42896999999994,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Pocket","Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC")
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC")
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").Length = 35.0
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FDus1k1NvqjUZUt_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FDus1k1NvqjUZUt_1_FV8QliItLpqUITY_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Plane", "plane_Sketch_FC2fcg1xajywUO9_1_JNC")
origin = App.Vector(0.00000000000000,2.50000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FC2fcg1xajywUO9_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("Sketcher::SketchObject","Sketch_FC2fcg1xajywUO9_1_JNC")
App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FC2fcg1xajywUO9_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC").addGeometry(Part.LineSegment(App.Vector(-2711.25980000000027,558.46723000000009,0.00000000000000),App.Vector(-41.25980000000000,558.46723000000009,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC").addGeometry(Part.LineSegment(App.Vector(-41.25980000000000,558.46723000000009,0.00000000000000),App.Vector(-41.25980000000000,-561.53276999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC").addGeometry(Part.LineSegment(App.Vector(-2711.25980000000027,-561.53276999999991,0.00000000000000),App.Vector(-41.25980000000000,-561.53276999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC").addGeometry(Part.LineSegment(App.Vector(-2711.25980000000027,558.46723000000009,0.00000000000000),App.Vector(-2711.25980000000027,-561.53276999999991,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Pocket","Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC")
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC")
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Plane", "plane_Sketch_FC2fcg1xajywUO9_1_JNG")
origin = App.Vector(0.00000000000000,2.50000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FC2fcg1xajywUO9_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("Sketcher::SketchObject","Sketch_FC2fcg1xajywUO9_1_JNG")
App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FC2fcg1xajywUO9_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG").addGeometry(Part.LineSegment(App.Vector(-1.25980000000000,558.46723000000009,0.00000000000000),App.Vector(2708.74019999999973,558.46723000000009,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG").addGeometry(Part.LineSegment(App.Vector(2708.74019999999973,558.46723000000009,0.00000000000000),App.Vector(2708.74019999999973,-561.53276999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG").addGeometry(Part.LineSegment(App.Vector(-1.25980000000000,-561.53276999999991,0.00000000000000),App.Vector(2708.74019999999973,-561.53276999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG").addGeometry(Part.LineSegment(App.Vector(-1.25980000000000,558.46723000000009,0.00000000000000),App.Vector(-1.25980000000000,-561.53276999999991,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Pocket","Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG")
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG")
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FC2fcg1xajywUO9_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FC2fcg1xajywUO9_1_FqpP9iIFO0QRwCc_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Plane", "plane_Sketch_F0d42iLpH2lWZyO_1_JRG")
origin = App.Vector(0.00000000000000,2.50000000000000,5.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0d42iLpH2lWZyO_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("Sketcher::SketchObject","Sketch_F0d42iLpH2lWZyO_1_JRG")
App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0d42iLpH2lWZyO_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG").addGeometry(Part.LineSegment(App.Vector(-1.25980000000000,-561.53276999999991,0.00000000000000),App.Vector(-6.25980000000000,-561.53276999999991,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG").addGeometry(Part.LineSegment(App.Vector(-6.25980000000000,-561.53276999999991,0.00000000000000),App.Vector(-6.25980000000000,558.46723000000009,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG").addGeometry(Part.LineSegment(App.Vector(-1.25980000000000,558.46723000000009,0.00000000000000),App.Vector(-6.25980000000000,558.46723000000009,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG").addGeometry(Part.LineSegment(App.Vector(-1.25980000000000,558.46723000000009,0.00000000000000),App.Vector(-1.25980000000000,-561.53276999999991,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Pad","Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG")
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG")
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").Length = 35.0
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0d42iLpH2lWZyO_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0d42iLpH2lWZyO_1_Fo0I1eSO1FtMY4A_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Plane", "plane_Sketch_Fk7XZ60OMxaQo6y_1_JVC")
origin = App.Vector(0.00000000000000,-20.42897000000000,40.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk7XZ60OMxaQo6y_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("Sketcher::SketchObject","Sketch_Fk7XZ60OMxaQo6y_1_JVC")
App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk7XZ60OMxaQo6y_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").addGeometry(Part.LineSegment(App.Vector(-2750.00000000000000,657.98725000000002,0.00000000000000),App.Vector(2822.74985000000015,657.98725000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").addGeometry(Part.LineSegment(App.Vector(2822.74985000000015,657.98725000000002,0.00000000000000),App.Vector(2822.74985000000015,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").addGeometry(Part.LineSegment(App.Vector(2822.74985000000015,579.57101999999998,0.00000000000000),App.Vector(2750.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").addGeometry(Part.LineSegment(App.Vector(2750.00000000000000,620.42896999999994,0.00000000000000),App.Vector(2750.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").addGeometry(Part.LineSegment(App.Vector(2750.00000000000000,620.42896999999994,0.00000000000000),App.Vector(-2750.00000000000000,620.42896999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").addGeometry(Part.LineSegment(App.Vector(-2750.00000000000000,620.42896999999994,0.00000000000000),App.Vector(-2750.00000000000000,657.98725000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Pocket","Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC")
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC")
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").Length = 35.0
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Plane", "plane_Sketch_Fk7XZ60OMxaQo6y_1_JVK")
origin = App.Vector(0.00000000000000,-20.42897000000000,40.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk7XZ60OMxaQo6y_1_JVK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("Sketcher::SketchObject","Sketch_Fk7XZ60OMxaQo6y_1_JVK")
App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk7XZ60OMxaQo6y_1_JVK"), [""])
App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK").addGeometry(Part.LineSegment(App.Vector(-2745.00000000000000,579.57101999999998,0.00000000000000),App.Vector(2745.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK").addGeometry(Part.LineSegment(App.Vector(2745.00000000000000,615.42896999999994,0.00000000000000),App.Vector(2745.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK").addGeometry(Part.LineSegment(App.Vector(-2745.00000000000000,615.42896999999994,0.00000000000000),App.Vector(2745.00000000000000,615.42896999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK").addGeometry(Part.LineSegment(App.Vector(-2745.00000000000000,615.42896999999994,0.00000000000000),App.Vector(-2745.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Pocket","Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK")
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").Profile = App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK")
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").Length = 35.0
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").Type = 4
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Plane", "plane_Sketch_Fk7XZ60OMxaQo6y_1_JVS")
origin = App.Vector(0.00000000000000,-20.42897000000000,40.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fk7XZ60OMxaQo6y_1_JVS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("Sketcher::SketchObject","Sketch_Fk7XZ60OMxaQo6y_1_JVS")
App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fk7XZ60OMxaQo6y_1_JVS"), [""])
App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").addGeometry(Part.LineSegment(App.Vector(-2750.00000000000000,579.57101999999998,0.00000000000000),App.Vector(-2745.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").addGeometry(Part.LineSegment(App.Vector(-2745.00000000000000,615.42896999999994,0.00000000000000),App.Vector(-2745.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").addGeometry(Part.LineSegment(App.Vector(-2745.00000000000000,615.42896999999994,0.00000000000000),App.Vector(2745.00000000000000,615.42896999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").addGeometry(Part.LineSegment(App.Vector(2745.00000000000000,615.42896999999994,0.00000000000000),App.Vector(2745.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").addGeometry(Part.LineSegment(App.Vector(2750.00000000000000,579.57101999999998,0.00000000000000),App.Vector(2745.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").addGeometry(Part.LineSegment(App.Vector(2750.00000000000000,620.42896999999994,0.00000000000000),App.Vector(2750.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").addGeometry(Part.LineSegment(App.Vector(2750.00000000000000,620.42896999999994,0.00000000000000),App.Vector(-2750.00000000000000,620.42896999999994,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").addGeometry(Part.LineSegment(App.Vector(-2750.00000000000000,620.42896999999994,0.00000000000000),App.Vector(-2750.00000000000000,579.57101999999998,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3z20LMPLyD2BiE_0").newObject("PartDesign::Pocket","Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS")
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").Profile = App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS")
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").Length = 35.0
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fk7XZ60OMxaQo6y_1_JVS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").Type = 4
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fk7XZ60OMxaQo6y_1_Fak1FYrnXnUP2CP_1_JVS").Offset = 0
App.ActiveDocument.recompute()

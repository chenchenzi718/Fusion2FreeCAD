import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00183608")
App.ActiveDocument.addObject("PartDesign::Body","Body_FQ49aURrOa5L0fs_0")
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").Label = "Body_FQ49aURrOa5L0fs_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FQ49aURrOa5L0fs_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQ49aURrOa5L0fs_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("Sketcher::SketchObject","Sketch_FQ49aURrOa5L0fs_0_JGC")
App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQ49aURrOa5L0fs_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC").addGeometry(Part.LineSegment(App.Vector(-619.00000000000000,75.00000000000000,0.00000000000000),App.Vector(619.00000000000000,75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC").addGeometry(Part.LineSegment(App.Vector(619.00000000000000,75.00000000000000,0.00000000000000),App.Vector(619.00000000000000,-75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC").addGeometry(Part.LineSegment(App.Vector(-619.00000000000000,-75.00000000000000,0.00000000000000),App.Vector(619.00000000000000,-75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC").addGeometry(Part.LineSegment(App.Vector(-619.00000000000000,75.00000000000000,0.00000000000000),App.Vector(-619.00000000000000,-75.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Pad","Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC")
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC")
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQ49aURrOa5L0fs_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQ49aURrOa5L0fs_0_FxXR0MuB2n1w8Pp_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FkYRvs8E0tCgWBm_1_JJC")
origin = App.Vector(619.00000000000000,-10.00000000000000,0.45000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FkYRvs8E0tCgWBm_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("Sketcher::SketchObject","Sketch_FkYRvs8E0tCgWBm_1_JJC")
App.ActiveDocument.getObject("Sketch_FkYRvs8E0tCgWBm_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FkYRvs8E0tCgWBm_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FkYRvs8E0tCgWBm_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FkYRvs8E0tCgWBm_1_JJC").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,74.55000000000000,0.00000000000000),App.Vector(-10.00000000000000,74.55000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkYRvs8E0tCgWBm_1_JJC").addGeometry(Part.LineSegment(App.Vector(-10.00000000000000,74.55000000000000,0.00000000000000),App.Vector(10.00000000000000,54.55000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FkYRvs8E0tCgWBm_1_JJC").addGeometry(Part.LineSegment(App.Vector(10.00000000000000,74.55000000000000,0.00000000000000),App.Vector(10.00000000000000,54.55000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FkYRvs8E0tCgWBm_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FkYRvs8E0tCgWBm_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Pocket","Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC")
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FkYRvs8E0tCgWBm_1_JJC")
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").Length = 1250.0
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FkYRvs8E0tCgWBm_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FkYRvs8E0tCgWBm_1_FOUhsHExAjbTCRO_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FgQ9P4FBXNGo60N_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgQ9P4FBXNGo60N_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("Sketcher::SketchObject","Sketch_FgQ9P4FBXNGo60N_1_JNC")
App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgQ9P4FBXNGo60N_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-40.00000000000000,0.00000000000000),App.Vector(47.00000000000000,-40.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC").addGeometry(Part.LineSegment(App.Vector(47.00000000000000,-40.00000000000000,0.00000000000000),App.Vector(47.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(47.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-40.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-20.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Pad","Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC")
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC")
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").Length = 1204.0
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgQ9P4FBXNGo60N_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").Type = 0
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").Midplane = 1
App.ActiveDocument.getObject("Extrude_FgQ9P4FBXNGo60N_1_FCI7KkB5Br2HFMo_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FSrIqcbedMNsVAu_1_JRC")
origin = App.Vector(602.00000000000000,13.50000000000000,-30.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSrIqcbedMNsVAu_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("Sketcher::SketchObject","Sketch_FSrIqcbedMNsVAu_1_JRC")
App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSrIqcbedMNsVAu_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC").addGeometry(Part.LineSegment(App.Vector(33.50000000000000,-10.00000000000000,0.00000000000000),App.Vector(13.50000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC").addGeometry(Part.LineSegment(App.Vector(13.50000000000000,-10.00000000000000,0.00000000000000),App.Vector(13.50000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC").addGeometry(Part.LineSegment(App.Vector(33.50000000000000,10.00000000000000,0.00000000000000),App.Vector(13.50000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC").addGeometry(Part.LineSegment(App.Vector(33.50000000000000,-10.00000000000000,0.00000000000000),App.Vector(33.50000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Pad","Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC")
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC")
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSrIqcbedMNsVAu_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSrIqcbedMNsVAu_1_FILfVcZYXIBNHD2_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FIu2CA7JNQrbEHX_1_JWC")
origin = App.Vector(622.00000000000000,37.00000000000000,-30.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FIu2CA7JNQrbEHX_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("Sketcher::SketchObject","Sketch_FIu2CA7JNQrbEHX_1_JWC")
App.ActiveDocument.getObject("Sketch_FIu2CA7JNQrbEHX_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FIu2CA7JNQrbEHX_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FIu2CA7JNQrbEHX_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FIu2CA7JNQrbEHX_1_JWC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FIu2CA7JNQrbEHX_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FIu2CA7JNQrbEHX_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Pad","Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC")
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FIu2CA7JNQrbEHX_1_JWC")
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FIu2CA7JNQrbEHX_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FIu2CA7JNQrbEHX_1_FQcEOKl0pZeUO4i_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FK1N6tTNAk9gLbm_1_JaC")
origin = App.Vector(-602.00000000000000,13.50000000000000,-30.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FK1N6tTNAk9gLbm_1_JaC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("Sketcher::SketchObject","Sketch_FK1N6tTNAk9gLbm_1_JaC")
App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FK1N6tTNAk9gLbm_1_JaC"), [""])
App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC").addGeometry(Part.LineSegment(App.Vector(-33.50000000000000,10.00000000000000,0.00000000000000),App.Vector(-13.50000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC").addGeometry(Part.LineSegment(App.Vector(-13.50000000000000,10.00000000000000,0.00000000000000),App.Vector(-13.50000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC").addGeometry(Part.LineSegment(App.Vector(-33.50000000000000,-10.00000000000000,0.00000000000000),App.Vector(-13.50000000000000,-10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC").addGeometry(Part.LineSegment(App.Vector(-33.50000000000000,-10.00000000000000,0.00000000000000),App.Vector(-33.50000000000000,10.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Pad","Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC")
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").Profile = App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC")
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").Length = 20.0
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FK1N6tTNAk9gLbm_1_JaC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").Type = 4
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FK1N6tTNAk9gLbm_1_FMM9LHegwDKwAuF_1_JaC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Plane", "plane_Sketch_FbqoFVpjZ3KbM5i_1_JeC")
origin = App.Vector(-622.00000000000000,37.00000000000000,-30.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbqoFVpjZ3KbM5i_1_JeC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("Sketcher::SketchObject","Sketch_FbqoFVpjZ3KbM5i_1_JeC")
App.ActiveDocument.getObject("Sketch_FbqoFVpjZ3KbM5i_1_JeC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbqoFVpjZ3KbM5i_1_JeC"), [""])
App.ActiveDocument.getObject("Sketch_FbqoFVpjZ3KbM5i_1_JeC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbqoFVpjZ3KbM5i_1_JeC").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),5.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbqoFVpjZ3KbM5i_1_JeC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbqoFVpjZ3KbM5i_1_JeC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Pad","Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC")
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").Profile = App.ActiveDocument.getObject("Sketch_FbqoFVpjZ3KbM5i_1_JeC")
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbqoFVpjZ3KbM5i_1_JeC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").Type = 4
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbqoFVpjZ3KbM5i_1_FpmVM0Cm3TnlPML_1_JeC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Plane", "plane_Sketch_Fn30jzwGlq3lOkw_1_JkC")
origin = App.Vector(574.50000000000000,23.50000000000000,-40.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fn30jzwGlq3lOkw_1_JkC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("Sketcher::SketchObject","Sketch_Fn30jzwGlq3lOkw_1_JkC")
App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fn30jzwGlq3lOkw_1_JkC"), [""])
App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC").addGeometry(Part.LineSegment(App.Vector(-47.49999999999999,-23.50000000000000,0.00000000000000),App.Vector(-1101.50000000000023,-23.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC").addGeometry(Part.LineSegment(App.Vector(-1101.50000000000023,-23.50000000000000,0.00000000000000),App.Vector(-1101.50000000000023,23.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC").addGeometry(Part.LineSegment(App.Vector(-47.49999999999999,23.50000000000000,0.00000000000000),App.Vector(-1101.50000000000023,23.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC").addGeometry(Part.LineSegment(App.Vector(-47.49999999999999,-23.50000000000000,0.00000000000000),App.Vector(-47.49999999999999,23.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQ49aURrOa5L0fs_0").newObject("PartDesign::Pocket","Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC")
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").Profile = App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC")
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fn30jzwGlq3lOkw_1_JkC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").Type = 4
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fn30jzwGlq3lOkw_1_Fy047qaFfyGkfpj_1_JkC").Offset = 0
App.ActiveDocument.recompute()

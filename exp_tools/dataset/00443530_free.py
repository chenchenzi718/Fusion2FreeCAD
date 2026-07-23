import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00443530")
App.ActiveDocument.addObject("PartDesign::Body","Body_F5oWE5TeLOxb5tF_0")
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").Label = "Body_F5oWE5TeLOxb5tF_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Plane", "plane_Sketch_F5oWE5TeLOxb5tF_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5oWE5TeLOxb5tF_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("Sketcher::SketchObject","Sketch_F5oWE5TeLOxb5tF_0_JGC")
App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5oWE5TeLOxb5tF_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(35.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC").addGeometry(Part.LineSegment(App.Vector(35.00000000000000,0.00000000000000,0.00000000000000),App.Vector(35.00000000000000,122.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,122.00000000000000,0.00000000000000),App.Vector(35.00000000000000,122.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,122.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Pad","Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC")
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC")
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5oWE5TeLOxb5tF_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5oWE5TeLOxb5tF_0_FYec858KAx7fzGi_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Plane", "plane_Sketch_FVTrccQLvf2FHDP_1_JJC")
origin = App.Vector(17.50000000000000,-6.35000000000000,48.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVTrccQLvf2FHDP_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("Sketcher::SketchObject","Sketch_FVTrccQLvf2FHDP_1_JJC")
App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVTrccQLvf2FHDP_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC").addGeometry(Part.LineSegment(App.Vector(-17.50000000000000,-48.50000000000000,0.00000000000000),App.Vector(-10.50000000000000,-48.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC").addGeometry(Part.LineSegment(App.Vector(-10.50000000000000,-48.50000000000000,0.00000000000000),App.Vector(-10.50000000000000,-73.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC").addGeometry(Part.LineSegment(App.Vector(-17.50000000000000,-73.50000000000001,0.00000000000000),App.Vector(-10.50000000000000,-73.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC").addGeometry(Part.LineSegment(App.Vector(-17.50000000000000,-48.50000000000000,0.00000000000000),App.Vector(-17.50000000000000,-73.50000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Pad","Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC")
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC")
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Plane", "plane_Sketch_FVTrccQLvf2FHDP_1_JJG")
origin = App.Vector(17.50000000000000,-6.35000000000000,48.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVTrccQLvf2FHDP_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("Sketcher::SketchObject","Sketch_FVTrccQLvf2FHDP_1_JJG")
App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVTrccQLvf2FHDP_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG").addGeometry(Part.LineSegment(App.Vector(17.50000000000000,-48.50000000000000,0.00000000000000),App.Vector(10.50000000000000,-48.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG").addGeometry(Part.LineSegment(App.Vector(10.50000000000000,-48.50000000000000,0.00000000000000),App.Vector(10.50000000000000,-73.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG").addGeometry(Part.LineSegment(App.Vector(10.50000000000000,-73.50000000000001,0.00000000000000),App.Vector(17.50000000000000,-73.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG").addGeometry(Part.LineSegment(App.Vector(17.50000000000000,-48.50000000000000,0.00000000000000),App.Vector(17.50000000000000,-73.50000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Pad","Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG")
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG")
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Plane", "plane_Sketch_FVTrccQLvf2FHDP_1_JJK")
origin = App.Vector(17.50000000000000,-6.35000000000000,48.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FVTrccQLvf2FHDP_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("Sketcher::SketchObject","Sketch_FVTrccQLvf2FHDP_1_JJK")
App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FVTrccQLvf2FHDP_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK").addGeometry(Part.LineSegment(App.Vector(-3.50000000000000,-48.50000000000000,0.00000000000000),App.Vector(3.50000000000000,-48.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK").addGeometry(Part.LineSegment(App.Vector(3.50000000000000,-48.50000000000000,0.00000000000000),App.Vector(3.50000000000000,-73.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK").addGeometry(Part.LineSegment(App.Vector(-3.50000000000000,-73.50000000000001,0.00000000000000),App.Vector(3.50000000000000,-73.50000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK").addGeometry(Part.LineSegment(App.Vector(-3.50000000000000,-48.50000000000000,0.00000000000000),App.Vector(-3.50000000000000,-73.50000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Pad","Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK")
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK")
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FVTrccQLvf2FHDP_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").Type = 0
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FVTrccQLvf2FHDP_1_FqULBmR9jLhSXET_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Plane", "plane_Sketch_F0Bc8DApzdqblqB_4_JNC")
origin = App.Vector(17.50000000000000,-6.35000000000000,48.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0Bc8DApzdqblqB_4_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("Sketcher::SketchObject","Sketch_F0Bc8DApzdqblqB_4_JNC")
App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0Bc8DApzdqblqB_4_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC").addGeometry(Part.LineSegment(App.Vector(-2.92500000000000,-27.65000000000000,0.00000000000000),App.Vector(2.92500000000000,-27.65000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC").addGeometry(Part.LineSegment(App.Vector(2.92500000000000,-27.65000000000000,0.00000000000000),App.Vector(2.92500000000000,-33.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC").addGeometry(Part.LineSegment(App.Vector(-2.92500000000000,-33.50000000000000,0.00000000000000),App.Vector(2.92500000000000,-33.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC").addGeometry(Part.LineSegment(App.Vector(-2.92500000000000,-27.65000000000000,0.00000000000000),App.Vector(-2.92500000000000,-33.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Pocket","Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC")
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").Profile = App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC")
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0Bc8DApzdqblqB_4_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0Bc8DApzdqblqB_4_FV8eCENXyp9Nmnq_4_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Plane", "plane_Sketch_FLk8V25j35bAW8i_1_JRC")
origin = App.Vector(17.50000000000000,-6.35000000000000,48.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLk8V25j35bAW8i_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("Sketcher::SketchObject","Sketch_FLk8V25j35bAW8i_1_JRC")
App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLk8V25j35bAW8i_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-20.15000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Pocket","Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC")
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRC")
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Plane", "plane_Sketch_FLk8V25j35bAW8i_1_JRG")
origin = App.Vector(17.50000000000000,-6.35000000000000,48.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLk8V25j35bAW8i_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("Sketcher::SketchObject","Sketch_FLk8V25j35bAW8i_1_JRG")
App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLk8V25j35bAW8i_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRG").addGeometry(Part.Circle(App.Vector(0.00000000000000,-12.65000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.25000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Pocket","Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG")
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRG")
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLk8V25j35bAW8i_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLk8V25j35bAW8i_1_FnZSIL86DQy6xRI_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Plane", "plane_Sketch_F0ipWLspCNE88Ii_1_JWC")
origin = App.Vector(17.50000000000000,-6.35000000000000,48.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0ipWLspCNE88Ii_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("Sketcher::SketchObject","Sketch_F0ipWLspCNE88Ii_1_JWC")
App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0ipWLspCNE88Ii_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC").addGeometry(Part.LineSegment(App.Vector(-9.85000000000000,73.50000000000000,0.00000000000000),App.Vector(-3.50000000000000,73.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC").addGeometry(Part.LineSegment(App.Vector(-3.50000000000000,73.50000000000000,0.00000000000000),App.Vector(-3.50000000000000,67.15000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC").addGeometry(Part.LineSegment(App.Vector(-9.85000000000000,67.15000000000001,0.00000000000000),App.Vector(-3.50000000000000,67.15000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC").addGeometry(Part.LineSegment(App.Vector(-9.85000000000000,73.50000000000000,0.00000000000000),App.Vector(-9.85000000000000,67.15000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Pocket","Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC")
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC")
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Plane", "plane_Sketch_F0ipWLspCNE88Ii_1_JWG")
origin = App.Vector(17.50000000000000,-6.35000000000000,48.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0ipWLspCNE88Ii_1_JWG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("Sketcher::SketchObject","Sketch_F0ipWLspCNE88Ii_1_JWG")
App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0ipWLspCNE88Ii_1_JWG"), [""])
App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG").addGeometry(Part.LineSegment(App.Vector(3.50000000000000,73.50000000000000,0.00000000000000),App.Vector(9.85000000000000,73.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG").addGeometry(Part.LineSegment(App.Vector(9.85000000000000,73.50000000000000,0.00000000000000),App.Vector(9.85000000000000,67.15000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG").addGeometry(Part.LineSegment(App.Vector(3.50000000000000,67.15000000000001,0.00000000000000),App.Vector(9.85000000000000,67.15000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG").addGeometry(Part.LineSegment(App.Vector(3.50000000000000,73.50000000000000,0.00000000000000),App.Vector(3.50000000000000,67.15000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F5oWE5TeLOxb5tF_0").newObject("PartDesign::Pocket","Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG")
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").Profile = App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG")
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").Length = 25.0
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0ipWLspCNE88Ii_1_JWG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").Type = 4
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0ipWLspCNE88Ii_1_FUdx4QL8GVCVIay_1_JWG").Offset = 0
App.ActiveDocument.recompute()

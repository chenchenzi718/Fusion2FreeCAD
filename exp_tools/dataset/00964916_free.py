import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00964916")
App.ActiveDocument.addObject("PartDesign::Body","Body_FwWBvjZYZcaOQfd_0")
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").Label = "Body_FwWBvjZYZcaOQfd_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Plane", "plane_Sketch_FwWBvjZYZcaOQfd_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwWBvjZYZcaOQfd_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("Sketcher::SketchObject","Sketch_FwWBvjZYZcaOQfd_0_JGC")
App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwWBvjZYZcaOQfd_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,60.00000000000000,0.00000000000000),App.Vector(20.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,60.00000000000000,0.00000000000000),App.Vector(20.00000000000000,59.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,59.00000000000000,0.00000000000000),App.Vector(20.00000000000000,59.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,60.00000000000000,0.00000000000000),App.Vector(-20.00000000000000,59.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Pad","Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC")
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC")
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").Length = 13.000000000000002
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_FYI6WJVPLyopJoo_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Plane", "plane_Sketch_FwWBvjZYZcaOQfd_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwWBvjZYZcaOQfd_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("Sketcher::SketchObject","Sketch_FwWBvjZYZcaOQfd_0_JGG")
App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwWBvjZYZcaOQfd_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(20.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG").addGeometry(Part.LineSegment(App.Vector(20.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(20.00000000000000,59.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,59.00000000000000,0.00000000000000),App.Vector(20.00000000000000,59.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-20.00000000000000,59.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Pad","Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG")
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").Profile = App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG")
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").Length = 1.0
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwWBvjZYZcaOQfd_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwWBvjZYZcaOQfd_0_Fb5oa92hpYGEpH5_1_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Plane", "plane_Sketch_FBdIIillc0jKOkT_1_JLC")
origin = App.Vector(0.00000000000000,0.00000000000000,-0.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBdIIillc0jKOkT_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("Sketcher::SketchObject","Sketch_FBdIIillc0jKOkT_1_JLC")
App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBdIIillc0jKOkT_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").addGeometry(Part.LineSegment(App.Vector(15.00000000000000,83.50000000000000,0.00000000000000),App.Vector(-21.00000000000000,83.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").addGeometry(Part.LineSegment(App.Vector(-21.00000000000000,83.50000000000000,0.00000000000000),App.Vector(-21.00000000000000,-41.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").addGeometry(Part.LineSegment(App.Vector(-21.00000000000000,-41.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,-41.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,59.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,-41.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,59.50000000000000,0.00000000000000),App.Vector(15.00000000000000,59.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").addGeometry(Part.LineSegment(App.Vector(15.00000000000000,83.50000000000000,0.00000000000000),App.Vector(15.00000000000000,59.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Pad","Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC")
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC")
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").Length = 275.0
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").Type = 0
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Plane", "plane_Sketch_FBdIIillc0jKOkT_1_JLK")
origin = App.Vector(0.00000000000000,0.00000000000000,-0.50000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FBdIIillc0jKOkT_1_JLK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("Sketcher::SketchObject","Sketch_FBdIIillc0jKOkT_1_JLK")
App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FBdIIillc0jKOkT_1_JLK"), [""])
App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK").addGeometry(Part.LineSegment(App.Vector(15.00000000000000,-41.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,-41.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,59.50000000000000,0.00000000000000),App.Vector(-20.00000000000000,-41.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK").addGeometry(Part.LineSegment(App.Vector(-20.00000000000000,59.50000000000000,0.00000000000000),App.Vector(15.00000000000000,59.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK").addGeometry(Part.LineSegment(App.Vector(15.00000000000000,-41.50000000000000,0.00000000000000),App.Vector(15.00000000000000,59.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Pad","Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK")
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").Profile = App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK")
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").Length = 275.0
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FBdIIillc0jKOkT_1_JLK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").Type = 0
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").Reversed = 1
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FBdIIillc0jKOkT_1_FQnqhUG7Jlfz14A_1_JLK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Plane", "plane_Sketch_FzUJVmIjAMz9vPZ_1_JPC")
origin = App.Vector(15.00000000000000,137.50000000000000,20.50000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzUJVmIjAMz9vPZ_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("Sketcher::SketchObject","Sketch_FzUJVmIjAMz9vPZ_1_JPC")
App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzUJVmIjAMz9vPZ_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPC").addGeometry(Part.Circle(App.Vector(60.50000000000000,0.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),50.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Pocket","Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC")
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPC")
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").Length = 5.0
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Plane", "plane_Sketch_FzUJVmIjAMz9vPZ_1_JPG")
origin = App.Vector(15.00000000000000,137.50000000000000,20.50000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FzUJVmIjAMz9vPZ_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("Sketcher::SketchObject","Sketch_FzUJVmIjAMz9vPZ_1_JPG")
App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FzUJVmIjAMz9vPZ_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPG").addGeometry(Part.Circle(App.Vector(-52.50000000000001,0.50000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),50.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Pocket","Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG")
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPG")
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").Length = 5.0
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FzUJVmIjAMz9vPZ_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FzUJVmIjAMz9vPZ_1_FylFqwidfmtwiOy_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Plane", "plane_Sketch_FSj3E1Geoz2dPsj_1_JTG")
origin = App.Vector(-3.00000000000000,137.50000000000000,83.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSj3E1Geoz2dPsj_1_JTG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("Sketcher::SketchObject","Sketch_FSj3E1Geoz2dPsj_1_JTG")
App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSj3E1Geoz2dPsj_1_JTG"), [""])
App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,115.49999999999999,0.00000000000000),App.Vector(-6.00000000000000,115.49999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,115.49999999999999,0.00000000000000),App.Vector(-6.00000000000000,97.49999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,97.49999999999997,0.00000000000000),App.Vector(-6.00000000000000,97.49999999999997,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,115.49999999999999,0.00000000000000),App.Vector(-16.00000000000000,97.49999999999997,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Pocket","Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG")
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").Profile = App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG")
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").Length = 2.0
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").Type = 4
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Plane", "plane_Sketch_FSj3E1Geoz2dPsj_1_JTC")
origin = App.Vector(-3.00000000000000,137.50000000000000,83.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FSj3E1Geoz2dPsj_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("Sketcher::SketchObject","Sketch_FSj3E1Geoz2dPsj_1_JTC")
App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FSj3E1Geoz2dPsj_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,117.50000000000000,0.00000000000000),App.Vector(-16.00000000000000,117.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC").addGeometry(Part.LineSegment(App.Vector(-16.00000000000000,117.50000000000000,0.00000000000000),App.Vector(-16.00000000000000,135.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,135.50000000000000,0.00000000000000),App.Vector(-16.00000000000000,135.50000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC").addGeometry(Part.LineSegment(App.Vector(-6.00000000000000,117.50000000000000,0.00000000000000),App.Vector(-6.00000000000000,135.50000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FwWBvjZYZcaOQfd_0").newObject("PartDesign::Pocket","Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC")
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC")
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FSj3E1Geoz2dPsj_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FSj3E1Geoz2dPsj_1_F9SopiE41Jb2FAS_1_JTC").Offset = 0
App.ActiveDocument.recompute()

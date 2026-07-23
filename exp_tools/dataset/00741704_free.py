import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00741704")
App.ActiveDocument.addObject("PartDesign::Body","Body_FusHgy6qVJFGiF9_0")
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").Label = "Body_FusHgy6qVJFGiF9_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Plane", "plane_Sketch_FusHgy6qVJFGiF9_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FusHgy6qVJFGiF9_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("Sketcher::SketchObject","Sketch_FusHgy6qVJFGiF9_0_JGC")
App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FusHgy6qVJFGiF9_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC").addGeometry(Part.LineSegment(App.Vector(11.56737000000000,-13.65612000000000,0.00000000000000),App.Vector(41.32101000000000,-13.65612000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC").addGeometry(Part.LineSegment(App.Vector(41.32101000000000,-13.65612000000000,0.00000000000000),App.Vector(41.32101000000000,16.25435000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC").addGeometry(Part.LineSegment(App.Vector(11.56737000000000,16.25435000000000,0.00000000000000),App.Vector(41.32101000000000,16.25435000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC").addGeometry(Part.LineSegment(App.Vector(11.56737000000000,-13.65612000000000,0.00000000000000),App.Vector(11.56737000000000,16.25435000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Pad","Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC")
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC")
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").Length = 69.4
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FusHgy6qVJFGiF9_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FusHgy6qVJFGiF9_0_FiyWwiLpo0eN7t2_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Plane", "plane_Sketch_Fy1YM8IpOe9ZbJf_1_JJC")
origin = App.Vector(26.44419000000000,1.29912000000000,69.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fy1YM8IpOe9ZbJf_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("Sketcher::SketchObject","Sketch_Fy1YM8IpOe9ZbJf_1_JJC")
App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fy1YM8IpOe9ZbJf_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC").addGeometry(Part.LineSegment(App.Vector(12.84251000000000,-13.35713000000000,0.00000000000000),App.Vector(-13.38543000000000,-13.35713000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC").addGeometry(Part.LineSegment(App.Vector(-13.38543000000000,-13.35713000000000,0.00000000000000),App.Vector(-13.38543000000000,13.29307000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC").addGeometry(Part.LineSegment(App.Vector(12.84251000000000,13.29307000000000,0.00000000000000),App.Vector(-13.38543000000000,13.29307000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC").addGeometry(Part.LineSegment(App.Vector(12.84251000000000,-13.35713000000000,0.00000000000000),App.Vector(12.84251000000000,13.29307000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Pocket","Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC")
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC")
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").Length = 2.0
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fy1YM8IpOe9ZbJf_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fy1YM8IpOe9ZbJf_1_FZAN1yteUmXHa5B_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Plane", "plane_Sketch_FZGttN5wXHo4xvJ_1_JNC")
origin = App.Vector(26.17273000000000,1.26709000000000,67.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FZGttN5wXHo4xvJ_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("Sketcher::SketchObject","Sketch_FZGttN5wXHo4xvJ_1_JNC")
App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FZGttN5wXHo4xvJ_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-11.29786000000000,-11.02576000000000,0.00000000000000),App.Vector(11.31892000000000,-11.02576000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(11.31892000000000,-11.02576000000000,0.00000000000000),App.Vector(11.31892000000000,11.60917000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-11.29786000000000,11.60917000000000,0.00000000000000),App.Vector(11.31892000000000,11.60917000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC").addGeometry(Part.LineSegment(App.Vector(-11.29786000000000,-11.02576000000000,0.00000000000000),App.Vector(-11.29786000000000,11.60917000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Pocket","Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC")
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC")
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FZGttN5wXHo4xvJ_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FZGttN5wXHo4xvJ_1_FYHZKTDI2ss6fvA_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Plane", "plane_Sketch_FHJE8cxeqrjHy6n_1_JRC")
origin = App.Vector(26.18326000000000,1.55880000000000,65.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FHJE8cxeqrjHy6n_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("Sketcher::SketchObject","Sketch_FHJE8cxeqrjHy6n_1_JRC")
App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FHJE8cxeqrjHy6n_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC").addGeometry(Part.LineSegment(App.Vector(9.71988000000000,9.46502000000000,0.00000000000000),App.Vector(-9.07892000000000,9.46502000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC").addGeometry(Part.LineSegment(App.Vector(-9.07892000000000,9.46502000000000,0.00000000000000),App.Vector(-9.07892000000000,-9.24972000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC").addGeometry(Part.LineSegment(App.Vector(9.71988000000000,-9.24972000000000,0.00000000000000),App.Vector(-9.07892000000000,-9.24972000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC").addGeometry(Part.LineSegment(App.Vector(9.71988000000000,9.46502000000000,0.00000000000000),App.Vector(9.71988000000000,-9.24972000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Pocket","Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC")
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC")
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FHJE8cxeqrjHy6n_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FHJE8cxeqrjHy6n_1_Fh4m4lOzvAGPHij_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Plane", "plane_Sketch_FYJXzONdzAQjvjF_1_JVC")
origin = App.Vector(26.50374000000000,1.66645000000000,63.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYJXzONdzAQjvjF_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("Sketcher::SketchObject","Sketch_FYJXzONdzAQjvjF_1_JVC")
App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYJXzONdzAQjvjF_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC").addGeometry(Part.LineSegment(App.Vector(7.55957000000000,-7.54747000000000,0.00000000000000),App.Vector(-7.85971000000000,-7.54747000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC").addGeometry(Part.LineSegment(App.Vector(-7.85971000000000,-7.54747000000000,0.00000000000000),App.Vector(-7.85971000000000,8.11944000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC").addGeometry(Part.LineSegment(App.Vector(7.55957000000000,8.11944000000000,0.00000000000000),App.Vector(-7.85971000000000,8.11944000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC").addGeometry(Part.LineSegment(App.Vector(7.55957000000000,-7.54747000000000,0.00000000000000),App.Vector(7.55957000000000,8.11944000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Pocket","Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC")
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC")
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYJXzONdzAQjvjF_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYJXzONdzAQjvjF_1_FKZSICA3Mu6MtAe_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Plane", "plane_Sketch_FeqfYuFOeJaPGiu_1_JZC")
origin = App.Vector(26.35367000000000,1.95243000000000,61.40000000000001)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeqfYuFOeJaPGiu_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("Sketcher::SketchObject","Sketch_FeqfYuFOeJaPGiu_1_JZC")
App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeqfYuFOeJaPGiu_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC").addGeometry(Part.LineSegment(App.Vector(-6.16788000000000,-5.99396000000000,0.00000000000000),App.Vector(6.07398000000000,-5.99396000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC").addGeometry(Part.LineSegment(App.Vector(6.07398000000000,-5.99396000000000,0.00000000000000),App.Vector(6.07398000000000,5.60153000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC").addGeometry(Part.LineSegment(App.Vector(-6.16788000000000,5.60153000000000,0.00000000000000),App.Vector(6.07398000000000,5.60153000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC").addGeometry(Part.LineSegment(App.Vector(-6.16788000000000,-5.99396000000000,0.00000000000000),App.Vector(-6.16788000000000,5.60153000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Pocket","Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC")
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC")
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeqfYuFOeJaPGiu_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeqfYuFOeJaPGiu_1_FIxVKsb7xhxHB8A_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Plane", "plane_Sketch_FOAFMLahVdszkzo_1_JdC")
origin = App.Vector(26.30672000000000,1.75622000000000,59.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FOAFMLahVdszkzo_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("Sketcher::SketchObject","Sketch_FOAFMLahVdszkzo_1_JdC")
App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FOAFMLahVdszkzo_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC").addGeometry(Part.LineSegment(App.Vector(-4.52772000000000,3.77665000000000,0.00000000000000),App.Vector(4.33964000000000,3.77665000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC").addGeometry(Part.LineSegment(App.Vector(4.33964000000000,3.77665000000000,0.00000000000000),App.Vector(4.33964000000000,-4.53696000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC").addGeometry(Part.LineSegment(App.Vector(-4.52772000000000,-4.53696000000000,0.00000000000000),App.Vector(4.33964000000000,-4.53696000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC").addGeometry(Part.LineSegment(App.Vector(-4.52772000000000,3.77665000000000,0.00000000000000),App.Vector(-4.52772000000000,-4.53696000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Pocket","Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC")
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC")
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FOAFMLahVdszkzo_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FOAFMLahVdszkzo_1_FhYSeO7TmqoJi9X_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Plane", "plane_Sketch_FWHgbwKGrAMNWaG_1_JhC")
origin = App.Vector(26.21268000000000,1.37607000000000,57.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FWHgbwKGrAMNWaG_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("Sketcher::SketchObject","Sketch_FWHgbwKGrAMNWaG_1_JhC")
App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FWHgbwKGrAMNWaG_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC").addGeometry(Part.LineSegment(App.Vector(-2.83100000000000,2.80523000000000,0.00000000000000),App.Vector(3.11321000000000,2.80523000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC").addGeometry(Part.LineSegment(App.Vector(3.11321000000000,2.80523000000000,0.00000000000000),App.Vector(3.11321000000000,-2.59991000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC").addGeometry(Part.LineSegment(App.Vector(-2.83100000000000,-2.59991000000000,0.00000000000000),App.Vector(3.11321000000000,-2.59991000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC").addGeometry(Part.LineSegment(App.Vector(-2.83100000000000,2.80523000000000,0.00000000000000),App.Vector(-2.83100000000000,-2.59991000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FusHgy6qVJFGiF9_0").newObject("PartDesign::Pocket","Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC")
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC")
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").Length = 2.0
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FWHgbwKGrAMNWaG_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FWHgbwKGrAMNWaG_1_FdfgMKdk4oGUPY5_1_JhC").Offset = 0
App.ActiveDocument.recompute()

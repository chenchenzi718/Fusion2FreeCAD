import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00934891")
App.ActiveDocument.addObject("PartDesign::Body","Body_FxuVYf0eZtv4g2d_0")
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").Label = "Body_FxuVYf0eZtv4g2d_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Plane", "plane_Sketch_FxuVYf0eZtv4g2d_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FxuVYf0eZtv4g2d_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("Sketcher::SketchObject","Sketch_FxuVYf0eZtv4g2d_0_JGC")
App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FxuVYf0eZtv4g2d_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").addGeometry(Part.LineSegment(App.Vector(-590.55000000000007,38.10000000000000,0.00000000000000),App.Vector(590.55000000000007,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").addGeometry(Part.LineSegment(App.Vector(590.55000000000007,38.10000000000000,0.00000000000000),App.Vector(596.89999999999998,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").addGeometry(Part.LineSegment(App.Vector(596.89999999999998,38.10000000000000,0.00000000000000),App.Vector(596.89999999999998,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").addGeometry(Part.LineSegment(App.Vector(590.55000000000007,-38.10000000000000,0.00000000000000),App.Vector(596.89999999999998,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").addGeometry(Part.LineSegment(App.Vector(-590.55000000000007,-38.10000000000000,0.00000000000000),App.Vector(590.55000000000007,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").addGeometry(Part.LineSegment(App.Vector(-590.55000000000007,-38.10000000000000,0.00000000000000),App.Vector(-596.89999999999998,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").addGeometry(Part.LineSegment(App.Vector(-596.89999999999998,38.10000000000000,0.00000000000000),App.Vector(-596.89999999999998,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").addGeometry(Part.LineSegment(App.Vector(-590.55000000000007,38.10000000000000,0.00000000000000),App.Vector(-596.89999999999998,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Pad","Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC")
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC")
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FxuVYf0eZtv4g2d_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FxuVYf0eZtv4g2d_0_FxqVlbKf5SCVtjy_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Plane", "plane_Sketch_FYixABvOWBfGfpp_1_JJC")
origin = App.Vector(0.00000000000000,-50.80000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYixABvOWBfGfpp_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("Sketcher::SketchObject","Sketch_FYixABvOWBfGfpp_1_JJC")
App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYixABvOWBfGfpp_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC").addGeometry(Part.LineSegment(App.Vector(-590.55000000000007,38.10000000000000,0.00000000000000),App.Vector(-590.55000000000007,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC").addGeometry(Part.LineSegment(App.Vector(-596.89999999999998,-38.10000000000000,0.00000000000000),App.Vector(-590.55000000000007,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC").addGeometry(Part.LineSegment(App.Vector(-596.89999999999998,38.10000000000000,0.00000000000000),App.Vector(-596.89999999999998,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC").addGeometry(Part.LineSegment(App.Vector(-596.89999999999998,38.10000000000000,0.00000000000000),App.Vector(-590.55000000000007,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Pad","Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC")
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC")
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").Length = 146.05
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Plane", "plane_Sketch_FYixABvOWBfGfpp_1_JJG")
origin = App.Vector(0.00000000000000,-50.80000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FYixABvOWBfGfpp_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("Sketcher::SketchObject","Sketch_FYixABvOWBfGfpp_1_JJG")
App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FYixABvOWBfGfpp_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG").addGeometry(Part.LineSegment(App.Vector(590.55000000000007,38.10000000000000,0.00000000000000),App.Vector(590.55000000000007,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG").addGeometry(Part.LineSegment(App.Vector(596.89999999999998,-38.10000000000000,0.00000000000000),App.Vector(590.55000000000007,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG").addGeometry(Part.LineSegment(App.Vector(596.89999999999998,38.10000000000000,0.00000000000000),App.Vector(596.89999999999998,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG").addGeometry(Part.LineSegment(App.Vector(596.89999999999998,38.10000000000000,0.00000000000000),App.Vector(590.55000000000007,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Pad","Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG")
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG")
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").Length = 146.05
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FYixABvOWBfGfpp_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FYixABvOWBfGfpp_1_FaB5kKywZLGK46q_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Plane", "plane_Sketch_Ff5BqUvez9Y11VX_1_JNC")
origin = App.Vector(-590.55000000000007,-123.82500000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff5BqUvez9Y11VX_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("Sketcher::SketchObject","Sketch_Ff5BqUvez9Y11VX_1_JNC")
App.ActiveDocument.getObject("Sketch_Ff5BqUvez9Y11VX_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff5BqUvez9Y11VX_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Ff5BqUvez9Y11VX_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff5BqUvez9Y11VX_1_JNC").addGeometry(Part.Circle(App.Vector(6.22300000000001,-12.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.70000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff5BqUvez9Y11VX_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff5BqUvez9Y11VX_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Pocket","Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC")
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Ff5BqUvez9Y11VX_1_JNC")
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff5BqUvez9Y11VX_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff5BqUvez9Y11VX_1_F9qKeUfTGz0od56_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Plane", "plane_Sketch_FqdAVnlthGFAS79_1_JRC")
origin = App.Vector(596.89999999999998,-98.42500000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,-0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FqdAVnlthGFAS79_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("Sketcher::SketchObject","Sketch_FqdAVnlthGFAS79_1_JRC")
App.ActiveDocument.getObject("Sketch_FqdAVnlthGFAS79_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FqdAVnlthGFAS79_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FqdAVnlthGFAS79_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FqdAVnlthGFAS79_1_JRC").addGeometry(Part.Circle(App.Vector(-25.52700000000001,-12.70000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),12.70000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FqdAVnlthGFAS79_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FqdAVnlthGFAS79_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Pocket","Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC")
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FqdAVnlthGFAS79_1_JRC")
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FqdAVnlthGFAS79_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FqdAVnlthGFAS79_1_Fcpc7t9wkDbiju0_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Plane", "plane_Sketch_FUuhlvZgLZiBthq_1_JWC")
origin = App.Vector(-558.79999999999995,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUuhlvZgLZiBthq_1_JWC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("Sketcher::SketchObject","Sketch_FUuhlvZgLZiBthq_1_JWC")
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUuhlvZgLZiBthq_1_JWC"), [""])
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC").addGeometry(Part.LineSegment(App.Vector(-1104.90000000000009,114.30000000000000,0.00000000000000),App.Vector(-996.95000000000005,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC").addGeometry(Part.LineSegment(App.Vector(-996.95000000000005,114.30000000000000,0.00000000000000),App.Vector(-996.95000000000005,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC").addGeometry(Part.LineSegment(App.Vector(-1104.90000000000009,38.10000000000000,0.00000000000000),App.Vector(-996.95000000000005,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC").addGeometry(Part.LineSegment(App.Vector(-1104.90000000000009,114.30000000000000,0.00000000000000),App.Vector(-1104.90000000000009,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Pad","Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC")
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").Profile = App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC")
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").Type = 4
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Plane", "plane_Sketch_FUuhlvZgLZiBthq_1_JWG")
origin = App.Vector(-558.79999999999995,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUuhlvZgLZiBthq_1_JWG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("Sketcher::SketchObject","Sketch_FUuhlvZgLZiBthq_1_JWG")
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUuhlvZgLZiBthq_1_JWG"), [""])
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG").addGeometry(Part.LineSegment(App.Vector(-146.04999999999995,114.30000000000000,0.00000000000000),App.Vector(-38.09999999999991,114.30000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG").addGeometry(Part.LineSegment(App.Vector(-38.09999999999991,114.30000000000000,0.00000000000000),App.Vector(-38.09999999999991,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG").addGeometry(Part.LineSegment(App.Vector(-146.04999999999995,38.10000000000000,0.00000000000000),App.Vector(-38.09999999999991,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG").addGeometry(Part.LineSegment(App.Vector(-146.04999999999995,114.30000000000000,0.00000000000000),App.Vector(-146.04999999999995,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Pad","Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG")
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").Profile = App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG")
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").Type = 4
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Plane", "plane_Sketch_FUuhlvZgLZiBthq_1_JWK")
origin = App.Vector(-558.79999999999995,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUuhlvZgLZiBthq_1_JWK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("Sketcher::SketchObject","Sketch_FUuhlvZgLZiBthq_1_JWK")
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUuhlvZgLZiBthq_1_JWK"), [""])
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK").addGeometry(Part.LineSegment(App.Vector(-1104.90000000000009,-38.10000000000000,0.00000000000000),App.Vector(-996.95000000000005,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK").addGeometry(Part.LineSegment(App.Vector(-996.95000000000005,-38.10000000000000,0.00000000000000),App.Vector(-996.95000000000005,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK").addGeometry(Part.LineSegment(App.Vector(-1104.90000000000009,38.10000000000000,0.00000000000000),App.Vector(-996.95000000000005,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK").addGeometry(Part.LineSegment(App.Vector(-1104.90000000000009,-38.10000000000000,0.00000000000000),App.Vector(-1104.90000000000009,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Pad","Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK")
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").Profile = App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK")
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").Type = 4
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Plane", "plane_Sketch_FUuhlvZgLZiBthq_1_JWO")
origin = App.Vector(-558.79999999999995,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FUuhlvZgLZiBthq_1_JWO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("Sketcher::SketchObject","Sketch_FUuhlvZgLZiBthq_1_JWO")
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FUuhlvZgLZiBthq_1_JWO"), [""])
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO").addGeometry(Part.LineSegment(App.Vector(-146.04999999999995,-38.10000000000000,0.00000000000000),App.Vector(-38.09999999999991,-38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO").addGeometry(Part.LineSegment(App.Vector(-38.09999999999991,-38.10000000000000,0.00000000000000),App.Vector(-38.09999999999991,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO").addGeometry(Part.LineSegment(App.Vector(-146.04999999999995,38.10000000000000,0.00000000000000),App.Vector(-38.09999999999991,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO").addGeometry(Part.LineSegment(App.Vector(-146.04999999999995,-38.10000000000000,0.00000000000000),App.Vector(-146.04999999999995,38.10000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FxuVYf0eZtv4g2d_0").newObject("PartDesign::Pad","Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO")
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").Profile = App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO")
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FUuhlvZgLZiBthq_1_JWO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").Type = 4
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FUuhlvZgLZiBthq_1_Fm46jNFzQevSehl_1_JWO").Offset = 0
App.ActiveDocument.recompute()

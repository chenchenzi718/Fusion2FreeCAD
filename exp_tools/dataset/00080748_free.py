import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00080748")
App.ActiveDocument.addObject("PartDesign::Body","Body_Ffl4W7V3USgoQMy_0")
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").Label = "Body_Ffl4W7V3USgoQMy_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Plane", "plane_Sketch_Ffl4W7V3USgoQMy_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ffl4W7V3USgoQMy_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("Sketcher::SketchObject","Sketch_Ffl4W7V3USgoQMy_0_JGC")
App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ffl4W7V3USgoQMy_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC").addGeometry(Part.LineSegment(App.Vector(67.50000000000000,90.00000000000000,0.00000000000000),App.Vector(-67.50000000000000,90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC").addGeometry(Part.LineSegment(App.Vector(-67.50000000000000,90.00000000000000,0.00000000000000),App.Vector(-67.50000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC").addGeometry(Part.LineSegment(App.Vector(67.50000000000000,-90.00000000000000,0.00000000000000),App.Vector(-67.50000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC").addGeometry(Part.LineSegment(App.Vector(67.50000000000000,90.00000000000000,0.00000000000000),App.Vector(67.50000000000000,-90.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Pad","Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC")
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC")
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").Length = 25.0
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ffl4W7V3USgoQMy_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ffl4W7V3USgoQMy_0_FPQeJMwQHpVjsh9_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Plane", "plane_Sketch_Fq1SB0x0UlFffAr_1_JJG")
origin = App.Vector(-17.68081000000000,-24.40264000000000,-90.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq1SB0x0UlFffAr_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("Sketcher::SketchObject","Sketch_Fq1SB0x0UlFffAr_1_JJG")
App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq1SB0x0UlFffAr_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG").addGeometry(Part.LineSegment(App.Vector(-49.81919000000000,0.59736000000000,0.00000000000000),App.Vector(-56.58895000000000,-4.18873000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG").addGeometry(Part.LineSegment(App.Vector(-42.15265000000000,24.40265000000000,0.00000000000000),App.Vector(-56.58895000000000,-4.18873000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG").addGeometry(Part.LineSegment(App.Vector(-44.42881999999999,0.59736000000000,0.00000000000000),App.Vector(-42.15265000000000,24.40265000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG").addGeometry(Part.LineSegment(App.Vector(-49.81919000000000,0.59736000000000,0.00000000000000),App.Vector(-44.42881999999999,0.59736000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Pad","Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG")
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG")
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").Length = 180.0
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").Type = 0
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Plane", "plane_Sketch_Fq1SB0x0UlFffAr_1_JJC")
origin = App.Vector(-17.68081000000000,-24.40264000000000,-90.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fq1SB0x0UlFffAr_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("Sketcher::SketchObject","Sketch_Fq1SB0x0UlFffAr_1_JJC")
App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fq1SB0x0UlFffAr_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC").addGeometry(Part.LineSegment(App.Vector(-49.81919000000000,0.59736000000000,0.00000000000000),App.Vector(-56.58895000000000,-4.18873000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC").addGeometry(Part.LineSegment(App.Vector(-85.18082000000000,-24.40264000000000,0.00000000000000),App.Vector(-56.58895000000000,-4.18873000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC").addGeometry(Part.LineSegment(App.Vector(-49.81919000000000,-24.40264000000000,0.00000000000000),App.Vector(-85.18082000000000,-24.40264000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC").addGeometry(Part.LineSegment(App.Vector(-49.81919000000000,-24.40264000000000,0.00000000000000),App.Vector(-49.81919000000000,0.59736000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Pad","Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC")
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC")
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").Length = 180.0
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fq1SB0x0UlFffAr_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").Type = 0
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fq1SB0x0UlFffAr_1_FDXKK8O9qQ4sZPZ_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Plane", "plane_Sketch_FbBCcBEfrwPJqRP_1_JNC")
origin = App.Vector(-88.56569999999999,-10.10695000000000,0.00000000000000)
x_axis=App.Vector(0.81654498000000,-0.57728181000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,0.99999999252008)
z_axis=App.Vector(-0.57728181000000,-0.81654498000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbBCcBEfrwPJqRP_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("Sketcher::SketchObject","Sketch_FbBCcBEfrwPJqRP_1_JNC")
App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbBCcBEfrwPJqRP_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC").addGeometry(Part.LineSegment(App.Vector(38.18835350974620,22.86985982893519,-0.00000244925190),App.Vector(17.50784220377880,22.86985982893519,0.00000133220941)),False)

App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC").addGeometry(Part.LineSegment(App.Vector(17.50784220377880,22.86985982893519,0.00000133220941),App.Vector(17.50784220377880,-19.41780985475627,0.00000133220941)),False)

App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC").addGeometry(Part.LineSegment(App.Vector(38.18835350974620,-19.41780985475627,-0.00000244925190),App.Vector(17.50784220377880,-19.41780985475627,0.00000133220941)),False)

App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC").addGeometry(Part.LineSegment(App.Vector(38.18835350974620,22.86985982893519,-0.00000244925190),App.Vector(38.18835350974620,-19.41780985475627,-0.00000244925190)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Pocket","Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC")
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC")
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Plane", "plane_Sketch_FbBCcBEfrwPJqRP_1_JNG")
origin = App.Vector(-88.56569999999999,-10.10695000000000,0.00000000000000)
x_axis=App.Vector(0.81654498000000,-0.57728181000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,0.99999999252008)
z_axis=App.Vector(-0.57728181000000,-0.81654498000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbBCcBEfrwPJqRP_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("Sketcher::SketchObject","Sketch_FbBCcBEfrwPJqRP_1_JNG")
App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbBCcBEfrwPJqRP_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-13.37671287105150,22.86985982893519,0.00000376686150),App.Vector(17.50784220377880,22.86985982893519,0.00000133220941)),False)

App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG").addGeometry(Part.LineSegment(App.Vector(17.50784220377880,22.86985982893519,0.00000133220941),App.Vector(17.50784220377880,-19.41780985475627,0.00000133220941)),False)

App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-13.37671287105150,-19.41780985475627,0.00000376686150),App.Vector(17.50784220377880,-19.41780985475627,0.00000133220941)),False)

App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG").addGeometry(Part.LineSegment(App.Vector(-13.37671287105150,22.86985982893519,0.00000376686150),App.Vector(-13.37671287105150,-19.41780985475627,0.00000376686150)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Pocket","Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG")
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG")
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbBCcBEfrwPJqRP_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbBCcBEfrwPJqRP_1_FaBm4qLTLUC3P7R_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Plane", "plane_Sketch_FdeRtQ2mC74jJJI_1_JRC")
origin = App.Vector(2.69518000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdeRtQ2mC74jJJI_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("Sketcher::SketchObject","Sketch_FdeRtQ2mC74jJJI_1_JRC")
App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdeRtQ2mC74jJJI_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC").addGeometry(Part.LineSegment(App.Vector(43.46776000000000,82.00000000000000,0.00000000000000),App.Vector(-22.57224000000000,82.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC").addGeometry(Part.LineSegment(App.Vector(-22.57224000000000,82.00000000000000,0.00000000000000),App.Vector(-22.57224000000000,51.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC").addGeometry(Part.LineSegment(App.Vector(43.46776000000000,51.00000000000000,0.00000000000000),App.Vector(-22.57224000000000,51.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC").addGeometry(Part.LineSegment(App.Vector(43.46776000000000,82.00000000000000,0.00000000000000),App.Vector(43.46776000000000,51.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Pocket","Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC")
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC")
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").Length = 25.0
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Plane", "plane_Sketch_FdeRtQ2mC74jJJI_1_JRG")
origin = App.Vector(2.69518000000000,-25.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdeRtQ2mC74jJJI_1_JRG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("Sketcher::SketchObject","Sketch_FdeRtQ2mC74jJJI_1_JRG")
App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdeRtQ2mC74jJJI_1_JRG"), [""])
App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG").addGeometry(Part.LineSegment(App.Vector(43.46776000000000,-51.00000000000000,0.00000000000000),App.Vector(-22.57224000000000,-51.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG").addGeometry(Part.LineSegment(App.Vector(-22.57224000000000,-51.00000000000000,0.00000000000000),App.Vector(-22.57224000000000,-82.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG").addGeometry(Part.LineSegment(App.Vector(43.46776000000000,-82.00000000000000,0.00000000000000),App.Vector(-22.57224000000000,-82.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG").addGeometry(Part.LineSegment(App.Vector(43.46776000000000,-51.00000000000000,0.00000000000000),App.Vector(43.46776000000000,-82.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Pocket","Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG")
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").Profile = App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG")
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").Length = 25.0
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdeRtQ2mC74jJJI_1_JRG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").Type = 4
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdeRtQ2mC74jJJI_1_F2ALav6JEteigWe_1_JRG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Plane", "plane_Sketch_FaatX0HNgSdlWA4_1_JXC")
origin = App.Vector(-67.05161000000000,-34.50960000000000,-54.70890000000000)
x_axis=App.Vector(0.45072230000000,-0.89266422000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000138550)
z_axis=App.Vector(-0.89266422000000,-0.45072230000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaatX0HNgSdlWA4_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("Sketcher::SketchObject","Sketch_FaatX0HNgSdlWA4_1_JXC")
App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaatX0HNgSdlWA4_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC").addGeometry(Part.LineSegment(App.Vector(-16.01463213295680,77.57876010748524,-0.00000203729399),App.Vector(16.01463213295680,77.57876010748524,0.00000203729400)),False)

App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC").addGeometry(Part.LineSegment(App.Vector(16.01463213295680,77.57876010748524,0.00000203729400),App.Vector(16.01463213295680,35.29109004889575,0.00000203729400)),False)

App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC").addGeometry(Part.LineSegment(App.Vector(-16.01463213295680,35.29109004889575,-0.00000203729399),App.Vector(16.01463213295680,35.29109004889575,0.00000203729400)),False)

App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC").addGeometry(Part.LineSegment(App.Vector(-16.01463213295680,77.57876010748524,-0.00000203729399),App.Vector(-16.01463213295680,35.29109004889575,-0.00000203729399)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Ffl4W7V3USgoQMy_0").newObject("PartDesign::Pocket","Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC")
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC")
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").Length = 10.0
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaatX0HNgSdlWA4_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaatX0HNgSdlWA4_1_FPG0TaxeLjlH3iD_1_JXC").Offset = 0
App.ActiveDocument.recompute()

import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00461706")
App.ActiveDocument.addObject("PartDesign::Body","Body_FgIJveWLIJfXNB1_0")
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").Label = "Body_FgIJveWLIJfXNB1_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FgIJveWLIJfXNB1_0_JHC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FgIJveWLIJfXNB1_0_JHC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FgIJveWLIJfXNB1_0_JHC")
App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FgIJveWLIJfXNB1_0_JHC"), [""])
App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC").addGeometry(Part.LineSegment(App.Vector(-82.44346000000000,427.39761999999996,0.00000000000000),App.Vector(133.45654000000002,427.39761999999996,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC").addGeometry(Part.LineSegment(App.Vector(133.45654000000002,427.39761999999996,0.00000000000000),App.Vector(133.45654000000002,-29.80238000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC").addGeometry(Part.LineSegment(App.Vector(-82.44346000000000,-29.80238000000000,0.00000000000000),App.Vector(133.45654000000002,-29.80238000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC").addGeometry(Part.LineSegment(App.Vector(-82.44346000000000,427.39761999999996,0.00000000000000),App.Vector(-82.44346000000000,-29.80238000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pad","Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC")
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").Profile = App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC")
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").Length = 19.05
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FgIJveWLIJfXNB1_0_JHC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").Type = 4
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FgIJveWLIJfXNB1_0_Ftu2bIaYv4cP6Cp_0_JHC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FRyAwkcB0Afsw4W_1_JMC")
origin = App.Vector(25.50654000000000,-19.05000000000000,198.79761999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRyAwkcB0Afsw4W_1_JMC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FRyAwkcB0Afsw4W_1_JMC")
App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRyAwkcB0Afsw4W_1_JMC"), [""])
App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC").addGeometry(Part.LineSegment(App.Vector(-94.87845000000000,-44.89605000000002,0.00000000000000),App.Vector(95.62155000000000,-44.89605000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC").addGeometry(Part.LineSegment(App.Vector(95.62155000000000,-44.89605000000002,0.00000000000000),App.Vector(95.62155000000000,-209.99605000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC").addGeometry(Part.LineSegment(App.Vector(-94.87845000000000,-209.99605000000003,0.00000000000000),App.Vector(95.62155000000000,-209.99605000000003,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC").addGeometry(Part.LineSegment(App.Vector(-94.87845000000000,-44.89605000000002,0.00000000000000),App.Vector(-94.87845000000000,-209.99605000000003,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pocket","Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC")
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").Profile = App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC")
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRyAwkcB0Afsw4W_1_JMC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").Type = 4
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRyAwkcB0Afsw4W_1_Fo6ZpLtFSTEQu5X_1_JMC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FmczSDdx9QbFUpl_1_JQK")
origin = App.Vector(25.50654000000000,-19.05000000000000,198.79761999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FmczSDdx9QbFUpl_1_JQK")
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQK"), [""])
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK").addGeometry(Part.LineSegment(App.Vector(-103.83239999999999,221.90028000000001,0.00000000000000),App.Vector(99.36760000000000,221.90028000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK").addGeometry(Part.LineSegment(App.Vector(99.36760000000000,221.90028000000001,0.00000000000000),App.Vector(99.36760000000000,171.10028000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK").addGeometry(Part.LineSegment(App.Vector(-103.83239999999999,171.10028000000000,0.00000000000000),App.Vector(99.36760000000000,171.10028000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK").addGeometry(Part.LineSegment(App.Vector(-103.83239999999999,221.90028000000001,0.00000000000000),App.Vector(-103.83239999999999,171.10028000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pocket","Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").Profile = App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").Length = 7.62
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").Type = 4
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FmczSDdx9QbFUpl_1_JQS")
origin = App.Vector(25.50654000000000,-19.05000000000000,198.79761999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FmczSDdx9QbFUpl_1_JQS")
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQS"), [""])
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQS").addGeometry(Part.Circle(App.Vector(-86.89416999999999,138.70286999999999,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.24000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pocket","Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").Profile = App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQS")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").Length = 7.62
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").Type = 4
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FmczSDdx9QbFUpl_1_JQO")
origin = App.Vector(25.50654000000000,-19.05000000000000,198.79761999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FmczSDdx9QbFUpl_1_JQO")
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQO"), [""])
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO").addGeometry(Part.LineSegment(App.Vector(-60.13009000000000,143.11024000000000,0.00000000000000),App.Vector(92.26991000000001,143.11024000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO").addGeometry(Part.LineSegment(App.Vector(92.26991000000001,143.11024000000000,0.00000000000000),App.Vector(92.26991000000001,132.95024000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO").addGeometry(Part.LineSegment(App.Vector(-60.13009000000000,132.95024000000001,0.00000000000000),App.Vector(92.26991000000001,132.95024000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO").addGeometry(Part.LineSegment(App.Vector(-60.13009000000000,143.11024000000000,0.00000000000000),App.Vector(-60.13009000000000,132.95024000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pocket","Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").Profile = App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").Length = 7.62
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").Type = 4
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FmczSDdx9QbFUpl_1_JQG")
origin = App.Vector(25.50654000000000,-19.05000000000000,198.79761999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FmczSDdx9QbFUpl_1_JQG")
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQG"), [""])
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG").addGeometry(Part.LineSegment(App.Vector(-101.14200000000001,99.23627000000002,0.00000000000000),App.Vector(0.45800000000000,99.23627000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG").addGeometry(Part.LineSegment(App.Vector(0.45800000000000,99.23627000000002,0.00000000000000),App.Vector(0.45800000000000,111.93627000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG").addGeometry(Part.LineSegment(App.Vector(-101.14200000000001,111.93627000000001,0.00000000000000),App.Vector(0.45800000000000,111.93627000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG").addGeometry(Part.LineSegment(App.Vector(-101.14200000000001,99.23627000000002,0.00000000000000),App.Vector(-101.14200000000001,111.93627000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pocket","Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").Profile = App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").Length = 7.62
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").Type = 4
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FmczSDdx9QbFUpl_1_JQa")
origin = App.Vector(25.50654000000000,-19.05000000000000,198.79761999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FmczSDdx9QbFUpl_1_JQa")
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQa"), [""])
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQa").addGeometry(Part.Circle(App.Vector(27.26049000000000,103.36764999999998,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pocket","Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").Profile = App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQa")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").Length = 7.62
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").Type = 4
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FmczSDdx9QbFUpl_1_JQW")
origin = App.Vector(25.50654000000000,-19.05000000000000,198.79761999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FmczSDdx9QbFUpl_1_JQW")
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQW"), [""])
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQW").addGeometry(Part.Circle(App.Vector(62.42299000000001,102.90699999999997,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),6.35000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pocket","Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").Profile = App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQW")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").Length = 7.62
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").Type = 4
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FmczSDdx9QbFUpl_1_JQe")
origin = App.Vector(25.50654000000000,-19.05000000000000,198.79761999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FmczSDdx9QbFUpl_1_JQe")
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQe"), [""])
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQe").addGeometry(Part.Circle(App.Vector(92.59727000000001,100.68569999999998,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),9.52500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pocket","Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").Profile = App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQe")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").Length = 7.62
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").Type = 4
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Plane", "plane_Sketch_FmczSDdx9QbFUpl_1_JQC")
origin = App.Vector(25.50654000000000,-19.05000000000000,198.79761999999999)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("Sketcher::SketchObject","Sketch_FmczSDdx9QbFUpl_1_JQC")
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FmczSDdx9QbFUpl_1_JQC"), [""])
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC").addGeometry(Part.LineSegment(App.Vector(-105.21860999999998,63.25565000000000,0.00000000000000),App.Vector(104.33139000000000,63.25565000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC").addGeometry(Part.LineSegment(App.Vector(104.33139000000000,63.25565000000000,0.00000000000000),App.Vector(104.33139000000000,-12.94435000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC").addGeometry(Part.LineSegment(App.Vector(-105.21860999999998,-12.94435000000002,0.00000000000000),App.Vector(104.33139000000000,-12.94435000000002,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC").addGeometry(Part.LineSegment(App.Vector(-105.21860999999998,63.25565000000000,0.00000000000000),App.Vector(-105.21860999999998,-12.94435000000002,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FgIJveWLIJfXNB1_0").newObject("PartDesign::Pocket","Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").Profile = App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC")
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").Length = 7.62
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FmczSDdx9QbFUpl_1_JQC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").Type = 4
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FmczSDdx9QbFUpl_1_FQcBGFiZuuo17un_1_JQC").Offset = 0
App.ActiveDocument.recompute()

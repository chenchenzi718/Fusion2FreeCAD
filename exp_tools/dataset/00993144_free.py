import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00993144")
App.ActiveDocument.addObject("PartDesign::Body","Body_FpIXIinvFw0BWML_0")
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").Label = "Body_FpIXIinvFw0BWML_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_FpIXIinvFw0BWML_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpIXIinvFw0BWML_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_FpIXIinvFw0BWML_0_JGC")
App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpIXIinvFw0BWML_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC").addGeometry(Part.LineSegment(App.Vector(37.90209000000000,107.87771000000001,0.00000000000000),App.Vector(37.90209000000000,-44.52229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC").addGeometry(Part.LineSegment(App.Vector(37.90209000000000,-44.52229000000000,0.00000000000000),App.Vector(37.90209000000000,-57.22229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC").addGeometry(Part.LineSegment(App.Vector(-9.19077000000000,-38.17229000000000,0.00000000000000),App.Vector(37.90209000000000,-57.22229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC").addGeometry(Part.LineSegment(App.Vector(-9.19077000000000,88.82771000000001,0.00000000000000),App.Vector(-9.19077000000000,-38.17229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC").addGeometry(Part.LineSegment(App.Vector(37.90209000000000,107.87771000000001,0.00000000000000),App.Vector(-9.19077000000000,88.82771000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pad","Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC")
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC")
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").Length = 127.0
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_FvaquyQNrNGuAXU_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_FpIXIinvFw0BWML_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpIXIinvFw0BWML_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_FpIXIinvFw0BWML_0_JGG")
App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpIXIinvFw0BWML_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG").addGeometry(Part.LineSegment(App.Vector(37.90209000000000,-57.22229000000000,0.00000000000000),App.Vector(88.70209000000000,-57.22229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG").addGeometry(Part.LineSegment(App.Vector(88.70209000000000,-57.22229000000000,0.00000000000000),App.Vector(88.70209000000000,-44.52229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG").addGeometry(Part.LineSegment(App.Vector(37.90209000000000,-44.52229000000000,0.00000000000000),App.Vector(88.70209000000000,-44.52229000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG").addGeometry(Part.LineSegment(App.Vector(37.90209000000000,-44.52229000000000,0.00000000000000),App.Vector(37.90209000000000,-57.22229000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pad","Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG")
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG")
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").Length = 38.1
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpIXIinvFw0BWML_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpIXIinvFw0BWML_0_F6vEqghb91ZXEtl_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_F2XpUr4iR8iRPbq_1_JLC")
origin = App.Vector(63.50000000000000,37.90209000000000,25.32771000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2XpUr4iR8iRPbq_1_JLC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_F2XpUr4iR8iRPbq_1_JLC")
App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2XpUr4iR8iRPbq_1_JLC"), [""])
App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-69.84999999999999,0.00000000000000),App.Vector(-63.50000000000000,-69.84999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,-82.55000000000000,0.00000000000000),App.Vector(-63.50000000000000,-69.84999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC").addGeometry(Part.LineSegment(App.Vector(-63.50000000000000,-82.55000000000000,0.00000000000000),App.Vector(0.00000000000000,-82.55000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-69.84999999999999,0.00000000000000),App.Vector(0.00000000000000,-82.55000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pad","Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC")
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").Profile = App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC")
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").Type = 4
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_F2XpUr4iR8iRPbq_1_JLG")
origin = App.Vector(63.50000000000000,37.90209000000000,25.32771000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2XpUr4iR8iRPbq_1_JLG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_F2XpUr4iR8iRPbq_1_JLG")
App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2XpUr4iR8iRPbq_1_JLG"), [""])
App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,69.84999999999999,0.00000000000000),App.Vector(63.50000000000000,69.84999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,82.55000000000000,0.00000000000000),App.Vector(63.50000000000000,69.84999999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG").addGeometry(Part.LineSegment(App.Vector(63.50000000000000,82.55000000000000,0.00000000000000),App.Vector(25.40000000000000,82.55000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG").addGeometry(Part.LineSegment(App.Vector(25.40000000000000,69.84999999999999,0.00000000000000),App.Vector(25.40000000000000,82.55000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pad","Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG")
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").Profile = App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG")
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2XpUr4iR8iRPbq_1_JLG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").Type = 4
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2XpUr4iR8iRPbq_1_F8KJDDJ2DPre47A_1_JLG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_FW1P5dECDzaG98G_1_JQG")
origin = App.Vector(19.05000000000000,88.70209000000000,101.52771000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FW1P5dECDzaG98G_1_JQG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_FW1P5dECDzaG98G_1_JQG")
App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FW1P5dECDzaG98G_1_JQG"), [""])
App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQG").addGeometry(Part.Circle(App.Vector(11.43000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pocket","Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG")
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").Profile = App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQG")
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").Type = 4
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_FW1P5dECDzaG98G_1_JQC")
origin = App.Vector(19.05000000000000,88.70209000000000,101.52771000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FW1P5dECDzaG98G_1_JQC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_FW1P5dECDzaG98G_1_JQC")
App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FW1P5dECDzaG98G_1_JQC"), [""])
App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQC").addGeometry(Part.Circle(App.Vector(-11.43000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pocket","Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC")
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").Profile = App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQC")
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FW1P5dECDzaG98G_1_JQC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").Type = 4
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FW1P5dECDzaG98G_1_FqN63HsriltBhs8_1_JQC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_FRYOl7TZvfcO1uJ_1_JVC")
origin = App.Vector(19.05000000000000,88.70209000000000,-50.87229000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRYOl7TZvfcO1uJ_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_FRYOl7TZvfcO1uJ_1_JVC")
App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRYOl7TZvfcO1uJ_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVC").addGeometry(Part.Circle(App.Vector(-11.43000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pocket","Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC")
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVC")
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_FRYOl7TZvfcO1uJ_1_JVG")
origin = App.Vector(19.05000000000000,88.70209000000000,-50.87229000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FRYOl7TZvfcO1uJ_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_FRYOl7TZvfcO1uJ_1_JVG")
App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FRYOl7TZvfcO1uJ_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVG").addGeometry(Part.Circle(App.Vector(11.43000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pocket","Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG")
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVG")
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FRYOl7TZvfcO1uJ_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FRYOl7TZvfcO1uJ_1_FVv8R000uWgFagf_1_JVG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_FaYZ0Rx55wVq4TN_1_JZC")
origin = App.Vector(95.25000000000000,88.70209000000000,-50.87229000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaYZ0Rx55wVq4TN_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_FaYZ0Rx55wVq4TN_1_JZC")
App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaYZ0Rx55wVq4TN_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZC").addGeometry(Part.Circle(App.Vector(24.13000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pocket","Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC")
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZC")
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Plane", "plane_Sketch_FaYZ0Rx55wVq4TN_1_JZG")
origin = App.Vector(95.25000000000000,88.70209000000000,-50.87229000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FaYZ0Rx55wVq4TN_1_JZG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("Sketcher::SketchObject","Sketch_FaYZ0Rx55wVq4TN_1_JZG")
App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FaYZ0Rx55wVq4TN_1_JZG"), [""])
App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZG").addGeometry(Part.Circle(App.Vector(-24.13000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.81000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FpIXIinvFw0BWML_0").newObject("PartDesign::Pocket","Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG")
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").Profile = App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZG")
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FaYZ0Rx55wVq4TN_1_JZG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").Type = 4
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FaYZ0Rx55wVq4TN_1_FXYtRMBqiG4n152_1_JZG").Offset = 0
App.ActiveDocument.recompute()

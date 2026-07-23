import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00903714")
App.ActiveDocument.addObject("PartDesign::Body","Body_F3EhkqxFQUXyF1Q_0")
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").Label = "Body_F3EhkqxFQUXyF1Q_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Plane", "plane_Sketch_F3EhkqxFQUXyF1Q_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3EhkqxFQUXyF1Q_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("Sketcher::SketchObject","Sketch_F3EhkqxFQUXyF1Q_0_JGC")
App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3EhkqxFQUXyF1Q_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC").addGeometry(Part.LineSegment(App.Vector(88.90000000000001,-9.52500000000000,0.00000000000000),App.Vector(-88.90000000000001,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC").addGeometry(Part.LineSegment(App.Vector(-88.90000000000001,-9.52500000000000,0.00000000000000),App.Vector(-88.90000000000001,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC").addGeometry(Part.LineSegment(App.Vector(88.90000000000001,9.52500000000000,0.00000000000000),App.Vector(-88.90000000000001,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC").addGeometry(Part.LineSegment(App.Vector(88.90000000000001,-9.52500000000000,0.00000000000000),App.Vector(88.90000000000001,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Pad","Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC")
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC")
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3EhkqxFQUXyF1Q_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F3EhkqxFQUXyF1Q_0_Fr2n3RkoUpz5Dy8_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Plane", "plane_Sketch_Ftd6f5yfY5kZWhW_1_JJO")
origin = App.Vector(-34.92500000000000,-0.00000000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftd6f5yfY5kZWhW_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("Sketcher::SketchObject","Sketch_Ftd6f5yfY5kZWhW_1_JJO")
App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftd6f5yfY5kZWhW_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,-6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,-6.35000000000000,0.00000000000000),App.Vector(-22.22500000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Pad","Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO")
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO")
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").Length = 31.75
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").Type = 0
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").Reversed = 1
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Plane", "plane_Sketch_Ftd6f5yfY5kZWhW_1_JJS")
origin = App.Vector(-34.92500000000000,-0.00000000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftd6f5yfY5kZWhW_1_JJS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("Sketcher::SketchObject","Sketch_Ftd6f5yfY5kZWhW_1_JJS")
App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftd6f5yfY5kZWhW_1_JJS"), [""])
App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,9.52500000000000,0.00000000000000),App.Vector(-28.57500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,9.52500000000000,0.00000000000000),App.Vector(-28.57500000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,15.87500000000000,0.00000000000000),App.Vector(-22.22500000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,15.87500000000000,0.00000000000000),App.Vector(-60.32500000000000,15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-60.32500000000000,-15.87500000000000,0.00000000000000),App.Vector(-60.32500000000000,15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,-15.87500000000000,0.00000000000000),App.Vector(-60.32500000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,-15.87500000000000,0.00000000000000),App.Vector(-22.22500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-22.22500000000000,-6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,-9.52500000000000,0.00000000000000),App.Vector(-28.57500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,-9.52500000000000,0.00000000000000),App.Vector(-28.57500000000000,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,-6.35000000000000,0.00000000000000),App.Vector(-53.97500000000001,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,6.35000000000000,0.00000000000000),App.Vector(-53.97500000000001,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,6.35000000000000,0.00000000000000),App.Vector(-53.97500000000001,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Pad","Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS")
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").Profile = App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS")
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").Length = 31.75
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftd6f5yfY5kZWhW_1_JJS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").Type = 0
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").Reversed = 1
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftd6f5yfY5kZWhW_1_FghMgCBydXmGJ0V_1_JJS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FfVoDzqRijlbgPi_1_JNC")
origin = App.Vector(-34.92500000000000,-0.00000000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfVoDzqRijlbgPi_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("Sketcher::SketchObject","Sketch_FfVoDzqRijlbgPi_1_JNC")
App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfVoDzqRijlbgPi_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,9.52500000000000,0.00000000000000),App.Vector(-28.57500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,9.52500000000000,0.00000000000000),App.Vector(-28.57500000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,9.52500000000000,0.00000000000000),App.Vector(-53.97500000000001,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Pocket","Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC")
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC")
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").Length = 127.0
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FfVoDzqRijlbgPi_1_JNG")
origin = App.Vector(-34.92500000000000,-0.00000000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfVoDzqRijlbgPi_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("Sketcher::SketchObject","Sketch_FfVoDzqRijlbgPi_1_JNG")
App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfVoDzqRijlbgPi_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,-9.52500000000000,0.00000000000000),App.Vector(-28.57500000000000,-9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,-9.52500000000000,0.00000000000000),App.Vector(-28.57500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,-6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,-9.52500000000000,0.00000000000000),App.Vector(-53.97500000000001,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Pocket","Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG")
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG")
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").Length = 127.0
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FfVoDzqRijlbgPi_1_JNO")
origin = App.Vector(-34.92500000000000,-0.00000000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfVoDzqRijlbgPi_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("Sketcher::SketchObject","Sketch_FfVoDzqRijlbgPi_1_JNO")
App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfVoDzqRijlbgPi_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,6.35000000000000,0.00000000000000),App.Vector(-53.97500000000001,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,-6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO").addGeometry(Part.LineSegment(App.Vector(-28.57500000000000,6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,-6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO").addGeometry(Part.LineSegment(App.Vector(-53.97500000000001,6.35000000000000,0.00000000000000),App.Vector(-28.57500000000000,6.35000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Pocket","Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO")
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO")
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").Length = 127.0
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfVoDzqRijlbgPi_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfVoDzqRijlbgPi_1_FYROpZCc4APen54_1_JNO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Plane", "plane_Sketch_Fm67FgZgnfF5edo_1_JRC")
origin = App.Vector(-34.92500000000000,-0.00000000000000,9.52500000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,-0.00000000000000)
z_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fm67FgZgnfF5edo_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("Sketcher::SketchObject","Sketch_Fm67FgZgnfF5edo_1_JRC")
App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fm67FgZgnfF5edo_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC").addGeometry(Part.LineSegment(App.Vector(-47.62500000000000,9.52500000000000,0.00000000000000),App.Vector(-34.92500000000000,9.52500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,9.52500000000000,0.00000000000000),App.Vector(-34.92500000000000,4.44500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC").addGeometry(Part.LineSegment(App.Vector(-34.92500000000000,4.44500000000000,0.00000000000000),App.Vector(-47.62500000000000,4.44500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC").addGeometry(Part.LineSegment(App.Vector(-47.62500000000000,9.52500000000000,0.00000000000000),App.Vector(-47.62500000000000,4.44500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Pad","Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC")
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC")
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").Length = 31.75
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fm67FgZgnfF5edo_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").Reversed = 1
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fm67FgZgnfF5edo_1_FJIKqdfOqv3wmUF_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Plane", "plane_Sketch_FPZ1wlIK3CgBetO_1_JVC")
origin = App.Vector(-15.87500000000000,-6.35000000000000,-6.35000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FPZ1wlIK3CgBetO_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("Sketcher::SketchObject","Sketch_FPZ1wlIK3CgBetO_1_JVC")
App.ActiveDocument.getObject("Sketch_FPZ1wlIK3CgBetO_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FPZ1wlIK3CgBetO_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FPZ1wlIK3CgBetO_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FPZ1wlIK3CgBetO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-41.27500000000000,-3.17500000000000,0.00000000000000),App.Vector(-15.95414000000000,-3.17500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPZ1wlIK3CgBetO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-15.95414000000000,-3.17500000000000,0.00000000000000),App.Vector(-41.27500000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FPZ1wlIK3CgBetO_1_JVC").addGeometry(Part.LineSegment(App.Vector(-41.27500000000000,-3.17500000000000,0.00000000000000),App.Vector(-41.27500000000000,-15.87500000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FPZ1wlIK3CgBetO_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FPZ1wlIK3CgBetO_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F3EhkqxFQUXyF1Q_0").newObject("PartDesign::Pad","Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC")
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FPZ1wlIK3CgBetO_1_JVC")
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FPZ1wlIK3CgBetO_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").Type = 0
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FPZ1wlIK3CgBetO_1_FbjDpASHAp9FFry_1_JVC").Offset = 0
App.ActiveDocument.recompute()

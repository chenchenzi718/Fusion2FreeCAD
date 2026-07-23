import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00851739")
App.ActiveDocument.addObject("PartDesign::Body","Body_FR4YRN3kHPuI7Hz_0")
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").Label = "Body_FR4YRN3kHPuI7Hz_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Plane", "plane_Sketch_FR4YRN3kHPuI7Hz_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FR4YRN3kHPuI7Hz_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("Sketcher::SketchObject","Sketch_FR4YRN3kHPuI7Hz_0_JGC")
App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FR4YRN3kHPuI7Hz_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC").addGeometry(Part.LineSegment(App.Vector(-26.11120000000000,-18.79600000000000,0.00000000000000),App.Vector(26.11120000000000,-18.79600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC").addGeometry(Part.LineSegment(App.Vector(26.11120000000000,-18.79600000000000,0.00000000000000),App.Vector(26.11120000000000,18.79600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC").addGeometry(Part.LineSegment(App.Vector(-26.11120000000000,18.79600000000000,0.00000000000000),App.Vector(26.11120000000000,18.79600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC").addGeometry(Part.LineSegment(App.Vector(-26.11120000000000,-18.79600000000000,0.00000000000000),App.Vector(-26.11120000000000,18.79600000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Pad","Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC")
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC")
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FR4YRN3kHPuI7Hz_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FR4YRN3kHPuI7Hz_0_FiTWRabIVfxIQ26_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Plane", "plane_Sketch_FFNsKrZYmLdYECD_1_JJC")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFNsKrZYmLdYECD_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("Sketcher::SketchObject","Sketch_FFNsKrZYmLdYECD_1_JJC")
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFNsKrZYmLdYECD_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC").addGeometry(Part.LineSegment(App.Vector(-24.84120000000000,-5.08000000000000,0.00000000000000),App.Vector(-14.68120000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC").addGeometry(Part.LineSegment(App.Vector(-14.68120000000000,-5.08000000000000,0.00000000000000),App.Vector(-14.68120000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC").addGeometry(Part.LineSegment(App.Vector(-24.84120000000000,5.08000000000000,0.00000000000000),App.Vector(-14.68120000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC").addGeometry(Part.LineSegment(App.Vector(-24.84120000000000,-5.08000000000000,0.00000000000000),App.Vector(-24.84120000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Pocket","Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC")
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC")
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Plane", "plane_Sketch_FFNsKrZYmLdYECD_1_JJG")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFNsKrZYmLdYECD_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("Sketcher::SketchObject","Sketch_FFNsKrZYmLdYECD_1_JJG")
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFNsKrZYmLdYECD_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG").addGeometry(Part.LineSegment(App.Vector(-12.14120000000000,-5.08000000000000,0.00000000000000),App.Vector(-1.98120000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG").addGeometry(Part.LineSegment(App.Vector(-1.98120000000000,-5.08000000000000,0.00000000000000),App.Vector(-1.98120000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG").addGeometry(Part.LineSegment(App.Vector(-12.14120000000000,5.08000000000000,0.00000000000000),App.Vector(-1.98120000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG").addGeometry(Part.LineSegment(App.Vector(-12.14120000000000,-5.08000000000000,0.00000000000000),App.Vector(-12.14120000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Pocket","Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG")
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG")
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Plane", "plane_Sketch_FFNsKrZYmLdYECD_1_JJK")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFNsKrZYmLdYECD_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("Sketcher::SketchObject","Sketch_FFNsKrZYmLdYECD_1_JJK")
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFNsKrZYmLdYECD_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK").addGeometry(Part.LineSegment(App.Vector(10.71880000000000,-5.08000000000000,0.00000000000000),App.Vector(0.55880000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK").addGeometry(Part.LineSegment(App.Vector(0.55880000000000,-5.08000000000000,0.00000000000000),App.Vector(0.55880000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK").addGeometry(Part.LineSegment(App.Vector(10.71880000000000,5.08000000000000,0.00000000000000),App.Vector(0.55880000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK").addGeometry(Part.LineSegment(App.Vector(10.71880000000000,-5.08000000000000,0.00000000000000),App.Vector(10.71880000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Pocket","Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK")
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK")
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Plane", "plane_Sketch_FFNsKrZYmLdYECD_1_JJO")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FFNsKrZYmLdYECD_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("Sketcher::SketchObject","Sketch_FFNsKrZYmLdYECD_1_JJO")
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FFNsKrZYmLdYECD_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO").addGeometry(Part.LineSegment(App.Vector(24.13000000000000,-5.08000000000000,0.00000000000000),App.Vector(13.97000000000000,-5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO").addGeometry(Part.LineSegment(App.Vector(13.97000000000000,-5.08000000000000,0.00000000000000),App.Vector(13.97000000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO").addGeometry(Part.LineSegment(App.Vector(24.13000000000000,5.08000000000000,0.00000000000000),App.Vector(13.97000000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO").addGeometry(Part.LineSegment(App.Vector(24.13000000000000,-5.08000000000000,0.00000000000000),App.Vector(24.13000000000000,5.08000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Pocket","Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO")
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO")
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FFNsKrZYmLdYECD_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FFNsKrZYmLdYECD_1_Fqln3eLq5KVJtqG_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Plane", "plane_Sketch_FU2zikm5Qgw5Aoh_1_JNC")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FU2zikm5Qgw5Aoh_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("Sketcher::SketchObject","Sketch_FU2zikm5Qgw5Aoh_1_JNC")
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FU2zikm5Qgw5Aoh_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNC").addGeometry(Part.Circle(App.Vector(-21.86940000000000,14.22400000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Pocket","Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC")
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNC")
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Plane", "plane_Sketch_FU2zikm5Qgw5Aoh_1_JNG")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FU2zikm5Qgw5Aoh_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("Sketcher::SketchObject","Sketch_FU2zikm5Qgw5Aoh_1_JNG")
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FU2zikm5Qgw5Aoh_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNG").addGeometry(Part.Circle(App.Vector(21.18360000000000,-13.51280000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Pocket","Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG")
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNG")
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Plane", "plane_Sketch_FU2zikm5Qgw5Aoh_1_JNK")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FU2zikm5Qgw5Aoh_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("Sketcher::SketchObject","Sketch_FU2zikm5Qgw5Aoh_1_JNK")
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FU2zikm5Qgw5Aoh_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNK").addGeometry(Part.Circle(App.Vector(21.18360000000000,14.22400000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Pocket","Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK")
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNK")
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Plane", "plane_Sketch_FU2zikm5Qgw5Aoh_1_JNO")
origin = App.Vector(-0.00000000000000,0.00000000000000,-0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FU2zikm5Qgw5Aoh_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("Sketcher::SketchObject","Sketch_FU2zikm5Qgw5Aoh_1_JNO")
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FU2zikm5Qgw5Aoh_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNO").addGeometry(Part.Circle(App.Vector(-21.86940000000000,-13.51280000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FR4YRN3kHPuI7Hz_0").newObject("PartDesign::Pocket","Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO")
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNO")
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FU2zikm5Qgw5Aoh_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FU2zikm5Qgw5Aoh_1_FbfriWvhtDLT6Le_1_JNO").Offset = 0
App.ActiveDocument.recompute()

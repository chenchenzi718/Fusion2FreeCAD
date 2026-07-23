import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00880440")
App.ActiveDocument.addObject("PartDesign::Body","Body_F41w51GSlLkzJ9k_0")
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").Label = "Body_F41w51GSlLkzJ9k_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Plane", "plane_Sketch_F41w51GSlLkzJ9k_0_JGG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F41w51GSlLkzJ9k_0_JGG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("Sketcher::SketchObject","Sketch_F41w51GSlLkzJ9k_0_JGG")
App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F41w51GSlLkzJ9k_0_JGG"), [""])
App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG").addGeometry(Part.LineSegment(App.Vector(3000.00000000000000,5000.00000000000000,0.00000000000000),App.Vector(3000.00000000000000,-3000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG").addGeometry(Part.LineSegment(App.Vector(3000.00000000000000,-3000.00000000000000,0.00000000000000),App.Vector(16000.00000000000000,-3000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG").addGeometry(Part.LineSegment(App.Vector(16000.00000000000000,5000.00000000000000,0.00000000000000),App.Vector(16000.00000000000000,-3000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG").addGeometry(Part.LineSegment(App.Vector(3000.00000000000000,5000.00000000000000,0.00000000000000),App.Vector(16000.00000000000000,5000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Pad","Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG")
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").Profile = App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG")
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").Length = 3000.0
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").Type = 4
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Plane", "plane_Sketch_F41w51GSlLkzJ9k_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F41w51GSlLkzJ9k_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("Sketcher::SketchObject","Sketch_F41w51GSlLkzJ9k_0_JGC")
App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F41w51GSlLkzJ9k_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC").addGeometry(Part.LineSegment(App.Vector(3000.00000000000000,-5000.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,-5000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC").addGeometry(Part.LineSegment(App.Vector(-3000.00000000000000,-5000.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,5000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC").addGeometry(Part.LineSegment(App.Vector(3000.00000000000000,5000.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,5000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC").addGeometry(Part.LineSegment(App.Vector(3000.00000000000000,5000.00000000000000,0.00000000000000),App.Vector(3000.00000000000000,-3000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC").addGeometry(Part.LineSegment(App.Vector(3000.00000000000000,-5000.00000000000000,0.00000000000000),App.Vector(3000.00000000000000,-3000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Pad","Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC")
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC")
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").Length = 3000.0
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F41w51GSlLkzJ9k_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F41w51GSlLkzJ9k_0_FsJNhjWPjTQchHP_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Plane", "plane_Sketch_FEktCdYqytDrFRn_1_JJG")
origin = App.Vector(13000.00000000000000,-1500.00000000000000,3000.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEktCdYqytDrFRn_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("Sketcher::SketchObject","Sketch_FEktCdYqytDrFRn_1_JJG")
App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEktCdYqytDrFRn_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG").addGeometry(Part.LineSegment(App.Vector(-10000.00000000000000,-3500.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,-3500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG").addGeometry(Part.LineSegment(App.Vector(-3000.00000000000000,-3500.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,-1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG").addGeometry(Part.LineSegment(App.Vector(-10000.00000000000000,-1500.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,-1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG").addGeometry(Part.LineSegment(App.Vector(-10000.00000000000000,-3500.00000000000000,0.00000000000000),App.Vector(-10000.00000000000000,-1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Pad","Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG")
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG")
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").Length = 3000.0
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Plane", "plane_Sketch_FEktCdYqytDrFRn_1_JJO")
origin = App.Vector(13000.00000000000000,-1500.00000000000000,3000.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEktCdYqytDrFRn_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("Sketcher::SketchObject","Sketch_FEktCdYqytDrFRn_1_JJO")
App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEktCdYqytDrFRn_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").addGeometry(Part.LineSegment(App.Vector(-16000.00000000000000,6500.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,6500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").addGeometry(Part.LineSegment(App.Vector(-3000.00000000000000,6500.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").addGeometry(Part.LineSegment(App.Vector(-3000.00000000000000,1500.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,-1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").addGeometry(Part.LineSegment(App.Vector(-10000.00000000000000,-1500.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,-1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").addGeometry(Part.LineSegment(App.Vector(-10000.00000000000000,-3500.00000000000000,0.00000000000000),App.Vector(-10000.00000000000000,-1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").addGeometry(Part.LineSegment(App.Vector(-10000.00000000000000,-3500.00000000000000,0.00000000000000),App.Vector(-16000.00000000000000,-3500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").addGeometry(Part.LineSegment(App.Vector(-16000.00000000000000,-3500.00000000000000,0.00000000000000),App.Vector(-16000.00000000000000,6500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Pad","Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO")
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO")
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").Length = 3000.0
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Plane", "plane_Sketch_FEktCdYqytDrFRn_1_JJC")
origin = App.Vector(13000.00000000000000,-1500.00000000000000,3000.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FEktCdYqytDrFRn_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("Sketcher::SketchObject","Sketch_FEktCdYqytDrFRn_1_JJC")
App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FEktCdYqytDrFRn_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC").addGeometry(Part.LineSegment(App.Vector(3000.00000000000000,6500.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,6500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC").addGeometry(Part.LineSegment(App.Vector(-3000.00000000000000,6500.00000000000000,0.00000000000000),App.Vector(-3000.00000000000000,1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC").addGeometry(Part.LineSegment(App.Vector(-3000.00000000000000,1500.00000000000000,0.00000000000000),App.Vector(3000.00000000000000,1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC").addGeometry(Part.LineSegment(App.Vector(3000.00000000000000,6500.00000000000000,0.00000000000000),App.Vector(3000.00000000000000,1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Pad","Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC")
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC")
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").Length = 3000.0
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FEktCdYqytDrFRn_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FEktCdYqytDrFRn_1_FeQsJu9i13lDWMz_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Plane", "plane_Sketch_F3HFVQlJ23WUKE9_1_JNC")
origin = App.Vector(9500.00000000000000,-3000.00000000000000,1500.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F3HFVQlJ23WUKE9_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("Sketcher::SketchObject","Sketch_F3HFVQlJ23WUKE9_1_JNC")
App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F3HFVQlJ23WUKE9_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC").addGeometry(Part.LineSegment(App.Vector(6000.00000000000000,1000.00000000000000,0.00000000000000),App.Vector(1000.00000000000000,1000.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC").addGeometry(Part.LineSegment(App.Vector(1000.00000000000000,1000.00000000000000,0.00000000000000),App.Vector(1000.00000000000000,-1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC").addGeometry(Part.LineSegment(App.Vector(1000.00000000000000,-1500.00000000000000,0.00000000000000),App.Vector(6000.00000000000000,-1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC").addGeometry(Part.LineSegment(App.Vector(6000.00000000000000,1000.00000000000000,0.00000000000000),App.Vector(6000.00000000000000,-1500.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Pocket","Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC")
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC")
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").Length = 7500.0
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F3HFVQlJ23WUKE9_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F3HFVQlJ23WUKE9_1_Fziq6HftDJNYY7m_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Plane", "plane_Sketch_Ff0rnXeY1f3F65O_1_JRC")
origin = App.Vector(-3000.00000000000000,0.00000000000000,3018.00000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,-0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ff0rnXeY1f3F65O_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("Sketcher::SketchObject","Sketch_Ff0rnXeY1f3F65O_1_JRC")
App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ff0rnXeY1f3F65O_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC").addGeometry(Part.LineSegment(App.Vector(5000.00000000000000,2982.00000000000000,0.00000000000000),App.Vector(-5000.00000000000000,2482.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5000.00000000000000,2982.00000000000000,0.00000000000000),App.Vector(-5000.00000000000000,2482.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5000.00000000000000,2982.00000000000000,0.00000000000000),App.Vector(-2735.78261999999995,2982.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC").addGeometry(Part.LineSegment(App.Vector(5000.00000000000000,2982.00000000000000,0.00000000000000),App.Vector(-2735.78261999999995,2982.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Pocket","Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC")
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC")
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").Length = 22234.203338623047
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ff0rnXeY1f3F65O_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ff0rnXeY1f3F65O_1_FJoxkrKvZPPzhes_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Plane", "plane_Sketch_FLXpGlSKBMtWSYA_1_JVG")
origin = App.Vector(3500.00000000000000,-5000.00000000000000,3000.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FLXpGlSKBMtWSYA_1_JVG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("Sketcher::SketchObject","Sketch_FLXpGlSKBMtWSYA_1_JVG")
App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FLXpGlSKBMtWSYA_1_JVG"), [""])
App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").addGeometry(Part.LineSegment(App.Vector(-6200.00000000000000,2700.00000000000000,0.00000000000000),App.Vector(6199.99999999999909,2700.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").addGeometry(Part.LineSegment(App.Vector(6199.99999999999909,2700.00000000000000,0.00000000000000),App.Vector(6199.99999999999909,299.99999999999983,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").addGeometry(Part.LineSegment(App.Vector(-799.99999999999977,299.99999999999983,0.00000000000000),App.Vector(6199.99999999999909,299.99999999999983,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").addGeometry(Part.LineSegment(App.Vector(-799.99999999999977,-2700.00000000000000,0.00000000000000),App.Vector(-799.99999999999977,299.99999999999983,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").addGeometry(Part.LineSegment(App.Vector(-799.99999999999977,-2700.00000000000000,0.00000000000000),App.Vector(-6200.00000000000000,-2700.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").addGeometry(Part.LineSegment(App.Vector(-6200.00000000000000,2700.00000000000000,0.00000000000000),App.Vector(-6200.00000000000000,-2700.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F41w51GSlLkzJ9k_0").newObject("PartDesign::Pocket","Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG")
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").Profile = App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG")
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").Length = 200.0
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FLXpGlSKBMtWSYA_1_JVG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").Type = 4
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FLXpGlSKBMtWSYA_1_F6GwNnvjDEki3Vr_1_JVG").Offset = 0
App.ActiveDocument.recompute()

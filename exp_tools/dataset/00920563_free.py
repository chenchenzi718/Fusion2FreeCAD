import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00920563")
App.ActiveDocument.addObject("PartDesign::Body","Body_F1US2KOP1xUfPGO_0")
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").Label = "Body_F1US2KOP1xUfPGO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Plane", "plane_Sketch_F1US2KOP1xUfPGO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F1US2KOP1xUfPGO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("Sketcher::SketchObject","Sketch_F1US2KOP1xUfPGO_0_JGC")
App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F1US2KOP1xUfPGO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC").addGeometry(Part.LineSegment(App.Vector(440.00000000000000,-1035.00000000000000,0.00000000000000),App.Vector(-440.00000000000000,-1035.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC").addGeometry(Part.LineSegment(App.Vector(-440.00000000000000,-1035.00000000000000,0.00000000000000),App.Vector(-440.00000000000000,1035.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC").addGeometry(Part.LineSegment(App.Vector(440.00000000000000,1035.00000000000000,0.00000000000000),App.Vector(-440.00000000000000,1035.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC").addGeometry(Part.LineSegment(App.Vector(440.00000000000000,-1035.00000000000000,0.00000000000000),App.Vector(440.00000000000000,1035.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Pad","Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC")
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC")
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").Length = 18.000000000000004
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F1US2KOP1xUfPGO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").Midplane = 1
App.ActiveDocument.getObject("Extrude_F1US2KOP1xUfPGO_0_F5CvXVOqY6yIFlW_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Plane", "plane_Sketch_F4IxAj15YI1zhhB_1_JJC")
origin = App.Vector(0.00000000000000,0.00000000000000,-9.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4IxAj15YI1zhhB_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("Sketcher::SketchObject","Sketch_F4IxAj15YI1zhhB_1_JJC")
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4IxAj15YI1zhhB_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJC").addGeometry(Part.Circle(App.Vector(0.00000000000000,127.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Pocket","Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC")
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJC")
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").Length = 18.000000000000004
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Plane", "plane_Sketch_F4IxAj15YI1zhhB_1_JJG")
origin = App.Vector(0.00000000000000,0.00000000000000,-9.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4IxAj15YI1zhhB_1_JJG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("Sketcher::SketchObject","Sketch_F4IxAj15YI1zhhB_1_JJG")
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4IxAj15YI1zhhB_1_JJG"), [""])
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJG").addGeometry(Part.Circle(App.Vector(0.00000000000000,387.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Pocket","Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG")
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").Profile = App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJG")
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").Length = 18.000000000000004
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").Type = 4
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Plane", "plane_Sketch_F4IxAj15YI1zhhB_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,-9.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4IxAj15YI1zhhB_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("Sketcher::SketchObject","Sketch_F4IxAj15YI1zhhB_1_JJK")
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4IxAj15YI1zhhB_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJK").addGeometry(Part.Circle(App.Vector(-400.00000000000000,127.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Pocket","Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK")
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJK")
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").Length = 18.000000000000004
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Plane", "plane_Sketch_F4IxAj15YI1zhhB_1_JJO")
origin = App.Vector(0.00000000000000,0.00000000000000,-9.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4IxAj15YI1zhhB_1_JJO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("Sketcher::SketchObject","Sketch_F4IxAj15YI1zhhB_1_JJO")
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4IxAj15YI1zhhB_1_JJO"), [""])
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJO").addGeometry(Part.Circle(App.Vector(-400.00000000000000,387.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Pocket","Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO")
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").Profile = App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJO")
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").Length = 18.000000000000004
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4IxAj15YI1zhhB_1_JJO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").Type = 4
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4IxAj15YI1zhhB_1_FxpoyB5pIYbFhBB_1_JJO").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Plane", "plane_Sketch_FdPqXjAQ803we8v_1_JPC")
origin = App.Vector(0.00000000000000,-1035.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdPqXjAQ803we8v_1_JPC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("Sketcher::SketchObject","Sketch_FdPqXjAQ803we8v_1_JPC")
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdPqXjAQ803we8v_1_JPC"), [""])
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPC").addGeometry(Part.Circle(App.Vector(-410.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Pocket","Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC")
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").Profile = App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPC")
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").Length = 28.0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").Type = 4
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Plane", "plane_Sketch_FdPqXjAQ803we8v_1_JPG")
origin = App.Vector(0.00000000000000,-1035.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdPqXjAQ803we8v_1_JPG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("Sketcher::SketchObject","Sketch_FdPqXjAQ803we8v_1_JPG")
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdPqXjAQ803we8v_1_JPG"), [""])
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPG").addGeometry(Part.Circle(App.Vector(410.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),4.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Pocket","Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG")
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").Profile = App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPG")
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").Length = 28.0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").Type = 4
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_F2o12wHck0pdHFl_1_JPG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Plane", "plane_Sketch_FdPqXjAQ803we8v_1_JPK")
origin = App.Vector(0.00000000000000,-1035.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdPqXjAQ803we8v_1_JPK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("Sketcher::SketchObject","Sketch_FdPqXjAQ803we8v_1_JPK")
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdPqXjAQ803we8v_1_JPK"), [""])
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPK").addGeometry(Part.Circle(App.Vector(-378.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Pocket","Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK")
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").Profile = App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPK")
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").Length = 13.000000000000002
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").Type = 4
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Plane", "plane_Sketch_FdPqXjAQ803we8v_1_JPO")
origin = App.Vector(0.00000000000000,-1035.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdPqXjAQ803we8v_1_JPO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("Sketcher::SketchObject","Sketch_FdPqXjAQ803we8v_1_JPO")
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdPqXjAQ803we8v_1_JPO"), [""])
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPO").addGeometry(Part.Circle(App.Vector(378.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),2.50000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F1US2KOP1xUfPGO_0").newObject("PartDesign::Pocket","Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO")
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").Profile = App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPO")
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").Length = 13.000000000000002
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdPqXjAQ803we8v_1_JPO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").Type = 4
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdPqXjAQ803we8v_1_FRTTiSSCwDYAAGN_1_JPO").Offset = 0
App.ActiveDocument.recompute()

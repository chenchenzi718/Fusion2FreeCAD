import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00640493")
App.ActiveDocument.addObject("PartDesign::Body","Body_F54tvClMAYHNNhz_0")
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").Label = "Body_F54tvClMAYHNNhz_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Plane", "plane_Sketch_F54tvClMAYHNNhz_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F54tvClMAYHNNhz_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("Sketcher::SketchObject","Sketch_F54tvClMAYHNNhz_0_JGC")
App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F54tvClMAYHNNhz_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC").addGeometry(Part.LineSegment(App.Vector(203.37450000000001,52.68207000000000,0.00000000000000),App.Vector(330.37450000000001,52.68207000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC").addGeometry(Part.LineSegment(App.Vector(330.37450000000001,52.68207000000000,0.00000000000000),App.Vector(330.37450000000001,-74.31793000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC").addGeometry(Part.LineSegment(App.Vector(203.37450000000001,-74.31793000000000,0.00000000000000),App.Vector(330.37450000000001,-74.31793000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC").addGeometry(Part.LineSegment(App.Vector(203.37450000000001,52.68207000000000,0.00000000000000),App.Vector(203.37450000000001,-74.31793000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Pad","Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC")
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC")
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").Length = 127.0
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F54tvClMAYHNNhz_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").Type = 0
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F54tvClMAYHNNhz_0_F0MuEJF8PlijvRU_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Plane", "plane_Sketch_FQYV3Q3mUiHrLkl_1_JJC")
origin = App.Vector(266.87450000000001,63.50000000000000,-74.31793000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQYV3Q3mUiHrLkl_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("Sketcher::SketchObject","Sketch_FQYV3Q3mUiHrLkl_1_JJC")
App.ActiveDocument.getObject("Sketch_FQYV3Q3mUiHrLkl_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQYV3Q3mUiHrLkl_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FQYV3Q3mUiHrLkl_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQYV3Q3mUiHrLkl_1_JJC").addGeometry(Part.Circle(App.Vector(4.31543000000001,1.01600000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),41.89759000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQYV3Q3mUiHrLkl_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQYV3Q3mUiHrLkl_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Pad","Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC")
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FQYV3Q3mUiHrLkl_1_JJC")
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQYV3Q3mUiHrLkl_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQYV3Q3mUiHrLkl_1_FpD1hYumiglHdvJ_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Plane", "plane_Sketch_Fb3FdSU9JbW3gqC_1_JNC")
origin = App.Vector(266.87450000000001,63.50000000000000,52.68207000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fb3FdSU9JbW3gqC_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("Sketcher::SketchObject","Sketch_Fb3FdSU9JbW3gqC_1_JNC")
App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fb3FdSU9JbW3gqC_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC").addGeometry(Part.LineSegment(App.Vector(-52.55217000000001,-45.47429000000000,0.00000000000000),App.Vector(50.85320999999998,-45.47429000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC").addGeometry(Part.LineSegment(App.Vector(50.85320999999998,-45.47429000000000,0.00000000000000),App.Vector(50.85320999999998,50.50433999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC").addGeometry(Part.LineSegment(App.Vector(-52.55217000000001,50.50433999999999,0.00000000000000),App.Vector(50.85320999999998,50.50433999999999,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC").addGeometry(Part.LineSegment(App.Vector(-52.55217000000001,-45.47429000000000,0.00000000000000),App.Vector(-52.55217000000001,50.50433999999999,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Pocket","Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC")
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC")
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").Length = 101.60000000000001
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fb3FdSU9JbW3gqC_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fb3FdSU9JbW3gqC_1_Fb4rLQ3BNVcyWGL_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Plane", "plane_Sketch_FoBBirao7cbVj4T_1_JRC")
origin = App.Vector(330.37450000000001,63.50000000000000,5.31749000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FoBBirao7cbVj4T_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("Sketcher::SketchObject","Sketch_FoBBirao7cbVj4T_1_JRC")
App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FoBBirao7cbVj4T_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5.01197000000000,79.63542000000001,0.00000000000000),App.Vector(10.64274999999999,79.63542000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC").addGeometry(Part.LineSegment(App.Vector(10.64274999999999,79.63542000000001,0.00000000000000),App.Vector(10.64274999999999,47.36458000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5.01197000000000,47.36458000000000,0.00000000000000),App.Vector(10.64274999999999,47.36458000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC").addGeometry(Part.LineSegment(App.Vector(-5.01197000000000,79.63542000000001,0.00000000000000),App.Vector(-5.01197000000000,47.36458000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Pad","Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC")
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC")
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FoBBirao7cbVj4T_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").Type = 0
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").Reversed = 1
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FoBBirao7cbVj4T_1_FvoF27lLrFdsNDa_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Plane", "plane_Sketch_F0meiIKm7a6xY5Z_1_JVC")
origin = App.Vector(203.37450000000001,63.50000000000000,5.30171000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0meiIKm7a6xY5Z_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("Sketcher::SketchObject","Sketch_F0meiIKm7a6xY5Z_1_JVC")
App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0meiIKm7a6xY5Z_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC").addGeometry(Part.LineSegment(App.Vector(-8.76412999999999,79.61964000000000,0.00000000000000),App.Vector(5.27432000000000,79.61964000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC").addGeometry(Part.LineSegment(App.Vector(5.27432000000000,79.61964000000000,0.00000000000000),App.Vector(5.27432000000000,47.38036000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC").addGeometry(Part.LineSegment(App.Vector(-8.76412999999999,47.38036000000000,0.00000000000000),App.Vector(5.27432000000000,47.38036000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC").addGeometry(Part.LineSegment(App.Vector(-8.76412999999999,79.61964000000000,0.00000000000000),App.Vector(-8.76412999999999,47.38036000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Pad","Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC")
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC")
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").UseCustomVector = 0
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0meiIKm7a6xY5Z_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").Type = 0
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").Reversed = 1
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0meiIKm7a6xY5Z_1_Fl10kjmv7Tz4zJr_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Plane", "plane_Sketch_FpYhSuYxOCfZMhf_1_JZC")
origin = App.Vector(330.37450000000001,63.50000000000000,5.31749000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FpYhSuYxOCfZMhf_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("Sketcher::SketchObject","Sketch_FpYhSuYxOCfZMhf_1_JZC")
App.ActiveDocument.getObject("Sketch_FpYhSuYxOCfZMhf_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FpYhSuYxOCfZMhf_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FpYhSuYxOCfZMhf_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FpYhSuYxOCfZMhf_1_JZC").addGeometry(Part.Circle(App.Vector(2.11757999999999,73.76583000000001,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.88884000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FpYhSuYxOCfZMhf_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FpYhSuYxOCfZMhf_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Pocket","Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC")
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FpYhSuYxOCfZMhf_1_JZC")
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FpYhSuYxOCfZMhf_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FpYhSuYxOCfZMhf_1_FqXRjxyJ9jxw5h4_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Plane", "plane_Sketch_F2GlNs0u9Iu5Bo4_1_JdC")
origin = App.Vector(203.37450000000001,63.50000000000000,5.30171000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F2GlNs0u9Iu5Bo4_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("Sketcher::SketchObject","Sketch_F2GlNs0u9Iu5Bo4_1_JdC")
App.ActiveDocument.getObject("Sketch_F2GlNs0u9Iu5Bo4_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F2GlNs0u9Iu5Bo4_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_F2GlNs0u9Iu5Bo4_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F2GlNs0u9Iu5Bo4_1_JdC").addGeometry(Part.Circle(App.Vector(-2.55237999999999,73.78161000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.50535000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F2GlNs0u9Iu5Bo4_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F2GlNs0u9Iu5Bo4_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Pocket","Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC")
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_F2GlNs0u9Iu5Bo4_1_JdC")
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").Length = 5.080000000000001
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F2GlNs0u9Iu5Bo4_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F2GlNs0u9Iu5Bo4_1_FNHxwXNfoxHpnEe_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Plane", "plane_Sketch_FusYS4omJJTnRQc_2_JkC")
origin = App.Vector(266.87450000000001,0.00000000000000,-10.81793000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FusYS4omJJTnRQc_2_JkC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("Sketcher::SketchObject","Sketch_FusYS4omJJTnRQc_2_JkC")
App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FusYS4omJJTnRQc_2_JkC"), [""])
App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC").addGeometry(Part.LineSegment(App.Vector(-48.20485000000002,-46.12857000000000,0.00000000000000),App.Vector(43.25451999999996,-46.12857000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC").addGeometry(Part.LineSegment(App.Vector(43.25451999999996,-46.12857000000000,0.00000000000000),App.Vector(43.25451999999996,-52.26006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC").addGeometry(Part.LineSegment(App.Vector(-48.20485000000002,-52.26006000000000,0.00000000000000),App.Vector(43.25451999999996,-52.26006000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC").addGeometry(Part.LineSegment(App.Vector(-48.20485000000002,-46.12857000000000,0.00000000000000),App.Vector(-48.20485000000002,-52.26006000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F54tvClMAYHNNhz_0").newObject("PartDesign::Pocket","Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC")
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").Profile = App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC")
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FusYS4omJJTnRQc_2_JkC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").Type = 4
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FusYS4omJJTnRQc_2_FB3W8iHmq6lTw79_2_JkC").Offset = 0
App.ActiveDocument.recompute()

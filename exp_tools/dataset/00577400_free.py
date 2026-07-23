import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00577400")
App.ActiveDocument.addObject("PartDesign::Body","Body_Fe7feyNPJ5Qwatn_0")
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").Label = "Body_Fe7feyNPJ5Qwatn_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_Fe7feyNPJ5Qwatn_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fe7feyNPJ5Qwatn_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_Fe7feyNPJ5Qwatn_0_JGC")
App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fe7feyNPJ5Qwatn_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,0.00000000000000,0.00000000000000),App.Vector(45.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,-60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.00000000000000,-60.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").addGeometry(Part.LineSegment(App.Vector(-45.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,60.00000000000000,0.00000000000000),App.Vector(-45.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,60.00000000000000,0.00000000000000),App.Vector(0.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").addGeometry(Part.LineSegment(App.Vector(45.00000000000000,0.00000000000000,0.00000000000000),App.Vector(45.00000000000000,60.00000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pad","Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC")
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC")
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").Length = 5.0
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fe7feyNPJ5Qwatn_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fe7feyNPJ5Qwatn_0_Fe23BXoAomxvksc_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_F4KS4XDPHLJZS26_1_JJK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4KS4XDPHLJZS26_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_F4KS4XDPHLJZS26_1_JJK")
App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4KS4XDPHLJZS26_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.LineSegment(App.Vector(-40.00000000000000,-45.00000000000000,0.00000000000000),App.Vector(-40.00000000000000,55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.LineSegment(App.Vector(-40.00000000000000,55.00000000000000,0.00000000000000),App.Vector(18.00000000000000,55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.LineSegment(App.Vector(18.00000000000000,55.00000000000000,0.00000000000000),App.Vector(18.00000000000000,50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(33.00000000000000,50.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),3.14159265358979,4.71238898038469),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.LineSegment(App.Vector(33.00000000000000,35.00000000000000,0.00000000000000),App.Vector(40.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.LineSegment(App.Vector(40.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(40.00000000000000,35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.LineSegment(App.Vector(33.00000000000000,-35.00000000000000,0.00000000000000),App.Vector(40.00000000000000,-35.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.ArcOfCircle(Part.Circle(App.Vector(33.00000000000000,-50.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),15.00000000000000),1.5707963267949,3.14159265358979),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.LineSegment(App.Vector(18.00000000000000,-55.00000000000000,0.00000000000000),App.Vector(18.00000000000000,-50.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.LineSegment(App.Vector(-18.00000000000000,-55.00000000000000,0.00000000000000),App.Vector(18.00000000000000,-55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.LineSegment(App.Vector(-40.00000000000000,-45.00000000000000,0.00000000000000),App.Vector(-18.00000000000000,-55.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").addGeometry(Part.Circle(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),30.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pad","Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK")
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK")
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4KS4XDPHLJZS26_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4KS4XDPHLJZS26_1_FPKZIiBKd53TRvG_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_F4ER8ZEAF1FOE57_1_JNW")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNW").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_F4ER8ZEAF1FOE57_1_JNW")
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNW").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNW"), [""])
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNW").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNW").addGeometry(Part.Circle(App.Vector(-14.14427000000000,-14.14000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNW").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNW").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pocket","Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").Profile = App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNW")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNW"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").Type = 4
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNW").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_F4ER8ZEAF1FOE57_1_JNC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_F4ER8ZEAF1FOE57_1_JNC")
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNC").addGeometry(Part.Circle(App.Vector(-20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pocket","Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNC")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_F4ER8ZEAF1FOE57_1_JNS")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNS").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_F4ER8ZEAF1FOE57_1_JNS")
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNS").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNS"), [""])
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNS").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNS").addGeometry(Part.Circle(App.Vector(-14.14427000000000,14.14000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNS").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNS").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pocket","Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").Profile = App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNS")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNS"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").Type = 4
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNS").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_F4ER8ZEAF1FOE57_1_JNG")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_F4ER8ZEAF1FOE57_1_JNG")
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNG"), [""])
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNG").addGeometry(Part.Circle(App.Vector(0.00000000000000,20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pocket","Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").Profile = App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNG")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_F4ER8ZEAF1FOE57_1_JNa")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNa").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_F4ER8ZEAF1FOE57_1_JNa")
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNa").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNa"), [""])
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNa").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNa").addGeometry(Part.Circle(App.Vector(14.14427000000000,14.14000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNa").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNa").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pocket","Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").Profile = App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNa")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNa"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").Type = 4
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNa").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_F4ER8ZEAF1FOE57_1_JNK")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_F4ER8ZEAF1FOE57_1_JNK")
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNK"), [""])
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNK").addGeometry(Part.Circle(App.Vector(20.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pocket","Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").Profile = App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNK")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").Type = 4
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_F4ER8ZEAF1FOE57_1_JNe")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNe").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_F4ER8ZEAF1FOE57_1_JNe")
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNe").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNe"), [""])
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNe").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNe").addGeometry(Part.Circle(App.Vector(14.14427000000000,-14.14000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNe").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNe").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pocket","Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").Profile = App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNe")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNe"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").Type = 4
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNe").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Plane", "plane_Sketch_F4ER8ZEAF1FOE57_1_JNO")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNO").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("Sketcher::SketchObject","Sketch_F4ER8ZEAF1FOE57_1_JNO")
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNO").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4ER8ZEAF1FOE57_1_JNO"), [""])
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNO").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNO").addGeometry(Part.Circle(App.Vector(0.00000000000000,-20.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),3.00000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNO").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNO").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_Fe7feyNPJ5Qwatn_0").newObject("PartDesign::Pocket","Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").Profile = App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNO")
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").Length = 5.0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4ER8ZEAF1FOE57_1_JNO"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").Type = 4
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4ER8ZEAF1FOE57_1_FvX0VsOGERi7nXC_1_JNO").Offset = 0
App.ActiveDocument.recompute()

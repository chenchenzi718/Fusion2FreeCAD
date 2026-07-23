import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00455800")
App.ActiveDocument.addObject("PartDesign::Body","Body_FfmGphisKKsMnix_0")
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").Label = "Body_FfmGphisKKsMnix_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_FfmGphisKKsMnix_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FfmGphisKKsMnix_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_FfmGphisKKsMnix_0_JGC")
App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FfmGphisKKsMnix_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC").addGeometry(Part.LineSegment(App.Vector(-50.80000000000000,0.00000000000000,0.00000000000000),App.Vector(-50.80000000000000,-304.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,-304.80000000000001,0.00000000000000),App.Vector(-50.80000000000000,-304.80000000000001,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC").addGeometry(Part.LineSegment(App.Vector(0.00000000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,-304.80000000000001,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pad","Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC")
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC")
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FfmGphisKKsMnix_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FfmGphisKKsMnix_0_F5gWHV4ltUf7jKx_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_FdlGThrxjH2jgs1_1_JJC")
origin = App.Vector(-50.80000000000000,-184.15000000000001,25.40000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdlGThrxjH2jgs1_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_FdlGThrxjH2jgs1_1_JJC")
App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdlGThrxjH2jgs1_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-184.15000000000001,-25.40000000000000,0.00000000000000),App.Vector(-273.05000000000001,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-273.05000000000001,-25.40000000000000,0.00000000000000),App.Vector(-273.05000000000001,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-120.65000000000001,127.00000000000000,0.00000000000000),App.Vector(-273.05000000000001,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-120.65000000000001,127.00000000000000,0.00000000000000),App.Vector(-120.65000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-184.15000000000001,25.40000000000000,0.00000000000000),App.Vector(-120.65000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").addGeometry(Part.LineSegment(App.Vector(-184.15000000000001,-25.40000000000000,0.00000000000000),App.Vector(-184.15000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pad","Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC")
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC")
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_FdlGThrxjH2jgs1_1_JJK")
origin = App.Vector(-50.80000000000000,-184.15000000000001,25.40000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FdlGThrxjH2jgs1_1_JJK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_FdlGThrxjH2jgs1_1_JJK")
App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FdlGThrxjH2jgs1_1_JJK"), [""])
App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK").addGeometry(Part.LineSegment(App.Vector(-184.15000000000001,-25.40000000000000,0.00000000000000),App.Vector(-120.65000000000001,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK").addGeometry(Part.LineSegment(App.Vector(-120.65000000000001,-25.40000000000000,0.00000000000000),App.Vector(-120.65000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK").addGeometry(Part.LineSegment(App.Vector(-184.15000000000001,25.40000000000000,0.00000000000000),App.Vector(-120.65000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK").addGeometry(Part.LineSegment(App.Vector(-184.15000000000001,-25.40000000000000,0.00000000000000),App.Vector(-184.15000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pad","Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK")
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").Profile = App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK")
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FdlGThrxjH2jgs1_1_JJK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").Type = 4
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").UpToFace = None
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").Reversed = 0
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").Midplane = 0
App.ActiveDocument.getObject("Extrude_FdlGThrxjH2jgs1_1_F7PEhTlG2PiEMlD_1_JJK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_FJt5Ja02rQunFxI_2_JNG")
origin = App.Vector(-57.15000000000000,12.70000000000000,76.20000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJt5Ja02rQunFxI_2_JNG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_FJt5Ja02rQunFxI_2_JNG")
App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJt5Ja02rQunFxI_2_JNG"), [""])
App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNG").addGeometry(Part.Circle(App.Vector(-38.09999999999999,50.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.94131000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pocket","Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG")
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").Profile = App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNG")
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").Type = 4
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_FJt5Ja02rQunFxI_2_JNC")
origin = App.Vector(-57.15000000000000,12.70000000000000,76.20000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJt5Ja02rQunFxI_2_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_FJt5Ja02rQunFxI_2_JNC")
App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJt5Ja02rQunFxI_2_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNC").addGeometry(Part.Circle(App.Vector(-38.09999999999999,-50.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.93750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pocket","Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC")
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").Profile = App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNC")
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJt5Ja02rQunFxI_2_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJt5Ja02rQunFxI_2_FH6ZUdj0Rtkq5ak_2_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_FJGx81Q4bx5hjvC_2_JSC")
origin = App.Vector(-50.80000000000000,-184.15000000000001,25.40000000000000)
x_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(-1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FJGx81Q4bx5hjvC_2_JSC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_FJGx81Q4bx5hjvC_2_JSC")
App.ActiveDocument.getObject("Sketch_FJGx81Q4bx5hjvC_2_JSC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FJGx81Q4bx5hjvC_2_JSC"), [""])
App.ActiveDocument.getObject("Sketch_FJGx81Q4bx5hjvC_2_JSC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FJGx81Q4bx5hjvC_2_JSC").addGeometry(Part.Circle(App.Vector(44.44999999999999,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.93750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FJGx81Q4bx5hjvC_2_JSC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FJGx81Q4bx5hjvC_2_JSC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pocket","Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC")
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").Profile = App.ActiveDocument.getObject("Sketch_FJGx81Q4bx5hjvC_2_JSC")
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FJGx81Q4bx5hjvC_2_JSC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").Type = 4
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FJGx81Q4bx5hjvC_2_FnZnhLOE7cjshG2_2_JSC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_F4FKaOLzhKPuCD8_1_JWG")
origin = App.Vector(0.00000000000000,-184.15000000000001,25.40000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4FKaOLzhKPuCD8_1_JWG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_F4FKaOLzhKPuCD8_1_JWG")
App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4FKaOLzhKPuCD8_1_JWG"), [""])
App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").addGeometry(Part.LineSegment(App.Vector(184.15000000000001,-25.40000000000000,0.00000000000000),App.Vector(273.05000000000001,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").addGeometry(Part.LineSegment(App.Vector(273.05000000000001,-25.40000000000000,0.00000000000000),App.Vector(273.05000000000001,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").addGeometry(Part.LineSegment(App.Vector(120.65000000000001,127.00000000000000,0.00000000000000),App.Vector(273.05000000000001,127.00000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").addGeometry(Part.LineSegment(App.Vector(120.65000000000001,127.00000000000000,0.00000000000000),App.Vector(120.65000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").addGeometry(Part.LineSegment(App.Vector(184.15000000000001,25.40000000000000,0.00000000000000),App.Vector(120.65000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").addGeometry(Part.LineSegment(App.Vector(184.15000000000001,-25.40000000000000,0.00000000000000),App.Vector(184.15000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pad","Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG")
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").Profile = App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG")
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").Type = 4
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_F4FKaOLzhKPuCD8_1_JWK")
origin = App.Vector(0.00000000000000,-184.15000000000001,25.40000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F4FKaOLzhKPuCD8_1_JWK").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_F4FKaOLzhKPuCD8_1_JWK")
App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F4FKaOLzhKPuCD8_1_JWK"), [""])
App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK").addGeometry(Part.LineSegment(App.Vector(184.15000000000001,-25.40000000000000,0.00000000000000),App.Vector(120.65000000000001,-25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK").addGeometry(Part.LineSegment(App.Vector(120.65000000000001,-25.40000000000000,0.00000000000000),App.Vector(120.65000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK").addGeometry(Part.LineSegment(App.Vector(184.15000000000001,25.40000000000000,0.00000000000000),App.Vector(120.65000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK").addGeometry(Part.LineSegment(App.Vector(184.15000000000001,-25.40000000000000,0.00000000000000),App.Vector(184.15000000000001,25.40000000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pad","Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK")
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").Profile = App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK")
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F4FKaOLzhKPuCD8_1_JWK"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").Type = 4
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").UpToFace = None
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").Reversed = 0
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").Midplane = 0
App.ActiveDocument.getObject("Extrude_F4FKaOLzhKPuCD8_1_F1waWM3oXMtzHwS_1_JWK").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG")
origin = App.Vector(6.35000000000000,12.70000000000000,76.20000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG")
App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG"), [""])
App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG").addGeometry(Part.Circle(App.Vector(38.09999999999999,50.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.93750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pocket","Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG")
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").Profile = App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG")
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaG"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").Type = 4
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaG").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Plane", "plane_Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC")
origin = App.Vector(6.35000000000000,12.70000000000000,76.20000000000000)
x_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("Sketcher::SketchObject","Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC")
App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC"), [""])
App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC").addGeometry(Part.Circle(App.Vector(38.09999999999999,-50.80000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),7.93750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FfmGphisKKsMnix_0").newObject("PartDesign::Pocket","Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC")
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").Profile = App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC")
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").Length = 6.3500000000000005
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F7Q1LqqGsZ8Q7Fs_1_JaC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").Type = 4
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F7Q1LqqGsZ8Q7Fs_1_FfilzkmYmfZhUuK_1_JaC").Offset = 0
App.ActiveDocument.recompute()

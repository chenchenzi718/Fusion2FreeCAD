import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00099014")
App.ActiveDocument.addObject("PartDesign::Body","Body_F0mbsH6ly2wQmyE_0")
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").Label = "Body_F0mbsH6ly2wQmyE_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Plane", "plane_Sketch_F0mbsH6ly2wQmyE_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F0mbsH6ly2wQmyE_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("Sketcher::SketchObject","Sketch_F0mbsH6ly2wQmyE_0_JGC")
App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F0mbsH6ly2wQmyE_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC").addGeometry(Part.LineSegment(App.Vector(-67.68894999999999,61.67455000000000,0.00000000000000),App.Vector(58.48747000000000,61.67455000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC").addGeometry(Part.LineSegment(App.Vector(58.48747000000000,61.67455000000000,0.00000000000000),App.Vector(58.48747000000000,-50.94646000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC").addGeometry(Part.LineSegment(App.Vector(-67.68894999999999,-50.94646000000000,0.00000000000000),App.Vector(58.48747000000000,-50.94646000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC").addGeometry(Part.LineSegment(App.Vector(-67.68894999999999,61.67455000000000,0.00000000000000),App.Vector(-67.68894999999999,-50.94646000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Pad","Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC")
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC")
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F0mbsH6ly2wQmyE_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F0mbsH6ly2wQmyE_0_FvGIJvp1YhdUNZY_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Plane", "plane_Sketch_Fu1xekoR64EPi1a_1_JJC")
origin = App.Vector(-4.60074000000000,5.36405000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fu1xekoR64EPi1a_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("Sketcher::SketchObject","Sketch_Fu1xekoR64EPi1a_1_JJC")
App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fu1xekoR64EPi1a_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC").addGeometry(Part.LineSegment(App.Vector(26.94037000000000,37.97986000000000,0.00000000000000),App.Vector(53.25692000000000,37.97986000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC").addGeometry(Part.LineSegment(App.Vector(53.25692000000000,37.97986000000000,0.00000000000000),App.Vector(53.25692000000000,22.78600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC").addGeometry(Part.LineSegment(App.Vector(26.94037000000000,22.78600000000000,0.00000000000000),App.Vector(53.25692000000000,22.78600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC").addGeometry(Part.LineSegment(App.Vector(26.94037000000000,37.97986000000000,0.00000000000000),App.Vector(26.94037000000000,22.78600000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Pad","Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC")
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC")
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fu1xekoR64EPi1a_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fu1xekoR64EPi1a_1_FEdoxRmbivGhNT9_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Plane", "plane_Sketch_F70KeN6nwZDHISI_1_JNC")
origin = App.Vector(-4.60074000000000,5.36405000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F70KeN6nwZDHISI_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("Sketcher::SketchObject","Sketch_F70KeN6nwZDHISI_1_JNC")
App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F70KeN6nwZDHISI_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.39367000000000,29.76522000000000,0.00000000000000),App.Vector(-53.53393000000000,29.76522000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-53.53393000000000,29.76522000000000,0.00000000000000),App.Vector(-53.53393000000000,51.36363000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.39367000000000,51.36363000000000,0.00000000000000),App.Vector(-53.53393000000000,51.36363000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC").addGeometry(Part.LineSegment(App.Vector(-19.39367000000000,29.76522000000000,0.00000000000000),App.Vector(-19.39367000000000,51.36363000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Pad","Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC")
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC")
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F70KeN6nwZDHISI_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F70KeN6nwZDHISI_1_FHOMMaYrCNE3PYe_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Plane", "plane_Sketch_FjdtqfTktPdSQ4M_1_JTC")
origin = App.Vector(-4.60074000000000,5.36405000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FjdtqfTktPdSQ4M_1_JTC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("Sketcher::SketchObject","Sketch_FjdtqfTktPdSQ4M_1_JTC")
App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FjdtqfTktPdSQ4M_1_JTC"), [""])
App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC").addGeometry(Part.LineSegment(App.Vector(23.66662000000000,-30.02075000000000,0.00000000000000),App.Vector(58.53121000000000,-30.02075000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC").addGeometry(Part.LineSegment(App.Vector(58.53121000000000,-30.02075000000000,0.00000000000000),App.Vector(58.53121000000000,-48.70759000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC").addGeometry(Part.LineSegment(App.Vector(23.66662000000000,-48.70759000000000,0.00000000000000),App.Vector(58.53121000000000,-48.70759000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC").addGeometry(Part.LineSegment(App.Vector(23.66662000000000,-30.02075000000000,0.00000000000000),App.Vector(23.66662000000000,-48.70759000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Pad","Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC")
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").Profile = App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC")
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FjdtqfTktPdSQ4M_1_JTC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").Type = 4
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FjdtqfTktPdSQ4M_1_FWy0Qv4ptikvAP7_1_JTC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Plane", "plane_Sketch_FswzLi46E4ojGDY_1_JRC")
origin = App.Vector(-4.60074000000000,5.36405000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FswzLi46E4ojGDY_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("Sketcher::SketchObject","Sketch_FswzLi46E4ojGDY_1_JRC")
App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FswzLi46E4ojGDY_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC").addGeometry(Part.LineSegment(App.Vector(-48.06167000000000,-48.78957000000000,0.00000000000000),App.Vector(-8.47190000000000,-48.78957000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC").addGeometry(Part.LineSegment(App.Vector(-8.47190000000000,-48.78957000000000,0.00000000000000),App.Vector(-8.47190000000000,-29.29756000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC").addGeometry(Part.LineSegment(App.Vector(-48.06167000000000,-29.29756000000000,0.00000000000000),App.Vector(-8.47190000000000,-29.29756000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC").addGeometry(Part.LineSegment(App.Vector(-48.06167000000000,-48.78957000000000,0.00000000000000),App.Vector(-48.06167000000000,-29.29756000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Pad","Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC")
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC")
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FswzLi46E4ojGDY_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FswzLi46E4ojGDY_1_Fdm32daDdsmjRH2_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Plane", "plane_Sketch_F6CKGISUlWgFxwW_1_JXC")
origin = App.Vector(-32.52948000000000,-35.20037000000000,-25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F6CKGISUlWgFxwW_1_JXC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("Sketcher::SketchObject","Sketch_F6CKGISUlWgFxwW_1_JXC")
App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F6CKGISUlWgFxwW_1_JXC"), [""])
App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC").addGeometry(Part.LineSegment(App.Vector(-25.60519000000000,10.79921000000000,0.00000000000000),App.Vector(-8.53506000000000,10.79921000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC").addGeometry(Part.LineSegment(App.Vector(-8.53506000000000,10.79921000000000,0.00000000000000),App.Vector(-8.53506000000000,-10.79920000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC").addGeometry(Part.LineSegment(App.Vector(-25.60519000000000,-10.79920000000000,0.00000000000000),App.Vector(-8.53506000000000,-10.79920000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC").addGeometry(Part.LineSegment(App.Vector(-25.60519000000000,-10.79920000000000,0.00000000000000),App.Vector(-25.60519000000000,10.79921000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Pad","Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC")
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").Profile = App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC")
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F6CKGISUlWgFxwW_1_JXC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").Type = 4
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F6CKGISUlWgFxwW_1_Fl6BWdBHb5u7moM_1_JXC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Plane", "plane_Sketch_FNk1sR7rQTk48Qm_1_JZC")
origin = App.Vector(28.91876000000000,-25.01888000000000,-25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FNk1sR7rQTk48Qm_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("Sketcher::SketchObject","Sketch_FNk1sR7rQTk48Qm_1_JZC")
App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FNk1sR7rQTk48Qm_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC").addGeometry(Part.LineSegment(App.Vector(19.73742000000000,7.59693000000000,0.00000000000000),App.Vector(6.57914000000000,7.59693000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC").addGeometry(Part.LineSegment(App.Vector(6.57914000000000,7.59693000000000,0.00000000000000),App.Vector(6.57914000000000,-7.59693000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC").addGeometry(Part.LineSegment(App.Vector(19.73742000000000,-7.59693000000000,0.00000000000000),App.Vector(6.57914000000000,-7.59693000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC").addGeometry(Part.LineSegment(App.Vector(19.73742000000000,7.59693000000000,0.00000000000000),App.Vector(19.73742000000000,-7.59693000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Pad","Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC")
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC")
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FNk1sR7rQTk48Qm_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FNk1sR7rQTk48Qm_1_F5hCLTuEFNTMmXu_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Plane", "plane_Sketch_FbXDTPsbmAFjSRm_1_JhC")
origin = App.Vector(27.78203000000000,44.72822000000000,-25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FbXDTPsbmAFjSRm_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("Sketcher::SketchObject","Sketch_FbXDTPsbmAFjSRm_1_JhC")
App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FbXDTPsbmAFjSRm_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC").addGeometry(Part.LineSegment(App.Vector(26.14844000000000,-9.34342000000000,0.00000000000000),App.Vector(8.71614000000000,-9.34342000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC").addGeometry(Part.LineSegment(App.Vector(8.71614000000000,-9.34342000000000,0.00000000000000),App.Vector(8.71614000000000,9.34342000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC").addGeometry(Part.LineSegment(App.Vector(26.14844000000000,9.34342000000000,0.00000000000000),App.Vector(8.71614000000000,9.34342000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC").addGeometry(Part.LineSegment(App.Vector(26.14844000000000,9.34342000000000,0.00000000000000),App.Vector(26.14844000000000,-9.34342000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Pad","Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC")
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC")
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FbXDTPsbmAFjSRm_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FbXDTPsbmAFjSRm_1_FDeNmBq5dsGaXWG_1_JhC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Plane", "plane_Sketch_Fg1ZxpWWRmWf7Jk_1_JlC")
origin = App.Vector(-22.97008000000000,44.40762000000000,-25.40000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
z_axis=App.Vector(0.00000000000000,0.00000000000000,-1.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fg1ZxpWWRmWf7Jk_1_JlC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("Sketcher::SketchObject","Sketch_Fg1ZxpWWRmWf7Jk_1_JlC")
App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fg1ZxpWWRmWf7Jk_1_JlC"), [""])
App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC").addGeometry(Part.LineSegment(App.Vector(-29.69233000000000,-9.74600000000000,0.00000000000000),App.Vector(-9.89744000000000,-9.74600000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC").addGeometry(Part.LineSegment(App.Vector(-9.89744000000000,-9.74600000000000,0.00000000000000),App.Vector(-9.89744000000000,9.74601000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC").addGeometry(Part.LineSegment(App.Vector(-29.69233000000000,9.74601000000000,0.00000000000000),App.Vector(-9.89744000000000,9.74601000000000,0.00000000000000)),False)

App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC").addGeometry(Part.LineSegment(App.Vector(-29.69233000000000,-9.74600000000000,0.00000000000000),App.Vector(-29.69233000000000,9.74601000000000,0.00000000000000)),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_F0mbsH6ly2wQmyE_0").newObject("PartDesign::Pad","Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC")
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").Profile = App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC")
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").Length = 50.800000000000004
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fg1ZxpWWRmWf7Jk_1_JlC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").Type = 4
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fg1ZxpWWRmWf7Jk_1_FvZOfAAYAKpZVgv_1_JlC").Offset = 0
App.ActiveDocument.recompute()

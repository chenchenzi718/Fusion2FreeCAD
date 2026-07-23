import sys
sys.path.append(r"D:\name_and_rebuild\FreeCAD\lib")
import FreeCAD as App
import Part
App.newDocument("00694843")
App.ActiveDocument.addObject("PartDesign::Body","Body_FQGgH2GuMlV8xxO_0")
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").Label = "Body_FQGgH2GuMlV8xxO_0"
App.ActiveDocument.recompute()

plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_FQGgH2GuMlV8xxO_0_JGC")
origin = App.Vector(0.00000000000000,0.00000000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FQGgH2GuMlV8xxO_0_JGC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_FQGgH2GuMlV8xxO_0_JGC")
App.ActiveDocument.getObject("Sketch_FQGgH2GuMlV8xxO_0_JGC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FQGgH2GuMlV8xxO_0_JGC"), [""])
App.ActiveDocument.getObject("Sketch_FQGgH2GuMlV8xxO_0_JGC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FQGgH2GuMlV8xxO_0_JGC").addGeometry(Part.Circle(App.Vector(0.10056000000000,-0.01075000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),19.05000000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FQGgH2GuMlV8xxO_0_JGC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FQGgH2GuMlV8xxO_0_JGC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pad","Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC")
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").Profile = App.ActiveDocument.getObject("Sketch_FQGgH2GuMlV8xxO_0_JGC")
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").Length = 15.875
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").Direction = (0, 0, 1)
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FQGgH2GuMlV8xxO_0_JGC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").Type = 4
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FQGgH2GuMlV8xxO_0_FX9731lHrXzgyVu_0_JGC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_FArXQYQA5LvpZJD_1_JJC")
origin = App.Vector(0.10056000000000,-15.87500000000000,-0.01075000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FArXQYQA5LvpZJD_1_JJC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_FArXQYQA5LvpZJD_1_JJC")
App.ActiveDocument.getObject("Sketch_FArXQYQA5LvpZJD_1_JJC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FArXQYQA5LvpZJD_1_JJC"), [""])
App.ActiveDocument.getObject("Sketch_FArXQYQA5LvpZJD_1_JJC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FArXQYQA5LvpZJD_1_JJC").addGeometry(Part.Circle(App.Vector(-0.10056000000000,0.01075000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),9.52500000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FArXQYQA5LvpZJD_1_JJC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FArXQYQA5LvpZJD_1_JJC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pocket","Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC")
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").Profile = App.ActiveDocument.getObject("Sketch_FArXQYQA5LvpZJD_1_JJC")
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").Length = 12.700000000000001
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FArXQYQA5LvpZJD_1_JJC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").Type = 4
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FArXQYQA5LvpZJD_1_F066vuJ3o6BoIXX_1_JJC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_FeTHkup991SrPpY_1_JNC")
origin = App.Vector(0.00000000000000,-3.17500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FeTHkup991SrPpY_1_JNC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_FeTHkup991SrPpY_1_JNC")
App.ActiveDocument.getObject("Sketch_FeTHkup991SrPpY_1_JNC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FeTHkup991SrPpY_1_JNC"), [""])
App.ActiveDocument.getObject("Sketch_FeTHkup991SrPpY_1_JNC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FeTHkup991SrPpY_1_JNC").addGeometry(Part.Circle(App.Vector(0.00000000000000,7.38003000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FeTHkup991SrPpY_1_JNC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FeTHkup991SrPpY_1_JNC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pocket","Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC")
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").Profile = App.ActiveDocument.getObject("Sketch_FeTHkup991SrPpY_1_JNC")
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FeTHkup991SrPpY_1_JNC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").Type = 4
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FeTHkup991SrPpY_1_FLx6kZV48carzMT_1_JNC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_FrrPTcTQhcEPJ98_1_JRC")
origin = App.Vector(0.00000000000000,-3.17500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FrrPTcTQhcEPJ98_1_JRC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_FrrPTcTQhcEPJ98_1_JRC")
App.ActiveDocument.getObject("Sketch_FrrPTcTQhcEPJ98_1_JRC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FrrPTcTQhcEPJ98_1_JRC"), [""])
App.ActiveDocument.getObject("Sketch_FrrPTcTQhcEPJ98_1_JRC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FrrPTcTQhcEPJ98_1_JRC").addGeometry(Part.Circle(App.Vector(0.00000000000000,-7.15490000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FrrPTcTQhcEPJ98_1_JRC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FrrPTcTQhcEPJ98_1_JRC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pocket","Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC")
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").Profile = App.ActiveDocument.getObject("Sketch_FrrPTcTQhcEPJ98_1_JRC")
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FrrPTcTQhcEPJ98_1_JRC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").Type = 4
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FrrPTcTQhcEPJ98_1_F7bsUSvcO4UFTQ8_1_JRC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_FwW3IpuZnLdwShN_1_JVC")
origin = App.Vector(0.00000000000000,-3.17500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FwW3IpuZnLdwShN_1_JVC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_FwW3IpuZnLdwShN_1_JVC")
App.ActiveDocument.getObject("Sketch_FwW3IpuZnLdwShN_1_JVC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FwW3IpuZnLdwShN_1_JVC"), [""])
App.ActiveDocument.getObject("Sketch_FwW3IpuZnLdwShN_1_JVC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FwW3IpuZnLdwShN_1_JVC").addGeometry(Part.Circle(App.Vector(7.32782000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FwW3IpuZnLdwShN_1_JVC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FwW3IpuZnLdwShN_1_JVC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pocket","Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC")
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").Profile = App.ActiveDocument.getObject("Sketch_FwW3IpuZnLdwShN_1_JVC")
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FwW3IpuZnLdwShN_1_JVC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").Type = 4
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FwW3IpuZnLdwShN_1_FQ2M1Ohf5AkMqL5_1_JVC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_F5sms8eshuNzd7G_1_JZC")
origin = App.Vector(0.00000000000000,-3.17500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_F5sms8eshuNzd7G_1_JZC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_F5sms8eshuNzd7G_1_JZC")
App.ActiveDocument.getObject("Sketch_F5sms8eshuNzd7G_1_JZC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_F5sms8eshuNzd7G_1_JZC"), [""])
App.ActiveDocument.getObject("Sketch_F5sms8eshuNzd7G_1_JZC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_F5sms8eshuNzd7G_1_JZC").addGeometry(Part.Circle(App.Vector(-7.42405000000000,0.00000000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_F5sms8eshuNzd7G_1_JZC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_F5sms8eshuNzd7G_1_JZC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pocket","Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC")
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").Profile = App.ActiveDocument.getObject("Sketch_F5sms8eshuNzd7G_1_JZC")
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_F5sms8eshuNzd7G_1_JZC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").Type = 4
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").UpToFace = None
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").Reversed = 0
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").Midplane = 0
App.ActiveDocument.getObject("Extrude_F5sms8eshuNzd7G_1_FurcpMo8tDy5opk_1_JZC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_Ftn9XKSJWZM5sVB_1_JdC")
origin = App.Vector(0.00000000000000,-3.17500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Ftn9XKSJWZM5sVB_1_JdC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_Ftn9XKSJWZM5sVB_1_JdC")
App.ActiveDocument.getObject("Sketch_Ftn9XKSJWZM5sVB_1_JdC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Ftn9XKSJWZM5sVB_1_JdC"), [""])
App.ActiveDocument.getObject("Sketch_Ftn9XKSJWZM5sVB_1_JdC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Ftn9XKSJWZM5sVB_1_JdC").addGeometry(Part.Circle(App.Vector(-5.25466000000000,5.17448000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Ftn9XKSJWZM5sVB_1_JdC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Ftn9XKSJWZM5sVB_1_JdC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pocket","Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC")
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").Profile = App.ActiveDocument.getObject("Sketch_Ftn9XKSJWZM5sVB_1_JdC")
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Ftn9XKSJWZM5sVB_1_JdC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").Type = 4
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Ftn9XKSJWZM5sVB_1_FSdgVGiSgMm3nLz_1_JdC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_Fif9xl9711N3Fmo_1_JhC")
origin = App.Vector(0.00000000000000,-3.17500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fif9xl9711N3Fmo_1_JhC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_Fif9xl9711N3Fmo_1_JhC")
App.ActiveDocument.getObject("Sketch_Fif9xl9711N3Fmo_1_JhC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fif9xl9711N3Fmo_1_JhC"), [""])
App.ActiveDocument.getObject("Sketch_Fif9xl9711N3Fmo_1_JhC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fif9xl9711N3Fmo_1_JhC").addGeometry(Part.Circle(App.Vector(5.30305000000000,4.84907000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fif9xl9711N3Fmo_1_JhC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fif9xl9711N3Fmo_1_JhC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pocket","Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC")
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").Profile = App.ActiveDocument.getObject("Sketch_Fif9xl9711N3Fmo_1_JhC")
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fif9xl9711N3Fmo_1_JhC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").Type = 4
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fif9xl9711N3Fmo_1_FgvIrI63SMlVaDx_1_JhC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_Fmm3wiz2WQbw7zE_1_JlC")
origin = App.Vector(0.00000000000000,-3.17500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_Fmm3wiz2WQbw7zE_1_JlC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_Fmm3wiz2WQbw7zE_1_JlC")
App.ActiveDocument.getObject("Sketch_Fmm3wiz2WQbw7zE_1_JlC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_Fmm3wiz2WQbw7zE_1_JlC"), [""])
App.ActiveDocument.getObject("Sketch_Fmm3wiz2WQbw7zE_1_JlC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_Fmm3wiz2WQbw7zE_1_JlC").addGeometry(Part.Circle(App.Vector(-5.21850000000000,-4.94935000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_Fmm3wiz2WQbw7zE_1_JlC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_Fmm3wiz2WQbw7zE_1_JlC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pocket","Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC")
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").Profile = App.ActiveDocument.getObject("Sketch_Fmm3wiz2WQbw7zE_1_JlC")
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_Fmm3wiz2WQbw7zE_1_JlC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").Type = 4
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").UpToFace = None
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").Reversed = 0
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").Midplane = 0
App.ActiveDocument.getObject("Extrude_Fmm3wiz2WQbw7zE_1_FsGMnczlB2zObni_1_JlC").Offset = 0
App.ActiveDocument.recompute()
plane = App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Plane", "plane_Sketch_FuL8VOE0az3mKhc_1_JpC")
origin = App.Vector(0.00000000000000,-3.17500000000000,0.00000000000000)
x_axis=App.Vector(1.00000000000000,0.00000000000000,0.00000000000000)
y_axis=App.Vector(-0.00000000000000,0.00000000000000,1.00000000000000)
z_axis=App.Vector(0.00000000000000,-1.00000000000000,0.00000000000000)
rot = App.Rotation(x_axis,y_axis,z_axis)
App.ActiveDocument.getObject("plane_Sketch_FuL8VOE0az3mKhc_1_JpC").Placement = App.Placement(origin,rot)
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("Sketcher::SketchObject","Sketch_FuL8VOE0az3mKhc_1_JpC")
App.ActiveDocument.getObject("Sketch_FuL8VOE0az3mKhc_1_JpC").AttachmentSupport = (App.ActiveDocument.getObject("plane_Sketch_FuL8VOE0az3mKhc_1_JpC"), [""])
App.ActiveDocument.getObject("Sketch_FuL8VOE0az3mKhc_1_JpC").MapMode = "FlatFace"
App.ActiveDocument.getObject("Sketch_FuL8VOE0az3mKhc_1_JpC").addGeometry(Part.Circle(App.Vector(5.30305000000000,-4.91319000000000,0.00000000000000),App.Vector(0.00000000000000,0.00000000000000,1.00000000000000),1.58750000000000),False)

App.ActiveDocument.recompute()
detect_cnt=App.ActiveDocument.getObject("Sketch_FuL8VOE0az3mKhc_1_JpC").detectMissingPointOnPointConstraints()
(App.ActiveDocument.getObject("Sketch_FuL8VOE0az3mKhc_1_JpC").makeMissingPointOnPointCoincident()) if detect_cnt>0 else None
App.ActiveDocument.recompute()
App.ActiveDocument.getObject("Body_FQGgH2GuMlV8xxO_0").newObject("PartDesign::Pocket","Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC")
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").Profile = App.ActiveDocument.getObject("Sketch_FuL8VOE0az3mKhc_1_JpC")
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").Length = 25.400000000000002
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").TaperAngle = 0.000000
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").Direction = (0, 0, -1)
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").ReferenceAxis = (App.ActiveDocument.getObject("Sketch_FuL8VOE0az3mKhc_1_JpC"), ["N_Axis"])
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").AlongSketchNormal = 1
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").Type = 4
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").UpToFace = None
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").Reversed = 0
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").Midplane = 0
App.ActiveDocument.getObject("Extrude_FuL8VOE0az3mKhc_1_FsiqZQMFDgZhxka_1_JpC").Offset = 0
App.ActiveDocument.recompute()

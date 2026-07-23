"""
Configuration and constants for Fusion2Free.

FreeCAD paths can be configured via environment variables or by modifying
FREECAD_CMD_PATH directly.
"""

import os


# ---------------------------------------------------------------------------
# FreeCAD version mode
# ---------------------------------------------------------------------------
# 0  = custom build forked from FreeCAD (the branch used in our experiments)
# 1  = official FreeCAD 1.0 release
FREECAD_VERSION_MODE = 0

# ---------------------------------------------------------------------------
# FreeCAD command-line path
# ---------------------------------------------------------------------------
# Override with environment variable FREECAD_CMD if not set.
FREECAD_CMD_PATH = os.environ.get(
    "FREECAD_CMD",
    r"D:\path\to\FreeCAD\bin\FreeCADCmd.exe",
)

# ---------------------------------------------------------------------------
# Line ending & recompute helper (used when generating FreeCAD Python scripts)
# ---------------------------------------------------------------------------
EOL = "\n"
RECOMPUTE = f"App.ActiveDocument.recompute(){EOL}"

# ---------------------------------------------------------------------------
# FreeCAD library path (for scripts that import FreeCAD modules directly)
# ---------------------------------------------------------------------------
FREECAD_LIB_PATH = os.environ.get(
    "FREECAD_LIB",
    r"D:\path\to\FreeCAD\lib",
)
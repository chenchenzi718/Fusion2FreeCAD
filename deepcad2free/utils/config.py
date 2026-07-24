"""
Configuration and constants for DeepCAD2Free.

All user-facing paths and defaults are centralized here. Override any value
via environment variable or by editing this file directly.
"""

import os

# ---------------------------------------------------------------------------
# FreeCAD command-line path (required for validation & bbox)
# ---------------------------------------------------------------------------
FREECAD_CMD_PATH = os.environ.get(
    "FREECAD_CMD",
    r"D:\path\to\FreeCAD\bin\FreeCADCmd.exe",
)

# ---------------------------------------------------------------------------
# Directory paths (relative to project root; can be absolute)
# ---------------------------------------------------------------------------
INPUT_DIR      = "data/cad_json"        # Raw DeepCAD JSON
REPAIR_DIR     = "data/cad_json_repair" # Cleaned JSON
OUTPUT_PY_DIR  = "data/cad_py_repair"   # Generated FreeCAD .py scripts
OUTPUT_FREE_DIR = "data/cad_free_repair" # Validated .FCStd files
LOG_DIR        = "logging"              # Log files & SQLite database

# ---------------------------------------------------------------------------
# Database paths
# ---------------------------------------------------------------------------
DB_PATH       = os.path.join(LOG_DIR, "log.db")
NAME_DB_PATH  = "utils/name_mapping.db"

# ---------------------------------------------------------------------------
# Processing defaults
# ---------------------------------------------------------------------------
DEFAULT_PROCESSES = 8     # Max worker processes (actual: min(cpu-1, this))
DEFAULT_BATCH_SIZE = 50   # DB flush interval

# ---------------------------------------------------------------------------
# Script generation constants
# ---------------------------------------------------------------------------
EOL       = "\n"
RECOMPUTE = f"App.ActiveDocument.recompute(){EOL}"
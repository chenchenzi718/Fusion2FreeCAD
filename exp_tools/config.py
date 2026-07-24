"""
Configuration for exp_tools -- experiment utilities for parametric CAD models.

All user-facing paths and defaults are centralized here. Override any value
via environment variable or by editing this file directly.
"""

import os

# ---------------------------------------------------------------------------
# FreeCAD command-line path (required for running experiments)
# ---------------------------------------------------------------------------
FREECAD_CMD_PATH = os.environ.get(
    "FREECAD_CMD",
    r"D:\path\to\FreeCAD\bin\FreeCADCmd.exe",
)

# ---------------------------------------------------------------------------
# Dataset path -- directory containing *_free.py model scripts
# ---------------------------------------------------------------------------
DATASET_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "dataset",
)

# ---------------------------------------------------------------------------
# Output path -- where experiment results are written
# ---------------------------------------------------------------------------
OUTPUT_DIR = "exp_output"

# ---------------------------------------------------------------------------
# Experiment parameters
# ---------------------------------------------------------------------------
SCALE_MIN = 0.1       # Lower bound for random scale factor
SCALE_MAX = 0.9       # Upper bound for random scale factor
NUM_SCALES = 5        # Number of random scales per feature
RANDOM_SEED = 42      # Random seed for reproducibility

# ---------------------------------------------------------------------------
# Processing defaults
# ---------------------------------------------------------------------------
DEFAULT_PROCESSES = 1  # exp_tools runs sequentially by default (FreeCAD license)
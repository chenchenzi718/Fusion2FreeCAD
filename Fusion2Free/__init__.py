"""
Fusion2Free -- Convert Fusion 360 (DeepCAD) JSON models to FreeCAD Python scripts.

Parts:
  - Part 1: Conversion engine (fusion2free package)
  - Part 2: Experiment tools (exp_tools package)

Author: Fusion2Free Contributors
License: MIT
"""

__version__ = "1.0.0"

from .converter import fusion2free
from .cleaner import repair_fusion

__all__ = ["fusion2free", "repair_fusion"]
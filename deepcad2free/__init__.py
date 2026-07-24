"""
DeepCAD2Free -- Convert DeepCAD JSON models to FreeCAD Python scripts.

Parts:
  - Part 1: Conversion engine (deepcad2free package)
  - Part 2: Experiment tools (exp_tools package)

Author: DeepCAD2Free Contributors
License: MIT
"""

__version__ = "1.0.0"

from .converter import deepcad2free
from .cleaner import repair_deepcad

__all__ = ["deepcad2free", "repair_deepcad"]
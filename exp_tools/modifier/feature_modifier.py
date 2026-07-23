"""
Feature modifier -- directly modify feature parameters in FreeCAD .FCStd files.

Usage (inside FreeCADCmd):
    FreeCADCmd.exe feature_modifier.py <fcstd_path> <target_feature_index>

Supported feature types:
  - PartDesign::Pad      -> increments Length by 0.1 mm
  - PartDesign::Pocket   -> increments Length by 0.1 mm
  - PartDesign::Fillet   -> increments Radius by 0.01 mm
  - PartDesign::Chamfer  -> increments Size by 0.01 mm
"""

import sys
import os

import FreeCAD as App


# ================================================================
# Arguments
# ================================================================
if len(sys.argv) < 3:
    print("Usage: feature_modifier.py <fcstd_path> <target_feature_index>")
    sys.exit(1)

fcstd_path = sys.argv[1]
target_idx = int(sys.argv[2])

# ================================================================
# Logging level
# ================================================================
App.setLogLevel("Default", "Message")
App.setLogLevel("App", "Message")
App.setLogLevel("Gui", "Message")
App.setLogLevel("Base", "Message")
App.setLogLevel("Progress", 0)
App.setLogLevel("Recompute", "Error")

# ================================================================
# Open document
# ================================================================
doc = App.openDocument(fcstd_path)

# ================================================================
# Collect target features
# ================================================================
target_types = {
    "PartDesign::Pad",
    "PartDesign::Pocket",
    "PartDesign::Fillet",
    "PartDesign::Chamfer",
}

features = [obj for obj in doc.Objects if obj.TypeId in target_types]

# Print detected features
print("Detected Features:")
for i, feat in enumerate(features):
    print(f"  [{i}] {feat.Name} ({feat.TypeId})")

# ================================================================
# Validate index
# ================================================================
if target_idx < 0 or target_idx >= len(features):
    print(f"Error: Invalid feature index {target_idx} (found {len(features)} features)")
    App.closeDocument(doc.Name)
    sys.exit(1)

feat = features[target_idx]

print(f"\nProcessing feature: {feat.Name} ({feat.TypeId})")

# ================================================================
# Modify feature
# ================================================================
try:
    if feat.TypeId == "PartDesign::Pad":
        old_len = feat.Length.Value
        doc.recompute()
        feat.Length = old_len + 0.1
        feat.recompute()
        doc.recompute()
        print(f"  Pad Length: {old_len} -> {feat.Length.Value}")

    elif feat.TypeId == "PartDesign::Pocket":
        old_len = feat.Length.Value
        doc.recompute()
        feat.Length = old_len + 0.1
        feat.recompute()
        doc.recompute()
        print(f"  Pocket Length: {old_len} -> {feat.Length.Value}")

    elif feat.TypeId == "PartDesign::Fillet":
        old_r = feat.Radius.Value
        doc.recompute()
        feat.Radius = old_r + 0.01
        feat.recompute()
        doc.recompute()
        print(f"  Fillet Radius: {old_r} -> {feat.Radius.Value}")

    elif feat.TypeId == "PartDesign::Chamfer":
        old_s = feat.Size.Value
        doc.recompute()
        feat.Size = old_s + 0.01
        feat.recompute()
        doc.recompute()
        print(f"  Chamfer Size: {old_s} -> {feat.Size.Value}")

except Exception as e:
    print(f"\nException: {e}")
    sys.exit(1)

# ================================================================
# Close
# ================================================================
App.closeDocument(doc.Name)
print("\nFinished.")
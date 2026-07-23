"""
Model test script -- load FreeCAD Python scripts, scan features, or modify parameters.

Modes (controlled by feature_idx magic values):
  - SINGLE  (default): modify the Length of a specific Pad/Pocket feature to a random value
  - SCAN    (feature_idx=999999): select a random feature (excluding first) and report
  - TEST    (feature_idx=888888): modify a specific feature by scale factor
  - SCAN_ALL (feature_idx=777777): scan and return ALL Pad/Pocket features

Usage (inside FreeCADCmd):
    FreeCADCmd.exe test_model.py <model_file.py> [feature_idx] [min_len|test_feature_idx] [max_len|scale_factor]

Note: The model_file.py is executed to rebuild the model, then features are scanned/modified.
"""

import sys
import os
import random
import json

import FreeCAD as App


# ---------------------------------------------------------------------------
# Logging helper
# ---------------------------------------------------------------------------

def log_msg(msg):
    """Output to both console and FreeCAD log."""
    print(msg)
    App.Console.PrintMessage(msg + "\n")


# ---------------------------------------------------------------------------
# Parse arguments
# ---------------------------------------------------------------------------
log_msg("[MODIFIER] sys.argv: " + str(sys.argv))

this_script = os.path.basename(__file__)
py_files = []
for arg in sys.argv:
    if arg.endswith(".py") and os.path.basename(arg) != this_script:
        if arg not in py_files:
            py_files.append(arg)

other_args = [arg for arg in sys.argv if not arg.endswith(".py")]

log_msg("[MODIFIER] Found Python files: " + str(py_files))
log_msg("[MODIFIER] Other args: " + str(other_args))

if len(py_files) < 1:
    log_msg("[MODIFIER ERROR] No model file found in arguments")
    sys.exit(1)

model_file = py_files[0]

# Parse numeric args
numeric_args = []
for arg in other_args:
    try:
        if "." in arg:
            numeric_args.append(float(arg))
        else:
            numeric_args.append(int(arg))
    except ValueError:
        pass

log_msg("[MODIFIER] Numeric args: " + str(numeric_args))

# Get parameters with defaults
feature_idx = int(numeric_args[0]) if len(numeric_args) > 0 else 0
min_len = float(numeric_args[1]) if len(numeric_args) > 1 else 10.0
max_len = float(numeric_args[2]) if len(numeric_args) > 2 else 50.0

# ---------------------------------------------------------------------------
# Determine mode
# ---------------------------------------------------------------------------
MODE = "single"
if feature_idx == 999999:
    MODE = "scan"
elif feature_idx == 888888:
    MODE = "test"
    test_feature_idx = int(min_len)
    test_scale_factor = max_len
    test_gradient_name = "unknown"
    for arg in other_args:
        if arg == "888888":
            continue
        if "\\" in arg or "/" in arg:
            continue
        try:
            float(arg)
            continue
        except ValueError:
            test_gradient_name = arg
            break
elif feature_idx == 777777:
    MODE = "scan_all"

log_msg("")
log_msg("=" * 70)
log_msg("[MODIFIER] Configuration")
log_msg("=" * 70)
log_msg("[MODIFIER] Mode: %s" % MODE.upper())
log_msg("[MODIFIER] Model file: %s" % model_file)
if MODE == "single":
    log_msg("[MODIFIER] Feature index: %d" % feature_idx)
    log_msg("[MODIFIER] Length range: [%.1f, %.1f] mm" % (min_len, max_len))
elif MODE == "test":
    log_msg("[MODIFIER] Test feature index: %d" % test_feature_idx)
    log_msg("[MODIFIER] Scale factor: %.2f" % test_scale_factor)
    log_msg("[MODIFIER] Gradient name: %s" % test_gradient_name)
log_msg("=" * 70)
log_msg("")

# ---------------------------------------------------------------------------
# Step 1: Execute the model script
# ---------------------------------------------------------------------------
log_msg("")
log_msg("=" * 70)
log_msg("[MODIFIER] Step 1: Executing original FreeCAD model script...")
log_msg("=" * 70)
log_msg("[MODIFIER] Output from original script follows below:")
log_msg("-" * 70)

if not os.path.exists(model_file):
    log_msg("[MODIFIER ERROR] File not found: %s" % model_file)
    sys.exit(1)

model_dir = os.path.dirname(os.path.abspath(model_file))
os.chdir(model_dir)

with open(model_file, "r") as f:
    code = f.read()

try:
    exec(code)
    log_msg("-" * 70)
    log_msg("[MODIFIER] Original script execution completed")
    log_msg("=" * 70)
except Exception as e:
    log_msg("-" * 70)
    log_msg("[MODIFIER ERROR] Original script failed: %s" % e)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Find all Pad/Pocket features
# ---------------------------------------------------------------------------
doc = App.ActiveDocument
if not doc:
    log_msg("[MODIFIER ERROR] No active document")
    sys.exit(1)

features = []
for obj in doc.Objects:
    if hasattr(obj, "Length") and obj.TypeId in (
        "PartDesign::Pad",
        "PartDesign::Pocket",
    ):
        features.append(obj)

# =========================================================================
# SCAN MODE
# =========================================================================
if MODE == "scan":
    log_msg("")
    log_msg("=" * 70)
    log_msg("[MODIFIER] SCAN MODE")
    log_msg("=" * 70)

    if not features:
        log_msg("[MODIFIER ERROR] No features with Length found")
        result = {"status": "error", "error": "no_features"}
    else:
        log_msg("[MODIFIER] Found %d features:" % len(features))
        for i, feat in enumerate(features):
            log_msg(
                "[MODIFIER]   [%d] %s (%s): %.2f mm"
                % (i, feat.Name, feat.TypeId, float(feat.Length))
            )

        if len(features) > 1:
            target_idx = random.randint(1, round(len(features) / 2))
            selection_reason = "random (excluding first)"
        else:
            target_idx = 0
            selection_reason = "only feature available"

        target = features[target_idx]
        original_len = float(target.Length)

        log_msg("")
        log_msg("[MODIFIER] Selected feature: [%d] %s" % (target_idx, target.Name))
        log_msg("[MODIFIER] Selection reason: %s" % selection_reason)
        log_msg("[MODIFIER] Original length: %.2f mm" % original_len)

        result = {
            "status": "success",
            "feature_idx": target_idx,
            "feature_name": target.Name,
            "feature_type": target.TypeId,
            "original_length": original_len,
            "total_features": len(features),
            "selection_reason": selection_reason,
        }

    log_msg("")
    log_msg("[MODIFIER] JSON_RESULT: " + json.dumps(result))
    os._exit(0)

# =========================================================================
# SCAN_ALL MODE
# =========================================================================
if MODE == "scan_all":
    log_msg("")
    log_msg("=" * 70)
    log_msg("[MODIFIER] SCAN_ALL MODE")
    log_msg("=" * 70)

    if not features:
        log_msg("[MODIFIER ERROR] No features with Length found")
        result = {"status": "error", "error": "no_features"}
    else:
        log_msg("[MODIFIER] Found %d features:" % len(features))
        for i, feat in enumerate(features):
            log_msg(
                "[MODIFIER]   [%d] %s (%s): %.2f mm"
                % (i, feat.Name, feat.TypeId, float(feat.Length))
            )

        features_list = []
        for i in range(len(features)):
            feat = features[i]
            features_list.append(
                {
                    "idx": i,
                    "name": feat.Name,
                    "type": feat.TypeId,
                    "original_length": float(feat.Length),
                }
            )

        result = {
            "status": "success",
            "total_features": len(features),
            "testable_features": features_list,
        }

    log_msg("")
    log_msg("[MODIFIER] JSON_RESULT: " + json.dumps(result))
    os._exit(0)

# =========================================================================
# SINGLE MODE or TEST MODE -- modify feature
# =========================================================================
log_msg("")
log_msg("=" * 70)
log_msg("[MODIFIER] Step 2: Modifying pad length...")
log_msg("=" * 70)

try:
    log_msg("[MODIFIER] Document name: %s" % doc.Name)

    if not features:
        log_msg("[MODIFIER ERROR] No features with Length found")
        sys.exit(1)

    log_msg("[MODIFIER] Found %d features:" % len(features))
    for i, feat in enumerate(features):
        log_msg(
            "[MODIFIER]   [%d] %s (%s): %.2f mm"
            % (i, feat.Name, feat.TypeId, float(feat.Length))
        )

    if MODE == "test":
        target_idx = test_feature_idx
        scale_factor = test_scale_factor
        gradient_name = test_gradient_name
        log_msg(
            "[MODIFIER] Gradient: %s (%.2fx)" % (gradient_name, scale_factor)
        )
    else:
        target_idx = feature_idx

    if target_idx >= len(features):
        log_msg(
            "[MODIFIER ERROR] Index %d out of range (max: %d)"
            % (target_idx, len(features) - 1)
        )
        sys.exit(1)

    target = features[target_idx]
    original = float(target.Length)

    if MODE == "test":
        new_len = original * scale_factor
    else:
        new_len = random.uniform(min_len, max_len)

    log_msg("")
    log_msg("[MODIFIER] Target feature: [%d] %s" % (target_idx, target.Name))
    log_msg("[MODIFIER]   Original length: %.2f mm" % original)
    if MODE == "test":
        log_msg("[MODIFIER]   Scale factor: %.2fx" % scale_factor)
    log_msg("[MODIFIER]   New length: %.2f mm" % new_len)

    doc.recompute()
    target.Length = new_len
    target.recompute()
    doc.recompute()

    log_msg("")
    log_msg("=" * 70)
    log_msg("[MODIFIER] SUMMARY")
    log_msg("=" * 70)
    log_msg("[MODIFIER] Model: %s" % os.path.basename(model_file))
    if MODE == "test":
        log_msg("[MODIFIER] Gradient: %s" % gradient_name)
        log_msg("[MODIFIER] Scale factor: %.2fx" % scale_factor)
    log_msg("[MODIFIER] Modified feature: [%d] %s" % (target_idx, target.Name))
    log_msg("[MODIFIER] Result: SUCCESS")
    log_msg("=" * 70)
    log_msg("")

    os._exit(0)

except Exception as e:
    log_msg("[MODIFIER ERROR] %s" % e)
    import traceback

    traceback.print_exc()
    os._exit(1)
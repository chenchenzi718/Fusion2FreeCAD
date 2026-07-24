"""
Model test script -- load FreeCAD Python scripts, scan features, or modify parameters.

Modes (controlled by the first non-.py argument):
  - scan   : scan and return ALL Pad/Pocket features as JSON
  - test   : modify a specific feature by scale factor, optionally export BRep

Usage (inside FreeCADCmd):
    # Scan all features
    FreeCADCmd.exe test_model.py <model_file.py> scan

    # Modify feature with scale factor
    FreeCADCmd.exe test_model.py <model_file.py> test <feature_idx> <scale_factor>
                                            [orig_brep_path] [mod_brep_path]

Note: The model_file.py is executed to rebuild the model, then features are
scanned or modified.
"""

import sys
import os
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

# Determine mode from first string token
MODE = None
test_args = {}
for arg in other_args:
    if arg == "scan":
        MODE = "scan"
        break
    elif arg == "test":
        MODE = "test"
        # Parse remaining args: feature_idx, scale_factor, [orig_brep], [mod_brep]
        rest = other_args[other_args.index("test") + 1:]
        try:
            test_args["feature_idx"] = int(rest[0])
            test_args["scale_factor"] = float(rest[1])
        except (IndexError, ValueError) as e:
            log_msg("[MODIFIER ERROR] 'test' requires: <feature_idx> <scale_factor>: %s" % e)
            sys.exit(1)
        if len(rest) > 2:
            test_args["orig_brep"] = rest[2]
        if len(rest) > 3:
            test_args["mod_brep"] = rest[3]
        break

if MODE is None:
    log_msg("[MODIFIER ERROR] No mode specified. Use 'scan' or 'test'.")
    sys.exit(1)

log_msg("")
log_msg("=" * 70)
log_msg("[MODIFIER] Configuration")
log_msg("=" * 70)
log_msg("[MODIFIER] Mode: %s" % MODE.upper())
log_msg("[MODIFIER] Model file: %s" % model_file)
if MODE == "test":
    log_msg("[MODIFIER] Feature index: %d" % test_args["feature_idx"])
    log_msg("[MODIFIER] Scale factor: %.4f" % test_args["scale_factor"])
    if "orig_brep" in test_args:
        log_msg("[MODIFIER] Original BRep: %s" % test_args["orig_brep"])
    if "mod_brep" in test_args:
        log_msg("[MODIFIER] Modified BRep: %s" % test_args["mod_brep"])
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


def _export_brep(path):
    """Export the shape of all PartDesign::Body objects to a BRep file."""
    for obj in doc.Objects:
        if obj.TypeId == "PartDesign::Body":
            shape = obj.Shape
            shape.exportBrep(path)
            log_msg("[MODIFIER] Exported BRep: %s (Body: %s)" % (path, obj.Name))


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
                "[MODIFIER]   [%d] %s (%s): %.4f mm"
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
            "features": features_list,
        }

    log_msg("")
    log_msg("[MODIFIER] JSON_RESULT: " + json.dumps(result))
    os._exit(0)


# =========================================================================
# TEST MODE -- modify feature by scale factor
# =========================================================================
log_msg("")
log_msg("=" * 70)
log_msg("[MODIFIER] Step 2: Modifying feature by scale factor...")
log_msg("=" * 70)

try:
    log_msg("[MODIFIER] Document name: %s" % doc.Name)

    if not features:
        log_msg("[MODIFIER ERROR] No features with Length found")
        sys.exit(1)

    target_idx = test_args["feature_idx"]
    scale_factor = test_args["scale_factor"]

    if target_idx < 0 or target_idx >= len(features):
        log_msg(
            "[MODIFIER ERROR] Feature index %d out of range (0-%d)"
            % (target_idx, len(features) - 1)
        )
        sys.exit(1)

    target = features[target_idx]
    original_len = float(target.Length)

    # Export original BRep before modification
    if "orig_brep" in test_args:
        os.makedirs(os.path.dirname(os.path.abspath(test_args["orig_brep"])), exist_ok=True)
        _export_brep(test_args["orig_brep"])

    new_len = original_len * scale_factor

    log_msg("")
    log_msg("[MODIFIER] Feature list:")
    for i, feat in enumerate(features):
        log_msg(
            "[MODIFIER]   [%d] %s (%s): %.4f mm"
            % (i, feat.Name, feat.TypeId, float(feat.Length))
        )

    log_msg("")
    log_msg("[MODIFIER] Target feature: [%d] %s" % (target_idx, target.Name))
    log_msg("[MODIFIER]   Original length: %.4f mm" % original_len)
    log_msg("[MODIFIER]   Scale factor: %.4fx" % scale_factor)
    log_msg("[MODIFIER]   New length: %.4f mm" % new_len)

    doc.recompute()
    target.Length = new_len
    target.recompute()
    doc.recompute()

    # Export modified BRep
    if "mod_brep" in test_args:
        os.makedirs(os.path.dirname(os.path.abspath(test_args["mod_brep"])), exist_ok=True)
        _export_brep(test_args["mod_brep"])

    log_msg("")
    log_msg("=" * 70)
    log_msg("[MODIFIER] SUMMARY")
    log_msg("=" * 70)
    log_msg("[MODIFIER] Model: %s" % os.path.basename(model_file))
    log_msg("[MODIFIER] Feature: [%d] %s (%s)" % (target_idx, target.Name, target.TypeId))
    log_msg("[MODIFIER] Scale: %.4fx (%.4f -> %.4f mm)" % (scale_factor, original_len, new_len))
    log_msg("[MODIFIER] Result: SUCCESS")
    log_msg("=" * 70)
    log_msg("")

    os._exit(0)

except Exception as e:
    log_msg("[MODIFIER ERROR] %s" % e)
    import traceback

    traceback.print_exc()
    os._exit(1)
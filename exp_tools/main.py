"""
exp_tools -- Experiment runner for parametric CAD model modification.

Run parameter modification experiments on all models in the dataset directory.
For each model:
  1. Scan all Pad/Pocket features
  2. For each feature, randomly sample scales from [SCALE_MIN, SCALE_MAX]
  3. Modify the feature by scale, export original/modified BRep
  4. Log results, collect a summary CSV

Usage:
    python -m exp_tools.main [--dataset-dir DIR] [--output-dir DIR] [--verbose]
"""

import argparse
import json
import logging
import os
import random
import shutil
import subprocess
import sys
import time

# No tqdm — clean stderr logs only

# ---------------------------------------------------------------------------
# Path setup — ensure project root is on sys.path
# ---------------------------------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from exp_tools.config import (
    FREECAD_CMD_PATH,
    DATASET_DIR,
    OUTPUT_DIR,
    RANDOM_SEED,
    NUM_SCALES,
    SCALE_MIN,
    SCALE_MAX,
)


# ---------------------------------------------------------------------------
# Logging — stderr-based so tqdm (stdout) is not disturbed
# ---------------------------------------------------------------------------

_COLORS = {
    "DEBUG":    "\033[36m",   # cyan
    "INFO":     "\033[32m",   # green
    "WARNING":  "\033[33m",   # yellow
    "ERROR":    "\033[31m",   # red
    "CRITICAL": "\033[35m",   # magenta
}
_RESET = "\033[0m"


class _ColorFormatter(logging.Formatter):
    """ANSI-colored formatter for console; plain text for file."""
    def format(self, record):
        msg = super().format(record)
        color = _COLORS.get(record.levelname, "")
        if color:
            return f"{color}{msg}{_RESET}"
        return msg


def setup_logging(log_path: str, verbose: bool = False):
    """Configure dual handlers: colored stderr console + plain file."""
    log_path = os.path.abspath(log_path)
    os.makedirs(log_path, exist_ok=True)

    log_file = os.path.join(log_path, "experiment.log")
    level = logging.DEBUG if verbose else logging.INFO

    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.setLevel(level)

    fmt_plain = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # File handler — no colors
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(level)
    fh.setFormatter(logging.Formatter(fmt_plain))
    root_logger.addHandler(fh)

    # Console handler — colors, stderr (tqdm uses stdout)
    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(level)
    ch.setFormatter(_ColorFormatter(fmt_plain))
    root_logger.addHandler(ch)

    return logging.getLogger(__name__)


logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Environment helper
# ---------------------------------------------------------------------------

def _clean_env():
    """
    Return a clean environment dict for FreeCADCmd subprocess.

    Removes Python-related variables (PYTHONHOME, PYTHONPATH, VIRTUAL_ENV,
    CONDA_* etc.) that confuse FreeCAD's embedded Python interpreter.
    """
    keep = {
        "PATH", "TEMP", "TMP", "SYSTEMROOT", "SystemRoot",
        "windir", "WINDIR", "COMPUTERNAME", "USERNAME",
        "USERPROFILE", "HOMEDRIVE", "HOMEPATH",
        "NUMBER_OF_PROCESSORS", "OS", "PROCESSOR_ARCHITECTURE",
    }
    env = {}
    for key, value in os.environ.items():
        if key.upper() in keep:
            env[key] = value
    return env


# ---------------------------------------------------------------------------
# FreeCAD runner
# ---------------------------------------------------------------------------

def _run_freecad(script_path, args, timeout_ms=300000):
    """
    Run a FreeCAD script via FreeCADCmd subprocess.

    Returns (stdout, stderr, returncode).
    """
    cmd = [FREECAD_CMD_PATH, script_path] + args
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=_clean_env(),
            timeout=timeout_ms / 1000,
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "TIMEOUT after {}ms".format(timeout_ms), -1
    except Exception as e:
        return "", str(e), -1


# ---------------------------------------------------------------------------
# Step 1: Scan a model
# ---------------------------------------------------------------------------

def scan_model(model_path, model_name, output_subdir):
    """
    Run test_model.py in scan mode. Return the parsed JSON result dict, or None.
    """
    log_file = os.path.join(output_subdir, "scan_all.log")
    json_file = os.path.join(output_subdir, "scan_all.json")

    modifier_dir = os.path.join(PROJECT_ROOT, "modifier")
    test_model = os.path.join(modifier_dir, "test_model.py")

    stdout, stderr, rc = _run_freecad(test_model, [model_path, "scan"])

    # Save raw log
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("=== SCAN LOG for " + model_name + " ===\n")
        f.write("Return code: " + str(rc) + "\n\n")
        f.write("--- stdout ---\n")
        f.write(stdout)
        f.write("\n--- stderr ---\n")
        f.write(stderr)

    if rc != 0:
        logger.error("  Scan failed (rc=%d): %s", rc, stderr[:200])
        return None

    # Extract JSON_RESULT from stdout
    for line in stdout.splitlines():
        if "JSON_RESULT:" in line:
            idx = line.index("JSON_RESULT:") + len("JSON_RESULT:")
            json_str = line[idx:].strip()
            result = json.loads(json_str)
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
            return result

    logger.error("  No JSON_RESULT found in scan output")
    return None


# ---------------------------------------------------------------------------
# Step 2: Modify a feature by scale
# ---------------------------------------------------------------------------

def modify_feature(model_path, model_name, feature_info, scale, feature_dir):
    """
    Run test_model.py in test mode for a single feature + scale combination.

    Returns a dict with experiment metadata + success status.
    """
    feat_idx = feature_info["idx"]
    feat_name = feature_info["name"]
    feat_type = feature_info["type"]
    orig_len = feature_info["original_length"]
    new_len = orig_len * scale

    scale_dir = os.path.join(feature_dir, "scale_{:.4f}".format(scale))
    os.makedirs(scale_dir, exist_ok=True)

    orig_brep = os.path.join(scale_dir, "original.brep")
    mod_brep = os.path.join(scale_dir, "modified.brep")

    modifier_dir = os.path.join(PROJECT_ROOT, "modifier")
    test_model = os.path.join(modifier_dir, "test_model.py")

    stdout, stderr, rc = _run_freecad(
        test_model,
        [model_path, "test", str(feat_idx), "{:.4f}".format(scale),
         orig_brep, mod_brep],
    )

    success = rc == 0 and os.path.exists(mod_brep)

    # Write experiment log
    exp_log = os.path.join(scale_dir, "experiment.log")
    with open(exp_log, "w", encoding="utf-8") as f:
        f.write("=== Experiment Log ===\n")
        f.write("Model:        {}\n".format(model_name))
        f.write("Feature idx:  {}\n".format(feat_idx))
        f.write("Feature name: {}\n".format(feat_name))
        f.write("Feature type: {}\n".format(feat_type))
        f.write("Original len: {:.4f} mm\n".format(orig_len))
        f.write("Scale factor: {:.4f}\n".format(scale))
        f.write("New length:   {:.4f} mm\n".format(new_len))
        f.write("Return code:  {}\n".format(rc))
        f.write("Success:      {}\n".format(success))
        f.write("\n--- FreeCAD stdout ---\n")
        f.write(stdout)
        f.write("\n--- FreeCAD stderr ---\n")
        f.write(stderr)

    return {
        "model_name": model_name,
        "feature_idx": feat_idx,
        "feature_name": feat_name,
        "feature_type": feat_type,
        "original_length": orig_len,
        "scale_factor": scale,
        "new_length": new_len,
        "return_code": rc,
        "success": success,
        "has_orig_brep": os.path.exists(orig_brep),
        "has_mod_brep": os.path.exists(mod_brep),
        "error": ("" if success else stderr[:500].replace("\n", " ")),
    }


# ---------------------------------------------------------------------------
# Main experiment runner
# ---------------------------------------------------------------------------

def run_experiments(dataset_dir, output_dir, seed, num_scales, scale_min, scale_max, verbose=False):
    """
    Run the full experiment suite:
      For each model → scan → for each feature → N random scale modifications.
    Write a summary CSV at the end.
    """
    dataset_dir = os.path.abspath(dataset_dir)
    output_dir = os.path.abspath(output_dir)

    # Setup logging
    logger = setup_logging(output_dir, verbose=verbose)

    # Set random seed for reproducibility
    random.seed(seed)
    logger.info("Random seed: %d", seed)

    # Check prerequisites
    if not os.path.isdir(dataset_dir):
        logger.error("Dataset directory not found: %s", dataset_dir)
        sys.exit(1)

    if not os.path.isfile(FREECAD_CMD_PATH):
        logger.error("FreeCADCmd not found: %s", FREECAD_CMD_PATH)
        logger.warning("Set FREECAD_CMD env var or edit exp_tools/config.py")
        sys.exit(1)

    # Collect model files
    model_files = sorted([
        f for f in os.listdir(dataset_dir)
        if f.endswith("_free.py")
    ])

    if not model_files:
        logger.error("No *_free.py files found in %s", dataset_dir)
        sys.exit(1)

    logger.info("=" * 60)
    logger.info("EXP_TOOLS — Experiment Runner")
    logger.info("=" * 60)
    logger.info("Dataset:  %s", dataset_dir)
    logger.info("Output:   %s", output_dir)
    logger.info("Models:   %d", len(model_files))
    logger.info("Scales:   %d per feature in [%.2f, %.2f]", num_scales, scale_min, scale_max)
    logger.info("FreeCAD:  %s", FREECAD_CMD_PATH)
    logger.info("=" * 60)

    os.makedirs(output_dir, exist_ok=True)

    # Summary rows
    summary_rows = []
    skipped_models = []
    total_ok = 0
    total_fail = 0
    total_models = len(model_files)

    logger.info("Processing %d models...", total_models)

    for model_idx, model_file in enumerate(model_files):
        model_name = model_file.replace("_free.py", "")
        model_path = os.path.join(dataset_dir, model_file)
        t0 = time.time()

        # Progress prefix: [ID X/Total]
        prefix = f"[{model_name} {model_idx + 1}/{total_models}]"

        # Copy .py script to output dir
        model_dir = os.path.join(output_dir, model_name)
        os.makedirs(model_dir, exist_ok=True)
        shutil.copy2(model_path, os.path.join(model_dir, model_file))

        # --- Scan ---
        scan_result = scan_model(model_path, model_name, model_dir)
        if scan_result is None or scan_result.get("status") != "success":
            skipped_models.append((model_name, "scan_failed"))
            summary_rows.append({
                "model_name": model_name,
                "feature_idx": -1,
                "feature_name": "",
                "feature_type": "",
                "original_length": 0,
                "scale_factor": 0,
                "new_length": 0,
                "return_code": -1,
                "success": False,
                "has_orig_brep": False,
                "has_mod_brep": False,
                "error": "scan_failed",
            })
            elapsed = round(time.time() - t0, 1)
            logger.error("%s scan FAILED — %.1fs", prefix, elapsed)
            continue

        features = scan_result.get("features", [])
        num_features = len(features)
        scan_elapsed = round(time.time() - t0, 1)

        if num_features == 0:
            skipped_models.append((model_name, "no_features"))
            logger.warning("%s scan ... 0 features found — %.1fs", prefix, scan_elapsed)
            continue

        logger.info("%s scan ... %d features found — %.1fs", prefix, num_features, scan_elapsed)

        # --- Modify each feature ---
        model_ok = 0
        model_fail = 0

        for feat_local_idx, feat in enumerate(features):
            feat_idx = feat["idx"]
            feat_dir = os.path.join(model_dir, f"feature_{feat_idx}")
            os.makedirs(feat_dir, exist_ok=True)

            t_feat = time.time()
            f_ok = 0
            f_fail = 0

            # Generate random scales for this feature
            scales = [random.uniform(scale_min, scale_max) for _ in range(num_scales)]

            for scale in scales:
                result = modify_feature(model_path, model_name, feat, scale, feat_dir)
                summary_rows.append(result)
                if result["success"]:
                    f_ok += 1
                else:
                    f_fail += 1

            f_elapsed = round(time.time() - t_feat, 1)
            model_ok += f_ok
            model_fail += f_fail

            # Per-feature log line
            feat_label = f"feat {feat_local_idx + 1}/{num_features}"
            ok_fail = f"{f_ok} OK, {f_fail} FAIL"
            logger.info("%s modify %s ... %s — %.1fs",
                        prefix, feat_label, ok_fail, f_elapsed)

        # Per-model summary
        total_model = model_ok + model_fail
        m_elapsed = round(time.time() - t0, 1)
        ok_fail_summary = f"{model_ok} OK, {model_fail} FAIL"
        if model_fail == 0:
            logger.info("%s done — %d features, %d experiments (%s) — %.1fs",
                        prefix, num_features, total_model, ok_fail_summary, m_elapsed)
        else:
            logger.warning("%s done — %d features, %d experiments (%s) — %.1fs",
                           prefix, num_features, total_model, ok_fail_summary, m_elapsed)

        total_ok += model_ok
        total_fail += model_fail

    # Report skipped models
    for name, reason in skipped_models:
        logger.warning("Skipped %s — %s", name, reason)

    logger.info("All experiments completed.")

    # ------------------------------------------------------------------
    # Write summary CSV
    # ------------------------------------------------------------------
    logger.info("=" * 60)
    logger.info("Writing summary CSV...")
    logger.info("=" * 60)

    summary_csv = os.path.join(output_dir, "summary.csv")
    headers = [
        "model_name", "feature_idx", "feature_name", "feature_type",
        "original_length", "scale_factor", "new_length",
        "return_code", "success", "has_orig_brep", "has_mod_brep",
        "error",
    ]

    with open(summary_csv, "w", encoding="utf-8") as f:
        f.write(",".join(headers) + "\n")
        for row in summary_rows:
            values = []
            for h in headers:
                v = str(row.get(h, "")).replace('"', '""')
                if "," in v or "\n" in v:
                    v = f'"{v}"'
                values.append(v)
            f.write(",".join(values) + "\n")

    # Print summary stats
    total = len(summary_rows)
    ok = total_ok
    fail = total_fail
    models_with_errors = set(
        r["model_name"] for r in summary_rows
        if not r["success"] and r["feature_idx"] == -1
    )
    exp_failures = set(
        r["model_name"] for r in summary_rows
        if not r["success"] and r["feature_idx"] >= 0
    )

    logger.info("Summary:")
    logger.info("  Total experiments: %d", total)
    logger.info("  Successful:        %d (%.1f%%)", ok, 100 * ok / max(total, 1))
    logger.info("  Failed:            %d (%.1f%%)", fail, 100 * fail / max(total, 1))
    logger.info("  Models w/ scan fail:    %d", len(models_with_errors))
    logger.info("  Models w/ mod fail:     %d", len(exp_failures))
    if models_with_errors:
        for m in sorted(models_with_errors):
            logger.warning("    Scan failed: %s", m)
    if exp_failures:
        logger.warning("    Modification failures in: %s", ", ".join(sorted(exp_failures)[:20]))

    logger.info("Summary CSV: %s", summary_csv)
    logger.info("Experiment output: %s", output_dir)
    logger.info("Pipeline finished.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="exp_tools — Run parameter modification experiments on CAD models"
    )
    parser.add_argument(
        "--dataset-dir",
        default=DATASET_DIR,
        help=f"Dataset directory with *_free.py files (default: {DATASET_DIR})",
    )
    parser.add_argument(
        "--output-dir",
        default=OUTPUT_DIR,
        help=f"Output directory for experiment results (default: {OUTPUT_DIR})",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=RANDOM_SEED,
        help=f"Random seed for reproducibility (default: {RANDOM_SEED})",
    )
    parser.add_argument(
        "--scales",
        type=int,
        default=NUM_SCALES,
        help=f"Number of random scales per feature (default: {NUM_SCALES})",
    )
    parser.add_argument(
        "--scale-min",
        type=float,
        default=SCALE_MIN,
        help=f"Minimum scale factor (default: {SCALE_MIN})",
    )
    parser.add_argument(
        "--scale-max",
        type=float,
        default=SCALE_MAX,
        help=f"Maximum scale factor (default: {SCALE_MAX})",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose (DEBUG) logging",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    run_experiments(
        dataset_dir=args.dataset_dir,
        output_dir=args.output_dir,
        seed=args.seed,
        num_scales=args.scales,
        scale_min=args.scale_min,
        scale_max=args.scale_max,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    main()
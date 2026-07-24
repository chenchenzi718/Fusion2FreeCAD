"""
DeepCAD2Free -- Main entry point for the conversion pipeline.

Usage:
    # Full pipeline (clean + convert + validate + bbox)
    python main.py

    # Only clean (repair DeepCAD JSON)
    python main.py --clean-only

    # Only convert (requires cleaned data in data/cad_json_repair/)
    python main.py --convert-only

    # Custom paths
    python main.py --input data/my_json/ --output data/my_output/
"""

import argparse
import gc
import logging
import multiprocessing as mp
import os
import shutil
import sys
import tempfile
import time

from tqdm import tqdm


# ---------------------------------------------------------------------------
# Path setup – ensure project root is on sys.path
# ---------------------------------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from deepcad2free.converter import deepcad2free
from deepcad2free.cleaner import repair_deepcad
from deepcad2free.utils.free_check import run_freecad_modeling
from deepcad2free.utils.get_free_bbox import get_combined_bbox, setup_to_deepcad
from deepcad2free.utils.load_deepcad import get_deepcad_sequence, load_deepcad
from deepcad2free.utils.logging_db import LogDatabase
from deepcad2free.utils.config import (
    FREECAD_CMD_PATH,
    INPUT_DIR,
    REPAIR_DIR,
    OUTPUT_PY_DIR,
    OUTPUT_FREE_DIR,
    LOG_DIR,
    DB_PATH,
    DEFAULT_PROCESSES,
    DEFAULT_BATCH_SIZE,
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

    log_file = os.path.join(log_path, "process.log")
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


# ---------------------------------------------------------------------------
# Step 1 -- Data cleaning
# ---------------------------------------------------------------------------

def clean_all(deepcad_input_path: str, deepcad_repair_path: str) -> int:
    """
    Walk *deepcad_input_path*, repair every JSON, and write to *deepcad_repair_path*.
    Returns the number of files processed.
    """
    deepcad_input_path = os.path.abspath(deepcad_input_path)
    deepcad_repair_path = os.path.abspath(deepcad_repair_path)

    if not os.path.isdir(deepcad_input_path):
        logger.error(f"Input directory not found: {deepcad_input_path}")
        return 0

    count = 0
    for root, _, files in os.walk(deepcad_input_path):
        rel = os.path.relpath(root, deepcad_input_path)
        target_dir = os.path.join(deepcad_repair_path, rel)
        os.makedirs(target_dir, exist_ok=True)

        for fname in tqdm(files, desc="Cleaning JSON"):
            if not fname.endswith(".json"):
                continue
            src = os.path.join(root, fname)
            dst = os.path.join(target_dir, fname)
            try:
                deepcad_json = load_deepcad(src)
                repaired = repair_deepcad(deepcad_json)
                with open(dst, "w", encoding="utf-8") as fout:
                    json.dump(repaired, fout, indent=4)
                count += 1
            except Exception as e:
                logger.error(f"Failed to clean {src}: {e}")

    logger.info(f"Cleaning done -- {count} file(s) repaired -> {deepcad_repair_path}")
    return count


# ---------------------------------------------------------------------------
# Step 2 -- Conversion helpers
# ---------------------------------------------------------------------------

def _log(msg: str):
    """Print to stderr from any process (worker or main) without corrupting tqdm."""
    print(msg, file=sys.stderr, flush=True)


def _log_ok(key: str, step: str):
    """Print a success line in green."""
    print(f"\033[32m[{key}] {step} OK\033[0m", file=sys.stderr, flush=True)


def _log_err(key: str, step: str, error: str):
    """Print an error line in red."""
    print(f"\033[31m[{key}] {step} error_code: {error}\033[0m",
          file=sys.stderr, flush=True)


def handle_conversion(key, val, op_seq, output_py_path):
    """Convert a single model, return update data for the database."""
    try:
        ret_str, Free_str, error_code = deepcad2free(key, val)
        if op_seq and op_seq[-1] == "S":
            error_code = "UNUSED SKETCH"

        if error_code:
            _log_err(key, "convert", error_code)

        update_data = {
            "is_convert": 1,
            "fusion_sequence": op_seq,
            "free_sequence": Free_str,
            "is_valid": 0,
            "error_code": error_code,
        }

        sub_dir = os.path.join(output_py_path, key[:4])
        os.makedirs(sub_dir, exist_ok=True)

        with tempfile.NamedTemporaryFile(mode="w", delete=False,
                                         encoding="utf-8") as temp_file:
            temp_file.write(ret_str)
            temp_path = temp_file.name

        target_path = os.path.join(sub_dir, f"{key}_free.py")
        shutil.move(temp_path, target_path)

        success = True
    except Exception as e:
        error_code = str(e)
        _log_err(key, "convert", error_code)
        update_data = {"is_convert": 0, "error_code": error_code}
        success = False

    gc.collect()
    return key, update_data, success


def handle_validation(key, output_py_path, log_path, output_free_path):
    """Validate a converted model via FreeCADCmd."""
    try:
        run_freecad_modeling(key, output_py_path, log_path, output_free_path)
        _log_ok(key, "validation")
        update_data = {"is_valid": 1}
        success = True
    except Exception as e:
        error_code = str(e)
        _log_err(key, "valid", error_code)
        update_data = {"is_valid": 0, "error_code": error_code}
        success = False

    gc.collect()
    return key, update_data, success


def handle_bbox(key, log_path, output_free_path, deepcad_path):
    """Compute and update the bounding box."""
    try:
        free_path = os.path.join(
            output_free_path, key[:4], f"{key}_free.FCStd"
        )
        bbox_tuple = get_combined_bbox(free_path)
        setup_to_deepcad(bbox_tuple, deepcad_path)
        _log_ok(key, "bbox")
        update_data = {"is_valid": 1}
        success = True
    except Exception as e:
        error_code = str(e)
        _log_err(key, "bbox", error_code)
        update_data = {"is_valid": 0, "error_code": error_code}
        success = False

    gc.collect()
    return key, update_data, success


def process_single_file(path_data):
    """Process a single JSON file (used as multiprocessing worker)."""
    path, output_py_path, output_free_path, log_path = path_data

    key = path[-13:-5]
    result_data = {"key": key, "updates": []}

    try:
        val = load_deepcad(path)
    except Exception as e:
        error_msg = f"Error loading {path}: {e}"
        _log_err(key, "load", error_msg)
        result_data["updates"].append(
            {
                "key": key,
                "data": {
                    "is_convert": 0,
                    "fusion_sequence": "",
                    "free_sequence": "",
                    "is_valid": 0,
                    "error_code": error_msg,
                },
            }
        )
        return result_data

    init_data = {
        "is_convert": 0,
        "fusion_sequence": "",
        "free_sequence": "",
        "is_valid": 0,
        "error_code": "",
    }
    result_data["updates"].append({"key": key, "data": init_data})

    op_seq = get_deepcad_sequence(val)
    result_data["updates"].append({"key": key, "data": {"fusion_sequence": op_seq}})

    _log(f"[{key}] processing ...")

    key, update_data, success = handle_conversion(
        key, val, op_seq, output_py_path
    )
    result_data["updates"].append({"key": key, "data": update_data})

    if success:
        key, valid_data, valid_success = handle_validation(
            key, output_py_path, log_path, output_free_path
        )
        result_data["updates"].append({"key": key, "data": valid_data})

        if valid_success:
            key, bbox_data, _ = handle_bbox(
                key, log_path, output_free_path, path
            )
            result_data["updates"].append({"key": key, "data": bbox_data})

    del val
    gc.collect()
    return result_data


# ---------------------------------------------------------------------------
# Step 2 -- Batch conversion pipeline
# ---------------------------------------------------------------------------

def convert_all(
    deepcad_repair_path: str,
    output_py_path: str,
    output_free_path: str,
    log_path: str,
    num_processes: int = None,
    batch_size: int = 50,
):
    """
    Convert all JSON files under *deepcad_repair_path*.

    For each model:
      1. Load DeepCAD JSON
      2. Convert to FreeCAD Python script
      3. Validate via FreeCADCmd
      4. Update bounding box
      5. Track status in SQLite database
    """
    deepcad_repair_path = os.path.abspath(deepcad_repair_path)
    output_py_path = os.path.abspath(output_py_path)
    output_free_path = os.path.abspath(output_free_path)
    log_path = os.path.abspath(log_path)
    db_path = os.path.join(log_path, "log.db")

    # Create directories
    for d in [output_py_path, output_free_path, log_path]:
        os.makedirs(d, exist_ok=True)

    # Collect JSON files
    json_path_list = []
    for root, _, files in os.walk(deepcad_repair_path):
        json_path_list.extend(
            [os.path.join(root, f) for f in files if f.endswith(".json")]
        )

    if not json_path_list:
        logger.warning(f"No JSON files found under {deepcad_repair_path}")
        return

    logger.info(f"Found {len(json_path_list)} JSON file(s) to convert")

    # Auto-detect process count
    if num_processes is None:
        num_processes = min(mp.cpu_count() - 1, DEFAULT_PROCESSES)
    num_processes = max(1, num_processes)
    logger.info(f"Using {num_processes} worker process(es)")

    db = LogDatabase(db_path)
    db.begin_transaction()

    try:
        tasks = [
            (path, output_py_path, output_free_path, log_path)
            for path in json_path_list
        ]

        results_buffer = []

        with mp.Pool(processes=num_processes) as pool:
            for i, result in enumerate(
                tqdm(
                    pool.imap(process_single_file, tasks, chunksize=5),
                    total=len(tasks),
                    desc="Converting",
                )
            ):
                if result and "updates" in result:
                    results_buffer.extend(result["updates"])

                if len(results_buffer) >= batch_size:
                    for update in results_buffer:
                        if "key" in update and "data" in update:
                            db.set_data_id(update["key"], **update["data"])

                    if i % 50 == 0:
                        db.commit()

                    if i % 100 == 0:
                        db.dump_to_csv(os.path.join(log_path, "log.csv"))

                    results_buffer = []
                    time.sleep(0.05)
                    gc.collect()

        # Flush remaining
        if results_buffer:
            for update in results_buffer:
                if "key" in update and "data" in update:
                    db.set_data_id(update["key"], **update["data"])

    finally:
        db.commit()
        db.dump_to_csv(os.path.join(log_path, "log.csv"))
        db.close()

    logger.info(
        f"Conversion done -> py:{output_py_path}  "
        f"fcstd:{output_free_path}  log:{log_path}"
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

import json

logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(
        description="DeepCAD2Free -- Convert DeepCAD JSON to FreeCAD Python scripts"
    )

    parser.add_argument(
        "--clean-only",
        action="store_true",
        help="Only run data cleaning, skip conversion",
    )
    parser.add_argument(
        "--convert-only",
        action="store_true",
        help="Only run conversion (requires data in cad_json_repair/)",
    )

    parser.add_argument(
        "--input",
        default=INPUT_DIR,
        help=f"Input directory with DeepCAD JSON files (default: {INPUT_DIR})",
    )
    parser.add_argument(
        "--repair-dir",
        default=REPAIR_DIR,
        help=f"Directory for repaired JSON (default: {REPAIR_DIR})",
    )
    parser.add_argument(
        "--output-py",
        default=OUTPUT_PY_DIR,
        help=f"Output directory for FreeCAD Python scripts (default: {OUTPUT_PY_DIR})",
    )
    parser.add_argument(
        "--output-free",
        default=OUTPUT_FREE_DIR,
        help=f"Output directory for .FCStd files (default: {OUTPUT_FREE_DIR})",
    )
    parser.add_argument(
        "--log-dir",
        default=LOG_DIR,
        help=f"Log directory (default: {LOG_DIR})",
    )
    parser.add_argument(
        "--processes",
        type=int,
        default=None,
        help=f"Number of worker processes (default: min(cpu-1, {DEFAULT_PROCESSES}))",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help=f"DB flush batch size (default: {DEFAULT_BATCH_SIZE})",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose (DEBUG) logging",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    # Default: run full pipeline (clean + convert)
    if not args.clean_only and not args.convert_only:
        mode = "full"
    elif args.clean_only:
        mode = "clean"
    else:
        mode = "convert"

    # Setup logging
    logger = setup_logging(args.log_dir, verbose=args.verbose)

    # Check FreeCAD path
    if mode != "clean":
        if FREECAD_CMD_PATH and "path\\to\\FreeCAD" in FREECAD_CMD_PATH:
            logger.warning(
                "FREECAD_CMD path still points to placeholder. "
                "Set the FREECAD_CMD environment variable to your FreeCADCmd.exe location."
            )

    # Step 1 -- Clean
    if mode in ("full", "clean"):
        logger.info("=" * 60)
        logger.info("STEP 1: Data Cleaning")
        logger.info(f"  Input:  {args.input}")
        logger.info(f"  Output: {args.repair_dir}")
        logger.info("=" * 60)

        cleaned = clean_all(args.input, args.repair_dir)

        if cleaned == 0:
            logger.error("Cleaning produced 0 files. Aborting.")
            sys.exit(1)

    # Step 2 -- Convert
    if mode in ("full", "convert"):
        logger.info("=" * 60)
        logger.info("STEP 2: Batch Conversion")
        logger.info(f"  Input:     {args.repair_dir}")
        logger.info(f"  Output .py:  {args.output_py}")
        logger.info(f"  Output .FCStd: {args.output_free}")
        logger.info(f"  Log:       {args.log_dir}")
        logger.info("=" * 60)

        convert_all(
            deepcad_repair_path=args.repair_dir,
            output_py_path=args.output_py,
            output_free_path=args.output_free,
            log_path=args.log_dir,
            num_processes=args.processes,
            batch_size=args.batch_size,
        )

    logger.info("Pipeline finished successfully.")


if __name__ == "__main__":
    # Windows: set high priority
    if os.name == "nt":
        try:
            import psutil
            p = psutil.Process(os.getpid())
            p.nice(psutil.HIGH_PRIORITY_CLASS)
        except (ImportError, PermissionError):
            pass

    main()
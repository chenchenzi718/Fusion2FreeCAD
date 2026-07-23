"""
Batch processor -- orchestrates the conversion pipeline for thousands of models.

Usage:
    python -m fusion2free.batch_processor

Steps for each model:
  1. Load Fusion 360 JSON
  2. Convert to FreeCAD Python script (via converter.fusion2free)
  3. Validate via FreeCADCmd (via free_check.run_freecad_modeling)
  4. Update bounding box (via get_free_bbox)
  5. Track status in SQLite database
"""

import time
import gc
import logging
import multiprocessing as mp
import tempfile
import shutil
import os

from tqdm import tqdm

from fusion2free.converter import fusion2free
from fusion2free.utils.free_check import run_freecad_modeling
from fusion2free.utils.get_free_bbox import get_combined_bbox, setup_to_fusion
from fusion2free.utils.load_fusion import get_fusion_sequence, load_fusion
from fusion2free.utils.logging_db import LogDatabase

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("process.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def setup_directories(paths):
    """Create directories if they do not exist."""
    for path in paths:
        os.makedirs(path, exist_ok=True)


def handle_conversion(key, val, op_seq, output_py_path, log_path):
    """Convert a single model, return update data for the database."""
    try:
        ret_str, Free_str, error_code = fusion2free(key, val)
        if op_seq[-1] == "S":
            error_code = "UNUSED SKETCH"
        if error_code:
            logger.info(f"data_id:{key}, convert error_code:{error_code}")

        update_data = {
            "is_convert": 1,
            "fusion_sequence": op_seq,
            "free_sequence": Free_str,
            "is_valid": 0,
            "error_code": error_code,
        }

        sub_dir = os.path.join(output_py_path, key[:4])
        os.makedirs(sub_dir, exist_ok=True)

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
            temp_file.write(ret_str)
            temp_path = temp_file.name

        target_path = os.path.join(sub_dir, f"{key}_free.py")
        shutil.move(temp_path, target_path)

        success = True
    except Exception as e:
        error_code = str(e)
        logger.error(f"data_id:{key}, convert error_code:{error_code}")
        update_data = {"is_convert": 0, "error_code": error_code}
        success = False

    gc.collect()
    return key, update_data, success


def handle_validation(key, output_py_path, log_path, output_free_path):
    """Validate a converted model via FreeCADCmd."""
    try:
        run_freecad_modeling(key, output_py_path, log_path, output_free_path)
        update_data = {"is_valid": 1}
        success = True
    except Exception as e:
        error_code = str(e)
        logger.error(f"data_id:{key}, valid error_code:{error_code}")
        update_data = {"is_valid": 0, "error_code": error_code}
        success = False

    gc.collect()
    return key, update_data, success


def handle_bbox(key, log_path, output_free_path, fusion_path):
    """Compute and update the bounding box."""
    try:
        free_path = os.path.join(
            output_free_path, key[:4], f"{key}_free.FCStd"
        )
        bbox_tuple = get_combined_bbox(free_path)
        setup_to_fusion(bbox_tuple, fusion_path)
        update_data = {"is_valid": 1}
        success = True
    except Exception as e:
        error_code = str(e)
        logger.error(f"data_id:{key}, valid error_code:{error_code}")
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
        val = load_fusion(path)
    except Exception as e:
        error_msg = f"Error loading {path}: {e}"
        logger.error(error_msg)
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

    ki = int(key)
    if ki < 1063718:
        return result_data

    init_data = {
        "is_convert": 0,
        "fusion_sequence": "",
        "free_sequence": "",
        "is_valid": 0,
        "error_code": "",
    }
    result_data["updates"].append({"key": key, "data": init_data})

    op_seq = get_fusion_sequence(val)
    result_data["updates"].append({"key": key, "data": {"fusion_sequence": op_seq}})

    logger.info(f"Now process: {key}")

    key, update_data, success = handle_conversion(
        key, val, op_seq, output_py_path, log_path
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


def process_json_files():
    """Main batch processing pipeline."""
    output_py_path = "./data/cad_py_repair/"
    output_free_path = "./data/cad_free_repair/"
    log_path = "./logging/"
    db_path = os.path.join(log_path, "log.db")
    fusion_prefix_path = "./data/cad_json_repair/"

    setup_directories([output_py_path, output_free_path, log_path])

    json_path_list = []
    for root, _, files in os.walk(fusion_prefix_path):
        json_path_list.extend(
            [os.path.join(root, file) for file in files if file.endswith(".json")]
        )

    db = LogDatabase(db_path)
    db.begin_transaction()

    try:
        tasks = [
            (path, output_py_path, output_free_path, log_path)
            for path in json_path_list
        ]

        batch_size = 50
        results_buffer = []

        num_processes = min(mp.cpu_count() - 1, 4)

        with mp.Pool(processes=num_processes) as pool:
            for i, result in enumerate(
                tqdm(
                    pool.imap(process_single_file, tasks, chunksize=5),
                    total=len(tasks),
                    desc="Processing files",
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

        if results_buffer:
            for update in results_buffer:
                if "key" in update and "data" in update:
                    db.set_data_id(update["key"], **update["data"])

    finally:
        db.commit()
        db.dump_to_csv(os.path.join(log_path, "log.csv"))
        db.close()


def run_with_memory_tracking():
    """Run the pipeline with memory monitoring (requires psutil)."""
    try:
        import psutil

        process = psutil.Process(os.getpid())

        def log_memory():
            memory_info = process.memory_info()
            memory_mb = memory_info.rss / 1024 / 1024
            logger.info(f"Memory usage: {memory_mb:.2f} MB")

        import threading

        def memory_logger():
            while True:
                log_memory()
                time.sleep(600)

        monitor_thread = threading.Thread(target=memory_logger, daemon=True)
        monitor_thread.start()
    except ImportError:
        logger.warning("psutil not installed -- memory monitoring disabled")

    process_json_files()


if __name__ == "__main__":
    if os.name == "nt":
        try:
            import psutil

            p = psutil.Process(os.getpid())
            p.nice(psutil.HIGH_PRIORITY_CLASS)
        except (ImportError, PermissionError):
            logger.warning("Cannot set process priority")

    run_with_memory_tracking()
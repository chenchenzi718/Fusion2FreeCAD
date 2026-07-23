"""
Gradient generator -- helper utilities for parameter modification experiments.

Provides functions to:
  - Process scan results from test_model.py SCAN_ALL mode
  - Generate random scale values for gradient tests
  - Write CSV reports
  - Copy valid results to output directories
"""

import sys
import os
import re
import json
import random
import shutil


def process_scan(scan_log, model_dir):
    """
    Process a scan log file and extract feature information.

    Writes scan_ok.txt and num_features.txt to model_dir.
    """
    with open(scan_log, "r", encoding="utf-8", errors="ignore") as f:
        log = f.read()

    match = re.search(r"JSON_RESULT:\s*(\{.*\})", log)
    if not match:
        with open(os.path.join(model_dir, "scan_ok.txt"), "w") as f:
            f.write("0")
        with open(os.path.join(model_dir, "num_features.txt"), "w") as f:
            f.write("0")
        return

    data = json.loads(match.group(1))
    features_file = os.path.join(model_dir, "features.json")
    with open(features_file, "w", encoding="utf-8") as f:
        json.dump(data, f)

    scan_ok = (
        1 if data.get("status") == "success" and data.get("testable_features") else 0
    )
    num_features = (
        len(data.get("testable_features", [])) if scan_ok else 0
    )

    with open(os.path.join(model_dir, "scan_ok.txt"), "w") as f:
        f.write(str(scan_ok))
    with open(os.path.join(model_dir, "num_features.txt"), "w") as f:
        f.write(str(num_features))


def get_feature(features_file, index):
    """Extract feature info for a given index from features.json."""
    with open(features_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    feat = data["testable_features"][int(index)]
    orig_len = float(feat["original_length"])
    info = f"{feat['idx']}|{feat['name']}|{feat['type']}|{orig_len:.4f}"
    model_dir = os.path.dirname(features_file)
    with open(os.path.join(model_dir, "feat_info.txt"), "w", encoding="utf-8") as f:
        f.write(info)


def generate_scales(output_file, min_val, max_val, count):
    """Generate 'count' random scale values in [min_val, max_val] and write to file."""
    scales = [
        random.uniform(float(min_val), float(max_val)) for _ in range(int(count))
    ]
    with open(output_file, "w") as f:
        for s in scales:
            f.write(f"{s:.4f}\n")


def escape_csv(s):
    """Escape a value for CSV output."""
    s = str(s)
    if "," in s or '"' in s or "\n" in s:
        return f'"{s.replace("\"", "\"\"")}"'
    return s


def write_report(
    report_file,
    model_name,
    feat_idx,
    feat_name,
    feat_type,
    group,
    scale_idx,
    scale_val,
    status,
    orig_len,
    new_len,
    err_msg,
):
    """Append a row to the CSV summary report."""
    line = (
        f"{escape_csv(model_name)},{feat_idx},{escape_csv(feat_name)},"
        f"{escape_csv(feat_type)},{group},{scale_idx},{scale_val},"
        f"{status},{orig_len},{new_len},{escape_csv(err_msg)}\n"
    )
    with open(report_file, "a", encoding="utf-8") as f:
        f.write(line)


def copy_valid(src_dir, dst_dir, src_model, dst_model_dir):
    """Copy valid test results to a validated output directory."""
    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
    dst_model = os.path.join(dst_model_dir, os.path.basename(src_model))
    if not os.path.exists(dst_model):
        shutil.copy2(src_model, dst_model)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "process_scan":
        process_scan(sys.argv[2], sys.argv[3])
    elif cmd == "get_feature":
        get_feature(sys.argv[2], sys.argv[3])
    elif cmd == "generate_scales":
        generate_scales(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif cmd == "write_report":
        write_report(*sys.argv[2:14])
    elif cmd == "copy_valid":
        copy_valid(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
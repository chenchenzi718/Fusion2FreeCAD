"""
FreeCAD model validation -- execute generated Python scripts via FreeCADCmd.

Uses subprocess to invoke FreeCADCmd (command-line FreeCAD) so that the
conversion pipeline does not require a FreeCAD Python import at import time.
"""

import os
import subprocess
import tempfile

from fusion2free.utils.config import FREECAD_CMD_PATH


def run_freecad_modeling(data_id, py_dir, logging_dir, output_free_path):
    """
    Execute a FreeCAD Python script and save the result as .FCStd.

    Args:
        data_id: identifier for the model
        py_dir: directory containing the generated *_free.py script
        logging_dir: directory for log files
        output_free_path: directory for .FCStd output
    """
    # --- Validation check disabled by default ---
    return

    output_dir = os.path.join(output_free_path, data_id[:4])
    os.makedirs(output_dir, exist_ok=True)

    save_path = os.path.join(output_dir, f"{data_id}_free.FCStd")

    py_dir = os.path.abspath(py_dir)
    py_subdir = os.path.join(py_dir, data_id[:4])
    os.makedirs(py_subdir, exist_ok=True)

    py_file_path = os.path.join(py_subdir, f"{data_id}_free.py")
    if not os.path.exists(py_file_path):
        raise FileNotFoundError(f"Python file not found: {py_file_path}")

    temp_script_content = f"""
import FreeCAD as App
import Part
import os

py_file_path = r"{py_file_path}"
print(f"Reading Python file: {{py_file_path}}")
with open(py_file_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            exec(line)

doc = App.ActiveDocument
if doc:
    doc.recompute()
    doc.saveAs(r"{save_path}")
    App.closeDocument(doc.Name)
"""

    print(f"Python file exists: {py_file_path}")

    temp_script_path = os.path.join(tempfile.gettempdir(), f"{data_id}_temp.py")
    with open(temp_script_path, "w", encoding="utf-8") as f:
        f.write(temp_script_content)

    cmd = [FREECAD_CMD_PATH, temp_script_path]

    result = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    try:
        os.remove(temp_script_path)
    except OSError:
        pass

    if result.stderr:
        raise Exception(
            "Error occurred during FreeCAD modeling:\\n"
            + result.stderr.split("\\n")[0]
        )

    return f"{data_id}_free.FCStd"


if __name__ == "__main__":
    run_freecad_modeling(
        "00000062",
        "./data/cad_py_repair",
        "./logging",
        "./data/cad_free_repair",
    )
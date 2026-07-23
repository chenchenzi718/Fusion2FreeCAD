"""
FreeCAD model validation -- execute generated Python scripts via FreeCADCmd.

Uses subprocess to invoke FreeCADCmd (command-line FreeCAD) so that the
conversion pipeline does not require a FreeCAD Python import at import time.
"""

import os
import subprocess
import tempfile

from fusion2free.utils.config import FREECAD_CMD_PATH


def _clean_env():
    """
    Return a clean environment dict for FreeCADCmd subprocess.

    Removes Python-related variables (PYTHONHOME, PYTHONPATH, VIRTUAL_ENV,
    CONDA_* etc.) that confuse FreeCAD's embedded Python interpreter.
    Keeps PATH, TEMP, TMP, and SystemRoot for normal Windows operation.
    """
    keep = {
        "PATH", "TEMP", "TMP", "SYSTEMROOT", "SystemRoot",
        "windir", "WINDIR", "COMPUTERNAME", "USERNAME",
        "USERPROFILE", "HOMEDRIVE", "HOMEPATH",
        "NUMBER_OF_PROCESSORS", "OS", "PROCESSOR_ARCHITECTURE",
    }
    # Normalize: uppercase all existing keys for matching
    env = {}
    for key, value in os.environ.items():
        if key.upper() in keep:
            env[key] = value
    return env


def run_freecad_modeling(data_id, py_dir, logging_dir, output_free_path):
    """
    Execute a FreeCAD Python script and save the result as .FCStd.

    Args:
        data_id: identifier for the model
        py_dir: directory containing the generated *_free.py script
        logging_dir: directory for log files
        output_free_path: directory for .FCStd output
    """
    output_dir = os.path.join(output_free_path, data_id[:4])
    os.makedirs(output_dir, exist_ok=True)

    save_path = os.path.join(output_dir, f"{data_id}_free.FCStd")

    py_dir = os.path.abspath(py_dir)
    py_subdir = os.path.join(py_dir, data_id[:4])
    os.makedirs(py_subdir, exist_ok=True)

    py_file_path = os.path.join(py_subdir, f"{data_id}_free.py")
    if not os.path.exists(py_file_path):
        raise FileNotFoundError(f"Python file not found: {py_file_path}")

    # ------------------------------------------------------------------
    # Wrapper script — executed inside FreeCAD's own Python interpreter.
    # Exits with code 0 on success, non-zero on any exception.
    # ------------------------------------------------------------------
    temp_script_content = f'''
import sys

py_file_path = r"{py_file_path}"
save_path    = r"{save_path}"

try:
    import FreeCAD as App

    # Execute the generated script in an isolated namespace
    import types
    script_module = types.ModuleType("__freecad_script__")
    script_module.__file__ = py_file_path
    exec(open(py_file_path, "r", encoding="utf-8").read(),
         script_module.__dict__)

    # Save the resulting document
    doc = App.ActiveDocument
    if doc is None:
        sys.exit(1)
    doc.recompute()
    doc.saveAs(save_path)
    App.closeDocument(doc.Name)
    sys.exit(0)

except Exception:
    sys.exit(1)
'''

    temp_script_path = os.path.join(tempfile.gettempdir(), f"{data_id}_temp.py")
    with open(temp_script_path, "w", encoding="utf-8") as f:
        f.write(temp_script_content)

    cmd = [FREECAD_CMD_PATH, temp_script_path]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=_clean_env(),
    )

    # Clean up temp script
    try:
        os.remove(temp_script_path)
    except OSError:
        pass

    if result.returncode != 0:
        # Validation failed — remove the .py script
        try:
            os.remove(py_file_path)
        except OSError:
            pass
        raise Exception(
            f"FreeCADCmd exited with code {result.returncode}\\n"
            + result.stderr[:500]
        )

    return f"{data_id}_free.FCStd"


if __name__ == "__main__":
    from fusion2free.utils.config import OUTPUT_PY_DIR, LOG_DIR, OUTPUT_FREE_DIR

    run_freecad_modeling(
        "00000007",
        OUTPUT_PY_DIR,
        LOG_DIR,
        OUTPUT_FREE_DIR,
    )
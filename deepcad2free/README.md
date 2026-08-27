# deepcad2free — Conversion Engine

## Pipeline

```
DeepCAD JSON ──→ Clean ──→ Convert ──→ Validate ──→ BBox ──→ DeepCAD JSON (updated)
                  │           │           │            │
               repair      .py script   FreeCAD     bbox written
               entities   per model     Cmd exec    back to JSON
```

Each model goes through four sequential steps:

1. **Clean** — Remove unused sketches, empty sketches, and empty extrude profiles. Re-index the sequence field.
2. **Convert** — Parse DeepCAD JSON and generate a FreeCAD Python script that rebuilds the same parametric model.
3. **Validate** — Execute the generated script via `FreeCADCmd` (subprocess). If execution fails, the `.py` file is deleted and an error code is recorded.
4. **BBox** — Open the resulting `.FCStd` file, compute the combined bounding box of all `PartDesign::Body` objects, and write the values back to the source JSON (mm → m conversion).

Status for every model is tracked in a SQLite database (`log/log.db`) and exported to CSV.

## Supported Operations

| DeepCAD | FreeCAD |
|---|---|
| Sketch (Line3D, Arc3D, Circle3D) | Sketcher::SketchObject |
| Extrude → NewBody / Join | PartDesign::Pad |
| Extrude → Cut | PartDesign::Pocket |

## Module-Level API

### converter

```python
from deepcad2free.converter import deepcad2free

script, seq_str, error_code = deepcad2free(data_id, deepcad_json)
```

Returns the generated FreeCAD Python script string, an abbreviated operation sequence (e.g. `SNSCSCSC`), and an error code (empty string on success).

### cleaner

```python
from deepcad2free.cleaner import repair_deepcad

repaired = repair_deepcad(deepcad_json)
```

Returns a cleaned copy of the DeepCAD JSON with problematic entities removed.

### load_deepcad

```python
from deepcad2free.utils.load_deepcad import load_deepcad, get_deepcad_sequence

json_data = load_deepcad("path/to/model.json")
seq = get_deepcad_sequence(json_data)  # e.g. "SNSCSCSC"
```

## Architecture Notes

- **Subprocess isolation** — FreeCAD is invoked via `FreeCADCmd` subprocess, never imported directly. This avoids Python version conflicts (`.pyd` files are compiled against a specific Python version).
- **Multiprocessing** — `main.py` dispatches models to worker processes via `multiprocessing.Pool`. Each worker processes one model sequentially through all four pipeline steps.
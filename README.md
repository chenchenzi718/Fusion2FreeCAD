# Fusion2Free

**Fusion2Free** converts Fusion 360 (DeepCAD) parametric CAD models into FreeCAD Python scripts, and provides tools for modifying model parameters in experiments.

## Quick Start

```bash
pip install -r requirements.txt
```

Set the FreeCAD path before running any scripts that interact with FreeCAD:

```bash
# Windows
set FREECAD_CMD=C:\path\to\FreeCAD\bin\FreeCADCmd.exe
set FREECAD_LIB=C:\path\to\FreeCAD\lib

# Linux / macOS
export FREECAD_CMD=/usr/bin/freecadcmd
export FREECAD_LIB=/usr/lib/freecad/lib
```

## Project Structure

```
Fusion2Free/
├── fusion2free/                   # Part 1: Conversion Engine
│   ├── converter.py               # Fusion 360 JSON -> FreeCAD Python
│   ├── cleaner.py                 # Fusion 360 JSON repair
│   ├── batch_processor.py         # Batch conversion pipeline
│   ├── reverse_converter.py       # FreeCAD -> Fusion 360 JSON (experimental)
│   └── utils/
│       ├── config.py              # Paths & constants
│       ├── free_operation.py      # FreeCAD script generation
│       ├── free_check.py          # FreeCAD model validation
│       ├── load_fusion.py         # Fusion 360 JSON parser
│       ├── logging_db.py          # SQLite status tracker
│       ├── naming_utils.py        # Entity name encoder (SHA-256)
│       ├── cad_filter.py          # Model length filter
│       └── get_free_bbox.py       # Bounding-box computation
│
└── exp_tools/                     # Part 2: Experiment Tools
    ├── modifier/
    │   ├── feature_modifier.py    # Modify Pad/Pocket/Fillet/Chamfer in .FCStd
    │   ├── test_model.py          # Load .py scripts, scan/modify features
    │   └── gradient_gen.py        # Gradient scale generator & helpers
    └── dataset/                   # Curated FreeCAD Python scripts (~425 models)
        └── *_free.py
```

## Part 1 -- Conversion Engine

Converts Fusion 360 serialized models (DeepCAD format) to executable FreeCAD Python scripts.

### Supported Operations

| Fusion 360 | FreeCAD |
|---|---|
| Sketch (Line3D, Arc3D, Circle3D) | Sketcher::SketchObject |
| Extrude → NewBody / Join | PartDesign::Pad |
| Extrude → Cut | PartDesign::Pocket |

### Usage

```python
from fusion2free.utils.load_fusion import load_fusion
from fusion2free.converter import fusion2free

# Load Fusion 360 JSON
fusion_json = load_fusion("path/to/model.json")
data_id = "00000001"

# Convert to FreeCAD Python script
script, seq_str, error = fusion2free(data_id, fusion_json)

# Write to file
with open(f"{data_id}_free.py", "w") as f:
    f.write(script)
```

### Batch Processing

```bash
# Process all JSON files in data/cad_json_repair/
python -m fusion2free.batch_processor
```

### Data Cleaning

```python
from fusion2free.cleaner import repair_fusion

repaired = repair_fusion(fusion_json)
```

Removes unused sketches, empty sketches, and empty extrude profiles.

### Reverse Conversion (Experimental)

```bash
python -m fusion2free.reverse_converter model.FCStd -o model.json
```

## Part 2 -- Experiment Tools

Utilities for modifying parameters of already-converted FreeCAD models.

### Dataset

The `exp_tools/dataset/` directory contains **425 curated FreeCAD Python scripts** that have been validated for experimental use. Each script recreates a parametric CAD model when executed inside FreeCAD.

See [exp_tools/dataset/dataset_info.md](exp_tools/dataset/dataset_info.md) for details.

### Feature Modifier

Modify Pad/Pocket/Fillet/Chamfer features in `.FCStd` files:

```bash
FreeCADCmd.exe exp_tools/modifier/feature_modifier.py model.FCStd 0
```

### Test Model

Scan features or modify by scale factor:

```bash
# Scan all features
FreeCADCmd.exe exp_tools/modifier/test_model.py model.py 777777

# Modify feature 2 with 1.5x scale
FreeCADCmd.exe exp_tools/modifier/test_model.py model.py 888888 2 1.5
```

### Gradient Generator

```python
from exp_tools.modifier.gradient_gen import generate_scales

generate_scales("scales.txt", 0.1, 1.9, 5)
```

## FreeCAD Version Compatibility

This project supports two FreeCAD configurations:

| Mode | Description |
|---|---|
| **0** (default) | Custom build forked from [TODO: fill in branch] used in our experiments |
| **1** | Official FreeCAD 1.0 release |

Set the mode in `fusion2free/utils/config.py`:

```python
FREECAD_VERSION_MODE = 0  # or 1 for FreeCAD 1.0
```

> **Note:** The conversion engine (Part 1) generates pure FreeCAD Python scripts that do not depend on any specific FreeCAD version. The experiment tools (Part 2) require FreeCADCmd to execute model scripts.

## License

MIT License. See [LICENSE](LICENSE).

## Citation

If you use this project in your research, please cite:

```bibtex
@inproceedings{fusion2free,
  author  = {TODO},
  title   = {Validity-Assured Fast Regeneration of Parametric Solid Modeling},
  booktitle = {TODO},
  year    = {2026}
}
```

## References

- [DeepCAD Dataset](https://github.com/liruilong940607/DeepCAD)
- [FreeCAD](https://www.freecad.org/)
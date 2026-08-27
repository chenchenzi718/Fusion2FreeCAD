# DeepCAD2Free

**DeepCAD2Free** converts DeepCAD parametric CAD models into FreeCAD Python scripts, and provides tools for modifying model parameters in experiments.

This repository is the public code release of the SIGGRAPH Asia 2026 project *Validity-Assured Regeneration of Parametric Solid Modeling*; see the [project page](https://mechano-pesudo.github.io/Validity_Assured_Fast_Regeneration_of_Parametric_Solid_Modeling/) for details. Please note:

1. This repository is **not** the complete code used in the paper. During the experiments, we embedded our algorithm into the open-source CAD system FreeCAD and compiled a custom FreeCAD build. For various reasons, we cannot release this custom build, and the scripts used to collect and analyze the experimental data (the VAR and FBR timings, etc.) are therefore not included here. The main functionality of this repository is to convert the DeepCAD JSON scripts into Python scripts executable by FreeCAD, and its functionality is so far limited. We release it to provide a possible starting point for related community research.

2. The project uses 424 models in Python form, far fewer than the original DeepCAD dataset, because we filtered the models: not all of them are suitable for our study. The filtering criteria are described in detail on the project page and in the supplementary material. All 424 models are released together in [`exp_tools/dataset/`](exp_tools/dataset/).

## Prerequisites

- **FreeCAD 1.0.1** — our experiments use a custom build forked from the official 0.22.0 dev branch; of the official releases, 1.0.1 is the closest to it. Other branches or release versions may have API compatibility issues.

## Setup

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure FreeCAD path

Set `FREECAD_CMD` to point to the FreeCAD command-line executable:

```bash
# Windows
set FREECAD_CMD=C:\path\to\FreeCAD\bin\FreeCADCmd.exe

# Linux / macOS
export FREECAD_CMD=/usr/bin/freecadcmd
```

Or edit `deepcad2free/utils/config.py` directly:

```python
FREECAD_CMD_PATH = os.environ.get(
    "FREECAD_CMD",
    r"C:\your\path\to\FreeCAD\bin\FreeCADCmd.exe",
)
```

### 3. Download the DeepCAD dataset

Download `cad_json` from the [DeepCAD repository](https://github.com/liruilong940607/DeepCAD) and place it at `data/cad_json/` (the default input directory).

Or change the default in `deepcad2free/utils/config.py`:

```python
INPUT_DIR  = "path/to/your/cad_json"
REPAIR_DIR = "path/to/your/cad_json_repair"
```

## Usage

### Convert DeepCAD → FreeCAD

```bash
# Full pipeline: clean → convert → validate → bbox
python -m deepcad2free.main

# Only clean (repair DeepCAD JSON)
python -m deepcad2free.main --clean-only

# Only convert (requires cleaned data)
python -m deepcad2free.main --convert-only

# Custom paths & options
python -m deepcad2free.main \
    --input data/my_json \
    --repair-dir data/my_repair \
    --output-py data/my_py \
    --output-free data/my_fcstd \
    --processes 4 \
    --verbose
```

#### Supported Operations

| DeepCAD | FreeCAD |
|---|---|
| Sketch (Line3D, Arc3D, Circle3D) | Sketcher::SketchObject |
| Extrude → NewBody / Join | PartDesign::Pad |
| Extrude → Cut | PartDesign::Pocket |

### Experiment Tools

The `exp_tools/` directory contains utilities for running parameter modification experiments on converted FreeCAD models.

#### Run All Experiments

For each model in the dataset, scan features and modify each by random scale factors:

```bash
# Default: 5 random scales per feature in [0.1, 1.9], seed=42
python -m exp_tools.main

# Custom parameters
python -m exp_tools.main \
    --dataset-dir exp_tools/dataset \
    --output-dir exp_output \
    --scales 5 --scale-min 0.1 --scale-max 1.9 \
    --seed 42 --verbose
```

Results are written to `--output-dir` with a `summary.csv` and per-model output folders.

#### Single-Model Tools

```bash
# Scan all features of a model
FreeCADCmd.exe exp_tools/modifier/test_model.py model.py scan

# Modify feature 2 with 1.5x scale
FreeCADCmd.exe exp_tools/modifier/test_model.py model.py test 2 1.5
```

#### Output Structure

```
exp_output/
├── experiment.log           # Overall run log
├── summary.csv              # Per-experiment summary (success/fail)
├── 00039419/                # Model output directory
│   ├── scan_all.json        # Feature scan result (JSON)
│   ├── scan_all.log         # FreeCAD scan output
│   └── feature_0/           # Per-feature directory
│       ├── scale_0.3456/    # Per-scale experiment
│       │   ├── experiment.log
│       │   ├── original.brep
│       │   └── modified.brep
│       ├── scale_0.7821/
│       │   └── ...
│       └── ...
├── 00040108/
│   └── ...
```

## Dataset

The `exp_tools/dataset/` directory contains the **424 curated FreeCAD Python scripts** used in the paper, converted from DeepCAD and validated for experimental use. Each script recreates a parametric CAD model when executed inside FreeCAD.

## License

MIT License. See [LICENSE](LICENSE).

## Citation

If you use this project in your research, please cite:

```bibtex
@inproceedings{chen2026validityassured,
  author  = {Chen, Zehao and Zheng, Zihe and Lu, Yang and Feng, Yushan and Li, Jialin and Chen, Cong and Liu, Ligang},
  title   = {Validity-Assured Regeneration of Parametric Solid Modeling},
  booktitle = {SIGGRAPH Asia},
  year    = {2026},
  doi     = {10.1145/3829340.3842251}
}
```

## References

- [DeepCAD Dataset](https://github.com/liruilong940607/DeepCAD)
- [FreeCAD](https://www.freecad.org/)
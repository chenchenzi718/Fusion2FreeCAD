# DeepCAD2Free

**DeepCAD2Free** converts DeepCAD parametric CAD models into FreeCAD Python scripts, and provides tools for modifying model parameters in experiments.

## Prerequisites

- **FreeCAD 1.0.1** — our experiments use a custom build forked from the official 1.0.1 branch. Other branches or release versions may have API compatibility issues.

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

For pipeline details and module-level API documentation, see [deepcad2free/README.md](deepcad2free/README.md).

### Experiment Tools

The `exp_tools/` directory contains utilities for running parameter modification experiments on converted FreeCAD models.

#### Run All Experiments

For each model in the dataset, scan features and modify each by random scale factors:

```bash
# Default: 5 random scales per feature in [0.1, 0.9], seed=42
python -m exp_tools.main

# Custom parameters
python -m exp_tools.main \
    --dataset-dir exp_tools/dataset \
    --output-dir exp_output \
    --scales 5 --scale-min 0.1 --scale-max 0.9 \
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

See [exp_tools/README.md](exp_tools/README.md) for more details.

## Dataset

The `exp_tools/dataset/` directory contains **425 curated FreeCAD Python scripts** that have been converted from DeepCAD and validated for experimental use. Each script recreates a parametric CAD model when executed inside FreeCAD.

See [exp_tools/dataset/dataset_info.md](exp_tools/dataset/dataset_info.md) for details.

## License

MIT License. See [LICENSE](LICENSE).

## Citation

If you use this project in your research, please cite:

```bibtex
@inproceedings{deepcad2free,
  author  = {TODO},
  title   = {Validity-Assured Fast Regeneration of Parametric Solid Modeling},
  booktitle = {TODO},
  year    = {2026}
}
```

## References

- [DeepCAD Dataset](https://github.com/liruilong940607/DeepCAD)
- [FreeCAD](https://www.freecad.org/)
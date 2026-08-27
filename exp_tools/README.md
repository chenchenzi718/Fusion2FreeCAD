# Experiment Tools

Utilities for modifying parameters of FreeCAD CAD models. These tools operate on the converted FreeCAD Python scripts in the `dataset/` directory.

## Structure

```
exp_tools/
├── main.py                  # Experiment runner (entry point)
├── config.py                # Configuration — paths, scale range, random seed
├── modifier/
│   ├── test_model.py        # Load .py scripts, scan or modify features
│   ├── feature_modifier.py  # Modify features in .FCStd files directly
│   └── gradient_gen.py      # Gradient scale generator & CSV helpers
└── dataset/                 # 424 validated FreeCAD Python scripts
```

## Quick Start

### 1. Configure

Edit `exp_tools/config.py` or set environment variables:

```bash
# Set FreeCAD path
set FREECAD_CMD=C:\path\to\FreeCAD\bin\FreeCADCmd.exe
```

### 2. Run Experiments

```bash
# Run all experiments with defaults
python -m exp_tools.main

# Custom parameters
python -m exp_tools.main \
    --dataset-dir exp_tools/dataset \
    --output-dir exp_output \
    --scales 5 \
    --scale-min 0.1 \
    --scale-max 1.9 \
    --seed 42 \
    --verbose
```

For each model, the runner:
1. **Scans** all Pad/Pocket features via `test_model.py scan`
2. **Samples** `NUM_SCALES` random scale factors from `[SCALE_MIN, SCALE_MAX]` per feature
3. **Modifies** the feature by each scale, exports BRep files
4. **Logs** results to per-experiment log files

### 3. Output Structure

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

## Test Model

The `test_model.py` script is executed inside `FreeCADCmd` and supports two modes:

### Scan Mode

List all modifiable Pad/Pocket features as JSON:

```bash
FreeCADCmd.exe modifier/test_model.py <model.py> scan
```

### Test Mode

Modify a feature by scale factor, optionally export BRep:

```bash
# Basic — modify only
FreeCADCmd.exe modifier/test_model.py <model.py> test <feature_idx> <scale_factor>

# With BRep export
FreeCADCmd.exe modifier/test_model.py <model.py> test <feature_idx> <scale_factor> \
    <original.brep> <modified.brep>
```

## Feature Modifier

Modify Pad/Pocket/Fillet/Chamfer features in `.FCStd` files.

**Supported features:**
| Feature Type | Modified Property | Default Delta |
|---|---|---|
| PartDesign::Pad | Length | +0.1 mm |
| PartDesign::Pocket | Length | +0.1 mm |
| PartDesign::Fillet | Radius | +0.01 mm |
| PartDesign::Chamfer | Size | +0.01 mm |

**Usage:**
```bash
FreeCADCmd.exe modifier/feature_modifier.py model.FCStd <feature_index>
```

## Gradient Generator

Helper functions for experiment orchestration:

```python
from exp_tools.modifier.gradient_gen import generate_scales

# Generate 5 random scales in [0.1, 1.9]
generate_scales("scales.txt", 0.1, 1.9, 5)
```

## Note on Removed Components

The original experiment pipeline included model screening and log analysis modules. These are not included in this release because they depend on a custom FreeCAD build that is not publicly available. The parameter modification tools provided here work with any FreeCAD installation.
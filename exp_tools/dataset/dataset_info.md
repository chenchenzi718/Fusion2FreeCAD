# Validation Dataset

## Overview

This directory contains **424 curated FreeCAD Python scripts** that have been converted from the DeepCAD dataset and validated for use in parametric CAD model modification experiments.

Each `.py` file is a self-contained FreeCAD script that:
1. Creates a new FreeCAD document
2. Builds a `PartDesign::Body` with one or more sketches
3. Applies Pad/Pocket (extrude) operations to create a solid model

## Naming Convention

Files follow the pattern `{data_id}_free.py`, where `data_id` is an 8-digit identifier from the DeepCAD dataset.

## Usage

### Run experiments via exp_tools

```bash
# Run all experiments on the dataset
python -m exp_tools.main --dataset-dir exp_tools/dataset
```

### Scan features (single model)

```bash
FreeCADCmd.exe exp_tools/modifier/test_model.py model_file.py scan
```

### Modify a feature by scale factor

```bash
FreeCADCmd.exe exp_tools/modifier/test_model.py model_file.py test <feature_idx> <scale_factor>
```

See the [exp_tools README](../README.md) for detailed instructions.

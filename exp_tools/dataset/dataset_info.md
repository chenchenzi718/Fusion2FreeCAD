# Validation Dataset

## Overview

This directory contains **425 curated FreeCAD Python scripts** that have been converted from the DeepCAD dataset and validated for use in parametric CAD model modification experiments.

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

## Filtering Criteria

The models in this dataset were selected through a multi-stage filtering process:
- Successfully converted from DeepCAD JSON to FreeCAD Python
- Successfully rebuilt in FreeCAD (no errors during script execution)
- Contain at least one modifiable Pad or Pocket feature
- Filtered for structural diversity (varying operation sequence lengths and types)

## Limitations

- Models only contain Sketch + Extrude (Pad/Pocket) operations
- Intersect operations are not supported
- Some models may fail when parameters are modified beyond a reasonable range
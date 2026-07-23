# Experiment Tools

Utilities for modifying parameters of FreeCAD CAD models. These tools operate on the converted FreeCAD Python scripts in the `dataset/` directory.

## Structure

```
exp_tools/
├── modifier/
│   ├── feature_modifier.py    # Modify features in .FCStd files directly
│   ├── test_model.py          # Load .py scripts, scan or modify features
│   └── gradient_gen.py        # Gradient scale generator & CSV helpers
└── dataset/                   # ~425 validated FreeCAD Python scripts
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
FreeCADCmd.exe feature_modifier.py model.FCStd <feature_index>
```

## Test Model

Load a FreeCAD Python script, scan its features, or modify parameters.

**Modes:**

| Mode | feature_idx | Description |
|---|---|---|
| SCAN_ALL | 777777 | List all modifiable Pad/Pocket features |
| TEST | 888888 | Modify a specific feature by scale factor |
| SINGLE | (default) | Modify feature at index to random length |

**Usage:**
```bash
# Scan all features (outputs JSON)
FreeCADCmd.exe test_model.py model.py 777777

# Modify feature 2 with 1.5x scale
FreeCADCmd.exe test_model.py model.py 888888 2 1.5 group_a_scale0

# Modify feature 0 to random length in [10, 50] mm
FreeCADCmd.exe test_model.py model.py 0 10 50
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
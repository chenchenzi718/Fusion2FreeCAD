# Fusion2Free 项目总结

## 项目概述

**Fusion2Free** 是一个专业的 CAD 模型转换与实验平台，主要功能包括：

1. **Fusion 360 JSON → FreeCAD Python 脚本转换** - 在不同 CAD 平台间转换参数化设计
2. **FreeCAD 版本验证与测试** - 对比不同 FreeCAD 构建版本（IREP 定制版 vs 标准版）的稳定性和性能
3. **CAD 模型修改与梯度测试** - 提供参数化特征编辑工具

---

## 项目结构

```
Fusion2Free-master/
├── 核心转换脚本
│   ├── fusion2free.py           # 主转换引擎 (Fusion JSON → FreeCAD Python)
│   ├── fusion2free_main.py      # 批处理协调器
│   ├── fusion_clean.py          # Fusion 360 模型清理/修复
│   ├── free2fusion.py           # 反向转换 (FreeCAD → Fusion)
│   ├── free2fusion_new.py       # 新版反向转换
│   ├── check_db_structure.py    # 数据库验证
│   └── reset_convert_status.py  # 转换状态重置工具
│
├── utils/                        # 工具模块
│   ├── define.py                 # 路径和常量定义 (FreeCAD 库路径等)
│   ├── free_opeartion.py        # FreeCAD 操作函数
│   ├── freeCheck.py              # FreeCAD 模型验证 (通过 FreeCADCmd)
│   ├── load_fusion.py            # Fusion 360 JSON 加载器/解析器
│   ├── logging_db.py             # SQLite 日志数据库
│   ├── naming_utils.py           # 平台间名称映射/编码
│   ├── cad_filter.py             # CAD 模型过滤
│   ├── get_free_bbox.py          # 包围盒计算
│   └── reduplicate_util.py       # 去重工具
│
├── test_suite/                   # 测试与实验框架
│   ├── test_model.py             # 单模型修改/梯度测试
│   ├── analyze_log.py            # 日志分析工具
│   ├── analysis_time.py          # 时间分析
│   ├── experiment.bat            # 实验运行器
│   ├── extract_py.bat            # Python 提取脚本
│   ├── extract_large.bat
│   ├── extract_py_with_name.bat
│   ├── analysis_time.bat         # 时间分析批处理
│   └── batch_gradient_test.bat   # 批量梯度测试
│
├── data/                         # 数据目录
│   ├── cad_json_repair/          # 输入: Fusion 360 JSON 文件 (0000-0026 子目录)
│   ├── cad_py_repair/            # 输出: 生成的 FreeCAD Python 脚本
│   ├── cad_free_repair/          # 输出: 生成的 FreeCAD .FCStd 文件
│   ├── dataset/                  # 数据集管理
│   ├── prune/                    # 修剪/过滤后的数据
│   └── old/                      # 旧数据 (验证样本等)
│
├── logging/                      # 日志和跟踪数据库
│   └── log.db                    # 记录转换状态的 SQLite 数据库
│
├── temp/                         # 临时文件
│   └── batch_gradient/           # 批量梯度测试输出
│
├── 配置文件
│   ├── README.md                 # 中文文档 (FreeCAD 对比为主)
│   ├── CLAUDE.md                 # 英文文档 (转换工具为主)
│   ├── PROJECT_SUMMARY.md        # 本文档
│   ├── requirements.txt          # Python 依赖
│   └── .gitignore
│
└── 其他
    ├── deepcad_data_split_6bit.pkl  # 预分割数据集 pickle
    ├── .vscode/                  # VS Code 配置
    ├── .claude/                  # Claude 配置
    └── .git/                     # Git 仓库
```

---

## 核心技术组件

### 1. 核心转换管道 (fusion2free.py)

系统的核心，将 Fusion 360 JSON 转换为 FreeCAD Python 脚本：
- 解析 Fusion 360 的序列化模型表示
- 转换草图（直线、圆弧、圆）
- 处理拉伸（NewBodyFeatureOperation、join、cut）
- 管理布尔运算
- 使用 `FreeCADNameEncoder` 将 Fusion 实体名称映射为 FreeCAD 安全名称

### 2. 批处理 (fusion2free_main.py)

- 处理 `data/cad_json_repair/` 中的数千个 CAD JSON 文件
- 通过 SQLite (`logging/log.db`) 跟踪转换状态
- 支持并行处理（线程安全的数据库写入）
- 通过 FreeCADCmd 验证转换后的模型

### 3. 数据库架构 (utils/logging_db.py)

```sql
CREATE TABLE logs (
    data_id TEXT PRIMARY KEY,
    is_convert INTEGER,        -- 1 = 已转换, 0 = 未转换
    fusion_sequence TEXT,       -- Fusion 的操作序列
    free_sequence TEXT,         -- 生成的 FreeCAD 操作序列
    is_valid INTEGER,           -- 1 = 已验证, 0 = 未验证
    error_code TEXT             -- 失败时的错误信息
);
```

### 4. FreeCAD 验证 (utils/freeCheck.py)

- 调用 FreeCADCmd.exe 执行生成的 Python 脚本
- 验证模型重建
- 导出为 .FCStd 格式

### 5. 测试框架 (test_suite/test_model.py)

三种操作模式：
1. **单模式**: 修改指定特征的拉伸长度
2. **扫描模式**: 随机选择并修改一个特征（排除第一个）
3. **测试模式**: 带缩放因子的梯度测试

功能：
- 加载并执行 FreeCAD Python 脚本
- 修改 PartDesign::Pad 特征
- 将修改后的模型导出为 STEP 文件
- 基于 JSON 的结果报告

---

## FreeCAD 版本对比实验

项目包含两个 FreeCAD 构建版本之间的广泛对比测试：

| 版本 | 描述 |
|------|------|
| **FC1** | IREP_Project 定制版 (FreeCAD 0.22.0devR38854) |
| **FC2** | 标准版 FreeCAD (FreeCAD 1.0.1R39285) |

**关键发现** (来自 README.md)：
- FC1 存在内存稳定性问题（"Illegal storage access" 崩溃）
- FC2 稳定性更好，无内存崩溃
- 在 3 个批次（共 63 个文件）上进行了测试

### 跨批次对比

| 批次 | 文件数 | FC1 崩溃率 | FC1 警告率 | FC2 正常率 | FC2 警告率 |
|------|--------|-----------|-----------|-----------|-----------|
| 0002 | 18 | 100% | 0% | 0% | 100% |
| 0003 | 8 | 0% | 25% | 100% | 0% |
| 0004 | 37 | 18.9% | 43.2% | 73.0% | 18.9% |

### 错误类型分类

- **内存错误**: `Illegal storage access` - 仅在 FC1 出现
- **几何警告**: `Wire is not closed` - 线框未闭合
- **拓扑警告**: `makeElementFace: resulting face is invalid` - 无法构建有效面
- **链接警告**: `No object linked` - 挤压操作缺少关联对象

---

## 梯度测试框架

### batch_gradient_test.bat

批量测试 CAD 模型的参数化修改功能，对每个模型执行 5 种梯度的参数缩放：

| 梯度名称 | 缩放因子 | 描述 |
|---------|---------|------|
| large_reduction | 0.25x | 大幅缩小 |
| small_reduction | 0.60x | 小幅缩小 |
| tiny_adjust | 1.02x | 微调 |
| small_increase | 1.50x | 小幅增大 |
| large_increase | 2.50x | 大幅增大 |

### analysis_time.py / analysis_time.bat

分析 validated 目录的测试结果：

- **失败判定**: 包含 `"criteria X failed"`
- **成功判定**: 包含 `"Fast Regeneration"` + `"Time ratio"`

成功案例提取 6 个指标：
- `criteria1_time` - 标准 1 耗时
- `criteria2_time` - 标准 2 耗时
- `sewing_time` - 缝合算法耗时
- `fast_regen_total` - 快速再生总耗时
- `gbr_total` - GBR 总耗时
- `time_ratio` - 时间比

### 输出目录结构

```
analysis/
├── summary.csv              # 所有模型汇总（每个模型一行）
├── per_model/               # 每个模型的详细结果（每个梯度一行）
│   ├── {model_name}.csv
│   └── ...
└── excellent/               # time_ratio > 5 的模型文件夹
    ├── {model_name}/
    └── ...
```

---

## Python 依赖

来自 requirements.txt：
- `colorama==0.4.6`
- `joblib==1.4.2` (并行处理)
- `numpy==1.24.4`
- `pandas==2.0.3`
- `python-dateutil==2.9.0.post0`
- `pytz==2024.2`
- `six==1.17.0`
- `tqdm==4.67.1` (进度条)
- `tzdata==2024.2`

---

## 支持的 Fusion 360 特征

- 草图（直线、圆弧、圆）
- 拉伸（新实体、合并、切割操作）
- 布尔运算（合并、切割）

---

## 数据流

```
Fusion 360 JSON (data/cad_json_repair/)
       ↓
   [fusion2free.py]
       ↓
FreeCAD Python Script (data/cad_py_repair/)
       ↓
   [freeCheck.py + FreeCADCmd]
       ↓
FreeCAD .FCStd File (data/cad_free_repair/)
       ↓
   [SQLite DB (logging/log.db)]
```

---

## 关键文件路径

- **主转换脚本**: `fusion2free_main.py`
- **核心转换器**: `fusion2free.py`
- **配置/路径**: `utils/define.py`
- **测试模型修改器**: `test_suite/test_model.py`
- **日志数据库**: `logging/log.db`
- **输入 JSON 数据**: `data/cad_json_repair/`

---

## 这是一个研究级 CAD 互操作性平台，用于模型转换和 FreeCAD 稳定性测试！

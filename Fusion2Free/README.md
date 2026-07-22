# Fusion2Free

Fusion2Free 是一个强大的 CAD 模型转换工具，专门用于将 Fusion 360 设计文件转换为 FreeCAD 格式。该工具支持复杂的几何体转换，并提供完整的数据验证和修复功能。

## 项目简介

在 CAD 设计工作流程中，不同软件平台之间的模型转换一直是一个挑战。Fusion2Free 旨在解决 Fusion 360 与开源 CAD 软件 FreeCAD 之间的互操作性问题，使设计师和工程师能够在这两个平台之间无缝切换。

主要功能：

- Fusion 360 JSON 模型到 FreeCAD Python 脚本的转换
- 自动修复常见的 CAD 模型问题
- 验证转换后的模型完整性
- 详细的转换日志和错误跟踪
- 批量处理大量模型文件
- 支持多线程并行处理

新增：快速再生（Fast Regeneration）测试套件（test_suite/）
- 测试修改模型参数后的快速再生性能
- 对比Fast Regeneration与GBR（Global Boolean Regeneration）
- 支持两组梯度范围测试：[0.1, 1.9]和[0.9, 1.1]
- 生成Excel报告和可视化图表

## 系统要求

- Python 3.6+
- FreeCAD 0.21+（安装在指定路径，默认为 `C:\Program Files\FreeCAD 0.21\lib`）
- 以下 Python 依赖项：
  - numpy
  - tqdm
  - joblib
  - sqlite3

## 安装说明

1. 克隆该仓库：

```bash
git clone https://github.com/yourusername/Fusion2Free.git
cd Fusion2Free
```

1. 安装依赖项：

```bash
pip install -r requirements.txt
```

1. 确保 FreeCAD 已正确安装，并检查 `utils/define.py` 中的路径是否与您的 FreeCAD 安装路径一致。

## 使用方法

### 基本用法

运行主转换程序：

```bash
python fusion2free_main.py
```

这将处理 `data/cad_json_repair` 目录中的所有 Fusion 360 JSON 文件，并将转换后的 FreeCAD 文件保存在 `data/cad_py_repair` 和 `data/cad_free_repair` 目录中。

### 高级用法

#### 清理 Fusion 360 模型

修复 Fusion 360 JSON 数据中的常见问题：

```bash
python fusion_clean.py
```

#### 生成变体 Fusion 360 模型

```bash
python free2fusion.py
```

#### 修改转换参数

在 `utils/define.py` 中调整路径和其他常量设置。

## 项目结构

- `fusion2free.py`: 核心转换引擎，将 Fusion 360 JSON 转换为 FreeCAD Python 脚本
- `fusion2free_main.py`: 主程序入口点
- `free2fusion.py`: 反向转换支持
- `fusion_clean.py`: Fusion 360 模型修复工具
- `utils/`: 功能模块目录
  - `define.py`: 全局常量定义
  - `free_opeartion.py`: FreeCAD 操作函数集
  - `freeCheck.py`: FreeCAD 模型验证工具
  - `load_fusion.py`: Fusion 模型加载函数
  - `logging_db.py`: 日志记录数据库
  - `naming_utils.py`: 命名转换工具
  - `cad_filter.py`: CAD 模型过滤工具
  - `get_free_bbox.py`: 获取 FreeCAD 模型边界盒信息
  - `reduplicate_util.py`: 数据去重工具

## 转换过程

Fusion2Free 的转换过程如下：

1. **加载 Fusion 模型**: 解析 Fusion 360 JSON 文件
2. **分析模型结构**: 识别草图、特征和操作序列
3. **转换几何体**: 将 Fusion 360 几何元素转换为 FreeCAD 对应项
4. **生成 Python 脚本**: 创建用于重建模型的 FreeCAD Python 脚本
5. **验证模型**: 在 FreeCAD 中执行生成的脚本并验证结果
6. **记录结果**: 将转换状态和可能的错误记录到数据库

## 支持的特性

当前版本支持以下 Fusion 360 特性的转换：

- 草图（直线、圆弧、圆）
- 拉伸（新体、连接、切除）
- 布尔操作（连接、切除）

## 数据库和日志

该工具使用 SQLite 数据库跟踪转换过程。日志包含以下信息：

- 数据 ID
- 转换状态
- Fusion 序列
- FreeCAD 序列
- 验证状态
- 错误代码

日志可以导出为 CSV 文件，便于分析和报告。

## 错误处理

Fusion2Free 识别并处理以下常见错误：

- EMPTY SKETCH: 空草图
- EMPTY EXTRUDE PROFILE: 空拉伸剖面
- UNUSED SKETCH: 未使用的草图

## 开发指南

### 添加新的几何体转换

要支持新的几何体类型，请在 `fusion2free.py` 中修改 `fusion2free` 函数，添加新的处理分支。

### 改进验证过程

可以通过修改 `utils/freeCheck.py` 中的验证逻辑来提高验证的准确性。

### 扩展支持的操作

要添加新的 CAD 操作支持，需要：

1. 在 `utils/free_opeartion.py` 中添加相应的 FreeCAD 操作函数
2. 在 `fusion2free.py` 中更新转换逻辑

## 贡献指南

欢迎贡献代码、报告问题或提出改进建议！请遵循以下步骤：

1. Fork 仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 许可证

该项目采用 \[您的许可证] 许可 - 详情请参阅 LICENSE 文件。

## 联系方式

如有问题或建议，请通过以下方式联系我们：

- Email: <your.email@example.com>
- Issue Tracker: <https://github.com/yourusername/Fusion2Free/issues>

## 快速再生（Fast Regeneration）测试套件

项目包含一个完整的测试套件（`test_suite/`），用于测试和验证快速再生算法的性能。

### 测试流程

1. **扫描模型**：识别所有Pad/Pocket特征及其原始尺寸
2. **梯度生成**：
   - Group A：5个随机值∈[0.1, 1.9]（大范围测试）
   - Group B：5个随机值∈[0.9, 1.1]（小范围微调测试）
3. **测试执行**：对每个特征的每个scale执行修改并记录日志
4. **结果分析**：生成Excel报告和可视化图表

### 运行测试

```cmd
cd test_suite
batch_gradient_test.bat
```

### Excel报告结构

生成的`analysis_report.xlsx`包含4个sheet：

| Sheet            | 说明                              |
|-----------------|----------------------------------|
| group_a         | Group A模型级汇总统计            |
| group_b         | Group B模型级汇总统计            |
| group_a_features| Group A特征级详细数据（每行一个feature）|
| group_b_features| Group B特征级详细数据（每行一个feature）|

### 分析和可视化

使用`Paper/analysis/`目录下的脚本：

```bash
# 生成统计图表
python Paper/analysis/plot_results.py analysis_report.xlsx
```

生成：
- `histogram_ratio_avg.pdf`：时间比直方图
- `scatter_gr_gbr.pdf`：GR vs GBR散点图

### 聚合逻辑

1. **Scale层**：对每个feature的5个scale结果取平均
2. **Feature层**：对每个model的所有feature结果取平均
3. **total_gbr_all/total_fast_all**：使用scale层平均而非求和

## 致谢

- FreeCAD 开发团队
- Autodesk Fusion 360 API 文档


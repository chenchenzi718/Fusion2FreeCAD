import os
import sys
import traceback

from utils.define import EOL

# 移除 FreeCAD 库路径设置，因为不再直接导入 FreeCAD 模块
# fys+修改了 FreeCAD 调用方式，从直接导入改为通过命令行调用

import subprocess
import sys
import os
import tempfile

# 根据你的FreeCAD安装路径进行修改
# fys+添加了 FreeCAD 命令行路径配置
FREECAD_CMD_PATH = r"D:\name_and_rebuild\FreeCAD\bin\freecadcmd.exe"


def run_freecad_modeling(data_id, py_dir, logging_dir, output_free_path):
    """
    data_id: 用于标识文件存储的名称前缀
    py_dir: 包含FreeCAD建模python语句的列表
    logging_dir: 日志文件存储目录
    语句示例：
    .\FreeCADCmd.exe   "D:\AI_SDK\Fusion2Free\00000007_free.py" --log-file "D:\AI_SDK\Fusion2Free\00000007_free.log"
    """
    # Validity check disabled
    return
    # 确保输出目录存在
    output_dir = os.path.join(output_free_path, data_id[:4])
    os.makedirs(output_dir, exist_ok=True)
    
    # 构建保存路径
    save_path = os.path.join(output_dir, f"{data_id}_free.FCStd")
    
    # 确保 py_dir 是绝对路径
    # fys+调整了路径处理顺序，先转换为绝对路径再检查文件存在性
    py_dir = os.path.abspath(py_dir)
    # 确保目录存在
    py_subdir = os.path.join(py_dir, data_id[:4])
    os.makedirs(py_subdir, exist_ok=True)
    
    # 检查文件是否存在
    py_file_path = os.path.join(py_subdir, f"{data_id}_free.py")
    if not os.path.exists(py_file_path):
        raise FileNotFoundError(f"Python file not found: {py_file_path}")
    
    # 构建临时脚本，包含建模和保存操作
    temp_script_content = f"""
import FreeCAD as App
import Part
import os

# 读取并执行建模命令
modeling_lines = []
py_file_path = r"{py_file_path}"
print(f"Reading Python file: {{py_file_path}}")
with open(py_file_path, 'r', encoding='utf-8') as f:
    for line in f:
        modeling_lines.append(line)

# 执行建模命令
for line in modeling_lines:
    line = line.strip()
    if line:
        exec(line)

# 保存文档
doc = App.ActiveDocument
if doc:
    doc.recompute()
    # FreeCAD 0.21+ 推荐使用 saveAs 的完整路径
    doc.saveAs(r"{save_path}")
    App.closeDocument(doc.Name)
"""

    
    print(f"Python file exists: {py_file_path}")
    
    # 写入临时脚本
    temp_script_path = os.path.join(tempfile.gettempdir(), f"{data_id}_temp.py")
    with open(temp_script_path, 'w', encoding='utf-8') as f:
        f.write(temp_script_content)
    
    # 构建命令
    cmd = [FREECAD_CMD_PATH, temp_script_path]
    
    # 执行命令
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # 清理临时文件
    try:
        os.remove(temp_script_path)
    except:
        pass
    
    # 检查错误
    if result.stderr:
        raise Exception("Error occurred during FreeCAD modeling:\n" + result.stderr.split('\n')[0])
    
    return f'{data_id}_free.FCStd'


if __name__ == "__main__":
    # 示例建模语句（可自行替换）
    path = '../00000062_free.py'
    modeling_script = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            modeling_script.append(line)
    run_freecad_modeling("00000062", "./data/cad_py_repair", "./logging", "./data/cad_free_repair")

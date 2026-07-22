import os
import sqlite3

# 数据库路径
db_path = os.path.join('logging', 'log.db')
# Python 文件存储路径
py_dir = './data/cad_py_repair/'

# 连接到数据库
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 查询所有 is_convert=1 的记录
cursor.execute("SELECT data_id FROM logs WHERE is_convert = 1")
records = cursor.fetchall()

# 重置文件不存在的记录的 is_convert 值
reset_count = 0
for record in records:
    data_id = record[0]
    # 构建文件路径
    file_path = os.path.join(py_dir, data_id[:4], f"{data_id}_free.py")
    # 检查文件是否存在
    if not os.path.exists(file_path):
        # 重置 is_convert 为 0
        cursor.execute("UPDATE logs SET is_convert = 0 WHERE data_id = ?", (data_id,))
        reset_count += 1
        print(f"Reset is_convert for {data_id}")

# 提交更改
conn.commit()
# 关闭连接
conn.close()

print(f"Reset {reset_count} records")

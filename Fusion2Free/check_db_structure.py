import os
import sqlite3

# 数据库路径
db_path = os.path.join('logging', 'log.db')

# 连接到数据库
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 查看所有表
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:")
for table in tables:
    print(f"- {table[0]}")

# 查看表结构
if tables:
    table_name = tables[0][0]
    print(f"\nStructure of table {table_name}:")
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    for column in columns:
        print(f"- {column[1]} ({column[2]})")

# 关闭连接
conn.close()

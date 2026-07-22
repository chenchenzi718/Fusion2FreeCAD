import sqlite3
import csv
from typing import Optional, List, Any

import sqlite3
import csv
from typing import List, Optional, Dict


class LogDatabase:
    def __init__(self, db_path: str, auto_commit: bool = False, use_wal: bool = True):
        """
        初始化数据库连接，并创建表（如果不存在）。

        :param db_path: 数据库文件路径
        :param auto_commit: 是否在每次更新后自动提交事务（会降低写入性能）
        :param use_wal: 是否启用 WAL(Write-Ahead Logging) 模式，提高并发写性能
        """
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # 启用 WAL 模式（可选）
        if use_wal:
            self.cursor.execute("PRAGMA journal_mode=WAL;")
            # WAL 模式需要手动 commit 一下才能生效
            self.conn.commit()

        self._create_table()

        # 如果 auto_commit = False，则由用户自行控制事务提交
        self.auto_commit = auto_commit

    def begin_transaction(self):
        """
        手动开始一个事务。
        """
        self.cursor.execute("BEGIN TRANSACTION;")

    def commit(self):
        """
        手动提交当前事务。
        """
        self.conn.commit()

    def _create_table(self):
        """
        创建日志表，如果表已经存在则跳过。
        """
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS logs (
            data_id TEXT PRIMARY KEY,
            is_convert INTEGER,
            fusion_sequence TEXT,
            free_sequence TEXT,
            is_valid INTEGER,
            error_code TEXT
        );
        """
        self.cursor.execute(create_table_sql)
        self.conn.commit()  # 这里必须提交，确保表结构已创建

    def _row_to_dict(self, row: tuple) -> dict:
        """
        将数据库行转换为字典。
        """
        return {
            'data_id': row[0],
            'is_convert': row[1],
            'fusion_sequence': row[2],
            'free_sequence': row[3],
            'is_valid': row[4],
            'error_code': row[5]
        }

    def get_data_id(self, data_id: str) -> Optional[dict]:
        """
        根据 data_id 获取记录。
        """
        self.cursor.execute("SELECT * FROM logs WHERE data_id = ?", (data_id,))
        row = self.cursor.fetchone()
        return self._row_to_dict(row) if row else None

    def set_data_id(self, data_id: str, **kwargs):
        """
        插入或更新记录。
        这里演示如何减少频繁的 commit 调用，提高写入效率。
        """
        existing_record = self.get_data_id(data_id)
        fields = []
        values = []
        if existing_record:
            # 更新现有记录
            for key, value in kwargs.items():
                if key in ['is_convert', 'fusion_sequence', 'free_sequence', 'is_valid', 'error_code']:
                    fields.append(f"{key} = ?")
                    values.append(value)
            values.append(data_id)
            if fields:
                update_sql = f"UPDATE logs SET {', '.join(fields)} WHERE data_id = ?"
                self.cursor.execute(update_sql, tuple(values))
        else:
            # 插入新记录
            insert_sql = """
            INSERT INTO logs (data_id, is_convert, fusion_sequence, free_sequence, is_valid, error_code)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            self.cursor.execute(insert_sql, (
                data_id,
                kwargs.get('is_convert', 0),
                kwargs.get('fusion_sequence', ''),
                kwargs.get('free_sequence', ''),
                kwargs.get('is_valid', 0),
                kwargs.get('error_code', '')
            ))

        # 如果启用了 auto_commit，则每次都立即写入磁盘
        if self.auto_commit:
            self.conn.commit()

    # 以下 Getter/Setter 可以保留（或者干脆只保留 set_data_id 来做所有更新）
    def get_is_convert(self, data_id: str) -> Optional[int]:
        row = self.get_data_id(data_id)
        return row['is_convert'] if row else None

    def set_is_convert(self, data_id: str, value: int):
        self.set_data_id(data_id, is_convert=value)

    def get_fusion_sequence(self, data_id: str) -> Optional[str]:
        row = self.get_data_id(data_id)
        return row['fusion_sequence'] if row else None

    def set_fusion_sequence(self, data_id: str, value: str):
        self.set_data_id(data_id, fusion_sequence=value)

    def get_free_sequence(self, data_id: str) -> Optional[str]:
        row = self.get_data_id(data_id)
        return row['free_sequence'] if row else None

    def set_free_sequence(self, data_id: str, value: str):
        self.set_data_id(data_id, free_sequence=value)

    def get_is_valid(self, data_id: str) -> Optional[int]:
        row = self.get_data_id(data_id)
        return row['is_valid'] if row else None

    def set_is_valid(self, data_id: str, value: int):
        self.set_data_id(data_id, is_valid=value)

    def get_error_code(self, data_id: str) -> Optional[str]:
        row = self.get_data_id(data_id)
        return row['error_code'] if row else None

    def set_error_code(self, data_id: str, value: str):
        self.set_data_id(data_id, error_code=value)

    # CSV 导出和导入
    def dump_to_csv(self, csv_path: str):
        """
        将表中内容导出到 CSV 文件。
        """
        self.cursor.execute("SELECT * FROM logs")
        rows = self.cursor.fetchall()
        with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            # 写入表头
            writer.writerow(['data_id', 'is_convert', 'fusion_sequence', 'free_sequence', 'is_valid', 'error_code'])
            # 写入数据
            writer.writerows(rows)

    def rebuild_from_csv(self, csv_path: str):
        """
        从 CSV 文件重建数据库表。
        """
        with open(csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            self.cursor.execute("DELETE FROM logs")  # 清空现有数据
            for row in reader:
                self.set_data_id(
                    row['data_id'],
                    is_convert=int(row['is_convert']),
                    fusion_sequence=row['fusion_sequence'],
                    free_sequence=row['free_sequence'],
                    is_valid=int(row['is_valid']),
                    error_code=row['error_code']
                )
        self.conn.commit()

    def count_invalid_records(self) -> int:
        """
        统计 is_valid 为 0 的记录数。
        """
        self.cursor.execute("SELECT COUNT(*) FROM logs WHERE is_valid = 0")
        return self.cursor.fetchone()[0]

    def count_by_error_code(self) -> List[tuple]:
        """
        按 error_code 统计记录数。
        """
        self.cursor.execute("""
            SELECT error_code, COUNT(*) 
            FROM logs 
            GROUP BY error_code
        """)
        return self.cursor.fetchall()

    def get_all_records(self) -> List[dict]:
        """
        获取所有记录。
        """
        self.cursor.execute("SELECT * FROM logs")
        rows = self.cursor.fetchall()
        return [self._row_to_dict(row) for row in rows]

    def close(self):
        """
        关闭数据库连接。
        """
        self.conn.close()


# 示例用法
if __name__ == "__main__":
    db = LogDatabase('logs.db')

    # 插入或更新记录
    db.set_data_id('id_001', is_convert=1, fusion_sequence='seq1', free_sequence='free1', is_valid=1, error_code='E001')
    db.set_data_id('id_002', is_convert=0, fusion_sequence='seq2', free_sequence='free2', is_valid=0, error_code='E002')

    # 获取记录
    record = db.get_data_id('id_001')
    print(record)

    # 更新某个字段
    db.set_error_code('id_001', 'E003')

    # 导出到CSV
    db.dump_to_csv('logs.csv')

    # 重建数据库
    db.rebuild_from_csv('logs.csv')

    # 统计
    invalid_count = db.count_invalid_records()
    print(f"Invalid Records: {invalid_count}")

    error_counts = db.count_by_error_code()
    print("Error Code Counts:")
    for error_code, count in error_counts:
        print(f"{error_code}: {count}")

    # 关闭数据库连接
    db.close()

"""
SQLite-based logging database for tracking conversion status.

Schema:
    data_id (TEXT PK) -- model identifier
    is_convert (INT)  -- 1 if conversion succeeded
    fusion_sequence (TEXT) -- abbreviated operation sequence from Fusion JSON
    free_sequence (TEXT)   -- abbreviated operation sequence of generated FreeCAD script
    is_valid (INT)  -- 1 if FreeCAD validation passed
    error_code (TEXT) -- error message on failure
"""

import csv
import sqlite3
from typing import List, Optional


class LogDatabase:
    """SQLite database for tracking conversion and validation status."""

    def __init__(self, db_path: str, auto_commit: bool = False, use_wal: bool = True):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        if use_wal:
            self.cursor.execute("PRAGMA journal_mode=WAL;")
            self.conn.commit()
        self._create_table()
        self.auto_commit = auto_commit

    def begin_transaction(self):
        """Manually begin a transaction."""
        self.cursor.execute("BEGIN TRANSACTION;")

    def commit(self):
        """Manually commit the current transaction."""
        self.conn.commit()

    def _create_table(self):
        """Create the logs table if it does not exist."""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS logs (
                data_id TEXT PRIMARY KEY,
                is_convert INTEGER,
                fusion_sequence TEXT,
                free_sequence TEXT,
                is_valid INTEGER,
                error_code TEXT
            );
            """
        )
        self.conn.commit()

    def _row_to_dict(self, row: tuple) -> dict:
        return {
            "data_id": row[0],
            "is_convert": row[1],
            "fusion_sequence": row[2],
            "free_sequence": row[3],
            "is_valid": row[4],
            "error_code": row[5],
        }

    def get_data_id(self, data_id: str) -> Optional[dict]:
        """Fetch a record by data_id."""
        self.cursor.execute(
            "SELECT * FROM logs WHERE data_id = ?", (data_id,)
        )
        row = self.cursor.fetchone()
        return self._row_to_dict(row) if row else None

    def set_data_id(self, data_id: str, **kwargs):
        """Insert or update a record. Accepts any subset of table columns as kwargs."""
        existing = self.get_data_id(data_id)
        valid_keys = {"is_convert", "fusion_sequence", "free_sequence", "is_valid", "error_code"}

        if existing:
            fields = []
            values = []
            for key, value in kwargs.items():
                if key in valid_keys:
                    fields.append(f"{key} = ?")
                    values.append(value)
            values.append(data_id)
            if fields:
                update_sql = f"UPDATE logs SET {', '.join(fields)} WHERE data_id = ?"
                self.cursor.execute(update_sql, tuple(values))
        else:
            self.cursor.execute(
                """
                INSERT INTO logs (data_id, is_convert, fusion_sequence, free_sequence,
                                  is_valid, error_code)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    data_id,
                    kwargs.get("is_convert", 0),
                    kwargs.get("fusion_sequence", ""),
                    kwargs.get("free_sequence", ""),
                    kwargs.get("is_valid", 0),
                    kwargs.get("error_code", ""),
                ),
            )

        if self.auto_commit:
            self.conn.commit()

    def get_is_convert(self, data_id: str) -> Optional[int]:
        row = self.get_data_id(data_id)
        return row["is_convert"] if row else None

    def set_is_convert(self, data_id: str, value: int):
        self.set_data_id(data_id, is_convert=value)

    def get_fusion_sequence(self, data_id: str) -> Optional[str]:
        row = self.get_data_id(data_id)
        return row["fusion_sequence"] if row else None

    def set_fusion_sequence(self, data_id: str, value: str):
        self.set_data_id(data_id, fusion_sequence=value)

    def get_free_sequence(self, data_id: str) -> Optional[str]:
        row = self.get_data_id(data_id)
        return row["free_sequence"] if row else None

    def set_free_sequence(self, data_id: str, value: str):
        self.set_data_id(data_id, free_sequence=value)

    def get_is_valid(self, data_id: str) -> Optional[int]:
        row = self.get_data_id(data_id)
        return row["is_valid"] if row else None

    def set_is_valid(self, data_id: str, value: int):
        self.set_data_id(data_id, is_valid=value)

    def get_error_code(self, data_id: str) -> Optional[str]:
        row = self.get_data_id(data_id)
        return row["error_code"] if row else None

    def set_error_code(self, data_id: str, value: str):
        self.set_data_id(data_id, error_code=value)

    def dump_to_csv(self, csv_path: str):
        """Export the logs table to a CSV file."""
        self.cursor.execute("SELECT * FROM logs")
        rows = self.cursor.fetchall()
        with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "data_id", "is_convert", "fusion_sequence",
                "free_sequence", "is_valid", "error_code",
            ])
            writer.writerows(rows)

    def rebuild_from_csv(self, csv_path: str):
        """Rebuild the logs table from a CSV file."""
        with open(csv_path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.cursor.execute("DELETE FROM logs")
            for row in reader:
                self.set_data_id(
                    row["data_id"],
                    is_convert=int(row["is_convert"]),
                    fusion_sequence=row["fusion_sequence"],
                    free_sequence=row["free_sequence"],
                    is_valid=int(row["is_valid"]),
                    error_code=row["error_code"],
                )
        self.conn.commit()

    def count_invalid_records(self) -> int:
        """Count records where is_valid == 0."""
        self.cursor.execute("SELECT COUNT(*) FROM logs WHERE is_valid = 0")
        return self.cursor.fetchone()[0]

    def count_by_error_code(self) -> List[tuple]:
        """Count records grouped by error_code."""
        self.cursor.execute(
            "SELECT error_code, COUNT(*) FROM logs GROUP BY error_code"
        )
        return self.cursor.fetchall()

    def get_all_records(self) -> List[dict]:
        """Return all records as a list of dicts."""
        self.cursor.execute("SELECT * FROM logs")
        return [self._row_to_dict(r) for r in self.cursor.fetchall()]

    def close(self):
        """Close the database connection."""
        self.conn.close()
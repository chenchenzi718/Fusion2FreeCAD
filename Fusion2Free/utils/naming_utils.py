"""
FreeCAD name encoder -- maps Fusion 360 entity IDs to FreeCAD-safe names.

Uses SHA-256 hashing to produce 24-character uppercase alphanumeric strings,
with SQLite persistence for deduplication.
"""

import hashlib
import sqlite3
import string


class FreeCADNameEncoder:
    """Encode Fusion 360 entity names to FreeCAD-safe identifiers."""

    def __init__(self, db_path="name_mapping.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        """Create the name_mapping table if it does not exist."""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS name_mapping (
                original_name TEXT PRIMARY KEY,
                encoded_name TEXT UNIQUE
            )
            """
        )
        self.connection.commit()

    def generate_unique_name(self, original_name):
        """
        Generate a unique name from a SHA-256 hash.

        Returns a 24-character uppercase alphanumeric string that starts with
        a letter (required by FreeCAD naming convention).
        """
        hash_object = hashlib.sha256(original_name.encode("utf-8"))
        hash_digest = hash_object.hexdigest().upper()
        unique_part = hash_digest[:24]
        first_char = unique_part[0]
        if first_char not in string.ascii_uppercase:
            first_char = "A"
        unique_name = first_char + unique_part[1:]
        return unique_name

    def encode_name(self, original_name):
        """Encode a name. If already encoded, return the existing encoding."""
        self.cursor.execute(
            "SELECT encoded_name FROM name_mapping WHERE original_name = ?",
            (original_name,),
        )
        result = self.cursor.fetchone()
        if result:
            return result[0]

        unique_name = self.generate_unique_name(original_name)
        attempt = 1
        max_attempts = 1000

        while True:
            try:
                self.cursor.execute(
                    "INSERT INTO name_mapping (original_name, encoded_name) VALUES (?, ?)",
                    (original_name, unique_name),
                )
                self.connection.commit()
                return unique_name
            except sqlite3.IntegrityError:
                unique_name = self.generate_unique_name(
                    original_name + f"{attempt}"
                )
                attempt += 1
                if attempt > max_attempts:
                    raise Exception("Cannot generate unique encoded name.")

    def decode_name_fusion2free(self, original_name):
        """
        Look up the encoded name for an original name.
        Returns None if not found in DB yet.
        """
        self.cursor.execute(
            "SELECT encoded_name FROM name_mapping WHERE original_name = ?",
            (original_name,),
        )
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def encode_names_bulk(self, original_names):
        """Encode multiple names. Returns {original: encoded} dict."""
        encoded_mapping = {}
        for name in original_names:
            encoded_mapping[name] = self.encode_name(name)
        return encoded_mapping

    def decode_names_bulk_free2fusion(self, encoded_names):
        """Bulk decode: returns {encoded: original} dict."""
        placeholders = ",".join("?" for _ in encoded_names)
        query = (
            f"SELECT encoded_name, original_name FROM name_mapping "
            f"WHERE encoded_name IN ({placeholders})"
        )
        self.cursor.execute(query, encoded_names)
        results = self.cursor.fetchall()
        return {encoded: original for encoded, original in results}

    def decode_names_bulk_fusion2free(self, encoded_names):
        """Bulk decode: returns {encoded: original} dict."""
        placeholders = ",".join("?" for _ in encoded_names)
        query = (
            f"SELECT encoded_name, original_name FROM name_mapping "
            f"WHERE encoded_name IN ({placeholders})"
        )
        self.cursor.execute(query, encoded_names)
        results = self.cursor.fetchall()
        return {encoded: original for encoded, original in results}

    def export_mapping(self, export_path):
        """Export the name mapping to a CSV file."""
        import csv

        self.cursor.execute(
            "SELECT original_name, encoded_name FROM name_mapping"
        )
        rows = self.cursor.fetchall()
        with open(export_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Original Name", "Encoded Name"])
            writer.writerows(rows)

    def import_mapping(self, import_path, direction):
        """Import name mapping from a CSV file."""
        import csv

        with open(import_path, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                original = row["Original Name"]
                encoded = row["Encoded Name"]
                try:
                    if direction == "fusion2free":
                        self.cursor.execute(
                            "INSERT INTO name_mapping (original_name, encoded_name) VALUES (?, ?)",
                            (original, encoded),
                        )
                    elif direction == "free2fusion":
                        self.cursor.execute(
                            "INSERT INTO name_mapping (original_name, encoded_name) VALUES (?, ?)",
                            (encoded, original),
                        )
                except sqlite3.IntegrityError:
                    pass
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        self.connection.close()
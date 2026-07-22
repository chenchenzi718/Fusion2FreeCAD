import hashlib
import sqlite3
import string
import os

from utils.load_fusion import load_fusion


class FreeCADNameEncoder:
    def __init__(self, db_path='name_mapping.db'):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        """初始化数据库，创建必要的表格。"""

        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS name_mapping (
                    original_name TEXT PRIMARY KEY,
                    encoded_name TEXT UNIQUE
                )
            ''')
        self.connection.commit()

    def generate_unique_name(self, original_name):
        """使用 SHA-256 哈希生成唯一名称，确保只包含大写字母和数字，并以字母开头。"""
        hash_object = hashlib.sha256(original_name.encode('utf-8'))
        hash_digest = hash_object.hexdigest().upper()  # 转为大写
        # 选择前16个字符作为名称，确保长度适中
        unique_part = hash_digest[:24]
        # 确保名称以字母开头
        first_char = unique_part[0]
        if first_char not in string.ascii_uppercase:
            first_char = 'A'  # 默认以 'A' 开头
        unique_name = first_char + unique_part[1:]
        return unique_name

    def encode_name(self, original_name):
        """
        将原始名称编码为 FreeCAD 合法的唯一名称。
        如果已经编码过，则返回现有的编码名称。
        """
        # 检查是否已编码
        self.cursor.execute('SELECT encoded_name FROM name_mapping WHERE original_name = ?', (original_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]

        # 生成唯一名称
        unique_name = self.generate_unique_name(original_name)
        attempt = 1
        max_attempts = 1000  # 防止无限循环

        while True:
            try:
                self.cursor.execute('INSERT INTO name_mapping (original_name, encoded_name) VALUES (?, ?)',
                                    (original_name, unique_name))
                self.connection.commit()
                return unique_name
            except sqlite3.IntegrityError:
                # 如果编码名称已存在，可能是哈希冲突，尝试添加一个序号
                unique_name = self.generate_unique_name(original_name + f"{attempt}")
                attempt += 1
                if attempt > max_attempts:
                    raise Exception("无法生成唯一的编码名称，达到最大尝试次数。")

    def decode_name_free2fusion(self, encoded_name):
        """
        通过编码名称查找原始名称。
        如果未找到，则返回 None。
        """
        self.cursor.execute('SELECT original_name FROM name_mapping WHERE encoded_name = ?', (encoded_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def decode_name_fusion2free(self, encoded_name):
        """
        通过编码名称查找原始名称。
        如果未找到，则返回 None。
        """
        self.cursor.execute('SELECT  encoded_name FROM name_mapping WHERE original_name = ?', (encoded_name,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def encode_names_bulk(self, original_names):
        """
        批量编码多个原始名称。
        返回一个字典 {原始名称: 编码名称}。
        """
        encoded_mapping = {}
        for name in original_names:
            encoded = self.encode_name(name)
            encoded_mapping[name] = encoded
        return encoded_mapping

    def decode_names_bulk_free2fusion(self, encoded_names):
        """
        批量解码多个编码名称。
        返回一个字典 {编码名称: 原始名称}。
        未找到的编码名称将不包含在结果中。
        """
        placeholders = ','.join('?' for _ in encoded_names)
        query = f'SELECT encoded_name, original_name FROM name_mapping WHERE encoded_name IN ({placeholders})'
        self.cursor.execute(query, encoded_names)
        results = self.cursor.fetchall()
        decoded_mapping = {encoded: original for encoded, original in results}
        return decoded_mapping

    def decode_names_bulk_fusion2free(self, encoded_names):
        """
        批量解码多个编码名称。
        返回一个字典 {编码名称: 原始名称}。
        未找到的编码名称将不包含在结果中。
        """
        placeholders = ','.join('?' for _ in encoded_names)
        query = f'SELECT encoded_name, original_name FROM name_mapping WHERE encoded_name IN ({placeholders})'
        self.cursor.execute(query, encoded_names)
        results = self.cursor.fetchall()
        decoded_mapping = {encoded: original for encoded, original in results}
        return decoded_mapping

    def export_mapping(self, export_path):
        """
        将映射导出为 CSV 文件。
        """
        import csv
        self.cursor.execute('SELECT original_name, encoded_name FROM name_mapping')
        rows = self.cursor.fetchall()
        with open(export_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Original Name', 'Encoded Name'])
            writer.writerows(rows)

    def import_mapping(self, import_path, direction):
        """
        从 CSV 文件导入映射。
        """
        import csv
        with open(import_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                original = row['Original Name']
                encoded = row['Encoded Name']
                try:
                    if direction == 'fusion2free':
                        self.cursor.execute('INSERT INTO name_mapping (original_name, encoded_name) VALUES (?, ?)',
                                            (original, encoded))
                    elif direction == 'free2fusion':
                        self.cursor.execute('INSERT INTO name_mapping (original_name, encoded_name) VALUES (?, ?)',
                                            (encoded, original))
                except sqlite3.IntegrityError:
                    # 如果已经存在，则跳过或更新
                    pass
        self.connection.commit()

    def close(self):
        """关闭数据库连接。"""
        self.connection.close()


# 示例使用
if __name__ == "__main__":
    # encoder = FreeCADNameEncoder()
    # original_names = [
    #     "零件A",
    #     "组件_B",
    #     "装配-1",
    #     "复杂名称@2024",
    #     "零件A",  # 重复名称测试
    #     "特殊字符!@#",
    #     "长名称" * 10  # 测试长名称
    # ]
    #
    # # 批量编码
    # encoded = encoder.encode_names_bulk(original_names)
    # for original, code in encoded.items():
    #     print(f"原名: {original} -> 编码名: {code}")
    #
    # # 逆向查找
    # test_encoded_names = [encoded_names for encoded_names in encoded.values()]
    # decoded = encoder.decode_names_bulk(test_encoded_names)
    # for encoded_name, original in decoded.items():
    #     print(f"编码名: {encoded_name} -> 原名: {original}")
    #
    # # 导出映射到 CSV
    # encoder.export_mapping('name_mapping_export.csv')
    # print("映射已导出到 'name_mapping_export.csv'")
    #
    # # 关闭数据库连接
    # encoder.close()
    encoder = FreeCADNameEncoder()

    fusion_prefix_path = '../data/cad_json/'
    json_list = []
    for root, dirs, files in os.walk(fusion_prefix_path):
        for file in files:
            if file.endswith('.json'):
                json_list.append(os.path.join(root, file))
    outer_type_list = {}
    op_str_dict = {}
    operation_type_list = {}
    for json_file in json_list:
        print(json_file)
        fusion_path = os.path.join(json_file)
        fusion_json = load_fusion(fusion_path)
        op_sequence = fusion_json['sequence']
        ops_entities = fusion_json['entities']
        op_name_list = [op_entry['entity'] for op_entry in op_sequence]
        encoded = encoder.encode_names_bulk(op_name_list)
        for op_entry in op_sequence:
            if op_entry['type'] == 'Sketch':
                profiles_dict = ops_entities[op_entry['entity']]['profiles']
                profile_name_list = [key for key, val in profiles_dict.items()]
                encoded = encoder.encode_names_bulk(profile_name_list)
    encoder.export_mapping('name_mapping_export.csv')
    print("映射已导出到 'name_mapping_export.csv'")

    # 关闭数据库连接
    encoder.close()

import base64
import json
from pathlib import Path
from openpyxl import load_workbook

from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

folder_path = Path('/Users/qsmy/Downloads/xingzheng')
# files = sorted(folder_path.glob('*.json'), key=lambda x: str(x.stem))

content_path = '/Users/qsmy/Downloads/xingzheng_content.xlsx'
workbook = load_workbook(content_path)

# 获取工作表
write_sheet = workbook.worksheets[0]  # 通过索引获取
# 写入表头
write_sheet.append(['s1', 's2', 's3', 's5', 's6', 's7', 's8', 's9',
                    's10', 's11', 's17', 's22', 's23', 's25', 's26',
                    's27', 's28', 's31', 's32', 's41', 's43', 's45',
                    's47', 's51', 'viewCount', 'wenshuAy'])

for file_path in folder_path.glob('*.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
        # 密钥（必须是 16 或 24 字节）
        if 'secretKey' in data and data["secretKey"] is not None:
            print(file_path)
            key = data["secretKey"].encode("utf-8")

            # 固定偏移量（IV，必须是 8 字节）
            # iv = b"20241231"  # 如果不足 8 字节，可以填充或截断
            iv = b"20250108"  # 如果不足 8 字节，可以填充或截断

            encrypted_base64 = data["result"]

            # 解密
            encrypted_data = base64.b64decode(encrypted_base64)
            cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv)
            decrypted_data = cipher_decrypt.decrypt(encrypted_data)
            plaintext = unpad(decrypted_data, DES3.block_size).decode("utf-8")
            json_object = json.loads(plaintext)
            if 's1' in json_object:
                # 构建数据行
                data_content = [
                    json_object.get('s1', ''), json_object.get('s2', ''), json_object.get('s3', ''),
                    json_object.get('s5', ''), json_object.get('s6', ''), json_object.get('s7', ''),
                    json_object.get('s8', ''), json_object.get('s9', ''), json_object.get('s10', ''),
                    json_object.get('s11', ''), json_object.get('s17', ''), json_object.get('s22', ''),
                    json_object.get('s23', ''), json_object.get('s25', ''), json_object.get('s26', ''),
                    json_object.get('s27', ''), json_object.get('s28', ''), json_object.get('s31', ''),
                    json_object.get('s32', ''), json_object.get('s41', ''), json_object.get('s43', ''),
                    json_object.get('s45', ''), json_object.get('s47', ''), json_object.get('s51', ''),
                    json_object.get('viewCount', ''), json_object.get('wenshuAy', '')
                ]

                if not all(not item for item in data_content):
                    # 将所有值转换为字符串
                    data_content = [str(item) for item in data_content]

                    # 写入数据
                    write_sheet.append(data_content)

# 保存文件
workbook.save(content_path)
print(f"File saved to {content_path}")
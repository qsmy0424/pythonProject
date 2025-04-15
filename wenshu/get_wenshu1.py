import base64
import json
import pandas as pd
from pathlib import Path

from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad


df = pd.DataFrame(columns=['44', '1', '2', '26', '7', 'rowkey', '9', '31', '10', '32', '43'])

folder_path = Path('/Users/qsmy/Downloads/Response_Body_01-02-2025-11-02-28.folder')
files = sorted(folder_path.glob('*.json'), key=lambda x: str(x.stem))

for file_path in files:
    with open(file_path, 'r') as file:
        data = json.load(file)
        # 密钥（必须是 16 或 24 字节）
        if 'secretKey' in data and data["secretKey"] is not None:
            print(file_path)
            key = data["secretKey"].encode("utf-8")

            # 固定偏移量（IV，必须是 8 字节）
            # iv = b"20241231"  # 如果不足 8 字节，可以填充或截断
            iv = b"20250102"  # 如果不足 8 字节，可以填充或截断

            encrypted_base64 = data["result"]

            # 解密
            encrypted_data = base64.b64decode(encrypted_base64)
            cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv)
            decrypted_data = cipher_decrypt.decrypt(encrypted_data)
            plaintext = unpad(decrypted_data, DES3.block_size).decode("utf-8")
            json_object = json.loads(plaintext)

            # print("Decrypted:", json_object)

            print(json_object["queryResult"]["resultList"])
            rows = []
            for item in json_object["queryResult"]["resultList"]:
                rows.append([
                    item["44"],
                    item["1"],
                    item["2"],
                    item["26"],
                    item["7"],
                    item["rowkey"],
                    item["9"],
                    item["31"],
                    item["10"],
                    item["32"],
                    item["43"]
                ])
            df = pd.concat([df, pd.DataFrame(rows, columns=df.columns)], ignore_index=True)
df.to_excel("/Users/qsmy/Downloads/result_xingzheng.xlsx", index=False)
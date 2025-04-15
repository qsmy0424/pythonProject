import mysql.connector
import base64
import json
import zlib
from pathlib import Path

from pymongo import MongoClient

from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

# 连接到 MySQL 数据库
db = mysql.connector.connect(
    host="192.168.4.214",  # 数据库主机
    user="root",  # 用户名
    port=13306,
    password="top123",  # 密码
    database="crawler_doc",  # 数据库名称
)

client = MongoClient(
    "mongodb://myusername:mypassword@192.168.4.215:27017", authSource="admin"
)

mongo_db = client["test"]

# 创建游标对象
cursor = db.cursor()


def insert_list_data(entity, doc_type):

    for item in entity["queryResult"]["resultList"]:
        # 计算 CRC32 校验和
        fields = ["1", "2", "26", "7", "31"]
        combined = "".join(str(item.get(field, "")) for field in fields).encode("utf-8")
        crc32_value = zlib.crc32(combined)
        cursor.execute("SELECT id FROM t_list where crc = %s", (crc32_value,))
        if len(cursor.fetchall()) == 0:
            mongo_db["doc_list"].insert_many(entity["queryResult"]["resultList"])
            data_tuple = (
                doc_type,
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
                item["43"],
                crc32_value,
            )
            cursor.execute(
                "INSERT INTO t_list(`type`, `44`, `1`, `2`, `26`, `7`, `rowkey`, `9`, `31`, `10`, `32`, `43`, `crc`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                data_tuple,
            )


def insert_content_data(item, doc_type):
    if "s1" in item:
        fields = ["s1", "s2", "s7", "s22", "s23", "s26", "s27", "s28", "s31"]
        combined = "".join(str(item.get(field, "")) for field in fields).encode("utf-8")
        crc32_value = zlib.crc32(combined)

        cursor.execute("SELECT id FROM t_content where crc = %s", (crc32_value,))
        exists_data = cursor.fetchall()
        if len(exists_data) == 0:
            item["crc"] = crc32_value
            mongo_db["doc"].insert_one(item)
            data_tuple = (
                doc_type,
                item["s1"],
                item["s2"],
                item["s3"],
                item["s5"],
                item["s6"],
                item["s7"],
                item["s8"],
                item["s9"],
                str(item.get("s10", "")),
                item["s31"],
                item["s41"],
                item["s43"],
                str(item.get("s22", "")),
                str(item.get("s23", "")),
                str(item.get("s25", "")),
                str(item.get("s26", "")),
                str(item.get("s27", "")),
                str(item.get("s28", "")),
                str(item["s17"]),
                str(item["s45"]),
                str(item["s11"]),
                str(item["relWenshu"]),
                str(item["qwContent"]),
                str(item["directory"]),
                str(item["globalNet"]),
                str(item["s47"]),
                str(item["viewCount"]),
                str(item["wenshuAy"]),
                item["crc"],
            )
            cursor.execute(
                "INSERT INTO t_content(type, `s1`,`s2`,`s3`,`s5`,`s6`,`s7`,`s8`,`s9`,`s10`,`s31`,`s41`,`s43`,`s22`,`s23`,`s25`,`s26`,`s27`,`s28`,`s17`,`s45`,`s11`,`relWenshu`,`qwContent`,`directory`,`globalNet`,`s47`,`viewCount`,`wenshuAy`, `crc`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                data_tuple,
            )
        else:
            print("数据已存在")


def close():
    # 提交更改到数据库
    db.commit()

    # 关闭游标和数据库连接
    cursor.close()
    db.close()


if __name__ == "__main__":
    # 固定偏移量（IV，必须是 8 字节）
    iv = b"20250411"  # 如果不足 8 字节，可以填充或截断
    type_value = 3
    folder_path = Path("C:\\Users\\qsmy\\Documents\\response_list")
    # for file_path in folder_path.glob("*rest.json"):
    for file_path in folder_path.glob("*.json"):
        print(file_path)
        print(file_path)
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            # 密钥（必须是 16 或 24 字节）
            if "secretKey" in data and data["secretKey"] is not None:
                key = data["secretKey"].encode("utf-8")

                encrypted_data = base64.b64decode(data["result"])
                cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv)
                decrypted_data = cipher_decrypt.decrypt(encrypted_data)
                plaintext = unpad(decrypted_data, DES3.block_size).decode("utf-8")
                json_object = json.loads(plaintext)
                # print(json_object)
                insert_list_data(json_object, type_value)
                # insert_content_data(json_object, type_value)
    close()

# 插入数据示例
# cursor.execute("INSERT INTO t_list (`44`, `1`) VALUES (%s, %s)", ("John Doe", "john@example.com"))

# cursor.execute(
#     "delete from t_list where id in (select id from (select MAX(id) from t_list t group by t.`1`,t.`26` having count(1) > 1) t_list1)")

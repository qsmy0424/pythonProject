from pymongo import MongoClient
from datetime import datetime
from urllib.parse import quote_plus
import logging

# logging.basicConfig(level=logging.DEBUG)

# client = MongoClient(
#     host="192.168.4.215", port=27017, username="myusername", password="mypassword"
# )

try:
    # 包含密码和数据库名的连接字符串
    client = MongoClient(
        "mongodb://myusername:mypassword@192.168.4.215:27017", authSource="admin"
    )

    # mongodb://myusername@192.168.4.215:27017/?authSource=admin

    # 测试插入操作
    db = client["test"]
    # collection = db["documents"]
    # collection.insert_one({"test": "PyMongo 连接成功！"})
    # db = client.admin.command("ping")  # 简单测试
    # print("Connected to Replica Set:", db["ok"])

    # document = {"name": "Alice", "age": 30}
    # db["documents"].insert_one(document)

    collection = db["documents"]
    cursor = db.documents.find({"name": "Alice"})
    for document in cursor:
        print(document)

    cursor = collection.find({"age": {"$gt": 25}}, {"name": 1, "_id": 0})
    for document in cursor:
        print(document)

    cursor = collection.find({"age": {"$gt": 25}}, {"_id": 1})
    for document in cursor:
        print(document)

except Exception as e:
    print(f"失败：{str(e)}")

import mysql.connector
import base64
import json
import zlib
from pathlib import Path

from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

# 连接到 MySQL 数据库
db = mysql.connector.connect(
    host="192.168.4.214",  # 数据库主机
    user="root",  # 用户名
    port=13306,
    password="top123",  # 密码
    database="crawler_doc"  # 数据库名称
)

# 创建游标对象
cursor = db.cursor()

cursor.execute("SELECT id,`1`,`2`,`26`,`7`,`31` FROM t_list")

result = cursor.fetchall()
for row in result:
    crc32_value = zlib.crc32(f"{row[1]}{row[2]}{row[3]}{row[4]}{row[5]}".encode('utf-8'))
    cursor.execute("UPDATE t_list SET crc = %s WHERE id = %s", (crc32_value, row[0]))


# 提交更改到数据库
db.commit()

# 关闭游标和数据库连接
cursor.close()
db.close()

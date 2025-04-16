import uvicorn
import base64
import json

from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

import do_mysql

app = FastAPI()

# 获取当前日期，并格式化为 YYYYMMDD
# 例如 "20250411"（如果今天是2025年4月11日）
current_date = datetime.now().strftime("%Y%m%d")

# 转换为 bytes 类型
iv = current_date.encode("utf-8")


@app.post("/items")
async def create_item(item_data: dict):
    # print("Received item:", item_data)
    if "secretKey" in item_data and item_data["secretKey"] is not None:
        key = item_data["secretKey"].encode("utf-8")
        encrypted_data = base64.b64decode(item_data["result"])
        cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv)
        decrypted_data = cipher_decrypt.decrypt(encrypted_data)
        plaintext = unpad(decrypted_data, DES3.block_size).decode("utf-8")
        json_object = json.loads(plaintext)
        # print(json_object)
        if "list" == item_data["type"]:
            do_mysql.insert_list_data(json_object, 3)
        if "doc" == item_data["type"]:
            do_mysql.insert_content_data(json_object, 3)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    print("Server started at http://0.0.0.0:8000")
    do_mysql.close()

import uuid
import os
import shutil

pld_path = '/Users/wwhm/Downloads/05/政和11'
new_path = '/Users/wwhm/Downloads/mark'
for item in os.listdir(pld_path):
    print(os.path.join(pld_path, item))
    shutil.move(os.path.join(pld_path, item), os.path.join(new_path, uuid.uuid4().hex.upper() + os.path.splitext(item)[1]))

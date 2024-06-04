import pandas as pd
import os

import openpyxl as vb

# print输出数据没有省略号
pd.set_option('display.width', None)
frames = []
# excel_writer = pd.ExcelWriter("表2.xlsx")
data = pd.read_excel(r'/Users/wwhm/Downloads/work/123.xlsx', '日志')

# for arr in df.values:
# print(arr[0])

# file_names = os.listdir(path)
# for name in file_names:
#     print(name)
#     df = pd.read_excel(os.path.join(path, name))
#     print(df)
#     frames.append(df)
# merge = pd.concat(frames, axis=0)
# merge.to_excel("result.xlsx")

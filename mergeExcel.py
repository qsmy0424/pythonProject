import pandas as pd
import os

path = "/Users/wwhm/Downloads/work/excel"
# print输出数据没有省略号
pd.set_option('display.width', None)
frames = []
file_names = os.listdir(path)
for name in file_names:
    df = pd.read_excel(os.path.join(path, name))
    frames.append(df)
merge = pd.concat(frames, axis=0)
merge.to_excel("result.xlsx")

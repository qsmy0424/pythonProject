import pandas as pd

df = pd.read_parquet("/Users/qsmy/Documents/models/chinese-law-and-regulations/data/train-00000-of-00001-8329bce6db03c820.parquet")
print(df.head())
# print(df.values)
# df.applymap(lambda x: print(f"Element: {x}"))

# 使用双重循环输出每个元素
# for row in df.index:
#     for col in df.columns:
#         print(f"Element at row {row}, column {col}: {df.loc[row, col]}")


# for index, row in df.iterrows():
#     print(f"Row {index}: {row.values}")

# 使用 values 属性逐行输出每一行元素
for row in df.values:
    print(f"Row: {row}")
from docx import Document
import pandas as pd

# 读取 Word 文档
doc_path = "C:\\Users\\qsmy\\Desktop\\文书评分(1).docx"  # 替换为你的 Word 文件路径
doc = Document(doc_path)

# 准备存储数据的列表
all_data = []

# 遍历文档中的所有表格
for table_idx, table in enumerate(doc.tables):
    # 提取表格数据
    data = []
    for row in table.rows:
        # row_data = [cell.text.strip() for cell in row.cells]
        row_data = []
        for cell in row.cells:
            text = cell.text.strip()
            if "落款" in text:
                text = "落款"
            row_data.append(text)

        data.append(row_data)

    # 转置表格（行变列，列变行）
    transposed_data = list(map(list, zip(*data)))  # 使用 zip 实现转置

    # 将转置后的数据按上下排列
    for col_idx, col in enumerate(transposed_data):
        all_data.append([f"Table {table_idx + 1}, Col {col_idx + 1}"] + col)

# 将数据转换为 Pandas DataFrame
df = pd.DataFrame(all_data)

# 将数据保存到 Excel 文件
excel_path = (
    "C:\\Users\\qsmy\\Desktop\\output22.xlsx"  # 替换为你想保存的 Excel 文件路径
)
df.to_excel(excel_path, index=False, header=False)

print(f"数据已成功保存到 {excel_path}")

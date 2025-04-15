import pandas as pd
import json

df = pd.read_excel('/Users/qsmy/Downloads/work/2022客观题.xlsx', sheet_name='Sheet2')

# data_list = [{"input": row.values[5], "output": row.values[8]} for _, row in df.iterrows()]

chat_list = []

txt_list = []

for _, row in df.iterrows():
    input_value = row.values[5]
    output_value = row.values[8]

    # 判断 output_value 是否为空，构建不同的字典
    if pd.isna(output_value) or output_value == "":
        txt_list.append({"text": input_value})
    else:
        chat_list.append({"input": input_value, "output": output_value})

# 转换为 JSON 格式
chat_json_data = json.dumps(chat_list, ensure_ascii=False, indent=4)
txt_json_data = json.dumps(txt_list, ensure_ascii=False, indent=4)

with open('/Users/qsmy/Downloads/work/chat_output.json', 'w', encoding='utf-8') as f:
    f.write(chat_json_data)

with open('/Users/qsmy/Downloads/work/txt_output.json', 'w', encoding='utf-8') as f:
    f.write(txt_json_data)

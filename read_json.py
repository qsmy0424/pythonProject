from pathlib import Path
import json
import pandas as pd


def get_before_first_newline(s):
    return s.split('\n', 1)[0]


df = pd.DataFrame(columns=['id', 'parentId', 'title', 'position', 'content'])

top_level_data = [
    [1080, 0, "宪法", 0, ""],
    [1217, 0, "司法制度和法律职业道德", 1, ""],
    [1357, 0, "刑法", 2, ""],
    [1436, 0, "刑事诉讼法", 3, ""],
    [1621, 0, "行政法与行政诉讼法", 4, ""],
    [1805, 0, "民法", 5, ""],
    [1926, 0, "商法", 6, ""],
    [2051, 0, "民事诉讼法", 7, ""]
]
df = pd.DataFrame(top_level_data, columns=df.columns)

folder_path = Path('/Users/qsmy/Downloads/law')
files = sorted(folder_path.glob('*.json'), key=lambda x: int(x.stem))

for file_path in files:
    parent_id = int(file_path.stem)
    with open(file_path, 'r') as file:
        data = json.load(file)
        rows = []

        for item in data["data"]:
            if item["position"] == 0:
                second_title = get_before_first_newline(item["content"])
                rows.append([item["parentId"], parent_id, second_title, 0, ""])

            rows.append([
                item["id"],
                item["parentId"],
                item["title"],
                item["position"],
                item["content"]
            ])

        df = pd.concat([df, pd.DataFrame(rows, columns=df.columns)], ignore_index=True)

df.to_excel("/Users/qsmy/Downloads/result.xlsx", index=False)

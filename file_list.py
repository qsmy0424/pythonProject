from pathlib import Path

write_file = "C:\\Users\\qsmy\\Desktop\\123.txt"

folder_path = Path('D:\\workspace\\IdeaProjects\\pvsp')

num = 0
for file_path in folder_path.rglob('*.java'):
    with open(file_path, 'r', encoding='utf-8') as file:
        with open(write_file, 'a', encoding='utf-8') as file1:
            for line in file.readlines():
                if (not line.startswith("import")) and line.find("//") == -1 and len(line) > 1:
                    num = num + 1
                    file1.write(str(num) + "    " + line)
                    if num > 4000:
                        exit()
    
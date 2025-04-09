import os
import shutil

count_dict = dict()
file_ext_dict = dict()

new_path = '/Users/wwhm/Downloads/mark'
unmark_path = '/Users/wwhm/Downloads/unmark'
for item in os.listdir(new_path):
    name = os.path.splitext(item)[0]
    file_ext_dict[name] = os.path.splitext(item)[1]
    if name in count_dict:
        count_dict[name] += 1
    else:
        count_dict[name] = 1

for key, value in count_dict.items():
    if value == 1:
        shutil.move(os.path.join(new_path, key + file_ext_dict[key]), os.path.join(unmark_path, key + file_ext_dict[key]))



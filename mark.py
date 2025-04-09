import os
import shutil

nameList = []

path = '/Users/wwhm/Downloads/断杆'
for item in os.listdir('/Users/wwhm/Downloads/断杆'):
    nameList.append(os.path.splitext(item)[0])

path1 = '/Users/wwhm/Downloads/倒斜杆'
for item in os.listdir(path1):
    if os.path.splitext(item)[1] == '.xml':
        if os.path.splitext(item)[0] in nameList:
            print(os.path.join(path1, item))
            shutil.move(os.path.join(path1, item), os.path.join(path, item))


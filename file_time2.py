import os
import time

import pywintypes
from win32con import FILE_FLAG_BACKUP_SEMANTICS
from win32con import FILE_SHARE_WRITE
from win32file import CloseHandle
from win32file import CreateFile
from win32file import GENERIC_WRITE
from win32file import OPEN_EXISTING
from win32file import SetFileTime


def modify_file_create_time(path, create_time_str, update_time_str, access_time_str):
    """定义文件或文件夹的创建、修改、访问时间"""
    path = os.path.abspath(path)
    if os.path.exists(path):
        try:
            format_str = "%Y-%m-%d %H:%M:%S"  # 时间格式
            file_handle = CreateFile(path, GENERIC_WRITE, FILE_SHARE_WRITE, None, OPEN_EXISTING,FILE_FLAG_BACKUP_SEMANTICS, 0)
            create_time= update_time= access_time = None
            if create_time_str :
                create_time = pywintypes.Time(time.mktime(time.strptime(create_time_str, format_str)))
            if update_time_str :
                update_time = pywintypes.Time(time.mktime(time.strptime(update_time_str, format_str)))
            if access_time_str :
                access_time = pywintypes.Time(time.mktime(time.strptime(access_time_str, format_str)))
            # 修改文件的创建时间
            SetFileTime(file_handle, create_time, update_time, access_time)
            # 关闭文件句柄
            CloseHandle(file_handle)
            print('成功:({})/({})/({})'.format(create_time_str, update_time_str, access_time_str))
        except Exception as e:
            print('失败:{}'.format(e))
    else:
        print('路径不存在:{}'.format(path))


if __name__ == '__main__':
    cTime = "2021-06-24 11:34:26"  # 创建时间
    mTime = "2023-10-01 12:12:00"  # 修改时间
    aTime = "2023-10-01 12:13:00"  # 访问时间
    #folder = r"d:/backup/db"  # 可以是文件也可以是文件夹
    file = r"d:/2021年二季度导入(1).xls"  # 可以是文件也可以是文件夹
    #modify_file_create_time(folder, cTime, mTime, aTime)
    modify_file_create_time(file, cTime, None, None)
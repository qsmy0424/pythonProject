import datetime
import os
import win32file
import win32api
import win32con

file_handle = os.open("D:\\aa.7z", os.O_RDWR | win32con.FILE_SHARE_WRITE)

file_info = win32file.GetFileTime(file_handle)

# os.close(file_handle)

new_create_time = (file_info[0], file_info[1])

print(file_info)

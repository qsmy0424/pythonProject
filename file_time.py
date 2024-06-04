import datetime
import os
import time


def change_file_creation_time(file_path, new_time):
    timestamp = time.mktime(new_time.timetuple())
    os.utime(file_path, (timestamp, timestamp))


if __name__ == '__main__':
    new_time = datetime.datetime(2023, 6, 1, 12, 0)
    change_file_creation_time("D:\\aa.7z", new_time)

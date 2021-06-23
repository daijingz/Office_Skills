# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import os
import time
from shutil import copy


path = 'Week1'


# Print all files' names (Those files have size > 1MB)
# os.path.getsize(os.path.join(filepath, file)) in unit "bytes"
for filepath, folders, files in os.walk(path):
    for file in files:
        size = (os.path.getsize(os.path.join(filepath, file))) / 1024 / 1024
        if size > 1.0:
            print(file)

# Print all files' names (Those files have been modified before given time) (With Given time)
for filepath, folders, files in os.walk(path):
    for file in files:
        # Extract file modifying time
        create_time = os.path.getmtime(os.path.join(filepath, file))
        # Extract file creating time
        create_time_new = os.path.getctime(os.path.join(filepath, file))

        # Formalizes time
        real_time = time.localtime(create_time)
        dt = time.strftime("%Y-%m-%d %H:%M", real_time)

        target_time = "2020-09-08 10:30"
        time_array = time.strptime(target_time, "%Y-%m-%d %H:%M")
        my_target_time = float(time.mktime(time_array))

        if my_target_time > create_time:
            print(file)
            print(dt)
            # Optional: If before then copy it to new folders.
            copy(os.path.join(filepath, file), os.path.join(r'Week2', file))
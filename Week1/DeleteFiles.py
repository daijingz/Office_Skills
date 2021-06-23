# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import os


path = 'Week1'


# Print all files' names (Those files have size > 1MB)
# os.path.getsize(os.path.join(filepath, file)) in unit "bytes"
for filepath, folders, files in os.walk(path):
    for file in files:
        size = (os.path.getsize(os.path.join(filepath, file))) / 1024 / 1024
        if size > 1.0:
            os.remove(os.path.join(filepath, file))
# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import os
from shutil import copy


# i.e. when folder A has folder B and folder C, and you are in folder B, we use 'C' as the path.
# (To check everything in the folder C)
# Same thing works on target copying addresses.
path = 'Week2'

# Scan through all files and copy all DOCX and PPT files to new directory
for filepath, folders, files in os.walk(path):
    for file in files:
        if '.docx' in file:
            print(os.path.join(filepath, file))
            copy(os.path.join(filepath, file), os.path.join(r'Week1', file))
        elif '.ppt' in file:
            print(os.path.join(filepath, file))
            copy(os.path.join(filepath, file), os.path.join(r'Week1', file))

# Scan through all files and copy all DOCX and PPT files to new directory (sub-directories)
for filepath, folders, files in os.walk(path):
    for file in files:
        if '.docx' in file:
            print(os.path.join(filepath, file))
            copy(os.path.join(filepath, file), os.path.join(r'Week1\DOCX', file))
        elif '.ppt' in file:
            print(os.path.join(filepath, file))
            copy(os.path.join(filepath, file), os.path.join(r'Week1\PPT', file))

# Checks whether there is a folder with given name, if not create a folder and put files inside
# Or directly put files inside
for filepath, folders, files in os.walk(path):
    for file in files:
        if '.docx' in file:
            print(os.path.join(filepath, file))
            copy(os.path.join(filepath, file), os.path.join(r'Week1\DOCX', file))
        elif '.ppt' in file:
            print(os.path.join(filepath, file))
            copy(os.path.join(filepath, file), os.path.join(r'Week1\PPT', file))
        elif '.txt' in file:
            if os.path.exists(r'Week1\TXT'):
                print('Target repository exists')
                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'Week1\TXT', file))
            else:
                print('Target repository does not exist')
                os.mkdir(r'Week1\TXT')
                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'Week1\TXT', file))
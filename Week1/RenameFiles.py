# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
from os import walk, mkdir, rename, path
import os


# File path in the same directory
opath = 'Week2'
for filepath, folders, files in walk(opath):
    counter = 0
    for file in files:
        print(filepath)
        type_name = filepath.split('//')[:-1]
        renamed = type_name + str(counter) + '.jpg'
        rename(os.path.join(filepath, file), renamed)
        counter += 1
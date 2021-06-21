# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import os


# Assume on the same layer we want to visit
# i.e. when folder A has folder B and folder C, and you are in folder B, we use 'C' as the path.
# (To check everything in the folder C)
path = 'Documentation'

# Show all files' paths with files' names
for filepath, folders, files in os.walk(path):
    print(filepath, files)

# Show filepath, sub-folders and containing files
for filepath, folders, files in os.walk(path):
    print(filepath, folders, files)

# Show all files' names
for filepath, folders, files in os.walk(path):
    print(files)

# Print all files in the target folder independently
for filepath, folders, files in os.walk(path):
    for file in files:
        print(file)

# Print all files in the target folder independently (with file paths)
for filepath, folders, files in os.walk(path):
    for file in files:
        print(os.path.join(filepath, file))

# Print all upper-most files and folders in the target repository
for i in os.listdir(path):
    print(i)

# Print all upper-most files and folders (with '.txt' in the name) in the target repository
for i in os.listdir(path):
    if '.txt' in i:
        print(i)
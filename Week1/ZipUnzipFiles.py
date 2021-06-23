# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import zipfile
import os


# Extract all files and zip them into a zipped folder (abc.zip)
# At the same time records all names to a txt file line by line
def zipF():
    z = zipfile.ZipFile('abc.zip', 'w')
    for file in os.listdir('Week1'):
        z.write(os.path.join('Week1', file))
        with open('', 'a',  encoding='gbk') as w:
            w.write(file+'\n')
    z.close()


# Unzip a zipped package (all files to Week2 folder)
def unzipF():
    f = zipfile.ZipFile('abc.zip', 'r')
    for file in f.namelist():
        f.extract(file, 'Week2')
    f.close()
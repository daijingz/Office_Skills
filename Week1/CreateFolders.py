# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
from os import walk, mkdir
from shutil import copy, move
from openpyxl import load_workbook


# Load excel
# this file does not exist in this folder (so there might have errors)
wb = load_workbook('Week1.xlsx')
# Use data in Sheet1
ws = wb['Sheet1']

# Print folder name and make a folder in specified location
for x in ws.rows:
    print(x[0].value, x[1].value)
    mkdir('week1/' + x[0].value)

# Read from second line (ignore the head of file)
# Print folder name and make a folder in specified location
ws2 = [x for x in ws.rows]
for x in ws2[1:]:
    print(x[0].value, x[1].value)
    mkdir('week1/' + x[0].value)
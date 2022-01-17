
from os import sep
import pandas as pd
import xlsxwriter
import sys
import csv
from re import search

import csv

arrCheck = []
with open('check.csv') as f:
    reader = csv.reader(f)
    arrCheck = list(reader)
print(len(arrCheck))

df1 = pd.read_csv('main_trim.csv', sep = ',')    
# df2 = pd.read_csv('check.csv', )

arrCity = df1['City']
# arrCheck = df2['values']
arrCode = df1['Code']



workbook = xlsxwriter.Workbook('Final.xlsx')
 
# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()
row = 0
column = 0
 
# Use the worksheet object to write
# data via the write() method.
for x in range(len(arrCity)):
    # print(arrCity[x]+","+arrCode[x])
       for y in range(len(arrCheck)):
            # print(arrCheck[y][0])
            if arrCity[x] in arrCheck[y][0]:
             print(arrCheck[y][0]+","+arrCode[x])
             worksheet.write(row,column, arrCheck[y][0])
             worksheet.write(row,column+1, arrCode[x].strip())
             row +=1             
             
# Finally, close the Excel file
# via the close() method.
workbook.close()

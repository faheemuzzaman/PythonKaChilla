
import pandas as pd
import xlsxwriter
import sys
import csv
from re import search



df1 = pd.read_csv('main.csv', sep=',')    
df2 = pd.read_csv('check.csv', sep=',')

arrCity = df1['City']
arrCheck = df2['values']
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
            if arrCity[x].strip() in arrCheck[y].strip():
             print(arrCheck[y].strip()+","+arrCode[x].strip())
             worksheet.write(row,column, arrCheck[y].strip())
             worksheet.write(row,column+1, arrCode[x].strip())
             row +=1
             break
             
# Finally, close the Excel file
# via the close() method.
workbook.close()

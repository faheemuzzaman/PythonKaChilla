
import pandas as pd
import sys
import csv
from re import search



df1 = pd.read_csv('main.csv', sep=',')    
df2 = pd.read_csv('check.csv', sep=',')

arrCity = df1['City']
arrCheck = df2['values']
arrCode = df1['Code']

f=open('final.csv','w+')


for x in range(len(arrCity)):
    # print(arrCity[x])
    for y in range(len(arrCheck)):
        # if arrCity[x] in arrCheck[y]:
        if arrCity[x].find(arrCheck[y]) != -1:
        # print(x,y)
        # if search(arrCode[x],arrCheck[y]):
            f.write(arrCode[x]+","+arrCity[y]+"\n")
f.close()
# df1.sort_values(sys.argv[3])
# df2.sort_values(sys.argv[3])
#df1.drop(df1.columns[list(map(int, sys.argv[4].split()))], axis = 1, inplace = True)
#df2.drop(df2.columns[list(map(int, sys.argv[4].split()))], axis = 1, inplace = True)

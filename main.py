from openpyxl import load_workbook
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import tkinter as tk
import math


#read spreadsheets and workbook
wb = load_workbook('Upper_Air_temps_data.xlsx')
tropoArr = []
stratoArr = []
troposphere = wb["Sheet1"]
stratosphere = wb["Sheet2"]

#array for tropospheric data
for col in troposphere.iter_rows(min_row=2, max_col=7, max_row=519, values_only=True):
    tropoArr.append(col)

#array for stratospheric data
for col in stratosphere.iter_rows(min_row=2, max_col=7, max_row=519, values_only=True):
    stratoArr.append(col)

#modified binary search method for openpyxl
def findInterval(arr, startMonth, startYear, endMonth, endYear, l=0):
    returns = []
    r=len(arr)
    while r-l > 1:
        middle = (l+(r-l))//2
        if arr[middle][0] == startYear:
            if startMonth == l:
                returns.append(middle)
            elif startMonth != l:
                diff = startMonth - arr[middle][1]
                returns.append(middle + diff)
            monthdiff = endMonth - startMonth
            yeardiff = endYear - startYear
            endIndex = returns[0] + (12*yeardiff + monthdiff)
            returns.append(endIndex)
            return returns

        elif arr[middle][0] > startYear:
            findInterval(arr, startMonth, startYear, endMonth, endYear, r, middle)
        elif arr[middle][0] < startYear:
            findInterval(arr,startMonth,startYear,endMonth,endYear,middle,l)
        else:
            print('one or more entries in specified range do not exist in the data')
            return None
            
# method for graphing data
def graphShit(arr, startMonth, startYear, endMonth, endYear, hemi):
    fig, ax = plt.subplots()

    ax.plot(xvalues, yvalues)
    plt.show()
    print(xvalues)
    print(yvalues)
graphShit(tropoArr, 1, 2000, 3, 2000, 2)

# fig, ax = plt.subplots()
# #logic test run
# xsummer = []
# ysummer = []
# xwinter = []
# ywinter = []
# xspring = []
# yspring = []
# xfall = []
# yfall = []
#
# for entry in tropoArr:
#     if entry[1] == (12 or 1 or 2):
#         ywinter.append(entry[2])
#         xwinter.append(entry[0])
#     elif entry[1] == (3 or 4 or 5):
#         yspring.append(entry[2])
#         xspring.append(entry[0])
#     elif entry[1] == (6 or 7 or 8):
#         ysummer.append(entry[2])
#         xsummer.append(entry[0])
#     elif entry[1] == (9 or 10 or 11):
#         yfall.append(entry[2])
#         xfall.append(entry[0])
#
# ax.plot(xsummer, ysummer, color = 'red')
# ax.plot(xwinter, ywinter, color = 'blue')
# ax.plot(xspring, yspring, color = 'cyan')
# ax.plot(xfall, yfall, color = 'orange')
# ax.set(xlabel = "year",
#        ylabel = 'temp anomaly')
# plt.show()

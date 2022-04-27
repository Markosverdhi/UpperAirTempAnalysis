
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
def findInterval(arr, startMonth, startYear, endMonth, endYear, r=None, l=0):
    returns = []
    if r == None:
        r=len(arr)
    while len(returns)==0:
        middle = l+(r-l)//2
        if arr[middle][0] == startYear:
            if startMonth == l:
                returns.append(middle + 2)
            elif startMonth != l:
                diff = startMonth - arr[middle][1]
                returns.append(middle + diff + 2)
            monthdiff = endMonth - startMonth
            yeardiff = endYear - startYear
            endIndex = returns[0] + (12*yeardiff + monthdiff)
            returns.append(endIndex)
            return returns

        elif arr[middle][0] > startYear:
            return findInterval(arr, startMonth, startYear, endMonth, endYear, middle, l)
        elif arr[middle][0] < startYear:
            return findInterval(arr, startMonth, startYear, endMonth, endYear, r, middle)
        else:
            print('one or more entries in specified range do not exist in the data')
            return None

# method for graphing data
def graph(arr, startMonth, startYear, endMonth, endYear):
    #searches for start and end index
    i = findInterval(arr, startMonth, startYear, endMonth, endYear)
    fig, ax = plt.subplots()
    xsummer = []
    ysummer = []
    xwinter = []
    ywinter = []
    xspring = []
    yspring = []
    xfall = []
    yfall = []

    for entry in arr[i[0]:i[1]]:
        if entry[1] == (12 or 1 or 2):
            ywinter.append(entry[2])
            xwinter.append(entry[0])
        elif entry[1] == (3 or 4 or 5):
            yspring.append(entry[2])
            xspring.append(entry[0])
        elif entry[1] == (6 or 7 or 8):
            ysummer.append(entry[2])
            xsummer.append(entry[0])
        elif entry[1] == (9 or 10 or 11):
            yfall.append(entry[2])
            xfall.append(entry[0])

    ax.plot(xsummer, ysummer, color = 'red')
    ax.plot(xwinter, ywinter, color = 'blue')
    ax.plot(xspring, yspring, color = 'cyan')
    ax.plot(xfall, yfall, color = 'orange')
    ax.set(xlabel = "year",
           ylabel = 'temp anomaly')
    plt.show()


graph(tropoArr, 1, 1988, 4, 1989)

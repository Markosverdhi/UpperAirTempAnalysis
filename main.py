
from openpyxl import load_workbook
import numpy as np
from matplotlib import pyplot as plt, dates as mdates
import pandas as pd
import tkinter as tk
import statistics as s


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
def graphBySeason(arr, startMonth, startYear, endMonth, endYear, hemi):
    #searches for start and end index
    i = findInterval(arr, startMonth, startYear, endMonth, endYear)
    #create the space for the plots
    fig, ax = plt.subplots(2,2)
    fig.set_figwidth(9)
    fig.set_figheight(9)


    #creating cleaned lists for plotting
    xsummer = []
    ysummer = []
    xwinter = []
    ywinter = []
    xspring = []
    yspring = []
    xfall = []
    yfall = []
    for entry in range(i[0],i[1]):
        if arr[entry][1] in {12, 1, 2}:
            ywinter.append(arr[entry][hemi])
            xwinter.append(mdates.datestr2num(f'{arr[entry][1]}/{arr[entry][0]}'))
        elif arr[entry][1] in {3, 4, 5}:
            yspring.append(arr[entry][hemi])
            xspring.append(mdates.datestr2num(f'{arr[entry][1]}/{arr[entry][0]}'))
        elif arr[entry][1] in {6,7,8}:
            ysummer.append(arr[entry][hemi])
            xsummer.append(mdates.datestr2num(f'{arr[entry][1]}/{arr[entry][0]}'))
        elif arr[entry][1] in {9, 10, 11}:
            yfall.append(arr[entry][hemi])
            xfall.append(mdates.datestr2num(f'{arr[entry][1]}/{arr[entry][0]}'))

    #creating plots
    ax[0][0].scatter(xwinter, ywinter, color = 'lightskyblue')
    ax[0][0].set_title('Winter')
    ax[0][1].scatter(xspring, yspring, color = 'palegreen')
    ax[0][1].set_title('Spring')
    ax[1][0].scatter(xsummer, ysummer, color = 'gold')
    ax[1][0].set_title('Summer')
    ax[1][1].scatter(xfall, yfall, color = 'chocolate')
    ax[1][1].set_title('Fall')

    for i in range(2):
        for j in range(2):
            ax[i][j].set(ylabel = 'temp anomaly')
            #YYYY/m formatting
            ax[i][j].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
            #set ticks for xaxis
            ax[i][j].xaxis.set_major_locator(mdates.MonthLocator(1,7))
            ax[i][j].xaxis.set_minor_locator(mdates.MonthLocator())
        #rotation of labels
            for label in ax[i][j].get_xticklabels(which = 'major'):
                label.set(rotation=45, horizontalalignment='right')

    plt.show()
    # print(yfall)
    # print(xfall)

def fiveNumberSum(arr, startMonth, startYear, endMonth, endYear, hemi):
    i = findInterval(arr, startMonth, startYear, endMonth, endYear)
    cData = []
    for entry in range(i[0],i[1]):
        cData.append(arr[entry][hemi])

    minimum = min(cData)
    maximum = max(cData)
    returns = [minimum, maximum]
    for i in range(3) : returns.insert(-1,float(format(s.quantiles(cData, n=4)[i-1], '.3f')))
    return returns

    # print(returns)


def boxPlot(arr, startMonth, startYear, endMonth, endYear, hemi):
    fns = fiveNumberSum(arr, startMonth, startYear, endMonth, endYear, hemi)
    box = plt.figure()
    ax = box.add_axes([0,0,1,1])
    p = ax.boxplot(fns)
    plt.show()


graphBySeason(tropoArr,1,1980,6,1990,2)

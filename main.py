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

# method for graphing data
def graphShit(arr, startMonth, startYear, endMonth, endYear):
    fig, ax = plt.subplots()
    if endYear - startYear <= 2:
        ax.plot(xsummer, ysummer, color = 'red')
        # ax.plot(xwinter, ywinter, color = 'blue')
        # ax.plot(xspring, yspring, color = 'cyan')
        # ax.plot(xfall, yfall, color = 'orange')
        # ax.set(xlabel = "year",
        #        ylabel = 'temp anomaly')
        # plt.show()

fig, ax = plt.subplots()
#logic test run
xsummer = []
ysummer = []
xwinter = []
ywinter = []
xspring = []
yspring = []
xfall = []
yfall = []

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

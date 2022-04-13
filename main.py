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

#method for graphing data
def graphShit(sheet, startMonth, startYear, endMonth, endYear):
    if int(endYear) - int(startYear) > 2:
        yValues = []
        for year in range(startYear,endYear):
            if sheet[0] == startYear:
                averages = []
                for iteration in sheet[0]:



#logic test run
xValues = []
yValues = []
for entry in tropoArr:
    xValues.append(entry[0])

for entry in tropoArr:
    yValues.append(entry[2])

plt.scatter(xValues, yValues)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:50:44 2015

@author: claireyun
"""

import LoadDataYear

def getDataMap(latRange, lonRange, year, var):
    dataMap = []
    for i in latRange:
        row = []
        for j in lonRange:
            x= LoadDataYear.loadDataYear(year, var, i, j)
            row.append(x)
        dataMap.append(row)
    return dataMap
    
def getAreaAvg(data):     #avg temp for each day averaged over x, y coordinates
    dailySum = []
    for i in range(len(data[0][0])):
        dailySum.append(0)
        for j in range(len(data)):
            for r in range(len(data[0])):
                dailySum[i] += data[j][r][i]
        dailySum[i] /= (len(data)*len(data[0]))
    return dailySum
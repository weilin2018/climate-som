# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:50:44 2015

@author: claireyun
"""

import LoadDataYear
import LatLonIndex

def getDataMap(latRange, lonRange, year, var):
    latLonRange = LatLonIndex.findLatLonRange(latRange, lonRange, [])
    dataMap = []
    lat=[]
    lon=[]
    for i in latLonRange[0]:
        row = []
        latrow=[]
        lonrow=[]
        for j in latLonRange[1]:
            x= LoadDataYear.loadDataYear(year, var, i, j)
            latrow.append(x[0])
            lonrow.append(x[1])
            row.append(x[2])
        dataMap.append(row)
        lat.append(latrow)
        lon.append(lonrow)
    return [lat,lon,dataMap]
    
def getAreaAvg(data):     #avg temp for each day averaged over x, y coordinates
    dailySum = []
    for i in range(len(data[0][0])):
        dailySum.append(0)
        for j in range(len(data)):
            for r in range(len(data[0])):
                dailySum[i] += data[j][r][i]
        dailySum[i] /= (len(data)*len(data[0]))
    return dailySum
    
def getTimeAvg(data):
    timeSum = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[0])):
            row.append(sum(data[i][j])/len(data[i][j]))
        timeSum.append(row)
    return timeSum
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:50:51 2015

@author: claireyun
"""

import GetDataMap
import FindExtremes

def AreaAvgOverTime(var, model, timeRange, latRange, lonRange):
    avgOverTime = []
    lat = []
    lon = []
    
    for i in range(timeRange[0],timeRange[1]):
        print i
        g = GetDataMap.getDataMap(latRange, lonRange, i, model, var)
        if len(lat) == 0:
            lat = g[0]
            lon = g[1]

        TimeAverage = GetDataMap.getTimeAvg(g[2])
        if(len(avgOverTime) == 0):
            for j in range(0,len(TimeAverage)):
                row = []
                for c in range(0,len(TimeAverage[0])):
                    row.append(TimeAverage[j][c])
                avgOverTime.append(row)
        else:
            for j in range(0,len(TimeAverage)):
                for c in range(0,len(TimeAverage[0])):
                    avgOverTime[j][c] += TimeAverage[j][c]
    
    for i in range(0, len(avgOverTime)):
        for j in range(0, len(avgOverTime[i])):
            avgOverTime[i][j] /= len(range(timeRange[0],timeRange[1]))
    
    return [lat, lon, avgOverTime]
    
def AreaExtremeAvgOverTime(var, model, timeRange, latRange, lonRange):
    extAvgOverTime = []
    lat = []
    lon = []
    
    for i in range(timeRange[0], timeRange[1]):
        print i
        g = GetDataMap.getDataMap(latRange, lonRange, i, model, var)
        if len(lat) == 0:
            lat = g[0]
            lon = g[1]

        annualExt = FindExtremes.findAnnualMax(g[2])
        if(len(extAvgOverTime) == 0):
            for j in range(0,len(annualExt)):
                row = []
                for c in range(0,len(annualExt[0])):
                    row.append(annualExt[j][c])
                extAvgOverTime.append(row)
        else:
            for j in range(0,len(annualExt)):
                for c in range(0,len(annualExt[0])):
                    extAvgOverTime[j][c] += annualExt[j][c]
    
    for i in range(0, len(extAvgOverTime)):
        for j in range(0, len(extAvgOverTime[i])):
            extAvgOverTime[i][j] /= len(range(timeRange[0], timeRange[1]))
    
    return [lat, lon, extAvgOverTime]
    
def AreaAvgDifference(areaTime1, areaTime2):
    avgOverTime = []
    for i in range(0,len(areaTime1[2])):
        row = []
        for j in range(0,len(areaTime1[2][0])):
            row.append(areaTime2[2][i][j]- areaTime1[2][i][j])
        avgOverTime.append(row)
    return avgOverTime
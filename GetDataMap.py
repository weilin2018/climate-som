# -*- coding: utf-8 -*-
"""
"""

import LoadDataYear
import LatLonIndex
import scipy.io

def getDataMap(latRange, lonRange, year, model, var):
    # load test data file
    testdata = scipy.io.loadmat(str('data/' + model + '/' + var + '/' + var + '_' + str(year) + '_01' + '_01'))
    testdata = testdata[str(var + '_' + str(year) + '_01' + '_01')][0]
    latLonRange = LatLonIndex.findLatLonRange(latRange, lonRange, testdata)
    
    
    dataMap = []
    lat=[]
    lon=[]
    for i in latLonRange[0]:
        row = []
        latrow=[]
        lonrow=[]
        for j in latLonRange[1]:
            x = LoadDataYear.loadDataYear(year, model, var, latindex = i, lonindex = j)
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
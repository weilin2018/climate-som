# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:25:36 2015

@author: student
"""

import scipy.io
import LoadDataYear
import matplotlib.pyplot as plt
import LatLonIndex
import GetDataMap
import SOM_WeightedAverage

SOM_WeightedAverage.GetWeightedAvg


#data = scipy.io.loadmat("tasmax_2005_01_01.mat")
##print data["tasmax_2005_01_01"][0][2][45,0,10]
#
#
##find function that finds range of latitude and longitude indexes
#LatLongCoord = LatLonIndex.findLatLonRange([35,50],[225,240],[])
#print LatLongCoord
#
#DataMap = GetDataMap.getDataMap(LatLongCoord[0], LatLongCoord[1], 2005, "tasmax")
##DataMapAvg = GetDataMap.getAreaAvg(DataMap)
#DataMapDay = GetDataMap.getDataMapDay(DataMap,2)
#print len(DataMapDay)
#print len(DataMapDay[0])
#
##plt.plot(DataMapAvg)
#weighted_average = SOM_WeightedAverage.GetWeightedAvg(DataMapDay,2)
#print len(weighted_average)
#print len(weighted_average[0])
#
#print DataMapDay[0][0],DataMapDay[0][1],DataMapDay[0][2]
#print weighted_average[0][0], weighted_average[0][1], weighted_average[0][2]
#
#latIndex = LatLonIndex.findLatIndex(42,[])
#lonIndex = LatLonIndex.findLongIndex(230,[])
#print latIndex
#print lonIndex
#data = LoadDataYear.loadDataYear(2004, "tasmax", latIndex[0], lonIndex[1])
##print data
##plt.plot(data)
#plt.hist(data, range(280,300,1), normed=True)
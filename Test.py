# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:25:36 2015

@author: student
"""

import scipy.io
import LoadDataYear
import matplotlib.pyplot as plt
import LatLonIndex

#data = scipy.io.loadmat("tasmax_2005_01_01.mat")
#print data["tasmax_2005_01_01"][0][2][45,0,10]
latIndex = LatLonIndex.findLatIndex(42,[])
lonIndex = LatLonIndex.findLongIndex(230,[])
print latIndex
data = LoadDataYear.loadDataYear(2005, "tasmax", latIndex[0], lonIndex[1])
#print data
#plt.plot(data)
plt.hist(data, range(280,300,1), normed=True)


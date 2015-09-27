# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:31:27 2015

@author: student
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy.io

DJF = range(335,359)+range(0,60)
MAM = range(60,151)
JJA = range(152,243)
SON = range(244,334)
season = SON

data = scipy.io.loadmat('wb_downscale.mat')

tempDataLat = data["lat"]
tempDataLon = data["lon"]
tempDataData = data["data"]

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)


sumData = 0
seasonalMean = []
for j in range(0,10):
    row = []
    for k in range(0,10):
        sumData = 0
        for l in range(0,18):
            for i in season:
                sumData = sumData + flatTData[l,j,k,i]
        avgData = sumData / (len(season)*18)
        row.append(avgData)
    seasonalMean.append(row)
print np.size(seasonalMean)

flatTData = np.array(seasonalMean)

#built in function of numpy -- eliminates all extra dimensions

m = Basemap(width=10000000/5,height=7000000/5,
            resolution='l',projection='stere',
            lat_ts = 40, lat_0=40, lon_0 = -70)
#center of the map

lon, lat = np.meshgrid(flatTLon[0,:], flatTLat[:,0])
x, y = m(lon,lat)
cs = m.pcolor(x,y,np.squeeze(flatTData), vmin=-10, vmax=30)

# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")

# Add Title
plt.title('Mean Temperature in 2000-2004 Relative to 1990-1995')

plt.show()
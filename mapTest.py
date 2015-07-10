# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 09:35:54 2015

@author: ethan
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import LatLonIndex
import GetDataMap

tempData = scipy.io.loadmat('tasmax_2005_01_01.mat')
tempData = tempData['tasmax_2005_01_01'][0]

upLat = 40
lowLat = 15
lftLon = 70
rgtLon = 100

latLonRange = LatLonIndex.findLatLonRange([lowLat, upLat], [lftLon, rgtLon], [])

latRange = latLonRange[0]
lonRange = latLonRange[1]

tempDataLat = tempData[0]
tempDataLon = tempData[1]
tempDataData = tempData[2]

flatTLat = []
flatTLon = []
flatTData = []

for x in range(len(latRange)):
    latRow = []
    lonRow = []
    dataRow = []
    for y in range(len(lonRange)):
        latRow.append(tempDataLat[latRange[x],lonRange[y]])
        lonRow.append(tempDataLon[latRange[x],lonRange[y]])
        dataRow.append(tempDataData[latRange[x],lonRange[y],0])
    flatTLat.append(latRow)
    flatTLon.append(lonRow)
    flatTData.append(dataRow)

flatTLat = np.array(flatTLat)
flatTLon = np.array(flatTLon)
flatTData = np.array(flatTData)

m = Basemap(width=5000000,height=3500000,
            resolution='l',projection='stere',\
            lat_ts=40,lat_0=(upLat+lowLat)/2.0,lon_0=(lftLon+rgtLon)/2.0)

lon, lat = np.meshgrid(flatTLon[0,:], flatTLat[:,0])
x, y = m(lon,lat)
cs = m.pcolor(x,y,np.squeeze(flatTData), vmin=min(min(x) for x in flatTData), vmax=max(max(x) for x in flatTData))

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
plt.title('DJF Maximum Temperature')
plt.savefig('test.png')
plt.show()







#
#x, y = m(flatTLon*180./np.pi, flatTLat*180./np.pi)
##cs = map.pcolor(x,y,flatTData,cmap='coolwarm', vmin=min(min(x) for x in flatTData), vmax=max(max(x) for x in flatTData))
##plt.axis([x.min(), x.max(), y.min(), y.max()])
##plt.colorbar()
#
#
## draw coastlines, country boundaries, fill continents.
#m.drawcoastlines()
#m.drawstates()
#m.drawcountries()
#
#plt.title('global temperature data')
#plt.show()
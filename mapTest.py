from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import scipy
import AreaAvgOverTime
import GetDataMap

tempData = scipy.io.loadmat('tasmax_2004_01_01.mat')
tempData = tempData['tasmax_2004_01_01'][0]

latRange = [25,35]
lonRange = [80,90]
avgOverTime1990 = AreaAvgOverTime.AreaAvgOverTime([1990,1993], latRange,lonRange)
avgOverTime2000 = AreaAvgOverTime.AreaAvgOverTime([2000,2005], latRange,lonRange)
avgOverTime = AreaAvgOverTime.AreaAvgDifference(avgOverTime1990, avgOverTime2000)

tempDataLat = avgOverTime1990[0]
tempDataLon = avgOverTime1990[1]
tempDataData = avgOverTime

flatTLat = np.array(tempDataLat)
flatTLon = np.array(tempDataLon)
flatTData = np.array(tempDataData)
print flatTData
print flatTLat
print flatTLon

m = Basemap(width=10000000/5,height=7000000/5,
            resolution='l',projection='stere',
            lat_ts = 40, lat_0=sum(latRange)/2, lon_0 = sum(lonRange)/2)

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
plt.title('Mean Temperature in 2000-2004 Relative to 1990-1995')

plt.show()


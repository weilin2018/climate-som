from mvpa2.suite import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
<<<<<<< HEAD
import scipy.io
=======
>>>>>>> 324c86f7757a1959ecd6dc4e2fb603633aab0283
import numpy
import random
import LoadDataYear

latRange = [36,46]
lonRange = [280,290]
baseYearRange = [1990, 2000]
futureYearRange = [2041, 2042]

# training
somTrainingData = []

# observations
wetBulbData = []

latGrid = []
lonGrid = []

print 'loading data'
for year in range(baseYearRange[0], baseYearRange[1]):
    print year

    for x in range(latRange[0], latRange[1]):
        latRow = []
        lonRow = []
        for y in range(lonRange[0], lonRange[1]):
            hussData = LoadDataYear.loadDataYear(year, 'ncep', 'shum', reallat = x, reallon = y)
            tasmaxData = LoadDataYear.loadDataYear(year, 'ncep', 'tmax', reallat = x, reallon = y)
            wbData = LoadDataYear.loadDataYear(year, 'ncep', 'wb', reallat = x, reallon = y)

            latRow.append(tasmaxData[0])
            lonRow.append(tasmaxData[1])

            for r in range(len(hussData[2])):
                element = []
                element.append(hussData[2][r])
                element.append(tasmaxData[2][r])
                wetBulbData.append(wbData[2][r])
                somTrainingData.append(element)
        if year == baseYearRange[0]:
            latGrid.append(latRow)
            lonGrid.append(lonRow)

somTrainingData = np.array(somTrainingData)

print 'initializing SOM mapper'
<<<<<<< HEAD
som = SimpleSOMMapper((3, 3), 100, learning_rate = 1e-5)
=======
som = SimpleSOMMapper((3, 3), 150, learning_rate = 1e-5)
>>>>>>> 324c86f7757a1959ecd6dc4e2fb603633aab0283

print 'training SOM'
som.train(somTrainingData)

mapped = som(somTrainingData)

print 'creating wet-bulb distribution'
mappedDist = {}
for i in range(0, len(mapped)):
    (x, y) = mapped[i]
    if (x, y) in mappedDist:
        mappedDist[(x, y)].append(wetBulbData[i])
    else:
        mappedDist[(x, y)] = [wetBulbData[i]]

nodeMeans = {}

plt.figure()
plt.hold(True)
keysList = mappedDist.keys()
for k in range(len(keysList)):
    nBins = 20
    wbHist = np.histogram(mappedDist[keysList[k]], nBins)
    nodeMeans[keysList[k]] = np.mean(mappedDist[keysList[k]])

    x = wbHist[1]
    y = wbHist[0]

    minLength = min(len(x), len(y))
    plt.plot(x[0:minLength], y[0:minLength])

plt.xlabel('wet bulb temperature (degrees C)')
plt.ylabel('occurances')
plt.savefig('som-nodes.png')
#plt.show()

nodeAssignments = []
futureWbDownscaling = []

print 'assigning nodes'
for year in range(futureYearRange[0], futureYearRange[1]):
    nodeRows = []
    for x in range(latRange[0], latRange[1]):
        nodeCols = []
        for y in range(lonRange[0], lonRange[1]):
            hussData = LoadDataYear.loadDataYear(year, 'gfdl-cm3', 'huss', reallat = x, reallon = y)
            tasmaxData = LoadDataYear.loadDataYear(year, 'gfdl-cm3', 'tasmax', reallat = x, reallon = y)

            nodeTime = []

            # find closest node
            for r in range(len(hussData[2])):
                hVal = hussData[2][r]
                tVal = tasmaxData[2][r]

                minIndex = -1
                minDist = -1

                for k1 in range(0, len(som.K)):
                    for k2 in range(0, len(som.K[k1])):
                        nodeH = som.K[k1][k2][0]
                        nodeT = som.K[k1][k2][1]

                        dist = math.sqrt((nodeH-hVal)**2 + (nodeT-tVal)**2)
                        if minIndex == -1 or dist < minDist:
                            minDist = dist
                            minIndex = (k1, k2)

                nodeTime.append(minIndex)
            nodeCols.append(nodeTime)
        nodeRows.append(nodeCols)
    nodeAssignments.append(nodeRows)

for year in range(0, len(nodeAssignments)):
    xData = []
    for x in range(0, len(nodeAssignments[year])):
        yData = []
        for y in range(0, len(nodeAssignments[year][x])):
            yearData = []
            for day in range(0, len(nodeAssignments[year][x][y])):
                key = nodeAssignments[year][x][y][day]
                dist = mappedDist[key]
                yearData.append(dist[random.randint(0, len(dist)-1)])
            yData.append(yearData)
        xData.append(yData)
    futureWbDownscaling.append(xData)

futureWbDownscaling = np.array(futureWbDownscaling)

d = {"wb_downscale":futureWbDownscaling}
scipy.io.savemat('wb_downscale.mat', mdict=d, appendmat=False, format='7')

for d in range(0, 360, 50):
    flatTLat = np.array(latGrid)
    flatTLon = np.array(lonGrid)
    flatTData = np.array(np.squeeze(futureWbDownscaling[0,:,:,d]))

    m = Basemap(width=10000000/5,height=7000000/5,
                resolution='l',projection='stere',
                lat_ts = 40, lat_0=sum(latRange)/2, lon_0 = sum(lonRange)/2)

    lon, lat = np.meshgrid(flatTLon[0,:], flatTLat[:,0])
    x, y = m(lon,lat)
    cs = m.pcolor(x,y,np.squeeze(flatTData), vmin=-5, vmax=25)

    # Add Grid Lines
    m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
    m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

<<<<<<< HEAD
    # Add Coastlines, States, and Country Boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # Add Colorbar
    cbar = m.colorbar(cs, location='bottom', pad = "10%")

    # Add Title
    plt.title('WB projections')
    plt.savefig('wb-projection-' + str(d) + '.png')
    #plt.show()
=======
>>>>>>> 324c86f7757a1959ecd6dc4e2fb603633aab0283

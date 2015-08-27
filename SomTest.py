from mvpa2.suite import *
import matplotlib.pyplot as plt
import random
import LoadDataYear

latRange = [38,42]
lonRange = [284,288]
baseYearRange = [2000, 2001]
futureYearRange = [2041, 2042]

# training
somTrainingData = []

# observations
wetBulbData = []

print 'loading data'
for year in range(baseYearRange[0], baseYearRange[1]):
    print year

    for x in range(latRange[0], latRange[1]):
        for y in range(lonRange[0], lonRange[1]):
            hussData = LoadDataYear.loadDataYear(year, 'ncep', 'shum', reallat = x, reallon = y)
            tasmaxData = LoadDataYear.loadDataYear(year, 'ncep', 'tmax', reallat = x, reallon = y)
            wbData = LoadDataYear.loadDataYear(year, 'ncep', 'wb', reallat = x, reallon = y)
            
            for r in range(len(hussData[2])):
                element = []
                element.append(hussData[2][r])
                element.append(tasmaxData[2][r])
                wetBulbData.append(wbData[2][r])
                somTrainingData.append(element)

somTrainingData = np.array(somTrainingData)

print 'initializing SOM mapper'
som = SimpleSOMMapper((5, 5), 100, learning_rate = 1e-5)

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
    for x in range(0, len(nodeAssignments[year])):
        xData = []
        for y in range(0, len(nodeAssignments[year][x])):
            yData = []
            for day in range(0, len(nodeAssignments[year][x][y])):
                dayData = []
                key = nodeAssignments[year][x][y][day]
                dist = mappedDist[key]
                dayData.append(dist[random.randint(0, len(dist)-1)])
            yData.append(dayData)
        xData.append(yData)
    futureWbDownscaling.append(xData)

futureWbDownscaling = np.array(futureWbDownscaling)
print futureWbDownscaling[0,0:2,0:2,0:10]



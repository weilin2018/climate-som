# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:11:24 2015

@author: claireyun
"""
import scipy.io
import LatLonIndex
#import matplotlib.pyplot as plt

def loadDataYear(year, model, var , latindex = -1, lonindex = -1, reallat = -1, reallon = -1):     
    data1d = []
    lat=[]
    lon=[]
    
    baseDir = 'data/' + model + '/' + var + '/'
    
    for i in range(1,13):
        t = ""
        if i < 10:
            t = var + '_' + str(year) + '_0' + str(i) + '_01'
        else:
            t = var + '_' + str(year) + '_' + str(i) + '_01'
        data = scipy.io.loadmat(baseDir + t + '.mat')
        data = data[t][0]
        
        if latindex == -1 and lonindex == -1 and (reallat != -1 and reallon != -1):
            latindex = LatLonIndex.findLatIndex(reallat, data)
            latindex = latindex[0]
            lonindex = LatLonIndex.findLonIndex(reallon, data)
            lonindex = lonindex[1]
            print lonindex
        
        if len(lat)==0:
            lat=data[0]
            lon=data[1]
            
        #for lat in range(0, len(tasmax[0])):
            #for lon in range (0, len(tasmax[1][0,:])):'

        for d in range(0, len(data[2][latindex,lonindex])):
            data1d.append(data[2][latindex,lonindex,d])
    #print temp    
    #print len(temp)
    return [lat[latindex,lonindex],lon[latindex,lonindex],data1d]
    
#t= loadDataYear(2005, 'tasmax', 45 , 0)

#plt.plot(t, "g")


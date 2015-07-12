# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:11:24 2015

@author: claireyun
"""
import scipy.io
#import matplotlib.pyplot as plt

def loadDataYear(year , var , latindex, lonindex):     
    temp = []
    lat=[]
    lon=[]
    
    for i in range(1,13):
        t = ""
        if i < 10:
            t = var + '_' + str(year) + '_0' + str(i) + '_01'
        else:
            t = var + '_' + str(year) + '_' + str(i) + '_01'
        tasmax= scipy.io.loadmat(t + '.mat')
        tasmax = tasmax[t][0]
        if len(lat)==0:
            lat=tasmax[0]
            lon=tasmax[1]
            
        #for lat in range(0, len(tasmax[0])):
            #for lon in range (0, len(tasmax[1][0,:])):'

        for d in range(0, len(tasmax[2][latindex,lonindex])):
            temp.append(tasmax[2][latindex,lonindex,d])
    #print temp    
    #print len(temp)
    return [lat[latindex,lonindex],lon[latindex,lonindex],temp]
    
#t= loadDataYear(2005, 'tasmax', 45 , 0)

#plt.plot(t, "g")


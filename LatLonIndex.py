# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy.io
import sys # (if you want to call something specific) from sys import maxint

temp = []

def findLatIndex(x,data):
    diff1 = sys.maxint
    diff2 = 0
    closesti = sys.maxint
    closestj = sys.maxint
    
    i = sys.maxint
    j = sys.maxint

    if len(data) == 0:
        data = scipy.io.loadmat('tasmax_2005_01_01.mat')   
        data = data['tasmax_2005_01_01'][0]
    
    for i in range(0,len(data[0])):
        for j in range(0, len(data[0][i,:])):
            diff2 = abs(x-data[0][i,j])
            if diff2 < diff1:
               # print diff1, diff2
               # print i, j
                diff1 = diff2
                closesti = i
                closestj = j
    return (closesti, closestj)
    
def findLongIndex(x,data):
    diff1 = sys.maxint
    diff2 = 0
    closesti = sys.maxint
    closestj = sys.maxint
    
    i = sys.maxint
    j = sys.maxint
    
    if len(data) == 0:
        data = scipy.io.loadmat('tasmax_2005_01_01.mat') 
        data = data['tasmax_2005_01_01'][0]

    for i in range(0,len(data[1])):
        for j in range(0, len(data[1][i,:])):
            diff2 = abs(x-data[1][i,j])
            if diff2 < diff1:
                diff1 = diff2
                closesti = i
                closestj = j
    return (closesti, closestj)
    
def findHighestTemp(data):
    high = sys.maxint
    x = []
    
    for i in range(0,len(data[2])):
        currentRow = []
        for j in range(0, len(data[2][i,:])):
            high = sys.maxint
            for s in range(0, len(data[2][i,j,:])):
                if data[2][i,j,s] > high or high == sys.maxint:
                    high = data[2][i,j,s]
            currentRow.append(high)
        x.append(currentRow)
    return x

#y = findHighestTemp(tasmax["tasmax_2005_01_01"][0])
#print y[65][142]
#print findLatIndex(42,tasmax["tasmax_2005_01_01"][0])
#print findLongIndex(286,tasmax["tasmax_2005_01_01"][0])
#print tasmax["tasmax_2005_01_01"][0][2][10,10]

#temp = tasmax["tasmax_2005_01_01"][0][2][10,10]
#plt.plot(temp,"g")
#plt.ylabel("Temperature")
#plt.xlabel("Days")
#plt.title("Daily Temperature")

#plt.show()


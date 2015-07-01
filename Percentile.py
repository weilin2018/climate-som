# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 12:58:46 2015

@author: claireyun
"""
import sys

def percentile(data, percentage):
    data.sort()
    return data[int(percentage/100.0 *len(data))]

def AnnualMax(data):
    max = sys.maxint
    for i in range(len(data)):
        if i > max or max == sys.maxint:
            max = data[i]
    
def AnnualMin(data):
    min = sys.maxint
    for j in range(len(data)):
        if j < min or min == sys.maxint:
            min = data[j]
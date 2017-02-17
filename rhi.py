# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:56:26 2017

@author: amagaldi
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import collections
import userpaths
import plotutils
from matplotlib.pyplot import *

# Setting the file and paths
dataFolder = userpaths.getDataFolder()
fileName = userpaths.getFileNameRHI()
currFile = dataFolder+fileName

# Read data
time, LOS, AZ, EL, R, RW  = userpaths.readDataFromCSV(currFile, 'RHI')

# Changes EL to the proper range of 10 - 170
EL=np.around(EL, decimals=0)
deri=np.diff(EL, n=1)
deri=np.append(deri, -1)
ders=np.sign(deri)
pm=np.argmax(ders<0)
for ik in range(pm, len(EL)):
    EL[ik]=EL[ik]+((90-EL[ik])*2)

# Moves the range to start at 0, and divides by 100
menor=min(R)
for k in range(len(R)):
    R[k]=((R[k]-menor)/100)+1

# Initializes a 'collection' structure for the Range
counter1=collections.Counter(R)
re=(counter1.keys())

# Initializes a 'collection' structure for the Elevation
counter=collections.Counter(EL)
ele=(counter.keys())

EL=EL.astype(np.int64)
R=R.astype(np.int64)

ele = np.arange(0, 180, 1)
re = np.arange(0, max(re)+1, 1)

mre=max(re)+1
mre=mre.astype(np.int64)
z_array = np.nan * np.empty((mre,len(ele)))

elevaciones = np.arange(0, 180, 1)

# Saves the RWS for every Range and elevation 
for i in range(len(EL)):
    z_array[R[i],EL[i]]=RW[i]

z_array=np.rot90(z_array)

plotutils.plot_polar_contour(z_array, elevaciones, re, "W")

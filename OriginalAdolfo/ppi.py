# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:38:36 2017

@author: amagaldi
"""

import collections
import os
import numpy as np
import matplotlib.cm as cm
from matplotlib.pyplot import *
import  userpaths
from plotutils import *

# Setting the file and paths
dataFolder = userpaths.getDataFolder()
fileName = userpaths.getFileNamePPI()
currFile = dataFolder+fileName

# Reading data
time, LOS, AZ, EL, R, RW  = userpaths.readDataFromCSV(currFile, 'RHI')

AZ=np.around(AZ, decimals=0)

# Fixing angle for azimuth. For those < 0, set > 180
for k in range(len(AZ)):
    if AZ[k]<0:
       AZ[k]=180-(AZ[k]*-1)+180

# Normalizing R?
menor=min(R)
for k in range(len(R)):
       R[k]=((R[k]-menor)/50)+1
RW =RW
counter1=collections.Counter(R)
re=(counter1.keys())

counter=collections.Counter(AZ)
azi=(counter.keys())

AZ=AZ.astype(np.int64)
R=R.astype(np.int64)
z_array = np.nan * np.empty((len(re)+1,len(azi)+6))

azimuths = np.arange(0, 360, 1)
re.append((re[-1])+1)

for ii in range(len(re)):
    re[ii]=((re[ii]*5)/100)

for i in range(len(RW)):
    z_array[R[i],AZ[i]]=RW[i]

z_array=np.rot90(z_array)

plot_polar_contour(z_array,azimuths

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:38:36 2017

@author: amagaldi
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import collections
from matplotlib.pyplot import *


os.chdir('/home/amagaldi/Downloads/2017-01-26/radial_wind_data/01-00/')
print os.getcwd()
aa='WLS100s-90_radial_wind_data_2017-01-26_01-03-09_19_PPI_32.csv'

csv = np.genfromtxt (aa , delimiter=";")
fisrts=csv[1:,0]

LOS=csv[1:,3]
AZ=csv[1:,4]
EL=csv[1:,5]
R =csv[1:,6]
RW =csv[1:,7]

AZ=np.around(AZ, decimals=0)
for k in range(len(AZ)):
    if AZ[k]<0:
       AZ[k]=180-(AZ[k]*-1)+180

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

def plot_polar_contour(values, azimuths, zeniths):
    theta = np.radians(azimuths)
    zeniths = np.array(zeniths)
    plt.set_cmap('seismic_r')
    values = np.array(values)
    values = values.reshape(len(azimuths), len(zeniths))

    r, theta = np.meshgrid(zeniths, np.radians(azimuths))
    fig, ax = subplots(subplot_kw=dict(projection='polar'))
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    #autumn()
    cax = ax.contourf(theta, r, values,500)
    #autumn()
    cb = fig.colorbar(cax)
    cb.set_label("Velocidad Radial")

    return fig, ax, cax

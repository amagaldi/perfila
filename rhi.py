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
from matplotlib.pyplot import *

os.chdir('/home/amagaldi/Downloads/2017-01-26/radial_wind_data/01-00/')
print os.getcwd()
aa='WLS100s-90_radial_wind_data_2017-01-26_01-19-21_19_RHI_30.csv'


csv = np.genfromtxt (aa , delimiter=";")
fisrts=csv[1:,0]

LOS=csv[1:,3]
AZ=csv[1:,4]
EL=csv[1:,5]
R =csv[1:,6]
RW =csv[1:,7]

EL=np.around(EL, decimals=0)
deri=np.diff(EL, n=1)
deri=np.append(deri, -1)
ders=np.sign(deri)
pm=np.argmax(ders<0)
for ik in range(pm, len(EL)):
            EL[ik]=EL[ik]+((90-EL[ik])*2)


menor=min(R)
for k in range(len(R)):
       R[k]=((R[k]-menor)/100)+1


counter1=collections.Counter(R)
re=(counter1.keys())

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

for i in range(len(EL)):
    z_array[R[i],EL[i]]=RW[i]
z_array=np.rot90(z_array)


def plot_polar_contour(values, azimuths, zeniths):
    theta = np.radians(azimuths)
    zeniths = np.array(zeniths)
    plt.set_cmap('seismic_r')
    values = np.array(values)
    values = values.reshape(len(azimuths), len(zeniths))

    r, theta = np.meshgrid(zeniths, np.radians(azimuths))
    fig, ax = subplots(subplot_kw=dict(projection='polar'))
    ax.set_theta_zero_location("W")
    ax.set_theta_direction(-1)

    cax = ax.contourf(theta, r, values,500)

    cb = fig.colorbar(cax)
    cb.set_label("Velocidad Radial")

    return fig, ax, cax

plot_polar_contour(z_array, elevaciones, re)

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:49:41 2017

@author: amagaldi
"""



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import collections
from matplotlib.pyplot import *
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.dates import HourLocator
from pylab import rcParams
rcParams['figure.figsize'] = 15, 10
#import gdal
#import wradlib

altura=[]
tiempo=[]

os.chdir('/Users/amagaldi/Desktop/2017-02-25/boundary_layer_altitude_data/')
aa='/Users/amagaldi/Desktop/2017-02-25/boundary_layer_altitude_data/'
for root, dirs, files in os.walk(aa):
    for name in files:
        if name.endswith((".csv")):
             ab=root.split('/')
             abc = datetime.strptime(ab[-1], '%H-%M')
             #tiempo.append(abc.hour) 
             #tiempo.append(abc.strftime('%H:%M'))
             tiempo.append(abc)
             csv = np.genfromtxt (root+"/"+name , delimiter=";")
             RW =csv[1:,6]
             altura.append(RW)
             #print RW




ax = plt.subplot()
ax.plot(tiempo, altura)
ax.xaxis.set_major_locator(HourLocator())
ax.xaxis.set_major_formatter(DateFormatter('%H-%M'))
ax.set_xlabel('hora') 
ax.set_ylabel('altura (m.a.g.l.)')
ax.title.set_text('2017-02-25')

plt.show()




#plt.plot(tiempo,altura)
#plt.gcf().autofmt_xdate()
#ax.xaxis.set_major_formatter(myFmt)
#plt.show()

#print(counter.most_common(3))
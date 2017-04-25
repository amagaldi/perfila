#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:14:25 2017

@author: amagaldi
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import collections
from matplotlib.pyplot import *
import userpaths

dataFolder = userpaths.getDataFolder()
fileName = userpaths.getFileNameVertical()
currFile = dataFolder+fileName

csv = np.genfromtxt (currFile , delimiter=";")

AZ=csv[1:,1] 
EL=csv[1:,2] 
R=csv[1:,3]        
XW=csv[1:,4]  
YW=csv[1:,5]
ZW =csv[1:,6]
CNR =csv[1:,7]
print(CNR[0:3])

for k in range(len(AZ)):
    if AZ[k]<0:
       AZ[k]=180-(AZ[k]*-1)+180
         

counter1=collections.Counter(R)
re=(counter1.keys())
re=sorted(re)
print(re)
ak=[]
#aqui lo que graficamos es CNR, si hacemos un loop para que grafique sobre 
#XW vel x , YW vel en y y  ZW vel en z ya esta o tal vez repetir estas lineas de abajo
# 3 veces más
for kk in range(len(re)):
    aj=[]
    for k in range(len(CNR)):
        if R[k]==re[kk]:
            aj.append(CNR[k])
            ab=np.nanmean(aj)
            
    ak.append(ab)  



plt.plot(ak,re)

plt.xlabel('CNR') 
plt.ylabel('altura (m.a.g.l.)')
plt.title('2017-02-25')      
plt.show()

ak=[]
for kk in range(len(re)):
    ax=[]
    for k in range(len(XW)):
        if R[k]==re[kk]:
            ax.append(XW[k])
            abx=np.nanmean(ax)
            
    ak.append(abx)  



plt.plot(ak,re)

plt.xlabel('Velocidad X') 
plt.xlabel('Velocidad [m/s]') 
plt.ylabel('altura (m.a.g.l.)')
plt.title('2017-02-25')  

plt.show()
ak=[]
for kk in range(len(re)):
    ay=[]
    for k in range(len(YW)):
        if R[k]==re[kk]:
            ay.append(YW[k])
            aby=np.nanmean(ay)
            
    ak.append(aby)  



plt.plot(ak,re)

plt.xlabel('Velocidad Y') 
plt.xlabel('Velocidad [m/s]') 
plt.ylabel('altura (m.a.g.l.)')
plt.title('2017-02-25')         

plt.show()
ak=[]
for kk in range(len(re)):
    az=[]
    for k in range(len(ZW)):
        if R[k]==re[kk]:
            az.append(ZW[k])
            abz=np.nanmean(az)
            
    ak.append(abz)  



plt.plot(ak,re)

plt.xlabel('Velocidad Z') 
plt.xlabel('Velocidad [m/s]') 
plt.ylabel('altura (m.a.g.l.)')
plt.title('2017-02-25')  
plt.show()

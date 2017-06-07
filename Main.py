from ftplib import FTP
from pandas import DataFrame
from datetime import *
import matplotlib.pyplot as plt
import plotutils
import numpy as np
import os, sys, getopt
import re
from DataContainer import *
from PPIandRHI import radialWindData
from WindReconstruction import windReconstruction
from BoundaryLayer import boundaryLayer

host = '132.248.8.202'
port = 21
inputFolder = '/data/WIND_CUBE/' 
outputFolder = 'images'
ftp = FTP() 
ftp.connect(host,port)

# This function MUST receive a date in the format 'YYYY-MM-DD' and a Time in the format 0-24
if __name__ == "__main__":

    allArguments = sys.argv[1:]
    if len(allArguments) < 2:
        selectedDate = '2017-06-02'
        times = ['00-00','01-00']
    else:
        selectedDate = allArguments[0]
        hour = int(allArguments[1])
        times = ['%.2d-00' % hour]

    # Login into the FTP server
    print(ftp.login())

    rootFolder = inputFolder+selectedDate
    for currFolder in times:
        time = currFolder.split('/')[-1]
        #radialWindData(ftp, rootFolder, selectedDate, time, outputFolder)
        windReconstruction(ftp, rootFolder, selectedDate, time, outputFolder)

    #boundaryLayer(ftp, rootFolder,  selectedDate, outputFolder)

    ftp.quit()

from ftplib import FTP
from pandas import DataFrame
from datetime import *
import matplotlib.pyplot as plt
import plotutils
import numpy as np
import os
import re
from DataContainer import *
from PPIandRHI import radialWindData
from WindReconstruction import windReconstruction
from BoundaryLayer import boundaryLayer

host = '132.248.8.202'
port = 21
selectedDate = '2017-06-02'
inputFolder = '/data/WIND_CUBE/' 
outputFolder = 'images'
ftp = FTP() 
ftp.connect(host,port)

if __name__ == "__main__":

    # Login into the FTP server
    print(ftp.login())

    rootFolder = inputFolder+selectedDate
    times = ['00-00','01-00']
    for currFolder in times:
        time = currFolder.split('/')[-1]
        #radialWindData(ftp, rootFolder, selectedDate, time, outputFolder)
        #windReconstruction(ftp, rootFolder, selectedDate, time, outputFolder)

    boundaryLayer(ftp, rootFolder,  selectedDate, outputFolder)

    ftp.quit()

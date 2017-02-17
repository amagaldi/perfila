import numpy as np
import matplotlib.pyplot as plt
import userpaths
import plotutils
from matplotlib.pyplot import *
import matplotlib.cm as cm
import plotutils
import matplotlib.colors as colors

# Setting the file and paths
dataFolder = userpaths.getDataFolder()
fileName = userpaths.getFileNameRHI()
currFile = dataFolder+fileName

# Read data
time, LOS, AZ, EL, R, RW  = userpaths.readDataFromCSV(currFile, 'RHI')

# Changes the angle for those elevations that are 'after' 90 deg
negIncrement= np.where(np.diff(EL) < 0)
EL[negIncrement[0][0]:] = 90+ (90-EL[negIncrement[0][0]:])

plotutils.plot_polar_scatter(RW, R, EL, "W")


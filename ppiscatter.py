import numpy as np
import userpaths
import plotutils

# Setting the file and paths
dataFolder = userpaths.getDataFolder()
fileName = userpaths.getFileNamePPI()
currFile = dataFolder+fileName

# Read data
time, LOS, AZ, EL, R, RW  = userpaths.readDataFromCSV(currFile, 'PPI')

#print("RW: ", RW[0:10])
#print("AZ: ", AZ[0:10])
#print("R: ", R[0:10])

# Changes the angle for those elevations that are 'after' 90 deg
negIncrement= np.where(np.diff(EL) < 0)

plt = plotutils.plot_polar_scatter(RW, R, AZ, "W")

plt.savefig('new.png')
plt.show()

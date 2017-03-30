from ftplib import FTP
from pandas import DataFrame
import plotutils
import numpy as np
from datetime import *

host = '132.248.8.98'
usr = 'computoatm'
psw = 'H0L4C0mput04tm$.'
port = 10219

ftp = FTP()
ftp.connect(host,port)

class DataContainer:

    datastr = ''
    data = []

    def readFromFTP(self,data):
        self.datastr+=data.decode("utf-8")

    def dataToArray(self, columns):
        tempArray = np.array(self.datastr.split('\n'))

        # Remove first and last line. First line has the header and last line
        # has wrong number of items
        temp2Array = np.array([x.split(';') for x in tempArray[1:-2]])
        print(temp2Array[0:3])

        # Last column has empty string, remove it
        dataArray = np.array(temp2Array[:,0:-1])

        self.data =  DataFrame(dataArray, columns=columns)
        for idx in range(1,len(columns)):
            self.data[columns[idx]] = self.data[columns[idx]].astype(float)

        print('Size of data: ', self.data.shape)
        return self.data

    def fixForRHI(self):
        EL = self.data['Elevation']
        negIncrement= np.where(np.diff(EL) < 0)
        EL[negIncrement[0][0]:] = 90+ (90-EL[negIncrement[0][0]:])


print(ftp.login( user=usr, passwd=psw))
day = '2017-03-24'
# Folder options:  boundary_layer_altitude_data
dataType = 'radial_wind_data'
time = '16-00'
folder = day+'/'+dataType+'/'+time+'/'

files = ftp.nlst(folder)

for currfile in files:
    
    print(currfile)
    if currfile.find('PPI') != -1:

        obj = DataContainer()
        ftp.retrbinary('RETR %s' % currfile, obj.readFromFTP)
        columns = ['Timestamp','ConfiID','ScanID','LOSID','Azimuth', \
                           'Elevation','Range','RWS','DRWS','CNR']
        data = obj.dataToArray(columns)

        plt = plotutils.plot_polar_scatter(data['RWS'],  data['Range'],data['Azimuth'], "W")
        plt.show()

    if currfile.find('RHI') != -1:

        obj = DataContainer()
        ftp.retrbinary('RETR %s' % currfile, obj.readFromFTP)
        columns = ['Timestamp','ConfiID','ScanID','LOSID','Azimuth', \
                           'Elevation','Range','RWS','DRWS','CNR']
        data = obj.dataToArray(columns)
        obj.fixForRHI()

        plt = plotutils.plot_polar_scatter(data['RWS'],  data['Range'],data['Elevation'], "W")
        plt.show()


ftp.quit()

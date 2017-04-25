from ftplib import FTP
from pandas import DataFrame
from datetime import *
import matplotlib.pyplot as plt
import plotutils
import numpy as np
import os

host = '132.248.8.98'
usr = 'computoatm'
psw = 'H0L4C0mput04tm$.'
port = 10219
selectedDate = '2017-02-25'
time = '16-00'
outputFolder = 'images'

ftp = FTP()
ftp.connect(host,port)

class DataContainer:
    """ This class is used to read files driectly from the FTP and to convert
    binary data into the proper numpy array"""

    datastr = ''
    data = []

    def readFromFTP(self,data):
        """ Reads binary data as string"""
        self.datastr+=data.decode("utf-8")

    def dataToArray(self, columns):
        """ Converts the orignal data in straing format to numpy array"""
        tempArray = np.array(self.datastr.split('\n'))

        # Remove first and last line. First line has the header and last line
        # has wrong number of items
        temp2Array = np.array([x.split(';') for x in tempArray[1:-2]])
        print(temp2Array[0:3])

        # Last column has empty string, remove it
        dataArray = np.array(temp2Array[:,0:-1])

        # Create a data frame with the requested columns
        self.data =  DataFrame(dataArray, columns=columns)
        for idx in range(1,len(columns)):
            self.data[columns[idx]] = self.data[columns[idx]].astype(float)

        #print('Size of data: ', self.data.shape)
        return self.data

    def fixForRHI(self):
        """ This is the change in data we need to do for RHI scans"""
        EL = self.data['Elevation']
        negIncrement= np.where(np.diff(EL) < 0)
        EL[negIncrement[0][0]:] = 90+ (90-EL[negIncrement[0][0]:])

def radialWindData(ftp, selectedDate, time, outputFolder):
    dataType = 'radial_wind_data'
    # Folder options:  boundary_layer_altitude_data
    folder = selectedDate+'/'+dataType+'/'+time+'/'
    # Create output folder
    outputFolder = outputFolder+'/'+selectedDate
    try:
        os.mkdir(outputFolder)
    except:
        print('warning: folder'+outputFolder+' already exists')

    files = ftp.nlst(folder)
    # Make 'generic' outputfile
    outFile = outputFolder+'/'

    # Iterate over all the files in the current FTP folder
    for currfile in files:

        temp = currfile.rfind('/')+1;
        finalOutputFile = outFile+currfile[temp:].replace('csv','png')

        # Verfiy we are interested in the current file
        if currfile.find('PPI') != -1 or currfile.find('RHI') != -1 :

            # Initialize the required container
            obj = DataContainer()
            print('Working with file:' , currfile)
            ftp.retrbinary('RETR %s' % currfile, obj.readFromFTP)
            columns = ['Timestamp','ConfiID','ScanID','LOSID','Azimuth', \
                               'Elevation','Range','RWS','DRWS','CNR']
            data = obj.dataToArray(columns)

            # Verify if the file comes from a PPI scan
            if currfile.find('PPI') != -1:
                plt = plotutils.plot_polar_scatter(data['RWS'],  data['Range'],data['Azimuth'], "W")

            # Verify if the file comes from a PPI scan
            if currfile.find('RHI') != -1:
                obj.fixForRHI()
                plt = plotutils.plot_polar_scatter(data['RWS'],  data['Range'],data['Elevation'], "W")

            #plt.show()
            plt.savefig(finalOutputFile)

def windReconstruction(ftp, selectedDate, time, outputFolder):
    dataType = 'wind_reconstruction_data'
    # Folder options:  boundary_layer_altitude_data
    folder = selectedDate+'/'+dataType+'/'+time+'/'
    # Create output folder
    outputFolder = outputFolder+'/'+selectedDate
    try:
        os.mkdir(outputFolder)
    except:
        print('warning: folder'+outputFolder+' already exists')

    files = ftp.nlst(folder)
    # Make 'generic' outputfile
    outFile = outputFolder+'/'

    # Iterate over all the files in the current FTP folder
    for currfile in files:

        temp = currfile.rfind('/')+1;
        # Verify if the file comes from a DBS scan
        if currfile.find('DBS') != -1:
            obj = DataContainer()
            print('Working with file:' , currfile)
            ftp.retrbinary('RETR %s' % currfile, obj.readFromFTP)
            columns = ['Timestamp', 'Azimuth', 'Elevation','Range','Xwind','Ywind','Zwind',\
                        'CNR','ConfIdx']

            # Get the date from the file as a DataFrame
            data = obj.dataToArray(columns)
            # Make an average of all columns by grouped ranges
            dataByRange = data.groupby('Range').mean()
            # Get the grouped ranges values
            ranges = dataByRange.index.values

            # ------- Plot CNR vel ------
            finalOutputFile = outFile+'CNR_'+currfile[temp:].replace('csv','png')
            plt.plot(dataByRange['CNR'],ranges)
            plt.xlabel('CNR') 
            plt.ylabel('m')
            plt.title(selectedDate+'-'+time)      
            plt.savefig(finalOutputFile)
            plt.close()

            # ------- Plot X,Y,Z vel ------
            finalOutputFile = outFile+'Allvel_'+currfile[temp:].replace('csv','png') 
            plt.plot(dataByRange['Xwind'],ranges,label='X-Wind') 
            plt.plot(dataByRange['Ywind'],ranges,label='Y-Wind') 
            plt.plot(dataByRange['Zwind'],ranges,label='Z-Wind') 
            plt.xlabel('m/s')
            plt.ylabel('m')
            plt.legend(loc='best')
            plt.title('All winds:'+selectedDate+'-'+time)      
            plt.savefig(finalOutputFile)
            plt.close()

            # ------- Plot Wind Magnitude ------
            finalOutputFile = outFile+'Magnitude_'+currfile[temp:].replace('csv','png')
            windMagnitude = np.sqrt(np.square(dataByRange['Xwind'])+np.square(dataByRange['Ywind'])+ np.square(dataByRange['Zwind']))
            plt.plot(windMagnitude,ranges)
            plt.xlabel('m/s') 
            plt.ylabel('m')
            plt.title('Wind magnitude :'+selectedDate+'-'+time)
            plt.savefig(finalOutputFile)
            plt.close()

def boundaryLayer(ftp, selectedDate, outputFolder):
    """ Reads and plots the boundary layer during the day"""
    dataType = 'boundary_layer_altitude_data'
    # Folder options:  boundary_layer_altitude_data
    folder = selectedDate+'/'+dataType
    # Create output folder
    outputFolder = outputFolder+'/'+selectedDate
    try:
        os.mkdir(outputFolder)
    except:
        print('warning: folder'+outputFolder+' already exists')

    foldersForThisDate = ftp.nlst(folder)
    print(foldersForThisDate)
    #files = ftp.nlst(folder)
    # Make 'generic' outputfile
#    outFile = outputFolder+'/'
#
#    # Iterate over all the files in the current FTP folder
#    for currfile in files:
#
#        temp = currfile.rfind('/')+1;
#        # Verify if the file comes from a DBS scan
#        if currfile.find('DBS') != -1:
#            obj = DataContainer()
#            print('Working with file:' , currfile)
#            ftp.retrbinary('RETR %s' % currfile, obj.readFromFTP)
#            columns = ['Timestamp', 'Azimuth', 'Elevation','Range','Xwind','Ywind','Zwind',\
#                        'CNR','ConfIdx']
#
#            # Get the date from the file as a DataFrame
#            data = obj.dataToArray(columns)
#            # Make an average of all columns by grouped ranges
#            dataByRange = data.groupby('Range').mean()
#            # Get the grouped ranges values
#            ranges = dataByRange.index.values
#
#            # ------- Plot CNR vel ------
#            finalOutputFile = outFile+'CNR_'+currfile[temp:].replace('csv','png')
#            plt.plot(dataByRange['CNR'],ranges)
#            plt.xlabel('CNR') 
#            plt.ylabel('m')
#            plt.title(selectedDate+'-'+time)      
#            plt.savefig(finalOutputFile)
#            plt.close()
#

if __name__ == "__main__":

    # Login into the FTP server
    print(ftp.login( user=usr, passwd=psw))

    #radialWindData(ftp, selectedDate, time, outputFolder)
    #windReconstruction(ftp, selectedDate, time, outputFolder)
    boundaryLayer(ftp, selectedDate, outputFolder)

    ftp.quit()

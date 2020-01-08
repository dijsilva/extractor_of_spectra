import numpy as np 
import csv
import xlsxwriter
import os
from datetime import datetime
import time


class Extractor:
    def __init__(self, namOfFiles, formatOfFile):
        self.nameOfFiles = namOfFiles

        self.filesFormat = formatOfFile
        self.listOfFiles = []

    def preViewOfFiles(self):
        if (len(self.nameOfFiles) > 1):
            for file in self.nameOfFiles:
                self.listOfFiles.append(file)
        if (len(self.nameOfFiles) == 1):
            self.listOfFiles.append(self.nameOfFiles[0])
        quantityOfFiles = len(self.listOfFiles)
        
        return quantityOfFiles
    
    def extractor(self, outputFile, createLogFile, useCommaSeparator):
        initTime = time.time()
        self.outputFile = outputFile
        self.createLogFile = createLogFile
        if (self.createLogFile == True):
            self.logFile = '{}\\{}_log.txt'.format(os.path.split(outputFile)[0], os.path.split(outputFile)[1].split('.')[0])
        self.useCommaSeparator = useCommaSeparator
        dictOfModificationsDates = {}
        for item in self.listOfFiles:
            if item not in dictOfModificationsDates:
                info = os.stat(item)
                lastmodification = datetime.fromtimestamp(info.st_mtime)
                dictOfModificationsDates[item] = lastmodification
        orderedDictOfModifications = sorted(dictOfModificationsDates, key=dictOfModificationsDates.get)

        if (self.createLogFile == True):
            logOutputFile = open(self.logFile, 'w')
            logOutputFile.write('{} spectras was used for extraction.\n\n'.format(len(orderedDictOfModifications)))

        listOfSpectras = []
        wavelengthTitle = []
        readTitle = True
        if self.filesFormat == '.csv':
            try:
                for file in orderedDictOfModifications:
                    f = open(file, 'r')
                    fileCSV = csv.reader(f, delimiter=',')
                    check = False
                    for line in fileCSV:
                        if check == False:
                            if 'Wavelength (nm)' in line[0]:
                                check = True
                        else:
                            listOfSpectras.append(line[1])
                            if readTitle == True:
                                wavelengthTitle.append(line[0])
                    readTitle = False
                    f.close()
                if (self.createLogFile == True):
                    logOutputFile.write('All files was read corrected.\n\n')
            except BaseException as e:
                if (self.createLogFile == True):
                    logOutputFile.write('An error occurred and the message is:\n\n')
                    logOutputFile.write(str(e))
                    logOutputFile.close()
                raise Exception ('An error ocurred')
        
        if self.filesFormat == '.dpt':
            try:
                for file in orderedDictOfModifications:
                    f = open(file, 'r')
                    check = False
                    for line in f:
                        listOfSpectras.append(line.split(',')[1])
                        if readTitle == True:
                            wavelengthTitle.append(line.split(',')[0])
                    readTitle = False
                    f.close()
                if (self.createLogFile == True):
                    logOutputFile.write('All files was read corrected.\n\n')
            except BaseException as e:
                if (self.createLogFile == True):
                    logOutputFile.write('An error occurred and the message is:\n\n')
                    logOutputFile.write(str(e))
                    logOutputFile.close()
                raise Exception ('An error ocurred')

        wavelengthTitle.extend(listOfSpectras)
        
        if self.useCommaSeparator == True:
            wavelengthTitle = [value.replace('.', ',') for value in wavelengthTitle]
        
        if self.useCommaSeparator == False:
            wavelengthTitle = [value.replace(',', '.') for value in wavelengthTitle]

        wavelength = int(len(wavelengthTitle) / (len(orderedDictOfModifications) + 1))
        spectra = np.array(wavelengthTitle).reshape(wavelength, len(orderedDictOfModifications) + 1, order='F')


        workbook = xlsxwriter.Workbook('{}'.format(self.outputFile))
        worksheet_spectra = workbook.add_worksheet('Absorbancy')
        row = 0

        for col, data in enumerate(spectra):
            worksheet_spectra.write_column(row, col, data)
        workbook.close()

        end = time.time()

        timeOfExecution = end - initTime
        
        if (self.createLogFile == True):
            logOutputFile.write('The time of execution was {:.2f} seconds. \n\n'.format(timeOfExecution))
            logOutputFile.write('The files was read in the order: \n\n')
            for files in orderedDictOfModifications:
                logOutputFile.write('{}\n'.format(str(os.path.split(files)[1])))
            logOutputFile.close()
        return

import numpy as np 
import csv
import xlsxwriter
import os
from datetime import datetime


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
        self.outputFile = outputFile
        self.createLogFile = createLogFile
        self.useCommaSeparator = useCommaSeparator
        dictOfModificationsDates = {}
        for item in self.listOfFiles:
            if item not in dictOfModificationsDates:
                info = os.stat(item)
                lastmodification = datetime.fromtimestamp(info.st_mtime)
                dictOfModificationsDates[item] = lastmodification
        orderedDictOfModifications = sorted(dictOfModificationsDates, key=dictOfModificationsDates.get)

        listOfSpectras = []
        wavelengthTitle = []
        readTitle = True
        if self.filesFormat == '.csv':
            for file in orderedDictOfModifications:
                f = open(item, 'r')
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
        if self.filesFormat == '.dpt':
            for file in orderedDictOfModifications:
                f = open(item, 'r')
                check = False
                for line in f:
                    listOfSpectras.append(line.split(',')[1])
                    if readTitle == True:
                        wavelengthTitle.append(line.split(',')[0])
                readTitle = False
                f.close()
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
        
        return




#teste = Extractor('/home/dsilva/Downloads/leitura_de_graos_26-12-19', '.csv')
#quantity, files = teste.preViewOfFiles()
#dates = teste.extractor('teste')

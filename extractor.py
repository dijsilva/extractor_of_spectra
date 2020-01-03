import numpy as np 
import csv
import xlsxwriter
import os
from datetime import datetime


class Extractor:
    def __init__(self, urlOfFiles, formatOfFile):
        self.directory = urlOfFiles
        
        if self.directory[-1] == '/':
            self.directory = self.directory[:-1]

        self.filesFormat = formatOfFile
        self.listOfFiles = []

    def preViewOfFiles(self):
        files = os.listdir(self.directory)
        for file in files:
            if file.endswith(self.filesFormat):
                self.listOfFiles.append(file)

        quantityOfFiles = len(self.listOfFiles)

        return quantityOfFiles, self.listOfFiles
    
    def extractor(self, outputFile, createLogFile):
        self.outputFile = outputFile
        self.createLogFile = createLogFile
        dictOfModificationsDates = {}
        for item in self.listOfFiles:
            if item not in dictOfModificationsDates:
                info = os.stat('{}/{}'.format(self.directory, item))
                lastmodification = datetime.fromtimestamp(info.st_mtime)
                dictOfModificationsDates[item] = lastmodification
        orderedDictOfModifications = sorted(dictOfModificationsDates, key=dictOfModificationsDates.get)

        listOfSpectras = []
        wavelengthTitle = []
        readTitle = True
        for file in orderedDictOfModifications:
            f = open('{}/{}'.format(self.directory, file), 'r')
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
        
        wavelengthTitle.extend(listOfSpectras)

        wavelength = int(len(wavelengthTitle) / (len(orderedDictOfModifications) + 1))
        spectra = np.array(wavelengthTitle).reshape(wavelength, len(orderedDictOfModifications) + 1, order='F')


        workbook = xlsxwriter.Workbook('{}'.format(self.outputFile))
        worksheet_spectra = workbook.add_worksheet('Absorbancy')
        row = 0

        for col, data in enumerate(spectra):
            worksheet_spectra.write_column(row, col, data)
        workbook.close()
        
        return




teste = Extractor('/home/dsilva/Downloads/leitura_de_graos_26-12-19', '.csv')
quantity, files = teste.preViewOfFiles()
dates = teste.extractor('teste')
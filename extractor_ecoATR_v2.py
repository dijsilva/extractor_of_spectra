"""Script para extrair as informações de absorbância dos espectros
gerados pelo software do aparelho EcoATR da empresa Bruker"""
"""Algoritmo escrito por: Diego Silva - Biotecnologia/UnB"""
import numpy as np
import time
import csv
import xlsxwriter
print("=-="*26)
print("""Bem vindo. Este algoritmo extrai os valores de absorbancia presentes nos
arquivos .csv gerados pelo software da OPUS. Depois de colocar os arquivos
no mesmo diretório do algoritomo:""")
print("=-="*26)
m = int(input('Insira o número de arquivos a serem lidos: '))
m = m + 1
name = str(input('Insira o nome do arquivo xlsx a ser salvo: '))
decimal_separator = int(input("\nVocê deve escolher o separador decimal. Digite o valor correposndente a sua escolha:\n\n1 = usar ponto [ . ]\n2 = usar vírgula [ , ]\n\nDigite o valor[ 1 ou 2 ]: "))
shouldApplySeparatorInColumn = str(input("Valores de comprimento de onda como por exemplo 2.400,60 podem apresentar problemas. Você deve checar isso.\nSabendo disso, o separador decimal deve ser aplicado nos valores de comprimentos de onda?\nResposta [S/N]: "))
shouldApplySeparatorInColumn = shouldApplySeparatorInColumn.upper()
if shouldApplySeparatorInColumn == "S":
    shouldApplySeparatorInColumn = True
if shouldApplySeparatorInColumn == "N":
    shouldApplySeparatorInColumn = False
spectra = list() 
s = 1
cont = 0
try:
    try:
        arch = open('1 ({}).dpt'.format(1))
    except:
        exit()
    """para extrair os comprimentos de onda"""
    for l in arch:
        l = l.split(',')[0]
        spectra.append(l)    
    """para extrair os valores de absorbância"""
    while s < m:
        cont = 0
        try:
            arch = open('1 ({}).dpt'.format(s))
        except:
            print('Erro encontrado: Reveja o nome do arquivo.')
        for l in arch:
            l = l.split(',')[1].split('\n')[0]
            spectra.append(l)
        s += 1
    """para salvar em um arquivo xlsx"""
    matriz = np.array(spectra)
    matriz = matriz.reshape(1655, (s), order='F')

    if shouldApplySeparatorInColumn == False:
        for i, info_I in enumerate(matriz):
            for j, infoJ in enumerate(info_I):
                if j != 0:
                    if ("." in infoJ) and (decimal_separator == 2):
                        infoJ = str(infoJ).replace(".", ",")
                        matriz[i,j] = infoJ
                    elif ("," in infoJ) and (decimal_separator == 1):
                        infoJ = str(infoJ).replace(",", ".")
                        matriz[i,j] = infoJ
                else:
                    pass

    if shouldApplySeparatorInColumn == True:
        for i, info_I in enumerate(matriz):
            for j, infoJ in enumerate(info_I):
                if ("." in infoJ) and (decimal_separator == 2):
                    infoJ = str(infoJ).replace(".", ",")
                    matriz[i,j] = infoJ
                elif ("," in infoJ) and (decimal_separator == 1):
                    infoJ = str(infoJ).replace(",", ".")
                    matriz[i,j] = infoJ
                
    workbook = xlsxwriter.Workbook('{}.xlsx'.format(name))
    worksheet_spectra = workbook.add_worksheet('Absorbancia')
    row = 0


    for col, data in enumerate(matriz):
        worksheet_spectra.write_column(row, col, data)
    workbook.close()
    print("Tarefa concluída. Até mais!")
    time.sleep(2)
except:
    print("Aconteceu algo de errado. Por favor, cheque as versões dos pacotes e o nome dos arquivos.")
    time.sleep(2)

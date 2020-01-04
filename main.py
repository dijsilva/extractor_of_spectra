import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from extractor import Extractor
import os
import time



HEIGHT = 550
WIDTH = 800
TITLE = 'Spectra Extractor'

#create tk app
app = tk.Tk()
app.minsize(WIDTH,HEIGHT)
app.resizable(width=False, height=False)
app.title(TITLE)

def openDialog():
    fileTypes = None
    if (((csvVar.get() == 1) and (dptVar.get() == 1)) or ((csvVar.get() == 0) and (dptVar.get() == 0))):
        win = tk.Toplevel()
        win.minsize(200,100)
        win.resizable(width=False, height=False)
        win.wm_title("Warning")

        l = tk.Label(win, text="You should choose one, and only one type of file.", pady=20, padx=40)
        l.pack(fill=tk.Y)

        b = ttk.Button(win, text="OK", command=win.destroy)
        b.place(relx=0.4, rely=0.6)

        return
    
    if dptVar.get() == 1:
        fileTypes = ('DPT files', '.dpt | .DPT')
    if csvVar.get() == 1:
        fileTypes = ('CSV files', '.csv | .CSV')

    global nameOfFiles
    nameOfFiles = filedialog.askopenfilenames(initialdir =  "/home", title = "Select A File", filetypes=[fileTypes])
    if nameOfFiles:
        folderPath.set((os.path.split(nameOfFiles[0])[0]))
        
        formatFile = ''
        if csvVar.get() == 1:
            formatFile = '.csv'
    
        if dptVar.get() == 1:
            formatFile = '.dpt'

        spectras = Extractor(nameOfFiles, formatFile)
        nOfSpectra =  spectras.preViewOfFiles()
        numberOfSpectra.set(str(nOfSpectra))

        progress['value'] = 25
        loadingStatus.set('Successfully uploaded!        ')
        app.update_idletasks()
        return

def openDialogSave():
    directorySave = filedialog.asksaveasfilename(initialdir =  "/home", title = "Select A File", filetypes=(('Excel Files', '*.xlsx'), ('Comma-separated values', '*.csv')))
    if directorySave:
        folderForSave.set(directorySave)
        progress['value'] = 50
        app.update_idletasks()
        loadingStatus.set('Output file defined')
        return directorySave


def handleSubmmit():

    if ((folderForSave.get() == 'Define the output file') or (folderPath.get() == 'Define the files for read')):
        win = tk.Toplevel()
        win.minsize(200,100)
        win.resizable(width=False, height=False)
        win.wm_title("Warning")

        l = tk.Label(win, text="You should choose the files for read and the output file.", pady=20, padx=40)
        l.pack(fill=tk.Y)

        b = ttk.Button(win, text="OK", command=win.destroy)
        b.place(relx=0.4, rely=0.6)

        return

    formatFile = ''
    createLogFile = False
    commaSeparator = False

    if csvVar.get() == 1:
        formatFile = '.csv'
    
    if dptVar.get() == 1:
        formatFile = '.dpt'
    
    if logVar.get() == 1:
        createLogFile = True
    
    if commaSepVar.get() == 1:
        commaSeparator = True

    extraction = Extractor(nameOfFiles, formatFile)
    extraction.preViewOfFiles()
    
    progress['value'] = 75
    loadingStatus.set('Extacting spectra')
    app.update_idletasks()

    try:
        time.sleep(1)
        extraction.extractor(folderForSave.get(), createLogFile, commaSeparator)
        progress['value'] = 100
        loadingStatus.set('Successfully done task')
        app.update_idletasks()
    except:
        loadingStatus.set('An error occurred. Check the log file.')


#create a 'container'
canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)
canvas.pack()

#the frame where itens will be drawn
frame = tk.Frame(app, bg='#d4d4d4', bd=5)
frame.place(relwidth=1, relheight=1)

titleOfSoftware = tk.Label(frame, text='Spectra Extractor', anchor='center', bg='#d4d4d4')
titleOfSoftware.pack()




frameDirectory = tk.Frame(app, bg='#d4d4d4', bd=2, highlightthickness=1, highlightbackground='#777', padx=10, pady=5)
frameDirectory["border"] = "1"
frameDirectory.place(relx=0.5, rely=0.08, relwidth=0.9, relheight=0.27, anchor='n')

titleOfDirectory = tk.Label(frameDirectory, text='Load files', anchor='center', bg='#d4d4d4')
titleOfDirectory.pack()

labelOfSpectrometer = tk.Label(frameDirectory, text='Select the type of files: ', anchor='center', bg='#d4d4d4')
labelOfSpectrometer.place(relwidth=0.24, relheight=0.15, rely=0.15, relx=0)

dptVar = tk.IntVar()
dptVar.set(0)
TidaButton = tk.Checkbutton(frameDirectory, text=".dpt", variable=dptVar, bg='#d4d4d4', activebackground='#d4d4d4')
TidaButton.place(relwidth=0.1, relheight=0.15, rely=0.15, relx=0.25)
csvVar = tk.IntVar()
csvVar.set(0)
EcoButton = tk.Checkbutton(frameDirectory, text=".csv", variable=csvVar, bg='#d4d4d4', activebackground='#d4d4d4')
EcoButton.place(relwidth=0.12, relheight=0.15, rely=0.15, relx=0.34)


labelOfSpectrometer = tk.Label(frameDirectory, text='Select files: ', anchor='center', bg='#d4d4d4')
labelOfSpectrometer.place(relwidth=0.132, relheight=0.15, rely=0.35, relx=0)
#local where the directory is showed
folderPath = tk.StringVar()
folderPath.set('Define the files for read')
entry = tk.Entry(frameDirectory, textvariable=folderPath, state='readonly', font='TkDefaultFont 10 italic', readonlybackground='white')
entry.place(relwidth=0.7, height=35, rely=0.55, relx=0.005)


# Creating a photoimage object to use image and resizing image to fit on button 
photo = tk.PhotoImage(file = os.path.join("images", "select.png")) 
photoimage = photo.subsample(10, 10) 

#creating button for select the directory
buttonOfStart = tk.Button(frameDirectory, text='SELECT FILES', image=photoimage, compound = 'left', padx=10, pady=5, command = openDialog, bd=2, highlightthickness=1, highlightbackground='#777', bg='#d4d4d4')
buttonOfStart["border"] = "1"
buttonOfStart.place(relwidth=0.29, height=35, relx=0.71, rely=0.55)

labelOfSpectrometer = tk.Label(frameDirectory, text='Number of spectra found: ', anchor='center', bg='#d4d4d4')
labelOfSpectrometer.place(relwidth=0.261, relheight=0.15, rely=0.85, relx=0)


numberOfSpectra = tk.StringVar()
labelOfSpectrometer = tk.Label(frameDirectory, textvariable=numberOfSpectra, anchor='center', bg='#d4d4d4')
labelOfSpectrometer.place(relheight=0.15, rely=0.85, relx=0.27)




saveDirectoryFrame = tk.Frame(app, bg='#d4d4d4', bd=2, highlightthickness=1, highlightbackground='#777', padx=10, pady=5)
saveDirectoryFrame["border"] = "1"
saveDirectoryFrame.place(relx=0.5, rely=0.356, relwidth=0.9, relheight=0.19, anchor='n')

titleOfsaveDirectoryFrame = tk.Label(saveDirectoryFrame, text='Save file', anchor='center', bg='#d4d4d4')
titleOfsaveDirectoryFrame.pack()

labelOfSaveFile = tk.Label(saveDirectoryFrame, text='Define the path an name of the output: ', anchor='center', bg='#d4d4d4')
labelOfSaveFile.place(relwidth=0.39, relheight=0.15, rely=0.35, relx=0)

#local where the directory is showed
folderForSave = tk.StringVar()
folderForSave.set('Define the output file')
SaveEntry = tk.Entry(saveDirectoryFrame, textvariable=folderForSave, state="readonly", bg='white', font='TkDefaultFont 10 italic', readonlybackground='white')
SaveEntry.place(relwidth=0.7, height=35, rely=0.55, relx=0.005)

#creating button for select the directory
buttonOfSave = tk.Button(saveDirectoryFrame, text='SAVE AS', image=photoimage, compound = 'left', padx=10, pady=5, command = openDialogSave, bd=2, highlightthickness=1, highlightbackground='#777', bg='#d4d4d4')
buttonOfSave["border"] = "1"
buttonOfSave.place(relwidth=0.29, height=35, relx=0.71, rely=0.55)












optionsFrame = tk.Frame(app, bg='#d4d4d4', bd=2, highlightthickness=1, highlightbackground='#777', padx=10, pady=5)
optionsFrame["border"] = "1"
optionsFrame.place(relx=0.5, rely=0.552, relwidth=0.9, relheight=0.23, anchor='n')

titleOfOptionsFrame = tk.Label(optionsFrame, text='Options', anchor='center', bg='#d4d4d4')
titleOfOptionsFrame.pack()

logVar = tk.IntVar()
logVar.set(0)
logButton = tk.Checkbutton(optionsFrame, text="Create a log file", variable=logVar, bg='#d4d4d4', activebackground='#d4d4d4')
logButton.place(width=130, relheight=0.2, rely=0.25, relx=0)

commaSepVar = tk.IntVar()
commaSepVar.set(1)
commaSepVarButton = tk.Checkbutton(optionsFrame, text="Use comma for decimal separator", variable=commaSepVar, bg='#d4d4d4', activebackground='#d4d4d4')
commaSepVarButton.place(width=247, relheight=0.2, rely=0.45, relx=0)



progress = ttk.Progressbar(app, orient = 'horizontal', 
              length = 100, mode = 'determinate')
progress.place(relwidth=0.8, relheight=0.02, relx=0.1, rely=0.805)


loadingStatus = tk.StringVar()
loadingStatus.set('Waiting for action...')
labelOfLoadingStatus = tk.Label(app, textvariable=loadingStatus, anchor='center', bg='#d4d4d4')
labelOfLoadingStatus.place(relheight=0.031, rely=0.835, relx=0.385)




# Creating a photoimage object to use image and resizing image to fit on button 
photoStart = tk.PhotoImage(file = os.path.join("images", "start.png")) 
photoimageStart = photoStart.subsample(20, 20) 

buttonOfStart = tk.Button(app, text='EXTRAIR', image=photoimageStart, compound = 'left', padx=10, pady=5, command = handleSubmmit, bd=2, highlightthickness=1, highlightbackground='#777', bg='#d4d4d4')
#buttonOfStart["border"] = "1"
buttonOfStart.place(relwidth=0.15, relheight=0.07, relx=0.4, rely=0.9)

app.mainloop()
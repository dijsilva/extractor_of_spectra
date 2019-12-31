import tkinter as tk
#from tkinter import *
from tkinter import filedialog
from tkinter import ttk



HEIGHT = 600
WIDTH = 800
TITLE = 'Spectra Extractor'

#create tk app
app = tk.Tk()
app.minsize(800,600)
app.resizable(width=False, height=False)
app.title(TITLE)

def openDialog():
    directory = filedialog.askdirectory(initialdir =  "/home", title = "Select A File")
    if directory:
        folderPath.set(directory)
        return directory

def openDialogSave():
    directorySave = filedialog.asksaveasfilename(initialdir =  "/home", title = "Select A File", filetypes=(('Comma-separated values', '*.csv'),
    ('Excel Files', '*.xlsx')))
    if directorySave:
        folderForSave.set(directorySave)
        return directorySave


def handleSubmmit():
    variablesButton = [TidaButton, EcoButton]
    variables = [csvVar, dptVar]
    if (((variables[0].get() == 1) and (variables[1].get() == 1)) or ((variables[0]).get() == 0) and (variables[1].get() == 0)):
        win = tk.Toplevel()
        win.minsize(200,100)
        win.resizable(width=False, height=False)
        win.wm_title("Warning")

        l = tk.Label(win, text="You should choose one, and only one type of file.", pady=20, padx=40)
        l.pack(fill=tk.Y)

        b = ttk.Button(win, text="OK", command=win.destroy)
        b.place(relx=0.4, rely=0.6)

        return 
        


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
frameDirectory.place(relx=0.5, rely=0.08, relwidth=0.9, relheight=0.28, anchor='n')

titleOfDirectory = tk.Label(frameDirectory, text='Load files', anchor='center', bg='#d4d4d4')
titleOfDirectory.pack()

labelOfSpectrometer = tk.Label(frameDirectory, text='Selecione o formato do arquivo: ', anchor='center', bg='#d4d4d4')
labelOfSpectrometer.place(relwidth=0.323, relheight=0.15, rely=0.25, relx=0)

dptVar = tk.IntVar()
dptVar.set(0)
TidaButton = tk.Checkbutton(frameDirectory, text=".dpt", variable=dptVar, bg='#d4d4d4', activebackground='#d4d4d4')
TidaButton.place(relwidth=0.1, relheight=0.2, rely=0.25, relx=0.32)
csvVar = tk.IntVar()
csvVar.set(0)
EcoButton = tk.Checkbutton(frameDirectory, text=".csv", variable=csvVar, bg='#d4d4d4', activebackground='#d4d4d4')
EcoButton.place(relwidth=0.12, relheight=0.2, rely=0.25, relx=0.42)


labelOfSpectrometer = tk.Label(frameDirectory, text='Selecione o diretório: ', anchor='center', bg='#d4d4d4')
labelOfSpectrometer.place(relwidth=0.22, relheight=0.15, rely=0.43, relx=0)
#local where the directory is showed
folderPath = tk.StringVar()
entry = tk.Entry(frameDirectory, font=40, textvariable=folderPath)
entry.place(relwidth=0.6, height=40, rely=0.75)


# Creating a photoimage object to use image and resizing image to fit on button 
photo = tk.PhotoImage(file = "images/select.png") 
photoimage = photo.subsample(10, 10) 

#creating button for select the directory
buttonOfStart = tk.Button(frameDirectory, text='SELECIONAR PASTA', image=photoimage, compound = 'left', padx=10, pady=5, command = openDialog, bd=2, highlightthickness=1, highlightbackground='#777', bg='#d4d4d4')
buttonOfStart["border"] = "1"
buttonOfStart.place(relwidth=0.39, height=40, relx=0.61, rely=0.75)














saveDirectoryFrame = tk.Frame(app, bg='#d4d4d4', bd=2, highlightthickness=1, highlightbackground='#777', padx=10, pady=5)
saveDirectoryFrame["border"] = "1"
saveDirectoryFrame.place(relx=0.5, rely=0.37, relwidth=0.9, relheight=0.21, anchor='n')

titleOfsaveDirectoryFrame = tk.Label(saveDirectoryFrame, text='Save file', anchor='center', bg='#d4d4d4')
titleOfsaveDirectoryFrame.pack()

labelOfSaveFile = tk.Label(saveDirectoryFrame, text='Defina o local onde o arquivo será salvo: ', anchor='center', bg='#d4d4d4')
labelOfSaveFile.place(relwidth=0.4, relheight=0.15, rely=0.43, relx=0)

#local where the directory is showed
folderForSave = tk.StringVar()
SaveEntry = tk.Entry(saveDirectoryFrame, font=40, textvariable=folderForSave)
SaveEntry.place(relwidth=0.6, height=40, rely=0.62)

#creating button for select the directory
buttonOfSave = tk.Button(saveDirectoryFrame, text='SELECIONAR PASTA', image=photoimage, compound = 'left', padx=10, pady=5, command = openDialogSave, bd=2, highlightthickness=1, highlightbackground='#777', bg='#d4d4d4')
buttonOfSave["border"] = "1"
buttonOfSave.place(relwidth=0.39, height=40, relx=0.61, rely=0.62)












optionsFrame = tk.Frame(app, bg='#d4d4d4', bd=2, highlightthickness=1, highlightbackground='#777', padx=10, pady=5)
optionsFrame["border"] = "1"
optionsFrame.place(relx=0.5, rely=0.59, relwidth=0.9, relheight=0.25, anchor='n')

titleOfOptionsFrame = tk.Label(optionsFrame, text='Options', anchor='center', bg='#d4d4d4')
titleOfOptionsFrame.pack()

logVar = tk.IntVar()
logVar.set(0)
logButton = tk.Checkbutton(optionsFrame, text="Create a log file", variable=logVar, bg='#d4d4d4', activebackground='#d4d4d4')
logButton.place(width=130, relheight=0.2, rely=0.25, relx=0)








# Creating a photoimage object to use image and resizing image to fit on button 
photoStart = tk.PhotoImage(file = "images/start.png") 
photoimageStart = photoStart.subsample(20, 20) 

buttonOfStart = tk.Button(app, text='EXTRAIR', image=photoimageStart, compound = 'left', padx=10, pady=5, command = handleSubmmit, bd=2, highlightthickness=1, highlightbackground='#777', bg='#d4d4d4')
#buttonOfStart["border"] = "1"
buttonOfStart.place(relwidth=0.15, relheight=0.07, relx=0.4, rely=0.9)

app.mainloop()
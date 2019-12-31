import tkinter as tk
#from tkinter import *
from tkinter import filedialog
from tkinter import BOTH, END, LEFT


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


#create a 'container'
canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)
canvas.pack()

#the frame where itens will be drawn
frame = tk.Frame(app, bg='#d4d4d4', bd=5)
frame.place(relwidth=1, relheight=1)

titleOfSoftware = tk.Label(frame, text='Spectra Extractor', anchor='center', bg='#d4d4d4')
titleOfSoftware.pack()

#d4d4d4
frameDirectory = tk.Frame(app, bg='#d4d4d4', bd=2, highlightthickness=1, highlightbackground='#777', padx=10, pady=5)
frameDirectory["border"] = "1"
frameDirectory.place(relx=0.5, rely=0.08, relwidth=0.9, relheight=0.5, anchor='n')

titleOfDirectory = tk.Label(frameDirectory, text='Escolha a pasta onde estão os arquivos', anchor='center', bg='#d4d4d4')
titleOfDirectory.pack()

labelOfSpectrometer = tk.Label(frameDirectory, text='Selecione o equipamento utilizado: ', anchor='center', bg='#d4d4d4')
labelOfSpectrometer.place(relwidth=0.35, relheight=0.1, rely=0.1, relx=0)

var1 = tk.IntVar()
TidaButton = tk.Checkbutton(frameDirectory, text="TIDA", variable=var1, bg='#d4d4d4', activebackground='#d4d4d4')
TidaButton.place(relwidth=0.12, relheight=0.1, rely=0.1, relx=0.35)
var2 = tk.IntVar()
EcoButton = tk.Checkbutton(frameDirectory, text="ECO-ATR", variable=var2, bg='#d4d4d4', activebackground='#d4d4d4')
EcoButton.place(relwidth=0.12, relheight=0.1, rely=0.1, relx=0.5)


#local where the directory is showed
folderPath = tk.StringVar()
entry = tk.Entry(frameDirectory, font=40, textvariable=folderPath)
entry.place(relwidth=0.6, relheight=0.12, rely=0.22)


# Creating a photoimage object to use image and resizing image to fit on button 
photo = tk.PhotoImage(file = "images/select.png") 
photoimage = photo.subsample(10, 10) 

#creating button for select the directory
buttonOfStart = tk.Button(frameDirectory, text='SELECIONAR PASTA', image=photoimage, compound = 'left', padx=10, pady=5, command = openDialog, bd=2, highlightthickness=1, highlightbackground='#777', bg='#d4d4d4')
buttonOfStart["border"] = "1"
buttonOfStart.place(relwidth=0.39, relheight=0.12, relx=0.61, rely=0.22)

app.mainloop()
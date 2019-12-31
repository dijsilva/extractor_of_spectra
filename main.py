import tkinter as tk
#from tkinter import *
from tkinter import filedialog

HEIGHT = 600
WIDTH = 800
TITLE = 'Spectra Extractor'

#create tk app
app = tk.Tk()
app.minsize(800,600)
app.resizable(width=False, height=False)
app.title(TITLE)

def openDialog():
    directory = filedialog.askopenfilename(initialdir =  "/home", title = "Select A File")
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
frameDirectory.place(relx=0.5, rely=0.08, relwidth=0.9, relheight=0.15, anchor='n')

titleOfDirectory = tk.Label(frameDirectory, text='Escolha o arquivo', anchor='center', bg='#d4d4d4')
titleOfDirectory.pack()

folderPath = tk.StringVar()
entry = tk.Entry(frameDirectory, font=40, textvariable=folderPath)
entry.place(relwidth=0.6, relheight=0.55, rely=0.4)


# Creating a photoimage object to use image and resizing image to fit on button 
photo = tk.PhotoImage(file = "images/select.png") 
photoimage = photo.subsample(10, 10) 

#creating button for select the directory
buttonOfStart = tk.Button(frameDirectory, text='SELECIONAR ARQUIVO', image=photoimage, compound = 'left', padx=10, pady=5, command = openDialog, bd=2, highlightthickness=1, highlightbackground='#777', bg='#d4d4d4')
buttonOfStart["border"] = "1"
buttonOfStart.place(relwidth=0.39, relheight=0.55, relx=0.61, rely=0.4)

app.mainloop()
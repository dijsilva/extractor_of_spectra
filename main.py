import tkinter as tk
from tkinter import filedialog

HEIGHT = 500
WIDTH = 700
TITLE = 'Spectra Extractor'

#create tk app
app = tk.Tk()
app.minsize(700,500)
app.title(TITLE)

def Dialog():
    a = filedialog.askopenfilename(initialdir =  "/home", title = "Select A File")
    print(a)

#create a 'container'
canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)
canvas.pack()

# Creating a photoimage object to use image and resizing image to fit on button 
photo = tk.PhotoImage(file = "images/start2.png") 
photoimage = photo.subsample(15, 15) 

#the frame where itens will be drawn
frame = tk.Frame(app, bg='#e4eef0', bd=5)
frame.place(relwidth=1, relheight=1)

buttonOfStart = tk.Button(app, text='Extrair!', image=photoimage, compound = 'left', padx=10, pady=5, command = Dialog)
buttonOfStart["border"] = "0"
buttonOfStart.pack(fill='y')

app.mainloop()
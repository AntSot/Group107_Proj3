from tkinter import *
from PIL import Image, ImageTk
import tkinter
'''import Tkinter as tk'''
from tkinter import messagebox
root = Tk()
'''root = Tk.Tk()'''

def showImg():
     load = Image.open('translatepic.png')
     render = ImageTk.PhotoImage(load)

     backroundimage = render

     img = Label(image=render)

     backroundlabel = Label
     
     img.image = backroundimage
     img.place(x=0,y=0)

     root.wm_geometry("822x462")

showImg()


'''background_image=PhotoImage("C:/Desktop/translatepic.jpg")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.wm_geometry("822x462")'''


root.title("Picture Translator")
root.geometry("822x462")


app = Frame(root)
app.grid()




button1 = Button(app, text = "Select Picture", width=10, height=7)
button1.grid(row=1, column=0)

button2 = Button(app, text = "Translate!", width=7, height=7)
button2.grid(row=10, column=0)





root.mainloop()

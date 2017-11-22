import threading
import random
import os.path
from tkinter import *
import os


def donothing():
    os.system("snek.py 1")


#Root = glugginn

root = Tk()
root.title('Leikjasalernið')
menubar = Menu(root)
#root.geometry("500x500")


topFrame=Frame(root)
one=Label(root,text="Velkominn í leikjasalinn")
one.pack(fill=X)

btn1 = Button(text="Battlefield 1", command=donothing)
btn1.pack()
btn2 = Button(text="Skyrim")
btn2.pack()
btn3 = Button(text="Overwatch")
btn3.pack()

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()

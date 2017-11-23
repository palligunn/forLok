import threading
import random
from random import randint
import os.path
from tkinter import *
import tkinter.messagebox
import os


def teningur():#if int(gisk) == dice: value error
    def rulla():
        tening = randint(1,7)
        if int(gisk) == int(tening):
            tkinter.messagebox.showinfo("Well Done!","Correct!")
        if int(gisk) != int(tening):
            tkinter.messagebox.showinfo("Error"," Invalid number: try again")

    root = Tk()

    Label(root,text="Veldu tölu").pack()

    g = StringVar()
    tala = Entry(root, textvariable=g).pack()
    gisk = g.get()

    submit = Button(root, text = "Kasta tening", command = rulla).pack()
    root.mainloop()

#def annarleikur():
    #annar kóði

#Root = glugginn

root = Tk()
root.title('Leikjasalernið')
menubar = Menu(root)
root.geometry("500x500") #stærðin af glugganum


topFrame=Frame(root)
one=Label(root,text="Velkominn í leikjasalinn")
one.pack(fill=X)

btn1 = Button(text="Teningakast", command=teningur)
btn1.pack()
btn2 = Button(text="Skyrim")
btn2.pack()
btn3 = Button(text="Overwatch")
btn3.pack()

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()

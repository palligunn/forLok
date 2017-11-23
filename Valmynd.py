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
        if gisk == tening:
            tkinter.messagebox.showinfo('Rétt!')
        if gisk != tening:
            tkinter.messagebox.showinfo('Vitlaust')

    root = Tk()

    root.geometry('170x120')#gluggastærð breiddXhæð

    Label(root,text="Veldu tölu").pack()


    g = StringVar() #lætur 'g' vera að int
    tala = Entry(root, textvariable=g).pack()#talan er sleginn inn hér og verður talan = g
    gisk = g.get()#talan sem er inn í g er sett inn í gisk
    Label(root,text=tala).pack()

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
helpmenu.add_command(label="Hjálp")
helpmenu.add_command(label="Um...")
menubar.add_cascade(label="Hjálp", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()

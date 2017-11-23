import threading
import random
from random import randrange
import os.path
from tkinter import *
import os


def teningur():#if int(guess) == dice: value error
    def rulla():
        dice = randrange(1,7)
        if int(guess) == dice:
            tkMessageBox.showinfo("Well Done!","Correct!")
        if int(guess) > 6:
            tkMessageBox.showinfo("Error"," Invalid number: try again")
        elif int(guess) <= 0:
            tkMessageBox.showinfo("Error"," Invalid number: try again")
        else:
            tkMessageBox.showinfo("Incorrect","Incorrect: dice rolled {}.".format(diceRoll))

    root = Tk()

    Label(root,text="Enter your guess").pack()

    g = StringVar()
    inputGuess = Entry(root, textvariable=g).pack()
    guess = g.get() #changed variable from v to g

    submit = Button(root, text = "Roll Dice", command = rulla).pack()
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
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()

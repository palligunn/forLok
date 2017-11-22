from random import randrange
from tkinter import *


def checkAnswer():
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

Label(root,text="Enter your guess").pack() #parent wasn't specified, added root

g = StringVar()
inputGuess = Entry(root, textvariable=g).pack() #changed variable from v to g
guess = g.get() #changed variable from v to g

submit = Button(root, text = "Roll Dice", command = checkAnswer).pack() #added root as parent
root.mainloop()
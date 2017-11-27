import threading
import random
from random import randint, randrange
from tkinter import *
import tkinter.messagebox
from turtle import *
from freegames import square, vector

def teningur():
    stig =100
    def rulla(numbers):

        tening = randint(1,6)
        if numbers == tening:
            tkinter.messagebox.showinfo('Rétt!')
        else:
            tkinter.messagebox.showinfo('Vitlaust', tening)



    root = Tk()

    root.geometry('200x200')#gluggastærð breiddXhæð

    #Label(root,text='veldu tölu').pack()

    text_Input = StringVar()
    one = Label(root,text=stig,bg='white',fg='black').grid(row=3, column=2)
    btn1 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='1',command=lambda: rulla(1)).grid(row=1, column=0)
    btn2 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='2',command=lambda: rulla(2)).grid(row=1, column=1)
    btn3 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='3',command=lambda: rulla(3)).grid(row=1, column=2)
    btn4 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='4',command=lambda: rulla(4)).grid(row=2, column=0)
    btn5 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='5',command=lambda: rulla(5)).grid(row=2, column=1)
    btn6 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='6',command=lambda: rulla(6)).grid(row=2, column=2)

    '''
    g = StringVar() #lætur 'g' vera að int
    tala = Entry(root, textvariable=g).pack()#talan er sleginn inn hér og verður talan = g
    gisk = g.get()#talan sem er inn í g er sett inn í gisk
    
    submit = Button(root, text = "Kasta tening", command = rulla).pack()
    '''
    root.mainloop()

#def annarleikur():
    #annar kóði

#Root = glugginn

root = Tk()
root.title('Leikjasalurinn')
menubar = Menu(root)
root.geometry("500x500") #stærðin af glugganum


topFrame=Frame(root)
one=Label(root,text="Velkominn í leikjasalinn")
one.pack(fill=X)

btn1 = Button(text="Teningakast", command=teningur)
btn1.pack()
btn2 = Button(text="leikur2")
btn2.pack()
btn3 = Button(text="leikur3")
btn3.pack()

'''
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Hjálp")
helpmenu.add_command(label="Um...")
menubar.add_cascade(label="Hjálp", menu=helpmenu)
'''
root.config(menu=menubar)
root.mainloop()

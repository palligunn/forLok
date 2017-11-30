import threading
from time import sleep
from random import randint, randrange, choice
from tkinter import *
import tkinter.messagebox
import tkinter.messagebox as tm
from turtle import *
from freegames import square, vector, floor

#class Leikmadur:
#    def __init__(self, nafn, lykilord):


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username")
        self.label_2 = Label(self, text="Password")

        self.entry_1 = Entry(self)#comment
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.logbtn = Button(self, text="nýskráning", command=self._nyskraning_btn_clicked)
        self.logbtn.grid(columnspan=2)


        self.pack()


    def _login_btn_clickked(self):
        #print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        #print(username, password)

        with open('notendaupplysingar.txt', 'r', encoding='utf-8') as f:
            for i in f:
                if username in f:
                    tm.showinfo("Login info", "Welcome John")
                    root.destroy()
                    command = valmynd()
                else:
                    tm.showerror("Login error", "Incorrect username")


    def _nyskraning_btn_clicked(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        with open('notendaupplysingar.txt','a', encoding='utf-8') as f:
            f.write(username)
            f.write('\n')
            #reyna að bæta við delimiter
            f.write(password)
            f.close()

def teningakast():
    stig = StringVar()# þarf að laga þetta svo að stigin breytast
    stig.set(1000)
    root = Tk()

    root.geometry('200x200')  # gluggastærð breiddXhæð

    # Label(root,text='veldu tölu').pack()
    tening = randint(1,6)
    text_Input = StringVar()  # takkarnir með tölum sem þú getur valið
    one = Label(root, textvariable=stig, bg='white', fg='black').grid(row=3, column=2)
    btn1 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='1',command=lambda: rulla(1,tening,root,stig)).grid(row=1, column=0)
    btn2 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='2',command=lambda: rulla(2,tening,root,stig)).grid(row=1, column=1)
    btn3 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='3',command=lambda: rulla(3,tening,root,stig)).grid(row=1, column=2)
    btn4 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='4',command=lambda: rulla(4,tening,root,stig)).grid(row=2, column=0)
    btn5 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='5',command=lambda: rulla(5,tening,root,stig)).grid(row=2, column=1)
    btn6 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='6',command=lambda: rulla(6,tening,root,stig)).grid(row=2, column=2)


def rulla(numer,tening,root,stig):
    stig = 1000
    if numer == tening:
        tkinter.messagebox.showinfo('Rétt!')#gefur upp nýjan glugga með hvort þú vannst eða tapaðir
        stig=stig+100
        print(stig)
        root.update_idletasks()
        root.destroy()
    else:
        tkinter.messagebox.showinfo('Vitlaust',tening)
        stig=stig-50
        print(stig)
        root.update_idletasks()
        return stig


def leikur1():
        punktur = vector(0, 0)#segir hvað hvar er á glugganum(s.s vector)
        snake = [vector(10, 0)]
        aim = vector(0, -10)

        def change(x, y):#breytir áttinni á snákinum
            aim.x = x
            aim.y = y

        def inside(head):
            "Return True if head inside boundaries."
            return -200 < head.x < 190 and -200 < head.y < 190

        def move():
            "Move snake forward one segment."
            head = snake[-1].copy()
            head.move(aim)

            if not inside(head) or head in snake:
                square(head.x, head.y, 9, 'red')
                update()
                tkinter.messagebox.showinfo('Leik Lokið!')
                Screen().bye()
                return

            snake.append(head)

            if head == punktur:
                print('Snake:', len(snake))
                punktur.x = randrange(-15, 15) * 10
                punktur.y = randrange(-15, 15) * 10
            else:
                snake.pop(0)

            clear()

            for body in snake:
                square(body.x, body.y, 9, 'black')

            square(punktur.x, punktur.y, 9, 'green')
            update()
            ontimer(move, 100)

        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        listen()
        onkey(lambda: change(10, 0), 'Right')
        onkey(lambda: change(-10, 0), 'Left')
        onkey(lambda: change(0, 10), 'Up')
        onkey(lambda: change(0, -10), 'Down')
        move()
        done()
        turtle.mainloop()



def leikur3():


    pattern = []
    guesses = []
    tiles = {
        vector(0, 0): ('red', 'dark red'),
        vector(0, -200): ('blue', 'dark blue'),
        vector(-200, 0): ('green', 'dark green'),
        vector(-200, -200): ('yellow', 'khaki'),
    }


    def grid():
        "Draw grid of tiles."
        square(0, 0, 200, 'dark red')
        square(0, -200, 200, 'blue')
        square(-200, 0, 200, 'green')
        square(-200, -200, 200, 'yellow')
        update()


    def flash(tile):
        "Flash tile in grid."
        glow, dark = tiles[tile]
        square(tile.x, tile.y, 200, glow)
        update()
        sleep(0.5)
        square(tile.x, tile.y, 200, dark)
        update()
        sleep(0.5)


    def grow():
        "Grow pattern and flash tiles."
        tile = choice(list(tiles))
        pattern.append(tile)

        for tile in pattern:
            flash(tile)

        print('Pattern length:', len(pattern))
        guesses.clear()


    def tap(x, y):
        "Respond to screen tap."
        onscreenclick(None)
        x = floor(x, 200)
        y = floor(y, 200)
        tile = vector(x, y)
        index = len(guesses)

        if tile != pattern[index]:
            tkinter.messagebox.showinfo('Leik Lokið!')
            Screen().bye()

        guesses.append(tile)
        flash(tile)

        if len(guesses) == len(pattern):
            grow()

        onscreenclick(tap)


    def start(x, y):
        "Start game."
        grow()
        onscreenclick(tap)


    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    grid()
    onscreenclick(start)
    done()
    turtle.mainloop()



def valmynd():
    def hætta():
        quit()

    root = Tk()
    root.title('Leikjasalurinn')
    menubar = Menu(root)
    root.geometry("500x500") #stærðin af glugganum


    topFrame=Frame(root)
    one=Label(root,text="Velkominn í leikjasalinn")
    one.pack(fill=X)
    root.configure(background='green')

    btn1 = Button(text="Teningakast", padx=10, pady=10, bg='blue', fg='yellow', command=teningakast)
    btn1.pack()
    btn2 = Button(text="Snake", padx=26, pady=10, bg='yellow', fg='cyan', command=leikur1)
    btn2.pack()
    btn3 = Button(text="Símon segir", padx=24, pady=10, bg='cyan', fg='blue', command=leikur3)
    btn3.pack()
    btn4 = Button(text="Hætta", padx=25, pady=10, bg='red', fg='black', command=hætta)
    btn4.pack()

    '''
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Hjálp")
    helpmenu.add_command(label="Um...")
    menubar.add_cascade(label="Hjálp", menu=helpmenu)
    '''
    root.config(menu=menubar)
    root.mainloop()

root = Tk()
lf = LoginFrame(root)
root.mainloop()
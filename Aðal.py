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

#það var eitthvað rosalegt vesen að setja inn þessi stigatöflu dót
#þannig að við slepptum því
class LoginFrame(Frame):#class fyrir innskráningu, í tkinter þá byrjar það alltaf á að runna class
    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Username")#nær í notendanafnið
        self.label_2 = Label(self, text="Password")#nær í lykilorðið

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")#breytir stöfunum í stjörnur svo ekki er hægt að sjá lykilorðið

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)#raðar upp glugganum
        self.entry_2.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)#setur inn login takkan

        self.logbtn = Button(self, text="nýskráning", command=self._nyskraning_btn_clicked)
        self.logbtn.grid(columnspan=2)#setur inn nýskráningartakkan


        self.pack()


    def _login_btn_clickked(self):
        #nær í allar upplýsingar og skoðar hvort það passar í skjalinu
        username = self.entry_1.get()
        password = self.entry_2.get()

        #print(username, password)

        with open('notendaupplysingar.txt', 'r', encoding='utf-8') as f:
            for i in f:
                if username != i and password != i:
                    print('leita...')
                    #sleep(3)
                    #tm.showerror("Login error", "Incorrect username")

                else:
                    tm.showinfo("Velkominn")
                    root.destroy()
                    command = valmynd()

    def _nyskraning_btn_clicked(self):#hendir upplýsingum í skjalið
        username = self.entry_1.get()
        password = self.entry_2.get()
        with open('notendaupplysingar.txt','a', encoding='utf-8') as f:
            f.write(username)
            f.write('\n')
            #reyna að bæta við delimiter
            f.write(password)
            f.close()

def teningakast():#fyrsti leikurinn
    stig = StringVar()# þarf að laga þetta svo að stigin breytast
    stig.set(1000)
    root = Tk()#opnar gluggan

    root.geometry('200x200')  # gluggastærð breiddXhæð

    # Label(root,text='veldu tölu').pack()
    tening = randint(1,6)#velur tölu á milli 1-6
    text_Input = StringVar()  # takkarnir með tölum sem þú getur valið
    one = Label(root, textvariable=stig, bg='white', fg='black').grid(row=3, column=2)
    btn1 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='1',command=lambda: rulla(1,tening,root,stig)).grid(row=1, column=0)#takkarnir
    btn2 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='2',command=lambda: rulla(2,tening,root,stig)).grid(row=1, column=1)
    btn3 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='3',command=lambda: rulla(3,tening,root,stig)).grid(row=1, column=2)
    btn4 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='4',command=lambda: rulla(4,tening,root,stig)).grid(row=2, column=0)
    btn5 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='5',command=lambda: rulla(5,tening,root,stig)).grid(row=2, column=1)
    btn6 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='6',command=lambda: rulla(6,tening,root,stig)).grid(row=2, column=2)


def rulla(numer,tening,root,stig):
    stig = 1000#virkar ekki af eitthverri ástæðu-bryngeir
    if numer == tening:
        tkinter.messagebox.showinfo('Rétt!')#gefur upp nýjan glugga með hvort þú vannst eða tapaðir
        stig=stig+100
        print(stig)
        root.update_idletasks()
        root.destroy()
    else:
        tkinter.messagebox.showinfo('Vitlaust')#segir að þú giskaðir á vitlaust
        stig=stig-50
        print(stig)
        root.update_idletasks()
        return stig


def leikur1():#notar ekki tKinter heldur Turtle sem er betra þegar þú gerir leiki
        punktur = vector(0, 0)#segir hvað hvar er á glugganum(s.s vector)
        snake = [vector(10, 0)]
        aim = vector(0, -10)

        def change(x, y):#breytir áttinni á snákinum
            aim.x = x
            aim.y = y

        def inside(head):
            "Skilar True ef snákurinn er inn á gluggnum"
            return -200 < head.x < 190 and -200 < head.y < 190

        def move():
            "hreyfir snákinn um eitt segment"
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
        #stýringarnar
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



def leikur3():#símon segir
    #notar turtle líka

    pattern = []
    guesses = []
    tiles = {
        vector(0, 0): ('red', 'dark red'),
        vector(0, -200): ('blue', 'dark blue'),
        vector(-200, 0): ('green', 'dark green'),
        vector(-200, -200): ('yellow', 'khaki'),#litirnir, bæði upplýstir og ekki
    }


    def grid():
        #Setur inn kassana með litina
        square(0, 0, 200, 'dark red')
        square(0, -200, 200, 'blue')
        square(-200, 0, 200, 'green')
        square(-200, -200, 200, 'yellow')
        update()


    def flash(tile):
        #lætur litina blikka!
        glow, dark = tiles[tile]
        square(tile.x, tile.y, 200, glow)
        update()
        sleep(0.5)
        square(tile.x, tile.y, 200, dark)
        update()
        sleep(0.5)


    def grow():
        #Spilar leikinn
        tile = choice(list(tiles))
        pattern.append(tile)

        for tile in pattern:
            flash(tile)

        print('Pattern length:', len(pattern))
        guesses.clear()


    def tap(x, y):
        #bregst við þegar þú klikkar
        onscreenclick(None)
        x = floor(x, 200)
        y = floor(y, 200)
        tile = vector(x, y)
        index = len(guesses)

        if tile != pattern[index]:
            tkinter.messagebox.showinfo('Leik Lokið!')
            Screen().bye()#slekkur á leiknum ef þú tapar

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
    turtle.mainloop()#lokar leiknum



def valmynd():
    def hætta():#lokar aðalvalmyndinni
        quit()

    root = Tk()#býr til gluggan
    root.title('Leikjasalurinn')
    menubar = Menu(root)
    root.geometry("500x500") #stærðin af glugganum


    topFrame=Frame(root)
    one=Label(root,text="Velkominn í leikjasalinn")
    one.pack(fill=X)
    root.configure(background='green')
    #býr til takkana á valmyndinni
    btn1 = Button(text="Teningakast", padx=10, pady=10, bg='blue', fg='yellow', command=teningakast)
    btn1.pack()
    btn2 = Button(text="Snake", padx=26, pady=10, bg='yellow', fg='cyan', command=leikur1)
    btn2.pack()
    btn3 = Button(text="Símon segir", padx=24, pady=10, bg='cyan', fg='blue', command=leikur3)
    btn3.pack()
    btn4 = Button(text="Hætta", padx=25, pady=10, bg='red', fg='black', command=hætta)
    btn4.pack()

    '''
    þetta er eitthvað sem við viljum eiga fyrir okkur sjálfa.
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Hjálp")
    helpmenu.add_command(label="Um...")
    menubar.add_cascade(label="Hjálp", menu=helpmenu)
    '''
    root.config(menu=menubar)
    root.mainloop()

root = Tk()
lf = LoginFrame(root)
root.mainloop()#glugginn sjálfur

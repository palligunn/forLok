import threading
from time import sleep
from random import randint, randrange, choice
from tkinter import *
import tkinter.messagebox
from turtle import *
from freegames import square, vector, floor

def valmynd():
#_______________________________________________Teningakast________________________________________________________________________________
    def teningakast():
        stig = 100

        def rulla(numbers):

            tening = randint(1, 6)
            if numbers == tening:
                tkinter.messagebox.showinfo('Rétt!')
            else:
                tkinter.messagebox.showinfo('Vitlaust', tening)

        root = Tk()

        root.geometry('200x200')  # gluggastærð breiddXhæð

        # Label(root,text='veldu tölu').pack()

        text_Input = StringVar()
        one = Label(root, text=stig, bg='white', fg='black').grid(row=3, column=2)
        btn1 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='1',command=lambda: rulla(1)).grid(row=1, column=0)
        btn2 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='2',command=lambda: rulla(2)).grid(row=1, column=1)
        btn3 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='3',command=lambda: rulla(3)).grid(row=1, column=2)
        btn4 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='4',command=lambda: rulla(4)).grid(row=2, column=0)
        btn5 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='5',command=lambda: rulla(5)).grid(row=2, column=1)
        btn6 = Button(root, padx=4, pady=4, bd=2, fg="black", font=('arial', 20, 'bold'), text='6',command=lambda: rulla(6)).grid(row=2, column=2)
#_____________________________________________________SNAKE_______________________________________________________________________________________
    def leikur1():
        food = vector(0, 0)
        snake = [vector(10, 0)]
        aim = vector(0, -10)

        def change(x, y):
            "Change snake direction."
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
                return

            snake.append(head)

            if head == food:
                print('Snake:', len(snake))
                food.x = randrange(-15, 15) * 10
                food.y = randrange(-15, 15) * 10
            else:
                snake.pop(0)

            clear()

            for body in snake:
                square(body.x, body.y, 9, 'black')

            square(food.x, food.y, 9, 'green')
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
                exit()

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

    def hætta():
        quit()

    root = Tk()
    root.title('Leikjasalurinn')
    menubar = Menu(root)
    root.geometry("500x500") #stærðin af glugganum


    topFrame=Frame(root)
    one=Label(root,text="Velkominn í leikjasalinn")
    one.pack(fill=X)

    btn1 = Button(text="Teningakast", command=teningakast)
    btn1.pack()
    btn2 = Button(text="Snake", command=leikur1)
    btn2.pack()
    btn3 = Button(text="leikur3", command=leikur3)
    btn3.pack()
    btn4 = Button(text="HÆTTA MANNFJANDI", command=hætta)
    btn4.pack()

    '''
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Hjálp")
    helpmenu.add_command(label="Um...")
    menubar.add_cascade(label="Hjálp", menu=helpmenu)
    '''
    root.config(menu=menubar)
    root.mainloop()

valmynd()
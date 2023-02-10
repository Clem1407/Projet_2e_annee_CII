from tkinter import *
from random import randint
import tkinter
from tkinter.messagebox import *

#Ref : https://pythonprogramming.altervista.org/tkinter-maze-generator-and-a-game/

def Labyrinthe():
    global f
    global labelnbr
    global nbrcache
    global sv
    global x1, y1
    global rouge, marron, violet, orange, bleu
    cell_size = 15  # pixels
    ms = 20  # rows and columns
    visited_cells = []
    walls = []
    revisited_cells = []

    # creates a list with 50 x 50 "w" items
    map = [['w' for _ in range(ms)] for _ in range(ms)]


    def create():
        "Create a rectangle with draw function (below) with random color"
        for row in range(ms):
            for col in range(ms):
                if map[row][col] == 'P':
                    color = 'white'
                elif map[row][col] == 'w':
                    color = 'black'
                draw(row, col, color)


    def draw(row, col, color):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        ffs.create_rectangle(x1, y1, x2, y2, fill=color)



    def check_neighbours(ccr, ccc):
        neighbours = [[
            ccr,
            ccc - 1,
            ccr - 1,
            ccc - 2,
            ccr,
            ccc - 2,
            ccr + 1,
            ccc - 2,
            ccr - 1,
            ccc - 1,
            ccr + 1,
            ccc - 1
        ],

            # left
            [ccr, ccc + 1, ccr - 1, ccc + 2, ccr, ccc + 2, ccr + 1, ccc + 2, ccr - 1, ccc + 1, ccr + 1, ccc + 1],  # right
            [ccr - 1, ccc, ccr - 2, ccc - 1, ccr - 2, ccc, ccr - 2, ccc + 1, ccr - 1, ccc - 1, ccr - 1, ccc + 1],  # top
            [ccr + 1, ccc, ccr + 2, ccc - 1, ccr + 2, ccc, ccr + 2, ccc + 1, ccr + 1, ccc - 1, ccr + 1, ccc + 1]]  # bottom
        visitable_neighbours = []
        for i in neighbours:  # find neighbours to visit
            if i[0] > 0 and i[0] < (ms - 1) and i[1] > 0 and i[1] < (ms - 1):
                if map[i[2]][i[3]] == 'P' or map[i[4]][i[5]] == 'P' or map[i[6]][i[7]] == 'P' or map[i[8]][i[9]] == 'P' or \
                        map[i[10]][i[11]] == 'P':
                    walls.append(i[0:2])
                else:
                    visitable_neighbours.append(i[0:2])
        return visitable_neighbours


    # StartingPoint

    # starting color of row
    scr = randint(1, ms)
    # starting random column
    scc = randint(1, ms)
    start_color = 'Green'
    # memorize row and column of the starting rectangle
    # current color row and current color column
    ccr, ccc = scr, scc
    x1 = ccr * 15
    y1 = ccc * 15
    print(scr, scc)
    print(ccr, ccc)

    map[ccr][ccc] = 'P'
    loop = 1
    while loop:
        visitable_neighbours = check_neighbours(ccr, ccc)
        if len(visitable_neighbours) != 0:
            d = randint(1, len(visitable_neighbours)) - 1
            ncr, ncc = visitable_neighbours[d]
            map[ncr][ncc] = 'P'
            visited_cells.append([ncr, ncc])
            ccr, ccc = ncr, ncc
        if len(visitable_neighbours) == 0:
            try:
                ccr, ccc = visited_cells.pop()
                revisited_cells.append([ccr, ccc])

            except:
                loop = 0


    window = Tk()
    window.title('Maze')
    canvas_side = ms * cell_size
    ffs = Canvas(window, width=canvas_side, height=canvas_side, bg='gray')
    label_title = Label(window, text="Nombre de cachés", font=("courrier", 22))
    ffs.pack()
    label_title.pack()

    create()
    y1 = scr * cell_size
    x1 = scc * cell_size
    draw(scr, scc, start_color)

    e = randint(1, len(revisited_cells)) - 1
    ecr = revisited_cells[e][0]
    ecc = revisited_cells[e][1]

    e1 = randint(1, len(revisited_cells)) - 1
    ecr1 = revisited_cells[e1][0]
    ecc1 = revisited_cells[e1][1]

    e2 = randint(1, len(revisited_cells)) - 1
    ecr2 = revisited_cells[e2][0]
    ecc2 = revisited_cells[e2][1]

    e3 = randint(1, len(revisited_cells)) - 1
    ecr3 = revisited_cells[e3][0]
    ecc3 = revisited_cells[e3][1]

    e4 = randint(1, len(revisited_cells)) - 1
    ecr4 = revisited_cells[e4][0]
    ecc4 = revisited_cells[e4][1]

    end_color = 'red'
    end_color1 = 'brown'
    end_color2 = 'purple'
    end_color3 = 'orange'
    end_color4 = 'blue'

    draw(ecr, ecc, end_color)
    draw(ecr1, ecc1, end_color1)
    draw(ecr2, ecc2, end_color2)
    draw(ecr3, ecc3, end_color3)
    draw(ecr4, ecc4, end_color4)

    def draw_rect():
        ffs.create_rectangle((x1, y1, x1 + 15, y1 + 15), fill="green")

    def del_rect():
        ffs.create_rectangle((x1, y1, x1 + 15, y1 + 15), fill="gray")

    f = 0
    nbrcache = 5
    sv = StringVar()
    labelnbr = Label(window, textvariable=sv, font=("courrier", 22))
    sv.set(str(nbrcache - f))
    labelnbr.pack()

    def cache():
        global f
        global labelnbr
        global nbrcache
        global sv
        labelnbr.pack_forget()
        f += 1
        labelnbr = Label(window, textvariable=sv, font=("courrier", 22))
        sv.set(str(nbrcache - f))
        labelnbr.pack()
        if f == 5:
            window.destroy()
            fenetre1.destroy()
            fen()

    rouge = 0
    marron = 0
    violet = 0
    orange = 0
    bleu = 0

    def move(event):
        global x1, y1
        global rouge, marron, violet, orange, bleu
        # print(event.char)
        del_rect()
        col = w = x1 // cell_size
        row = h = y1 // cell_size
        if col == ecc and row == ecr and rouge == 0:
            cache()
            rouge += 1
        if col == ecc1 and row == ecr1 and marron == 0:
            cache()
            marron += 1
        if col == ecc2 and row == ecr2 and violet == 0:
            cache()
            violet += 1
        if col == ecc3 and row == ecr3 and orange == 0:
            cache()
            orange += 1
        if col == ecc4 and row == ecr4 and bleu == 0:
            cache()
            bleu += 1
        print("before", map[row][col])
        if event.char == "q":
            if map[row][col - 1] == "P":
                x1 -= cell_size
        elif event.char == "d":
            if map[row][col + 1] == "P":
                x1 += cell_size
        elif event.char == "z":
            if map[row - 1][col] == "P":
                y1 -= cell_size
        elif event.char == "s":
            if map[row + 1][col] == "P":
                y1 += cell_size

        draw_rect()
        col = w = x1 // cell_size
        row = h = y1 // cell_size
        print(w, h)
        print("after", map[row][col])

    window.bind("<Key>", move)
    window.mainloop()

# creer une nouvelle fenetre
fenetre1 = tkinter.Tk()

# personnnaliser ma fenetre
fenetre1.title("Jeu du cache cache")
# widgets
mainmenu = tkinter.Menu(fenetre1)
fenetre1.config(menu=mainmenu)
fenetre1.geometry("1200x800")
fenetre1.minsize(460, 300)
fenetre1.config(background='#5392f5')

def fenetre():
    global fenetre1
    # frame
    frame = Frame(fenetre1, width=310, height=200, bg='#5392f5')
    label_title = Label(fenetre1, text="Labyrinthe", font=("courrier", 22))
    label_title.pack()

    def choix():
        # frame choice
        frame = Frame(fenetre1)
        frame.place(relx=0.026, rely=0.063, relheight=0.8, relwidth=0.924)
        frame.configure(relief='groove', borderwidth="2", background="#9cc2ff")

        Facile = Button(frame, text='''Facile''', font=("Bahnschrift", 30), bg='#09234d', fg='white', command=Labyrinthe)
        Facile.pack(expand="yes")

        Normal = Button(frame, text='''Normal''', font=("Bahnschrift", 30), bg='#09234d', fg='white', command=Labyrinthe)
        Normal.pack(expand="yes")

        Difficile = Button(frame, text='''Difficile''', font=("Bahnschrift", 30), bg='#09234d', fg='white', command=Labyrinthe)
        Difficile.pack(expand="yes")

        ButtonN5 = Button(frame, text='''comeback''', font=("Bahnschrift", 15), bg='black', fg='white',
                          command=frame.destroy)
        ButtonN5.place(relx=0.015, rely=0.870)

        label_title.destroy()

    # ajouter un premier boutton

    Jouer_button = Button(frame, text="Jouer au jeu ", font=("Elephant", 30), bg='#093a87', fg='white', command=choix)
    Jouer_button.place(relx=0.076, rely=0.123)

    # ajouter un deuxième boutton
    Regle_button = Button(frame, text="Règles ", font=("Elephant", 30), bg='#093a87', fg='white')
    Regle_button.place(relx=0.250, rely=0.623)

    # ajouter
    frame.pack(expand=YES)

    # afficher

    fenetre1.mainloop()

def fen():
    fen = Tk()
    fen.title("Bravo")
    fen.geometry("800x600")
    fen.config(background='#5392f5')
    # frame choice
    frame3 = Frame(fen)

    frame3.place(relx=0.026, rely=0.063, relheight=0.8, relwidth=0.924)
    frame3.configure(relief='groove', borderwidth="2", background="#9cc2ff")
    label_title3 = Label(fen, text="Bravo ! Vous avez gagné", font=("courrier", 22))
    label_title3.pack()
    Rejouer = Button(frame3, text='''Rejouer''', font=("Bahnschrift", 30), bg='#09234d', fg='white', command = Labyrinthe)
    Rejouer.pack(expand="yes")

    Retour = Button(frame3, text='''Retour''', font=("Bahnschrift", 15), bg='black', fg='white',command=frame3.destroy)
    Retour.place(relx=0.015, rely=0.870)


fenetre()
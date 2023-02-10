from tkinter import*
import tkinter
import tkinter.filedialog as tkfd

#creer une nouvelle fenetre
fenetre = tkinter.Tk()


#personnnaliser ma fenetre
fenetre.title("Jeu du cache cache")
# widgets
mainmenu = tkinter.Menu(fenetre)

fenetre.config(menu=mainmenu)
fenetre.geometry("1200x800")
fenetre.minsize(460, 300)
fenetre.config(background='#5392f5')
#frame
frame = Frame(fenetre, width=310, height=200, bg='#5392f5')
label_title = Label(fenetre, text="Labyrinthe", font=("courrier", 22))
label_title.pack()

def choix():

    # frame choice
    frame = Frame(fenetre)
    frame.place(relx=0.026, rely=0.063, relheight=0.8, relwidth=0.924)
    frame.configure(relief='groove', borderwidth="2", background="#9cc2ff")

    Facile = Button(frame, text='''Facile''', font=("Bahnschrift", 30), bg='#09234d', fg='white')
    Facile.pack(expand="yes")

    Normal = Button(frame, text='''Normal''', font=("Bahnschrift", 30), bg='#09234d', fg='white')
    Normal.pack(expand="yes")

    Difficile = Button(frame, text='''Difficile''', font=("Bahnschrift", 30), bg='#09234d', fg='white')
    Difficile.pack(expand="yes")

    ButtonN5 = Button(frame, text='''comeback''', font=("Bahnschrift", 15), bg='black', fg='white', command=frame.destroy)
    ButtonN5.place(relx=0.015, rely=0.870)

    label_title.destroy()

#ajouter un premier boutton

Jouer_button = Button(frame, text="Jouer au jeu ", font=("Elephant", 30), bg='#093a87', fg='white', command=choix)
Jouer_button.place(relx=0.076, rely=0.123)

#ajouter un deuxième boutton
Regle_button = Button(frame, text="Règles ", font=("Elephant", 30), bg='#093a87', fg='white')
Regle_button.place(relx=0.250, rely=0.623)

#ajouter
frame.pack(expand=YES)

#afficher
fenetre.mainloop()
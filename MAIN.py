from Game import *
import tkinter as tk
from tkinter import messagebox


def ask_parameters():
    global root, default_x, default_y, default_mine, cheat

    if root is not None:
        root.destroy()

    root = tk.Tk()
    default_x = tk.StringVar(root)
    default_y = tk.StringVar(root)
    default_mine = tk.StringVar(root)
    cheat = tk.BooleanVar(root)

    root.focus_force()
    default_x.set("10")
    default_y.set("10")
    default_mine.set("10")

    label_x = tk.Label(root, text="Longueur")
    label_x.grid(row=0, column=0)
    input_x = tk.Entry(root, textvariable=default_x)
    input_x.grid(row=0, column=2)

    label_y = tk.Label(root, text="Largeur")
    label_y.grid(row=1, column=0)
    input_y = tk.Entry(root, textvariable=default_y)
    input_y.grid(row=1, column=2)

    label_mine = tk.Label(root, text="Nombre de mines")
    label_mine.grid(row=2, column=0)
    input_mine = tk.Entry(root, textvariable=default_mine)
    input_mine.grid(row=2, column=2)

    label_cheat = tk.Label(root, text="Cheat")
    label_cheat.grid(row=3, column=0)
    checkbox_cheat = tk.Checkbutton(root, variable=cheat)
    checkbox_cheat.grid(row=3, column=1)

    btn_send = tk.Button(root, text="Lancer", command=is_valid)
    btn_send.grid(row=4, column=1)

    def on_closing():
        if messagebox.askyesno("Quitter", "Vous voulez vraiment quitter le jeu ? :'("):
            root.destroy()
            exit(0)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()


def is_valid():
    if default_x.get() == '' or default_y.get() == '' or default_mine.get() == '':
        tk.messagebox.showwarning("Un problème est survenu", "Tous les champs ne sont pas remplis")
        ask_parameters()
    elif int(default_x.get()) == 0 or int(default_y.get()) == 0 or int(default_mine.get()) == 0:
        tk.messagebox.showwarning("Un problème est survenu", "les valeurs ne peuvent pas être 0")
        ask_parameters()
    elif int(default_mine.get()) > int(default_x.get()) * int(default_y.get()):
        tk.messagebox.showwarning("Un problème est survenu", "Il y a plus de mines que de case disponible")
        ask_parameters()
    else:
        global root
        root.destroy()


def launch():
    global cheat
    ask_parameters()

    x = int(default_x.get())
    y = int(default_y.get())
    mine = int(default_mine.get())

    Game(x, y, mine, cheat).run()
    restart()


def restart():
    global root
    root = tk.Tk()
    root.withdraw()
    answer = messagebox.askyesno("The end", "Encore ?")
    if answer:
        launch()
    else:
        pygame.quit()
        quit()


# Define parameters
root = None
default_x = None
default_y = None
default_mine = None
cheat = False

# LAUNCH APP
launch()

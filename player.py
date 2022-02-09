from fileinput import filename
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from pygame import mixer
mixer.init()
root = Tk()
root.geometry("500x400")
root.resizable(False, False)
root.title("Sigma Music PLayer")

bottom_plate = Label(text="Anas-Dew", bg="Black",
                     fg="White", font="sans 9 italic")
bottom_plate.pack(side=BOTTOM, fill=X)


# ---NECESARY FUNCTIONS------------------------------------


def select_file():
    global main_title
    filetypes = (
        ('Music files', '*.mp3'),
        ('All files', '*.*')
    )

    mfile = fd.askopenfilename(
        title='Open music',
        initialdir='/',
        filetypes=filetypes)
    print("File Path : " + mfile)
    with open(mfile) as music:
        m = music.name[35:150].split(" ")
        main_title = m[0]
        title_bar.config(text=main_title)

    mixer.music.load(mfile)
    mixer.music.play()    

def Pause():
    mixer.music.pause()
#to stop the  song 
def Stop():
    mixer.music.stop()
def Resume():
    mixer.music.unpause()
# MENU BAR-----------------------------------------------------

def menu_bar():
    menubar = Menu(root)

    # Adding File Menu and commands
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    file.add_command(label='Open...', command=lambda: select_file())
    file.add_command(label='Play', command=lambda: select_file.playit())
    file.add_separator()
    file.add_command(label='Exit', command=root.destroy)

    # Adding more Menu and commands
    more = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='More', menu=more)
    more.add_command(label='Source Code', command=None)
    more.add_command(label='Meow !!', command=root.destroy)
    more.add_separator()
    more.add_command(label='About', command=None)
    root.config(menu=menubar)


menu_bar()
# -------------------------------------------------------------
open_button = ttk.Button(
    root,
    text='Open Music',
    command=lambda: select_file()
)

open_button.pack(expand=True)

# --------------------------------------------------------
# NAVIGATION FRAME
play_navi = Frame(root, bg="grey", width=10, borderwidth=10)

title_bar = Label(play_navi, text="Choose Music",
                  bg="grey", fg="White", font="sans 14 italic")
title_bar.pack(side=LEFT, padx=10)

play_button = Button(play_navi, text="Pause",
                     bg="Black", fg="White", font="sans 9 italic", command=Pause)
play_button.pack(side=RIGHT)
play_button = Button(play_navi, text="Resume",
                     bg="Black", fg="White", font="sans 9 italic", command=Resume)
play_button.pack(side=RIGHT)

play_navi.pack(side=BOTTOM, fill=X)

# ------------------------------------------------------


root.mainloop()

from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
from pygame import mixer
import webbrowser
from time import sleep
import os
os.chdir('Music_Player')


mixer.init()
root = Tk()
width = 400
height = 170
root.geometry(f"{width}x{height}")
root.resizable(False, False)

root.title("Sigma Music Player")
mixer.music.load("Sigmaintro.mp3")
mixer.music.play()
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
    mixer.music.load(mfile)
    mixer.music.play()
    title_bar.config(text="Playing...")


def Pause():
    mixer.music.pause()
    title_bar.config(text="Paused.")
# to stop the  song


def Stop():
    mixer.music.stop()


def Resume():
    mixer.music.unpause()
    title_bar.config(text="Playing...")
# MENU BAR-----------------------------------------------------


def menu_bar():
    menubar = Menu(root)

    def loop():
        messagebox.showwarning("Alert","This feature is in development.")

    # Adding File Menu and commands
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    file.add_command(label='Open...', command=lambda: select_file())
    file.add_command(label='Replay', command=lambda: mixer.music.play())
    file.add_checkbutton(label='Loop',command=loop)
    file.add_separator()
    file.add_command(label='Exit', command=root.destroy)

    # Adding more Menu and commands
    more = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='More', menu=more)
    more.add_command(label='Source Code',command=lambda: webbrowser.open_new(
        r"https://github.com/Anas-Dew/Sigma-Music-Player"))

    def meow():
       user_choice = messagebox.askyesno("Feedback","Did you like this app ?")
       print(user_choice)
       if user_choice == True:
           rate_choice = messagebox.askyesno("Support","Rate my project on Github.")
           if rate_choice == True:
               messagebox.showinfo("Redirect","You are being redirected to Github.")
               webbrowser.open_new(
        r"https://github.com/Anas-Dew/Sigma-Music-Player")
           
    more.add_command(label='Meow !!', command=meow)
    more.add_separator()
    more.add_command(label='About', command=lambda: messagebox.showinfo("Developer's Note","Have you liked this little project ? Give your feedback/suggestion on Github and follow up there for more future big projects."))
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
play_navi = Frame(root, bg="dark grey", width=10,
                  borderwidth=5, relief="groove")
# can_widget = Canvas(root, width=100,height=50,bg="grey",borderwidth=0)
# can_widget.pack()

title_bar = Label(play_navi, text="Choose Music",
                  bg="dark grey", fg="black", font="Purisa 19 italic")
title_bar.pack(side=LEFT, padx=10)
pause_button = Button(play_navi, text="Pause",
                      bg="Black", fg="White", font="sans 9 italic", padx=15, command=Pause)
pause_button.pack(side=RIGHT, padx=5)
resume_button = Button(play_navi, text="Resume",
                       bg="Black", fg="White", font="sans 9 italic", padx=10, command=Resume)
resume_button.pack(side=RIGHT, padx=20)

play_navi.pack(side=BOTTOM, fill=X)

# ------------------------------------------------------

root.mainloop()

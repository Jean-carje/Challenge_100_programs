# # notebook.py - A simple notebook program
# Author: Jean Carlos Estevez
# Date: May 16, 2024
# Language: Python 3.12
# Dependencies: os, tkinter
# System requirements: Windows, Mac, or Linux with Python 3.12 installed

import tkinter
import os


class App():
    def __init__(self, root) -> None:
        self.root = root
        root.title("Notebook")

        self.window()

    def window(self):
        menu = tkinter.Menu(root)
        root.config(menu=menu)
        
        filemenu = tkinter.Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open...')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        
        helpmenu = tkinter.Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About')



if __name__ == "__main__":
    root = tkinter.Tk()
    main = App(root)
    root.mainloop()
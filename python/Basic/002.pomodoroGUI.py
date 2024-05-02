# # pomodoro.py - A simple pomodoro program
# Author: Jean Estevez
# Date: March 07, 2024
# Language: Python 3.12
# Dependencies: time, tkinter
# System requirements: Windows, Mac, or Linux with Python 3.12 installed


import tkinter

class App:
    def __init__(self, root) -> None:
        self.root = root
        root.title("Pomodoro")

        # timers
        self.MIN_POMODORO = 0
        self.SEC_POMODORO = "03"
        self.MIN_REST = 0
        self.SEC_REST = "06"

        self.show_window()

    def show_window(self):
        # timer in window
        self.label = tkinter.Label(self.root, text=f'{self.MIN_POMODORO}:{self.SEC_POMODORO}', bg="green", font=("Helvetica", 42))
        self.label.pack()

        # buttons 
        self.btn1 = tkinter.Button(self.root, text="Play", command=self.start_timer, font=("Helvetica", 12))
        self.btn1.pack(side="left", padx=5)

        self.btn2 = tkinter.Button(self.root, text="Stop", command=self.stop_timer, font=("Helvetica", 12))
        self.btn2.pack(side="left", padx=5)
        
        self.btn3 = tkinter.Button(self.root, text="Reset", command=self.reset_timer, font=("Helvetica", 12))
        self.btn3.pack(side="left", padx=5)

    def start_timer(self):
        pass

    def stop_timer(self):
        pass

    def reset_timer(self):
        pass


if __name__ == "__main__":
    root = tkinter.Tk()
    main = App(root)
    root.mainloop()


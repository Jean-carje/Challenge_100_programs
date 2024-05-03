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
        self.MIN_POMODORO = 1
        self.SEC_POMODORO = 3
        self.MIN_REST = 2
        self.SEC_REST = 6

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
        if self.MIN_POMODORO > 0 and self.SEC_POMODORO > 0:
            self.update_timer(self.MIN_POMODORO, int(self.SEC_POMODORO))
            self.MIN_POMODORO, self.SEC_POMODORO = 0, 0
        else:
            self.update_timer(self.MIN_REST, int(self.SEC_RMIN_REST))
            self.MIN_REST, self.SEC_RMIN_REST = 0, 0


    def update_timer(self, minute, seconds):

        self.label.config(text=f'{minute}:{seconds}')

        if minute == 0 and seconds == 0:
            return None
        
        if seconds == 0:
            minute -= 1
            seconds = 59
        else:
            seconds -= 1

        self.label.after(1000, lambda: self.update_timer(minute, seconds))


    def stop_timer(self):
        pass

    def reset_timer(self):
        self.MIN_POMODORO = 1
        self.SEC_POMODORO = 3
        self.MIN_REST = 2
        self.SEC_REST = 6
        self.label.config(text=f'{self.MIN_POMODORO}:{self.SEC_POMODORO}')


if __name__ == "__main__":
    root = tkinter.Tk()
    main = App(root)
    root.mainloop()


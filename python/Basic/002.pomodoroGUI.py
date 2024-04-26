# # pomodoro.py - A simple pomodoro program
# Author: Jean Estevez
# Date: March 07, 2024
# Language: Python 3.12
# Dependencies: time, tkinter
# System requirements: Windows, Mac, or Linux with Python 3.12 installed


import time
import tkinter

class App:
    def __init__(self, root) -> None:
        self.root = root
        root.title("Pomodoro")

        self.MIN_POMODORO = 0
        self.SEC_POMODORO = "03"
        self.MIN_REST = 0
        self.SEC_REST = "04"

        self.show_window()

    def show_window(self):
        self.lbl = tkinter.Label(root, bg="green", font=("Helvetica", 48), text=f"{str(self.MIN_POMODORO)}:{str(self.SEC_POMODORO)}")
        self.lbl.pack()

        self.btn_start = tkinter.Button(root, text="Start", command=self.start_timer)
        self.btn_start.pack()

        self.btn_stop = tkinter.Button(root, text="Stop", command=self.stop_timer)
        self.btn_stop.pack()

        self.btn_reset = tkinter.Button(root, text="Reset", command=self.reset_timer)
        self.btn_reset.pack()

    def start_timer(self):
        if self.MIN_POMODORO > -1:
            self.lbl.config(text=f"{str(self.MIN_POMODORO)}:{str(self.SEC_POMODORO)}")
            self.root.after(1000, self.update_timer, self.MIN_POMODORO, int(self.SEC_POMODORO))
            # self.MIN_POMODORO, self.SEC_POMODORO = -1, 0
        self.lbl.config(text=f"{str(self.MIN_REST)}:{str(self.SEC_REST)}")
        self.root.after(1000, self.update_timer, self.MIN_REST, int(self.SEC_REST))
        # self.MIN_POMODORO, self.SEC_POMODORO = 25, "00"

    def update_timer(self, minutes, seconds):
        if seconds == 0 and minutes > 0:
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1
        self.lbl.config(text=f"{str(minutes)}:{str(seconds)}")
        if minutes == 0 and seconds == 0:
            return None
        self.root.after(1000, self.update_timer, minutes, seconds)

    def stop_timer(self):
        pass

    def reset_timer(self):
        pass



if __name__ == "__main__":
    root = tkinter.Tk()
    main = App(root)
    root.mainloop()


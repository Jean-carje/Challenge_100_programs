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

        # state timer
        self.state_play = True
        self.state_type = "Pomodoro"

        self.show_window()

    def show_window(self):
        # timer in window
        self.label = tkinter.Label(self.root, text=f'{self.MIN_POMODORO:02d}:{self.SEC_POMODORO:02d}', bg="green", font=("Helvetica", 42))
        self.label.pack()

        # buttons 
        self.btn1 = tkinter.Button(self.root, text="Play", command=self.start_timer, font=("Helvetica", 12))
        self.btn1.pack(side="left", padx=5)

        self.btn2 = tkinter.Button(self.root, text="Stop", command=self.stop_timer, font=("Helvetica", 12))
        self.btn2.pack(side="left", padx=5)
        
        self.btn3 = tkinter.Button(self.root, text="Reset", command=self.reset_timer, font=("Helvetica", 12))
        self.btn3.pack(side="left", padx=5)

    def start_timer(self):
        if self.MIN_POMODORO > 0 or self.SEC_POMODORO > 0:
            self.state_type = "Pomodoro"  # It is used to check at stop, what time it was running
            self.state_play = True
            self.update_timer(self.MIN_POMODORO, int(self.SEC_POMODORO))
        else:
            self.state_type = "Rest"  # It is used to check at stop, what time it was running
            self.update_timer(self.MIN_REST, int(self.SEC_REST))


    def update_timer(self, minute, seconds):
        # update values timer
        if self.state_type == "Pomodoro":
            self.MIN_POMODORO = minute
            self.SEC_POMODORO =  seconds
        else:
            self.MIN_REST = minute
            self.SEC_REST = seconds
    
        self.label.config(text=f'{minute:02d}:{seconds:02d}')

        # update minute and seconds
        if minute == 0 and seconds == 0:
            return None
        
        if seconds == 0:
            minute -= 1
            seconds = 59
        else:
            seconds -= 1

        if self.state_play:
            # To pause the execution of after, by pressing stop
            self.label.after(1000, lambda: self.update_timer(minute, seconds))


    def stop_timer(self):
        self.state_play = False

    def reset_timer(self):
        self.state_play = False

        self.MIN_POMODORO = 1
        self.SEC_POMODORO = 3
        self.MIN_REST = 2
        self.SEC_REST = 6
        self.label.config(text=f'{self.MIN_POMODORO:02d}:{self.SEC_POMODORO:02d}')


if __name__ == "__main__":
    root = tkinter.Tk()
    main = App(root)
    root.mainloop()


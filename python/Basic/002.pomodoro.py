# # pomodoro.py - A simple pomodoro program
# Author: Jean Estevez
# Date: March 07, 2024
# Language: Python 3.10
# Dependencies: time
# System requirements: Windows, Mac, or Linux with Python 3.10 installed


import time 

# values
min_pomodoro = 25
sec_pomodoro = 0
min_rest = 5
sec_rest = 0

# Bucle principal
while True:
    print("""
          select a option:
          1 - Start
          2 - Reset
          """)
    option = int(input(" ---> "))

    if option == 2:
        min_pomodoro = 25
        sec_pomodoro = 0
        min_rest = 5
        sec_rest = 0
    elif option == 1:
        # Start Pomodoro
        while min_pomodoro > 0 or sec_pomodoro > 0:
            print(min_pomodoro, ":", sec_pomodoro)
            if sec_pomodoro == 0 and min_pomodoro > 0:
                min_pomodoro -= 1
                sec_pomodoro = 59
            else:
                sec_pomodoro -= 1
                time.sleep(1)

        # Start Rest
        while min_rest > 0 or sec_rest > 0:
            print(min_rest, ":", sec_rest)
            if sec_rest == 0 and min_rest > 0:
                min_rest -= 1
                sec_rest = 59
            else:
                sec_rest -= 1
                time.sleep(1)
        
        # Reset values
        min_pomodoro = 25
        sec_pomodoro = 0
        min_rest = 5
        sec_rest = 0


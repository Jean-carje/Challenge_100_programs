# # pomodoro.py - A simple pomodoro program
# Author: Jean Estevez
# Date: March 07, 2024
# Language: Python 3.12
# Dependencies: time, tkinter
# System requirements: Windows, Mac, or Linux with Python 3.12 installed


import time

# Valores predeterminados
MIN_POMODORO = 25
SEC_POMODORO = 0
MIN_REST = 5
SEC_REST = 0

def show_menu():
    """Menu options."""
    print("""
          Select Option:
          1 - Start
          """)

def start_timer(minutes, seconds):
    """Start Pomodoro and print minutes and seconds."""
    while minutes > 0 or seconds > 0:
        print(f"{minutes}:{seconds}")
        if seconds == 0 and minutes > 0:
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1
            time.sleep(1)

# def reset_values():
#     """Reset values"""
#     return MIN_POMODORO, SEC_POMODORO, MIN_REST, SEC_REST

def main():
    """Main funtion."""

    while True:
        show_menu()
        option = input(" ---> ")

        # if option == '2':
        #     MIN_POMODORO, SEC_POMODORO, MIN_REST, SEC_REST = reset_values()
        if option == '1':
            # Start Pomodoro
            start_timer(MIN_POMODORO, SEC_POMODORO)
            # rest time
            start_timer(MIN_REST, SEC_REST)
            # reset values
            # MIN_POMODORO, SEC_POMODORO, MIN_REST, SEC_REST = reset_values()

if __name__ == "__main__":
    main()


# toDoList.py - A simple To-Do List program
# Author: Jean Estevez
# Date: 2023
# Language: Python 3.10
# Dependencies: None
# System requirements: Windows, Mac, or Linux with Python 3.10 installed


import os
import os.path
import datetime
import sqlite3
import json

class App():
    def __init__(self) -> None:
        self.current_date = datetime.date.today()
        self.file_data_source = os.getcwd()

    def screen_print(self):
        print("\t\tWelcome!")
        print(f"Today: {self.current_date}")

        print("""\nMenu:
        1-New ToDo List
        2-Open ToDo List
        3-Delete ToDo List
        4-Delete All ToDo List's
        5-Close""")

        


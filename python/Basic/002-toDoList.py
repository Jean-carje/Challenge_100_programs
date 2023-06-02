# toDoList.py - A simple To-Do List program
# Author: Jean Estevez
# Date: May 6, 2023
# Language: Python 3.10
# Dependencies: None
# System requirements: Windows, Mac, or Linux with Python 3.10 installed

import os.path
import datetime
import pickle

# variables
current_date = datetime.date.today()
file_data_source = os.getcwd()
NAME_FOLDER_DATA = "toDo_DATA"
dir_folder_data = os.path.join(file_data_source, NAME_FOLDER_DATA)

# functions
def new_toDo_list(name):
    pass

print("\t\tWelcome!")
print(f"Today: {current_date}")

# Create folder toDo_DATA
try:
    os.mkdir(dir_folder_data)
except FileExistsError:
    pass

print("""Menu:
1-New ToDo List
2-Open ToDo List
3-Delete ToDo List
4-Delete All ToDo List
5-Close""")

try:
    choice = int(input("Select a number of the list? "))
except:
    choice = int(input("Please, Select a number of the list?: "))

if choice == 1:
    pass



# toDoList.py - A simple To-Do List program
# Author: Jean Estevez
# Date: May 6, 2023
# Language: Python 3.10
# Dependencies: None
# System requirements: Windows, Mac, or Linux with Python 3.10 installed

import os
import os.path
import datetime
import sqlite3
import json

# variables
current_date = datetime.date.today()
file_data_source = os.getcwd()
# NAME_FOLDER_DATA = "toDo_DATA"
# dir_folder_data = os.path.join(file_data_source, NAME_FOLDER_DATA)
data_today = {}

# functions
def create_database():
    conn = sqlite3.connect('todo_list.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                due_date DATE, 
                task_description TEXT)''')
    conn.commit()
    conn.close()

def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

def update_screen_task():
    numb_index = 1
    for task, state in data_today:
        state_task = " " if state == False else "1"  
        print(f"{numb_index} - [{state_task}]  {task}")
        numb_index += 1

def get_task_for_index(n):
    numb_index = 1
    task = ""
    for task, state in data_today:
        if numb_index == n:
            return task
        else:
            numb_index += 1


def new_toDo_list(name):
    while True:
        clear_terminal()
        print(f"\t\tToday: {current_date}")
        update_screen_task()
        print("\t1-Add\t2-modify\t3-delete\t4-exit")
        choice = input(">> ")
        if choice == "1":
            description_task = input("task: ")
            data_today[description_task] = False}
            continue
        elif choice == "2":
            number_task_to_modifiy = int(input("Insert (number) of the task to be modified: "))
            print("""1-Mark (completed, not completed)
            2-Modify text""")

            task_modify = get_task_for_index()
            option_to_modify = int(input(">> "))
            if option_to_modify == 1:
                state = data_today[task_modify]
                data_today[number_task_to_modifiy]["state"] = not state
                continue
            elif option_to_modify == 2:
                new_text = input("New text: ")
                data_today[number_task_to_modifiy]["text"] = new_text
                continue
        elif choice == "3":
            number_task_to_delete = int(input("Insert (number) of the task to be deleted: "))

        elif choice == "4":
            pass
        else:
            pass
    

# code
print("\t\tWelcome!")
print(f"Today: {current_date}")

# Create folder toDo_DATA
# try:
#     os.mkdir(dir_folder_data)
# except FileExistsError:
#     pass

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



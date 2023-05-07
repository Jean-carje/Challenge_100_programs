# Calculator.py - A simple calculator program
# Author: Jean Estevez
# Date: May 6, 2023
# Language: Python 3.10
# Dependencies: None
# System requirements: Windows, Mac, or Linux with Python 3.10 installed

# Description:
# This program provides basic arithmetic operations for two numbers: addition, subtraction, multiplication, exponentiation, root and division.
# It takes two inputs from the user, performs the selected operation, and displays the result.

# Functions:
# - add(num1, num2): Adds two numbers and returns the result.
# - subtract(num1, num2): Subtracts two numbers and returns the result.
# - multiply(num1, num2): Multiplies two numbers and returns the result.
# - divide(num1, num2): Divides two numbers and returns the result. Handles division by zero errors.
# - exponentiation(base, exp): exponentiation 
# - root(root, index): root

# Usage:
# Run the program and follow the prompts to input two numbers and select an operation.
# The result will be displayed on the screen.

# Code:

# functions for each arithmetic operation
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
# /////////////////////////////////////////////////////////////////
# ERROR: The division function does not properly handle cases where the
#  second number is a text string instead of a number.
# def divide(num1, num2):
#     # Handle division by zero errors
#     if num2 == 0:
#         return "Error: Division by zero"
#     else:
#         return num1 / num2
# -----------------------------------------------------------------
# Best Code
def divide(num1, num2):
    # Handle division by zero errors and string input errors
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input"
# /////////////////////////////////////////////////////////////////
    
def exponentiation(base, exp):
    return pow(base, exp)

# /////////////////////////////////////////////////////////////////
# ERROR: The root functions do not properly handle negative cases.
#  For example, if the root function is called with a negative
#  number and an even index, it should not return a real answer.
# def root(raiz, index):
#     result = 1
#     while True:
#         op = result ** index
#         if op == raiz:
#             return result
#         else:
#             result += 1
# -----------------------------------------------------------------
# Best Code
def root(num):
    if num < 0:
        return "Error: Imaginary number"
    else:
        return num ** 0.5
# /////////////////////////////////////////////////////////////////

# Code for print
# Prompt the user for input and perform the selected operation

print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. exponentiation")
print("6. root")

choice = int(input("Enter your choice (1-6): "))

if choice in [1, 2, 3, 4]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if choice == 1:
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == 2:
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == 3:
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == 4:
        result = divide(num1, num2)
        print("Result: ", result)
    else:
        print("Invalid choice")
elif choice in [5, 6]:
    num1 = float(input("Enter the number: "))
    if choice == 5:
        num2 = float(input("Enter the exp/index number: "))
        result = exponentiation(num1, num2)
        print("Result: ", result)
    else:
        result = root(num1)
        print("Result: ", result)
else:
    print("Invalid choice")


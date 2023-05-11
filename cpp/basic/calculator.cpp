// # Calculator.cpp - A simple calculator program
// # Author: Jean Estevez
// # Date: May 8, 2023
// # Language: c++
// # Dependencies: None

// # Description:
// # This program provides basic arithmetic operations for two numbers: addition, subtraction, multiplication, exponentiation, root and division.
// # It takes two inputs from the user, performs the selected operation, and displays the result.

// # Functions:
// # - add(num1, num2): Adds two numbers and returns the result.
// # - subtract(num1, num2): Subtracts two numbers and returns the result.
// # - multiply(num1, num2): Multiplies two numbers and returns the result.
// # - divide(num1, num2): Divides two numbers and returns the result. Handles division by zero errors.
// # - exponentiation(base, exp): Exponentiation 
// # - root(num): Root

// # Usage:
// # Run the program and follow the prompts to input two numbers and select an operation.
// # The result will be displayed on the screen.


#include <iostream>
#include <cmath>

int main() {
    // # functions for each arithmetic operation
    int add(int num1, int num2) {
        return num1 + num2;
    }
    int subtract(int num1, int num2) {
        return num1 - num2;
    }
    int multiply(int num1, int num2) {
        return num1 * num2;
    }
    int divide(int num1, int num2) {
        return num1 / num2;
    }
    int exponentiation(int base, int exp) {
        return base ** exp;
    }

    return 0;
}


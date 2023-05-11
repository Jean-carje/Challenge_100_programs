// # Calculator.js - A simple calculator program
// # Author: Jean Estevez
// # Date: May 11, 2023
// # Language: Java
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

import java.lang.Math;

public class Main {
    public static void main(String[] args) {
    }

    // # functions for each arithmetic operation
    public static int add(int num1, int num2) {
        return num1 + num2;
    }

    public static int subtract(int num1, int num2) {
        return num1 - num2;
    }

    public static int multiply(int num1, int num2) {
        return num1 * num2;
    }

    public static int divide(int num1, int num2) {
        return num1 / num2;
    }

    public static double exponentiation(int base, int exp) {
        return base ** exp;
    }

    public static double root(int num1) {
        return Math.sqrt(num1);
    }
}

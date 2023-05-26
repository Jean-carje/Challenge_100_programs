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
#include <string>

// # functions for each arithmetic operation
double add(double num1, double num2) {
    return num1 + num2;
}
double subtract(double num1, double num2) {
    return num1 - num2;
}
double multiply(double num1, double num2) {
    return num1 * num2;
}
std::string divide(double num1, double num2) {
    if (num1 == 0.0 || num2 == 0.0) {
        return "Error: Invalid input";
    } 
    return std::to_string(num1 / num2);
}
double exponentiation(double base, double exp) {
    return std::pow(base, exp);
}

double root(double num) {
    if (num < 0) {
        return -1.0; // error
    } else {
        return std::sqrt(num);
    }
}

// ---------------------------------------------------
int main() {
    std::cout << "Select an operation:\n";
    std::cout << "1. Add\n";
    std::cout << "2. Subtract\n";
    std::cout << "3. Multiply\n";
    std::cout << "4. Divide\n";
    std::cout << "5. Exponentiation\n";
    std::cout << "6. Root\n";

    std::cout << "Enter your choice (1-6): ";
    int choice;
    std::cin >> choice;

    if (choice == 6) {
        std::cout << "Enter the number: ";
        double num;
        std::cin >> num;
        std::cout << "Result: " << root(num);
    } else if (choice > 6 || choice < 1) {
        std::cout << "Invalid choice";
    } else {
        double num1;
        std::cout << "Enter the first number : ";
        std::cin >> num1;
        double num2;
        std::cout << "Enter the second number : ";
        std::cin >> num2;
        switch (choice) {
            case 1:
                std::cout << "Result: " << add(num1, num2);
                break;
            case 2:
                std::cout << "Result: " << subtract(num1, num2);
                break;
            case 3:
                std::cout << "Result: " << multiply(num1, num2);
                break;
            case 4:
                std::cout << "Result: " << divide(num1, num2);
                break;
            case 5:
                std::cout << "Result: " << exponentiation(num1, num2);
                break;
            default:
                break;
        }
    }
    return 0;

}


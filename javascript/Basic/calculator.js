// # Calculator.js - A simple calculator program
// # Author: Jean Estevez
// # Date: May 6, 2023
// # Language: Javascript
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

// # functions for each arithmetic operation
let add = (num1, num2) => num1 + num2;

let subtract = (num1, num2) => num1 - num2;

let multiply = (num1, num2) => num1 * num2;

let divide = (num1, num2) => {
    if (num1 > 0 && num2 > 0) {
        return num1 / num2;
    } else {
        return "Error: Invalid input"
    }
};

let exponentiation = (base, exp) => base ** exp;

let root = (num) => {
    if (num < 0) {
        return "Error: Imaginary number";
    } else {
        return num ** 0.5;
    }
};

// Código para imprimir
// Pedir al usuario la entrada y realizar la operación seleccionada

console.log(`Select an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponentiation
6. Root`);

let choice = parseInt(prompt("Enter your choice (1-6): "));

if (choice >= 1 && choice <= 4) {
    let num1 = parseFloat(prompt("Enter the first number: "));
    let num2 = parseFloat(prompt("Enter the second number: "));
    if (choice == 1) {
        result = add(num1, num2);
        console.log("Result: ", result);
    } else if (choice == 2) {
        result = subtract(num1, num2);
        console.log("Result: ", result);
    } else if (choice == 3) {
        result = multiply(num1, num2);
        console.log("Result: ", result);
    } else if (choice == 4) {
        result = divide(num1, num2);
        console.log("Result: ", result);
    } else {
        console.log("Invalid choice");
    }
} else if (choice >= 5 && choice <= 6) {
    let num1 = parseFloat(prompt("Enter the number: "));
    if (choice == 5) {
        let num2 = parseFloat(prompt("Enter the exponent number: "));
        result = exponentiation(num1, num2);
        console.log("Result: ", result);
    } else {
        result = root(num1);
        console.log("Result: ", result);
    }
} else {
    console.log("Invalid choice");
}
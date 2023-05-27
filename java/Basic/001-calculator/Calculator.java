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
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Select an operation:");
        System.out.println("1. Add");
        System.out.println("2. Subtract");
        System.out.println("3. Multiply");
        System.out.println("4. Divide");
        System.out.println("5. Exponentiation");
        System.out.println("6. Root");

        System.out.print("Enter your choice (1-6): ");
        int choice = scanner.nextInt();

        if (choice >= 1 && choice <= 5) {
            System.out.print("Enter the first number: ");
            int num1 = scanner.nextInt();
            System.out.print("Enter the second number: ");
            int num2 = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Result: " + add(num1, num2));
                    break;
                case 2:
                    System.out.println("Result: " + subtract(num1, num2));
                    break;
                case 3:
                    System.out.println("Result: " + multiply(num1, num2));
                    break;
                case 4:
                    System.out.println("Result: " + divide(num1, num2));
                    break;
                case 5:
                    System.out.println("Result: " + exponentiation(num1, num2));
                    break;
            }
        } else if (choice == 6) {
            System.out.print("Enter the number: ");
            int num = scanner.nextInt();
            System.out.println("Result: " + root(num));
        } else {
            System.out.println("Invalid choice");
        }
    }

    // Functions for each arithmetic operation

    public static int add(int num1, int num2) {
        return num1 + num2;
    }

    public static int subtract(int num1, int num2) {
        return num1 - num2;
    }

    public static int multiply(int num1, int num2) {
        return num1 * num2;
    }

    public static String divide(int num1, int num2) {
        if (num2 != 0) {
            return Integer.toString(num1 / num2);
        } else {
            return "Error: Division by zero";
        }
    }

    public static double exponentiation(int base, int exp) {
        return Math.pow(base, exp);
    }

    public static double root(int num) {
        return Math.sqrt(num);
    }
}

#include <iostream>

// Function to perform addition
double add(double a, double b) {
    return a + b;
}

// Function to perform subtraction
double subtract(double a, double b) {
    return a - b;
}

// Function to perform multiplication
double multiply(double a, double b) {
    return a * b;
}

// Function to perform division
double divide(double a, double b) {
    if (b != 0) {
        return a / b;
    } else {
        std::cout << "Error: Division by zero is not allowed." << std::endl;
        return 0;
    }
}

int main() {
    int choice;
    double num1, num2, result;
    
    // Display menu
    std::cout << "Select operation:\n";
    std::cout << "1. Addition\n";
    std::cout << "2. Subtraction\n";
    std::cout << "3. Multiplication\n";
    std::cout << "4. Division\n";
    std::cout << "Enter your choice (1-4): ";
    std::cin >> choice;
    
    // Take user input for numbers
    std::cout << "Enter two numbers: ";
    std::cin >> num1 >> num2;
    
    // Perform operation based on user choice
    switch (choice) {
        case 1:
            result = add(num1, num2);
            std::cout << "Result: " << result << std::endl;
            break;
        case 2:
            result = subtract(num1, num2);
            std::cout << "Result: " << result << std::endl;
            break;
        case 3:
            result = multiply(num1, num2);
            std::cout << "Result: " << result << std::endl;
            break;
        case 4:
            result = divide(num1, num2);
            std::cout << "Result: " << result << std::endl;
            break;
        default:
            std::cout << "Invalid choice. Please select a valid option." << std::endl;
    }
    
    return 0;
}


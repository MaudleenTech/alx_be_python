#!/usr/bin/env python3
# This script performs simple arithmetic operations using a match-case statement.

# 1. Prompt for User Input and convert to float (to handle division/decimals)
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit()

# 2. Ask for the operation
operation = input("Choose the operation (+, -, *, /): ")

# 3. Perform the Calculation Using Match Case
# Initialize result variable
result = None

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        # Handle division by zero case gracefully
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
        result = num1 / num2
    case _:
        # Handle invalid operation input
        print("Invalid operation selected.")
        exit()

# 4. Output the Result
if result is not None:
    # Use f-string to display the result
    print(f"The result is {result}.")
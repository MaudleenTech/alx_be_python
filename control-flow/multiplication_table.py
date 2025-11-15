#!/usr/bin/env python3
# This script generates a multiplication table for a number provided by the user.

# 1. Prompt User for a Number and convert to an integer
try:
    number_str = input("Enter a number to see its multiplication table: ")
    number = int(number_str)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# 2. Generate and Print the Multiplication Table using a for loop (1 to 10 inclusive)
# range(1, 11) generates numbers 1, 2, 3, ..., 10.
for i in range(1, 11):
    # Calculate the product
    product = number * i
    
    # Print the result in the specified format: "X * Y = Z"
    # Using an f-string for clear formatting.
    print(f"{number} * {i} = {product}")
#!/usr/bin/env python3
# This script uses nested loops (while and for) to print a square pattern
# of asterisks based on user input size.

# 1. Prompt User for Pattern Size
try:
    size_str = input("Enter the size of the pattern: ")
    size = int(size_str)
    
    # Input validation: ensure size is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
        
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# 2. Draw the Pattern using nested loops

# Outer loop (while loop) controls the rows (height)
row_count = 0
while row_count < size:
    # Inner loop (for loop) controls the columns (width)
    # This loop prints the asterisks side-by-side for the current row
    for col_count in range(size):
        # The end="" prevents a newline, keeping the asterisks on the same line.
        print("*", end="")
    
    # After the inner loop completes (the whole row is drawn), print a newline
    # to move the cursor to the start of the next row.
    print()
    
    # Crucial: Increment the row counter to ensure the while loop terminates
    row_count += 1
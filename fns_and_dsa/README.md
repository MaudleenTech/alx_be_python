ALX Backend Python: Functions, Data Structures, and Modules (fns_and_dsa)

This repository documents my exploration and implementation of core Python fundamentals essential for backend development. The projects within the fns_and_dsa directory focus on Functions, Modules, Data Structures (Lists), and control flow, emphasizing practical application and strict compliance with coding standards.

🧠 Learning Objectives

Upon reviewing this section, a student should be able to:

Modular Programming: Define, separate, and import functions across multiple Python files to build reusable code components.

Data Structures: Apply fundamental list methods (append, remove) and handle real-world list manipulation, including error handling for missing elements.

Variable Scope: Differentiate between global and local variables and effectively use global constants for shared values (e.g., conversion factors).

Standard Library Usage: Utilize key modules like datetime for practical applications, such as date formatting and calculating time differences.

Input Handling & Validation: Implement robust try...except blocks to handle non-numeric input and raise specific errors as required.

🛠 Project Breakdown: Concepts and Implementation

Each task directly targets a specific set of foundational Python concepts.

Task

File

Primary Concept(s)

Key Implementation Details

0

arithmetic_operations.py & main.py

Modularity & Reusability

Separated core logic (arithmetic_operations.py) from execution (main.py). Demonstrated conditional logic (if/elif) for function behavior and error handling (division by zero).

1

shopping_list_manager.py

Lists & Control Flow

Used the Python list as a dynamic data storage structure. Implemented a continuous menu loop (while True) and used list.remove() with try...except ValueError to handle items not found.

2

explore_datetime.py

Python Standard Library (datetime)

Utilized datetime.now() for current time and timedelta for calculating a future date, demonstrating date manipulation and string formatting (strftime).

3

temp_conversion_tool.py

Global Scope & Constants

Defined and accessed global variables (FAHRENHEIT_TO_CELSIUS_FACTOR, CELSIUS_TO_FAHRENHEIT_FACTOR) within local function scope. Demonstrated controlled error raising (raise ValueError).

💻 Code Deep Dive: Implementation Highlights

Task 0: Function & Module Separation

This task showcased how to break a program into logical pieces, which is the foundation of modularity in Python.

# arithmetic_operations.py
def perform_operation(num1, num2, operation):
    # ... logic for add, subtract, multiply
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is not allowed"
        return num1 / num2
    # ...


Task 1: Robust List Management

The shopping_list_manager.py emphasized user experience by providing clear feedback, especially when trying to remove an item that doesn't exist.

# shopping_list_manager.py (Removing an Item)
item_to_remove = input("Enter the item to remove: ").strip()
try:
    shopping_list.remove(item_to_remove)
    print(f"'{item_to_remove}' removed from the list.")
except ValueError:
    print(f"Error: '{item_to_remove}' not found in the list.")


Task 3: Global Variables and Controlled Errors

The temp_conversion_tool.py script provided a clear illustration of using constants defined in the global scope, ensuring conversion factors are consistent across all functions. It also includes the specific error-raising mechanism required for non-numeric input.

# temp_conversion_tool.py (Global Constants and Error Handling)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        try:
            temperature = float(temp_input)
        except ValueError:
            # Mandatory error raise for non-numeric input
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        # ... rest of the conversion logic


🚀 Setup and Execution

Prerequisites

Python 3.x installed.

Running the Scripts

Clone the repository:

git clone https://github.com/MaudleenTech/alx_be_python/tree/main
cd alx_be_python/fns_and_dsa


Execute any script directly:

python3 main.py                 # To test Task 0
python3 shopping_list_manager.py
python3 explore_datetime.py
python3 temp_conversion_tool.py

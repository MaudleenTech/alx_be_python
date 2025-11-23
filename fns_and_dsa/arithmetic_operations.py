# This module contains the perform_operation function for basic arithmetic.

def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation == 'multiply':
        return num1 * num2
    
    elif operation == 'divide':
        if num2 == 0:
            return "Division by zero is not allowed"
        return num1 / num2
    
    else:
        return f"Error: Unsupported operation '{operation}'"
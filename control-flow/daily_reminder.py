#!/usr.bin/env python3
# This script processes a single task's priority and time-sensitivity
# to provide a customized daily reminder.

# 1. Prompt for Task Details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# 2. Process the Task Based on Priority using Match Case
# Determine the core priority description
priority_desc = ""
match priority:
    case 'high':
        priority_desc = "high"
    case 'medium':
        priority_desc = "medium"
    case 'low':
        priority_desc = "low"
    case _:
        priority_desc = "unlisted"

# Start building the final reminder string structure
reminder_message = f"Reminder: '{task}' is a {priority_desc} priority task"

# 3. Modify the Reminder Based on Time Sensitivity using an if statement
if time_bound == 'yes':
    # Append the required time-sensitive message directly
    reminder_message += " that requires immediate attention today!"

# 4. Output the Customized Reminder
print(reminder_message)

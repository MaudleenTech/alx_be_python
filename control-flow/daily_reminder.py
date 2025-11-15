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
        # Use the input priority if unlisted, for flexibility
        priority_desc = priority

# 3. Determine Final Output Message based on time sensitivity
if time_bound == 'yes':
    # Output for time-bound tasks (starts with 'Reminder: ')
    final_message = (
        f"Reminder: '{task}' is a {priority_desc} priority task"
        " that requires immediate attention today!"
    )
else:
    # Output for non-time-bound tasks (starts with 'Note: ')
    final_message = (
        f"Note: '{task}' is a {priority_desc} priority task."
        " Consider completing it when you have free time."
    )

# 4. Output the Customized Reminder
print(final_message)

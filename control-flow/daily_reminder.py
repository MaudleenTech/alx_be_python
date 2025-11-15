#!/usr/bin/env python3
# This script processes a single task's priority and time-sensitivity
# to provide a customized daily reminder.

# 1. Prompt for Task Details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize the base reminder message
base_reminder = ""

# 2. Process the Task Based on Priority using Match Case
match priority:
    case 'high':
        base_reminder = f"'{task}' is a high priority task"
    case 'medium':
        base_reminder = f"'{task}' is a medium priority task"
    case 'low':
        base_reminder = f"'{task}' is a low priority task"
    case _:
        # Handle unexpected priority input
        base_reminder = f"'{task}' has an unlisted priority"

# 3. Modify the Reminder Based on Time Sensitivity using an if statement
if time_bound == 'yes':
    # Append the required time-sensitive message
    final_reminder = f"Reminder: {base_reminder} that requires immediate attention today!"
else:
    # Append a standard closing phrase for non-time-bound or unlisted priority tasks
    final_reminder = f"Reminder: {base_reminder}. Consider completing it soon."

# 4. Output the Customized Reminder
print(final_reminder)
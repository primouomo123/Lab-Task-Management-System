from datetime import datetime

# Import validation functions
from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    task = {"title": title, "description": description, "due_date": due_date, "completed": False}

    try:
        validate_task_title(task["title"])
        validate_task_description(task["description"])
        validate_due_date(task["due_date"])
        tasks.append(task)
        print("Task added successfully!")
    except ValueError as e:
        print(f"Error adding task: {e}")
        return
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if not tasks:
        print("No tasks available.")
        return
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    if not tasks:
        return []
    pending_tasks = [task for task in tasks if not task["completed"]]
    return pending_tasks

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0
    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / len(tasks)) * 100
    return progress
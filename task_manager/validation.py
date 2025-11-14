from datetime import datetime

def validate_task_title(title):
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters.")
    if len(title) > 100:
        raise ValueError("Title must not exceed 100 characters.")
    
def validate_task_description(description):
    description = description.strip()
    if not description:
        raise ValueError("Task description cannot be empty.")
    if len(description) < 10:
        raise ValueError("Description must be at least 10 characters.")
    if len(description) > 500:
        raise ValueError("Description must not exceed 500 characters.")   
    
def validate_due_date(due_date):
    due_date = due_date.strip()
    if not due_date:
        raise ValueError("Due date cannot be empty.")
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")
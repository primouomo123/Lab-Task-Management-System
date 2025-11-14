# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title:\n")
            description = input("Enter task description:\n")
            due_date = input("Enter due date (YYYY-MM-DD):\n")

            add_task(title, description, due_date)

        elif choice == "2":
            index = int(input("Enter task index to mark as complete:\n"))
            mark_task_as_complete(index)
        
        elif choice == "3":
            pending_tasks = view_pending_tasks()
            if not pending_tasks:
                print("No pending tasks.")
            else:
                for i, task in enumerate(pending_tasks):
                    print(f"{i}. Title: {task['title']}, Description: {task['description']}, Due Date: {task['due_date']}")
        
        elif choice == "4":
            progress = calculate_progress()
            print(f"Progress: {progress:.1f}% complete")
            
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()

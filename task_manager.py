import sys

class Task:
    """
    A class to represent a task in the task management system.
    
    Attributes:
        title (str): The title of the task.
        level (str): Priority level of the task (1-5).
        deadline (str): Deadline for the task in YYYY-MM-DD format.
        is_done (bool): Completion status of the task.
    """

    def __init__(self, title: str, level: str, deadline: str, is_done: bool = False):
        """
        Initializes a new Task object.

        Args:
            title (str): Task title.
            level (str): Task priority level (1-5).
            deadline (str): Task deadline in YYYY-MM-DD format.
            is_done (bool): Task completion status (default is False).
        """
        self.title = title
        self.level = level
        self.deadline = deadline
        self.is_done = is_done

    def mark_done(self):
        """Marks the task as completed."""
        self.is_done = True

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the task.

        Returns:
            dict: Task details.
        """
        return {
            'Title': self.title,
            'Level': self.level,
            'Deadline': self.deadline,
            'Completed': 'Yes' if self.is_done else 'No'
        }

def view_tasks(tasks: list):
    """
    Displays all tasks in the list.

    Args:
        tasks (list): List of Task objects.
    """
    if not tasks:
        print("No tasks to display.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks, start=1):
        task_info = task.to_dict()
        print(f"{i}. Title: {task_info['Title']}, Level: {task_info['Level']}, Deadline: {task_info['Deadline']}, Completed: {task_info['Completed']}")

def add_task(tasks: list):
    """
    Prompts user to add a new task and appends it to the list.

    Args:
        tasks (list): List of Task objects.
    """
    title = input("Enter task title: ")
    level = input("Enter task level (1-5): ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    new_task = Task(title, level, deadline)
    tasks.append(new_task)
    print("Task added!")

def mark_task_done(tasks: list):
    """
    Marks a selected task as done based on user input.

    Args:
        tasks (list): List of Task objects.
    """
    if not tasks:
        print("No tasks available to mark as done.")
        return
    view_tasks(tasks)
    try:
        task_index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index].mark_done()
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task(tasks: list):
    """
    Deletes a selected task based on user input.

    Args:
        tasks (list): List of Task objects.
    """
    if not tasks:
        print("No tasks available to delete.")
        return
    view_tasks(tasks)
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    """
    Main function that runs the task management loop.
    """
    tasks = []

    while True:
        print("\n=== Task Manager Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()

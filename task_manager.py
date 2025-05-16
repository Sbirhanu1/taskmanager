import sys

class Task:
    def __init__(self, title, level, deadline, is_done=False):
        self.title = title
        self.level = level
        self.deadline = deadline
        self.is_done = is_done

    def mark_done(self):
        self.is_done = True

    def to_dict(self):
        return {
            'Title': self.title,
            'Level': self.level,
            'Deadline': self.deadline,
            'Completed': 'Yes' if self.is_done else 'No'
        }

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    for task in tasks:
        task_info = task.to_dict()
        print(f"Title: {task_info['Title']}, Level: {task_info['Level']}, Deadline: {task_info['Deadline']}, Completed: {task_info['Completed']}")

def add_task(tasks):
    title = input("Enter task title: ")
    level = input("Enter task level (1-5): ")
    deadline = input("Enter task deadline (YYYY-MM-DD): ")
    new_task = Task(title, level, deadline)
    tasks.append(new_task)
    print("Task added!")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index].mark_done()
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = []
    
    while True:
        print("\n1. View Tasks")
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

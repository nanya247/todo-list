import json

tasks = []


def add_task(name, due_date="", priority="Low"):
    task = {"name": name, "due_date": due_date, "priority": priority, "completed": False}
    tasks.append(task)
    save_tasks()


def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['name']} - Due: {task['due_date']} - Priority: {task['priority']} - Status: {status}")

def delete_task(index):
    if 1 <= index <= len(tasks):
        tasks.pop(index - 1)
        save_tasks()
    else:
        print("Invalid task index.")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def main():
    load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Task name: ")
            due_date = input("Due date (optional, e.g., 2025-05-25): ")
            priority = input("Priority (optional, e.g., High, Medium, Low): ")
            add_task(name, due_date, priority)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = int(input("Enter the task number to delete: "))
            delete_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


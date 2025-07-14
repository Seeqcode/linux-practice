import os

todo_file = "tasks.txt"  # File where tasks will be saved

def show_tasks():
    if os.path.exists(todo_file):
        with open(todo_file, "r") as f:
            tasks = f.readlines()
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\nNo tasks yet.")
    else:
        print("\nNo tasks file found.")

def add_task():
    task = input("Enter a new task: ")
    with open(todo_file, "a") as f:
        f.write(task + "\n")
    print("✅ Task added!")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        with open(todo_file, "r") as f:
            tasks = f.readlines()
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            with open(todo_file, "w") as f:
                f.writelines(tasks)
            print(f"🗑️ Task deleted: {removed.strip()}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a number.")

def menu():
    while True:
        print("\n[1] View tasks\n[2] Add task\n[3] Delete task\n[4] Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Bye! 👋")
            break
        else:
            print("❌ Invalid option. Try again.")

menu()

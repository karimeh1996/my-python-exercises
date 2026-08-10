# To-Do List Manager
tasks = []

while True:
    print("\n" + "="*30)
    print("📋 TO-DO LIST MENU:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Exit")
    print("="*30)

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        new_task = input("Enter a new task: ")
        if new_task.strip() == "":
            print("❌ Task cannot be empty.")
        else:
            tasks.append(new_task)
            print(f"✅ Task '{new_task}' added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("📭 The task list is empty.")
        else:
            print("\n📌 Your tasks:")
            number = 1
            for task in tasks:
                print(f"{number}. {task}")
                number += 1

    elif choice == "3":
        if len(tasks) == 0:
            print("📭 There are no tasks to remove.")
        else:
            print("\n📌 Your tasks:")
            number = 1
            for task in tasks:
                print(f"{number}. {task}")
                number += 1

            task_number = input("Enter the number of the task to remove: ")

            if task_number.isdigit():
                index = int(task_number) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print(f"✅ Task '{removed_task}' successfully removed.")
                else:
                    print("❌ Invalid number.")
            else:
                print("❌ Please enter a valid number.")

    elif choice == "4":
        print("👋 Have a nice day.")
        break

    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

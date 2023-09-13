tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")
    elif choice == '2':
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice")

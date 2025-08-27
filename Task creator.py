tasks = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    print("\nOptions: add / remove / quit")
    choice = input("What do you want to do? ")

    if choice == "add":
        task = input("Enter a new task: ")
        tasks.append(task)
    elif choice == "remove":
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
    elif choice == "quit":
        break
    else:
        print("Invalid option")

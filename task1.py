
# Initialize an empty to-do list
todo_list = []

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f'"{task}" has been added to your to-do list.')

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f'"{removed_task}" has been removed from your to-do list.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
# Initialize an empty to-do list with a dictionary to store tasks and their status
todo_list = {}

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Mark task as completed")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list[task] = False
    print(f'"{task}" has been added to your to-do list.')

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, (task, completed) in enumerate(todo_list.items(), start=1):
            status = "Completed" if completed else "Not Completed"
            print(f"{i}. {task} - {status}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the number of the task to remove: "))
            if 1 <= task_number <= len(todo_list):
                tasks = list(todo_list.keys())
                removed_task = tasks[task_number - 1]
                del todo_list[removed_task]
                print(f'"{removed_task}" has been removed from your to-do list.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_task_completed():
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the number of the task to mark as completed: "))
            if 1 <= task_number <= len(todo_list):
                tasks = list(todo_list.keys())
                task = tasks[task_number - 1]
                todo_list[task] = True
                print(f'"{task}" has been marked as completed.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    display_menu()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        mark_task_completed()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

        

#output
'''To-Do List Menu:
1. Add a task
2. View tasks
3. Remove a task
4. Exit
Choose an option (1-4): 1
Enter the task: name
"name" has been added to your to-do list.

To-Do List Menu:
1. Add a task
2. View tasks
3. Remove a task
4. Exit
Choose an option (1-4): 2

Your To-Do List:
1. name

To-Do List Menu:
1. Add a task
2. View tasks
3. Remove a task
4. Exit
Choose an option (1-4): 3

Your To-Do List:
1. name

Enter the number of the task to remove: 4
Invalid task number.

To-Do List Menu:
1. Add a task
2. View tasks
3. Remove a task
4. Exit
Choose an option (1-4):'''
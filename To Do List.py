# To-do List
print("Welcome to the To-Do List App!\n")

def main_menu():
    print("[1] [Add] a task")
    print("[2] [View] tasks")
    print("[3] [Mark] a task as complete")
    print("[4] [Del]ete a task")
    print("[5] [Quit]")

    response = input().lower()
    if response == "1" or "add" in response:
        add_task()
    elif response == "2" or "view" in response:
        view_tasks(True)
    elif response == "3" or "mark" in response:
        mark_task()
    elif response == "4" or "del" in response:
        delete_task()
    elif response == "5" or "quit" in response:
        quit_app()
    else:
        print("Input not recognized. Please enter a number or word seen in [brackets]!")

def add_task():
    print("Task added")

def view_tasks(display_msg):
    if display_msg:
        print("Viewing all tasks:")
    
def mark_task():
    print("Which task would you like to toggle complete status of?")
    view_tasks(False)
    
def delete_task():
    print("Which task would you like to delete?")
    view_tasks(False)
    print("Task deleted")
    
def quit_app():
    print("Thank you for using the To-Do app!")
    exit()
    
def add_task():
    print("Task added")

while True:
    main_menu()
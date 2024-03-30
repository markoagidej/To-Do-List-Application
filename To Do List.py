# To-do List

import datetime

print("Welcome to the To-Do List App!\n")
todo_list = []

STATS_INDEX         = 0
DESCRIPTION_INDEX   = 1
DATE_CREATED_INDEX  = 2
DATE_DUE_INDEX      = 3

status_list = [
    "RED",
    "YELLOW",
    "GREEN"
]

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
    description = set_description()
    priority = set_priority()
    status =  set_status()
    date_due = set_date()
    date_created = datetime.datetime.now()


    new_task = [
        status,
        description,
        date_created,
        date_due
    ]

    todo_list.insert(priority, new_task)
    
    print("Task added")

def view_tasks(display_msg):
    if todo_list:
        if display_msg:
            print("Viewing all tasks:")
        counter = 1
        for task in todo_list:
            print(f"{counter}. {task[STATS_INDEX]} | {task[DESCRIPTION_INDEX]} | Created: {task[DATE_CREATED_INDEX]} | {task[DATE_DUE_INDEX]}")
            counter += 1
    else:
        print("You do not have any tasks yet!")
    
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

def set_description():
    return input("Enter a description for your task:\n")
    
def set_priority():
    while True:
        if todo_list:
            priority = input("Enter a priority number from 1-" + str(len(todo_list) + 1) + ", or hit ENTER to add to end of list.\n")
            if priority > len(todo_list) + 1:
                print("That priority number is larger than the number of tasks you have on the list!")
                continue
            else:
                return priority
        else:
            return 0

def set_status():
    return input("Enter a status for this task (RED/YELLOW/GREEN), or hit ENTER to default to RED.\n")

def set_date():
    return input("Enter a Due Date or Other Note.\n")

while True:
    main_menu()
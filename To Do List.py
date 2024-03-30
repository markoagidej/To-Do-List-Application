# To-do List

import datetime

print("Welcome to the To-Do List App!\n")
todo_list = []

##ENUMs and Constants
TASK_INDEX_STATUS       = 0
TASK_INDEX_DESCRIPTION  = 1
TASK_INDEX_DATE_CREATED = 2
TASK_INDEX_DATE_DUE     = 3

STATUS_INDEX_RED    = 0
STATUS_INDEX_YELLOW = 1
STATUS_INDEX_GREEN  = 2

STATUS_LIST = [
    "RED   ",
    "YELLOW",
    "GREEN "
]

## Main menu (First to run)
def main_menu():
    print("[1] [Add] a task")
    print("[2] [View] tasks")
    print("[3] [Status] Update")
    print("[4] [Delete] a task")
    print("[5] [Quit]")

    response = input().lower()
    if response == "1" or "add" in response:
        add_task()
    elif response == "2" or "view" in response:
        view_tasks(True)
    elif response == "3" or "status" in response:
        change_status_task()
    elif response == "4" or "delete" in response:
        delete_task()
    elif response == "5" or "quit" in response:
        quit_app()
    else:
        print("Input not recognized. Please enter a number or word seen in [brackets]!")

## Main menu functions
def add_task():
    description = set_description()
    priority = set_priority()
    status =  set_status(True)
    date_due = set_date()
    date_created = datetime.datetime.now()


    new_task = [
        status,
        description,
        date_created,
        date_due
    ]

    todo_list.insert(priority, new_task)
    
    print(f"Task {description} added")

def view_tasks(display_msg):
    if todo_list:
        if display_msg:
            print("Viewing all tasks:")
        counter = 1
        for task in todo_list:
            print(f"{counter}. {task[TASK_INDEX_STATUS]} | {task[TASK_INDEX_DESCRIPTION]} | Created: {task[TASK_INDEX_DATE_CREATED]} | {task[TASK_INDEX_DATE_DUE]}")
            counter += 1
    else:
        print("You do not have any tasks yet!")
    
def change_status_task():
    print("Which task number would you like to update the status of?")
    view_tasks(False)
    task_num = input()
    set_status(False, task_num)
    
def delete_task():
    print("Which task would you like to delete?")
    view_tasks(False)
    to_delete_priority = input()
    try:
        to_delete_number = int(to_delete_priority)
    except:
        print("Input must be a number within the range of tasks currently on the list (" + get_list_range() + ")")

    
def quit_app():
    print("Thank you for using the To-Do app!")
    exit()

##Setting values within Tasks
def set_description():
    while True:
        description = input("Enter a description for your task:\n")
        if description:
            return description
        else:
            print("You must input something for description!")
    
def set_priority():
    while True:
        if todo_list:
            priority = input("Enter a priority number from " + get_list_range() + ", or hit ENTER to add to end of list.\n")
            if priority:
                try:
                    priority = int(priority)
                    if priority > len(todo_list):
                        print("That priority number is larger than the number of tasks you have on the list!")
                        continue
                    else:
                        return priority - 1
                except: # input is not a number withing range of list items
                    print("Input must be a number within the range of tasks currently on the list (" + get_list_range() + ")")
            else: # if no input given, set ot last index
                return len(todo_list)
        else: # if todo_list is empty skip all logic and isert at first index
            return 0

def set_status(new_task, task_priority = -1):
    if new_task:
        while True:
            status = input("Enter a status for this task [RED/YELLOW/GREEN], or hit ENTER to default to RED.\n")
            if status.upper() == "RED":
                return STATUS_LIST[STATUS_INDEX_RED]
            elif status.upper() == "YELLOW":
                return STATUS_LIST[STATUS_INDEX_YELLOW]
            elif status.upper() == "GREEN":
                return STATUS_LIST[STATUS_INDEX_GREEN]
            else:
                if status:
                    print("Input must be [RED],[YELLOW], or [GREEN].")
                else:
                    return STATUS_LIST[STATUS_INDEX_RED]

    else:
        try:
            task_number = int(task_priority)
            if task_number >= 1 and task_number <= len(todo_list):
                while True:
                    status = input("Enter a status for this task [RED/YELLOW/GREEN], or [+]/[-] to move status forward or backward\n")                    
                    if status.upper() == "RED":
                        todo_list[task_number][TASK_INDEX_STATUS] = STATUS_LIST[STATUS_INDEX_RED]
                        print(f"Status of priority task {task_number} set to RED")
                        break
                    elif status.upper() == "YELLOW":
                        todo_list[task_number][TASK_INDEX_STATUS] = STATUS_LIST[STATUS_INDEX_YELLOW]
                        print(f"Status of priority task {task_number} set to YELLOW")
                        break
                    elif status.upper() == "GREEN":
                        todo_list[task_number][TASK_INDEX_STATUS] = STATUS_LIST[STATUS_INDEX_GREEN]
                        print(f"Status of priority task {task_number} set to GREEN")
                        break
                    elif status == "+":
                        if todo_list[task_number][TASK_INDEX_STATUS] == STATUS_LIST[STATUS_INDEX_RED]:
                            todo_list[task_number][TASK_INDEX_STATUS] = STATUS_LIST[STATUS_INDEX_YELLOW]
                            print(f"Status of priority task {task_number} set to YELLOW")
                            break
                        elif todo_list[task_number][TASK_INDEX_STATUS] == STATUS_LIST[STATUS_INDEX_YELLOW]:
                            todo_list[task_number][TASK_INDEX_STATUS] = STATUS_LIST[STATUS_INDEX_GREEN]
                            print(f"Status of priority task {task_number} set to GREEN")
                            break
                        else: # todo_list[task_number][TASK_INDEX_STATUS] == STATUS_LIST[STATUS_INDEX_GREEN]                            
                            print(f"Status of priority task {task_number} can not be moved further ahead than its current status: GREEN")
                    elif status == "-":
                        if todo_list[task_number][TASK_INDEX_STATUS] == STATUS_LIST[STATUS_INDEX_GREEN]:
                            todo_list[task_number][TASK_INDEX_STATUS] = STATUS_LIST[STATUS_INDEX_YELLOW]
                            print(f"Status of priority task {task_number} set to YELLOW")
                            break
                        elif todo_list[task_number][TASK_INDEX_STATUS] == STATUS_LIST[STATUS_INDEX_YELLOW]:
                            todo_list[task_number][TASK_INDEX_STATUS] = STATUS_LIST[STATUS_INDEX_RED]
                            print(f"Status of priority task {task_number} set to RED")
                            break
                        else: # todo_list[task_number][TASK_INDEX_STATUS] == STATUS_LIST[STATUS_INDEX_RED]                            
                            print(f"Status of priority task {task_number} can not be moved further back than its current status: RED")
                    else: # Bad input
                        print("Input must be [RED],[YELLOW], or [GREEN].")
            else: # task_number is number but below or above rang of task list
                print("Input must be within the range of tasks currently on the list (" + get_list_range() + ")")
        except: # ERROR for non-number input
            print("Input must be a number within the range of tasks currently on the list (" + get_list_range() + ")")

def set_date():
    return input("Enter a Due Date or Other Note.\n")

## Utility functions
def get_list_range():
    if len(todo_list) == 1:
        return "1"
    else:
        return "1-" + str(len(todo_list))

while True:
    main_menu()
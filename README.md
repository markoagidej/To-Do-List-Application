# To-do List app

## Overview:

This is an app for keeping track of a list of tasks!

Each task you add to the list will have up to 5 attributes as follows:
    Description
    Priority
    Completion Status
    Create Date
    Due Date

Description is the only attribute you must input something for.

Priority determines the order of the list. If you do not enter a value here, the task will automatically go to the bottom of the list and be assigned the appropriate priority number.

Completion Status will be represented with a color. GREEN = Done, YELLOW = WIP, RED = Unstarted. If you do not enter a value, it will default to Red.

Create date is automatically created!

Due Date is more of a note to your self. Enter whatever format date you prefer using (Though you could just enter any note here to yourself!). If you do not enter a value, this will be empty.


This To-Do app has the following functions:
    1. Adding Tasks
    2. Viewing Tasks
    3. Changing Status
    4. Deleting Tasks
    5. Qutting the app

## How to use:

Once you run the program you will see a list of 5 actions you can perform and will be prompted to choose an action.
Each action is designated with a number and a key-word in brackets[]. Type an option in brackets and press ENTER to perform the associated action.

### 1. Adding Tasks
    Add a task to the list!

    You will be promted to enter a description for the task.
    The Create Date will be automatically created for you!
    Then you will be prompted to add a Priority, Status, and Due Date.

### 2. Viewing Tasks
    This will display the entire list of tasks and their associated attributes in order of priority

### 3. Change Status
    This option will let you toggle the completion status of a task.

    First you will be prompted to select a task from your list.
    Then you will choose a status for the task, GREEN, YELLOW, or RED.
    You can manually enter the color you would like, or use a shortcut!
    Since the colors are meant to represent the stages of a task, they have a natural progression as follows:
            RED     ->        Yellow       ->   GREEN
        (unstarted)     (work-in-progress)     (done)
    You can simply type '+' or '-' to move the status one step forward or backward.
    For example, if you are just starting work on a task (Going from RED to YELLOW), type '+' and ENTER, and the task will have its status changed from RED to YELLOW!
    Alternatively, if you thought a task was done, but you need to work on it again, type '-' and ENTER. The task will change from GREEN to YELLOW!

### 4. Deleting Tasks
    Remove a task from the list!

    Select a task from the list to remove. All tasks after the deleted one will automatically move up in priority!

### 5. Qutting the app
    Quit the app

    Self-explanatory. Thanks for using my app!
from taskmanager import Taskmanager
from user import User
from task import Task


def update_task(task_manager):
    task_id = int(
        input("\nPlease enter task id you want to update: "))
    print(
        "If you don't want to update any field keep it blank or else update it")
    task_name = input("Update task name: ")
    due_date = input("Update due date: ")
    print("Priority levels")
    print("0 -> Low ")
    print("1 -> High ")
    lvl = input("Select priority level: ")
    if lvl != "":
        lvl = int(lvl)
    priority = ""
    if lvl == 0:
        priority = "low"
    elif lvl == 1:
        priority = "high"
    task_manager.update_user_task(
        task_id, task_name=task_name, due_date=due_date, priority=priority)


def add_task(task_manager):
    print("\nPlease follow the steps below to add a new task!!")
    task_name = input("Enter task name: ")
    due_date = input("Enter due date: ")
    print("Priority levels")
    print("0 -> Low ")
    print("1 -> High ")
    lvl = int(input("Select priority level: "))
    priority = "low"
    if lvl == 0:
        priority = "low"
    elif lvl == 1:
        priority = "high"
    else:
        print("Wrong input priority level set to 0")
    task_manager.add_user_task(
        Task(task_name=task_name, due_date=due_date, priority=priority))


def runSystem():
    print("<--- Welcome to the task manager --->")
    while True:
        print("Please select an option")
        print("1. Create profile to use task manager")
        print("2. exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:

            name = input("Please enter your name: ")
            task_manager = Taskmanager(User(name))

            while True:
                print(f"""\n<--- {name.capitalize()
                                  } Welcome to task manager ---> """)
                print("Tell us what do you want to do!!")
                print("1. Add task?")
                print("2. View all task?")
                print("3. update any task?")
                print("4. Delete any task?")
                print("5. Sort your task by priority?")
                print("6. Sort your task by due date?")
                print("7. Delete your profile?")
                print("8. View pending task")
                print("9. View completed task")
                print("10. Completed a task?")
                print("11. Exit")

                cmd = int(input("Please select your option: "))
                if cmd == 1:  # add task
                    add_task(task_manager)
                elif cmd == 2:
                    task_manager.view_user_task("all")
                elif cmd == 3:
                    update_task(task_manager)
                elif cmd == 4:
                    task_id = int(
                        input("\nEnter task id you want to delete: "))
                    task_manager.delete_user_task(task_id=task_id)
                elif cmd == 5:
                    task_manager.sort_user_task_by_priority()
                    task_manager.view_user_task("all")
                elif cmd == 6:
                    task_manager.sort_task_by_due_date()
                    task_manager.view_user_task("all")
                elif cmd == 7:
                    task_manager.delete_profile()
                    break
                elif cmd == 8:
                    task_manager.view_user_task("pending")
                elif cmd == 9:
                    task_manager.view_user_task("completed")
                elif cmd == 10:
                    task_id = int(input("Please enter a valid task id: "))
                    task_manager.update_user_task(
                        task_id, status="completed")
                else:
                    break

        elif ch == 2:
            break
        else:
            print("Invalid input")


runSystem()

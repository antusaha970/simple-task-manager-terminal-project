from task import Task
from datetime import datetime


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.taskList = []  # list of task object #{1:task}

    def add_task(self, task):
        id = len(self.taskList)+1
        self.taskList.append({id: task})
        print("New task added!!")

    def view_task(self, status=None):
        print("\t<---- Your Tasks ---->")
        print(f"id\ttask name\tdue date\tpriority\tstatus")
        for task_dict in self.taskList:
            for k, v in task_dict.items():
                if status == "pending" and v.status == "pending":
                    print(f"""{k}\t{v.task_name}\t{
                        v.due_date}\t{v.priority}\t{v.status}""")
                elif status == "completed" and v.status == "completed":
                    print(f"""{k}\t{v.task_name}\t{
                        v.due_date}\t{v.priority}\t{v.status}""")
                else:
                    print(f"""{k}\t{v.task_name}\t{
                        v.due_date}\t{v.priority}\t{v.status}""")

    def update_task(self, task_id, **kwargs):
        for task_dict in self.taskList:
            for id, val in task_dict.items():
                if task_id == id:
                    val.update_task(**kwargs)
        print("Task updated")

    def delete_task(self, task_id):
        for task in self.taskList:
            for k, _ in task.items():
                if k == task_id:
                    self.taskList.remove(task)
                    print(f"""Task removed""")

    def sort_task_by_priority(self):
        def sort_parameter(task_dict):
            for k, v in task_dict.items():
                if v.priority.lower() == "high":
                    return False
            return True
        self.taskList.sort(key=sort_parameter)
        print("Your tasks has been sorted by priority")

    def sort_task_by_due_date(self):
        def sort_parameter(task_dict):
            for k, v in task_dict.items():
                return v.due_date
        self.taskList.sort(key=sort_parameter)
        print("Your tasks has been sorted by date")

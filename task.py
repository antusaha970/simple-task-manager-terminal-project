from datetime import datetime


class Task:
    def __init__(self, task_name, due_date, priority) -> None:
        self.task_name = task_name
        self.due_date = due_date
        self.priority = priority  # low,high
        self.status = "pending"  # pending or completed
        self.creation_date = datetime.now().date().strftime("%d/%m/%y")  # 22/04/24

    def update_task(self, **kwargs):
        for key, val in kwargs.items():
            if key == "task_name":
                if val != "":
                    self.task_name = val
            elif key == "due_date":
                if val != "":
                    self.due_date = val
            elif key == "priority":
                if val != "":
                    self.priority = val
            elif key == "status":
                if val != "":
                    self.status = val

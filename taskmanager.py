
class Taskmanager:
    all_users = []

    def __init__(self, user) -> None:
        self.user = user  # user class object

    def change_user(self, user):
        self.user = user

    def add_user_task(self, task):  # accept task object
        self.user.add_task(task)

    def view_user_task(self, status=None):
        self.user.view_task(status)

    def update_user_task(self, task_id, **kwargs):
        self.user.update_task(task_id, **kwargs)

    def delete_user_task(self, task_id):
        self.user.delete_task(task_id)

    def sort_user_task_by_priority(self):
        self.user.sort_task_by_priority()

    def sort_task_by_due_date(self):
        self.user.sort_task_by_due_date()

    def delete_profile(self):
        self.user = None
        print("Your profile has been deleted")

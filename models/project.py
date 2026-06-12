from .task import Task

class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_complete()
                return True
        
        return False
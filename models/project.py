from .task import Task

class Project(Task):
    id_counter = 1

    def __init__(self, owner_id, title, description, due_date, project_id=None):
        if project_id is None:
            self.id = Project.id_counter
            Project.id_counter += 1
        else:
            self.id = project_id
            Project.id_counter = max(
                Project.id_counter,
                project_id + 1
            )
        
        super().__init__(title)
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
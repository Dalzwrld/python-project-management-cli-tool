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

    def to_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["owner_id"],
            data["title"],
            data["description"],
            data["due_date"],
            data["id"]
        )

    def __str__(self):
        return f"{self.id}: {self.title}"
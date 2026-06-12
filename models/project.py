class Project():
    id_counter = 1

    def __init__(self, owner_id, title, description, due_date, project_id=None):
        if project_id is None:
            self.id = Project.id_counter
            Project.id_counter += 1
        else:
            self.id = project_id
            Project.id_counter = max(Project.id_counter, project_id + 1)
        
        self.owner_id = owner_id
        self.title = title
        self.description = description
        self.due_date = due_date

    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date
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
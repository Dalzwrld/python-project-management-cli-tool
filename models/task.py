class Task:
    id_counter = 1

    def __init__(
        self,
        project_id,
        title,
        assigned_to,
        status="Pending",
        task_id=None
    ):

        if task_id is None:
            self.id = Task.id_counter
            Task.id_counter += 1
        else:
            self.id = task_id
            Task.id_counter = max(
                Task.id_counter,
                task_id + 1
            )

        self.project_id = project_id
        self.title = title
        self.assigned_to = assigned_to
        self.status = status

    def mark_complete(self):
        self.status = "Completed"

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
            data["project_id"],
            data["title"],
            data["assigned_to"],
            data["status"],
            data["id"]
        )

    def __str__(self):
        return f"{self.id}: {self.title} [{self.status}]"
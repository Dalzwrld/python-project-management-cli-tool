class Task:
    def __init__(self, title, assigned_to=None):
        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"

    def mark_complete(self):
        self.status = "Complete"

    def to_dict(self):
        return {
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status
        }
class Task:
    def __init__(self, title, assigned_to=None):
        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"
from .person import Person
import re

class User(Person):
    id_counter = 1
    def __init__(self, name, email):
        super().__init__(name, email)

        self.id = User.id_counter
        User.id_counter += 1

        self.projects = []
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not re.match(email_pattern, value):
            raise ValueError("Invalid email format.")

    def add_project(self, project):
        self.projects.append(project)

    def __str__(self):
        return f"{self.name} ({self.email})"
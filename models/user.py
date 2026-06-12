from .person import Person
import re

class User(Person):
    all_users = []

    id_counter = 1
    def __init__(self, name, email, user_id=None):
        super().__init__(name, email)

        if user_id is None:
            self.id = User.id_counter
            User.id_counter += 1
        else:
            self.id = user_id
            User.id_counter += 1

        self.projects = []

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["email"],
            data["id"]
        )
    
    def to_dict(self):
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not re.match(email_pattern, value):
            raise ValueError("Invalid email format.")
        
        self._email = value

    def add_project(self, project):
        self.projects.append(project)

    def __str__(self):
        return f"{self.name} ({self.email})"
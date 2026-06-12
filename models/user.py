from person import Person

class User(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
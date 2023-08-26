class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # toString
    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\n'

    # Other methods and attributes
    def get_name(self):
        return self.name

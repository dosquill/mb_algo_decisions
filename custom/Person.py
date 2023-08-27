class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # toString
    def __str__(self):
        return f'Name: {self.name}\nSurname: {self.surname}\n'


    # GETTERS
    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    

    # SETTERS
    def set_name(self, name):
        self.name = name
    
    def set_surname(self, surname):
        self.surname = surname


    # OTHER METHODS
    def copy(self):
        return Person(self.name, self.surname)
    

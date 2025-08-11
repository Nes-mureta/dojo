# models.py
class Room:
    def __init__(self, name):
        self.name = name
        self.occupants = []
    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}) (capacity: {self.capacity})occupants: {len(self.occupants)})"
        
class Office(Room):
    capacity = 6
    
class LivingSpace(Room):
    capacity = 4

class Person:
    def __init__(self, name):
        self.name = name
        self.first_name = name.split()[0]
        
    def __str__(self):
        return f"{self.__class__.__name__}:{self.name} "
        
class Staff(Person):
    pass

class Fellow(Person):
    def __init__(self, name, wants_living_space='NO'):
        super().__init__(name)
        self.wants_living_space = wants_living_space.upper() == 'YES'
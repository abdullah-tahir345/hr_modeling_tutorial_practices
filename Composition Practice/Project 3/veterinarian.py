
class Veterinarian:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        
    def treat_animal(self, animal):
        print(f'{self.name} is treating {animal.name} ({animal.species}).')
        
        
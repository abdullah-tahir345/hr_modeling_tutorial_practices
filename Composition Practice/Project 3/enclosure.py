
class Enclosure:
    def __init__(self, capacity, environmental_conditions):
        self.capacity = capacity
        self.environmental_conditions = environmental_conditions
        self.animals = []
        
    def add_animal(self, animal):
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
            print(f'Animal {animal.name} has been added to the enclosure.')
        else:
            print("Enclosure is full. Can't add more animals.")
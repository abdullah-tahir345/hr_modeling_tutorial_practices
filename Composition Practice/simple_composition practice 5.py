class Animal:
    def __init__(self, species, sound, color):
        self.species = species
        self.sound = sound
        self.color = color
        
    def display_info(self):
        print(f'Species : {self.species}')
        print(f'Sound : {self.sound}')
        print(f'Color : {self.color}')
        
        
class AnimalCategory:
    def __init__(self, category_name):
        self.category_name = category_name
        self.animals = []
        
    def add_animal(self, animal_object):
        self.animals.append(animal_object)
        
    def display_category_info(self):
        print(f'Category : {self.category_name}')
        print('-------------------------------')
        for animal in self.animals:
            animal.display_info()
            print()

class Zoo:
    def __init__(self):
        self.categories = []
        
    def add_categories(self, category):
        self.categories.append(category)
        
    def display_zoo_info(self):
        print('Zoo Information : ')
        print('------------------')
        for category in self.categories:
            category.display_category_info()
            print()
            
            
lion = Animal('Lion', 'Roar', 'Yellow')
zebra = Animal('Zebra', 'Bray', 'Zig Zag Black White')

mammals_category = AnimalCategory('Mammals')

mammals_category.add_animal(animal_object=lion)
mammals_category.add_animal(animal_object=zebra)

mammals_category.display_category_info()

zoo = Zoo()
zoo.add_categories(mammals_category)

zoo.display_zoo_info()
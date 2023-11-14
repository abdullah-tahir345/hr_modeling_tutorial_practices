# Super method is used to call the both class (parent and child class) constructor. If we don't use
# super method the child class constructor will override the parent class constructor.

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        print('This is parent class constructor.')
        
    def make_sound(self):
        print("Animal sound is : ",self.sound)
        
        
class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)      # Calling the parent class constructor
        self.breed = breed
        print('This is child class constructor.')
        
    def bark(self):
        print("Dog barks")
        
        
dog = Dog('Puppy', 'barks', 'American')
dog.make_sound()
dog.bark()
dog.bark()

#instance variables
print(dog.name)
print(dog.sound)
print(dog.breed)
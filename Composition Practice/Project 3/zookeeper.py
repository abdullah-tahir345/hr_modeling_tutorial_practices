
class Zookeeper:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        
    def feed_animals(self, enclosure):
        print(f"{self.name} is feeding the animals in the {enclosure.environmental_conditions} enclosure.")

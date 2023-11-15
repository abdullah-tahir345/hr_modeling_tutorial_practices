from animal_heath_record import HealthRecord
from animal import Animal
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from zoo import Zoo

# Animals
simba = Animal('Simba', 'Lion')
mufasa = Animal('Mufasa', 'Lion')
leo = Animal('Leo', 'Lion')
elephant = Animal('Dumbo', 'Elephant')

# Health Record of animals
simba_health_record_10 = HealthRecord('05-10-2023', 'antibiotic Treatment', 'flu Vacination', 'Regular Checkup')
simba_health_record_11 = HealthRecord('05-11-2023', 'Antibiotic treatment', 'No Vacination', 'Regular Checkup')
mufasa_health_record_10 = HealthRecord('01-10-2023', 'Deworming', 'Annual Shots', 'Dental Examination')

# Add health record
simba.add_health_record(simba_health_record_10)
simba.add_health_record(simba_health_record_11)
mufasa.add_health_record(mufasa_health_record_10)

# Create Enclosures
enclosure_1 = Enclosure(2, 'Savannah')
enclosure_2 = Enclosure(1, 'Forest')

# Add animal in enclosure
enclosure_1.add_animal(simba)
enclosure_1.add_animal(mufasa)

print()
enclosure_1.add_animal(leo) # Give us exception
print()
enclosure_2.add_animal(elephant)

# Create zookeepers and Veterinarians
zookeeper_james = Zookeeper('James', 'Mammals')
veterinarian_john = Veterinarian('John', 'Dental Care')


# Create Zoo
zoo = Zoo()

# Add Enclosure, Zookeepers and Veterinarians
zoo.add_enclosure(enclosure_1)
zoo.add_enclosure(enclosure_2)
zoo.add_zookeeper(zookeeper_james)
zoo.add_verterinarian(veterinarian_john)

print()
# Perform Actions
for enclosure in zoo._enclosures:
    zookeeper_james.feed_animals(enclosure)

print()
for animal in enclosure_1.animals:
    veterinarian_john.treat_animal(animal)
    
print()
zoo.sell_ticket(50)
zoo.sell_ticket(50)
zoo.sell_ticket(100)
zoo.sell_ticket(500)

print()
print(f'Zoo Revenue: ${zoo._revenue}')
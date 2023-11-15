# from animal_heath_record import HealthRecord

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self._health_history = []         #Health history objects stored here
        
    def add_health_record(self, health_record):
        self._health_history.append(health_record)
        
        
# Create a sample heath record and save it in the Animal class
# lion = Animal('Simba', 'Lion')
# lion_health_record_10 = HealthRecord('05-10-2023', 'antibiotic Treatment', 'flu Vacination', 'Regular Checkup')
# lion_health_record_11 = HealthRecord('05-11-2023', 'Antibiotic treatment', 'No Vacination', 'Regular Checkup')

# lion.add_health_record(lion_health_record_10)
# lion.add_health_record(lion_health_record_11)


# print(f'Animal Name : {lion.name}')
# print(f'Animal Species : {lion.species}')
# print()
# for i, hr in enumerate(lion._health_history):
#     print(f'Animal Health Record {i+1} Date : {hr.date}')
#     print(f'Animal Health Record {i+1} Treatment : {hr.treatment}')
#     print(f'Animal Health Record {i+1} Vaccination : {hr.vaccination}')
#     print(f'Animal Health Record {i+1} Examination : {hr.examination}')
#     print()      

class Engine:
    def __init__(self, hoursepower, fuel_type):
        self.hoursepower = hoursepower
        self.fuel_type = fuel_type
        

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        
    def start_engine(self):
        print(f'The {self.make} {self.model} engine is now started.')
        
    def display_info(self):
        print(f'Make : {self.make}')
        print(f'Model : {self.model}')
        print(f'Year : {self.year}')
        print(f'Hoursepower : {self.engine.hoursepower}')
        print(f'Fuel Type : {self.engine.fuel_type}')
        print()
        
        
engine_ = Engine(450, 'Gasoline')
car_1 = Car('Ferrari', '488 GTB', 2019, engine=engine_)
car_1.start_engine()
car_1.display_info()

print('-------------------')

car_2 = Car('BMW', '589 MTC', 2023, engine=engine_)
car_2.start_engine()
car_2.display_info()
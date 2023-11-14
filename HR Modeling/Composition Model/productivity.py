class ProductivitySystem:
    def track_system(self, employees, hours):
        print('Tracking Productivity Of Employee')
        print('---------------------')
        for employee in employees:
            print(employee.work(hours))
        print('')
        

#Productivity System -- Roles
class ManagerRole:
    def work(self, hours):
        return f'{self.name} yells for {hours} hours.'
    
class SecretaryRole:
    def work(self, hours):
        return f'{self.name} do paper work for {hours} hours.'
    
class SalesRole:
    def work(self, hours):
        return f'{self.name} take orders for {hours} hours on phone.'
    
class FactoryPersonRole:
    def work(self, hours):
        return f'{self.name} make products for {hours} hours.'
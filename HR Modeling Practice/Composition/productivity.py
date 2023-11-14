class ManagerRole:
    def work(self, hours):
        return f'screams and yells for {hours} hours.'
        
class SecretaryRole:
    def work(self, hours):
        return f'expends {hours} hours doing office paper work.'
        
class SaleRole:
    def work(self, hours):
        return f'expends {hours} hours on the phone.'
        
class FactoryRole:
    def work(self, hours):
        return f'manufacures gadgets for {hours} hours on the phone.'




class ProductivitySystem:
    def __init__(self):
        self.roles = {
            'manager' : ManagerRole,
            'secretary' : SecretaryRole,
            'sales' : SaleRole,
            'factory' : FactoryRole
            }
        
    def get_role(self, role_id):
        role_type = self.roles.get(role_id)
        if not role_type:
            raise ValueError('Role Not Found')
        return role_type
    
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name} : {result}')
        print('')
        

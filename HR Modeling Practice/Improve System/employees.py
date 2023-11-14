from hr import PayrollSystem
from productivity import ProductivitySystem
from contacts import AddressBook

class Employee:
    # Constructor of the Employee class and intialize it's instance variables
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll
    
    def work(self, hours):
        duties = self.role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self.payroll.track_work(hours)
        
    def calculate_payroll(self):
        return self.payroll.calculate_payroll()
    
    

class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id' : 1,
                'name' : 'John Steve',
                'role' : 'manager'
            },
            {
                'id' : 2,
                'name' : 'Elsa Jane',
                'role' : 'secretary'
            },
            {
                'id' : 3,
                'name' : 'John Frost',
                'role' : 'factory'
            },
            {
                'id' : 4,
                'name' : 'Johny Depp',
                'role' : 'sales'
            },
            {
                'id' : 5,
                'name' : 'Steve Jobs',
                'role' : 'secretary'
            },
            ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_address = AddressBook()
        
    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]
    
    def _create_employee(self, id, name, role):
        address = self.employee_address.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)

    
    
# class Manager(Employee, ManagerRole, SalaryPolicy):
#     # Inherit the employee class members and intialize the needed instance variables
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id, name)


# class Secretary(Employee, SecretaryRole, SalaryPolicy):
#     # Inherit the employee class members and intialize the needed instance variables
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id, name)


# class SalesPerson(Employee, SaleRole, ComissionPolicy):
#     # Constructor of this ComissionEmployee(Derived From SalaryEmployee class)
#     def __init__(self, id, name, weekly_salary, comission):
#         ComissionPolicy.__init__(self, weekly_salary, comission)
#         super().__init__(id, name)  #call the constructor of the parent class SalaryEmployee and retrieve all it's members in this derived class 


# class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
#     # Constructor of this ComissionEmployee(Derived From SalaryEmployee class)
#     def __init__(self, id, name, hours_worked, hours_rate):
#         HourlyPolicy.__init__(self, hours_worked, hours_rate)
#         super().__init__(id, name)  #call the constructor of the parent class SalaryEmployee and retrieve all it's members in this derived class 
        

# class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hours_rate):
#         HourlyPolicy.__init__(self, hours_worked, hours_rate)
#         super().__init__(id, name)
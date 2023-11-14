from hr import SalaryPolicy, HourlyPolicy, ComissionPolicy
from productivity import ManagerRole, SecretaryRole, SaleRole, FactoryRole

class Employee:
    # Constructor of the Employee class and intialize it's instance variables
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Manager(Employee, ManagerRole, SalaryPolicy):
    # Inherit the employee class members and intialize the needed instance variables
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)


class Secretary(Employee, SecretaryRole, SalaryPolicy):
    # Inherit the employee class members and intialize the needed instance variables
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)


class SalesPerson(Employee, SaleRole, ComissionPolicy):
    # Constructor of this ComissionEmployee(Derived From SalaryEmployee class)
    def __init__(self, id, name, weekly_salary, comission):
        ComissionPolicy.__init__(self, weekly_salary, comission)
        super().__init__(id, name)  #call the constructor of the parent class SalaryEmployee and retrieve all it's members in this derived class 


class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    # Constructor of this ComissionEmployee(Derived From SalaryEmployee class)
    def __init__(self, id, name, hours_worked, hours_rate):
        HourlyPolicy.__init__(self, hours_worked, hours_rate)
        super().__init__(id, name)  #call the constructor of the parent class SalaryEmployee and retrieve all it's members in this derived class 
        

class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hours_rate):
        HourlyPolicy.__init__(self, hours_worked, hours_rate)
        super().__init__(id, name)
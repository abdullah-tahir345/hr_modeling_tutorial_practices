from hr import SalaryPayroll, HourlyPayroll, ComisssionPayroll
from productivity import *

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.address = None
        
class Manager(Employee, ManagerRole, SalaryPayroll):
    def __init__(self, id, name, weekly_salary):
        # MRO
        SalaryPayroll.__init__(self, weekly_salary)
        super().__init__(id, name)

class Secretary(Employee, SecretaryRole, SalaryPayroll):
    def __init__(self, id, name,weekly_salary):
        # MRO
        SalaryPayroll.__init__(self, weekly_salary)
        super().__init__(id, name)
        
class SalesBoy(Employee, SalesRole, ComisssionPayroll):
    def __init__(self, id, name, weekly_salary, comission):
        # MRO
        ComisssionPayroll.__init__(self, weekly_salary, comission)
        super().__init__(id, name)
        
class FactoryPerson(Employee, FactoryPersonRole, HourlyPayroll):
    def __init__(self, id, name, work_hours, pay_per_hour):
        HourlyPayroll.__init__(self, work_hours, pay_per_hour)
        super().__init__(id, name)

#Multiple Inheritance
class TemporarySecretary(Employee, SecretaryRole, HourlyPayroll): #--Warning shows because HourlyPayroll and SecretaryRole is inherited from staric(*)
    def __init__(self, id, name, work_hours, pay_per_hour):
        HourlyPayroll.__init__(self, work_hours, pay_per_hour)
        super().__init__(id, name)
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

        
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    
    def calculate_payroll(self):
        return self.weekly_salary

    
class HourlyEmployee(Employee):
    def __init__(self, id, name, work_hours, pay_per_hour):
        super().__init__(id, name)
        self.work_hours = work_hours
        self.pay_per_hour = pay_per_hour
        
    def calculate_payroll(self):
        return self.work_hours * self.pay_per_hour
    

class ComisssionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, comission):
        super().__init__(id, name, weekly_salary)
        self.comission = comission
        
    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll()
        return fixed_salary + self.comission
    
    
    
    
#Productivity System
class Manager(SalaryEmployee):
    def work(self, hours):
        return f'{self.name} yells for {hours} hours.'
    
class Secretary(SalaryEmployee):
    def work(self, hours):
        return f'{self.name} do paper work for {hours} hours.'
    
class SalesPerson(ComisssionEmployee):
    def work(self, hours):
        return f'{self.name} take orders for {hours} hours on phone.'
    
class FactoryPerson(HourlyEmployee):
    def work(self, hours):
        return f'{self.name} make products for {hours} hours.'
    
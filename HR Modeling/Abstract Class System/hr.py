from abc import ABC,abstractmethod 

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    @abstractmethod
    def calculate_payroll(self):
        pass
        
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


class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculate Payroll')
        print('-----------------')
        for employee in employees:
            print(f'Payroll for : {employee.id} - {employee.name}')
            print(f' - Check amount : {employee.calculate_payroll()}')
            
            print()
        
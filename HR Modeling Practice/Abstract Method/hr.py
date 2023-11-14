# Import the abc module and make the abstract class. So, we don't make it's object and make sure that
# abstract method is created in every class
from abc import ABC, abstractmethod

class Employee(ABC):
    # Constructor of the Employee class and intialize it's instance variables
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    # Create the abstract method
    @abstractmethod
    def calculate_payroll(self):
        pass



class SalaryEmployee(Employee):
    # Inherit the employee class members and intialize the needed instance variables
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
        
    # Calculate the weekly salary
    def calculate_payroll(self):
        return self.weekly_salary



class HourlyEmployee(Employee):
    # Inherit the employee class members and intialize the needed instance variables
    def __init__(self, id, name, hours_worked, hours_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate
    
    # Calculate the salary of hourly employees (Hours Worked * Hours Rate)
    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate


    
class ComissionEmployee(SalaryEmployee):
    # Constructor of this ComissionEmployee(Derived From SalaryEmployee class)
    def __init__(self, id, name, weekly_salary, comission):
        super().__init__(id, name, weekly_salary)  #call the constructor of the parent class SalaryEmployee and retrieve all it's members in this derived class 
        self.comission = comission
    
    # Calculate the salary and also add comission in the salary (Fixed Salary + Comission)
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.comission
    


# Calculate the payroll of all employee and we use the objects here and get the payroll of employee
class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for : {employee.id} - {employee.name}')
            print(f'- Check amount : {employee.calculate_payroll()}')
            print('')
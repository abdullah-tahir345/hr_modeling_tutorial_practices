
# Calculate the payroll of all employee and we use the objects here and get the payroll of employee
class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for : {employee.id} - {employee.name}')
            print(f'- Check amount : {employee.calculate_payroll()}')
            print('')
            
class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary
        
    # Calculate the weekly salary
    def calculate_payroll(self):
        return self.weekly_salary



class HourlyPolicy:
    def __init__(self, hours_worked, hours_rate):
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate
    
    # Calculate the salary of hourly employees (Hours Worked * Hours Rate)
    def calculate_payroll(self):
        return self.hours_worked * self.hours_rate


    
class ComissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, comission):  #call the constructor of the parent class SalaryEmployee and retrieve all it's members in this derived class 
        super().__init__(weekly_salary)    
        self.comission = comission
    
    # Calculate the salary and also add comission in the salary (Fixed Salary + Comission)
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.comission
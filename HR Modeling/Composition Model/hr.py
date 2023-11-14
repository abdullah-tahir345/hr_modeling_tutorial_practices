class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculate Payroll')
        print('-----------------')
        for employee in employees:
            print(f'Payroll for : {employee.id} - {employee.name}')
            print(f' -  Check amount : {employee.calculate_payroll()}')
            if employee.address:
                print(f' -  Address : {employee.address}')
            print()

# --Policies
class SalaryPayroll:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary
    
    def calculate_payroll(self):
        return self.weekly_salary

    
class HourlyPayroll:
    def __init__(self, work_hours, pay_per_hour):
        self.work_hours = work_hours
        self.pay_per_hour = pay_per_hour
        
    def calculate_payroll(self):
        return self.work_hours * self.pay_per_hour
    

class ComisssionPayroll(SalaryPayroll):
    def __init__(self, weekly_salary, comission):
        super().__init__(weekly_salary)
        self.comission = comission
        
    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll()
        return fixed_salary + self.comission
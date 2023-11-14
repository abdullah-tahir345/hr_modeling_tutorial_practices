
# Calculate the payroll of all employee and we use the objects here and get the payroll of employee
class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for : {employee.id} - {employee.name}')
            print(f'- Check amount : {employee.calculate_payroll()}')
            print('')
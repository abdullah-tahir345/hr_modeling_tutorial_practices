# Import the hr.py module and then create objects of class
import hr
import disgruntled

# Object of class SalaryEmployee
salaryemployee1 = hr.SalaryEmployee(1, 'James', 25000)
# Object of class HourlyEmployee
hourlyemployee1 = hr.HourlyEmployee(2, 'Tom', 5, 1500)
hourlyemployee2 = hr.HourlyEmployee(4, 'Chris', 12, 1500)
# Object of class ComissionEmployee
comissionemployee1 = hr.ComissionEmployee(3, 'Gerry', 15000, 5000)

# Create the disgruntled.py employee object
disgruntledemployee = disgruntled.DisgruntledEmployee(5, 'Grayson')

# Invalid Employee -- This will create an error because it don't have the instance method of calculate_payroll
# employee1 = hr.Employee(5, 'Setve')
# payroll1 = hr.PayrollSystem()
# payroll1.calculate_payroll([
#     employee1
#     ])

# Create the object of PayrollSystem class 
payroll = hr.PayrollSystem()
# Pass the objects list to the payroll object  
payroll.calculate_payroll([
    salaryemployee1,
    hourlyemployee1,
    comissionemployee1,
    hourlyemployee2,
    disgruntledemployee
    ])
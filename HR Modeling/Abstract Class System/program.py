import hr

# Now, We can't make it's object because it's an abstract class. So, it give us an error.
# employee = hr.Employee(4, 'Barbie')

salary_employee = hr.SalaryEmployee(1, 'James', 2000)
hourly_employee = hr.HourlyEmployee(2, 'Norie', 10, 25)
comission_employee = hr.ComisssionEmployee(3, 'Joe', 1000, 100)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    comission_employee
    ])
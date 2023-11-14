import hr
import disgruntled

disgruntled_employee = disgruntled.DisEmployee(4, 'Barbies')

salary_employee = hr.SalaryEmployee(1, 'James', 2000)
hourly_employee = hr.HourlyEmployee(2, 'Norie', 10, 25)
comission_employee = hr.ComisssionEmployee(3, 'Joe', 1000, 100)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    comission_employee,
    disgruntled_employee
    ])
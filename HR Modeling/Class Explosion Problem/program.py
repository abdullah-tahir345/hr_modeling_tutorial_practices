import hr
import employees
import productivity


#salary_employee = employees.SalaryEmployee(1, 'James', 2000)
#hourly_employee = employees.HourlyEmployee(2, 'Norie', 10, 25)
#comission_employee = employees.ComisssionEmployee(3, 'Joe', 1000, 100)

manager = employees.Manager(1, 'James', 2000)
secretary = employees.Secretary(2, 'Norie', 1500)
sales_boy = employees.SalesPerson(3, 'Joe', 1000, 100)
factory_person = employees.FactoryPerson(4, 'Barbie', 12, 150)

employees_list = [
    manager,
    secretary,
    sales_boy,
    factory_person
    ]

productive_system = productivity.ProductivitySystem()
productive_system.track_system(employees_list, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees_list)
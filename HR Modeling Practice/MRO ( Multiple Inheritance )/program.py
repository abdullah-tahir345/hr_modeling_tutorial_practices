# Import the hr.py module and then create objects of class
import hr
import employees
import productivity

# Object of class SalaryEmployee
manager = employees.Manager(1, 'James', 25000)
# Object of class HourlyEmployee
secretary = employees.Secretary(2, 'Tom', 15000)
factory_worker = employees.FactoryWorker(4, 'Chris', 12, 1500)
# Object of class ComissionEmployee
sales_guy = employees.SalesPerson(3, 'Gerry', 15000, 5000)

temporary_secretary = employees.TemporarySecretary(5, 'John Doe', 5, 1500)


employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary
    ]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
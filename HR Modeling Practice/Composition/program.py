# Import the hr.py module and then create objects of class
import hr
import employees
import productivity
import contacts

# Object of class SalaryEmployee
manager = employees.Manager(1, 'James', 25000)
manager.address = contacts.Address('11 Street', 'Lahore', 'Punjab', 55222)
# Object of class HourlyEmployee
secretary = employees.Secretary(2, 'Tom', 15000)
secretary.address = contacts.Address('15 Street', 'Faisalabad', 'Punjab', 55122)
factory_worker = employees.FactoryWorker(4, 'Chris', 12, 1500)
factory_worker.address = contacts.Address('20 Street', 'Islamabad', 'Punjab', 54222)
# Object of class ComissionEmployee
sales_guy = employees.SalesPerson(3, 'Gerry', 15000, 5000)
sales_guy.address = contacts.Address('05 Street', 'Quetta', 'Balochistan', 45678)

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
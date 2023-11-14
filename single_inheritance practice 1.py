# Parent Class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display_info(self):
        # Display basic information about a person
        print(f"Name : {self.name}\nAge : {self.age}\nAddress : {self.address}")


# Child Class
class Employee(Person):
    def __init__(self, name, age, address, employee_id, salary):
        # Call the constructor of the parent class (Person)
        super().__init__(name, age, address)
        # Additional attributes specific to employees
        self.employee_id = employee_id
        self.salary = salary
    
    def display_info(self):
        # Call the display_info method of the parent class (Person)
        super().display_info()
        # Display additional information specific to employees
        print(f"Employee ID : {self.employee_id}\nSalary : {self.salary}")


# Child Class
class Manager(Employee):
    def __init__(self, name, age, address, employee_id, salary, department):
        # Call the constructor of the parent class (Employee)
        super().__init__(name, age, address, employee_id, salary)
        # Additional attribute specific to managers
        self.department = department
    
    def display_info(self):
        # Call the display_info method of the parent class (Employee)
        super().display_info()
        # Display additional information specific to managers
        print(f"Department : {self.department}")

# Instances of the classes
per1 = Person('Johns', 21, 'New York')
# Display information for a person
per1.display_info()

print('-----------------------------')
emp1 = Employee('Johns', 21, 'New York', 1, 50000)
# Display information for an employee
emp1.display_info()

print()

emp2 = Employee('Harry', 25, 'New York', 2, 20000)
# Display information for another employee
emp2.display_info()

print('-----------------------------')
manager1 = Manager('Johns', 21, 'New York', 1, 50000, 'IT')
# Display information for a manager
manager1.display_info()

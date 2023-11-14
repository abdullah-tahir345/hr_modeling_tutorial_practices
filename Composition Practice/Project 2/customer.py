class Person:
    def __init__(self, name, email):
        # Initialize common attributes for Person class
        self.name = name
        self.email = email

class Customer(Person):
    def __init__(self, id, name, email):
        # Call the constructor of the parent class and add additional attributes
        super().__init__(name, email)
        self.id = id

    def display_customer_info(self):
        # Display information about a customer
        print('Customers Information')
        print('---------------------')
        print(f'Customer ID : {self.id}')
        print(f'Customer Name : {self.name}')
        print(f'Customer Email : {self.email}')
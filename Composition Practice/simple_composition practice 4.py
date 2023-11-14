# Define a class representing Furniture
class Furniture:
    def __init__(self, table, sofa):
        # Initialize attributes for the number of tables and sofas
        self.table = table
        self.sofa = sofa

# Define a class representing Address
class Address:
    def __init__(self, street, city):
        # Initialize attributes for street and city
        self.street = street
        self.city = city

    # Override the __str__ method to provide a string representation of the address
    def __str__(self):
        return f'{self.street}, {self.city}'

# Define a class representing House
class House:
    def __init__(self, size, location, furniture):
        # Initialize attributes for house size, location (an instance of Address), and furniture (an instance of Furniture)
        self.size = size
        self._location = location  # Note: _location is marked with an underscore to indicate it's a private attribute
        self._furniture = furniture  # Note: _furniture is marked with an underscore to indicate it's a private attribute

    # Define a method to display information about the house
    def display_info(self):
        print(f'Size : {self.size}')
        print(f'Location : {self._location}')  # Access the location using _location attribute
        print(f'Tables : {self._furniture.table}')  # Access the number of tables using _furniture attribute
        print(f'Sofa : {self._furniture.sofa}')  # Access the number of sofas using _furniture attribute
        print()

# Create an instance of Furniture with specific quantities of tables and sofas
furniture_1 = Furniture(10, 2)
# Create an instance of Address with a specific street and city
address_1 = Address('11th Street', 'Maxico')
# Create an instance of House with specific size, location (address_1), and furniture (furniture_1)
h1 = House('11 SQ Ft', location=address_1, furniture=furniture_1)

# Create another instance of Furniture with different quantities of tables and sofas
furniture_2 = Furniture(5, 3)
# Create another instance of Address with a different street and city
address_2 = Address('09th Street', 'Lahore')
# Create another instance of House with different size, location (address_2), and furniture (furniture_2)
h2 = House('05 SQ Ft', location=address_2, furniture=furniture_2)

# Display information about the first house
h1.display_info()

# Display information about the second house
print('-----------------------')
h2.display_info()

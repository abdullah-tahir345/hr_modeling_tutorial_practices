from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    @abstractmethod
    def add_to_cart(self):
        pass
    
    @abstractmethod
    def display_info(self):
        pass
    
class ElectronicProduct(Product):
    def __init__(self, name, price, quantity, brand, warranty_period, power_source):
        super().__init__(name, price, quantity)
        self.brand = brand
        self.warranty_period = warranty_period
        self.power_source = power_source
        
    def add_to_cart(self):
        print('Product added to the cart.')
        
    def display_info(self):
        print(f"Name : {self.name}\nPrice : {self.price}\nQuantity : {self.quantity}\nBrand : {self.brand}\nWarranty Period : {self.warranty_period}\nPower Source : {self.power_source}")
        
class ClothingProduct(Product):
    def __init__(self, name, price, quantity, size, color):
        super().__init__(name, price, quantity)
        self.size = size
        self.color = color
        
    def add_to_cart(self):
        print('Product added to the cart.')
        
    def display_info(self):
        print(f"Name : {self.name}\nPrice : {self.price}\nQuantity : {self.quantity}\nSize : {self.size}\nColor : {self.color}")
        
        
        
e1 = ElectronicProduct('Washing Machine', 25000, 10, 'Electronical', '5 Years', 'Electricity')
e1.display_info()

print('-------------------------')
c1 = ClothingProduct('Shirt', 3000, 50, 32, 'Red')
c1.display_info()
from customer import Customer
from products import Products
from order import Order

# Customers
c1 = Customer(1, 'James', 'james@gmail.com')
c2 = Customer(2, 'Harry', 'harry@gmail.com')
c3 = Customer(3, 'Auston', 'auston@gmail.com')
c4 = Customer(4, 'Barbie', 'barbie@gmail.com')
c5 = Customer(5, 'Jane', 'jane@gmail.com')

# Products
p1 = Products(1, 'Lux Soup', 150)
p2 = Products(2, 'Zinger Burger', 350)
p3 = Products(3, 'Pizza', 1500)
p4 = Products(4, 'Burger', 150)
p5 = Products(5, 'Surf Excel', 1000)

o1 = Order(1, customer=c3)
o1.add_product(p2)
o1.add_product(p1)
o1.add_product(p5)
o1.remove_product(p3)

o1.calculate_total()
o1.display_order_info()
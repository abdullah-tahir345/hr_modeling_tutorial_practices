class Order:
    DEFAULT_TOTAL = 0  # Class constant for default total

    def __init__(self, order_id, customer):
        # Initialize order attributes
        self.order_id = order_id
        self._customer = customer
        self._products = []

    def add_product(self, product_object):
        # Add a product to the order
        self._products.append(product_object)

    def remove_product(self, product_object):
        # Remove a product from the order if it exists
        try:
            self._products.remove(product_object)
        except ValueError:
            print("Product not found in the order.")

    def calculate_total(self):
        # Calculate the total price of products in the order
        total = Order.DEFAULT_TOTAL
        for product in self._products:
            total += product.price
        print(f'Your Total Is : {total}')

    def display_order_info(self):
        # Display information about the order and its customer
        print('Order Information')
        print('-----------------')
        print(f'Customer Name : {self._customer.name}')
        print(f'Customer Email : {self._customer.email}')
        print()
        for product in self._products:
            product.display_product_info()
        print()
        self.calculate_total()
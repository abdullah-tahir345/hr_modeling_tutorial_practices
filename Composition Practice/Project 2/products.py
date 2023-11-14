class Products:
    def __init__(self, product_id, name, price):
        # Initialize product attributes
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product_info(self):
        # Display information about a product
        print('Product Information')
        print('---------------------')
        print(f'Product ID : {self.product_id}')
        print(f'Product Name : {self.name}')
        print(f'Product Price : {self.price}')
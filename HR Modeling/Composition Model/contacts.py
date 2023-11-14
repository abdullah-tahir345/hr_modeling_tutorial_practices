class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        
    def __str__(self):
        address = [self.street]
        
        address.append(f'\t{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(address)
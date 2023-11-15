
class Zoo:
    def __init__(self):
        self._enclosures = []
        self._zookeepers = []
        self._veterinarians = []
        self._revenue = 0
        
    def add_enclosure(self, enclosure):
        self._enclosures.append(enclosure)
        
    def add_zookeeper(self, zookeeper):
        self._zookeepers.append(zookeeper)
        
    def add_verterinarian(self, veterinarian):
        self._veterinarians.append(veterinarian)
        
    def sell_ticket(self, price):
        print('Vistor bought a ticket.')
        self._revenue += price
from abc import ABC, abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def gun(self):
        pass
        
class Army(DefenceForce):
    def area(self):
        print('Army Area : Land')
    def gun(self):
        print('Army Gun : AK47')
        
class AirForce(DefenceForce):
    def area(self):
        print('AirForce Area : Air')
    def gun(self):
        print('AirForce Gun : AK48')
        
class Navy(DefenceForce):
    def area(self):
        print('Navy Area : Sea')
    def gun(self):
        print('Navy Gun : AK49')
        
n = Navy()
n.area()
n.gun()

print()
a = AirForce()
a.area()
a.gun()

print()
ar = Army()
ar.area()
ar.gun()

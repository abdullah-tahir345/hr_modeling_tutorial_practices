from abc import ABC, abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def gun(self):
        print('Gun : AK47')
        
class Army(DefenceForce):
    def area(self):
        print('Army Area : Land')
        
class AirForce(DefenceForce):
    def area(self):
        print('AirForce Area : Air')
        
class Navy(DefenceForce):
    def area(self):
        print('Navy Area : Sea')
        
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

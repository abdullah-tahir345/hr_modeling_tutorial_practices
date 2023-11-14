from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self):
        print('Parent class constructor.')
    
    # Abstract Method
    @abstractmethod
    def disp(self):
        pass
    
    def showF(self):
        print('This is concrete method.')
        

class Son(Father):
    def __init__(self):
        super().__init__()
        print('Child class constructor.')
    
    def disp(self):
        print('This is child class instance method and it is abstract method in base class.')
        
    def showS(self):
        print('This is child class instance method.')
        

s = Son()
print()
s.disp()
print()
s.showF()
print()
s.showS()
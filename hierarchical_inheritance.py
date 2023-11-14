# Hierarchical Inheritance : When multiple derived classes are created
# from one base class then this is called hierarchical inheritance.

class Father(object):
    def __init__(self):
        print('This is father constructor.')
        
    def showF(self):
        print('This is father class instance method.')
        
        
class Son(Father):
    def __init__(self):
        super().__init__()      #Calling the parent class constructor
        print('This is son constructor.')
        
    def showS(self):
        print('This is son class instance method.')
        
    
class Daughter(Father):
    def __init__(self):
        print('This is daughter constructor.')
    
    def showD(self):
        print('This is daughter class instance method.')
        
f = Father()
f.showF()

print()
s = Son()
s.showF()
s.showS()

print()
d = Daughter()
d.showF()
d.showD() 
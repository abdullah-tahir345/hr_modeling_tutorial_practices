# Single Inheritance : In single inheritance only one child class inherited from one parent class 
# properties and class members.

# Parent/Base/Super Class
class Father(object):
    money = 1000
    
    def show(self):
        print('This is the Parent class instance method.')
        
    @classmethod
    def showmoney(cls):
        print('This is the class method. And money is : ',cls.money)
        
# Child/Derived/Sub Class
class Son(Father):
    def disp(self):
        print('This is child class instance method.')
        
s = Son()
s.disp()          # Call of child class instance method
s.show()         # Call of parent class instance method
s.showmoney()    # Call of parent class class/static method
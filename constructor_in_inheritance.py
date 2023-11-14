# Parent Class
class Father:
    # Constructor call itself when an object is made
    def __init__(self):
        self.money = 100000
        print('This is constructor of Parent Class.')
        
# Child Class
class Son(Father):
    def show(self):
        print('This is the child class instance variable. Money is : ',self.money)
        
# Object of Child Class
s = Son() # Constructor call here
s.show()

# Access instance variable using child class object
print('This is child class instance variable and it value is --> ',s.money)

s.money = 2000
print('This is child class instance variable and it value is --> ',s.money)
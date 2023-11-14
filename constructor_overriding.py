# If we have constructor in both classes then child class constructor have more priority as compared
# to the parent class constructor.

# Parent Class
class Father:
    def __init__(self):
        self.money = 5000
        print('This is Parent Class constructor.')
        
    def show(self):
        print('This is the parent class instance meethod. And money is : ', self.money)
        
# Child Class
class Son(Father):
    def __init__(self):
        self.money = 2000
        self.car = 'Ferrari'
        print('This is child class constructor.')
    
    def disp(self):
        print('This is Child class instance method.')
        

f = Father()
s = Son() 
print(s.car)
class Rectangle:
    def __init__(self, length, height):
        self._length = length
        self._height = height
        
    @property
    def area(self):
        return self._length * self._height
    
    def resize(self, new_length, new_height):
        self._length = new_length
        self._height = new_height
    
    
class Square(Rectangle):
    def __init__(self, side_size):
        super().__init__(side_size, side_size)
        
        
rectangle = Rectangle(2, 4)
rectangle.resize(5, 3)
assert rectangle.area == 15

square = Square(2)
square.resize(5, 4)

print('Area : ', square.area)

# assert square.area == 20

print('OK!')
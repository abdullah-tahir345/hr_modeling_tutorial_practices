# Simple Composition Example

class Engine:
    pass

class Wheel:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
        self.front_left_wheel = Wheel()
        self.front_right_wheel = Wheel()
        self.back_left_wheel = Wheel()
        self.back_right_wheel = Wheel()
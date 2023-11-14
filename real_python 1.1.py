class MyClass:
    pass

c = MyClass()

o = object()
print(dir(o))

# This is same as the directory of the object class object. Because
# this class inherited from the object class and we know that in python
# everything is an object. So, here MyClass is inherited from the parent
# class which is object class.
print()   #For spacing in output
print(dir(c))
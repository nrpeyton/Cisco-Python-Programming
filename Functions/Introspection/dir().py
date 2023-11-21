# Example use of the dir() function on a module
import math

print(dir(math))
'''
OUTPUT:
The output will list all the names, functions and constants in the math module.
This includes mathematical functions like cos, sin, tan, exp, log, sqrt, as well as constants like pi and e.
'''

# Note: When an object has a custom dir() method, it's called by dir(). This enables objects with custom getattr() or getattribute() to tailor their attribute reporting.






# Using dir() on a built-in type
print(dir(list))

'''
OUTPUT:
The output will list all the attributes and methods associated with the list type.
This includes methods like append, clear, copy, count, extend, index, insert, pop, remove, reverse, and sort, among others.
'''






# Using dir() on a custom object
class SampleClass:
    def __init__(self):
        self.x = 10
    def sample_method(self):
        return self.x

obj = SampleClass()
print(dir(obj))

'''
OUTPUT:
The output will include the list of usual methods and attributes, along with 'sample_method' and 'x', which are defined in SampleClass.
This list will typically include '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'sample_method', and 'x'.
'''



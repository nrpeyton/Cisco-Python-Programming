hasattr(object, 'name')

'''
The arguments are an object and a string. The result is True if the string is the name of one of the object's attributes, False if not. 
'''

class ExampleClass:
    def __init__(self):
        self.a = 2

example_object = ExampleClass()
print(hasattr(example_object, 'a')) # Output: True









'''
This function can also operate on classes to check if a class variable is available.
'''

class ExampleClass:
    attr = 1

print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

'''
Output:
True
False
'''
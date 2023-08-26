class ExampleClass:
    counter = 0 # class attribute, shared by ALL instances
    def __init__(self, val = 1):
        self.__first = val # instance attribute, belongs to its own object, and stored seperately in each object
        ExampleClass.counter += 1  # # class attribute, shared by ALL instances; requires prefix because __init__ is in method scope, focused on instances. To access a class attribute, you must be explicit.


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

# outputs dict of INDEPENDENT instance attributes*    # outputs SAME value SHARED by all instances (objects)**
print(example_object_1.__dict__,                     example_object_1.counter)
print(example_object_2.__dict__,                     example_object_2.counter)
print(example_object_3.__dict__,                     example_object_3.counter)

'''
* each instance attribute requires its own memory location
** a class attribute is only stored once

Instance attributes are stored per instance, consuming memory for each object I create. Class attributes are shared across all instances and only stored once, 
making them more memory-efficient when the attribute's value is supposed to be the same for all instances. This distinction is not just theoretical - it can impact
performance and resource usage.
'''
class ExampleClass:
    counter = 0 # class variable, shared by ALL instances
    def __init__(self, val = 1):
        self.__first = val # instance variable, belongs to its own object, and stored seperately in each object
        ExampleClass.counter += 1  # class variable, shared by ALL instances; requires prefix here because __init__ is in method scope, focused on instances. To access a class attribute, you must be explicit.


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
'''
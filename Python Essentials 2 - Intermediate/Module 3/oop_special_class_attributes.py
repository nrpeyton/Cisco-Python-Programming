#                                                CLASS SPECIAL ATTRIBUTES:
#                                                Class.__dict__
#                                                Class.__name__
#                                                Class.__module__
#                                                Class.__bases__


# Class.__dict__

class Snakes:
    pass

class Python(Snakes):
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False

version_2 = Python()
print(Python.__dict__) # Output: {'__module__': '__main__', 'population': 1, 'victims': 0, '__init__': <function Python.__init__ at 0x7fe079b19440>, '__dict__': <attribute '__dict__' of 'Python' objects>, '__weakref__': <attribute '__weakref__' of 'Python' objects>, '__doc__': None}

'''
Output includes the namespace of the class, which includes attributes, methods, and other metadata:

__module__:     Indicates the module in which the class is defined.
__init__:       The initializer method of the class, which is called when a new instance is created.
__dict__:       A dictionary containing the namespace for the class.
__weakref__:    Allows the creation of weak references to instances of the class.
__doc__:        The class's documentation string, which is None by default if not specified.

Important: don't confuse with object.__dict__, which ONLY outputs object/instance variables.
'''





# Class.__name__

class Python:
    pass

print(Python.__name__, 's are snakes', sep='')  # Output: Pythons are snakes

# Outputs as a string.




# Class.__module__

class Python:
    pass

print(Python.__module__)  # Output: '__main__'

'''
Output:
- Indicates the module in which the class is defined.
- Outputs as a string.
- Example: For a class defined in the main script, its __module__ property will output '__main__'.
'''




# Class.__bases__

class Snakes:
    pass

class Python(Snakes):
    pass

print(Python.__bases__)  # Output: (<class '__main__.Snakes'>,)

'''
Output:
- A tuple containing the base classes (superclasses) of the 'Python' class.
- In this case, the 'Python' class inherits from the 'Snakes' class.
- Outputs as a tuple, even if there is only one base class.
'''

print(Python.__bases__[0].__name__) # Output: Snakes
"""ASTERISK '*' USED ALONE"""

def func(a, *, b, c): # * specifies that all arguments following it must be provided as keyword arguments.
    pass

# Correct call
func(1, b=2, c=3)



"""ASTERISK '*' BEFORE A PARAMATER """

def func(arg, *args): # Allows the function to accept any number of positional arguments (the first is still captured by 'arg').
    pass

# Correct call
func(1, 2, 3, 4, 5) #  Python transforms '*args' into a tuple for use within the function:

# Printed 'args':
(2, 3, 4, 5)

# [EXTRA] Unpack on calling fun:
tuple = 1, 2, 3, 4, 5
func(1, *tuple) # Useful if you already have a tuple, otherwise printout would be: ((2, 3, 4, 5),)



"""DOUBLE ASTERISK '**' BEFORE A PARAMATER """

def example_function(**kwargs): # An arbitary number of arguments received by a '**' prefixed parameter are automatically packed into a dictionary.
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(arg1="Hello", arg2=42)

# This is often referred to as "keyword argument unpacking".









#   F U N C T I O N   R U L E S


""" Functions Without Arguments 
(Function checks itself first, then checks the global scope.) """


d = 'a'

def fun():
    d += 'b'    # raises error: outside immutables are read-only
    print(d)


fun()
print(d)




d = ['a', 'b']

def fun():
    d.insert(-1, 'c')    # this works; outside mutables CAN be modified
    print(d)


fun()
print(d) # prints: ['a', 'c', 'b']





"""Functions With Arguments"""


d = 'a'

def fun(d):
    d += 'b'    
    print(d)


fun(d)
print(d) # prints:
# ab
# a



""" When a variable is passed in a function call, it's not just a new copy of the value or only the value itself being passed, but a 
reference to the original variable that is added to the function's local namespace.

Mutables:
The original (outer) variable is modified.

Immutables:
The original (outer) variable is COPIED for seperate local use within the function's local scope.
"""


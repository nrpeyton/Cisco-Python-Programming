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

 This is often referred to as "keyword argument unpacking".
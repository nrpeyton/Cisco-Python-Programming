def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(f"`{str(args)}`")

try:
    raise Exception("1st arg", "2nd arg") # Instantiate an instance of the Exception class with two arguments..
except Exception as e: # In Python's exception handling, 'as e' creates a reference to, not a copy of, the exception object.
    print(e, e.__str__(), e.args) # Printing 'e' implicitly is the same as invoking e.__str__() explicitly.  And 'args' is just an instance property (a tuple) storing the arguments passed to the exception object's constructor.
    print_args(e.args)





# When creating user defined exceptions, they must be new subclasses derived from predefined ones.  Either closely related, or not.  For a structure not closely related to Python's existing tree, we can choose a top base, like BaseException or Exception.




                                            # CLOSELY RELATED TO BUILT-IN EXCEPTIONS ()

class MyZeroDivisionError(ZeroDivisionError):	
    pass

def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:		
        raise ZeroDivisionError("some bad news")


# Usage
for mode in [False, True]:      # Simulate errors.
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:      # Simulate errors.
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')








                                                # BUILDING CUSTOM EXCEPTION HIERARCHIES

class PizzaError(Exception): # Start building it by defining a general exception as a new base class for any other specialized exception. 
    def __init__(self, pizza, message): # To collect more specific information here than regular Exceptions do, our constructor will take two arguments.
        Exception.__init__(self, message) # We pass the second parameter to the superclass constructor; 
        self.pizza = pizza # and save the first inside our own property.


class TooMuchCheeseError(PizzaError): # For specific issues, such as excessive cheese, first derive a new class from PizzaError;
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese # then initialise the more specific issue by adding it to the constructor.







                                                # BUILDING CUSTOM EXCEPTION HIERARCHIES
                                                        # (with simulation)

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese

# Simulation
def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza, pe.args)
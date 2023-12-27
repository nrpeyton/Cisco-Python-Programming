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











class InvalidDataError(Exception):
    def __init__(self, msg, index):
        self.message = msg
        self.index = index
        super().__init__(self.message + str(self.index))
    
    
def check_list(lst):
    index = 0
    
    for elem in lst:
        try:
            if isinstance(elem, int) == False and isinstance(elem, float) == False:
                raise InvalidDataError("Non-numerical element found at index: ", index)

        except InvalidDataError as e:
            return str(e)
        index += 1
    return 'Check okay: all list elements are numerical'

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 'e']

print(check_list(list1))
print(check_list(list2))









class CustomError(Exception):
    def __init__(self, msg, company): # this method is not required ****
        self.args = (msg, company)
        

company_annual_sales = {'Meta': 5000, 'Google': 10000, 'OpenAI': 1000, 'Tesla': 2000}

def update_company_sales(company, sales):
    if company in company_annual_sales.keys():
        company_annual_sales[company] = sales
    elif company not in company_annual_sales.keys():
        raise CustomError('Unknown Company Error: ', company)



try:
    company = input('Enter Company Name: ')
    annual_sales = int(input("Enter Company's Annual Sales: "))
    update_company_sales(company, annual_sales)
except ValueError as ve:
    print(ve)
except CustomError as ce: # Remember 'ce' (aka 'e') is an alias of the instance of the CustomError class.  
    print(ce.args[0], ce.args[1]) # We can still access e.args ('ce'.args here) because we've overriden the built-in Exception class's constructor and created our own 'args' tuple.

print(company_annual_sales)

"""
REMEMBER:
**** The 'args' tuple is a property of the built-in Exception class's constructor method. So it's ONLY updated with arguments passed to the built-in 
Exception's constructor.  Since we are overriding the built-in Exception class's constructor with our own class's constructor and 'args' tuple, we 
are still able to access an e.args tuple. If our custom __init__ method on lines 2/3 were remeoved and replaced only with 'pass', this would have no 
affect on the program because CustomError would start inheriting the built-in Exception class's constructor.
"""
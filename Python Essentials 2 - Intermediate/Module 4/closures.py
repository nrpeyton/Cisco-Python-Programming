'''
A closure in Python is a function that retains access to variables from its surrounding environment, even after the outer function, where it was defined, has 
finished execution.
'''

def tag(tg):
    tg2 = tg[0] + '/' + tg[1:]

    # Define the inner function 'inner'
    def inner(str):
        return tg + str + tg2
    return inner # Return a reference to the inner function (not calling it, hence no parentheses)


b_tag = tag('<b>') # Call 'tag' with argument '<b>', and store the returned function reference in 'b_tag'
print(b_tag('Monty Python')) # Now call the function referenced by 'b_tag', passing 'Monty Python' as argument

# Outputs: <b>Monty Python</b>








def greet():
    # variable defined outside the inner function
    name = "John"
    
    # return a nested anonymous function
    return lambda: "Hi " + name

# call the outer function
message = greet()

# call the inner function
print(message())

# Output: Hi John







# Define then execute a list of closures.

def create_multiplier_functions(n):
    closures = []
    
    for i in range(1, n+1):
        
        def inner(arg, i=i):
            return arg * i
        
        closures.append(inner)
    
    return closures
    
    
# Example usage
multipliers = create_multiplier_functions(4)
print(multipliers[0](6))  # Prints: 6
print(multipliers[1](6))  # Prints: 12
print(multipliers[2](6))  # Prints: 18
print(multipliers[3](6))  # Prints: 24





# Same as above but using lambda.

def create_multiplier_functions(n):
    
    return [lambda arg, i=i: arg * i for i in range(1, n+1)]
    
    
# Example usage
multipliers = create_multiplier_functions(4)
print(multipliers[0](6))  # Should print 6 (6*1)
print(multipliers[1](6))  # Should print 12 (6*2)
print(multipliers[2](6))  # Should print 18 (6*3)
print(multipliers[3](6))  # Should print 24 (6*4)








def running_total_maker(subtotal = 0):
    total = 0
    def add_to_total(number):
        nonlocal total
        total += number + subtotal
        return total
        
    return add_to_total

add_numb = running_total_maker()
print(add_numb(5)) # Output: 5
print(add_numb(1)) # Output: 6

"""
Outer scope variables (from parent functions) can be read but not modified by an inner (child) function.  There are two exceptions to this below:
1. To use outer scope variables on the left side of an assignment in an inner function, the 'nonlocal' keyword can be used. 
2. Only use mutable data types, such as a list, see next example below:***
"""





# Challenge: Write a closure that counts the number of times it has been called. 
def outer():
    tally = [0]
    def inner():
        tally[0] += 1 # Using a mutable data type allows modification of outer scope variable***
        return tally[0]
    return inner

start_tally = outer()
print(start_tally()) # Output: 1
print(start_tally()) # Output: 2
print(start_tally()) # Output: 3







import random

def outer():
    multiplier = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    def inner(operand):
        return operand * multiplier
    
    return inner

multiply = outer()
print(multiply(1))







# Actually useful use case for closures:
def caching_function_factory(func):
    cache = {}
    def cached_function(*args):
        if args in cache:
            return str(cache[args]) + ' (cached)'
        result = func(*args)
        cache[args] = result
        return result
    return cached_function

# Example usage
def compute_expensive_operation(x, y):
    # Simulate an expensive operation
    return x * y  # Replace with a more expensive computation if desired

cached_operation = caching_function_factory(compute_expensive_operation)
print(cached_operation(1, 10)) # Output: 10
print(cached_operation(1, 10)) # Output: 10 (cached)


# First print staement:
# caching_function_factory executed with compute_expensive_operation(x, y) as arg
# initialise cache dictionary
# return cached_function: cached_operation is a reference to cached_function
# cached_operation is called: calling cached_function with args 1, 10
# result = func(*args) executes func: compute_expensive_operation(x, y)
# so result = x*y = 1*10= 10
# cache[1, 10] = 10
# return 10
# print 10
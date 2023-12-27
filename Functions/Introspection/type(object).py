type(object)

'''
The type() function in Python is used to determine the class type of an object. It returns the class object that the argument belongs to. 
In Python, classes and types eventually became the same thing.  
This function is useful for checking the type of an object at runtime. It can also be used to compare the type of an object against a known type.
'''





number = 42
text = "Hello World"

# Using type() to find out the type of variables
print(type(number))  # Output: <class 'int'>
print(type(text))    # Output: <class 'str'>






class ExampleClass:
    pass

obj = ExampleClass()
print(type(obj))    # Output: <class '__main__.ExampleClass'>






class ExampleClass:
    pass

obj = ExampleClass()
# Remember the __name__ attribute only exists inside classes, not objects.  The below line works because its essentially saying class.__name__
print(type(obj).__name__)   # Output: ExampleClass





try:
    print("5"/0)
except Exception as e:
    print(type(e).__name__, e) # Output: TypeError






# class type(name, bases, dict, **kwds)

"""
With three arguments, return a new type object. This is essentially a dynamic form of the class statement. The name string is the class name and 
becomes the __name__ attribute. The bases tuple contains the base classes and becomes the __bases__ attribute; if empty, object, the ultimate base 
of all classes, is added. The dict dictionary contains attribute and method definitions for the class body; it may be copied or wrapped before becoming 
the __dict__ attribute. The following two statements create identical type objects:
"""

#1
class X:
    a = 1

#2
X = type('X', (), dict(a=1))





F = type('Food', (), {'remember2buy': 'spam'}) # is the same as:


class Food:
    remember2buy = 'spam'

F = Food


# Note that capital 'F' here is non-conventional.



# Instance instantiation can also be done dynamically:

food_instance = type('Food', (), {'remember2buy': 'spam'})()
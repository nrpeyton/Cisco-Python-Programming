type(object)

'''
The type() function in Python is used to determine the class type of an object. It returns the class object that the argument belongs to. 
In Python, classes and types are essentially the same thing.
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
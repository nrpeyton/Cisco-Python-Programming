setattr(object, name, value)

'''
The setattr() function assigns a value to an object's attribute. If the attribute does not exist, setattr will create it. 
This function accepts three arguments: the object, the attribute name, and the value to assign to that attribute. 
This is particularly useful for dynamically setting attributes based on runtime conditions, allowing greater flexibility in how objects are manipulated.
'''

class MyClass:
    attribute = "Old value"

obj = MyClass()

# Using setattr() to change the value of 'attribute'
setattr(obj, 'attribute', "New value")
print(obj.attribute)  # Output: New value

# Using setattr() to add a new attribute 'new_attribute'
setattr(obj, 'new_attribute', "Value of new attribute")
print(obj.new_attribute)  # Output: Value of new attribute






# Introspection: Increment all integer attributes of 'obj' that start with 'i'.
class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

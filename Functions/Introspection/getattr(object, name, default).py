getattr(object, name, default)

'''
The getattr() function in Python is used to retrieve the value of an attribute from an object. If the attribute exists, its value is returned. 
If the attribute does not exist and a default value is provided, that default is returned; otherwise, AttributeError is raised. 
This function is especially useful in situations where attribute names are determined dynamically and you want to safely fetch their values 
without risking an AttributeError.
'''

class MyClass:
    attribute = "This is an attribute value"

obj = MyClass()

# Using getattr() to retrieve the value of 'attribute'
print(getattr(obj, 'attribute'))  # Output: This is an attribute value

# Using getattr() with a default value if the attribute does not exist
print(getattr(obj, 'nonexistent_attribute', 'Default Value'))  # Output: Default Value
isinstance(object, type) # checks if object is an instance of type or a subclass thereof. Returns True or False.
isinstance(object, classinfo) # arg 2 must be a type, a tuple of types, or a union.
'''
object: The instance to check.
type: The type to check against (or a tuple of types to check against).
Examples:
'''

isinstance(5, int) # True
isinstance(5.0, float) # True
isinstance("Hello", str) # True
print(isinstance(5, (int,float) )) # True     If a tuple is used, 'OR' is applied, not 'AND'.


class myObj:
  name = "John"
y = myObj()
x = isinstance(y, myObj) # True


# Used for type-checking and ensuring code robustness.


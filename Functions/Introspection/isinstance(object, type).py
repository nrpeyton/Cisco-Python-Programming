isinstance(object, type) # checks if object is an instance of type or a subclass thereof. Returns True or False.

'''
object: The instance to check.
type: The type to check against (or a tuple of types to check against).
Examples:
'''

isinstance(5, int) # True
isinstance(5.0, float) # True
isinstance("Hello", str) # True


class myObj:
  name = "John"
y = myObj()
x = isinstance(y, myObj) # True


# Used for type-checking and ensuring code robustness.


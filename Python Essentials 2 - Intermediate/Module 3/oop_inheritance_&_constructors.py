# Subclasses inherit the attributes of the superclass...
class Parent:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Child(Parent):
    pass

obj = Child('a', 'b', 'c')

print(obj.a, obj.b, obj.c) # Output: a b c





# ...Except when overridden; the constructor in the subclass overrides the super's constructor causing an AttributeError: 'child object has no attribute 'a'.
class Parent:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Child(Parent):
    def __init__(self, a, b, c):
        pass

obj = Child('a', 'b', 'c')

print(obj.a, obj.b, obj.c) # Output: AttributeError: 'child' object has no attribute 'a'





# If we need a constructor in the subclass (i.e., to only add an extra attriburte 'd'), we can still make use of the super's constructor by invoking it inside the sub's constructor.
class Parent:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Child(Parent):
    def __init__(self, a, b, c, d):
        Parent.__init__(self, a, b, c) # Extra: `Parent.__init__(self, a, b, c)` could be replaced with `super.()__init__(a, b, c)`
        self.d = d

obj = Child('a', 'b', 'c', 'd')

print(obj.a, obj.b, obj.c, obj.d) # Output: a b c d





'''
This behaviour would be the same for all overridden attributes, not just the constructor.

In order to find any object/class property, Python looks for it inside:
1. The object itself;
2. All classes involved in the object's inheritance line from bottom to top;
3. If there is more than one class on a particular inheritance path, Python scans them from left to right;
4. If both of the above fail, the AttributeError exception is raised.
'''
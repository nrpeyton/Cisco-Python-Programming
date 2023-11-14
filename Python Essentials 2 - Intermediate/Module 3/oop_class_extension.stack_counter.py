'''                                       3.2.1.14 LAB: Extending Stack Class with Counter

DIFFICULTY: Easy/Medium
TIME: 20-45 minutes

OBJECTIVES:
- Improve skills in defining classes.
- Utilize existing classes to create new classes with added functionalities.

SCENARIO:
Extend the Stack class behavior to count all elements that are pushed and popped by defining a subclass. Implement a property for counting pop operations, initializing it to zero in the constructor, and provide a method to return the value (name it get_counter()). The task includes following the provided Stack class and ensuring the code outputs 100.
'''




class Stack:
    def __init__(self): # constructor
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

# sub-class of Stack
class CountingStack(Stack):
    def __init__(self): # own constructor
        Stack.__init__(self) # calling parent's constructor
        self.__counter = 0 # initialise counter

    def get_counter(self):
        return self.__counter # return counter's value initialised in CountingStack subclass.

    def pop(self):
        Stack.pop(self) # call the pop function in the base (aka parent) class
        self.__counter += 1 # add to counter

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())





'''
An improved version counts all popped values instead of just the number of pops.  The output is 4950.  The CountingStack.pop() method
would be changed to:

    def pop(self):
        var = Stack.pop(self)
        self.__counter += var
'''
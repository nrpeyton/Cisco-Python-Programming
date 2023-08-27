                                        #   C L A S S   V A R I A B L E S

class ExampleClass:
    varia = 1
    def __init__(self, val):
        varia = 10 # local variable only (nothing to do with the class variable above)
        ExampleClass.varia = 2 # changes class variable above.  printed first as just a class variable (no object or instance), but then printed again below it when used in new object (instance)
        self.varia += 1 # updates the instance


object1 = ExampleClass(2)
print(ExampleClass.varia)
print(object1.varia)



'''
Naming the variable is the most important aspect of the example because:
Changing the assignment to self.varia = val would create an instance variable of the same name as the class's one;
Changing the assignment to varia = val would operate on a method's local variable; (we strongly encourage you to test both of the above cases - this will make it easier for you to remember the difference)
'''

''' SUMMARY:
variable = value (only nested in class)         can be accessed as only a class variable directly, but also used/shared in all created objectes (instances)
variable = value (only nested in __init__)      no scope outside its own function
self.variable = value (nested in __init__)      scope is to separate objects; shadows (overrides) class variable when set

'''








                                    #   C H E C K   A N   A T T R I B U T E ' S   E X I S T E N C E
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()
                                        # outputs:
print(hasattr(example_object, 'b'))     # true
print(hasattr(example_object, 'a'))     # true
print(hasattr(ExampleClass, 'b'))       # false - line only checks for class variables
print(hasattr(ExampleClass, 'a'))       # true


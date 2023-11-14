# You're going to negate the __venomous property of the version_2 object, ignoring the fact that the property is private. How will you do this?

class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False

version_2 = Python()





# The expression:

'mike' > 'Mike'

# is?

'''
ASCII 65(A) to 90(Z)
ASCII 97(a) to 122(z)

Python string comparison ends at the first difference; the string with the higher ASCII value at that point is greater.
'''




# What is the expected output of the following code?

try:
    print("5"/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")





# The following code does what?

print(float("1, 3"))






'''
Which of the following are examples of Python built-in concrete exceptions? (Select two answers):

ArithmeticError

ImportError

BaseException

IndexError
'''










'''
Concrete Exceptions:

ValueError
TypeError
IndexError
KeyError
ImportError
NameError
FileNotFoundError
ZeroDivisionError
AttributeError
SyntaxError

Not Concrete:

BaseException
ArithmeticError
IO Error
OS Error

'''







# What is BOM?







# What is the length of the following string assuming there is no whitespaces between the quotes?

"""
"""






# What is the expected output of the following code?

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)






# Which of the following lines describe a true condition?

'smith' > 'Smith'

'Smiths' < 'Smith'

'Smith' > '1000'

'11' < '8'





# What is the expected output of the following code?

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])





# What is the expected result of the following code?

s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)






# What is the expected value of the result variable after the following code is executed?

import math
result = math.e == math.exp(1)






# (Complete the sentence) Setting the generator's seed with the same value each time your program is run guarantees that...






# Which of the platform module's functions will you use to determine the name of the CPU running inside your computer?






# What is the expected output of the following snippet?

import platform
print(len(platform.python_version_tuple()))






# You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?






# You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?






# Some additional and necessary packages are stored inside the D:\Python\Project\Modules directory. Write a code ensuring that the directory is traversed by Python in order to find all requested modules.






# The directory mentioned in the previous exercise contains a sub-tree of the following structure: abc/def/mymodule.py.  Assuming that D:\Python\Project\Modules has been successfully appended to the sys.path list, write an import directive letting you use all the mymodule entities.






# What is __pycache__ and __init__.py ?
'''
__pychache__ is a folder containing semi-compiled code (bytecode) stored in the same folder as your scripts.  It simply allows subsequent program runs to execute faster.
The folder is usually hidden by vscode to prevent clutter, except when creating directories with user created modules.

__init__.py is an often empty file that indicates to Python that its containing directory is a Package.  Prior to Python 3.3, this was required.

'''
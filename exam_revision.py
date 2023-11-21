# List of all questions to be revised:

#Q1 You're going to negate the __venomous property of the version_2 object. How will you do this?

class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False

version_2 = Python()

# Answer: version_2._Python__venomous = not version_2._Python__venomous




'''
#Q2 What is the output of the following expression?

'mike' > 'Mike'

Hint: 
ASCII 65(A) to 90(Z)
ASCII 97(a) to 122(z)
Python string comparison ends at the first difference; the string with the higher ASCII value at that point is greater.
'''

# Answer: True





# Q3 What is the expected output of the following code?

try:
    print("5"/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")

# Answer: Prints "some"






# Q4 The following code does what?

print(float("1, 3"))

# Answer: ValueError




''' Q5
Which of the following are examples of Python built-in concrete exceptions? (Select two answers):

ArithmeticError

ImportError

BaseException

IndexError
'''

# Answer: IndexError, ImportError








'''Q6
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







# Q7 What is BOM?

# Answer: Byte Order Mark





# Q8 What is the length of the following string assuming there is no whitespaces between the quotes?

"""
"""

# Answer: 





#Q9 What is the expected output of the following code?

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)

# Answer: It is either hard or possible.




# Q10 Which of the following lines describe a true condition?

1. 'smith' > 'Smith'

2. 'Smiths' < 'Smith'

3. 'Smith' > '1000'

4. '11' < '8'

# Answer: 1, 4



# Q11 What is the expected output of the following code?

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])

# Answer: 'are'



# Q12What is the expected result of the following code?

s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)

# Answer: 




# Q13 What is the expected value of the result variable after the following code is executed?

import math
result = math.e == math.exp(1)

# Answer: True




# Q14 (Complete the sentence) Setting the generator's seed with the same value each time your program is run guarantees that...

# Answer: You'll get the same output.





# Q15 Which of the platform module's functions will you use to determine the name of the CPU running inside your computer?

# Answer: platform.processor()





# Q15 What is the expected output of the following snippet?

import platform
print(len(platform.python_version_tuple()))

# Answer: 3




# Q16 You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?

# Answer:
import sys
if __name__ == '__main__':
    sys.exit()




# Q17 Some additional and necessary packages are stored inside the D:\Python\Project\Modules directory. Write a code ensuring that the directory is traversed by Python in order to find all requested modules.

# Answer: 
import sys
sys.path.append('D:\\Python\\Project\\Modules')




# Q18 The directory mentioned in the previous exercise contains a sub-tree of the following structure: abc/def/mymodule.py.  
# Assuming that D:\Python\Project\Modules has been successfully appended to the sys.path list, write an import directive letting you use all the mymodule entities.

# Answer: 
import abc.def.mymodule



# Q19 What is __pycache__ and __init__.py ?
'''
__pychache__ is a folder containing semi-compiled code (bytecode) stored in the same folder as your scripts.  It simply allows subsequent program runs to execute faster.
The folder is usually hidden by vscode to prevent clutter, except when creating directories with user created modules.

__init__.py is an often empty file that indicates to Python that its containing directory is a Package.  Prior to Python 3.3, this was required.

'''
# Answer: 
__pycache__ is a directory that stores semi-compiled code (bytecode) of modules the first time they're imported so that subsequent runs are faster
__init__.py is placed in directories of packages (and subpackages) to let Python know they are packages.



''' Q20 
# Explain how to:
1. Check pip version?
2. Install pip package?
3. Install pipo package only for a specific user ?
'''
# Answer: 
1. pip3 --version
2. pip3 install package_name
3. pip3 install --user package_name


'''
Q21 :  When you use pip to install a package that requires one or more dependencies, then:

-you'll have to install all the dependencies by yourself before you install the desired package
-pip will take care of everything by itself
-you'll have to install all the dependencies by yourself after you install the desired package
-the package will install all the dependencies during its first run
'''
# Answer: -pip will take care of everything by itself



'''
Q22:  A list of package's dependencies can be obtained from pip using its command named:

-dir
-show
-list
-deps
'''
# Answer: -show




'''
Q23:  What is true about the pip search command? (Select three answers)

1. it needs working Internet connection to work
2. all its searches are limited to locally installed packages
3. it searches through package names and summaries
4. it searches through all PyPI packages
'''
# Answer: 1, 3, 4




'''
Q24:   During the first import of a module, Python deploys the pyc files in which of the below directories?
(Note: Although bytecode (pyc files) are created on a script's first execution, they aren't necessarily stored in the __pycache__ folder).

1. __pycache__
2. mymodules
3. hashbang
4. __init__
'''

# Answer: 1





'''Q25 For each print statement, what are the possible outputs?
from random import randrange, randint

1. print(randrange(1), end= ' ')
2. print(randrange(0, 1), end= ' ' )
3. print(randrange(0, 20, 5), end= ' ')
4. print(randint(0, 2), '\n')

Answers:
1. 0
2. 0
3. 0, 10, 15
4. 0, 1, 2


'''






'''
Q26:  
A) How to use pip to remove an installed package?
1. pip remove package
2. pip --uninstall package
3. pip uninstall package
4. pip install --uninstall package

B) What is the command to a) i) view all installed packages? ii) view a package's dependencies? iii) search for packages?

Answers: 
A) 3. pip uninstall package
B) pip list
'''



'''
Q27:   Choose the true statements. (Select two answers)

1. The version function from the platform module returns a string with your Python version
2. The processor function from the platform module returns an integer with the number of processes currently running in your OS
3. The version function from the platform module returns a string with your OS version
4. The system function from the platform module returns a string with your OS name
'''
# Answer: 3, 4




'''
Q28:   When a module is imported, its contents:

1. are ignored
2. may be executed (explicitly)
3. are executed once (implicitly)
4. are executed as many times as they are imported
'''
# Answer: 3




# Q29 What is the output of: factorial(4)
# Answer: 24




# Q30 What is the output of math.log10(100)
# Answer: 2




# Q31 What is the output of a) math.ceil(2.5) and b) math.floor(2.5)?
# Answer: a) 3.0 b) 2.0




''' Q32 Python's math module includes a function that calculates the exponential of a given number, effectively computing Euler's number 
(approximately 2.71828). Can you name this function and demonstrate how to use it to calculate the exponential of 1?

Answer: 
import math
math.exp(1)
'''




# Q33 What is the result of math.floor(-5.1) and math.ceil(-2.5)?
# Answer: -6.0 and -2.0




# Q34 What is the result of math.floor(-20.5) and math.ceil(-12.89)?
# Answer: 




# Q35 What is the output of print(math.radians(90))?
# Answer: 1.57




''' Q36
a) What is the output of print("5"/0) and b) what is the output of int("1, 2")

Answer: 
a) TypeError
b) ValueError
'''



''' Q37
What is the expected output of the following code?

import math

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("fine")
finally:
    print("the end")

Answer: 

'''





# Q38:
class Bird:
    aviary = 0
    def __init__(self, species):
        self.species = species
        Bird.aviary += 1
    def __str__(self):
        return self.species + " chirps."

class SongBird(Bird):
    def __str__(self):
        return super().__str__() + " Singing a melody."

class HuntingBird(Bird):
    def __str__(self):
        return super().__str__() + " Watching for prey."

    
''' 
Your Task:
Define a HuntingBird subclass named ForestHuntingBird, and equip it with an __str__() method overriding an inherited method of the same name. 
The new bird's __str__() method should return the string "<species> chirps. Watching for prey. Loves the forest!"
'''
# Answer:
class ForestHuntingBird(HuntingBird):
    def __str__(self):
        return super().__str__() + "Loves the forest!"






''' Q39:
True or False: In Python, the method str.upper() creates a new string and does not modify the original string.

Choose True or False.
'''
# Answer: True






''' Q40:
Write a Python code snippet to concatenate the following two strings with a space between them: "Hello" and "World".  Use a string method.

Answer:
' '.join(['Hello', 'World'])

'''





# Q41: What will be the output of the following code?
s = "abcd"
print(s[0:4:-1])

# Answer:





# Q42: Write a snippet to convert "This is a string" to "string a is This"
'''Answer:

print(' '.join("This is a string".split()[::-1]))

# or

s = "This is a string".split()
s.reverse()
print(' '.join(s))
'''




# Q43: What is the output of the following snippet?

s = "Coffee is black"
print(s[::-3])

'''
A) Cf  a
B) Coffee is black
C) Ca  fc
D) klsef
'''
# Answer: D





# Q44: Name three list methods that return a value and seven that don't.

'''
Answer:

Returners: 
Non-returners: 
'''





# Q45: How many arguments does the string class's 'join' method method take?
# Answer: 






# Q46: What is the result of math.hypot(7, 0)
# Answer: 





''' Q47: Write three snippets to iterate through the dictionary:
a) its key-value pairs
b) only its keys
c) only its values
'''

dic = {1: 'one', 2: 'two', 3: 'three'}

''' Answer:



'''







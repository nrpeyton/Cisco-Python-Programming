# pylint: disable=all
# type: ignore
#region Code without hints

# List of all questions to be revised.  Every question is a flavour of one I got wrong, added here each time.
# One set of '*****' indicates I got the question wrong again a number of days after previously revising it.  Additional sets, wrong again, and so on.
# All answers are corrected before this document is saved by me.  If any are blank I deleted the answer as extra reminder to re-revise that question.  No answers will be 'left incorrect' before I upload this file to github.

#Q1 You're going to negate the __venomous property of the version_2 object. How will you do this?      *****

class Snake:
    total_snakes = 1
    prey_count = 0

    def __init__(self):
        self.body_length_ft = 3
        self.__isvenomous = False

snake_instance = Snake()


''' Answer: 
snake_instance._Snake__isvenomous = not snake_instance._Snake__isvenomous
'''




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

'''
try:
    print("5"/ 0)
except ArithmeticError:
    print("Arithmetic Error Encountered")
except ZeroDivisionError:
    print("Division by Zero Error")
except:
    print("General Error")
'''

# Answer: General Error - Type Error






# Q4 The following one-liners output what?                

print(float("1, 3"))



# Answer: ValueError



print(float("1,3"))



# Answer: ValueError



print(float("1. 3"))



# Answer: ValueError



print(float("1.3"))



# Answer: 1.3





''' Q5
Which of the following are examples of Python built-in concrete exceptions? (Select two answers):

ArithmeticError

ImportError

BaseException

IndexError
'''

# Answer: ImportError and IndexError








# Q6  what is the output of a, b, c, d, e, and f? 

print(math.floor(-29) + math.trunc(10.6))                                   #a) 
print([i for i in range(1, math.ceil(11))])                                 #b) 
print([i for i in range(5) if i % 2 == 0 and i % 1 == i])                   #c) 

print('\n', 5 is 5.0)                                                       #d) 
print(5 == 5.0)                                                             #e) 
print(5 is 5)                                                               #f) 

# g) What data type is returned by math.floor(), math.ceil() and math.trunc() ?

'''
Q6 Answers:
a) -19
b) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c) [0]

d) False
e) True
f) True

g) INT
'''







# Q7 What is BOM?

# Answer: Byte Order Mark




# Q8 What is the length of the following string assuming there is no whitespaces between the quotes?

"""
"""

# Answer: 1





#Q9 What is the expected output of the following code?

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)

# Answer: It is either hard or possible




# Q10 Which of the following lines describe a true condition?                               20-2

1. 'smith' > 'Smith' 

2. 'Smiths' < 'Smith' 

3. 'Smith' > '1000' 

4. '11' < '8' 

5. '!' < '5'

# Answer: True, False, False, True, False






# Q11 What is the expected output of the following snippets?            1-2

# A) 
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])

# Answer: are


# B)                                                                            nnnnn
x = '\t\\'*2 + '\t'
print(len(x.split('t')))

# Answer: 1





# Q12 A) What is the expected result of the following code?         mmmmm      mmmmm           25-1            19-2

s1 = '45.6'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)

# Answer: ValueError

# Q12 B) What if s1 was a float?

# Answer: False



# Q13 What is the expected value of the result variable after the following code is executed?                   20-2

import math
result = math.e == math.exp(1)

# Answer: 




# Q14 (Complete the sentence) Setting the generator's seed with the same value each time your program is run guarantees that...

# Answer: The sequences will appear in the same order.





# Q15 Which of the platform module's functions will you use to determine the name of the CPU running inside your computer?              20-2

# Answer:  FIND OUT WHAT HAPPENS FOR PLATFORM.PROCESSOR AND PLATFORM.MACHINE FOR WINDOWS.





# Q15 What is the expected output of the following snippet?

import platform
print(len(platform.python_version_tuple()))

# Answer: 3




# Q16 You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?                 20-2

# Answer:
import sys
if __name__ == '__main__':
    sys.exit() ##### sys or os???





# Q17 Some additional and necessary packages are stored inside the D:\Python\Project\Modules directory. Write a code ensuring that the directory is traversed by Python in order to find all requested modules.

# Answer: 
import sys
sys.path.append('D:\\Python\\Project\\Modules')  or  sys.path.append('D:/Python/Project/Modules')                                                                                                                                                                    import sys
                                                                                                                                                                        sys.path.append('D:/Python/Project/Modules') or sys.path.append('D:\\Python\\Project\\Modules')




# Q18 The directory mentioned in the previous exercise (D:\Python\Project\Modules) contains a sub-tree of the following structure: abc/def/mymodule.py.        *****        *****
# Assuming that D:\Python\Project\Modules has been successfully appended to the sys.path list, write an import directive letting you use all the mymodule entities.

# Answer: 
from abc.def import mymodule #(preferred) 
#or  
import abc.def.mymodule # (would require using an alias, or using the full directive for any functions, etc)




# Q19 What is __pycache__ and __init__.py ?

# Answer: 
# Semi-Compiled python bytecode, created automatically the first time a module is imported.  Can speed up code execution.
# __init__.py is a file that tells Python to treat the current folder as a standard package, even if it is empty. It only needs to exist.  Or, it can additionally be configured to streamline import statements.
























'''
__pychache__ is a folder containing semi-compiled code (bytecode) stored in the same folder as your scripts.  It simply allows subsequent program runs to execute faster.
The folder is usually hidden by vscode to prevent clutter, except when creating directories with user created modules.

__init__.py is an often empty file that indicates to Python that its containing directory is a Package.  Prior to Python 3.3, this was required.  It is also useful for 
streamlining/simplifying import statements.

'''








'''
Q20 :  When you use pip to install a package that requires one or more dependencies, then:

-you'll have to install all the dependencies by yourself before you install the desired package
-pip will take care of everything by itself
-you'll have to install all the dependencies by yourself after you install the desired package
-the package will install all the dependencies during its first run
'''
# Answer: -pip will take care of everything by itself



'''
Q21:  A list of package's dependencies can be obtained from pip using its command named:

dir
show
list
deps
'''
# Answer: pip show




'''
Q22:  What is true about the pip search command? (Select three answers)

1. it needs working Internet connection to work
2. all its searches are limited to locally installed packages
3. it searches through package names and summaries
4. it searches through all PyPI packages
'''
# Answer: 1, 3, 4 (now obsolete)




'''      *****
Q23:   During the first import of a module, Python deploys the pyc files in which of the below directories?
(Note: Although bytecode (pyc files) are created on a script's first execution, they aren't necessarily stored in the __pycache__ folder).

1. __pycache__
2. mymodules
3. hashbang
4. __init__
'''

# Answer: __pycache__





'''Q24 For each print statement, what are the possible outputs?
from random import randrange, randint

print(randrange(1), end= ' ')
print(randrange(0, 1), end= ' ' )
print(randrange(0, 20, 5), end= ' ')
print(randint(0, 2), '\n')

Answers:
1. 0
2. 0
3. 0, 5, 10, 15
4. 0, 1, 2            mmmmm


'''






'''                                                                                                            mmmmm            mmmmm           21-1            20-2
Q25:
A) What apt command removes installed software? And what pip command removes an installed package?
# Answer: sudo apt remove packagename       pip uninstall packagename

B) What is the pip command to view all installed packages?
# Answer:  pip list

C) What is the pip command to view a package's dependencies?
# Answer: pip show packagename

D) What is the pip command to search for packages?
# Answer: pip search packagename (no longer works)

E) What is the pip command to update a package?
# Answer: pip install -U packagename

F) In the command `pip --version`, is 'version' a command or an option?
# Answer: An option of the 'pip' command itself                                       'Version' is' a general option of the pip command itself.  The typical usage is `pip <command> [options] <target>`.  But here, pip is the only command, so the --version flag follows directly.

G) What is the pip command if you only wanted to install version 1.0.4 of a package for the current user?
# Answer: pip install --user 'packagename==1.0.4'
'''



''' Q26                                                 mmmmm
# Explain how to:
1. Check pip version?
2. Install pip package?
3. Install pip package only for the current user ?
'''
# Answer: 
1. pip --version
2. pip install packagename
3. pip install --user packagename





'''
Q27:   a) Choose the true statements. (Select two answers)

1. The version function from the platform module returns a string with your Python version
2. The processor function from the platform module returns an integer with the number of processes currently running in your OS
3. The version function from the platform module returns a string with your OS version
4. The system function from the platform module returns a string with your OS name
'''
# Answer: 3, 4



# b) What is the output of the following snippet?                                                                           21-1           REDO FOR WINDOWS FOR: platform.machine(), platform.processor(),                      

import platform
print(platform.machine(), platform.processor(), platform.system(), platform.platform(), platform.version())

# Answer:    
"""
x86_64
x86_64
Linux                               or  Windows
Linux Kernel Build Info and CPU     or  (Windows):   Windows + Build Info & Version + CPU
Linux Distribution + version        or  (Windows):   Shorter version number only
"""




















""" Answers (for referece)
#        x86 x86 linux linux_kernel_info linux_distro
# or     x86 x86 windows 'windows 10 [build_info]' build_info
"""














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

# Answer: a) 3  b) 2




''' Q32 Python's math module includes a function that calculates the exponential of a given number, effectively computing Euler's number 
(approximately 2.71828). Can you name this function and demonstrate how to use it to calculate the exponential of 1?

Answer: 
import math
math.exp(1) == math.e
'''




# Q33 What is the result of: a) math.floor(-55.19) and b) math.ceil(-3.7)?
# Answer:
# a) -56
# b) -3



# Q34 What is the result of:      *****      *****      mmmmm      mmmmm
s = '123456789'
for i in range(len(s)):
    print(math.floor(int(s[i])) and math.ceil(int(s[i])))

''' Answer:
1
2
3
4
5
6
7
8
9
'''



# Q35 What is the output of print(math.radians(90))?                                        20-2
# Answer: 




''' Q36
a) What is the output of print("5"/0) and b) what is the output of int("1, 2")

Answer: 
a) TypeError
b) ValueError
'''



# Q37: What is the expected output of the following code snippet?
import math

try:
    print(math.sqrt(-16))
except ValueError:
    print("dreamland")
else:
    print("smooth sailing")
finally:
    print("curtain call")

# Answer: 
"""
dreamland
curtain call
"""





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
         return  super().__str__() + 'Loves the forest!'







''' Q39:
True or False: In Python, the method str.upper() creates a new string and does not modify the original string.

Choose True or False.
'''
# Answer: True





''' Q40:      *****
Write a Python code snippet to concatenate the following two strings with a space between them: "Greetings" and "Everyone".  Use a string method.

Answer:
' '.join(['Greetings', 'Everyone'])



'''






# Q41: a)What will be the output of the following code?     mmmmm     mmmmm
s = 'abcd'
print(s[0:1:-1])

# Answer: ''



# Q41: b)What will be the output of the following code?     mmmmm     mmmmm                        Remember to ACTUALLY step backwards when counting!
s = "abcd"
print(s[0:4:-1])

# Answer: ''



# Q41: c)What will be the output of the following code?     mmmmm     mmmmm
s = 'abcde'
print(s[2:4:-1])

# Answer: ''




# Q41: d)What will be the output of the following code?     mmmmm     mmmmm
s = "abcd"
print(s[2:0:-1])

# Answer: cb




# Q41: e)What will be the output of the following code?     mmmmm     mmmmm
s = "abcd"
print(s[-2:-3:-1])

# Answer: c





# Q42: Write a Python snippet to reverse the word order in the sentence 'Exploration ignites curiosity'.      *****


'''Answer:

l = 'Exploration ignites curiosity'.split()
l.reverse()
print(' '.join(l))

#or

' '.join('Exploration ignites curiosity'.split()[::-1])



















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
# Answer: klsef



# Q44 a): Name four list methods that return a value and seven that don't.                                  

'''
Answer:
pop
count
index
????copy                                                                                20-2

insert
append
extend
reverse
sort
remove
clear


'''


# Q44 b): Which string methods don't return a value?

# Answer: Actually ALL string methods DO return a value!



# Q44 c): Which 'only' iterables can list methods be used on?  How can we extract a substring from a string?        mmmmm

# Answer: Lists!  List methods cannot be used on other iterables!  Slices[3:7] create a copy.




# Q45: How many arguments does the string class's 'join' method take?  And what data type does it take?       *****                 20-2

# Answer: 






# Q46: What is the result of math.hypot(6, 0)
# Answer: 6




''' Q47: What is the result of math.hypot(1, 2)
a) 6.92
b) 4
c) 2
d) 2.23
'''
# Answer: 2.23






''' Q48: Write three snippets to iterate through the dictionary:                         20-2
a) its key-value pairs
b) only its keys
c) only its values
'''

dic = {1: 'one', 2: 'two', 3: 'three'}

''' Answer:
a) 
b) for i in dic.keys()
c) for i in dic.values()

'''




# Q49: A) What is the ouput of this?    B) And what if we removed the first two lines?           mmmmm                20-2

lst_obj = (-1, 11, 0)
lst_obj[0] += 1
obj = range(1, 11, 0)

# Answer (A): TypeError.
# Answer (B): 






# Q50: Without worrying about missing characters or duplicate characters, what will be the likely range of the first element and last element?          mmmmm
# An approximate range can be a-c or y-z.
from random import randint

lst = [chr(randint(ord('a'), ord('z'))) for i in range(25)]
sorted(lst)
print(lst)


# Answer: It won't be sorted into order because the 'sorted()' function does NOT work in-place.  It returns a value that hasn't been been assigned to anything here.                                                                                                                                                      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> no change, because sorted() returns a value.  The inplace list.sort() method's target is prefixed to it where as the sorted() function's target is its first arg.







# Q51: What is the output?      nnnnn
def fun(n):
    return -n

n = -25
print(fun(n))


# Answer: 25





# Q52: What is the output of snippets A and B?

# A)                                                                    nnnnn
for i in range(3):
    print("Apple:", i)
    if i == 1:
        break
else:
    print("Orange")

print("-----")



""" Answer:
Apple: 0
Apple: 1
-----
"""




# B)                                                                    nnnnn
j = 0
while j < 3:
    print("Mango:", j)
    j += 1
else:
    print("Watermelon")



""" Answer:
Mango: 0
Mango: 1
Mango: 2
Watermelon
"""







# Q53: a) Why is a's assignment line not erroneous?  And which list's elements are mapped to 'x'?          nnnnn
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['z', 'a', 'b']

def fun(xxyz):
    return xxyz in list1
a = list(filter(fun, list2))
print(a)

# Answer: filter essentially "fills in" fun's argument by mapping it to filter's second argument, list2.  Each element is passed to the function, and the false ones filtered out.                                                                                                                                                            >>>>>>>>>>>>>>>>>>>>>>>>In the assignment, 'fun' is a reference to the 'fun' function.  Filter calls fun(xxyz) with list2 mapped to 'xxyz'. Filter only returns the true results.


# Q53: b) Keeping only the first two lines and the last line from the snippet above, convert the rest of the snippet to its lambda equivalent.

""" Answer: 
a = list(filter(lambda xxyz: xxyz in list1, list2))
"""

# Q53: c) If map() and filter() are multiple choice answers in an exam, how can we quickly eliminate map()?                     21-1

# Answer: The map() answers will have the same number of elemements, but the filter() ones may have less.                                                                                                                                                    >>>>>>>>>>>>>>>>>>>>>>>> If there is a smaller number of elements in the output list vs the input target.





#  Q54: pass











# Q55: What is the output?          nnnnn                       20-2

elements = {}
for character in 'Gandalf':
    if character in 'Saruman':
        elements[ord(character)] = character
else:
    elements[ord('u')] = 'u'

for key in elements.keys():
    print(elements[key], end=' ')

# Answer: 







# Q56: What is the expected output of the following snippet ?               nnnnn

x = 5//2
func = lambda x:+3
print(func(x))



# Answer: 3







# Q57: What is the expected output of the following snippet

my_list = list('yoDA')
print(''.join(my_list).capitalize())


# Answer: Yoda






# Q58 a): What are the four types below (answer in the order they appear)?              nnnnn
import datetime

print(datetime.datetime.now())

# Answer: module, module, class, function                                                                                                                                              >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>module, module, class, function


# Q58 b): What are the four types below (answer in the order they appear)?              nnnnn
from datetime import datetime

print(datetime.now())

# Answer: module, class, class, function                                                                                                                                               >>>>>>>>>>>>>>>>>>>>>>>>>>>>module, class, class, function


# Q58 c): What are the rules for the 'import' keyword if used without 'from'?                       21-1            20-2

# Answer:                                                                                                                                                                               must be a module or a package.  If its only a package, the package's __init__.py file may need to be updated to access modules within it.



# Q59: What is the output?                                  nnnnn

list_1 = list('Chewie')
list_2 = list('Han')
list_3 = list('Luke')
    
try:
    list_1=list_2
    list_2.insert(0,list_3[0])
    assert list_1[0] == 'H'
except:
    print('Error')
else:
    print('OK')
finally:
    print('Done')

# Answer: Error, Done







# Q60: What is the output?                                  nnnnn               nnnnn

my_list = ['banana', 'tiger', '789Xy', 'Chess']
my_list.sort(key = lambda x: x[::-1])
print(my_list[0]) 

# Answer: banana





# Q61: What's the output?

class A:
    def __init__(self, x=5):
        self.x = x
    
class B(A):
    def __init__(self, y=2):
        super().__init__(y) 
    def set(self, y):
        self.x = y + 3
        return self.x
    
b = B()
print(b.set(b.x + 2))

# Answer: 7






# Q62: Whats the difference between regular and namespace packages in the context of __init__.py

# Answer: Standard packages require __init__.py in the root of the package, namespaces packages do not require an __init__.py file.

























# Answer: If we spread modules and subpackages across several sub-directories contained in a parent directory, this "root" directory previously required an
# __init__.py file before Python would recognise it as a package.  Since Python 3.3, an __init__.py file is no longer required.  Python
# can now (implicitly) treat this folder as a new 'namespace' package .  The only difference between namespace packages and regular packages is
# the existance of the __init__.py file. This means we can now use regular OS directories (folders) as packages.  The __init__.py file can still be
# useful for setting up more specific environments or even simplifying imports.  Packages continuing to use an __init__.py file are (still) known as 'regular' 
# packages.  This may be counter-intuative for someone new to Python because they can work with packages without ever encountering an __init__.py file.







# Q63: A) What is the output?    B) Can class variables be accessed by instances of those classes?          nnnnn       19-1
# C) Provide a reason for the answer to 'B' 

class Zodiac:
    Alpha = False
    def __init__(self, m, n):
        self.m = m
        self.__n = n
    def change(self, p):
        Zodiac.Alpha = p

leo = Zodiac(8, 6)
virgo = Zodiac(15, 7)
leo.__o = True
virgo.change(9)
print(leo.__dict__)
print(leo.Alpha)
print(virgo.Alpha)

""" Answers:
A) 
m: 8, _Zodiac__n: 6, __o: True
9
9



B) Yes                                                                                                                                                                          >>>>>>>>>>>>>>>>>   Yes class variables can be accessed by instances of those classes.  The value will be the same for all instances.
C) Class variables are shared across all instances of the class, allowing them to be accessed and modified by any instance.  All instances accessing a class variable will see the same location in memory.
"""






# Q64: A) What is the output?  B) What would happen if we removed the '+' from the open flag?                nnnnn

L = [f"{x}\n" for x in range(5, 15)]
f = open("modifiedfile.txt", "a+")
f.writelines(L)
f.seek(0)
print(f.read())
f.close()

# A) Answer:
"""
5
6
7
8
9
10
11
12
13
14
"""

# B) Answer: f.read() would raise an UnsupportedOperation error.








# Q65:                                                                                                                          nnnnn
# A) Can the list [5, 6, 8, 2, 4, 3, 10, 7, 9, 3] be generated by the line below?  Provide a reason.
from random import sample
x=sample([i for i in range(1,11)], 10)

# Answer: No.  Sample does not replace elements after they've been chosen. In other words, sample can't pick the same elemement twice.                                                                                                                                                        >>>>>>>>>>>>>>>>>>>>>>>>>  No, sample()'s algorithm is designed never to pick the same element, this ensures all returned elements are distinct.


# B) What is the output?    26-1

from random import sample
list = [i for i in range(-1, 3)]
x = sample(list, 5)
print(x)

# Answer: Raises a ValueError due to the requested sample-size being larger than the population.







# Q66 A): Which of the code snippets below can be used to obtain ['Spain','Brazil'] from nations?

nations = ['Spain','UK£','Germany!','France3','Brazil']

 
extracted = list(map(lambda x: x.isalnum(), nations))  
print(extracted)
 
extracted = list(filter(lambda x: x[-1].isalpha(), nations))
print(extracted)
 
extracted = list(map(lambda x: x.isalpha(), nations))
print(extracted)
 
extracted = list(filter(lambda x: x[-1].isalnum(), nations))
print(extracted)

# Answer: 2nd snippet



# Q66 B): Which character groups exclusively return 'True' for isalnum() ?

# Answer: Letters and numbers.

# Q66 C): Which character groups exclusively return 'True' for isalpha() ?

# Answer: Letters.








# Q67 A): Consider the following Python code:                                          nnnnn

class Planet:                    # line 1
    def __init__(self, name):    # line 2
        self.name = name         # line 3
                                  # line 4
class Earth(Planet):             # line 5
    #insert code here            # line 6
                                  # line 7
earth_instance = Earth("Earth")  # line 8
print(earth_instance)            # line 9

"""
Task: Which code snippet, when inserted at line 6, will make the above code produce the following output:
I am Earth, child of Planet
"""

# Option 1
def __str__(self):
    return "I am " + self.__name__ + ", child of " + super(self)

# Option 2
def __str__(self):
    return "I am " + self.name + ", child of " + Earth.__bases__[0].__name__

# Option 3
def __str__(self):
    return "I am " + self.name + ", child of " + Earth.super().__name__

# Option 4
def __str__(self):
    return "I am " + self.name + ", child of " + super().__name__



# Answer: Option 2

# Q67 B): What does super() return?  Where does Python look for an attribute suffixed to super() ?  And what can/can't __name__ be used on?

# Answers: super() returns a proxy object, and __name__ cannot be used on objects (instances) or variables.                                                                                                                                                  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>super().__name__ doesn't work because super() returns a 'proxy' object to access the parent class's methods, not the class itself. Since __name__ is a class attribute, not an object attribute, it can't be accessed through the proxy object returned by super().  It can be used on classes, functions and methods; and modules.

# Q67 C): What type is __bases__ and what does it contain?              nnnnn

# Answer: __bases__ is a tuple and it contains the direct superclasses themselves.  Option 2 works because __name__ can be used on a class. It returns a string.                                                                                                                                                   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Tuple containing a class's direct superclasses.





# Q68:                                                              nnnnn       20-1

"""
A) Why can't a class constructor return a value?

# Answer: Because the object (instance) is stored in the variable specified when instantiating the class.  If the constructor returned a value, the variable would store that value, not the object/instance.






















# Answer (for marking): Instantiating an instance stores it in a variable so it can be used.  If the constructor returned a value, Python would have to store it instead of a reference to the instance.


B) Why can't a class constructor be invoked directly from inside its class?  Can it be invoked from a subclass?

# Answer: Answer (for marking): A class cannot be invoked inside itself because it's not yet fully formed.  Python knows when the flow exits the class block, at which point, setting up the class's namespace is finalised and it
becomes instantiable.  In contrast, a class may be invoked from its subclass because its definition is complete.
"""






# Q69: What is the expected output of the following code snippets?                   nnnnn           20-1

# A)
planet_catalog = {1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars'}

try:
    for planet_index in range(len(planet_catalog)):
        if not(planet_catalog[planet_index + 1].isalpha()):
            raise ValueError
    print("Done")
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
except KeyError:
    print("KeyError")

# Answer: Done






# B)
book_archive = {
    1: 'Middlemarch', 2: 'Anna Karenina', 3: 'The Sun Also Rises', 4: 'The Old Man and the Sea',
    5: 'Great Expectations', 6: 'Heart of Darkness', 7: 'A Passage to India', 8: 'On the Road',
    9: 'A Farewell to Arms', 10: 'Dracula', 11: 'Slaughterhouse-Five', 12: 'The Stranger',
    13: 'Gone with the Wind', 14: 'The Call of the Wild', 15: 'The Scarlet Letter', 16: 'The Trial',
    17: 'The Picture of Dorian Gray', 18: 'The Metamorphosis', 19: 'Catch-22', 20: 'Rebecca',
    21: 'Bleak House', 22: 'Vanity Fair', 23: 'To the Lighthouse', 24: 'Les Misérables', 25: 'Fahrenheit 451'
}

try:
    for literature_index in range(len(book_archive)):
        if not(book_archive[literature_index + 1].isalpha()):
            raise ValueError
    print("Catalog Check Complete")
except ValueError:
    print("verror ")
except IndexError:
    print(" eirror")
except KeyError:
    print(" kerror")

# Answer: verror








# Q70: A) Is id(str1) != id(str2) True or False?
str1 = 'Hello'
str2 = 'Hello'
print(id(str1) != id(str2))


# Answer: False




# Q70: B) Is id(a) == id(b) True or False?
a = 256
b = 256
print(id(a) == id(b))


# Answer: True




# Q70: C) Is id(x) == id(y) True or False?
x = 257
y = 257
print(id(x) == id(y))


# Answer: True




# Q70: D) Is id(list1) == id(list2) True or False?
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1) == id(list2))


# Answer: False




# Q70: E) Is id(tup1) == id(tup2) True or False?
tup1 = (1, 2, 3)
tup2 = (1, 2, 3)
print(id(tup1) == id(tup2))


# Answer: True




# Q70: F) Is id(s1) == id(s2) True or False?
s1 = 'Hello, world!'
s2 = 'Hello, world!'
print(id(s1) == id(s2))


# Answer: True




# Q70: G) Is id(f1) == id(f2) True or False?
f1 = 1.0
f2 = 1.0
print(id(f1) == id(f2))


# Answer: True




# Q70: G) Is id(f1) == id(f2) True or False?
f1 = 1.0
f2 = 1.0



# Answer: True



"""
Immutables: 
Multiple variables referring to the same value point to the same object in memory (interning); but not always the case for long or complex values.

Mutables:
A new memory object is always created.
"""



""" Q70 (continued):                                                                   nnnnn          nnnnn          nnnnn          21-1
h) What is the output?   i) Name four mutable data types?
"""

class MysticCreature:
    def __init__(self, energy=5):
        self.energy = +energy
    def recharge(self, energy=7):
        self.energy += energy
        return self.energy

dragon1 = MysticCreature(8)
phoenix2 = MysticCreature(4)
dragon1 = phoenix2
phoenix2.recharge()
print(dragon1.energy)

# h) Answer: 11
# i) Answer: lists, dictionaries, sets, byte arrays.

""" Mutable vs Immutable:

Mutables: When assinging a variable to another variable of a mutable object, both will then be pointed to the same object in memory.

Imutables: If assigning one variable (vA) to another (vB), the newly assigned variable (vB) is pointed to the same object in memory as vA, 
however if we "modified" vA, vA would get a new memory object and vB would stay the same.  

In short:
Nothing changes until either variable is modified, for mutables, the underlying memory is changed; for immutables, a new memory object is created.
"""

# j) What is the output?

class Planet:
    def __init__(self, position=0):
        self.orbit = position
    def rotate(self):
        self.orbit += 1

planet1 = Planet(2)
planet2 = planet1
planet2.rotate()
planet1.rotate()
print(planet2.orbit)

# j) Answer: 4



# k) What is the output?
str1 = 'corsair'
str2 = 'asrock'
str3 = 'asus'
str1 = str2
str2 += ' manuf'
print(str1)

# k) Answer: asrock




# Q71: What is the expected output of the following code snippet?               20-1                26-1


galaxy = 'Andromeda'

def alter(galaxy):
    return galaxy[:-5]

try:
    for star_system in range(3):
        galaxy = alter(galaxy)
        assert galaxy
    print(galaxy)
except IndexError:
    print("Stellar Indexing Error")
except LookupError:
    print("Galactic Lookup Failure")
except:
    print("Cosmic Anomaly Detected")

# Answer: Cosmic Anomaly Detected





# Q72: How many characters are removed from the string?
'sd9f867as7806df8079as6df0896asdf7806789'[:-23]

# Answer: 23





# Q73: You are writing a Python function and want to handle both ArithmeticError exceptions and LookupError exceptions under one single except branch.

# The function looks like this :

def my_fun(x,y):                    # line 1
    try:                            # line 2
        # my code for try branch    # line 3
    # catch exceptions here         # line 4
        # my code for except branch # line 5
    return None                     # line 6


# Which of the below lines do you need to insert in line 4 to achieve this requirement ?


except ArithmeticError, LookupError:

except (ArithmeticError, LookupError):

The requirement can't be achieved with one single except branch - each exception needs its own except branch.

except [ArithmeticError, LookupError]:


# Answer: except (ArithmeticError, LookupError):







""" Q75: List 7 open() modes and their behaviour.

r: reads from beginning; file must exist or raises FileNotFoundError
w: creates or truncates; existing file not required.

r+: reads & update; reads or writes starting at the beginning; file must exist.
w+: write & update: writes or reads from the beginning; existing file not required.

x: creates a file for writing at the beginning; raises FileExistsError if file exists. Safer alternative to 'w'.
a: append opens or creates a file for writing at the end; existing file not required.
a+: opens (or creates) a file for appending at the end; existence not required; writes always move the position (back) to the end.

"""







# Q76: What is the expected output of the following code snippet?

import errno

try:
    scroll = open('enchanted_scroll.txt', 'wt')
    for wizard in range(10):
        spell = "scroll #" + str(wizard+1) + "\n"
        scroll.write(spell)
    scroll.close()
except:
    print("Mystical I/O error occurred:")
# End of code

try:
    grimoire = open("enchanted_scroll.txt", "x")
    grimoire.write("123")
    grimoire.close()
except IOError as incantation:
    if incantation.errno == errno.ENOENT:
        print("A")
    elif incantation.errno == errno.EEXIST:
        print("B")
    else:
        print("C")
else:
    print("D")

# Answer: B




# Q77: What is the expected output of the following code snippet?

planet = chr(ord('A') + 1) > chr(ord('k') - 1)
print(planet)

# Answer: False






# Q78: True or false for each of these?                                                                     21-2 (mix up)

print(bool(''), bool([]), bool(0,), bool({}), bool(None), end='')
print('', bool([[]]), bool((0,)))

# Answer: 
"""
F, F, F, F, F, T, T
"""





# Q79: What is the output of the following code if the user enters 67 when prompted?            21-1            26-1

class OutOfBoundsError(Exception):
    def __init__(self, num, message="Number is not within the specified range"):
        self.num = num
        self.message = message
        super().__init__(self.message, self.num)

try:
    selection = int(input("Enter integer between 0 and 100: "))
    if not 1 <= selection <= 87:
        raise OutOfBoundsError(selection)
except Exception as ex:
    for arg in ex.args:
        print(arg, end=' ')

# Answer: No output




# Q80: What is the output?
from math import factorial as superpower_calculation

try:
    print(superpower_calculation(-6))
except:
    print("Error #1")
except ValueError:
    print("Error #2")

# Answer: SyntaxError






# Q81: What is the expected output of the following code snippet?

class Tree:
    def __init__(self, number):
        self.leaf = number

class Oak(Tree):
    pass

class Pine:
    def __init__(self, number):
        self.leaf = number + 2

class Maple(Pine):
    def __init__(self, number):
        super().__init__(number + 2)

class Birch(Oak, Maple):
    pass

b = Birch(3)
print(b.leaf)

# Answer: 3






# # Q82: What is the expected output of the following code snippet?             26-1 (use second Q82 below)

# class Element:
#     E = 0
#     def __init__(self, value):
#         self.atom = value

# class Metal(Element):
#     M = 1
#     def __init__(self, value):
#         self.atom = value + 1
#         super().__init__(value - 1)

# class Gas:
#     G = 2
#     def __init__(self, value):
#         self.atom = value + 2

# class Liquid(Metal, Gas):
#     L = 3

# l = Liquid(4)
# print(l.atom)

# # Answer: 



# Q82: What is the expected output of the following code snippet?

class Spice:
    S = 0
    def __init__(self, quantity):
        self.grain = quantity

class Herb(Spice):
    H = 1
    def __init__(self, quantity):
        self.grain = quantity + 1
        super().__init__(quantity - 1)

class Flavor:
    F = 2
    def __init__(self, quantity):
        self.grain = quantity + 2

class Seasoning(Herb, Flavor):
    Se = 3

s = Seasoning(5)
print(s.grain)

# Answer: 4






# Q83 
# a): Which of the five statements below are correct? (pick 2)                             21-1
"""
1. UTF-8 is based solely on the ASCII encoding.

2. ASCII can encode more than a million characters.

3. UTF-8 is the eighth version of the UTF standard, replacing UTF-7.

4. With UTF-8 some characters may use 8 bits for their code points while others may use 16 bits.

5. UTF-8 can encode 1,112,064 characters.
"""
# Answer: 4, 5


# b) Which of the following is a true statement? (Select 2 Answers)                         21-2

"""
Unicode is a standard

UTF-8 is an encoding

Unicode is an encoding

UTF-8 is a standard

UTF-8 is the only encoding apart from ASCII
"""

# Answer: Unicode is a standard and UTF-8 is an implimentation of it.







# Q84: What are each of these constants?                                                   22-1         Got all correct (26-1)          21-2

"""
errno.EACCES → 

# Answer: 

errno.EBADF → 

# Answer: 

errno.EEXIST → 

# Answer: 

errno.EFBIG → 

# Answer: 

errno.EISDIR → 

# Answer: 

errno.EMFILE → 

# Answer: 

errno.ENOENT → 

# Answer: 

errno.ENOSPC → 

# Answer: 

"""




# Q85:                                                                          21-1

""" You are being asked to create a Python program that will randomly return five unique integers between 0 and 132 (both 0 and 132 are included as 
possible choices). Which code will achieve this requirement? """


# Option A
import random
print("Selected constellations are: ", random.sample(range(133), k=5))

# Option B
import random
print("Selected constellations are: ", random.randrange(0, 132, 7))

# Option C
import random
print("Selected constellations are: ", random.choices(range(132), k=5))

# Option D
import random
print("Selected constellations are: ", [random.randint(0, 132) for space_object in range(5)])


# Answer: A








# Q86: Wich of the following evaluates to True given the following code? (Select 2 Answers)             5-2

a = "television"

print(a.index('ele') == 1)              # 1

print(a.index('e', 2) == 1)             # 2

print(a.index('e', 2) == 3)             # 3

print(a.index('i') == 4)                # 4

print(a.index('i') == 6)                # 5

# Answer: 1, 3





# Q87: Which of the following is True about bytearrays? (Select 2 Answers)

"""
1) bytearrays can store characters

2) The readinto() method can be used to read bytes from a file into an existing bytearray

3) bytearrays can only have integer values between 0 and 255 inclusive

4) bytearrays are immutable

5) bytearrays cannot be written to files
"""

# Answer: 2, 3. 






# Q88: What is the expected output of the following code snippet?                       21-2 (also see Q94)

class GalaxyError(Exception):
    pass
 
try:
    raise Exception("X", "Y")
except GalaxyError:
    print("Greetings", end=" ")
finally:
    print("Farewell")

# Answer: 





# Q89: What is the expected output?                 8-2

class A:
    def __init__(self, var):
        A.var = var
 
a = A(10)
b = A(100)
print(a.var)

# Answer: 100





# Q90: 
# a) What is the expected output of the following code snippet?                 8-2             21-2

creature_stats = {'goblin':1, 'troll':2}
try:
    creature_stats[1]
except IndexError:
    print('Cave', end=' ')
except Exception as exc:
    print(exc.args, end=' ')

# Answer: 

# b) What distinguishes KeyError's error argument handling, specifically when accessing a non-existent key in a dictionary, from that of other Python error types?

# Answer:                                                                                                                                                                                      The non-existent key itself is passed as an argument, instead of a description of the error.






# Q91: What is the expected output of the following code snippet?                 8-2

string_sequence = "def"
 
for element in string_sequence:
    element = 'y'
 
print(string_sequence)

# Answer: def (also, see extra info below):


"""
string_sequence = "def"
 
for element in string_sequence:
    print(element)                 #extra print() for tracking
    element = 'y'
    print(element)                 #extra print() for tracking
 
print(string_sequence)

Console
d
y #
e
y #
f
y #
def

"""






# Q92: Given the following classes:                                             8-2             correct_but_MORE_PRACTICE_NEEDED__21-2

class Alpha:
    pass
class Beta(Alpha):
    pass
class Gamma(Beta):
    pass
class Delta(Alpha):
    pass

# Which of the following are correct declarations of subclasses? (Select 2 Answers)

class subclass1(Alpha, Beta): # a
    pass

class subclass2(Gamma, Delta): # b
    pass

class subclass3(Alpha, Delta): # c
    pass

class subclass4(Beta, Gamma): # d
    pass

class subclass5(Delta, Gamma): # e
    pass


# Answer: b, e





# Q93:                                                                      9-2

"""
The file abc.txt contains the following 3 lines of text:

abc
def
ghi

The output of the below snippet is: 
<_io.TextIOWrapper name='abc.txt' mode='r' encoding='cp1252'>
What would happen if we tried to iterate over the stream directly?
"""

file = open('abc.txt')
print(file)

# Answer: Acting as an iterator, io.TextIOWrapper calls __next__, printing the text up to the next new line character until StopIteration is raised when reaching EOF.















# Q94: What is the expected output of the following code snippet?                 8-2
class ExampleException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
    
    def __str__(self):
        return 'a'

try:
    raise ExampleException('test')
except Exception as e:                      # see note (scroll right)                                                                                                           This line does NOT alter the instance of the exception that was raised (see below**)!
    print(e)

# Answer: a






# Q95: Essentially, what is the only real limit of the 'del' keyword?                 8-2

# Answer: Can't remove parts of immutables.






# Q96: What is the output of the following snippet of code?                 8-2             21-2

class A:
    pass
class B:
    pass
class C(B):
    pass
 
c = C()
print(isinstance(c, (B,A)))

# 





# Q97: A)Which of the following snippets outputs 'abc' to the screen? (Select two answers).             21-2

# Option A
print(sorted("abc"))

# Option B
temporary_variable = "abc".sort()
print(str(temporary_variable))

# Option C
print(''.join(sorted("abc")))

# Option D
temporary_variable2 = list("abc")
temporary_variable2.sort()
print(''.join(temporary_variable2))

# Answer: 

# B) What data type does sorted() always return?  And what can it not sort?

# Answer: sorted() always returns a list (and automatically converts other types to lists).  However, it can't sort between different data types, i.e., between 'str' and 'int'.



# Q98: What is the output of the following snippet of code?                 11-2
x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
 
def func(data):
    res = data[0][0]
    for da in data:
        for d in da:
            if res < d:
                res = d
    return res
 
print(func(x[0]))

# Answer: 4










# Q99: What is the output of the 2 following  snippets?

class E (Exception):
	def __init__(self, message):
		self.message = message
	
	def __str__(self):
		return "it's nice to see you"

try:
    print("I feel fine")
    raise E("what a pity")
except Exception as e:
    print(e)
else:
    print("the show must go on")



"""Answer: 
what a pity
it's nice to see you
"""



"""
Python exceptions are designed so that more general except branches are capable of catching a wider number of exceptions.  This means a superclass in
the except branch can catch its subclass exceptions.
To catch a more concrete exception when both concrete and non-concrete branches exist, the subclasse(s) or 'more concrete' exception(s) should be placed first.
"""





class E (Exception):
	def __init__(self, message):
		self.message = message
	
	def __str__(self):
		return "it's nice to see you"

try:
    print("I feel fine")
    raise Exception("what a pity")
except E as e:
    print(e)
else:
    print("the show must go on")



# Answer: Not caught.



"""
However, if the except branch is a subclass of the exception (i.e., the exception being RAISED is the parent), it can not catch the exception.  This is similar
to how an instance of a superclass doesn't have the attributes of its subclasses.

If subclasses could catch superclass exceptions, it would lead to a scenario where very specific handlers are invoked for general problems they're not designed
to address directly, potentially leading to inappropriate error handling.
"""














# Q100: What is the output?
print('' in '', '' in ' a')

# Answer: True True







# Q101 - Error Handling

# Q: Which of the following is false?


#1 A try statement can have a finally clause without an except clause.

#2 A try statement can have one or more finally clauses.

#3 A try statement can have one or more except clauses.

#4 A try statement can have a finally clause and an except clause.

# Answer: 2






# Q102: 

# A) Given the code below, complete the display() method body in a way that will ensure that the retrieve() method is properly invoked.

class Artifact:
    def __init__(self):
        self.collection = 1
 
    def retrieve(self):
        return self.collection
 
    def display(self):
        # Insert a method here
 
 
item = Artifact()
item.display()

# (Select two answers.)

print(Artifact.retrieve(self))

print(Artifact.retrieve())

print(retrieve())

print(self.retrieve())

# Answer: 1st, 4th.




# B) Comment out the incorrect lines, make two small corrections, then run the program to check it works.               CORRECT_BUT_NEED_MORE_PRACTICE_21-2

class ScienceExperiment:
    variable = 'Experiment Data'
    def __init__(self):
        experiment_note = 'Note Content'
        print(self.experiment_note)


    def record(self):
        observation = 'Observation Details'
        print(self.observation)

test = ScienceExperiment()
test.record()

ScienceExperiment.experiment_note
ScienceExperiment.record()
print(test.__dict__)
print(test.experiment_note)


# Answer (did it work)?: yes, you can't do class.instance_variable, as it'll look for a class variable that doesn't exist. You also can't 'only' do class.instance_method() because the method would be missing the 1 required positional arg: 'self'.                                                                                                                                                                             # Hint: 'self'









# Q103: 

# A) Is the result of the following line 0 or 0.0?

print(1 // 2 * 3)


# Answer: 0


# B) What's the result this time?  Why?

print(9 // 3 // 1.0)

# Answer: 3.0                                                                                                                                                    # The divide (/) operator always returns a float.  The floor divide (aka int division) operator (//) truncates to an integer if all operands are ints.  If at least one operand is a float, '//' returns a float.






#Q104: What is the output and why?

def t():
    return 'Peter'           'Wellert'

print(t())


# Answer: PeterWellert: Python concatenates the strings.






#Q105:                                                                                                  21-2

# A) Provide a detailed list of all the output for this snippet (any order will do). 

class MyClass:
    """docstring test"""

    class_var = 1
 
    def __init__(self):
        self.instance_var = 1
 
    def my_meth(self):
        pass
 
 
object = MyClass()

for i in MyClass.__dict__:
    print(i, '\t\t', MyClass.__dict__[i])


# Answer: 







"""
__module__      __main__
__dict__        <attribute '__dict__' of 'MyClass' objects>
__weakref__     <attribute '__weakref__' of 'MyClass' objects>
__doc__         docstring test

__init__        <function MyClass.__init__ at 0x...>
my_meth         <function MyClass.my_meth at 0x...>
class_var       1

Note: The dictionary can be used to access these entities directly, i.e., they're not just strings.
"""




# Q106: What is the output for each snippet?                    21-2

lst = [1, 2]
lst += (1, 2, 3)
print(lst)
# Answer: 

print([1, 2] * 2 + [3])
# Answer: 

print([1, 2] + list((3, 4)))
# Answer: 

print([1, 2] + (3, 4))
# Answer: 

lst = [1, 2]
lst.append([3, 4])
print(lst)
# Answer: 

lst = [1, 2, 3]
lst.append((1,))
print(lst)
# Answer: 

lst = [1, 2, 3]
lst += (1,)
print(lst)
# Answer: 

print([[]] * 3)
# Answer: 

tup1 = (1, 2)
tup2 = (3, 4)
print([tup1] + [tup2])
# Answer: 

lst = [1, 2, 3]
(lst.append(4), lst)[1]
print(lst)
# Answer: 

print([x for x in (1, 2)] + [y for y in [3, 4]])
# Answer: 

lst = [1, 2, 3]
lst *= (1,)
print(lst)
# Answer: 

lst = [1, 2, 3]
lst += 1,
print(lst)
# Answer: 


"""Info:

+       Concatenates two sequences of the same type, returning a new sequence.  Must be the same data types.
+=      For lists: extends the sequence in-place with elements from another sequence or iterable; for strings and tuples, concatenates and reassigns due to immutability.

*       Repeats the sequence for a given integer, returning a new sequence.
*=      Repeats the sequence in-place for lists; for strings and tuples, creates and reassigns a new repeated sequence.  Integer required:  `[1, 2, 3] *= [1]` will raise a TypeError.


"""




# Q107: What does each command do?

cd ../
cd ./
cd /

"""
Answers:
up a level
cwd
root


"""





# Q108: Copy to an editor and check your answer for each expression.

print(True if False else True) # 
print(True if True else False) # 
print('Yes' if False else 'No') # 
print(False if False else True) # 
print(0 if True else 1) # 
print(True if False else False) # 
print('A' if not False else 'B') # 
print(False if True else False) # 
print('Python' if 10 > 5 else 'Java') # 
print(False if True else True) # 
print('Not Empty' if '' else 'Empty') #  
print(True if False else True) # 





# Q109: What is the output?  Why?

class Un:
    value = "Eins"
 
    def say(self):
        return self.value.lower()
  
class Deux(Un):
    value = "Zwei"
  
class Troi(Un):
    def say(self):
        return self.value.upper()
  
class Quatre(Troi, Deux):
    pass

d = Quatre()
b = Deux()

print(Un.value, Deux.value, d.value, b.value)

# Answer: Eins, Zwei, Zwei, Zwei






# Q: What is the output?      *****      *****      mmmmm      mmmmm

s = '123456'
even_sum = 0
odd_product = 1

for i in range(len(s)):
    num = int(s[i])
    if i % 2 == 0:
        even_sum += num
    else:
        odd_product *= num

print("Sum of numbers at even indices:", even_sum)
print("Product of numbers at odd indices:", odd_product)

''' Answer:

'''





# Q: What is the output?      mmmmm            mmmmm

s = '13579'
total = 0

for i in range(1, len(s)):
    if i % 2 == 0:
        total += int(s[i])

print("Total of even-indexed numbers:", total)

# Answer: 









#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q [Improving speed of mental arithmetic]: What is the   F I R S T   and   L A S T   number printed from each of the following snippets?:

s = '0'
for i in range(len(s)):
    print(s[i], end='')


# Answer: 0



s = '01'
for i in range(len(s)):
    print(s[i], end='')


# Answer: 01



s = 'AB'
for i in range(len(s)):
    print(s[i], end='')


# Answer: AB



s = '0123'
for i in range(len(s)):
    print(s[i], end='')


# Answer: 03



s = '456789'
for i in range(len(s)):
    print(s[i], end='')


# Answer: 49



s = '123456789'
for i in range(len(s)):
    print(s[i], end='')


# Answer: 19



s = '23456789'
for i in range(len(s)):
    print(s[i], end='')


# Answer: 29



s = '67890'
for i in range(len(s)):
    print(s[i], end='')


# Answer: 60



s = '01234567890123456789'
for i in range(len(s)):
    print(s[i], end='')


# Answer: 09



s = 'g8 49g'
for i in range(len(s)):
    print(s[i], end='')


# Answer: gg

# Q# b) What do all these answers have in common?
# Answer: When iterating over an iterable's length with range in a loop, if the operations within the loop don't modify the elements or their order, the output always mirrors the original iterable.

# Q# c) What is: 1 % 2, 0 % 1, 2 % 1 ?






# Answer: 1, 0, 0

# Q# d) Answer the below snippets:

s = '0'
sum1 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
print(sum1)


# Answer: 0



s = '01'
sum1 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
print(sum1)


# Answer: 0



s = '0123'
sum1 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
print(sum1)


# Answer: 2



s = '234'
sum1 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
print(sum1)


# Answer: 6



s = '234567'
sum1 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
print(sum1)


# Answer: 12



s = '013456'
sum1 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
print(sum1)


# Answer: 8



s = '2345678901'
sum1 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
print(sum1)


# Answer: 20



s = '12345'
sum1 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
print(sum1)


# Answer: 9



s = '3456789'
sum1 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
print(sum1)


# Answer: 24






# Q# e) Answer the below snippets:

s = '0'
sum1 = 0
sum2 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1)
print(sum2)



""" Answer: 
0
0
"""



s = '01'
sum = 0
sum1 = 0
sum2 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1)
print(sum2)



""" Answer: 
0
1
"""




s = '0123'
sum1 = 0
sum2 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1)
print(sum2)



# Answer: 2, 4




s = '234'
sum1 = 0
sum2 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1)
print(sum2)



# Answer: 6, 3




s = '234567'
sum1 = 0
sum2 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1)
print(sum2)


# Answer: 12, 15




s = '013456'
sum1 = 0
sum2 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1)
print(sum2)


# Answer: 8, 11



s = '2345678901'
sum1 = 0
sum2 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1)
print(sum2)



# Answer: 20, 25




s = '12345'
sum1 = 0
sum2 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1)
print(sum2)



# Answer: 9, 6





s = '3456789'
sum1 = 0
sum2 = 0
for i in range(len(s)):
    x = int(s[i])
    if i % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1)
print(sum2)



# Answer: 24, 18






l = [0]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)



# Answer: []






l = [0, 1]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)



# Answer: [1]





l = [0, 1, 2]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)



# Answer: [1]







l = [0, 1, 2, 3]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)



# Answer: [1, 9]






l = [0, 1, 2, 3, 4]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)



# Answer: [1, 9]







l = [0, 1, 2, 3, 4, 5]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)



# Answer: [1, 9, 25]






l = [1, 2]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)



# Answer: [4]






l = [1, 2, 3]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)



# Answer: [4]







l = [1, 2, 3, 4, 5]
nl = [e**2 for e in l if l.index(e) % 2 == 1]
print(nl)



# Answer: [4, 16]





l = [0]
nl = [e**2 for e in l if l.index(e) % 2 == 0]
print(nl)



# Answer: [0]






l = [0, 1]
nl = [e**2 for e in l if l.index(e) % 2 == 0]
print(nl)



# Answer: [0]





l = [0, 1, 2]
nl = [e**2 for e in l if l.index(e) % 2 == 0]
print(nl)



# Answer: [0, 4]







l = [0, 1, 2, 3]
nl = [e**2 for e in l if l.index(e) % 2 == 0]
print(nl)



# Answer: [0, 4]






l = [0, 1, 2, 3, 4]
nl = [e**2 for e in l if l.index(e) % 2 == 0]
print(nl)



# Answer: [0, 4, 16]







l = [0, 1, 2, 3, 4, 5]
nl = [e**2 for e in l if l.index(e) % 2 == 0]
print(nl)



# Answer: [0, 4, 16]






l = [1, 2]
nl = [e**2 for e in l if l.index(e) % 2 == 0]
print(nl)



# Answer: [1]






l = [1, 2, 3]
nl = [e**2 for e in l if l.index(e) % 2 == 0]
print(nl)



# Answer: [1, 9]







l = [1, 2, 3, 4, 5, 6, 7]
nl = [e**2 for e in l if l.index(e) % 2 == 0]
print(nl)



# Answer: [1, 9, 25, 49]







#################################################################################################################







# MULTIPLE CHOICE:

list1 = [3, 4]
list2 = [4, 5, 6]

a = list(filter(lambda x: x in list1, list2))
print(a)

"""
A) [3, 4]
B) [5, 6]
C) []
D) [4]
"""


# Answer: D






list1 = [2, 4, 6]
list2 = [1, 2, 3, 4]

a = list(filter(lambda x: x in list1, list2))
print(a)

"""
A) [2, 4]
B) [1, 3]
C) []
D) [2, 3, 4]
"""

# Answer:  A) [2, 4]







list1 = [10, 20, 30]
list2 = [20, 30, 40, 50]

a = list(filter(lambda x: x in list1, list2))
print(a)

"""
A) [20, 30, 40]
B) [20, 30]
C) []
D) [10, 20, 30]
"""


# Answer: B) [20, 30]






list1 = [15, 25]
list2 = [5, 10, 15, 20, 25, 30]

a = list(filter(lambda x: x in list1, list2))
print(a)

"""
A) [15, 25]
B) [5, 10, 20, 30]
C) [10, 20, 30]
D) []
"""


# Answer: A) [15, 25]






list1 = [1, 2]
list2 = [1, 2, 3]

a = list(filter(lambda x: x not in list1, list2))
print(a)

"""
A) [2, 3]
B) []
C) [3]
D) [1, 2]
"""


# Answer: C) [3]




list1 = [5, 6, 7]
list2 = [4, 5, 6, 7, 8]

a = list(filter(lambda x: x not in list1, list2))
print(a)

"""
A) [5, 6, 7]
B) [4, 8]
C) [4, 5, 6, 7, 8]
D) []
"""


# Answer: B) [4, 8]






list1 = [2, 3, 5]
list2 = [1, 2, 3, 4, 5, 6]

a = list(filter(lambda x: x not in list1, list2))
print(a)

"""
A) [2, 3, 5]
B) [1, 4, 6]
C) [1, 2, 3, 4, 5, 6]
D) [1, 3, 5]
"""


# Answer: B) [1, 4, 6]






list1 = [3, 6, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = list(filter(lambda x: x not in list1, list2))
print(a)

"""
A) [1, 2, 4, 5, 7, 8]
B) [3, 6, 9]
C) [1, 2, 3, 4, 5, 6, 7, 8, 9]
D) []
"""


# Answer: A) [1, 2, 4, 5, 7, 8]







list1 = ['a', 'b']
list2 = ['b', 'c', 'd']

a = list(filter(lambda x: x in list1, list2))
print(a)

"""
A) ['a', 'b']
B) ['c', 'd']
C) []
D) ['b']
"""

# Answer: D) ['b']




list1 = [7, 'x', 9]
list2 = ['y', 7, 'z', 'x']

a = list(filter(lambda x: x in list1, list2))
print('\n', a)

"""
A) []
B) ['y', 'z']
C) [7, 'x']
D) [7, 'x', 'y', 'z']
"""

# Answer: C) [7, 'x']





list1 = [15, 'apple', 20]
list2 = ['banana', 20, 'apple', 30]

a = list(filter(lambda x: x in list1, list2))
print('\n', a)

"""
A) [15, 'apple', 20]
B) ['banana', 30]
C) ['apple', 20]
D) []
"""

# Answer: C) ['apple', 20]





list1 = [40, 'orange', 50]
list2 = ['orange', 50, 'lemon', 60]

a = list(filter(lambda x: x in list1, list2))
print('\n', a)

"""
A) ['orange', 50]
B) ['lemon', 60]
C) []
D) [40, 'orange', 50]
"""

# Answer: A) ['orange', 50]





list1 = ['cat', 3]
list2 = [1, 'cat', 4, 'dog']

a = list(filter(lambda x: x not in list1, list2))
print('\n', a)

"""
A) [1, 'cat', 4, 'dog']
B) []
C) ['cat', 4]
D) [1, 4, 'dog']
"""

# Answer: d





list1 = [5, 'mouse', 8]
list2 = [7, 'mouse', 9, 'rat', 8]

a = list(filter(lambda x: x not in list1, list2))
print('\n', a)

"""
A) [7, 'mouse', 9, 'rat', 8]
B) [5, 'mouse', 8]
C) [7, 9, 'rat']
D) []
"""

# Answer: c





list1 = [2, 'bird', 'fish']
list2 = [1, 2, 'cat', 'bird', 6]

a = list(filter(lambda x: x not in list1, list2))
print('\n', a)

"""
A) [1, 'cat', 6]
B) [2, 'bird', 'fish']
C) [1, 2, 'cat', 'bird', 6]
D) [2, 'bird']
"""

# Answer: a





list1 = ['frog', 'toad', 9]
list2 = [1, 2, 'frog', 4, 'lizard', 'toad', 8, 9]

a = list(filter(lambda x: x not in list1, list2))
print('\n', a)

"""
A) [1, 2, 4, 'lizard', 8]
B) ['frog', 'toad', 9]
C) [1, 2, 'frog', 4, 'lizard', 'toad', 8, 9]
D) []
"""

# Answer: a







###################################################################################################

# FILL IN THE BLANKS (COPY/PASTE SOMEWHERE FIRST)

# Challenge 1: Intended Output [0, 0, 0, 1, 1, 1, 2, 2, 2]
print([_ for _ in range(3) for _ in range(3)])

# Challenge 2: Intended Output [2, 4, 6, 2, 4, 6, 2, 4, 6]
print([_ for _ in range(3) for _ in range(2, 7, 2)])

# Challenge 3: Intended Output ['A', 'B', 'A', 'B', 'A', 'B']
print([_ for _ in range(3) for _ in ['A', 'B']])

# Challenge 4: Intended Output [0, 2, 4, 0, 2, 4]
print([_ for _ in range(2) for _ in range(0, 6, 2)])

# Challenge 5: Intended Output [3, 3, 3, 4, 4, 4, 5, 5, 5]
print([_ for _ in range(3, 6) for _ in range(3)])

# Challenge 6: Intended Output [1, 3, 5, 1, 3, 5, 1, 3, 5]
print([_ for _ in range(3) for _ in range(1, 6, 2)])

# Challenge 7: Intended Output [0, 'x', 0, 'x', 0, 'x']
print([_ for _ in range(3) for _ in [0, 'x']])

# Challenge 8: Intended Output ['a', 'b', 'c', 'a', 'b', 'c']
print([_ for _ in range(2) for _ in ['a', 'b', 'c']])

# Challenge 9: Intended Output [10, 12, 14, 10, 12, 14, 10, 12, 14]
print([_ for _ in range(3) for _ in range(10, 15, 2)])

# Challenge 10: Intended Output [1, 3, 1, 3, 1, 3]
print([_ for _ in range(3) for _ in range(1, 4, 2)])







# Challenge 1: Intended Output [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
print([[_ for j in range(3)] for _ in range(3)])

# Challenge 2: Intended Output [[2, 2, 2], [4, 4, 4], [6, 6, 6]]
print([[_ for i in range(3)] for _ in range(2, 7, 2)])

# Challenge 3: Intended Output [['A', 'A', 'A'], ['B', 'B', 'B']]
print([[_ for _ in range(3)] for _ in ['A', 'B']])

# Challenge 4: Intended Output [[0, 0], [2, 2], [4, 4]]
print([[_ for i in range(2)] for _ in range(0, 6, 2)])

# Challenge 5: Intended Output [[3, 4, 5], [3, 4, 5], [3, 4, 5]]
print([[_ for i in range(3, 6)] for _ in range(3)])

# Challenge 6: Intended Output [[1, 1, 1], [3, 3, 3], [5, 5, 5]]
print([[_ for i in range(3)] for _ in range(1, 6, 2)])

# Challenge 7: Intended Output [[0, 0, 0], ['x', 'x', 'x']]
print([[_ for i in range(3)] for _ in [0, 'x']])

# Challenge 8: Intended Output [['a', 'a'], ['b', 'b'], ['c', 'c']]
print([[_ for _ in range(2)] for _ in ['a', 'b', 'c']])

# Challenge 9: Intended Output [[10, 10, 10], [12, 12, 12], [14, 14, 14]]
print([[_ for i in range(3)] for _ in range(10, 15, 2)])

# Challenge 10: Intended Output [[1, 1, 1], [3, 3, 3]]
print([[_ for _ in range(3)] for _ in range(1, 4, 2)])




###################################################################################################




# FLAT List Comprehensions with Two Iterators (20 Challenges)

# 1
print([x + y for x in range(3) for y in range(2)])  # [0, 1, 1, 2, 2, 3]
# Answer: 

# 2
print([x * y for x in range(2) for y in range(3)])  # [0, 0, 0, 0, 1, 2]
# Answer: 

# 3
print([x - y for x in range(4) for y in range(2)])  # [0, -1, 1, 0, 2, 1, 3, 2]
# Answer: 

# 4
print([x for x in range(3) for y in range(2) if x > y])  # [1, 2, 2]
# Answer: 

# 5
print([y for x in range(2) for y in range(3) if x < y])  # [1, 2, 2]
# Answer: 

# 6
print([x * y for x in range(2) for y in range(2) if x != y])  # [0, 0]
# Answer: 

# 7
print([x + y for x in range(2) for y in range(2) if x == y])  # [0, 2]
# Answer: 

# 8
print([x - y for x in range(3) for y in range(3) if x >= y])  # [0, 1, 0, 2, 1, 0]
# Answer: 

# 9
print([x * y for x in range(2) for y in range(3) if y % 2 == 0])  # [0, 0, 0, 2]
# Answer: 

# 10
print([x + y for x in range(3) for y in range(2) if (x + y) % 2 == 0])  # [0, 2, 2]
# Answer: 




# NESTED List Comprehensions with Two Iterators (20 Challenges)

# 1
print([[x + y for x in range(2)] for y in range(2)])  # [[0, 1], [1, 2]]
# Answer: 

# 2
print([[x * y for x in range(2)] for y in range(3)])  # [[0, 0], [0, 1], [0, 2]]
# Answer: 

# 3
print([[x - y for x in range(3)] for y in range(2)])  # [[0, 1, 2], [-1, 0, 1]]
# Answer: 

# 4
print([[x for x in range(2) if x > y] for y in range(2)])  # [[1], []]
# Answer: 

# 5
print([[y for x in range(2) if x < y] for y in range(3)])  # [[], [1], [2, 2]]
# Answer: 

# 6
print([[x * y for x in range(2) if x != y] for y in range(2)])  # [[0], [0]]
# Answer: 

# 7
print([[x + y for x in range(2) if x == y] for y in range(2)])  # [[0], [2]]
# Answer: 

# 8
print([[x - y for x in range(3) if x >= y] for y in range(3)])  # [[0, 1, 2], [0, 1], [0]]
# Answer: 

# 9
print([[x * y for x in range(2) if y % 2 == 0] for y in range(3)])  # [[0, 0], [], [0, 2]]
# Answer: 

# 10
print([[x + y for x in range(2) if (x + y) % 2 == 0] for y in range(2)])  # [[0], [2]]
# Answer: 





###################################################################################################



# practice:
 2**0, 2**1, 2**2, 2**3, 2**4 and 0**2, 1**2, 2**2, 3**2, 4**2
    double last                         square left operand


# basic recursion?























#endregion
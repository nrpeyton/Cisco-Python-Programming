# type: ignore # pylint: disable=all

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





# Q3 What is the expected output of the following code?      *****

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

# Answer: General Error






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

# Answer: ImportError and IndexError








''' Q6  what is the output of a, b, c, d, e, and f?      *****

a) print(math.floor(-29) + math.trunc(10.6))
b) print([i for i in range(1, math.ceil(11))])
c) print([i for i in range(5) if i % 2 == 0 and i % 1 == i])

d) print(5 is 5.0)
e) print(5 == 5.0)
f) print(5 is 5)

g) What data type is returned by math.floor(), math.ceil() and math.trunc() ?


Q6 Answers:
a) -19
b) [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c) [0]                                     mmmmm      mmmmm      mmmmm

d) False
e) True
f) True

g) int
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




# Q10 Which of the following lines describe a true condition?

1. 'smith' > 'Smith' t

2. 'Smiths' < 'Smith' f

3. 'Smith' > '1000' t

4. '11' < '8' t

# Answer: 1, 3, 4






# Q11 What is the expected output of the following snippets?

# A) 
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])

# Answer: 


# B)                                                                            nnnnn
x = '\t\\'*2 + '\t'
print(len(x.split('t')))

# Answer: 





# Q12What is the expected result of the following code?      mmmmm      mmmmm

s1 = '12.8'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)

# Answer: Value Error




# Q13 What is the expected value of the result variable after the following code is executed?

import math
result = math.e == math.exp(1)

# Answer: True




# Q14 (Complete the sentence) Setting the generator's seed with the same value each time your program is run guarantees that...

# Answer: the same result will be generated.





# Q15 Which of the platform module's functions will you use to determine the name of the CPU running inside your computer?

# Answer: platform.processor





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
sys.path.append('D:/Python/Project/Modules') or sys.path.append('D:\\Python\\Project\\Modules')




# Q18 The directory mentioned in the previous exercise contains a sub-tree of the following structure: abc/def/mymodule.py.        *****        *****
# Assuming that D:\Python\Project\Modules has been successfully appended to the sys.path list, write an import directive letting you use all the mymodule entities.

# Answer: from abc.def import mymodule




# Q19 What is __pycache__ and __init__.py ?
'''
__pychache__ is a folder containing semi-compiled code (bytecode) stored in the same folder as your scripts.  It simply allows subsequent program runs to execute faster.
The folder is usually hidden by vscode to prevent clutter, except when creating directories with user created modules.

__init__.py is an often empty file that indicates to Python that its containing directory is a Package.  Prior to Python 3.3, this was required.  It is also useful for 
streamlining/simplifying import statements.

'''
# Answer: 
# __pycache__ On the first import of a module, Python compiles the code into bytecode to make future executions more efficient.  The bytecode is stored on __pycache__
# __init__.py In older Python versions an empty file called __init__.py was used to declare a directory as a container for package or subpackage.  This is now only a convention.



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




'''      *****
Q24:   During the first import of a module, Python deploys the pyc files in which of the below directories?
(Note: Although bytecode (pyc files) are created on a script's first execution, they aren't necessarily stored in the __pycache__ folder).

1. __pycache__
2. mymodules
3. hashbang
4. __init__
'''

# Answer: __pycache__





'''Q25 For each print statement, what are the possible outputs?
from random import randrange, randint

print(randrange(1), end= ' ')
print(randrange(0, 1), end= ' ' )
print(randrange(0, 20, 5), end= ' ')
print(randint(0, 2), '\n')

Answers:
1. 0
2. 0
3. 0, 5, 10, 15
4.             mmmmm


'''






'''                                                                                                            mmmmm
Q26:
A) What apt command removes installed software? And what pip command removes an installed package?
# Answer: sudo apt remove name, pip uninstall name

B) What is the pip command to view all installed packages?
# Answer: pip list

C) What is the pip command to view a package's dependencies?
# Answer: pip show name

D) What is the pip command to search for packages?
# Answer: pip search name (no longer works)

E) What is the pip command to update a package?
# Answer: pip install -u name
'''


'''
Q27:   Choose the true statements. (Select two answers)

1. The version function from the platform module returns a string with your Python version
2. The processor function from the platform module returns an integer with the number of processes currently running in your OS
3. The version function from the platform module returns a string with your OS version
4. The system function from the platform module returns a string with your OS name
'''
# Answer: 3 and 4




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
math.exp(1)
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

'''



# Q35 What is the output of print(math.radians(90))?
# Answer: 1.57




''' Q36
a) What is the output of print("5"/0) and b) what is the output of int("1, 2")

Answer: 
a) TypeError
b) ValueError
'''



''' Q37
What is the expected output of the following code?          mmmmm          mmmmm - actually got it correct but wasn't sure if sqrt(-n) is valid

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
inf
the end

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
class ForesteHuntingBird(HuntingBird):
    def __str__(self):
        return super().__str__() + 'Loves the forest!'







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

# Answer: 



# Q41: b)What will be the output of the following code?     mmmmm     mmmmm                        Remember to ACTUALLY step backwards when counting!
s = "abcd"
print(s[0:4:-1])

# Answer: 



# Q41: c)What will be the output of the following code?     mmmmm     mmmmm
s = 'abcde'
print(s[2:4:-1])

# Answer: 




# Q41: d)What will be the output of the following code?     mmmmm     mmmmm
s = "abcd"
print(s[2:0:-1])

# Answer: 




# Q41: e)What will be the output of the following code?     mmmmm     mmmmm
s = "abcd"
print(s[-2:-3:-1])

# Answer: 





# Q42: Write a Python snippet to reverse the word order in the sentence 'Exploration ignites curiosity'.      *****


'''Answer:


lst = "Exploration ignites curiosity".split()
lst.reverse()
str = ' '.join(lst)

# or:

print(' '.join("Exploration ignites curiosity.split()[::-1]))

















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
copy
count
pop
index

insert
append
extend

sort
reverse

remove
clear

'''


# Q44 b): Which string methods don't return a value?

# Answer: None of them.  All string methods DO return a value.




# Q44 c): Which 'only' iterables can list methods be used on?  How can we extract a substring from a string?        mmmmm

# Answer: 




# Q45: How many arguments does the string class's 'join' method take?  And what data type does it take?       *****

# Answer: 1 argument.  It takes an iterable.






# Q46: What is the result of math.hypot(7, 0)
# Answer: 7




''' Q47: What is the result of math.hypot(1, 2)
a) 6.92
b) 4
c) 2
d) 2.23
'''
# Answer: 2.23






''' Q48: Write three snippets to iterate through the dictionary:
a) its key-value pairs
b) only its keys
c) only its values
'''

dic = {1: 'one', 2: 'two', 3: 'three'}

''' Answer:
a) for i in dic.items()
b) for k in dic.keys()
c) for v in dic.values()

'''




# Q49: What is the ouput of this?               mmmmm

lst_obj = (-1, 11, 0)
lst_obj[0] += 1
obj = range(1, 11, 0)

# Answer: 







# Q50: Without worrying about missing characters or duplicate characters, what will be the likely range of the first element and last element?          mmmmm
# An approximate range can be a-c or y-z.
lst = [chr(randint(ord('a'), ord('z'))) for i in range(25)]
sorted(lst)
print(lst)


# Answer: 







# Q51: What is the output?      nnnnn
def fun(n):
    return -n

n = -10
print(fun(n))


# Answer: 





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

"""




# B)                                                                    nnnnn
j = 0
while j < 3:
    print("Mango:", j)
    j += 1
else:
    print("Watermelon")



""" Answer:
Mango 0
Mango 1
Mango 2
Watermelon
"""







# Q53: a) Why is a's assignment line not erroneous?  And which list's elements are mapped to 'x'?          nnnnn
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['z', 'a', 'b']

def fun(x):
    return x in list1
a = list(filter(fun, list2))
print(a)

# Answer: In the assignment, 'fun' is a reference to the 'fun' function.  Filter calls fun(x) with list2 mapped to 'x'. Filter only returns the true results.


# Q53: b) Keeping only the first two lines and the last line from the snippet above, convert the rest of the snippet to its lambda equivalent.

""" Answer: 
a = list(filter(lambda x: x in list1, list2))
"""






# Q54: a) What is the output?   b) Name three other types with similar behavior; what do they all have in common?                nnnnn          nnnnn
class Feline:
    def __init__(self, f=1):
        self.f = +f
    def reset(self, f=2):
        self.f += f
        return self.f
 
cat1 = Feline(2)
cat2 = Feline(3)
cat1 = cat2
cat2.reset()
print(cat1.f)



# Q54 a) Answer: 
# Q54 b) Answer: lists, dictionaries and byte arrays.






# Q55: What is the output?          nnnnn

l={}
for i in 'Skywalker':
    if i in 'Vader':
        l[ord(i)]=i
else:
    l[ord('d')]='d' 
    
for j in l.keys():
    print(l[j], end=' ')

# Answer: a e r d







# Q56: What is the expected output of the following snippet ?               nnnnn

x = 5//2
func = lambda x:+3
print(func(x))



# Answer: 3







# Q57: What is the expected output of the following snippet ?

my_list = list('yoDA')
print(''.join(my_list).capitalize())


# Answer: Yoda






# Q58 a): What are the four types below (answer in the order they appear)?              nnnnn
import datetime

print(datetime.datetime.now())

# Answer: module, module, class, function



# Q58 b): What are the four types below (answer in the order they appear)?              nnnnn
from datetime import datetime

print(datetime.now())

# Answer: module class class function






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

# Answer: 
Error
Done






# Q60: What is the output?                                  nnnnn

new_list = ['banana', 'tiger', '789Xy', 'Chess']
my_list.sort(key = lambda x: x[::-1])
print(my_list[0]) 

# Answer: 





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

# Answer: If we spread modules and subpackages across several sub-directories contained in a parent directory, this "root" directory previously required an
# __init__.py file before Python would recognise it as a package.  Since Python 3.3, an __init__.py file is no longer required.  Python
# can now (implicitly) treat this folder as a new 'namespace' package .  The only difference between namespace packages and regular packages is
# the existance of the __init__.py file. This means we can now use regular OS directories (folders) as packages.  The __init__.py file can still be
# useful for setting up more specific environments or even simplifying imports.  Packages continuing to use an __init__.py file are (still) known as 'regular' 
# packages.  This may be counter-intuative for someone new to Python because they can work with packages without ever encountering an __init__.py file.






# Q63: A) What is the output?    B) Can class variables be accessed by instances of those classes?  C) What about class an instance __dict__ ?  D) Provide a reason for the answer to 'B'           nnnnn

class Omega:
    A= True
    def __init__(self, x, y):
        self.a = x
        self.__b = y
    def set(self, z):
        Omega.A = z
 
omega= Omega(5, 3)
beta = Omega(10, 5)
omega.__d = True
beta.set(5)
print(omega.__dict__)
print(omega.A)
print(beta.A)

""" Answers:
A) 



B) 
C) 
D)
"""






# Q64: A) What is the output?  B) What would happen if we removed the '+' from the open flag?                nnnnn

L = [f"{x}\n" for x in range(5, 15)]
f = open("modifiedfile.txt", "a+")
f.writelines(L)
f.seek(0)
print(f.read())
f.close()

# A) Answer: 
# B) Answer: 








# Q65: Can the list [5, 6, 8, 2, 4, 3, 10, 7, 9, 3] be generated by the line below?  Provide a reason.

x=sample([i for i in range(1,11)], 10)

# Answer: 







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

# Answer: 



# Q66 B): Which character groups exclusively return 'True' for isalnum() ?

# Answer: 

# Q66 C): Which character groups exclusively return 'True' for isalpha() ?

# Answer: 








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



# Answer: 

# Q67 B): What does super() return?  Where does Python look for an attribute suffixed to super() ?  And what can/can't __name__ be used on?

# Answers: super().__name__ doesn't work because super() returns a 'proxy' object to access the parent class's methods, not the class itself. Since __name__ is a class attribute, not an object attribute, it can't be accessed through the proxy object returned by super()







# Q68: 

"""
A) Why can't a class constructor return a value?

# Answer: 


B) Why can't a class constructor be invoked directly from inside its class?  Can it be invoked from a subclass?

# Answer: 
"""






# Q69: What is the expected output of the following code snippet?                   nnnnn

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

# Answer: 







# Q70: A) # Is id(str1) != id(str2) True or False?
str1 = 'Hello'
str2 = 'Hello'

# Answer: 


# Q70: B) Is id(a) == id(b) True or False?
a = 256
b = 256

# Answer: 


# Q70: C) Is id(x) == id(y) True or False?
x = 257
y = 257


# Answer: 

# Q70: D) Is id(list1) == id(list2) True or False?
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# Answer: 


# Q70: E) Is id(tup1) == id(tup2) True or False?
tup1 = (1, 2, 3)
tup2 = (1, 2, 3)

# Answer: 


# Q70: F) Is id(s1) == id(s2) True or False?
s1 = 'Hello, world!'
s2 = 'Hello, world!'

# Answer: 


# Q70: G) Is id(f1) == id(f2) True or False?
f1 = 1.0
f2 = 1.0

# Answer: 










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



# practice 2^0, 2^1, 2^2, 2^3, 2^4 and 0^2, 1^2, 2^2, 3^2, 4^2
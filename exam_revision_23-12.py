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
c)                                      mmmmm      mmmmm

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



# Q11 What is the expected output of the following code?

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])

# Answer: are



# Q12What is the expected result of the following code?      mmmmm      mmmmm

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

1. print(randrange(1), end= ' ')
2. print(randrange(0, 1), end= ' ' )
3. print(randrange(0, 20, 5), end= ' ')
4. print(randint(0, 2), '\n')

Answers:
1. 0
2. 0
3. 0, 5, 10, 15
4.             mmmmm


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



# Q34 What is the result of:      *****      *****      mmmmm
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






# Q41: a)What will be the output of the following code?     mmmmm
s = "abcd"
print(s[0:1:-1])

# Answer: 



# Q41: b)What will be the output of the following code?     mmmmm
s = "abcde"
print(s[4:0:-1])

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






# Q49: Without worrying about missing characters or duplicate characters, what will be the likely range of the first element and last element?          mmmmm
# An approximate range can be a-c or y-z.
lst = [chr(randint(ord('a'), ord('z'))) for i in range(25)]
sorted(lst)
print(lst)
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





# Q: What is the output?      mmmmm      

s = '13579'
total = 0

for i in range(1, len(s)):
    if i % 2 == 0:
        total += int(s[i])

print("Total of even-indexed numbers:", total)

# Answer: 





# Q: What is the ouput of this?

lst_obj = (-1, 11, 0)
lst_obj[0] += 1
obj = range(1, 11, 0)

# Answer: TypeError



#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Q [Improving speed of mental arithmetic]: What is the first and last number printed from each of the following snippets?:

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



# Answer: 0




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



# Answer: 0, 1




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
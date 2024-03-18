# pylint: disable=all
# type: ignore
#region Code without hints

# List of all questions to be revised.  Every question is a flavour of one I got wrong (out of over 600 in total), added here each time.
# One set of '*****' indicates I got the question wrong again a number of days after previously revising it.  Additional stars (or dates), wrong again, and so on.
# All answers are corrected before this document is saved by me.  If any are blank I deleted the answer as extra reminder to re-revise that question.  No answers will be 'left incorrect' before I upload this file to github.



# Q10 Which of the following lines describe a true condition?                               20-2

print('smith' > 'Smith')

print('Smiths' < 'Smith' )

print( 'Smith' > '1000' )

print( '11' < '8' )

print('!' < '5')

# Answer: ALL CORRECT












# Q12 A) What is the expected result of the following code?         mmmmm      mmmmm           25-1            19-2             26-2

s1 = '45.6'
i = int(s1)
s2 = str(i)
f = float(s2)
print(s1 == s2)

# Answer:  NOT A FUCKING TYPE ERROR!  ITS THE VALUE THATS WRONG!  STRING IS NOT AN INVALID DATA TYPE FOR THE INT() FUNCTION!!!!!!!

# Q12 B) What if s1 was a float?

# Answer: False



# Q13 What is the expected value of the result variable after the following code is executed?                   20-2

import math
result = math.e == math.exp(1)

# Answer: Technically false but would be True: rounding error.







# Q16 You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?                 20-2

# Answer: place the main calls/usage in an if condition: 
if not __name__ == '__main__':
    # <some code>

























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
4. What is the small flag ('-u') used for?
'''
# Answer: 
1. pip --version
2. pip install packagename
3. pip install --user packagename  or  pip install -u packagename
4. No such option.  Will cause an error.






# b) What is the output of the following snippet?                                                                           21-1           REDO FOR WINDOWS FOR: platform.machine(), platform.processor(),                      

import platform
print(platform.machine(), platform.processor(), platform.system(), platform.platform(), platform.version())

# Answer:    
"""
x86_64                              or  AMD64
x86_64                              or  Intel64 Family 6 Model 158 Stepping 9, GenuineIntel
Linux                               or  Windows
Linux Kernel Build Info and CPU     or  Windows-10-10.0.19045-SP0
Linux Distribution + version        or  10.0.19045
"""













""" Answers (for referece)
#        x86 x86 linux Linux_Kernel_Build_Info_and_CPU linux_distro
# or     x86 x86 windows 'windows 10 [build_info]' build_info
"""












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
# Answer: 1.57







# Q44 a): Name four list methods that return a value and seven that don't.  Also list the parameters for each.                              

'''
Answer:
l.pop([i])
l.count()
list.index(x[, start[, end]])
l.copy()                                                                              20-2

l.insert(i, x)
l.append(x)
l.extend(iterable)
l.reverse()
l.sort(*, key=None, reverse=False)
remove(x)
clear()

x = value
i = index

'''



# Q45: How many arguments does the string class's 'join' method take?  And what data type does it take?       *****                 20-2

# Answer: 
1, iterable








''' Q48: A) Write three snippets to iterate through the dictionary.  B) Also, if iterating over a dictionary directly without these methods, what is iterated?               20-2
i) its key-value pairs
ii) only its keys
iii) only its values
'''

dic = {1: 'one', 2: 'two', 3: 'three'}

''' Answer:
i) for i in dic.items()
ii) for i in dic.keys()
iii) for i in dic.values()
'''

# Answer (B): Only its keys.  Using `for i in dic.keys()` is the same as just doing `for i in dic`.






# Q49: A) What is the ouput of this?    B) And what if we removed the first two lines?           mmmmm                20-2

lst_obj = (-1, 11, 0)
lst_obj[0] += 1
obj = range(1, 11, 0)

# Answer (A): TypeError
# Answer (B): ValueError









# Q55: What is the output?          nnnnn                       20-2

elements = {}
for character in 'Gandalf':
    if character in 'Saruman':
        elements[ord(character)] = character
else:
    elements[ord('u')] = 'u'

for key in elements.keys():
    print(elements[key], end=' ')

# Answer: a n u











# Q58 c): What are the rules for the 'import' keyword if used without 'from'?                       21-1            20-2

# Answer: What's after 'import' can only be a module or a package.  The full path of whats specified after the 'import' keyword is whats added to the namespace and must be used for accessing.




























""" Q75: List 7 open() modes and their behaviour.


r: reads from beginning; file must exist or raises FileNotFoundError
w: creates or truncates; existing file not required.

r+: reads & update; reads or writes starting at the beginning; file must exist.
w+: write & update: writes or reads from the beginning; existing file not required.

x: creates a file for writing at the beginning; raises FileExistsError if file exists. Safer alternative to 'w'.
a: append opens or creates a file for writing at the end; existing file not required.
a+: opens (or creates) a file for appending at the end; existence not required; writes always move the position (back) to the end.

"""









# Q78: True or false for each of these?                                                                     21-2 (mix up)

print(bool(''), bool([]), bool(0,), bool({}), bool(None), end='')
print('', bool([[]]), bool((0,)))

# Answer: 
"""
F, F, F, F, F, T, T
"""









# b) Which of the following is a true statement? (Select 2 Answers)                         21-2

"""
Unicode is a standard

UTF-8 is an encoding

Unicode is an encoding

UTF-8 is a standard

UTF-8 is the only encoding apart from ASCII
"""

# Answer: Unicode is a standard.  UTF-8 is an encoding.







# Q84: What are each of these constants?                                                   22-1         Got all correct (26-1)          21-2

"""
errno.EACCES → 

# Answer: 

errno.EBADF → 

# Answer: 

errno.EEXIST → 

# Answer: 

errno.EFBIG → ??????????

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











# Q88: What is the expected output of the following code snippet?                       21-2 (also see Q94)

class GalaxyError(Exception):
    pass
 
try:
    raise Exception("X", "Y")
except GalaxyError:
    print("Greetings", end=" ")
finally:
    print("Farewell")

# Answer: Farewell will be executed but the exception will not be caught.








# Q90: 
# a) What is the expected output of the following code snippet?                 8-2             21-2        23-2

creature_stats = {'goblin':1, 'troll':2}
try:
    creature_stats[1]
except IndexError:
    print('Cave', end=' ')
except Exception as exc:
    print(exc.args, end=' ')

# Answer: 

# b) What distinguishes KeyError's error argument handling, specifically when accessing a non-existent key in a dictionary, from that of other Python error types?

# Answer: The bad key is passed to the args tuple instead of a description of the error.                                                                                                                                                                                   The non-existent key itself is passed as an argument, instead of a description of the error.






# Q91: What is the expected output of the following code snippet? What if the variable was mutable?                8-2

string_sequence = "def"
 
for element in string_sequence:
    element = 'y'
 
print(string_sequence)

# Answer: def (also, see extra info below): def;  the loop variable is just assigned the value, typically temporarily as its incremented.  It is not the element it represents or even a reference to it.
# Changing the value of the loop variable does not affect the items in the iterable itself, even for mutables.

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

class Star:
    pass
class Nebula(Star):
    pass
class Galaxy(Nebula):
    pass
class BlackHole(Star):
    pass

# Which of the following are correct declarations of subclasses (r.e., MRO)? (Select 2 Answers)

class CosmicPhenomenon1(Star, Nebula): # a
    pass

class CosmicPhenomenon2(Galaxy, BlackHole): # b
    pass

class CosmicPhenomenon3(Star, BlackHole): # c
    pass

class CosmicPhenomenon4(Nebula, Galaxy): # d
    pass

class CosmicPhenomenon5(BlackHole, Galaxy): # e
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








# Q96: What is the output of the following snippet of code?                 8-2             21-2

class A:
    pass
class B:
    pass
class C(B):
    pass
 
c = C()
print(isinstance(c, (B,A)))

# Answer: True





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


# Answer: c & d



# B) What data type does sorted() always return?  And what can it not sort?


# Answer: sorted() always returns a list (and automatically converts other types to lists).  However, it can't sort between different data types, i.e., between 'str' and 'int'.



# C) What would be the output if the 2 lines in option B were executed?                                      23-2               


# Answer: AttributeError:  'str' object has no attribute 'sort'






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
I feel fine"
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
    return 'Peter''Wellert'

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
__module__      # type(MyClass.__dict__['__module__']) == type('string')            output: True                        same as Class.__module__ in ...ntedProgramming/Introspection/..._miscellaneous_summary.py
__dict__
__doc__
__weakref__

__init__
my_meth
class_var







"""
__module__      __main__                                                                            23-2
__dict__        <attribute '__dict__' of 'MyClass' objects>
__weakref__     <attribute '__weakref__' of 'MyClass' objects>
__doc__         docstring test

__init__        <function MyClass.__init__ at 0x...>
my_meth         <function MyClass.my_meth at 0x...>
class_var       1

Note: The dictionary can be used to access these entities directly, i.e., they're not just strings.  NB: Class.__module__ itself is actually just a string!
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

# ALL CORRECT 23-2 AND ALL CORRECT 24-2








# Q106 (continued): What is the output for each snippet?

print([1, 2] + [3, 4])
# Answer: 

print(('a', 'b') + ('c',))
# Answer: 

lst = ['x']
lst += ['y', 'z']
print(lst)
# Answer: 

print([0] * 4)
# Answer: 

print(('NO',) * 2)
# Answer: 

lst = [9, 8]                                                # 26-2              correct
lst.append([7])
print(lst)
# Answer: 

lst = ['a', 'b']                                            # 26-2              3-3-24          correct__but_practice_required
lst.extend('cd')
print(lst)
# Answer: 

print([1, 2] + 3)
# Answer: 

lst = [5, 6]
lst += (7, 8)
print(lst)
# Answer: 

print([[True]] * 3)
# Answer: 




# Q106 (continued): What is the output for each snippet?

# Challenge 1
lst = [1, 2]
lst *= 2
print(lst)
# Answer:

# Challenge 2
print([1, 2] + [3, 4])
# Answer:

# Challenge 3
lst = ['a', 'b']
lst += ('c', 'd')
print(lst)
# Answer:

# Challenge 4
print(('a', 'b') * 3)
# Answer:

# Challenge 5                                                                 23-2            24-2              correct
print([True] + [False] * 2)
# Answer:

# Challenge 6                                                                 23-2            26-2              correct
lst = [1, 2]
lst.append([3] * 2)
print(lst)
# Answer:

# Challenge 7
lst = ['x', 'y']
lst += 'z'
print(lst)
# Answer:

# Challenge 8
print((1,) + (2,))
# Answer:

# Challenge 9                                                                                   24-2            correct
lst = [1, 2, 3]
lst *= 0
print(lst)
# Answer:

# Challenge 10
print({'a': 1} + {'b': 2})
# Answer:

# Challenge Bonus
x = input()
y = input()
print (x + y)
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

# All correct 23-2; 3-3-24



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

# Answer: Eins Zwei Zwei Zwei









# Q110

# A) What is the expected output of the following lines?

print(type(2E7))
print(5e3)
print(7.3e5)

"""
Answers (A):
float
5000
730000
"""


# B) Write '9 times ten to the power of 4 ' in scientific notation:


# Answer (B): 9e4



# C) Write 8.2e7 in words and as an integer:


# Answer (C): 8.2 times ten to the power of 7       82000000



# D) Write 570e-3 as an integer:


# Answer (D): 0.570


# E) Write an equation to calculate 500e-3

# Answer (E): 500 * (10 ** -3)







# Q111) What is the expected output of the following code?  Remember to check it precisely.                     correct_23-2_but_ensuring_recallable

info_storage = {}
info_storage[2.0] = 3
info_storage['2'] = 4
info_storage[2] = 5
print(info_storage)
 
total = 0
for item in info_storage:
    print(item)
    total += info_storage[item]
 
print(total)

# Answer: 9 (also correct 24-2)







# Q112 - What is the expected output of the following code?

z = [21, 22, 23, 24, 25, 26, 27, 28, 29]
z[::3] = 110, 220, 330, 440
print(z)

# [110, 22, 23, 220, 25, 26, 330, 28, 29]

# [21, 22, 110, 220, 330]

# The code is erroneous.

# [21, 110, 23, 24, 220, 26, 27, 330, 29]

# Answer: ValueError







# Q113) Sort these into errorenous and not errorenous.

print(int('1')) #a
print(int('1.45')) #b
print(int('1+1')) #c
print(int(1.45)) #d
print(int(1.234*3/2)) #e

print(float('10/1')) #f
print(float('10')) #g
print(float(10)) #h
print(float(10/1)) #i

""" Answer: 
ERRORENOUS: b, c, f

GOOD: a, d, e, g, h, i

Takeaway: int can always convert to float, and float can also always be converted to int.  But for strings, values must already be in the correct format. The ONLY exception is 
float('10'), where the decimal suffix is not required.  A string formatted as a float can NOT be used with int().
"""



# Q114) A method able to read data from a file into a bytes object, is named:

"""
readin()

readout()

read()

readinto()
"""

# Answer: read()






# Q115) Is the maximum value of the following code 3 or 4?  Why?

import random
print(int(random.random() * 4))

# Answer: 3, random.random() is end exclusive, i.e., the maximum here would be 3.9999999...









# Q116) Which of the expressions will evaluate to True?                                         CORRECT_BUT_SLOW

class Planet:
    name = "Mercury"
 
    def orbit(self):
        return self.name.lower()
 
class Comet(Planet):
    name = "Halley"
 
class Asteroid(Planet):
    def orbit(self):
        return self.name.upper()
 
class Meteoroid(Asteroid, Comet):
    pass

m = Meteoroid()
c = Comet()

# (Select two answers.)

Planet in Meteoroid.__bases__    #a

m.orbit() == "HALLEY"            #b

isinstance(m, Comet)             #c

m.name == "Mercury"              #d


# Answer: b, c









# Q117 A) Which of the expressions will evaluate to True?

class Alpha:
    value = "Alpha"
 
    def say(self):
        return self.value.lower()
 
class Beta(Alpha):
    value = "Beta"
 
class Gamma(Alpha):
    def say(self):
        return self.value.upper()
 
class Delta(Gamma, Beta):
    pass

d = Delta()
b = Beta()

# (Select two answers.)

Alpha in Delta.__bases__    #a

d.say() == "BETA"           #b

isinstance(d, Beta)         #c

d.value == "Alpha"          #d


# Answer: b c






#117 B) What is the output?

class Base:
    def __init__(self):
        print("Base init")

class A(Base):
    def __init__(self):
        super().__init__()
        print("A init")

class B(Base):
    def __init__(self):
        super().__init__()
        print("B init")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init")

c = C()

# Answer: Remember in diamonds, the branches are merged.  C.__mro__ would output: C, A, B, Base







# Q118: You are writing a Python program that calculates a physical property based on an input value.                           CORRECT_IN_END_BUT_PAINFULLY_SLOW
# The formula to calculate this property is described as 'r' equals 'q' multiplied by negative one, 
# then raised to the second power, where 'q' is the input value and 'r' is the result. 

q = eval(input('Enter a value for q: '))

# Which of the following is a valid expression for the given requirement?

# A:
r = (q-) ** 2

# B:
r = -(q) ** 2

# C:
r = (-q) ** 2

# D:
r = (q) ** -2

# Answer: C: r = (-q) ** 2







# Q119:  Apart from list.count() and list.index(), what is the ONLY other list method that takes a 'value' argument rather than a 'position'?  And why can list.pop() raise an 
# IndexError but list.index() raises a ValueError?

# Answer: list.remove(value)     list.index(value) can raise a ValueError because it takes a value as its argument, not an index/position.  list.pop() however takes an index, so can
# raise an IndexError.                                                                                                                                                            >>>>>>>>>>>>>>>>>pop() raises an INdexError because its argument is a n index (position).  index() raises a ValueError because its argument is a value.







# Q120: Is pip automatically installed with Python?

# Answer: yes





# Q121) Function Parameters: Which of these five snippets will not raise an exception?

#a
def func(x=2, y=3):
    return x * y
 
print(func(x=2, 1))



#b
def func(x=2, y=3):
    return x * y
 
print(func(y=2))


#c
def fun(1):
    return a

print(fun())


#d
def func(x=1, y):
    return x * y
 
print(func(y=2))


#e
def func(x, y):
    return x * y
 
print(func(x = 2, y))


#f
def fun(x, y, z):
    return y + z
    
x = 1
print(fun(x, z='a', y='b'))


#g
x = 1
def fun(x, y=1, z=1):
    return x * y * z

print(fun(x, z=1, y=1))


# Answers:  b, f, g.  keyword args must be placed last (after positional), but their order is not important.











# Q123) Why can there never only be an odd number of backslash (escape characters) in a string?                         23-2

# Answer:  The odd one out will escape the closing quote, causing a syntax error at the string.







# Q124) What is the expected output of the following code snippet?                                                      23-2
def generate_greeting():
    base_name = 'Orlando'
    append_suffix = lambda x: base_name + ' ' + x
    return append_suffix
 
heroes = generate_greeting()
 
print(heroes('Frodo'))


# Answer: Orlando Frodo













# Q125) Look at the 3 snippets below and answer these three questions:

"""
Override Check: "Is self.args explicitly set in the custom exception?"
Super Init Args: "Are arguments passed to super().__init__ without explicitly setting self.args?"
Bypass Init Effect: "What does overwriting (and passing) __init__ do to self.args?"
"""

# Answer: ✓
# Answer: ✓
# Answer: ✓

"""
  Priority __str__ / e.args:

#1
Custom self.args Override: If self.args is explicitly set in a custom exception's constructor, this value takes precedence for the exception's string representation.

#2
Inherited Behavior with super().__init__: When super().__init__ is called with arguments, those arguments populate self.args in the inherited exception, influencing its 
string representation accordingly.

#3
Default self.args Preservation: Overriding __init__ without calling super() and without explicitly setting self.args still results in self.args being populated with the 
arguments passed during exception raising, likely due to Python's underlying exception handling mechanisms.

"""


#1
class CustomException(Exception):
    
    def __init__(self, msg):
        super().__init__(msg, msg, msg, msg, msg, msg, msg, msg)
        self.args = ('test',)                                                                                                                                                       # printed

try:
    raise CustomException('this is a message')                                                                                                                                      # not printed
except CustomException as e:
    print(e) # 


#2
class CustomException(Exception):
    
    def __init__(self, msg):
        super().__init__(msg, msg, msg, msg, msg, msg, msg, msg) # arbitrary

try:
    raise CustomException('this is a message')
except CustomException as e:
    print(e)                                                                                                                                                                         # printed 8 times




#3
class CustomException(Exception):
    
    def __init__(self, msg):
        pass

try:
    raise CustomException('this is a message')
except CustomException as e:
    print(e.args)                                                                                                                                                                    # still prints






# Q126 A): What is the expected output of the following code snippet?

# Snippet 1:
x = 6
y = 4
result1 = x ** 2 - y ** 2
print(result1)
result1 += x // 2 - y
print(result1)

# Answer: 19


# Snippet 2:                    3-3-24
a = 7
b = 3
output2 = a % b + 4
print(output2) 
output2 *= a // b ** 2
print(output2)

# Answer: 0


# Snippet 3:                    3-3-24          4-3-24
m = 9
n = 5
total3 = m - 2 * n
print(total3)
total3 //= 3 + n % 2
print(total3)

# Answer: -1


# Snippet 4:
p = 3
q = 2
calculation4 = p + 3 ** q
print(calculation4)
calculation4 -= (p // q) + 4
print(calculation4)

# Answer: 7




# Q127) Where in the operator precedence order are all augmented operators?  How does this work?

# Answer: The entire right side is calculated first following normal BODMAS (brackets, orders/powers, division, multiplication, addition, subtraction) rules.
# Only after, is the augmented operator then applied.







# Q128) Write code to print all prime numbers between 2 and 100.

num = 2

while num <= 100:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num)
    num += 1






# Q129) Although custom exceptions may technically inherit from `BaseException`, the Python documentation recommends using `Exception`.
# If neither are used, what error handling mechanism would raise a TypeError?


# Answer: Attempting to catching a class that does not inherit from BaseException.







# Q130) What is the expected output of the following code?

class A:
 
    def __init__(self, x=1):
        self.x = x
 
    def set(self, x):
        self.x = x + 3
        return x
 
 
a = A()
print(a.set(a.x + 1))


# Answer: 2






# Q131) Except itself, is 'None' equal to anything at all? Even 'false', or '0'??

# Answer: No!!









# Q132 a) Function & Scope Rules.  What is the output of the below snippets?            correct_but_more_practice_needed__3-3-24


"""
Remember, whether simply assigning a new variable to an existing variable (outside the context of functions) or passing arguments in functions, the behaviour is consistent:

'b' points to the same object in memory as 'a'.  This is NOT a direct reference to 'a', which in turn points to the same object in memory, no!.  We mean 'a' and 'b' both seperately point to the SAME memory address, so for example:

a = 1
b = a

VARIABLE    MEMORY ADDRESS
a           0x1345563412
b           0x1345563412



a = [0, 1]
b = a

VARIABLE    MEMORY ADDRESS
a           0x1345563412 (Note: Beyond learning scope, but for collections like lists, 'a' and 'b' refers to a structure that itself points to the elements' memory locations).
b           0x1345563412



The nuance comes afterwards, depending on mutability:

# IMMUTABLES
a = 1
b = a

a = 2 # points 'a' to a new memory object.
print(b) # Output: 1.   'b' still points to the same object in memory. 


# MUTABLES
Further nuance: Behaviour is determined by whether we are reassigning the entire variable or modifying its contents.

# Reassigning the entire variable (same behaviour as immutables):
a = [0]
b = a

a = [9]
print(b) # Output: [0]


# Modifying a variable's contents:
a = [0]
b = a

a[0] = [9]
print(b) # Output: [9]

"""





# Snippet 1:
candy_bag = [0, 1]

def refill_bag():
    candy_bag[1] = 9

refill_bag()
print(candy_bag)


# Answer: ✓ [0, 9]
# Explanation: Variables outside a function have scope inside them.  For immutables, this is limited to read-only.




# Snippet 2:
def function():
    global variable
    variable += 1


variable = 1
function()
print(variable)



# Answer: 2
# Explanation: The global keyword grants global scope to a variable used as its argument.  Removing the 'global' line would cause UnboundLocalError because Python would be trying to re-assign an outside variable that it only sees as local.




# Snippet 3:
meal_plan = [0, 1]

def extend_plan():
    global meal_plan    
    meal_plan += [4, 5]

extend_plan()
print(meal_plan)


# Answer: ✓ [0, 1, 4, 5]
# Explanation: The global keyword grants global scope to a variable used as its argument.  Removing the 'global' line causes UnboundLocalError for the same reason as above, due to the augmented operator's (+=) attempted reassignment of a variable that doesn't exist in the local namespace.






# Snippet 4:
def function(parameter):
    parameter[0] = 1


the_list = [0, 1]
function(the_list)
print(the_list)


# Answer: [1, 1]
# Explanation: 'parameter' is a reference to the same object in memory as the original (passed) variable. This comes under the rules for modifying a mutable's contents via a reference to it in another variable:
# This shared reference allows changes through parameter to impact 'the_list', illustrating mutable objects' behaviour where operations on one reference affect the original due to a common memory structure for the elements.




# Snippet 5:
def function(parameter):
    parameter = [2]


the_list = [1]
function(the_list)
print(the_list)


# Answer: 1
# Explanation: Although we are dealing with a mutable object (a list), we are reassigning the entire variable, not merely modifying its contents.  Assigning a non-global variable inside a function only creates a local variable, therefore has nothing to do with the original.







# Snippet 6:
hero = 'Fox'

def rename_hero(new_name):
    global hero
    hero = new_name
    return hero

rename_hero('Bear')
print(hero)


# Answer: Bear
# Explanation: Using the global keyword makes the change apply globally.





# Snippet 7:
m = [0,1]

def fun():
    m += [2, 3]

fun()
print(m)


# Answer: UnboundLocalError
# Explanation: The error occurs because the += operation implicitly requires 'm' to be accessed as a local variable within the function, yet 'm' is not defined locally nor explicitly marked as global, leading to a conflict when attempting access before assignment.



# Snippet 8:

def process(data):
    data[1] = 2
    return data[-2]


measurements = [0 for i in range(3)]
process(measurements)
print(measurements[-2])


# Answer: 2





# Q132 b) Which of the following sentences is true and why?  What if it was a partial slice?                                23-2          correct_but_unsure: 3-3-24

wizard_name = 'Merlin'
spell_name = wizard_name[:]

# A) spell_name is longer than wizard_name

# B) wizard_name and spell_name are different (but equal) strings.

# C) wizard_name is longer than spell_name

# D) wizard_name and spell_name are different names of the same string.

# Answers: Slicing only copies to a new object & memory ID when its a mutable.  For immutables, slicing is just the same as assigning another variable to the same object 
# due to interning.  'Copying' with [:] only works with mutable data types like a list. A string is an immutable data type. Whether you slice the whole thing or just assign
# it, you always end up with a reference to the same object.

# Fully slicing immutables just creates another variable referencing the same object in memory (interning). Partial slicing or slicing mutables copies it, creating a new object.







# # Q132) Function & Scope Rules.  What is the output of these two snippets?  (You may read the comments).


# m = [0,1]

# def fun():

#     m[0] = 9 # valid

# fun()
# print(m)


# # Answer: [9,1]



# m = [0,1]

# def fun():
#     global m    # This will NOT work without the global keyword:
#     m += [2, 3] # Inside a function, m = m + [2, 3] reassigns m, requiring global to use the m from the global namespace; without it, Python sees 'm' as an undefined local variable.

# fun()
# print(m)


# # Answer: [0, 1, 2, 3]



# y = 'R2D2'
# def my_func(x):
#     global y
#     y = x
#     return y
 
# x = 'Yoda'
# my_func('C3PO')
# print(y)


# # Answer: 






# Q133) Tuples only have two methods, what are they?

# Answer: count and index







# Q134) Operator priority
**
unary - +, bitwise not (~)
* / % //
+ -
bitwise << >>
bitwise AND &
bitwise XOR ^
bitwise OR |
comparison operators (< > == != <= >=), membership (in, not in), identity (is, is not)
logical not
logical and
logical or

# Q135: What is the expected output of the following code snippet?

movie_titles1 = ['Inception', 'Interstellar', 'Dunkirk']
movie_titles2 = movie_titles1
movie_titles3 = movie_titles1[:]

movie_titles2[0] = 'Tenet'
movie_titles3[1] = 'Memento'

score = 0

for film in (movie_titles1, movie_titles2, movie_titles3):
    if film[0] == 'Tenet':
        score += 1
    if film[1] == 'Memento':
        score += 2

print(score)


# Answer: 4






# Q136) Why is XOR referred to as "exclusive OR"?


# Answer: XOR is only 'true' if its bits are different.







# Q137) Are dictionary methods' .keys(), .values() and .items() subscriptable?  Why not?  What does .items() return?


# Answer: NONE of these are subscriptable.  They all return a view, which is more memory efficient.   items() view displays like a list of tuples.








# Q138) How many stars are printed?


planet_count = 9
while planet_count > 0:
    planet_count -= 3
    print('*')
    if planet_count == 3:
        break
    else:
        continue
    print('*')
else:
    print('*')


# Answer: 2








# Q139) What data types can be used in dictionary keys?             3-3-24


# Answer: hashable types only, i.e., immutables.  Tuples can be used as long as they only contain hashables.






"""
Hashable objects include IMMUTABLE types like strings, numbers (integers and floats), and tuples (only if the tuple contains hashable types itself).
"""








# Q140) What is the expected output of the following code snippet?

ancient_relics = {(4, 5): 1, (5, 6): 2}
print(ancient_relics[4, 5])


# Answer: 1








# Qn) What is the output?

class Taxi:
    def print_number(self):
        print(self.get_number())

    def get_number(self):
        return "unknown"

class Yellow(Taxi):
    def get_number(self):
        return "261"

cab = Yellow()
cab.print_number()

# Answer: 261






# Qn) Given the code below, which of the following expressions will evaluate to True?
# (Select two answers.)

class Composer:
    def create(self):
        return "composer"


class Mozart(Composer):
    def create(self):
        return "mozart"


class Beethoven(Composer):
    def create(self):
        return "beethoven"


class Bach(Mozart, Beethoven):
    pass


b = Bach()
m = Mozart()


print(b.create() == "beethoven") 

print(Beethoven in Bach.__bases__) #

print(isinstance(b, Composer)) #

print(m is b) 

# Answer: 2nd and 3rd





# Qn) What is the output?

print(' ' * 0 < 1 * ' ')

print(str(None))

"""Answer: 
True
None
"""







# Qn) What is the expected output of the following code?

consts = [3.141592, 2.718282]
try:
    print(consts.index(314e-2))
except Exception as exception:
    print(exception.args)
else:
    print("success")


-1

('success')

False

('3.14 is not in list',)


# Answer: Last one. 

# '.args' only stores the args passed to the exception's constructor (although this doesn't always have to coded explicitly), which most often includes only the description of the error (or other relevant data provided at the time of raising the exception), and not the class name of the exception itself.




# Qn) What is the expected output of the following code?  And then also, what would happen if the exception was not caught?

class Failure(IndexError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "problem"


try:
    print("launch")
    raise Failure("ignition")
except RuntimeError as error:
    print(error)
except IndexError as error:
    print("ignore")
else:   
    print("landing")



problem

ignore

ignition

launch


# Answer: launch, ignore







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

When dealing with 2**0, 2**1, 2**3, 2**4, 2**5, a quick calculation is: double the exponent, starting from 2**0:1

when dealing with 0**2, 1**2, 2**2, 3**2, 4**2, 5**2, just square the left operand!





















#endregion
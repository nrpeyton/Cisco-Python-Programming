'''
map(function, iterable)

The map() function executes a specified function (1st argument) on elements from given iterable(s) (subsequent arguments), aligning each iterable's elements 
to the function's parameters by position, and returns an iterator of the results.
'''

def power_of_two(x):
    return 2 ** x

def square(x):
    return x * x

list_1 = [x for x in range(5)]
list_2 = list(map(power_of_two, list_1))
print(list_2) # Outputs: [1, 2, 4, 8, 16]

for x in map(square, list_2):
    print(x, end=' ') # Outputs: 1 4 16 64 256 




# LAMBDA VERSION
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()






'''
If more arguments (iterables) are specified, they are evaluated in parallel.
'''

def add(x, y):
    return x + y

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(add, numbers1, numbers2)

# Convert result to a list to see the output
print(list(result))  # Output: [5, 7, 9]







'''
filtered(function, iterable)

Returns an iterator (e.g., a list), but only the items that evaluated to true are kept, with the false being filtered out.
'''

from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
